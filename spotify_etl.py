import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import s3fs

def run_spotify_etl():

    #Spotify Authentication For Api
    client_credentials_manager = SpotifyClientCredentials(client_id="your_client_id", client_secret="your_client_secret")

    #object of Spotify Library and Putting Credentials to it
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    #top 100 Songs Globally Playlist Link
    playlist_link ="https://open.spotify.com/playlist/5ABHKGoOzxkaa28ttQV9sE"

    #Now we want extract id from above link
    playlist_url = playlist_link.split("/")[-1].split("?")[0]
    print(playlist_url)

    data = sp.playlist_tracks(playlist_url)
    data['items']
    #print(data)

    print(len(data['items']))

    print(data['items'][0]['track']['album'])

    #album Dataset
    album_list = []
    for row in data['items']:
        album_id = row['track']['album']['id']
        album_name = row['track']['album']['name']
        album_release_date = row['track']['album']['release_date']
        album_total_tracks = row['track']['album']['total_tracks']
        album_url = row['track']['album']['external_urls']['spotify']
        album_element = {'album_id': album_id,'album_name': album_name,'release_date': album_release_date,'total_tracks': album_total_tracks,'url': album_url }
        album_list.append(album_element)

    #print(album_list)
    album_df = pd.DataFrame.from_dict(album_list)
    #converting To CSV file
    album_df.to_csv("s3://spotify_top_100_tracks/name_it_to_csv_file.csv"")



