from src.repositorio import save_data_clima, get_rows_clima_detalhado
from src.clima_model import ClimaDetalhado
from datetime import datetime 


def save_data():
    save_data_clima(ClimaDetalhado(
        temperatura_atual = 20.0,
        temperatura_minima = 13.0,
        temperatura_maxima = 33.4,
        data_hora = datetime.now(),
        clima = 1,
        periodo = "tarde"
    ))


def load_data():
    rows = get_rows_clima_detalhado(
        datetime.now()
    )
    return rows