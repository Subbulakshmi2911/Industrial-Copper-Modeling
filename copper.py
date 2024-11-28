import streamlit as st
import pandas as pd
import pickle
from streamlit_option_menu import option_menu
from PIL import Image

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #F4F4F4;
    }
    .main-header {
        text-align: center;
        color: #009999;
        margin-bottom: 20px;
    }
    .section-header {
        color: #333;
        font-size: 20px;
        margin-top: 30px;
    }
    .stButton>button {
        background-color: #009999;
        color: white;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #006666;
    }
    .info-box {
        background-color: #E6FFFA;
        padding: 15px;
        border: 1px solid #00CCCC;
        border-radius: 5px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Main title
st.markdown("<h1 class='main-header'>Industrial Copper Modeling Application</h1>", unsafe_allow_html=True)

# Load models and data
with open('D:/Copper modling/trained_classification_model.pkl', 'rb') as file:
    model1 = pickle.load(file)

with open('D:/Copper modling/df_Regression_model.pkl', 'rb') as df_file:
    df = pickle.load(df_file)

with open('D:/Copper modling/trained_Regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Unique values and mappings
unique_customers = df['customer'].unique()
unique_product_refs = df['product_ref'].unique()
unique_country_code = df['country'].unique()
unique_apps = df['application'].unique()

item_type_map = {
    5: 'W', 6: 'WI', 3: 'S', 1: 'Others', 2: 'PL', 0: 'IPL', 4: 'SLAWR'
}
item_type_map1 = {
    0: 'Lost', 1: 'Won', 2: 'Draft', 3: 'To be approved',
    4: 'Not lost for AM', 5: 'Wonderful', 6: 'Revised',
    7: 'Offered', 8: 'Offerable'
}
item_type_map_reverse = {v: k for k, v in item_type_map.items()}
item_type_map1_reverse = {v: k for k, v in item_type_map1.items()}

# Sidebar menu
with st.sidebar:
    select = option_menu("Main Menu", ["Home", "Prediction Models", "About"], 
                         icons=["house", "gear", "info-circle"], default_index=0,
                         styles={
                             "container": {"padding": "5px", "background-color": "#EFFBFF"},
                             "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px", "--hover-color": "#CCE5FF"},
                             "nav-link-selected": {"background-color": "#009999"},
                         })

if select == "Home":
    image1 = Image.open("D:/Copper modling/download.jpg")
    st.image(image1, use_container_width=True)

    st.header("Skills Takeaway From This Project")
    st.markdown("<ul><li>Python Scripting</li><li>Data Preprocessing</li><li>EDA</li><li>Streamlit</li></ul>", unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>Introduction</h3>", unsafe_allow_html=True)
    st.write("""
        This project aims to develop two machine learning models for the copper industry to 
        address challenges in predicting selling prices and lead classification. By leveraging advanced 
        techniques like data normalization and tree-based models, this project aims to provide 
        accurate predictions for optimal pricing decisions and lead capturing.
    """)
    
if select == "Prediction Models":
    tab1, tab2 = st.tabs(["Status Prediction", "Price Prediction"])

    with tab1:
        st.title("Status Prediction")
        st.markdown("<h3 class='section-header'>Input Features</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            quantity_tons = st.number_input("Quantity (tons):", min_value=2, max_value=151, step=1)
            customer = st.selectbox("Customer:", options=unique_customers)
            product_ref = st.selectbox("Product Reference:", options=unique_product_refs)
            country = st.selectbox("Country:", options=unique_country_code)
            item_type_label = st.selectbox("Item Type:", options=list(item_type_map.values()))

        with col2:
            application = st.selectbox("Application:", options=unique_apps)
            thickness = st.number_input("Thickness (mm):", min_value=0.18, max_value=6.45, step=0.01)
            width = st.number_input("Width (mm):", min_value=700, max_value=1980, step=1)
            selling_price = st.number_input("Selling Price:", min_value=243.0, max_value=1379.0, step=0.1)
            lead_time = st.number_input("Lead Time:", min_value=1, max_value=448, step=1)

        st.markdown("<h3 class='section-header'>Prediction Result</h3>", unsafe_allow_html=True)
        if st.button("Predict Status"):
            input_data = pd.DataFrame({
                "quantity tons": [quantity_tons],
                "customer": [customer],
                "country": [country],
                "item type": [item_type_map_reverse[item_type_label]],
                "application": [application],
                "thickness": [thickness],
                "width": [width],
                "product_ref": [product_ref],
                "selling_price": [selling_price],
                "lead_time": [lead_time],
            })
            try:
                prediction = model1.predict(input_data)[0]
                status_label = "Win" if prediction == 1 else "Loss"
                st.success(f"Predicted Status: {status_label}")
            except Exception as e:
                st.error(f"Prediction failed: {e}")

    with tab2:
        st.title("Price Prediction")
        st.markdown("<h3 class='section-header'>Input Features</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            quantity_tons = st.number_input("Quantity (tons):", min_value=2, max_value=151, step=1,key="input1")
            customer = st.selectbox("Customer:", options=unique_customers,key="input2")
            product_ref = st.selectbox("Product Reference:", options=unique_product_refs,key="input3")
            country = st.selectbox("Country:", options=unique_country_code,key="input4")
            item_type_label = st.selectbox("Item Type:", options=list(item_type_map.values()),key="input5")
            
        with col2:
            application = st.selectbox("Application:", options=unique_apps,key="input6")
            thickness = st.number_input("Thickness (mm):", min_value=0.18, max_value=6.45, step=0.01,key="input7")
            width = st.number_input("Width (mm):", min_value=700, max_value=1980, step=1,key="input8")
            status = st.selectbox("status:", options=list(item_type_map1.values()),key="input10")
            lead_time = st.number_input("Lead Time:", min_value=1, max_value=448, step=1,key="input9")
            
        st.markdown("<h3 class='section-header'>Prediction Result</h3>", unsafe_allow_html=True)
        if st.button("Predict Status",key="input11"):
            input_data = pd.DataFrame({
                "quantity tons": [quantity_tons],
                "customer": [customer],
                "country": [country],
                "status":[item_type_map1_reverse[status]],
                "item type": [item_type_map_reverse[item_type_label]],
                "application": [application],
                "thickness": [thickness],
                "width": [width],
                "product_ref": [product_ref],
                "lead_time": [lead_time],
            })
            try:
                predicted_price = model.predict(input_data)[0]
                st.success(f"The predicted selling price is: **${predicted_price:,.2f}**")
            except Exception as e:
                st.error(f"Prediction failed: {e}")

if select == "About":
    st.title("About This Project")
    st.markdown("<h3 class='section-header'>Approach</h3>", unsafe_allow_html=True)
    st.write("""
        This project involved the following steps:
        1. Data Understanding
        2. Data Cleaning and Preprocessing
        3. Exploratory Data Analysis
        4. Model Building and Evaluation
        5. Deployment Using Streamlit
    """)
