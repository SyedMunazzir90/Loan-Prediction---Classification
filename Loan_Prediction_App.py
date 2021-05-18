import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.markdown("<h1 style='text-align: center; '>Loan Prediction App</h1>", unsafe_allow_html=True)


st.sidebar.header('Apply Filters')
st.text("                 ")
st.text("                 ")
st.text("                 ")
st.text("                 ")
st.text("                 ")
st.text("                 ")
st.text("                 ")
st.text("                 ")
st.text("                 ")
st.text("                 ")
st.text("                 ")
st.text("                 ")

model = pickle.load(open('random_forests', 'rb'))

#driver = st.sidebar.selectbox('What are you looking for ?', ('---Select---', 'Prediction','Exploratory Data Analysis'))
driver = 'Prediction'
def user_input_features(): 

	applicant_income = st.sidebar.slider('Applicant Income ?', 150, 100000, 1)
	co_applicant_income = st.sidebar.slider('Co Applicant Income ?', 100, 50000, 1)
	loan_amount = st.sidebar.slider('Loan Amount ?', 10000, 700000, 10000)
	dependents = st.sidebar.selectbox('How many dependents ?', ('---Select---', 'Zero','One','Two','More than 3'))
	property_area = st.sidebar.selectbox('What is the property type ?', ('---Select---', 'Semi Urban','Urban','Rural'))
	self_employed = st.sidebar.selectbox('Self Employed ?', ('---Select---', 'Yes','No'))
	gender = st.sidebar.selectbox('Gender ?', ('---Select---', 'Male','Female'))
	education = st.sidebar.selectbox('Education ?', ('---Select---', 'Graduate','Not Graduate'))
	married = st.sidebar.selectbox('Married ?', ('---Select---', 'Yes','No'))
	credit_history = st.sidebar.selectbox('Credit History ?', ('---Select---', 'Good','Bad'))
	
	submit = st.sidebar.button('Submit')
	

	
	features =	{'applicant_income': applicant_income,
				'co_applicant_income': co_applicant_income,
				'loan_amount': loan_amount,
				'dependents': dependents,
				'property_area':property_area,
				'self_employed': self_employed,
				'gender': gender,
				'education': education,
				'married': married,
				'credit_history': credit_history
				} 
	
	return features, submit 

if driver == 'Prediction':
	features, submit  = user_input_features()

	if((submit == 1 ) & (features['dependents'] != '---Select---') & (features['property_area'] != '---Select---') 
		& (features['self_employed'] != '---Select---') & (features['gender'] != '---Select---') 
	 	& (features['education'] != '---Select---') & (features['married'] != '---Select---') 
	 	& (features['credit_history'] != '---Select---')) :


		if features['dependents'] == 'Zero':
			features['dependents'] = 0

		if features['dependents'] == 'One':
			features['dependents'] = 1

		if features['dependents'] == 'Two':
			features['dependents'] = 2

		if features['dependents'] == 'More than 3':
			features['dependents'] = 3

		if features['property_area'] == 'Semi Urban':
			features['property_area'] = 0

		if features['property_area'] == 'Urban':
			features['property_area'] = 1

		if features['property_area'] == 'Rural':
			features['property_area'] = 2

		if features['self_employed'] == 'Yes':
			features['self_employed'] = 1

		if features['self_employed'] == 'No':
			features['self_employed'] = 0

		if features['gender'] == 'Male':
			features['gender'] = 0

		if features['gender'] == 'Female':
			features['gender'] = 1

		if features['education'] == 'Graduate':
			features['education'] = 1

		if features['education'] == 'Not Graduate':
			features['education'] = 0

		if features['married'] == 'Yes':
			features['married'] = 1

		if features['married'] == 'No':
			features['married'] = 0

		if features['credit_history'] == 'Good':
			features['credit_history'] = 1

		if features['credit_history'] == 'Bad':
			features['credit_history'] = 0

		features['applicant_income'] = np.log(features['applicant_income'])
		features['co_applicant_income'] = np.log(features['co_applicant_income'])
		features['loan_amount'] = np.log(features['loan_amount'])


		dataset = pd.DataFrame(features, index = [0])

		result = model.predict(dataset)

		if result == 0:
	 		st.markdown("<h2 style='text-align: center; '> Sorry!!! Your loan application will most likely be Rejected.</h2>", unsafe_allow_html=True)		
		else:
			st.markdown("<h2 style='text-align: center; '>Congratulations!!! Your loan application will most likely be Approved.</h2>", unsafe_allow_html=True)

	
	




