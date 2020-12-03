import time

def background_task(n):
    delay = 10
    print("Task running")
    time.sleep(delay)
    print(len(n))
    return len(n)

