import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    url = "https://news.ycombinator.com/"
    try:
        print("Attempting to fetch the webpage...")
        response = requests.get(url)
        response.raise_for_status()  
        print("Webpage fetched successfully.")

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        print("HTML parsed successfully.")


        headlines = soup.find_all("span", class_="titleline")
        print(f"Found {len(headlines)} headlines.")

        found_matches = False
        for headline in headlines:
            title = headline.find("a").text
            if "Python" in title or "Replit" in title:
                print(f"Match found: {title}")
                found_matches = True

        if not found_matches:
            print("No headlines containing 'Python' or 'Replit' were found.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the webpage: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("Starting Hacker News scraper...")
    scrape_hacker_news()
    print("Scraper finished.")