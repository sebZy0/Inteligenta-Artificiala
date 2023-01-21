import requests
API_KEY = "a86be34867bfdfd933aba050c7d329ec"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Introdu numele orasului:")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)

print(response.status_code)

if response.status_code == 200:
    data = response.json
    print(data)
    vreme = data['weather'][0]['description']
    temperature = round(data['main']['temp'], 2)
    wind = data['wind']['speed']
    print(vreme)
    print(temperature)
    print(wind)
    file_name = "data.txt"

    with open(file_name, "w") as file:
        file.write('data=' + str(data))
else:
    print("Nu exista orasul")
