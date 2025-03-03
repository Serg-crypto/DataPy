import requests


tokenAPI = "Is5E8BS8qS5zdFNx4KEWEScdxUKSclzIusqkZ1dI"
company = "TSLA"


url = "https://api.stockdata.org/v1/data/quote"

 # Parámetros de la solicitud
params = {
    "symbols": company,
    "api_token": tokenAPI
}


try:
    response = requests.get(url, params = params)
    response.raise_for_status()  # Lanza una excepción si el código de estado no es 200
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as http_err:
    # Manejar errores HTTP (4xx, 5xx)
    print(f"Error HTTP: {http_err}")
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")


