# A simple todoist polybar plugin

It tells you how many tasks you have completed this week, e.g. 
```
7/10 tasks completed this week
```

## Setup
1. Copy your integration key from todoist into a file called auth_token within the same folder as the python script

2. Update you polybar config

```
[module/todoist]
type = custom/script
exec = python ~/.config/polybar/todoist_polybar/todoist_poly.py
click-left = xdg-open https://todoist.com/app
interval = 500
```


