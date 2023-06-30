# Spotify Playlistr

## Overview

Spotify Playlistr is a Python script that scrapes a webpage for artist-track combinations and creates a Spotify playlist from them. The script uses Language Models (LLM) to parse and extract the artist-track combinations. The script is powered by Python 3.10, spotipy, beautifulsoup4, LLM, strip-tags, and ttok.

## Installation

### Prerequisites

Ensure you have Python 3.10 installed. If not, you can download it from the official Python website.

### Steps

1. Clone this repository to your local machine using `git clone https://github.com/username/Spotify-Playlistr.git`.

2. Change into the project directory: `cd Spotify-Playlistr`.

3. Install the required dependencies with [PDM](https://pdm.fming.dev/):
    - If you don't have PDM installed, install it using `pip install pdm`.
    - Once PDM is installed, install the dependencies by running `pdm install`.

4. Copy the `.env.example` file and rename it to `.env`. Alternatively, you'll be asked for your secret keys when you firt run the script.

5. Open the `.env` file and add your Spotify client ID and client secret.

### Obtaining Spotify Client ID and Secret

You can obtain your Spotify Client ID and Client Secret from the Spotify Developer Dashboard:

1. Login to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Click on `Create an App`.
3. Follow the prompts to create an app.
4. Once your app is created, you should be able to see your `Client ID` and `Client Secret`.

Copy these into your `.env` file.

### Obtaining OpenAI API Key

You can obtain your OpenAI API key from the OpenAI Developer Dashboard:
1. Go to [OpenAI API keys page](https://platform.openai.com/account/api-keys)
2. create a new secret key, or copy of the existing ones
3. Copy the key into your `.env` file.

## Usage

To use Spotify Playlistr, run the main script using `python main.py` and follow the prompts.

The script will generate a tracklist in the "queries" directory, and you can review the list before continuing.

## Limitations

Please note that using the Language Models (LLM) via the OpenAI API incurs some costs, based on the current pricing and model. The default model is GPT3.5 turbo, and a single request should be less than a few cents. More information can be found on the [OpenAI Pricing page](https://openai.com/pricing).

## License

This project is licensed under the terms of the MIT license.
