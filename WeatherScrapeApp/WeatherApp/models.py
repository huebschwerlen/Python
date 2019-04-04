from django.db import models
import requests
from bs4 import BeautifulSoup
from WeatherApp.viewmodels import alertViewModel


STATE_CHOICES = (
        ('AK', 'Alaska'),
        ('AL', 'Alabama'),
        ('AR', 'Arkansas'),
        ('AZ', 'Arizona'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DC', 'District of Columbia'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('IA', 'Iowa'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('MA', 'Massachusetts'),
        ('MD', 'Maryland'),
        ('ME', 'Maine'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MO', 'Missouri'),
        ('MS', 'Mississippi'),
        ('MT', 'Montana'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('NE', 'Nebraska'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NV', 'Nevada'),
        ('NY', 'New York'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('PR', 'Puerto Rico'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VA', 'Virginia'),
        ('VI', 'Virgin Islands'),
        ('VT', 'Vermont'),
        ('WA', 'Washington'),
        ('WI', 'Wisconsin'),
        ('WV', 'West Virginia'),
        ('WY', 'Wyoming'),
)
# Create your models here.
class Student(models.Model):
    first_name = models.CharField('First Name', max_length=60)
    last_name = models.CharField('Last Name', max_length=60)
    # state = models.CharField('State Initials', max_length=2)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)



    def __unicode__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.state)

    def __str__(self):
        return "First Name: %s Last Name: %s  State: %s" % (self.first_name, self.last_name, self.state)

    def get_alert(self):
        link = "https://alerts.weather.gov/cap/" + self.state + ".php?x=1"
        page = BeautifulSoup(requests.get(link).content, "html.parser")
        entries = page.find_all("entry")
        vM = alertViewModel(entries[0])

        return vM



    # def get_alert(self):
    #     result = requests.get("https://alerts.weather.gov/cap/{}.php?x=1".format(self.state))
    #     src = result.content
    #     soup = BeautifulSoup(src, 'lxml')
    #     alerts = soup.find('entry')
    #     alertVM = alertVM()
    #     alertVM.summary = alerts.summary.text
    #     alertVM.expires = alerts.find('cap:expires')
    #     alertVM.effective = alerts.find('cap:effective')
    #     # for alert in alerts:
    #     #     alert.find('cap:event')
    #     #     print(alert.find('cap:event'))
    #     return alerts



        # for alerts in soup.find_all('entry'):
        #     expires = alerts.find_all('cap:expires')
        #     return expires


        # for alerts in soup.find_all('entry'):
        #     title = alerts.title
        #     return title
        #
        #     summary = alerts.summary
        #     return summary
        #
        #     effective = alerts.find('cap:effective')
        #     return effective
        #
        #     expires = alerts.find('cap:expires')
        #     return expires
        #
        #     certainty = alerts.find('cap:certainty')
        #     return certainty
        #
        #     area = alerts.find('cap:areadesc')
        #     return area







