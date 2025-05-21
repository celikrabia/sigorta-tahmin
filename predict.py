import joblib
import numpy as np
import pandas as pd

def load_model(filepath):
    """
    Load a trained model from disk
    
    Args:
        filepath (str): Path to the saved model
        
    Returns:
        model: Loaded model
    """
    return joblib.load(filepath)

def predict_charges(model, features):
    """
    Make predictions using the trained model
    
    Args:
        model: Trained model
        features (pd.DataFrame): Features for prediction
        
    Returns:
        np.array: Predicted insurance charges
    """
    return model.predict(features)

def format_prediction(prediction):
    """
    Format prediction output
    
    Args:
        prediction (float): Raw prediction value
        
    Returns:
        str: Formatted prediction string
    """
    return f"Predicted insurance charges: ${prediction:.2f}" 