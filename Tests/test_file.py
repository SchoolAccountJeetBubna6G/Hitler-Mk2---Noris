
def timer(time_):
    import time
    time_val = time_
    while time_val > 0:
        time_val -= 1
        print('Time remaining:',time_val)
        time.sleep(1)