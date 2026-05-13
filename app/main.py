import streamlit as st
from config import *
from prediction import predict_yield

# PAGE CONFIG

st.set_page_config(
    page_title="AgriPredict AI",
    page_icon=" ",
    layout="wide"
)

# CSS

st.markdown("""
<style>

.stApp{
    background-color:#081c15;
}

header{
    visibility:hidden;
}

.block-container{
    padding-top:1rem;
    padding-left:3rem;
    padding-right:3rem;
}

.hero-container{
    text-align:center;
    margin-top:20px;
    margin-bottom:40px;
}

.hero-title{
    font-size:72px;
    font-weight:800;
    color:white;
    margin-bottom:10px;
}

.hero-green{
    color:#95d840;
}

.metric-card{
    background:#10261d;
    padding:20px;
    border-radius:18px;
    border:1px solid rgba(255,255,255,0.05);
    height:180px;

    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;

    text-align:center;
}

.metric-title{
    font-size:26px;
    font-weight:600;
    color:white;
    margin-bottom:12px;
}

.metric-value{
    font-size:36px;
    font-weight:800;
    color:white;
}

.section-title{
    font-size:38px;
    font-weight:700;
    color:white;
    margin-top:35px;
}

.stButton>button{
    background:#95d840;
    color:#081c15;
    border:none;
    border-radius:14px;
    padding:14px 28px;
    font-size:18px;
    font-weight:bold;
}

.prediction-card{
    background:#10261d;
    padding:35px;
    border-radius:20px;
    text-align:center;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# HERO SECTION

st.markdown(
"""
<div class="hero-container">

<h1 class="hero-title">
 AgriPredict <span class="hero-green">AI</span>
</h1>

</div>
""",
unsafe_allow_html=True
)

# KPI CARDS

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">

    <div class="metric-title">
    Prediction Engine
    </div>

    <div class="metric-value">
    Random Forest
    </div>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">

    <div class="metric-title">
    Model Performance
    </div>

    <div class="metric-value">
    88.5%
    </div>

    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">

    <div class="metric-title">
    Training Dataset
    </div>

    <div class="metric-value">
    600 Rows
    </div>

    </div>
    """, unsafe_allow_html=True)

# INPUT SECTION

st.markdown("""
<h2 class="section-title">
Agricultural Input Parameters
</h2>
""", unsafe_allow_html=True)

left, right = st.columns(2)

with left:

    state = st.selectbox(
        "Select State",
        STATES
    )

    crop = st.selectbox(
        "Select Crop",
        CROPS
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        value=700.0
    )

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        value=30.0
    )

with right:

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        value=60.0
    )

    soil = st.selectbox(
        "Soil Type",
        SOIL_TYPES
    )

    fertilizer = st.selectbox(
        "Fertilizer Type",
        FERTILIZERS
    )

st.markdown("<br>", unsafe_allow_html=True)

# PREDICTION

if st.button("Predict Crop Yield"):

    prediction = predict_yield(
        state,
        crop,
        rainfall,
        temperature,
        humidity,
        soil,
        fertilizer
    )

    st.markdown(
    f"""
    <div class="prediction-card">

    <h2>Predicted Crop Yield</h2>

    <h1 style="font-size:60px;color:#95d840;">
    {prediction}
    </h1>

    <h3>Quintals Per Hectare</h3>

    </div>
    """,
    unsafe_allow_html=True
    )

# FOOTER

st.markdown("""
<hr>

<center>

<h4 style="color:white;">
Built with Streamlit, Python & Machine Learning
</h4>

<p style="color:#b7c9b9;">
AgriPredict AI • Smart Agriculture Analytics Platform
</p>

</center>
""", unsafe_allow_html=True)
