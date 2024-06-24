# Importing necessary dependencies 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 
import pickle as pkl 
import numpy as np


# Loading the trained model
with open('model.pkl', 'rb') as f :
    model = pkl.load(f)

# Streamlit framework

# home page
def HOME():
    st.title("HOME")
    st.write("""This application predicts customer churn in the telecom industry based on essential inputs, offering insights into how various factors influence churn.

**Walkthrough of the Application**
**1. What is Customer Churn ?**

Customer churn refers to the phenomenon where customers stop doing business with a company. In the telecom industry, it specifically means customers discontinuing their services with a telecom provider, such as canceling their subscriptions or switching to a competitor.

**2. Application Overview:**

Objective: Predict customer churn and understand its relationship with key factors in the telecom sector.

Inputs Required: Users provide relevant data points such as, service usage patterns, contract details (like tenure, contract type), and any customer support interactions.

Functionality:

Prediction: The application uses machine learning model to forecast whether a customer is likely to churn based on the provided data.
Insights: It provides actionable insights into which features (e.g., contract type, customer tenure) most strongly correlate with churn, helping businesses proactively manage customer retention strategies.
Usage:

Users interact with a user-friendly interface where they input customer data.
They receive immediate predictions 

**3. Application Flow:**

Step 1: Input Data: Users enter customer data into the application.

Step 2: Prediction: The application processes the input data through machine learning algorithms to predict whether a customer is likely to churn.

**4. Impact:**

By leveraging predictive analytics, telecom companies can enhance customer satisfaction, optimize marketing efforts, and ultimately improve business profitability by reducing customer churn.""")

# customer churn prediction page
def CUSTOMER_CHURN_PREDICTION():
    st.title("CUSTOMER CHURN PREDICTION")

    tenure = st.slider('**Enter the Customer Tenure(months)**', max_value=200, min_value=0, value=100)
    tenure_input = st.number_input('Tenure', max_value=200, min_value=0, value=tenure)
    if tenure != tenure_input:
        tenure = tenure_input
    
    monthlycharges = st.slider('**Enter the Customer Monthly charges**', max_value=10000.00, min_value=0.00, value=100.00)
    monthlycharges_input = st.number_input('Customer Monthly Charges', max_value=10000.00, min_value=0.00, value=monthlycharges)
    if monthlycharges != monthlycharges_input:
        monthlycharges = monthlycharges_input
    
    Totalcharges = st.slider('**Enter the Customer Total Charges**', max_value=10000.00, min_value=0.00, value=100.00)
    Totalcharges_input = st.number_input('Customer Total Charges', max_value=10000.00, min_value=0.00, value=Totalcharges)
    if Totalcharges != Totalcharges_input:
        Totalcharges = Totalcharges_input

    InternetService_Fiber_optic = st.radio('**Select if the Customer uses Internet Service(Fiber Optic)**', ['YES', 'NO'])
    if InternetService_Fiber_optic == 'YES':
        InternetService_Fiber_optic = True
    elif InternetService_Fiber_optic == 'NO':
        InternetService_Fiber_optic = False
    else:
        st.warning('**PLEASE SELECT AN OPTION(YES/NO)**', icon="⚠️")

    Contract_Two_year = st.radio('**Select if the Customer has a Two year Contract**', ['YES', 'NO'])
    if Contract_Two_year == 'YES':
        Contract_Two_year = True
    elif Contract_Two_year == 'NO':
        Contract_Two_year = False
    else:
        st.warning('**PLEASE SELECT AN OPTION(YES/NO)**', icon="⚠️")
    
    PaymentMethod_Electronic_check = st.radio('**Select if the Customer uses Payment Method(Electronic Check)**', ['YES', 'NO'])
    if PaymentMethod_Electronic_check == 'YES':
        PaymentMethod_Electronic_check = True
    elif PaymentMethod_Electronic_check == 'NO':
        PaymentMethod_Electronic_check = False
    else:
        st.warning('**PLEASE SELECT AN OPTION(YES/NO)**', icon="⚠️")

    if st.button("**SUBMIT**"):
        input_data = np.array([[tenure_input, monthlycharges_input, Totalcharges_input, InternetService_Fiber_optic, Contract_Two_year, PaymentMethod_Electronic_check]])
        response = model.predict(input_data)
        if response[0] == 1:
            st.write("The Customer is likely to **CHURN**")
        elif response[0] == 0:
            st.write("The Customer is likely to **NOT CHURN**")

# customer churn data insights page
def CUSTOMER_CHURN_DATA_INSIGTHS():
    st.title("CUSTOMER CHURN DATA INSIGTHS")

# creating sessions 
if 'section' not in st.session_state:
    st.session_state.section = 'section1'

# sidebar
st.sidebar.title('GO TO')
if st.sidebar.button('**HOME**'):
    st.session_state.section  = 'section1'

if st.sidebar.button('**CUSTOMER CHURN PREDICTION**'):
    st.session_state.section  = 'section2'

if st.sidebar.button('**CUSTOMER CHURN DATA INSIGTHS**'):
    st.session_state.section  = 'section3'

if st.session_state.section  == 'section1':
    HOME()
elif st.session_state.section  == 'section2':
    CUSTOMER_CHURN_PREDICTION()
elif st.session_state.section  == 'section3':
    CUSTOMER_CHURN_DATA_INSIGTHS()


