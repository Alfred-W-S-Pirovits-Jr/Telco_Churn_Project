import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
from env import get_db_url
import os


def get_telco_data():
    
    # Querey the database to collect a joined column of customers, contract_types, internet_service_types, and payment_types
    query = '''
    SELECT * 
    FROM customers
    JOIN contract_types USING (contract_type_id)
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN payment_types USING (payment_type_id);
    '''
    
    # Creates a telco.csf from the query if there is none and returns the data.  If a csv already exists, it reads and returens it.
    filename = 'telco.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else: 
        #read the SQL query into a dataframe
        telco_churn_db = pd.read_sql(query, get_db_url('telco_churn'))
        
        # Write that dataframe to disk for later.  Called "caching" the data for later.
        telco_churn_db.to_csv(filename)
        
    return telco_churn_db

