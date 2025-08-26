import pickle 
import streamlit as st 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID  = '80d11324e6024b00a67764645881e38f'
CLIENT_SECRET = 'e65b6e0e26444455a08168aed723f6de'

client_credentials_manager = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret= CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)   

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(song):
    index = df[df['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:7]:
        artist = df.iloc[i[0]].artist
        recommended_music_posters.append(get_song_album_cover_url(df.iloc[i[0]].song, artist))
        recommended_music_names.append(df.iloc[i[0]].song)

    return recommended_music_names, recommended_music_posters

st.header('Music Recommender System')
df = pickle.load(open("df.pkl", "rb"))          # songs dataframe
similarity = pickle.load(open("similarity.pkl", "rb"))   # similarity matrix


music_list = df['song'].values
selected_movie = st.selectbox (
    "Type or select a song from dropdown",
    music_list
)

if st.button('show Recommendation'):
    recommended_music_names,recommended_music_posters= recommend(selected_movie)
    col1,col2,col3,col4,col5,col6 = st.columns(6)
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
    with col2:
        st.text(recommended_music_names[1])   
        st.image(recommended_music_posters[1])
    with col3:
        st.text(recommended_music_names[2])   
        st.image(recommended_music_posters[2])
    with col4:
        st.text(recommended_music_names[3])   
        st.image(recommended_music_posters[3]) 
    with col5:
        st.text(recommended_music_names[4])   
        st.image(recommended_music_posters[4])
    with col6:
        st.text(recommended_music_names[5])   
        st.image(recommended_music_posters[5])               