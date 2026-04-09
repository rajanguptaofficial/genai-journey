import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true"

try:

    reponse = requests.get(url)

    reponse.raise_for_status()
    data = reponse.json()
    print(data) 

except requests.exceptions.ConnectionError:
    print("No internet")
except requests.exceptions.InvalidURL:
    print("Invalid url")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error : {e}") 
except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")            

except Exception as e:
    print(f"Error: {e}")
    