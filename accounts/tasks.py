from celery import task
# We can have either registered task

@task(name='find_events')
def send_events():
     pass