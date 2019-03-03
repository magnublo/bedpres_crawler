from threading import Thread

from django.apps import AppConfig
from events import crawler

def start_daemon():
    crawler.crawler_daemon()

class MyAppConfig(AppConfig):

    name = 'my_project'
    verbose_name = "Bedpres crawler"
    def ready(self):
        thread = Thread(target=start_daemon)
        thread.start()




