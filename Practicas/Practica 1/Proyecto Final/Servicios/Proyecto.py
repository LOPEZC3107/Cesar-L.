import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def loadData():

    files=os.listdir('./proyecto/data')
    for file in files:
        print(file)
        df=pd.read_csv(f"./proyecto/data/{file}")
        namefile=file.split(".")[0]
        with sqlite3.connect('./proyecto/database.db') as conn:
            df.to_sql(f'{namefile}',con=conn, index=False, if_exists='replace')
            print(f'data carga {namefile}')
        print(df.head())

def generateReport():
     with sqlite3.connect('./proyecto/database.db') as conn:
            query= 'SELECT * FROM amazon'
            df=pd.read_sql(query,conn)
            df['actual_price'] = df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)
            filter_df = df[(df['actual_price'] > 30000)]
            #df.head()
            #dfv2=df.apply(filter_by_price[price])
            #df.to_csv('./proyecto/reports/amazon-report.csv')
            filter_df.to_csv('./proyecto/reports/amazon-report.csv',index=False)
            #print(df.head())
            print(filter_df.head())
def shOwData():
     with sqlite3.connect('./proyecto/database.db') as conn:
            query='select * from amazon'   
            df=pd.read_sql(query,conn)
            df['actual_price'] = df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)
            filter_df = df[df['actual_price'] > 28080]
            fig,ax=plt.subplots(figsize=(10,6))
            ax.scatter(filter_df['category'], filter_df['actual_price'], alpha=0.7)
            plt.xlabel('Categoría')
            plt.ylabel('Precio Actual')
            plt.title('Gráfico de Dispersión')
            plt.show()