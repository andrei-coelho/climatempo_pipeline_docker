from src.clima_model import ClimaDetalhado, ClimaResumoDiario

def modelo():
    clima = ClimaDetalhado()
    clima2 = ClimaResumoDiario()
    print("Testando modelos: ", 
        isinstance(clima, ClimaDetalhado)
        and 
        isinstance(clima2, ClimaResumoDiario)
    )