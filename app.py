import streamlit as st
import pickle
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd


with open('model.pkl', 'rb') as f :
    model = pickle.load(f)

Testing_Data = pd.read_csv('Testing_data.csv')

Predictions = model.predict(Testing_Data)

# Count the number of churned and non-churned users
churn_counts = pd.Series(Predictions).value_counts()

# Plot the counts
fig, ax = plt.subplots()
sns.barplot(x=churn_counts.index, y=churn_counts.values, ax=ax)
ax.set_title('Count of Churned and Non-Churned Users')
ax.set_xlabel('Churn')
ax.set_ylabel('Count')

# Display the plot in the streamlit app
st.pyplot(fig)