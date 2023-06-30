import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re
from dotenv import load_dotenv
import inquirer

def create_playlist():
    # Load environment variables from .env file
    load_dotenv()

    # Use environment variables
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    redirect_url = os.getenv("SPOTIFY_REDIRECT_URL")


    def choose_file():
        # List all files in the "queries" directory
        files = sorted(os.listdir("queries"), reverse=True)

        # If there are no files, print an error message and exit
        if not files:
            print("No files found in the 'queries' directory. Please generate a query file first.")
            exit(1)

        questions = [
            inquirer.List('choice',
                          message="(2) Please select a file",
                          choices=files),
        ]

        answers = inquirer.prompt(questions)

        # Get the selected filename
        return answers['choice']


    def get_title(filename):
        # Extract the title from the filename and convert to normal casing
        title = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", filename)  # Remove date
        title = re.sub(r"-\d+\.txt$", "", title)  # Remove unique identifier
        title = title.replace("-", " ")  # Replace hyphens with spaces
        return title.title()  # Convert to title case

    def search_tracks(artist_track_pairs):
    # Step 6: Search for tracks and add them to results
        track_ids = []
        track_details = []
        for pair in artist_track_pairs:
            results = sp.search(q=pair, type='track', limit=1)
            tracks = results['tracks']['items']
            if tracks:
                track = tracks[0]
                track_ids.append(track['id'])
                track_details.append(f"{track['name']} by {track['artists'][0]['name']}")

        # Display the found tracks to the user
        print("\n(2) Found the following tracks:")
        for i, detail in enumerate(track_details):
            print(f"{i+1}. {detail}")

        return track_ids

    def create_playlist(track_ids, user_id, playlist_name):
        # Ask for confirmation
        confirmation = input("\n(2) Do you want to create a playlist with these tracks? Press Enter to confirm, or type anything else to cancel:")
        if confirmation.lower() != "":
            print("Cancelled playlist creation.")
            exit(0)

        # Create the playlist and add the tracks
        playlist = sp.user_playlist_create(user_id, playlist_name, public=False)
        sp.playlist_add_items(playlist['id'], track_ids)

        # Step 7: Return the playlist URL
        print("Success! 🥳 Created playlist:", playlist['external_urls']['spotify'])
    filename = choose_file()
    title = get_title(filename)

    # Step 3: Read the file into a list of artist-song pairs
    with open("queries/" + filename, 'r') as f:
        artist_track_pairs = [line for line in f if line.strip()]


    # Step 4: Ask for the playlist name
    playlist_name = input(f"(2) Please enter the playlist name (press Enter for to accept suggestion '{title}'): ")
    playlist_name = playlist_name or title

    # Step 5: Authenticate with Spotify API and create the playlist
    scope = "playlist-modify-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url, scope=scope))
    user_id = sp.current_user()["id"]

    track_ids = search_tracks(artist_track_pairs=artist_track_pairs)

    create_playlist(track_ids=track_ids, user_id=user_id, playlist_name=playlist_name)