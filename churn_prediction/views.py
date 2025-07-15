from django.shortcuts import render, redirect
from django.http import JsonResponse
import pandas as pd
import numpy as np
import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
import os
from .forms import CustomerForm
import json

# Try to load the model, continue even if fails
try:
    # Load the trained model
    model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'model.pkl')
    model = joblib.load(model_path)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def index(request):
    """Home page view"""
    return render(request, 'index.html')

def dashboard(request):
    """Dashboard view with visualizations"""
    try:
        # Load data for visualizations
        df_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'WA_Fn-UseC_-Telco-Customer-Churn.csv')
        df = pd.read_csv(df_path)
        
        # Check column names - handle different naming conventions
        if 'TotalCharges' in df.columns:
            total_charges_col = 'TotalCharges'
        elif 'Total Charges' in df.columns:
            total_charges_col = 'Total Charges'
        elif 'Total_Charges' in df.columns:
            total_charges_col = 'Total_Charges'
        else:
            # If column not found, set a default value
            df['TotalCharges'] = df['MonthlyCharges'] * df['tenure']
            total_charges_col = 'TotalCharges'
        
        # Convert to numeric
        df[total_charges_col] = pd.to_numeric(df[total_charges_col], errors='coerce')
        df = df.dropna(subset=[total_charges_col])
        
        # Generate charts
        charts = {}
        
        # Chart 1: Contract vs Churn
        contract_churn = df.groupby(['Contract', 'Churn']).size().unstack()
        plt.figure(figsize=(10, 6))
        contract_churn.plot(kind='bar', stacked=True)
        plt.title('Churn Count by Contract Type')
        plt.xlabel('Contract Type')
        plt.ylabel('Number of Customers')
        plt.xticks(rotation=0)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        charts['contract_churn'] = get_graph()
        
        # Chart 2: Total Charges Distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(df[total_charges_col], bins=30, kde=True)
        plt.title('Distribution of Total Charges')
        plt.xlabel('Total Charges')
        plt.ylabel('Frequency')
        plt.tight_layout()
        charts['total_charges'] = get_graph()
        
        # Basic stats
        total_customers = len(df)
        churn_rate = df[df['Churn'] == 'Yes'].shape[0] / total_customers * 100
        avg_tenure = df['tenure'].mean()
        avg_monthly_charges = df['MonthlyCharges'].mean()
        
        context = {
            'charts': charts,
            'total_customers': total_customers,
            'churn_rate': round(churn_rate, 2),
            'avg_tenure': round(avg_tenure, 2),
            'avg_monthly_charges': round(avg_monthly_charges, 2)
        }
        
        return render(request, 'dashboard.html', context)
    except Exception as e:
        return render(request, 'dashboard.html', {'error': str(e)})

def prediction_form(request):
    """Display form to input customer data"""
    form = CustomerForm()
    return render(request, 'prediction.html', {'form': form})

def predict_churn(request):
    """Process form data and make prediction"""
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Check if model is loaded
            if model is None:
                return render(request, 'results.html', {
                    'error': 'Model not loaded. Please ensure the model file exists at models/model.pkl'
                })
            
            # Get form data - use the exact column names expected by the model
            customer_data = {
                'Gender': [form.cleaned_data['gender']],
                'Senior_Citizen': [int(form.cleaned_data['senior_citizen'])],
                'Partner': [form.cleaned_data['partner']],
                'Dependents': [form.cleaned_data['dependents']],
                'Tenure': [form.cleaned_data['tenure']],
                'Phone_Service': [form.cleaned_data['phone_service']],
                'Multiple_Lines': [form.cleaned_data['multiple_lines']],
                'Internet_Service': [form.cleaned_data['internet_service']],
                'Online_Security': [form.cleaned_data['online_security']],
                'Online_Backup': [form.cleaned_data['online_backup']],
                'Device_Protection': [form.cleaned_data['device_protection']],
                'Tech_Support': [form.cleaned_data['tech_support']],
                'Streaming_TV': [form.cleaned_data['streaming_tv']],
                'Streaming_Movies': [form.cleaned_data['streaming_movies']],
                'Contract': [form.cleaned_data['contract']],
                'Paperless_Billing': [form.cleaned_data['paperless_billing']],
                'Payment_Method': [form.cleaned_data['payment_method']],
                'Monthly_Charges': [form.cleaned_data['monthly_charges']],
                'Total_Charges': [form.cleaned_data['total_charges']]
            }
            
            try:
                # Create DataFrame from the form data
                input_df = pd.DataFrame(customer_data)
                
                # Make prediction
                prediction = model.predict(input_df)
                probability = model.predict_proba(input_df)[0][1]
                
                result = 'Yes' if prediction[0] == 1 else 'No'
                
                context = {
                    'prediction': result,
                    'probability': round(probability * 100, 2),
                    'customer_data': form.cleaned_data,
                    'will_churn': prediction[0] == 1
                }
                
                return render(request, 'results.html', context)
            except Exception as e:
                return render(request, 'results.html', {'error': f"Prediction error: {str(e)}"})
    
    # If not POST or form invalid, redirect to form
    return redirect('prediction_form')

# Utility function to convert matplotlib plots to base64 for template display
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()
    plt.close()
    return graph