import requests
import pandas as pd
from airflow import DAG
from airflow.decorators import task
import pendulum
from dotenv import load_dotenv
import os
from google.cloud import bigquery

load_dotenv('../.env')
api_key = os.getenv('API_KEY')
bigquery_json_path = 'dags/elevated-style-426310-s8-efb512dc5cb5.json'
table_id = os.getenv('TABELA_ID')

with DAG(
    dag_id = 'etl_currency_bigquery',
    start_date = pendulum.datetime(2025, 7, 31, 0, 0, 4, tz="UTC"),
    schedule='@monthly',
    catchup=False
) as dag:

    @task
    def connect_api():
        url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
        response = requests.get(url)
        data = response.json()
        return data
    
    @task
    def preprocessing_data(data):
        df = pd.DataFrame.from_dict(data['conversion_rates'], orient='index')
        df.reset_index(inplace=True)
        df.columns = ['moeda', 'valor']
        df['last_update'] = data['time_last_update_utc']
        return df
    
    ##Não é uma boa prática retornar esse tipo de objetivo via xcom, pode dar erro de serialização. Então dito isso, irei criar uma única função para contornar esse problema.
    @task
    # def connect_bigquery():
    #     CAMINHO_CHAVE = fr"{bigquery_json_path}"
    #     client = bigquery.Client.from_service_account_json(CAMINHO_CHAVE)
    #     return client
    
    # @task
    # def load_data(df, client):
    #     job_config = bigquery.LoadJobConfig(write_disposition='WRITE_APPEND')
    #     job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    #     job.result()

    #     print("Dados enviados com sucesso")

    @task
    def connect_and_load_data(df):
        CAMINHO_CHAVE = fr"{bigquery_json_path}"
        client = bigquery.Client.from_service_account_json(CAMINHO_CHAVE)
        job_config = bigquery.LoadJobConfig(write_disposition='WRITE_APPEND')
        job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
        job.result()

        print("Dados enviados com sucesso")

    data = connect_api()
    df = preprocessing_data(data)
    connect_and_load_data(df)