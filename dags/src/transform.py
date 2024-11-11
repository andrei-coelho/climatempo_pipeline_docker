
from datetime import datetime
import math

def transformation_to_data_clima(data):
   
    agora = datetime.now()
    periodo = "noite"

    if 0 <= agora.hour < 6:
        periodo = "madru"
    elif 6 <= agora.hour < 12:
        periodo = "manha"
    elif 12 <= agora.hour < 18:
        periodo = "tarde"

    temperatura = float(data['current']['temp']) - 273.15
    tempo = data['current']['weather'][0]
    clima = 1
    if tempo['main'] == 'Rain':
        clima = 4
    elif tempo['main'] == 'Drizzle':
        clima = 3
    elif tempo['main'] == 'Thunderstorm':
        clima = 5
    elif tempo['main'] == 'Clouds':
        clima = 2
    
    return {
        "temperatura_atual":math.ceil(temperatura * 100) / 100,
        "periodo":periodo,
        "data_hora":agora,
        "clima": clima
    }