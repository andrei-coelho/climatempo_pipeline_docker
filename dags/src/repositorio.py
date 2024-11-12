from src.clima_model import *
from util.config import get_session
from datetime import datetime, timedelta 
from logging import getLogger
from typing import Union

logger = getLogger()

def save_data_clima(clima: Union[ClimaDetalhado, ClimaResumoDiario]) -> bool:
    Session = get_session()
    session = Session()
    try:
        session.add(clima)
        session.commit()
    except Exception as e:
        session.rollback() 
        raise Exception(f"Erro ao tentar armazenar clima usando 'save_data_clima' do repositorio: {e}")
    finally:
        session.close()

def get_rows_clima_detalhado(dia:DateTime):
    
    Session = get_session()
    session = Session()
    
    dia_inicio = datetime.combine(dia, datetime.min.time())
    dia_fim = datetime.combine(dia, datetime.max.time())

    res = session.execute("select * from clima_detalhado where data_hora >= :dia_inicio and data_hora <= :dia_fim ", {
        "dia_inicio":dia_inicio,
        "dia_fim":dia_fim
    })

    registros = res.fetchall()
    session.close()
    return registros 