import datetime
import time
import winsound

def alarm(Timing):
    altime = datetime.datetime.strptime(Timing, "%I:%M %p")
    
    print(f"Done, alarm is set for {Timing}")

    while True:
        current_time = datetime.datetime.now()
        if current_time.hour == altime.hour and current_time.minute == altime.minute:
            start_time = time.time()  # Record the start time
            while time.time() - start_time < 20:  # Run for 1 minute
                print("Alarm is running")
                winsound.PlaySound('abc', winsound.SND_LOOP)
            break 
        else:
            # Sleep for 1 minute before checking again
            time.sleep(60)
