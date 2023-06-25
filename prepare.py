import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import os
import acquire
from sklearn.model_selection import train_test_split


def prep_telco():
    # Acquires the telco data
    telco_churn_db = acquire.get_telco_data() 

    #  Drops columns 'payment_type_id', 'internet_service_type_id', 'contract_type_id' and gets dummies for 
    # 'gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type'
    #  Didn't use for the final project
    telco_churn_db = telco_churn_db.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    dummy_telco_churn_db = pd.get_dummies(telco_churn_db[['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type']], dummy_na=False, drop_first=True)
    telco_churn_db = pd.concat([telco_churn_db, dummy_telco_churn_db], axis=1)
    return telco_churn_db

def prep_telco_alternative():
    telco_churn_db = acquire.get_telco_data()

    #Drops the id columns because they will throw off the results of the ML models and are not correlated with churn
    telco_churn_db = telco_churn_db.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    
    #Create a dummy column for gender, partner, dependents, phone_service, multiple_lines, online_security, online_backup, device_protection, tech_support, streaming_tv, streaming_movies, paperless_billing, churn, internet_service_type, and payment_type columns.
    #These dummies will drop the first column
    dummy_telco_churn_db = pd.get_dummies(telco_churn_db[['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'internet_service_type', 'payment_type']], dummy_na=False, drop_first=True)
    
    #Since month-to-month seems VERY correlated to churn rate I am not dropping first when doing contract type specifically for knn nearest neighbors where I have to cut down the dimensions and choose the best correlated issues.  
    #I expect the decision trees to give me more intuition on the most highly correlated dimensions to choose
    
    dummy_telco_churn_db_first = pd.get_dummies(telco_churn_db[['contract_type']], dummy_na=False, drop_first=False) 
    telco_churn_db = pd.concat([telco_churn_db, dummy_telco_churn_db, dummy_telco_churn_db_first], axis=1)
    
    # Dropping all object columns as they are redundant and coded in other columns.
    
    telco_churn_db = telco_churn_db.drop(columns=telco_churn_db.select_dtypes(exclude='number').columns)

    # Drop all no_internet service columns from dataframe because it is redundant with internet service type none
    telco_churn_db = telco_churn_db.drop(columns=['online_backup_No internet service', 'device_protection_No internet service', 'tech_support_No internet service', 'streaming_tv_No internet service', 'streaming_movies_No internet service', 'online_security_No internet service'])
    
    return telco_churn_db

def split_data(df, stratify_col):

    # Splits the data into train, validate, and test sets with sizes .8,.2 and .2 respectively
    train_validate, test = train_test_split(df, test_size = .2, random_state=823, stratify=df[stratify_col])
    train, validate = train_test_split(train_validate, test_size=.25, random_state=823, stratify=train_validate[stratify_col])
    return train, validate, test

def split_data_label(df, stratify_col, test_size=.2, validate_size=.2):

    #  This version allows the user to specify the desired test size and validate size and divides the original dataframe accordingly.
    train_validate, test = train_test_split(df, test_size = .2, random_state=823, stratify=df[stratify_col])
    train, validate = train_test_split(train_validate, test_size= validate_size / (1 - test_size), random_state=823, stratify=train_validate[stratify_col])
    
    #  This part seperates the data into the proper train validate and test sets assuming that the target variable is the same as column the user wants to stratify upon. 
    X_train = train.drop(columns=[stratify_col])
    y_train = train[stratify_col]

    X_validate = validate.drop(columns=[stratify_col])
    y_validate = validate[stratify_col]

    X_test = test.drop(columns=[stratify_col])
    y_test = test[stratify_col]

    return X_train, y_train, X_validate, y_validate, X_test, y_test