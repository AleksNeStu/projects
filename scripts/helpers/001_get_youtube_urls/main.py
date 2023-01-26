import scrapetube

CHANNEL_ID = "CHANNEL-ID"
CHANNEL_URL = "CHANNEL_URL"
PLAYLIST_ID = "PLAYLIST_ID"

# Get all videos for a channel
chanel_videos = list(scrapetube.get_channel(channel_id=CHANNEL_ID, channel_url=CHANNEL_URL))
chanel_videos_id = [c_video['videoId'] for c_video in chanel_videos]
for c_video in chanel_videos_id:
    # print(f"https://youtu.be/{c_video}", sep="\n")
    #https://www.youtube.com/?feature=youtu.be
    print(f"https://www.youtube.com/watch?v={c_video}", sep="\n")


# Get all videos for a playlist
playlist_videos = list(scrapetube.get_playlist(playlist_id=PLAYLIST_ID))
playlist_videos_id = [p_video['videoId'] for p_video in playlist_videos]

# Make a search
found_videos = list(scrapetube.get_search("python"))
found_videos_id = [f_video['videoId'] for f_video in found_videos]