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
#unique_customers = df['customer'].unique()
unique_product_refs = unique_product_refs = {
    640665: 0,
    1721130331: 1,
    1693867563: 2,
    1671876026: 3,
    1670798778: 4,
    1665584662: 5,
    628377: 6,
    640405: 7,
    1671863738: 8,
    640400: 9,
    929423819: 10,
    164141591: 11,
    1690738206: 12,
    628117: 13,
    1693867550: 14,
    1332077137: 15,
    628112: 16,
    1722207579: 17,
    164336407: 18,
    164337175: 19,
    1668701725: 20,
    1282007633: 21,
    1668701376: 22,
    1665572374: 23,
    1668701718: 24,
    1690738219: 25,
    1668701698: 26,
    1665572032: 27,
    1665584320: 28,
    1665584642: 29,
    611993: 30,
    611733: 31,
    611728: 32
}

#unique_product_refs_reverse = {v: k for k, v in unique_product_refs.items()}

unique_country_code = {
    89.0: 0,
    40.0: 1,
    80.0: 2,
    79.0: 3,
    39.0: 4,
    77.0: 5,
    78.0: 6,
    26.0: 7,
    27.0: 8,
    28.0: 9,
    32.0: 10,
    25.0: 11,
    107.0: 12,
    30.0: 13,
    84.0: 14,
    38.0: 15,
    113.0: 16
}

#unique_country_code_reverse = {v: k for k, v in unique_country_code.items()}

unique_apps = {
    58.0: 0,
    68.0: 1,
    59.0: 2,
    56.0: 3,
    28.0: 4,
    69.0: 5,
    22.0: 6,
    25.0: 7,
    4.0: 8,
    15.0: 9,
    40.0: 10,
    3.0: 11,
    66.0: 12,
    20.0: 13,
    39.0: 14,
    10.0: 15,
    5.0: 16,
    26.0: 17,
    27.0: 18,
    67.0: 19,
    19.0: 20,
    29.0: 21,
    2.0: 22,
    65.0: 23,
    70.0: 24,
    79.0: 25,
    42.0: 26,
    41.0: 27,
    38.0: 28,
    99.0: 29
}

#unique_apps_reverse = {v: k for k, v in unique_apps.items()}

item_type_map = {'WI':0, 'PL':1, 'Others':2, 'IPL':3, 'S':4,
                                 'W':5, 'SLAWR':6}

item_type_map1 = {'Lost':1, 'Won':2, 'Draft':0, 'To be approved':5, 'Not lost for AM':3,
                                 'Wonderful':8, 'Revised':4, 'Offered':6, 'Offerable':7}

#item_type_map_reverse = {v: k for k, v in item_type_map.items()}
#item_type_map1_reverse = {v: k for k, v in item_type_map1.items()}



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
            #customer = st.selectbox("Customer:", options=unique_customers)
            #product_ref = st.selectbox("Product Reference:", options=unique_product_refs)
            #country = st.selectbox("Country:", options=unique_country_code)
            product_ref = st.selectbox("Product Reference", options=list(unique_product_refs.keys()))
            selected_value = unique_product_refs[product_ref]
            country = st.selectbox("Country:", options=list(unique_country_code.keys()))
            item_type_label = st.selectbox("Item Type:", options=list(item_type_map.keys()))

        with col2:
            #application = st.selectbox("Application:", options=unique_apps)
            application = st.selectbox("Application::", options=list(unique_apps.keys()))
            thickness = st.number_input("Thickness (mm):", min_value=0.18, max_value=6.45, step=0.01)
            width = st.number_input("Width (mm):", min_value=700, max_value=1980, step=1)
            selling_price = st.number_input("Selling Price:", min_value=243.0, max_value=1379.0, step=0.1)
            lead_time = st.number_input("Lead Time:", min_value=1, max_value=448, step=1)

        st.markdown("<h3 class='section-header'>Prediction Result</h3>", unsafe_allow_html=True)
        if st.button("Predict Status"):
            input_data = pd.DataFrame({
                "quantity tons": [quantity_tons],
                #"customer": [customer],
                "item type": item_type_map[item_type_label],
                "thickness": [thickness],
                "width": [width],
                "selling_price": [selling_price], 
                "country_encoded": unique_country_code[country],
                "application_encoded": unique_apps[application],
                "product_ref_encode": [selected_value],
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
            #customer = st.selectbox("Customer:", options=unique_customers,key="input2")
            product_ref_encode = st.selectbox("Product Reference", options=list(unique_product_refs.keys()),key="input2")
            selected_value = unique_product_refs[product_ref_encode]
            country = st.selectbox("Country:", options=list(unique_country_code.keys()),key="input4")
            item_type_label = st.selectbox("Item Type:", options=list(item_type_map.keys()),key="input5")
            
        with col2:
            application = st.selectbox("Application::", options=list(unique_apps.keys()),key="input6")
            thickness = st.number_input("Thickness (mm):", min_value=0.18, max_value=6.45, step=0.01,key="input7")
            width = st.number_input("Width (mm):", min_value=700, max_value=1980, step=1,key="input8")
            status = st.selectbox("status:", options=list(item_type_map1.keys()),key="input10")
            lead_time = st.number_input("Lead Time:", min_value=1, max_value=448, step=1,key="input9")
            
        st.markdown("<h3 class='section-header'>Prediction Result</h3>", unsafe_allow_html=True)
        if st.button("Predict Status",key="input11"):
            input_data = pd.DataFrame({
                "quantity tons": [quantity_tons],
                #"customer": [customer],
                "status":item_type_map1[status],
                "item type": item_type_map[item_type_label],
                "thickness": [thickness],
                "width": [width], 
                "country_encoded": unique_country_code[country],
                "application_encoded": unique_apps[application],
                "product_ref_encode": unique_product_refs[product_ref],
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
