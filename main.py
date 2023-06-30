from generate_queries import generate_queries
from create_playlist import create_playlist

def setup():
    client_id = input("Please enter your Spotify Client ID: ")
    client_secret = input("Please enter your Spotify Client Secret: ")
    redirect_uri = input("Please enter your Spotify Redirect URI: ")

    with open(".env", "w") as f:
        f.write(f"SPOTIPY_CLIENT_ID={client_id}\n")
        f.write(f"SPOTIPY_CLIENT_SECRET={client_secret}\n")
        f.write(f"SPOTIPY_REDIRECT_URI={redirect_uri}\n")

    print("Setup completed. You can now use the program.")


def main():
    confirmation_do_get = input("\nDo you want to get tracks from a website? Press Enter to confirm, or type anything else to cancel: ")

    if confirmation_do_get == "":
        # Call the first script
        generate_queries()

    # Ask the user if they want to continue
    confirmation = input("\nDo you want to create a new playlist? Press Enter to confirm, or type anything else to cancel: ")
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