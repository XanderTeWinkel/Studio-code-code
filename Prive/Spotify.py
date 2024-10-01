import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotify API credentials
client_id = 'deae65fce131433e9a5877b83d89ddd6'  # Replace with your Client ID
client_secret = '77fa1745a19a42d8a1a8239e6f8f0b61'  # Replace with your Client Secret

# Authentication via Client Credentials Flow
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_track_features(track_name, artist_name_input):      # noqa: PLR0914
    # Search for the track by name and artist
    query = f"track:{track_name} artist:{artist_name_input}"
    results = sp.search(q=query, type='track', limit=1)
    
    # Check if any tracks were found
    if results['tracks']['items']:                          # type: ignore
        track = results['tracks']['items'][0]               # type: ignore
        track_id = track['id']
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        artist_id = track['artists'][0]['id']
        popularity = track['popularity']
        
        # Get audio features for the track
        audio_features = sp.audio_features(track_id)[0]     # type: ignore
        
        # Get artist details to retrieve genre
        artist_info = sp.artist(artist_id)                  # type: ignore
        genres = artist_info['genres']                      # type: ignore
        genres_str = ", ".join(genres) if genres else "Unknown"
        
        # Extract relevant features
        danceability = audio_features['danceability']
        energy = audio_features['energy']
        valence = audio_features['valence']
        tempo = audio_features['tempo']
        acousticness = audio_features['acousticness']
        
        # Print track information and features
        print(f"Track: {track_name} by {artist_name}")
        print(f"Popularity: {popularity}")
        print(f"Genres: {genres_str}")
        print(f"Danceability: {danceability}")
        print(f"Energy: {energy}")
        print(f"Valence: {valence}")
        print(f"Tempo: {tempo} BPM")
        print(f"Acousticness: {acousticness}")
        
        return track_name, artist_name, popularity, genres_str, danceability, energy, valence, tempo, acousticness
    print("Track not found")
    return None
