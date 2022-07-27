from gettext import install
import numbers
from pydoc import describe
from statistics import median
from turtle import shape
from unicodedata import numeric

def EDA_SCRIPT(data_path):
    import pandas as pd 
    import numpy as np 
    import matplotlib.pyplot as plt
    import os

    #loading data
    try:
        df = pd.read_csv(data_path)
    except Exception :
        try:
            df = pd.read_excel(data_path)
        except Exception :
            try:
               df = pd.read_json(data_path)
            except Exception :
                try:
                   df = pd.read_xml(data_path)
                except Exception :
                    print('Wrong path!\n please check the extention(csv,excel,json,xml)')

    else :
        print('DataFrame : ')
        display(df.head())

        print('_____________________________________________________________________')
        print('Data Information : ')
        display(df.info())

        print('_____________________________________________________________________')
        print('Data Describtion : ')
        display(df.describe())

        print('_____________________________________________________________________')
        print('NaN percentage for each column : ')
        name = []
        percentage = []
        for i in df.columns:
            name.append(i)
            s = (str((df[i].isnull().sum/df.shape[0]*100).round(2))+'&')
            percentage.append(s)
        nan_percentage_dict['name'] = name
        nan_percentage_dict['percentage'] = percentage
        nan_percentage_df = pd.DataFrame(nan_percentage_dict)
        display(nan_percentage_dict)   


    #Separate columns
    numerical_col = []
    cat_col = []
    cols = df.columns
    for i in ranage(len(cols)):
        if df[cols[i]].dtype == np.int64 or df[cols[i]].dtype == np.int32 or df[cols[i]] :
            numerical_col.append(cols[i])
        else :
            cat_col.append(cols[i])

    #check nan values
    numerical_col_nan = []
    cat_col_nan = []
    for i in numerical_col:
        if(df[i].isnull().sum()>0 ):
            numerical_col.append(i)
    for i in cat_col:
        if(df[i].isnull().sum()>0 ):
            cat_col.append(i)

    #Filling nan values
    if(len(numerical_col.nan)>0):
        print('Filling numerical nan values now : ')
        for i in numerical_col_nan:
            median = df[i].describe()['50%'].round(2)
            df[i].fillna(median , inplace= True)
    elif(len(cat_col.nan)>0):
        print('Filling categorical nan values now : ')
        for i in cat_col_nan:
            mode = df[i].describe()['freq']
            df[i].fillna(mode , inplace= True)
    elif() :
        print('There is no nan values ')

    



            



        
    


   