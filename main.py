import random
import schedule
import time
import os
from datetime import datetime

def load_quotes(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_random_quote(quotes):
    return random.choice(quotes)

def save_daily_quote(quote):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"daily_quote_{today}.txt"

    with open(filename, 'w') as file:
        file.write(f"Your motivational quote for {today}:\n\n{quote}")

    print(f"⏰ Daily motivational quote saved to {filename}")

def daily_quote_task():
    quote = get_random_quote(quotes)
    save_daily_quote(quote)

# Load quotes from file
quotes = load_quotes("motivational_quotes.txt")

# Schedule the job to run daily
schedule.every().day.at("09:00").do(daily_quote_task)  # Runs at 9 AM every day

# Initial run to get a quote immediately
daily_quote_task()

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)