import datetime
import random
import time

from django.db.models import Max, Min

from cookie.models import Cookie
from events.models import Crawl
from my_project.settings import CRAWL_DAEMON_REFRESH_INTERVAL, CRAWL_INTERVAL


def crawler_daemon():
    time.sleep(CRAWL_DAEMON_REFRESH_INTERVAL)
    last_crawl = Crawl.objects.aggregate(Max('date_time'))

    if datetime.datetime.now() - last_crawl >= CRAWL_INTERVAL:
        run_crawl()
        if Crawl.objects.count() > 9:
            oldest_crawl = Crawl.objects.aggregate(Min('date_time'))
            oldest_crawl.delete()
        Crawl.objects.create(datetime.datetime.now())


def run_crawl():
    cookie = Cookie.objects.get()
    selected_cookie = cookie[random.randint(len(cookie))]