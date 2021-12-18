import time

def countdown(t):
    while t:
        minutes, seconds = divmod(t, 60)
        timer = f"{minutes:02d}:{seconds:02d}"
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Timer completed!")

t = int(input("Enter the time in seconds: "))
countdown(t)
