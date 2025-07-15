# Telecom Customer Churn Prediction Platform

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0%2B-green)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap%205-purple)

A visually appealing, interactive web application built with Django that predicts customer churn in the telecom industry using machine learning.

## ✨ Features

- **Customer Churn Prediction**: Predict whether customers are likely to churn based on various factors
- **Interactive Dashboard**: Visualize churn analytics with dynamic charts and key metrics
- **User-Friendly Interface**: Beautiful purple-themed UI with intuitive navigation
- **Responsive Design**: Works seamlessly across desktop and mobile devices
- **Data Visualization**: Interactive charts to understand churn patterns and distribution
- **Real-time Analysis**: Input customer data and get instant churn predictions

## 🛠️ Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn, Joblib
- **Visualization**: Matplotlib, Seaborn

## 📋 Prerequisites

- Python 3.9+
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation



1. **Create and activate virtual environment (recommended)**

```bash
# Windows
python -m venv venv
venv\Scripts\activate


2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up the dataset and model**

- Place the Telco Customer Churn dataset (`WA_Fn-UseC_-Telco-Customer-Churn.csv`) in the `churn_prediction_project/data` directory
- Either train a model using the provided Jupyter notebook or place a pre-trained model in `churn_prediction_project/models/model.pkl`

4. **Run migrations**

```bash
cd churn_prediction_project
python manage.py migrate
```

5. **Run the server**

```bash
python manage.py runserver
```

6. **Access the application**

Open your browser and navigate to: `http://127.0.0.1:8000/`

## 📊 Usage

1. **Home Page**: Overview of the churn prediction platform
2. **Dashboard**: View churn analytics and visualizations
3. **Prediction Form**: Enter customer information to predict churn:
   - Fill in demographic details (gender, senior citizen status, etc.)
   - Provide account information (tenure, contract type, etc.)
   - Input service details (phone service, internet service, etc.)
   - Add billing information (payment method, charges, etc.)
4. **Results Page**: View the prediction result with probability and customer profile summary

## 📁 Project Structure

```
churn_prediction_project/
├── churn_prediction/             # Main Django app
│   ├── templates/                # HTML templates
│   │   ├── base.html            # Base template with common elements
│   │   ├── index.html           # Home page
│   │   ├── dashboard.html       # Analytics dashboard
│   │   ├── prediction.html      # Prediction form
│   │   └── results.html         # Prediction results
│   ├── forms.py                 # Form definitions
│   ├── views.py                 # View functions
│   └── urls.py                  # URL routing
├── data/                        # Data directory
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset
├── models/                      # Model directory
│   └── model.pkl                # Trained ML model
├── manage.py                    # Django management script
└── requirements.txt             # Project dependencies
```

## 🔧 Customization

- **Model**: Replace the model.pkl file with your own trained model
- **Dataset**: Use your own customer dataset (ensure column names match)
- **UI**: Modify the templates and CSS to change the appearance
- **Features**: Extend the project by adding more visualizations or analysis tools

## 📈 Model Training

The machine learning model was trained using:
- Random Forest Classifier
- Features include customer demographics, services subscribed, and billing information
- Target variable is customer churn (Yes/No)

For retraining the model:
1. Use the provided Jupyter notebook or create your own training script
2. Save the model using joblib to the models directory
3. Make sure feature names match those expected by the prediction form




Developed with ❤️ by [Chitwan Rana]
