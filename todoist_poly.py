import os
from datetime import datetime, timedelta

from todoist.api import TodoistAPI

cwd = os.path.dirname(__file__)
path = os.path.join(cwd, 'api_token')
with open(path, 'r') as token_file:
    token = token_file.read()

api = TodoistAPI(token)
api.sync()

due_this_week = 0
done = 0
for item in api.items.all():
    due_date = item['due']
    if not due_date:
        continue

    due_datee = item['due']['date']
    completed = item['checked']
    if due_date is not None:
        due_date = due_datee[:15]
        dueTimestamp = datetime.strptime(due_date, '%Y-%m-%d')
        today = datetime.today()
        this_week = today + timedelta(weeks=1)

        if (this_week - dueTimestamp).total_seconds() > 0 and not completed:
            due_this_week += 1

        if (this_week - dueTimestamp).total_seconds() > 0 and completed:
            done += 1

print(str(done) + "/" + str(due_this_week + done) + " tasks completed")
