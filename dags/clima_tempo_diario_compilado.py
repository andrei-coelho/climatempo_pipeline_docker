from airflow import DAG 
from airflow.operators.python import PythonOperator 
from collections import defaultdict
import math
from src.repositorio import get_rows_clima_detalhado, save_data_clima
from datetime import datetime, timedelta
from src.clima_model import ClimaResumoDiario

def save_dialy_average_data_clima():

    hoje = datetime.now()
    hoje = datetime(hoje.year, hoje.month, 1)
    rows = get_rows_clima_detalhado(hoje)

    sum_temp = 0
    count_temp = 0
    period_sums = defaultdict(int)
    period_counts = defaultdict(int)

    for row in rows:
        sum_temp += row[1]
        count_temp += 1

        if row[6] in {'manha', 'tarde', 'noite', 'madru'}:
            period_sums[row[6]] += row[5]
            period_counts[row[6]] += 1

    temperatura_media_geral = sum_temp / count_temp if count_temp > 0 else 0

    clima_resumo_diario = {
        "dia":hoje,
        "temperatura_media_geral": temperatura_media_geral,
        "clima_geral_manha": math.floor(period_sums['manha'] / period_counts['manha']) if period_counts['manha'] > 0 else 0,
        "clima_geral_tarde": math.floor(period_sums['tarde'] / period_counts['tarde']) if period_counts['tarde'] > 0 else 0,
        "clima_geral_noite": math.floor(period_sums['noite'] / period_counts['noite']) if period_counts['noite'] > 0 else 0,
        "clima_geral_madru": math.floor(period_sums['madru'] / period_counts['madru']) if period_counts['madru'] > 0 else 0,
    }

    climaResumoObj = ClimaResumoDiario(**clima_resumo_diario)
    if not save_data_clima(climaResumoObj):
        raise Exception("Erro ao tentar salvar resumo diario do clima em 'save_dialy_average_data_clima' no arquivo dags/clima_tempo_diario_compilado.py")

    

with DAG(
    'salvar_resumo_diario_do_clima',
    description='salva o resumo diario do clima na parte da manhã, tarde, noite e madrugada',
    default_args={
        'retries':10
    },
    start_date=datetime.now() - timedelta(days=1),
    schedule_interval='23:58'
) as dag:
    
    salvar_task = PythonOperator(
        task_id = 'salvar_resumo_diario',
        python_callable=save_dialy_average_data_clima
    )

    salvar_task