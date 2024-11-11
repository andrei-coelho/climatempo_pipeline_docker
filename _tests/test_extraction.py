from src.extraction import get_data_wether

def extraction():
    resp = get_data_wether()
    keys = resp.keys()
    print("transformação: ", 
        "temperatura_atual" in keys and 
        "periodo" in keys and
        "clima" in keys 
    )