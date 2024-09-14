import requests
import json
import os
import openai
from openai.error import OpenAIError

# Set up OpenAI API
openai.api_key = os.environ['OPENAI_API_KEY']

# Set up NewsAPI
newsKey = os.environ['newsapi']
country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"

def get_news():
    result = requests.get(url)
    data = result.json()
    return data['articles'][:5]  # Get top 5 stories

def summarize_article(article_url):
    prompt = f"Summarize the following article in 3 paragraphs: {article_url}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes news articles."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=6
        )
        return response.choices[0].message['content'].strip()
    except OpenAIError as e:
        return f"Error summarizing article: {str(e)}"

def main():
    print("Today's Top 5 News Stories:\n")
    articles = get_news()
    for i, article in enumerate(articles, 1):
        print(f"Story {i}:")
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        print("Summary:")
        summary = summarize_article(article['url'])
        print(summary)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()