import scrapetube

CHANNEL_ID = "CHANNEL-ID"
CHANNEL_URL = "https://www.youtube.com/@user"
PLAYLIST_ID = "PLAYLIST_ID"

def get_from_channel(channel_url=CHANNEL_URL):
    # Get all videos for a channel
    chanel_videos = list(scrapetube.get_channel(channel_url=channel_url))
    chanel_videos_id = [c_video['videoId'] for c_video in chanel_videos]

    video_urls = []
    for c_video in chanel_videos_id:
        # print(f"https://youtu.be/{c_video}", sep="\n")
        #https://www.youtube.com/?feature=youtu.be
        # print(f"https://www.youtube.com/watch?v={c_video}", sep="\n")
        video_urls.append(f"https://www.youtube.com/watch?v={c_video}")
    return video_urls


def get_from_playlist(playlist_id=PLAYLIST_ID):
    # Get all videos for a playlist
    playlist_videos = list(scrapetube.get_playlist(playlist_id=playlist_id))
    playlist_videos_id = [p_video['videoId'] for p_video in playlist_videos]
    return playlist_videos_id

def search(query: str = 'python'):
    # Make a search
    found_videos = list(scrapetube.get_search(query))
    found_videos_id = [f_video['videoId'] for f_video in found_videos]

if __name__ == '__main__':
    video_urls = get_from_channel()
    with open('r.txt', 'w') as f:
        f.write('\n'.join(video_urls))