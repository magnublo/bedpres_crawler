from celery import task
# We can have either registered task

def send_events_for_all_users():
    pass


@task(name='find_events')
def send_events(user=None):
     if user:
         pass
     else:
         send_events_for_all_users()