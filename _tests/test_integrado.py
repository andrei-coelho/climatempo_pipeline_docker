from dags.src.clima_model import ClimaDetalhado
from dags.src.extraction import get_data_wether
from dags.src.repositorio import save_data_clima

def get_atual_temperatura():
    data = get_data_wether()
    save_data_clima(ClimaDetalhado(
        data_hora=data['data_hora'],
        clima = data['clima'],
        periodo = data['periodo'],
        temperatura_atual = data['temperatura_atual'],
        temperatura_minima = 0.0,
        temperatura_maxima = 0.0
    ))