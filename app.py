
#import required libraries
import streamlit as st
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error as mae


import joblib
model_regressor = joblib.load('bigmart_app_model.sav')

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
    Weight = st.number_input("Item Weight in lbs  (Ex: 10.3333)")
    MRP = st.number_input("Item MRP in $ (Ex: 10.3333)")
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

      # Create a dataframe
      df_app = pd.DataFrame()
      # df_app = [Weight, MRP, Size]

      df_app['Weight'] = Weight
      df_app['MRP'] = MRP
      df_app['Size'] = Size

      # reshape the dataframe since we have a single sample
      df_app.reshape(1,-1)

      # apply minmax scalar to the dataframe
      scaler = preprocessing.MinMaxScaler()
      minmax_all = scaler.fit_transform(df_app)
      minmax_all = pd.DataFrame(minmax_all, columns=df_app.columns.tolist())

      # Reshape the values before sending it to the model as it contains single sample  (for single feature we should apply(-1,1))
      minmax_all.reshape(1, -1)


      # Generate predictions using the model
      prediction = model_regressor.predict(minmax_all['Weight'], minmax_all['MRP'], minmax_all['Size'])
      
      return prediction

if __name__=='__main__':
    main()
