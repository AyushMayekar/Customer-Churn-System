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
    st.write("**The following are the insights of the data:**")
    st.image("pairplot.jpg", caption="PAIRPLOT", use_column_width=True)
    st.write("""
            **Understanding the Pairplot**
A pairplot is a collection of scatter plots arranged in a grid format. Each scatter plot in the grid shows the relationship between a pair of features. Additionally, it can show the distribution of a single feature along the diagonal.

**Features in the Pairplot**\n
Senior Citizen: Indicates whether a customer is a senior citizen or not.\n
Tenure: The number of months the customer has stayed with the company.\n
Total Charges: The total amount charged to the customer.\n
Monthly Charges: The amount charged to the customer every month.\n
Churn: Indicates whether the customer has churned (left the company) or not.\n

**How to Interpret the Pairplot**

Diagonals:
Each diagonal plot shows the distribution of a single feature. For example, a histogram of the tenure shows how long most customers stay with the company.
Look for peaks and spreads to understand common values and variability in each feature.

Scatter Plots:
Each scatter plot shows the relationship between two features. For example, a plot of tenure vs. Monthly Charges will show how the length of stay relates to monthly charges.
Points are typically color-coded by the churn status (e.g., blue for non-churned, orange for churned).

Correlations:
Positive Correlation: Features that tend to increase together. For example, if higher Total Charges are associated with longer tenure, you’ll see an upward trend in their scatter plot.
Negative Correlation: One feature decreases as the other increases. For example, if higher Monthly Charges are associated with a higher likelihood of churn, you’ll see a downward trend when plotting Monthly Charges against Churn.
Cluster Patterns:

Look for clusters of points. For example, a cluster of senior citizens with high monthly charges who also churn might suggest that high charges are a pain point for older customers.
            """)

    st.image("barplot.jpg", caption="BARPLOT", use_column_width=True)
    st.write("""

**Understanding the Barplot**
A barplot is a great way to visualize categorical data and its relationship with a numerical feature. In this case, we are examining the relationship between customer churn, total charges, and the payment method of electronic check.

**Features in the Barplot**

Churn: Indicates whether the customer has churned (left the company) or not.\n
Total Charges: The total amount charged to the customer.\n
Payment Method - Electronic Check: Whether the customer uses electronic check as their payment method.\n
**How to Interpret the Barplot**

Bars Representing Churn:
The x-axis will show the churn status (e.g., Yes or No).
The y-axis will show the average total charges for each churn status.

Hue - Payment Method:
The bars will be color-coded based on whether the payment method is electronic check or not.
This will allow us to compare the total charges for customers using electronic check vs. other payment methods within each churn category.""")
    col1, col2 = st.columns(2)
    with col1:
        st.image("violin.jpg", caption="VIOLIN-PLOT", use_column_width=True)
        st.write("""
**Understanding the Violin Plot**\n
A violin plot is a powerful visualization tool that combines the features of a box plot and a density plot. It provides insights into the distribution of data across different categories. In this case, we are using a violin plot to showcase the relationship between customer churn and tenure, with a focus on customers with a two-year contract.

**Features in the Violin Plot**\n
Churn: Indicates whether the customer has churned (left the company) or not.\n
Tenure: The length of time (in months) that the customer has been with the company.\n
Contract - Two Year: Indicates whether the customer has a two-year contract.\n
**How to Interpret the Violin Plot**\n
Churn Categories:
The x-axis will show the churn status (e.g., Yes or No).\n
Tenure Distribution:
The y-axis will show the tenure in months.
The shape of the violin will display the distribution of tenure for each churn category. A wider section of the violin indicates a higher density of customers with that tenure.\n
Hue - Contract Two Year:
The plot will be color-coded based on whether the customer has a two-year contract or not.
This allows for a comparison of tenure distributions within churn categories, split by contract type.""")
    with col2 :
        st.image("jointplot.jpg", caption="JOINT-PLOT", use_column_width=True)
        st.write("""
**Understanding the Joint Plot with Density Plot**\n
A joint plot is a convenient way to visualize the relationship between two variables along with their individual distributions. Using a density plot within the joint plot provides a clearer understanding of the data distribution. In this case, we are visualizing the relationship between customer churn and the type of internet service, specifically fiber optic.

**Features in the Joint Plot**\n
Churn: Indicates whether the customer has churned (left the company) or not.\n
Internet Service - Fiber Optic: Indicates whether the customer is using fiber optic internet service.\n
**How to Interpret the Joint Plot**\n
Churn Categories:
The x-axis will show the churn status (e.g., Yes or No).\n
Internet Service - Fiber Optic:
The y-axis will show whether the customer uses fiber optic internet service (typically represented as binary: 1 for Yes, 0 for No).\n
Density Plot:
The joint plot will include density contours that show where data points are concentrated.
These contours provide insight into the distribution and concentration of churn status relative to the use of fiber optic service.""")



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


