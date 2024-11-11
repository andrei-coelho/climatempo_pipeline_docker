from airflow import DAG 
from airflow.operators.python import PythonOperator

from src.extraction import get_data_wether
from src.repositorio import save_data_clima
from src.clima_model import ClimaDetalhado
from datetime import timedelta, datetime

def get_atual_temperatura():
    data = get_data_wether()
    if not save_data_clima(ClimaDetalhado(
        data_hora=data['data_hora'],
        clima = data['clima'],
        periodo = data['periodo'],
        temperatura_atual = data['temperatura_atual'],
        temperatura_minima = 0.0,
        temperatura_maxima = 0.0
    )): raise Exception("Erro ao tentar armazenar clima usando 'save_data_clima' do repositorio")


default_args = {
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

with DAG(
    'salvar_clima_a_cada_minuto',
    description='salva o clima detalhado por minuto',
    default_args=default_args,
    start_date=datetime.now() - timedelta(days=1),
    schedule_interval=timedelta(minutes=1)
) as dag:
    
    salvar_task = PythonOperator(
        task_id = 'salvar_clima_datalhado',
        python_callable=get_atual_temperatura
    )

    salvar_task