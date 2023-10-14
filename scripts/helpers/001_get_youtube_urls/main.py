import os
from typing import List, Optional
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse, parse_qs
import scrapetube
from pyyoutube import Api, Playlist
import json
import re
from utils import find_key_values

# Web flow (mandatory) (canonicalBaseUrl)
USER_URL_PART = "programmingwithmosh"  # https://www.youtube.com/@{USER_URL_PART}
# Api flow (optional to make extra assertions)
API_KEY = ""  # https://developers.google.com/youtube/registering_an_application


class YouApi:
    def __init__(self, api_key: str, *args, **kwargs):
        self.api = Api(api_key=api_key, *args, **kwargs)

    def get_ch(self, channel_id: Optional[str] = None, *args, **kwargs) -> str:
        # chs = yt_api.get_channel_info(for_username=USER_NAME)
        chs = self.api.get_channel_info(channel_id=channel_id, *args, **kwargs)
        assert len(chs.items) == 1
        ch_info = chs.items[0].to_dict()
        ch_id = ch_info['id']
        assert channel_id == ch_id
        return ch_id

    def get_ch_pls(self, channel_id: Optional[str] = None, count: Optional[int] = None, *args, **kwargs) -> list[Playlist]:
        # count (int, optional):
        #     The count will retrieve playlist data.
        #     Default is 5.
        #     If provide this with None, will retrieve all playlists.
        ch_pls = self.api.get_playlists(channel_id=channel_id, count=count, *args, **kwargs)
        act_count, exp_count = len(ch_pls.items), ch_pls.pageInfo.totalResults
        assert act_count == exp_count, f"Expected pls count {act_count}, actual pls count {exp_count}"
        return ch_pls.items

    def get_pls_ids(self, channel_id: str = None, *args, **kwargs) -> List[str]:
        ch_pls = self.get_ch_pls(channel_id=channel_id, *args, **kwargs)
        ch_pls_ids = [ch.id for ch in ch_pls]
        return ch_pls_ids


class YouScraper:
    _URL_VIDEO = "https://www.youtube.com/watch?v={video_id}"  # "https://youtu.be/{c_video}"

    def __init__(self, user_url_part: str):
        self.user_url_part = user_url_part
        self.ch_url = f"https://www.youtube.com/@{user_url_part}"
        self.pls_url = f"{self.ch_url}/playlists"
        self._ch_soup = None
        self.ch_id = self.get_ch_id()

    @property
    def ch_soup(self):
        if not self._ch_soup:
            self._ch_soup = self._get_soup(self.ch_url)
        return self._ch_soup

    def pls_soup(self):
        pls_soup = self._get_soup(self.pls_url)
        return pls_soup

    def _get_soup(self, url):
        page = urlopen(url)
        page_html = page.read().decode("utf-8")
        page_soup = BeautifulSoup(page_html, "html.parser")
        return page_soup

    def get_ch_id(self):
        # NOTE: Option to get via browser dev tools
        link_tags = self.ch_soup.find_all(name="link", rel='alternate', type='application/rss+xml')
        assert len(link_tags) == 1
        ch_href = link_tags[0].attrs.get('href')
        channel_id = parse_qs(urlparse(ch_href).query).get('channel_id', [None])[0]
        assert channel_id is not None
        return channel_id

    def get_pls_ids(self, extra_dict_check: bool = False) -> List[str]:
        # NOTE: Option to get via browser dev tools
        pls_soup = self.pls_soup()

        target_sc_id = 'var ytInitialData = '
        pl_tag = "playlistId"
        script_tags = [st for st in pls_soup.find_all("script") if target_sc_id in st.text]
        assert len(script_tags) == 1
        script_tag_str = script_tags[0].text

        js_str = script_tag_str.lstrip(target_sc_id).rstrip(';')
        pl_pattern = r'"playlistId":"(.*?)"'

        pls_ids_req = set(re.findall(pl_pattern, js_str))

        if extra_dict_check:
            # NORE: this part can be skipped
            pls_ids_dict = set()
            # Dict approach
            js_dict = json.loads(js_str)
            pls_ids_dict = set(find_key_values(js_dict, pl_tag))
            # NOTE: Deprecated
            # tabs = js_dict['contents']['twoColumnBrowseResultsRenderer']['tabs']
            # for tab in tabs:
            #     if pl_tag in str(tab):
            #         tabs1 = tab['tabRenderer']['content']['sectionListRenderer']['contents']
            #         for tab1 in tabs1:
            #             if pl_tag in str(tab1):
            #                 tab2 = tab1['itemSectionRenderer']['contents']
            #                 assert len(tab2) == 1
            #                 tabs3 = tab2[0]['shelfRenderer']['content']['horizontalListRenderer']['items']
            #                 for tab3 in tabs3:
            #                     if pl_tag in str(tab3):
            #                         pl_id = tab3.get('gridPlaylistRenderer', {}).get('playlistId')
            #                         if pl_id:
            #                             pls_ids_dict.add(pl_id)
            assert pls_ids_req == pls_ids_dict

        pls_ids = [i for i in pls_ids_req if i.startswith("PLT")]
        return sorted(pls_ids)


    def get_video_urls(self, video_ids: List[str]):
        video_urls = []
        for video_id in video_ids:
            video_urls.append(self._URL_VIDEO.format(video_id=video_id))
        return video_urls

    def ch_info_to_video_ids(self, channel_url=None, **kwargs):
        chanel_videos = list(scrapetube.get_channel(channel_url=channel_url, **kwargs))

        chanel_videos_ids = []
        for c_video in chanel_videos:
            v_id = c_video['videoId']
            chanel_videos_ids.append(v_id)

        return chanel_videos_ids
        # video_urls = self.video_ids_to_video_urls(chanel_videos_ids)
        # return video_urls

    def pls_id_to_video_ids(self, playlist_id: str):
        # Get all videos for a playlist
        playlist_videos = list(scrapetube.get_playlist(playlist_id=playlist_id))
        playlist_videos_ids = [p_video['videoId'] for p_video in playlist_videos]
        return playlist_videos_ids
        # video_urls = self.video_ids_to_video_urls(playlist_videos_id)
        # return video_urls

    def search_video_title_part(self, query: str = 'python'):
        found_videos = list(scrapetube.get_search(query))
        found_videos_ids = [f_video['videoId'] for f_video in found_videos]
        return found_videos_ids

    # #TODO: Ref purpose
    # def get_ch_by_url_username(self, url_username: str):
    #     ch_ids_search = []
    #     chs_search = self.api.search_by_keywords(q=USER_URL_PART, search_type="channel")
    #     for ch in chs_search.items:
    #         ch_ids_search.append(ch.id.channelId)
    #     chs = [ys.api.get_channel_info(channel_id=ch_id) for ch_id in ch_ids_search]


def video_urls_to_file(video_urls: List[str], file_name: str):
    with open(f'{file_name}.txt', 'w') as f:
        f.write('\n'.join(video_urls))


def from_file_to_video_urls(file_name: str):
    with open(f'{file_name}.txt', 'r') as f:
        res = list(f)
        return res


if __name__ == '__main__':
    api_key = API_KEY or os.environ.get('GOOGLE_API_KEY', "")
    api = YouApi(api_key) if api_key else None

    # WEB
    scraper = YouScraper(user_url_part=USER_URL_PART)
    ch_id = scraper.ch_id
    pls_ids_api = []
    pls_ids_sc = scraper.get_pls_ids(extra_dict_check=True)

    # APi
    if api:
        pls_ids_api = api.get_pls_ids(ch_id)
        assert pls_ids_api == pls_ids_sc

    # SAVE RESULTS
