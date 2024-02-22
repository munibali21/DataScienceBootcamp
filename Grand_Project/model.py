import streamlit as st
import pickle
import pandas as pd

# Load the model
loaded_model = pickle.load(open('model_v2.pkl', 'rb'))

# Function to label encode categorical features
def label_encode_features(df):
    # Replace these with your actual label encoders
    home_encoder = {'Own': 2, 'Rent': 3, 'Mortgage': 0, 'Other': 1}
    intent_encoder = {'Debt Consolidation': 0, 'Home Improvement': 2, 'Medical Expenses': 1, 'Venture': 3,'Education':4,'Personal':5}
    default_encoder={'Y':1,'N':0}
    df['Default']=df['Default'].map(default_encoder)
    df['Home'] = df['Home'].map(home_encoder)
    df['Intent'] = df['Intent'].map(intent_encoder)

    return df

# Function to get predictions
def get_prediction(age, income, home, emp_length, intent, amount, rate, percent_income, default, cred_length):
    # Convert cred_length to float
    cred_length = float(cred_length)

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'Age': [age],
        'Income': [income],
        'Home': [home],
        'Emp_length': [emp_length],
        'Intent': [intent],
        'Amount': [amount],
        'Rate': [rate],
        'Percent_income': [percent_income],
        'Default': [default],
        'Cred_length': [cred_length]
    })

    # Label encode categorical features
    input_data = label_encode_features(input_data)

    # Make predictions
    prediction = loaded_model.predict(input_data)

    
    return prediction

# Streamlit app
def main():
    st.title('Loan Approval Prediction')

    # Input form
    age = st.slider('Age', 18, 100)
    income = st.number_input('Income')
    home = st.selectbox('Home', ['Own', 'Rent', 'Mortgage','Other'])
    emp_length = st.slider('Employment Length',0,41)
    intent = st.selectbox('Loan Intent', ['Debt Consolidation', 'Home Improvement', 'Medical Expenses', 'Venture','Education','Personal'])
    amount = st.number_input('Loan Amount')
    rate = st.number_input('Interest Rate')
    percent_income = st.number_input('Percentage of Income')
    default=st.radio("Have you ever been late in making a payment?", ('Y','N'))
    cred_length = st.slider('Cred_length',2,30)

    # Get prediction
    if st.button('Predict'):
        prediction = get_prediction(age, income, home, emp_length, intent, amount, rate, percent_income,default,
                                     cred_length)
        if prediction[0]==0:
            st.success(f'unapproved:{prediction}')
        else:
            st.success(f'approved:{prediction}')
        #st.success(f'The predicted loan status is: {prediction}')

if __name__ == '__main__':
    main()
