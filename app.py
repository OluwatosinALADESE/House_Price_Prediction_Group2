import streamlit as st
import joblib
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Group 2 House Pricing Project",
    page_icon="🌿",
    layout="wide"
)


# Load the Model
model = joblib.load('house_model.pkl')

# Custom CSS for our Aesthetic
st.markdown("""
    <style>
    /* Main Title Styling - Elegant Serif */
    .main-header {
        font-size: 100px;
        font-weight: 400;
        color: #4A443F;
        text-align: center;
        font-family: 'Playfair Display', 'Garamond', serif;
        margin-top: 20px;
    }
    
    /* Subtitle Styling */
    .sub-text {
        text-align: center;
        color: #8C857B;
        font-size: 25px;
        letter-spacing: 2px;
        font-family: 'Lato', sans-serif;
        text-transform: uppercase;
        margin-bottom: 50px;
    }

    
    .result-card {
        background-color: #EFE8DE; 
        padding: 40px; 
        border-radius: 150px 150px 20px 20px; /* This creates the Arch */
        text-align: center; 
        margin-top: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    /* Input Labels */
    .stSlider label, .stNumberInput label {
        color: #6B635B !important;
        font-family: 'Garamond', serif;
        font-size: 18px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# our Sidebar: Team Members 
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #4A443F; font-family: serif;'>Our Team</h2>", unsafe_allow_html=True)
    st.write("---")
    
    team_members = [
        "Oluwatosin Alades Esther 23/0249",
        "Alafin Joseph Afolabi 23/0125",
        "Adebisi Oluwanisola Dorcas 23/0157",
        "Adara Gladness Ademide 23/0014",
        "Amanambu Emmanuel Chibueze 23/0285",
        "Ademuyiwa Boluwatife David 23/0215",
        "⁠AJIBOLA Ibukunoluwa MARY 23/0204", 
        "Anyiam Tochukwu Kelvin 23/0255",
        "Adewale Emmanuel 23/0199",
        "Adebisi Treasure Oluwatomi 23/0120",
        "Adeyemi Kelvin Oluwatobi 23/0198"
    ]
    
    for member in team_members:
        st.markdown(f"<div style='margin-bottom: 10px; color: #6B635B;'>• {member}</div>", unsafe_allow_html=True)
        
    st.write("---")

# Main Page Content
st.markdown('<p class="sub-text">This Is A Data Powered Evaluation</p>', unsafe_allow_html=True)
st.markdown('<p class="main-header">Modern Living Spaces</p>', unsafe_allow_html=True)

st.write("---")

# Layout: 3 Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🌿 Property Age")
    age = st.slider("Years since construction", 0, 50, 10)

with col2:
    st.markdown("### 🛋️ Interior")
    rooms = st.number_input("Number of Rooms", min_value=1, max_value=20, value=6)

with col3:
    st.markdown("### 🏙️ Neighborhood")
    population = st.number_input("Area Population", min_value=0, value=30000)

st.write(" ")
st.write(" ")

# Center the Predict Button and Result
c1, c2, c3 = st.columns([1, 2, 1])

with c2:
    if st.button("Calculate Valuation", use_container_width=True):
        features = np.array([[age, rooms, population]])
        prediction = model.predict(features)
        
        #our Arched Result Card
        st.markdown(f"""
            <div class="result-card">
                <p style='color: #8C857B; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px;'>Estimated Market Value</p>
                <h1 style='color: #4A443F; font-size: 55px; font-family: serif; margin: 0;'>${prediction[0]:,.2f}</h1>
            </div>
        """, unsafe_allow_html=True)