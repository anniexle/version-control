import datetime

current_time = datetime.datetime.now()
current_date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

with open("version.md", "w") as f:
    f.write(current_date_time + '\n')

