#!/usr/bin/env python3

import os
import re
import argparse
from googleapiclient.discovery import build

class YouTubeAPI:
    def __init__(self, api_key):
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_channel_id(self, channel_name):
        try:
            response = self.youtube.search().list(
                part="snippet",
                q=channel_name,
                type="channel",
                maxResults=1
            ).execute()

            if response["items"]:
                return response["items"][0]["snippet"]["channelId"]
            else:
                print("Channel not found.")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_channel_playlists(self, channel_id, max_results=50):
        try:
            response = self.youtube.playlists().list(
                part="snippet,contentDetails",
                channelId=channel_id,
                maxResults=max_results
            ).execute()

            playlists = [
                {
                    "title": item["snippet"]["title"],
                    "url": f"https://www.youtube.com/playlist?list={item['id']}"
                }
                for item in response.get("items", [])
            ]

            return playlists
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

class YouTubeChannel:
    def __init__(self, url):
        self.url = url
        self.name = self.extract_channel_name()

    def extract_channel_name(self):
        match = re.search(r'@([A-Za-z0-9_-]+)', self.url)
        if not match:
            raise ValueError("Invalid channel URL")
        return match.group(1)

def main(api_key, channel_url):
    try:
        youtube_api = YouTubeAPI(api_key)
        youtube_channel = YouTubeChannel(channel_url)
        channel_id = youtube_api.get_channel_id(youtube_channel.name)
        if channel_id:
            playlists = youtube_api.get_channel_playlists(channel_id)
            for playlist in playlists:
                print(playlist['url'])
    except ValueError as e:
        print(e)

CHANEL_URL = 'https://www.youtube.com/@Scienide1995_Deep_and_Dub'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get YouTube channel playlists.')
    parser.add_argument('channel_url', type=str, nargs='?', default=CHANEL_URL, help='The URL of the YouTube channel')
    args = parser.parse_args()

    api_key = os.getenv('YOUTUBE_API_KEY')
    main(api_key, args.channel_url)
