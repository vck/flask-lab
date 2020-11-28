
def background_task(n):
    delay = 2
    print("Task running")
    time.sleep(delay)
    print(len(n))
    return len(n)

