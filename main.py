import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import os


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def scrape_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for unwanted in content(["table", "div", "figure", "script", "style"]):
        unwanted.extract()
    text = content.get_text()
    refs = soup.find_all("ol", {"class": "references"})
    references = [ref.get_text() for ref in refs]
    return text, references

def summarize_text(text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Summarize the following text in no more than 3 paragraphs:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text

def main():
    url = input("Paste wiki URL > ")
    print("Scraping Wikipedia article...")
    article_text, references = scrape_wikipedia(url)
    print("Summarizing the article...")
    summary = summarize_text(article_text)
    print("\nSummary:")
    print(summary)
    print("\nReferences:")
    for i, ref in enumerate(references, 1):
        print(f"{i}. {ref}")

if __name__ == "__main__":
    main()