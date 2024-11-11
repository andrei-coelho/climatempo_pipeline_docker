from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import BigInteger, Integer, Float, Column, DateTime, String, Date

Base = declarative_base ()

class ClimaDetalhado(Base):
    __tablename__ = "clima_detalhado"
    id = Column(BigInteger, primary_key=True)
    temperatura_atual = Column(Float, nullable=False)
    temperatura_minima = Column(Float, nullable=False)
    temperatura_maxima = Column(Float, nullable=False)
    data_hora = Column(DateTime, nullable=False)
    clima = Column(Integer, nullable=False)
    periodo = Column(String(100), nullable=False)


class ClimaResumoDiario(Base):
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    __tablename__ = "clima_resumo_diario"
    id = Column(BigInteger, primary_key=True)
    dia = Column(Date, nullable=False)
    temperatura_media_geral = Column(Float, nullable=False)
    clima_geral_manha = Column(Integer, nullable=False)
    clima_geral_tarde = Column(Integer, nullable=False)
    clima_geral_noite = Column(Integer, nullable=False)
    clima_geral_madru = Column(Integer, nullable=False)