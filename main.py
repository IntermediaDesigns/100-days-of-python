import requests
from bs4 import BeautifulSoup
import schedule
import time
from datetime import datetime
from replit import db

# List of topics of interest (converted to lowercase for case-insensitive matching)
topics_of_interest = ["python", "web", "data", "machine learning", "ai", "javascript"]

def scrape_events():
    url = "https://replit.com/community-hub"
    print(f"Fetching data from {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    events = []
    event_divs = soup.find_all("div", {"class": "css-36v8q4"})
    print(f"Found {len(event_divs)} potential event divs")

    for div in event_divs:
        title = div.text.strip()
        link = div.find("a")
        if link and 'href' in link.attrs:
            full_link = "https://replit.com" + link['href'] if link['href'].startswith('/') else link['href']
            events.append((title, full_link))
            print(f"Found event: {title}")

    return events

def filter_events(events):
    filtered_events = []
    for title, link in events:
        if any(topic in title.lower() for topic in topics_of_interest):
            filtered_events.append((title, link))
            print(f"Matched event: {title}")
        else:
            print(f"Unmatched event: {title}")
    return filtered_events

def write_to_file(event=None):
    with open('new_events.txt', 'a') as f:
        if event:
            f.write(f"\nNew event as of {datetime.now()}:\n")
            f.write(f"{event[0]}: {event[1]}\n")
            print(f"New event added to new_events.txt: {event[0]}")
        else:
            f.write(f"\nScraper run at {datetime.now()}, no new matching events found.\n")
            print("No new matching events found, updated new_events.txt")

def job():
    print(f"\nRunning scraper job at {datetime.now()}...")
    all_events = scrape_events()
    filtered_events = filter_events(all_events)

    new_events_found = False
    for event in filtered_events:
        if event[1] not in db:
            db[event[1]] = event[0]  # Store the event in the database
            write_to_file(event)  # Write new event to file
            new_events_found = True

    if not new_events_found:
        write_to_file()  # Write a message saying no new events were found

    print(f"Job completed. Found {len(filtered_events)} events of interest out of {len(all_events)} total events.")

if __name__ == "__main__":
    print("Replit Event Scraper Challenge started.")
    print(f"Looking for topics: {', '.join(topics_of_interest)}")
    print("Running initial job...")
    job()  # Run the job immediately when the script starts

    print("Scheduling future jobs every 6 hours...")
    schedule.every(6).hours.do(job)

    print("Press Ctrl+C to exit.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Script stopped by user.")