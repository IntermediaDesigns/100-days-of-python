import requests
from bs4 import BeautifulSoup
import time
import schedule
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import base64
from email.mime.text import MIMEText
import os.path
import pickle

# Dictionary to store product information
products = {
    "laptop": {
        "url": "https://www.bestbuy.com/site/macbook-air-13-3-laptop-apple-m1-chip-8gb-memory-256gb-ssd-space-gray/5721600.p",
        "current_price": 999.99,
        "desired_price": 899.99
    },
    "headphones": {
        "url": "https://www.bestbuy.com/site/sony-wh-1000xm4-wireless-noise-cancelling-over-the-ear-headphones-black/6408356.p",
        "current_price": 349.99,
        "desired_price": 299.99
    }
}

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = Flow.from_client_secrets_file(
                'credentials.json',
                scopes=SCOPES,
                redirect_uri='urn:ietf:wg:oauth:2.0:oob')

            auth_url, _ = flow.authorization_url(prompt='consent')
            print(f'Please visit this URL to authorize the application: {auth_url}')
            code = input('Enter the authorization code: ')
            flow.fetch_token(code=code)
            creds = flow.credentials

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service

def scrape_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.find('div', {'class': 'priceView-hero-price priceView-customer-price'})
    if price_element:
        price = price_element.find('span', {'aria-hidden': 'true'}).text.strip('$')
        return float(price)
    return None

def send_email(service, product, current_price, desired_price, url):
    sender_email = "intermediadesignsllc@gmail.com"  # Replace with your Gmail address
    receiver_email = "intermediadesignsllc@gmail.com"  # Replace with the email where you want to receive alerts

    subject = f"Price Alert: {product} is now cheaper!"
    body = f"""
    The price for {product} has dropped!

    Current price: ${current_price:.2f}
    Your desired price: ${desired_price:.2f}

    Check it out here: {url}
    """

    message = MIMEText(body)
    message['to'] = receiver_email
    message['from'] = sender_email
    message['subject'] = subject

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    try:
        message = service.users().messages().send(userId="me", body={'raw': raw_message}).execute()
        print(f"Email alert sent for {product}")
    except Exception as e:
        print(f"An error occurred: {e}")

def check_prices(service):
    print("Checking prices...")
    for product, info in products.items():
        print(f"Checking price for {product}...")
        current_price = scrape_price(info['url'])
        if current_price is None:
            print(f"Failed to retrieve price for {product}")
            continue
        print(f"Current price for {product}: ${current_price:.2f}")
        if current_price != info['current_price']:
            print(f"Price changed for {product}")
            products[product]['current_price'] = current_price
            if current_price <= info['desired_price']:
                print(f"{product} is now cheaper than desired price!")
                send_email(service, product, current_price, info['desired_price'], info['url'])
        else:
            print(f"No price change for {product}")
    print("Price check completed")

def main():
    service = get_gmail_service()
    print("Gmail service initialized")

    # Perform an immediate check
    check_prices(service)

    # Schedule daily checks
    schedule.every().day.at("10:00").do(check_prices, service)
    print("Scheduled daily price check at 10:00")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()