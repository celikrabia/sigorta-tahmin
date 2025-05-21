from utils import load_data, preprocess_data, split_features_target
from train_model import train_model, evaluate_model, save_model

def main():
    # Load data
    data = load_data("insurance.csv")
    
    # Preprocess data (charges sütununu koru)
    processed_data = preprocess_data(data, keep_charges=True)
    
    # Split features and target
    X, y = split_features_target(processed_data)
    
    # Train model
    model, X_test, y_test = train_model(X, y)
    
    # Evaluate model
    metrics = evaluate_model(model, X_test, y_test)
    print("\nModel Performance Metrics:")
    print(f"Mean Squared Error: {metrics['mse']:.2f}")
    print(f"Root Mean Squared Error: {metrics['rmse']:.2f}")
    print(f"R-squared Score: {metrics['r2']:.2f}")
    
    # Save model
    save_model(model, "model.joblib")
    print("\nModel saved as 'model.joblib'")

if __name__ == "__main__":
    main() 