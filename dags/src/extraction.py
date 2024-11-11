import requests
from src.transform import transformation_to_data_clima
from util.config import get_api_data 

api_data = get_api_data()
url_extr = api_data['url_extract']
url_extr = url_extr.replace('{key}', api_data['key'])
url_extr = url_extr.replace('{lat}', str(api_data['lat']))
url_extr = url_extr.replace('{lon}', str(api_data['lon']))


def get_data_wether():
    data = requests.get(url_extr)
    data_wether = transformation_to_data_clima(data.json())
    return data_wether


