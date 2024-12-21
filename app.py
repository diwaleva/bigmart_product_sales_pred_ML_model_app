
#import streamlit
import streamlit as st

import pickle as pickle
# import the libraries
import pandas as pd
import numpy as np
# importing required libraries
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error as mae
# from sklearn.metrics import mean_squared_error
from math import sqrt
import pickle, csv
import warnings
warnings.filterwarnings('ignore')

# loading the trained model
# pickle_in = open('bigmart_streamlit_app_model.pkl', 'rb')
# model_regressor = pickle.load(open('model.pkl','rb'))

filename = 'bigmart_streamlit_app_model.pkl'
# Load the model from the file
with open(filename, 'rb') as file:
        model_regressor = pickle.load(file)

# this is the main function in which we define our app
def main():
    # header of the page
    html_temp = """
    <div style ="background-color:lightblue;padding:13px">
    <h1 style ="color:dark-gray;text-align:center;">Check your Item Outlet Sales Predictions</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    # following lines create boxes in which user can enter data required to make prediction
    Weight = st.number_input("Item Weight in lbs  (Ex: 3000.3333)")
    MRP = st.number_input("Item MRP in $ (Ex: 3000.3333)")
    Size = st.selectbox('Outlet_Size',("Small","Medium","High"))
    result =""

    # when 'Check' is clicked, make the prediction and store it
    if st.button("Check"):
        result = prediction(Weight, MRP, Size)
        st.success('Your item outlet sales is {}'.format(result))

# defining the function which will make the prediction using the data which the user inputs
def prediction(Weight, MRP, Size):
    # 2. Loading and Pre-processing the data

      if Size == "Small":
        Size = 1.0
      if Size == "Medium":
        Size = 2.0
      if Size == "High":
        Size = 3.0

      ## 3. Standardize the data using MinMaxScalar 
      df_app = pd.DataFrame()
      df_app = [Weight, MRP, Size]
      
      scaler = preprocessing.MinMaxScaler()
      minmax_all = scaler.fit_transform(df_app)
      minmax_all = pd.DataFrame(minmax_all, columns=df_app.columns.tolist())


      prediction = model_regressor.predict(
        [minmax_all])
      
      return prediction

if __name__=='__main__':
    main()
