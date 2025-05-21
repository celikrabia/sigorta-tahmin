import streamlit as st
import pandas as pd
import numpy as np
from utils import preprocess_data
from predict import load_model, predict_charges, format_prediction

def evaluate_insurance_cost(cost):
    """Evaluate the insurance cost and provide feedback"""
    if cost < 10000:
        return {
            "level": "Çok Uygun",
            "color": "green",
            "description": "Bu sigorta maliyeti piyasa ortalamasının oldukça altında. Çok avantajlı bir teklif.",
            "icon": "✅"
        }
    elif cost < 20000:
        return {
            "level": "Uygun",
            "color": "lightgreen",
            "description": "Bu sigorta maliyeti piyasa ortalamasının altında. İyi bir teklif.",
            "icon": "👍"
        }
    elif cost < 30000:
        return {
            "level": "Orta",
            "color": "orange",
            "description": "Bu sigorta maliyeti piyasa ortalamasına yakın. Normal bir teklif.",
            "icon": "➖"
        }
    elif cost < 40000:
        return {
            "level": "Yüksek",
            "color": "red",
            "description": "Bu sigorta maliyeti piyasa ortalamasının üzerinde. Dikkatli değerlendirilmeli.",
            "icon": "⚠️"
        }
    else:
        return {
            "level": "Çok Yüksek",
            "color": "darkred",
            "description": "Bu sigorta maliyeti piyasa ortalamasının çok üzerinde. Alternatif teklifler değerlendirilmeli.",
            "icon": "❌"
        }

# Set page config
st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="🏥",
    layout="wide"
)

# Title
st.title("Insurance Cost Predictor")
st.write("Predict insurance charges based on customer information")

# Load model
@st.cache_resource
def load_cached_model():
    return load_model("model.joblib")

try:
    model = load_cached_model()
except:
    st.error("Model file not found. Please train the model first.")
    st.stop()

# Input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        sex = st.selectbox("Sex", ["female", "male"])
        bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
        
    with col2:
        children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
        smoker = st.selectbox("Smoker", ["no", "yes"])
        region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])
    
    submitted = st.form_submit_button("Predict Insurance Cost")

if submitted:
    # Create input dataframe
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })
    
    # Preprocess input data
    processed_data = preprocess_data(input_data)
    
    # Make prediction
    prediction = predict_charges(model, processed_data)[0]
    
    # Format and evaluate prediction
    formatted_prediction = format_prediction(prediction)
    evaluation = evaluate_insurance_cost(prediction)
    
    # Display result with evaluation
    st.markdown(f"""
    <div style='text-align: center; padding: 20px; border-radius: 10px; background-color: {evaluation['color']}; color: white;'>
        <h2>Predicted Insurance Cost: {formatted_prediction}</h2>
        <h3>{evaluation['icon']} Değerlendirme: {evaluation['level']}</h3>
        <p style='font-size: 16px;'>{evaluation['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Show feature importance
    st.subheader("Feature Importance")
    feature_importance = pd.DataFrame({
        'Feature': processed_data.columns,
        'Importance': np.abs(model.coef_)
    })
    st.bar_chart(feature_importance.set_index('Feature')) 