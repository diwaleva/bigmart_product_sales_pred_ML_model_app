# bigmart_product_sales_pred_ML_model_app
A self-service ML Model based app for making Bigmart product sales predictions based on user input data. It consists of a user friendly UI to input data for generating predictions. The ML model is a simple Linear Regression. The data is pre-processed and standardized before sending the data to the model. GitHub and Streamlit are leveraged for model deployment.

## Model Data Dictionary:
**Item Weight**: Weight of the product. (Selected for final model)
**Item_Fat_Content**: Amount of fat in the products( Low or Regular) 
**Item_Type**: Type of Item (Dairy, Drinks, Fruits, Others)
**Item_MRP**: Maximum Retail Price (list price) of the product. (Selected for final model)
**Outlet_Size**: The size of the store in terms of ground areas covererd (Small, Medium, High). (Selected for final model)
**Item_Outlet_Sales**: This is the target outcome variable. It represents the sale of product in a particular store.

## Model Training Data: big_mart_data.csv

## Saved Model: 
- **Model File**: bigmart_app_model.sav
- **Model** : Linear Regression()


### Model Training Summary:

#### Data Value Counts:
    - Item_Weight assumes 409 values.
    - Item_Fat_Content assumes 2 values i.e. Low Fat, Regular
    - Item_Type assumes 4 values
    - Outlet_Size assumes 3 values
    - Item_MRP  assumes 3806 values
    - Item_Outlet_Sales assumes 2449 values.

#### Normalization:
MinMax Scaler

#### Decision Tree Decision Making:
![Bigmart App Decision Tree](/content/bigmart_app_decision-tree-img.png)


### Random Forest Feature Importances:

| Variable        | Importances  
| ----------------|:-------------:|
| Item_MRP        | 0.989842      |
| Outlet_Size     | 0.002691      |
| Item_Weight     | 0.00612       |
| Item_Type_Others| 0.001015      |
| Item_Fat_Content| 0.000327      |
| Item_Type_Dairy | 0.000327      |
| Item_Type_Drinks| 0.000000      |
| Item_Type_Fruits| 0.000000      |


### Selected Features utilized for Model Training and Prediction: Item_MRP, Item_Weight, Outlet_Size







