from datetime import datetime
import os
import requests

succes_file = open('file_log/access.log', "a")
error_file = open('file_log/error.log', "a")


class GetInfo:
    def __init__(self, url):
        self.url = url

    def show_object(self):
        try:
            URL = self.url
            response = requests.get(URL)
            PB = response.json()

            succes_file.write(f"| {os.getlogin()} | {datetime.today().strftime('%d.%m.%Y %H:%M:%S')}\
        | {str(response.status_code)} {str(response.reason)} Operation success!\n")
            return(PB)
        except Exception as ex:
            error_file.write(f"| {os.getlogin()} | {datetime.today().strftime('%d.%m.%Y %H:%M:%S')}\
        | {str(response.status_code)} {str(response.reason)} Operation failed!\n")
        finally:
            succes_file.close()
            error_file.close()


us = GetInfo(
    'https://api.privatbank.ua/p24api/exchange_rates?json&date=20.06.2021')
print(us.show_object())
