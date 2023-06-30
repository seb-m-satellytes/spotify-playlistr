import subprocess
import datetime
from bs4 import BeautifulSoup
import requests
import re
import os

def generate_queries():
    load_dotenv()

    # Use environment variables
    openai_api_key = os.getenv("OPENAI_API_KEY")

    def fetch_web_page(url):
        """ Fetch the content of the web page. """
        print(f'Fetching {url}...')
        try:
            response = requests.get(website_url)
            response.raise_for_status()  # this will raise an exception if the response indicates an error
        except requests.exceptions.RequestException as e:
            print(f"Error fetching web page: {e}")
            exit(1)

        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string

        return soup, title

    def convert_title(title):
        """ Convert title to kebab-case """
        title = re.sub(r"[^\w\s]", "", title)  # Remove punctuation
        title = re.sub(r"\s+", "-", title)  # Replace spaces with hyphens
        title = title.lower()  # Convert to lowercase
        return title

    def prepare_filename(title):
        """ Prepare filename with today's date, the title, and a unique identifier """
        today = datetime.date.today().isoformat()
        existing_files = os.listdir("queries")
        for i in range(1, len(existing_files) + 2):
            filename = f"{today}-{title}-{i}.txt"
            if filename not in existing_files:
                break
        return filename

    def curl_and_generate_pairs(website_url, filename, html_class):
        """ Curl the URL, strip the tags and extract artist-track pairs """
        command = f'curl -s {website_url}'
        if html_class:
            command += f' | strip-tags {html_class} -m'
        if token_length:
            command += f' | ttok -t {token_length}'
        command += f' | llm --key {openai_api_key} --model gpt-3.5-turbo-16k-0613 --system "Find relevant combinations of artist and track from the following text and return them as a list of \'trackname artist:artistname\' combinations. Do not use ordered or unordered list indicators, simple put each item on a new line. Details: Given scraped input that contains several artist and song names optionally in any HTML tags. Do not repeat the artist name. Example input: \'I love the song Yellow Submarine by The Beatles\' or \'Have you heard of Ocean Eyes by Billie Eilish?\' or \'<a href="https://darkestescort.bandcamp.com/album/feast-in-time-of-plague?ref=heavyblogisheavy.com">Feast in Time of Plague by Darkest Escort</a> \'. Example output: \'Yellow Submarine artist:The Beatles\', \'Ocean Eyes artist:Billie Eilish\', \'Feast in Time of Plague artist:Darkest Escort\'."'
        print("Fetch page and generate pairs...")

        # Execute the command
        result = subprocess.run(command, shell=True, capture_output=True)

        # Write the artist-song pairs to a file
        with open("queries/" + filename, 'w') as f:
            f.write(result.stdout.decode())
        print(f"Written artist-song pairs to queries/{filename}")

    # Step 1: Ask for website URL and optional HTML class
    website_url = input("Please enter the website URL: ")
    html_class = input("Please enter an optional HTML Query Selector (press Enter to skip): ")
    token_length = input("Please enter a maximum token length (press Enter to skip):")

    soup, title = fetch_web_page(website_url)

    title = convert_title(title)
    filename = prepare_filename(title)

    curl_and_generate_pairs(website_url=website_url, filename=filename, html_class=html_class)
