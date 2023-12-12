'''
Scheduler to run the web scraping daily we can also use it to call the script to refresh the model daily.
'''
# You should use a chronos or chorontab program instead of a while loop
#* * * * * python web_scraper.py

import schedule
import time
import subprocess

def my_task():
    subprocess.run(['python', 'web_scraper.py'])

if __name__ == "__main__":

    # Schedule the task to run every day at 3 AM
    schedule.every().day.at("12:00").do(my_task)

    # Keep the script running to execute scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)
