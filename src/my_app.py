import streamlit as st
import numpy as np
import pandas as pd
import pickle

# target mapping
target_mapping = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

# load model
with open('model/model.pkl', "rb") as f:
	model = pickle.load(f)
	

@st.cache()

def prediction(sepal_length, sepal_width, petal_length, petal_width):
	# get predictions
	pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
	pred_val = target_mapping[pred[0]]
	return pred_val


# putting the app related codes in main()
def main():
	# -- Set page config
	apptitle = 'DSSI'
	st.set_page_config(page_title=apptitle, page_icon='random', 
		layout= 'wide', initial_sidebar_state="expanded")
	# random icons in the browser tab

	# give a title to your app
	st.title('Solution Implementation')
	#front end elements of the web page 
	# pick colors from: https://www.w3schools.com/tags/ref_colornames.asp
	html_temp = """ <div style ="background-color:AntiqueWhite;padding:15px"> 
       <h1 style ="color:black;text-align:center;">Iris Species Detection app</h1> 
       </div> <br/>"""

    #display the front end aspect
	st.markdown(html_temp, unsafe_allow_html = True)
	# let us make infrastructure to provide inputs
	# we will add the inputs to side bar
	st.sidebar.info('Provide input using the panel')
	st.info('Click Assess button below')

	sepal_length = st.number_input(label="Sepal_length",min_value=1.0,\
									step=0.1,max_value=10.0,\
									format="%f")
	st.write('input sepal_length', sepal_length)
	sepal_width = st.number_input(label="Sepal_width",\
									min_value=1.0,\
									step=0.1,\
									max_value=10.0,\
									format="%f")
	st.write('input sepal_width', sepal_width)
	petal_length = st.number_input(label="Petal_length",\
									min_value=0.0,\
									step=0.1,\
									max_value=10.0,\
									format="%f")
	st.write('input petal_length', petal_length)
	petal_width = st.number_input(label="Petal_width",\
									min_value=0.0,\
									step=0.1,\
									max_value=10.0,\
									format="%f")
	st.write('input petal_width', petal_width)
	

	result =""
	# assessment button
	if st.button("Predict"):
		assessment = prediction(sepal_length, sepal_width, petal_length, petal_width)
		st.success('**System assessment says:** {}'.format(assessment))

	# if st.button("Reset"):
	# 	pyautogui.hotkey("ctrl","F5")

	# st.balloons()
	st.success("App is working!!") # other tags include st.error, st.warning, st.help etc.

if __name__ == '__main__':
	main()
