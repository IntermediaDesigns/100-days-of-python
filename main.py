import os
import requests
import openai
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up API keys
openai.api_key = os.environ['OPENAI_API_KEY']
newsapi_key = os.environ['NEWSAPI_KEY']
spotify_client_id = os.environ['SPOTIFY_CLIENT_ID']
spotify_client_secret = os.environ['SPOTIFY_CLIENT_SECRET']

# Set up Spotify client
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret
))

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}"
    response = requests.get(url)
    data = response.json()
    return data['articles'][:5]  # Get top 5 stories

def summarize_article(article_url):
    prompt = f"Summarize {article_url} in no more than four words."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes news articles."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=10
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error summarizing article: {str(e)}"

def search_spotify(query):
    results = spotify.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'preview_url': track['preview_url']
        }
    return None

def main():
    print("Daily Track Generator\n")
    articles = get_news()

    for i, article in enumerate(articles, 1):
        print(f"Story {i}:")
        print(f"Title: {article['title']}")

        summary = summarize_article(article['url'])
        print(f"Summary: {summary}")

        track = search_spotify(summary)
        if track:
            print(f"Track: {track['name']} by {track['artist']}")
            print(f"Prompt words: {summary}")
            print(f"Preview URL: {track['preview_url']}")
        else:
            print("No matching track found.")

        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()