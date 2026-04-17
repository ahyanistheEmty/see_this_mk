import time
import sys

def countdown_timer(seconds):
    print(f"Starting countdown for {seconds} seconds...")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("00:00")
    print("Time's up!")

if __name__ == "__main__":
    try:
        user_input = int(input("Enter the time in seconds: "))
        countdown_timer(user_input)
    except ValueError:
        print("Please enter a valid integer for seconds.")
