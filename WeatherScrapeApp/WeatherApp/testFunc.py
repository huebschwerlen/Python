import requests
from bs4 import BeautifulSoup

# def get_site(request, state):
#     result = requests.get(f"https://alerts.weather.gov/cap{state}.php?x=1")
#     src = result.content
#     soup = BeautifulSoup(src, 'lxml')
#     # alert = soup.find_all('table', class_= 'entry')
#
#     for table in soup.find_all('table'):
#         #https://stackoverflow.com/questions/38233838/selecting-second-child-in-beautiful-soup
#         alert = table.tbody.select('tr > td')[2].table.tbody.select('tr > td')[2].select('td > table')[2].tbody.tr.text
#
#     return render(request, 'WeatherApp/students-form.html', {'alert': alert})


state = "nd"
result = requests.get("https://alerts.weather.gov/cap/{}.php?x=1".format(state))
src = result.content
soup = BeautifulSoup(src, 'lxml')
alerts = soup.find_all('entry')
for alert in alerts:
    print(alert.text)



#selenium get current url
