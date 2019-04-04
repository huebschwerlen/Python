from bs4 import BeautifulSoup


class alertViewModel:
    def __init__(self, entry):
        self.summary = entry.summary.get_text()
        self.expires = entry.find("cap:expires").get_text()
        self.effective = entry.find("cap:effective").get_text()




# from django.db import models
#
# class alertVM(models.Model):
#     summary = ''
#     expires = ''
#     effective = ''
#     managed = False



