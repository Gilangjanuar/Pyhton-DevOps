import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Bandung, Indonesia"
dest = "Bekasi, Indonesia"
key = "P513gTGtftsPM68zW8rulP5csuyqrGk6"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)