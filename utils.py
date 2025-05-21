import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """
    Load insurance data from CSV file
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded insurance data
    """
    return pd.read_csv(file_path)

def preprocess_data(data, keep_charges=False):
    """
    Preprocess the insurance data
    
    Args:
        data (pd.DataFrame): Raw insurance data
        keep_charges (bool): Whether to keep the charges column
        
    Returns:
        pd.DataFrame: Preprocessed data
    """
    # Create a copy of the data
    df = data.copy()
    
    # Convert categorical variables to numeric
    df['sex'] = df['sex'].map({'female': 0, 'male': 1})
    df['smoker'] = df['smoker'].map({'no': 0, 'yes': 1})
    
    # One-hot encode region
    region_dummies = pd.get_dummies(df['region'], prefix='region')
    
    # Drop original region column
    df = df.drop('region', axis=1)
    
    # Add dummy variables
    df = pd.concat([df, region_dummies], axis=1)
    
    # Ensure all expected columns exist
    for col in ['region_northeast', 'region_northwest', 'region_southeast', 'region_southwest']:
        if col not in df.columns:
            df[col] = 0
    
    # Reorder columns to match the expected order
    feature_cols = ['age', 'sex', 'bmi', 'children', 'smoker',
                    'region_northeast', 'region_northwest', 'region_southeast', 'region_southwest']

    if keep_charges and 'charges' in data.columns:
        feature_cols = feature_cols + ['charges']

    df = df[feature_cols]
    return df

def split_features_target(data):
    """
    Split data into features and target
    
    Args:
        data (pd.DataFrame): Preprocessed data
        
    Returns:
        tuple: (X, y) where X is features and y is target
    """
    X = data.drop('charges', axis=1)
    y = data['charges']
    return X, y

def prepare_input_data(age, sex, bmi, children, smoker, region):
    """
    Prepare input data for prediction
    
    Args:
        age (int): Age of the person
        sex (str): Sex of the person
        bmi (float): Body Mass Index of the person
        children (int): Number of children the person has
        smoker (str): Whether the person is a smoker
        region (str): Region of the person
        
    Returns:
        pd.DataFrame: Preprocessed input data
    """
    # Create a DataFrame with the input data
    data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })
    
    # Preprocess the data
    processed_data = preprocess_data(data)
    
    return processed_data 