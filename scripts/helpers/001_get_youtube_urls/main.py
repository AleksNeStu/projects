from typing import List

import scrapetube

CHANNEL_ID = "CHANNEL-ID"
CHANNEL_URL = "https://www.youtube.com/@user"
PLAYLIST_ID = "PLAYLIST_ID"

def _form_urls(ids: List[str]):
    urls = []
    for c_video in ids:
        # print(f"https://youtu.be/{c_video}", sep="\n")
        #https://www.youtube.com/?feature=youtu.be
        # print(f"https://www.youtube.com/watch?v={c_video}", sep="\n")
        urls.append(f"https://www.youtube.com/watch?v={c_video}")

    return urls


def get_from_channel(channel_url=None):
    if channel_url:
        # Get all videos for a channel
        chanel_videos = list(scrapetube.get_channel(channel_url=channel_url))
        chanel_videos_id = [c_video['videoId'] for c_video in chanel_videos]

        video_urls = _form_urls(chanel_videos_id)
        return video_urls


def get_from_playlist(playlist_id=PLAYLIST_ID):
    if playlist_id:
        # Get all videos for a playlist
        playlist_videos = list(scrapetube.get_playlist(playlist_id=playlist_id))
        playlist_videos_id = [p_video['videoId'] for p_video in playlist_videos]

        video_urls = _form_urls(playlist_videos_id)
        return video_urls

def search(query: str = 'python'):
    # Make a search
    found_videos = list(scrapetube.get_search(query))
    found_videos_id = [f_video['videoId'] for f_video in found_videos]

if __name__ == '__main__':
    chanel_urls = get_from_channel(CHANNEL_URL)
    if chanel_urls:
        with open('chanel_urls.txt', 'w') as f:
            f.write('\n'.join(chanel_urls))

    playlist_urls = get_from_playlist(PLAYLIST_ID)
    if playlist_urls:
        with open('playlist_urls.txt', 'w') as f:
            f.write('\n'.join(playlist_urls))