from generate_queries import generate_queries
from create_playlist import create_playlist
import os

def setup():
    client_id = input("(Setup) Please enter your Spotify Client ID: ")
    client_secret = input("(Setup) Please enter your Spotify Client Secret: ")
    redirect_uri = input("(Setup) Please enter your Spotify Redirect URI (defaults to localhost): ")
    openai_api_key = input("(Setup) Please enter your OpenAI API key: ")

    with open(".env", "w") as f:
        f.write(f"SPOTIFY_CLIENT_ID={client_id}\n")
        f.write(f"SPOTIFY_CLIENT_SECRET={client_secret}\n")
        f.write(f"SPOTIFY_REDIRECT_URI={redirect_uri if redirect_uri != '' else 'http://localhost:8080/'}\n")
        f.write(f"OPENAI_API_KEY={openai_api_key}\n")

    print("Setup completed. You can now use the program. Change the values in the .env file at any time.")


def main():
    confirmation_do_get = input("\n(1) Do you want to parse tracks from a website? Press Enter to confirm, or type anything else to skip this step: ")

    if confirmation_do_get == "":
        # Call the first script
        generate_queries()

    # Ask the user if they want to continue
    confirmation = input("\n(2) Do you want to create a new playlist from a file? Press Enter to confirm, or type anything else to cancel: ")
    if confirmation.lower() == "":
        # Call the second script
        create_playlist()
    else:
        print("Cancelled playlist creation.")
        exit(0)  # this will exit the main() function and end the program


if __name__ == "__main__":
    if not os.path.exists(".env"):
        setup()
    main()