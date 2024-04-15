import datetime
now = datetime.datetime.now()
# Calculate the time 15 seconds ahead
future_time = now + datetime.timedelta(seconds=15)
future_time_str = future_time.strftime('%H:%M')
