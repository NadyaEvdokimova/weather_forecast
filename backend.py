import requests

API_KEY = 'e2acc7230d23e3157c5fe7596898f7f4'


def get_data(place, forecast_days, kind):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url=url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == 'Temperature':
        filtered_data = [data["main"]["temp"] for data in filtered_data]
    if kind == "Sky":
        filtered_data = [data["weather"][0]["main"] for data in filtered_data]
    return filtered_data


if __name__ == '__main__':
    print(get_data('Budva', 5, 'Sky'))
