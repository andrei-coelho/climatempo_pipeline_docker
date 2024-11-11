from src.transform import transformation_to_data_clima


def transformations():
    data = {
        "lat": -23.5507,
        "lon": -46.6334,
        "timezone": "America/Sao_Paulo",
        "timezone_offset": -10800,
        "current": {
            "dt": 1730742452,
            "sunrise": 1730708307,
            "sunset": 1730755304,
            "temp": 296.01,
            "feels_like": 296.31,
            "pressure": 1014,
            "humidity": 75,
            "dew_point": 291.35,
            "uvi": 0.77,
            "clouds": 75,
            "visibility": 10000,
            "wind_speed": 3.6,
            "wind_deg": 30,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ]
        },
    }
    dataF = transformation_to_data_clima(data)
    print("transformação: ", (
        dataF['temperatura_atual'] == 22.87 and
        dataF['periodo'] == 'tarde' and
        dataF['clima'] == 2
    ))