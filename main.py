from flask import Flask, render_template, request, redirect, url_for
import requests
import os
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

def get_access_token():
    clientID = os.environ['CLIENT_ID']
    clientSecret = os.environ['CLIENT_SECRET']
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type":"client_credentials"}
    auth = HTTPBasicAuth(clientID, clientSecret)
    response = requests.post(url, data=data, auth=auth)
    return response.json()["access_token"]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    print("Search route accessed")
    if request.method == 'POST':
        year = request.form['year']
        offset = request.form.get('offset', type=int, default=0)
    else:  # GET request
        year = request.args.get('year')
        offset = request.args.get('offset', type=int, default=0)

    print(f"Year: {year}, Offset: {offset}")

    if not year:
        return redirect(url_for('index'))

    try:
        access_token = get_access_token()
        print(f"Access token obtained: {access_token[:10]}...")

        url = "https://api.spotify.com/v1/search"
        headers = {'Authorization': f'Bearer {access_token}'}
        search = f"?q=year:{year}&type=track&limit=10&offset={offset}"
        fullURL = f"{url}{search}"
        print(f"Full URL: {fullURL}")

        response = requests.get(fullURL, headers=headers)
        print(f"Response status code: {response.status_code}")

        if response.status_code != 200:
            print(f"Error response: {response.text}")
            return f"Error from Spotify API: {response.status_code}"

        tracks = response.json()["tracks"]["items"]
        print(f"Number of tracks found: {len(tracks)}")

        songs = []
        for track in tracks:
            song = {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'preview_url': track['preview_url']
            }
            songs.append(song)

        return render_template('results.html', songs=songs, year=year, offset=offset)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)