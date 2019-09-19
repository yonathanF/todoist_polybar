import os
from datetime import datetime, timedelta

from todoist.api import TodoistAPI

cwd = os.path.dirname(__file__)
path = os.path.join(cwd, 'api_token')
with open(path, 'r') as token_file:
    token = token_file.read()


def process(api):
    """
    :api: the todoist api
    :returns: None. Prints to STD
    """
    due_today = 0
    for item in api.items.all():
        due_date = item['due']
        if not due_date:
            continue

        due_datee = item['due']['date']
        completed = item['checked']
        if due_date is not None:
            due_date = due_datee[:15]
            dueTimestamp = datetime.strptime(due_date, '%Y-%m-%d')
            tomorrow = datetime.now() + timedelta(1)
            midnight = datetime(year=tomorrow.year,
                                month=tomorrow.month,
                                day=tomorrow.day,
                                hour=0,
                                minute=0,
                                second=0)
            if midnight > dueTimestamp and not completed:
                due_today += 1

    print("[" + str(due_today) + " tasks left]")


try:
    api = TodoistAPI(token)
    api.sync()
    process(api)
except:
    print("[No access]")
