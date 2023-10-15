import json
import logging
import os
import re
from abc import abstractmethod
from collections import defaultdict
from typing import List, Optional, Set, Tuple
from collections import Counter
from urllib.parse import urlparse, parse_qs
from urllib.request import urlopen

import scrapetube
from bs4 import BeautifulSoup
from pytube import Channel as ChannelP, Playlist as PlaylistP
from pytube.helpers import uniqueify
from pyyoutube import Api, Playlist, Channel

from utils import find_key_values

logger = logging.getLogger(__name__)


# Web flow (mandatory) (canonicalBaseUrl)
USER_URL_PART = "programmingwithmosh"  # https://www.youtube.com/@{USER_URL_PART}
# Api flow (optional to make extra assertions)
API_KEY = ""  # https://developers.google.com/youtube/registering_an_application
F_CH_VIDEOS = "ch_videos_urls.txt"
F_PLS_VIDEOS = "pls_videos_urls.txt"
F_NO_PLS_VIDEOS = "no_pls_videos_urls.txt"


class ChannelPwPatch(ChannelP):
    # https://patch-diff.githubusercontent.com/raw/pytube/pytube/pull/1409.diff
    @staticmethod
    def _extract_videos(raw_json: str) -> Tuple[List[str], Optional[str]]:
        """Extracts videos from a raw json page

        :param str raw_json: Input json extracted from the page or the last
            server response
        :rtype: Tuple[List[str], Optional[str]]
        :returns: Tuple containing a list of up to 100 video watch ids and
            a continuation token, if more videos are available
        """
        initial_data = json.loads(raw_json)
        # this is the json tree structure, if the json was extracted from
        # html
        try:

            # PATCH!!!
            videos = initial_data["contents"][
                "twoColumnBrowseResultsRenderer"][
                "tabs"][1]["tabRenderer"]["content"][
                "richGridRenderer"]["contents"]
            # PATCH!!!

        except (KeyError, IndexError, TypeError):
            try:
                # this is the json tree structure, if the json was directly sent
                # by the server in a continuation response
                important_content = initial_data[1]['response']['onResponseReceivedActions'][
                    0
                ]['appendContinuationItemsAction']['continuationItems']
                videos = important_content
            except (KeyError, IndexError, TypeError):
                try:
                    # this is the json tree structure, if the json was directly sent
                    # by the server in a continuation response
                    # no longer a list and no longer has the "response" key
                    important_content = initial_data['onResponseReceivedActions'][0][
                        'appendContinuationItemsAction']['continuationItems']
                    videos = important_content
                except (KeyError, IndexError, TypeError) as p:
                    logger.info(p)
                    return [], None

        try:
            continuation = videos[-1]['continuationItemRenderer'][
                'continuationEndpoint'
            ]['continuationCommand']['token']
            videos = videos[:-1]
        except (KeyError, IndexError):
            # if there is an error, no continuation is available
            continuation = None

        # remove duplicates
        return (
            uniqueify(
                list(
                    # PATCH!!!
                    # only extract the video ids from the video data
                    map(
                        lambda x: (
                            f"/watch?v="
                            f"{x['richItemRenderer']['content']['videoRenderer']['videoId']}"
                        ),
                        videos
                    )
                    # PATCH!!!
                ),
            ),
            continuation,
        )


class Common:

    @abstractmethod
    def get_pls_videos_ids_map(*args, **kwargs):
        raise NotImplementedError

    def get_pls_videos_ids(self, pls_ids: Set[str] = None, *args, **kwargs):
        pls_videos_ids_map = self.get_pls_videos_ids_map(pls_ids, *args, **kwargs)
        pls_videos_ids = []
        for pl_videos_ids in pls_videos_ids_map.values():
            pls_videos_ids.extend(pl_videos_ids)

        return set(pls_videos_ids)


class YouApi(Common):
    # https://developers.google.com/youtube/v3/docs/
    # https://sns-sdks.lkhardy.cn/python-youtube/usage/work-with-client/
    # YouTube Data API v3

    def __init__(self, api_key: str, ch_id: str, *args, **kwargs):
        self.api = Api(api_key=api_key, *args, **kwargs)
        self.ch_id = ch_id

    def get_ch(self, *args, **kwargs) -> Channel:
        ch_info = self.api.get_channel_info(channel_id=self.ch_id, *args, **kwargs)
        assert len(ch_info.items) == 1
        ch = ch_info.items[0]
        assert ch.id == self.ch_id
        return ch

    #TODO: Api find duplicates, but sount of set web == list of this serach (set no)
    def get_ch_videos_ids(self, *args, **kwargs) -> Set[str]:
        # https://developers.google.com/youtube/v3/docs/search/list
        def find_unique_ch_videos_ids(exp_count: int):
            # Initialize variables
            unique_video_ids = set()
            next_page_token = None
            total_results = 0  # Track the total number of results

            # Fetch the channel's videos and deduplicate the results
            while True:
                results = self.api.search(
                    # part="id",
                    search_type="video",
                    # maxResults=50,  # Adjust as needed
                    channel_id=self.ch_id,
                    page_token=next_page_token,
                    *args,
                    **kwargs
                )

                for item in results.items:
                    video_id = item.id.videoId
                    if video_id not in unique_video_ids:
                        # Process the video data here
                        unique_video_ids.add(video_id)
                        total_results += 1

                next_page_token = results.nextPageToken
                if not next_page_token or total_results >= 1000:  # Limit the total number of results as needed
                    if exp_count == len(unique_video_ids):
                        break

            return unique_video_ids

        ch_videos = self.api.search(
            # part="id",
            search_type='video',
            limit=50,
            count=1000,
            channel_id=self.ch_id,
            *args,
            **kwargs
        )
        ch_videos_ids = [c_video.id.videoId for c_video in ch_videos.items]
        ch_videos_ids_len = len(ch_videos_ids)

        # TODO: Fix issue with duplicate search result (count is expected but after set applying it's randomly less)
        ch_videos_ids_duplicates = [item for item, count in Counter(ch_videos_ids).items() if count > 1]
        if ch_videos_ids_duplicates:
            ch_videos_ids_unique = find_unique_ch_videos_ids(exp_count=ch_videos_ids_len)
            if len(ch_videos_ids_unique) == ch_videos_ids_len:
                return ch_videos_ids_unique
            else:
                raise ValueError("No unique ch_videos_ids found")

        return set(ch_videos_ids)

    def get_ch_pls(self, channel_id: Optional[str] = None, count: Optional[int] = None, *args, **kwargs) -> list[Playlist]:
        # count (int, optional):
        #     The count will retrieve playlist data.
        #     Default is 5.
        #     If provide this with None, will retrieve all playlists.
        ch_pls = self.api.get_playlists(channel_id=channel_id, count=count, *args, **kwargs)
        act_count, exp_count = len(ch_pls.items), ch_pls.pageInfo.totalResults
        assert act_count == exp_count, f"Expected pls count {act_count}, actual pls count {exp_count}"
        return ch_pls.items

    def get_pls_ids(self, *args, **kwargs) -> Set[str]:
        ch_pls = self.get_ch_pls(channel_id=self.ch_id, *args, **kwargs)
        ch_pls_ids = set([ch_pl.id for ch_pl in ch_pls])
        assert len(ch_pls) == len(ch_pls_ids)
        return ch_pls_ids

    def get_pls_videos_ids_map(self, pls_ids: List[str] = None, count: Optional[int] = None, *args, **kwargs):
        pls_videos_ids_map = defaultdict(list)

        for pl_id in pls_ids:
            pl_videos = self.api.get_playlist_items(playlist_id=pl_id, count=count, *args, **kwargs)
            pl_videos_ids = [pl_video.contentDetails.videoId for pl_video in pl_videos.items]
            pls_videos_ids_map[pl_id].extend(pl_videos_ids)

        return dict(pls_videos_ids_map)


class YouScraper(Common):
    # https://scrapetube.readthedocs.io/en/latest/

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

    def get_pls_ids(self, extra_dict_check: bool = True) -> Set[str]:
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
        pls_ids_set = set(pls_ids)
        assert len(pls_ids_set) == len(pls_ids)
        return pls_ids_set

    def get_ch_videos_ids(self, *args, **kwargs) -> Set[str]:
        ch_videos = list(scrapetube.get_channel(channel_id=self.ch_id, *args, **kwargs))
        ch_videos_ids = set([c_video['videoId'] for c_video in ch_videos])
        assert len(ch_videos_ids) == len(ch_videos)
        return ch_videos_ids

    def get_pls_videos_ids_map(self, pls_ids: List[str] = None, *args, **kwargs):
        pls_videos_ids_map = defaultdict(list)

        for pl_id in pls_ids:
            pl_videos = list(scrapetube.get_playlist(playlist_id=pl_id, *args, **kwargs))
            pl_videos_ids = [pl_video['videoId'] for pl_video in pl_videos]
            pls_videos_ids_map[pl_id].extend(pl_videos_ids)

        return dict(pls_videos_ids_map)


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


class YouDownloader:
    def __init__(self, user_url_part: str):
        self.user_url_part = user_url_part
        self.ch_url = f"https://www.youtube.com/c/{user_url_part}"
        self.ch = self.get_ch()

    def get_ch(self):
        ch = ChannelPwPatch(self.ch_url)
        return ch

    def refresh_ch(self):
        self.ch = self.get_ch()

    # def get_ch_videos_urls(self):
    #
    #
    #     ch_videos_ids = scraper.get_ch_videos_ids()
    #     pls_ids = scraper.get_pls_ids(extra_dict_check=True)
    #     pls_videos_ids = scraper.get_pls_videos_ids(pls_ids)
    #     return ch_videos_ids, pls_videos_ids


def format_video_urls(video_ids: Set[str]):
    video_urls = [f"https://www.youtube.com/watch?v={video_id}" for video_id in video_ids]
    return video_urls

def video_urls_to_file(video_urls: List[str], file_name: str):
    with open(f'{file_name}.txt', 'w') as f:
        f.write('\n'.join(video_urls))


def from_file_to_video_urls(file_name: str):
    with open(f'{file_name}.txt', 'r') as f:
        res = list(f)
        return res


def get_videos_ids(inst):
    ch_videos_ids = inst.get_ch_videos_ids()
    pls_ids = inst.get_pls_ids()
    pls_videos_ids = inst.get_pls_videos_ids(pls_ids)
    return ch_videos_ids, pls_videos_ids, pls_ids


def save_files_w_video_urls(ch_videos_ids: Set[str], pls_videos_ids: Set[str], exp_ch_videos_urls: Set[str] = None):
    # GET DIFF AND SAVE RESULTS
    videos_wo_pl_ids: Set[str] = ch_videos_ids - pls_videos_ids
    videos_ids_map = {
        F_CH_VIDEOS: ch_videos_ids,
        F_PLS_VIDEOS: pls_videos_ids,
        F_NO_PLS_VIDEOS: videos_wo_pl_ids,
    }
    for f_name, videos_ids in videos_ids_map.items():
        videos_urls = format_video_urls(videos_ids)
        if f_name == F_CH_VIDEOS and exp_ch_videos_urls:
            assert exp_ch_videos_urls == set(videos_urls)
        video_urls_to_file(videos_urls, f_name)

def exec_logic(user_url_part: str, use_scrapper_only: Optional[bool] = True):
    # use_web_not_api: True - will be used web to get ch_id, rest of ops will be also web
    # use_web_not_api: False - will be used web to get ch_id, rest of ops will be api
    # use_web_not_api: None - will be used web to get ch_id, rest of ops will be web and api to double checks final result
    scraper = YouScraper(user_url_part=user_url_part)
    downloader = YouDownloader(user_url_part=user_url_part)
    assert scraper.ch_id == downloader.ch.channel_id
    ch_id = scraper.ch_id
    exp_ch_videos_urls = set(downloader.ch.video_urls)

    ch_videos_ids, pls_videos_ids = set(), set()
    if use_scrapper_only:
        ch_videos_ids, pls_videos_ids, pls_ids = get_videos_ids(scraper)
        save_files_w_video_urls(ch_videos_ids, pls_videos_ids)

    else:
        api_key = API_KEY or os.environ.get('GOOGLE_API_KEY', "")
        api = YouApi(api_key, ch_id)
        ch_videos_ids, pls_videos_ids, pls_ids  = get_videos_ids(api)

        if use_scrapper_only is None:
            ch_videos_ids_sc, pls_videos_ids_sc, pls_ids_sc = get_videos_ids(scraper)
            assert ch_videos_ids == ch_videos_ids_sc
            assert pls_videos_ids == pls_videos_ids_sc
            assert pls_ids == pls_ids_sc

    count_ch_videos_ids = len(ch_videos_ids)
    count_pls_videos_ids = len(pls_videos_ids)
    count_diff = count_ch_videos_ids - count_pls_videos_ids
    logger.info("count_ch_videos_ids: %s, count_pls_videos_ids: %s, count_diff: %s", count_ch_videos_ids, count_pls_videos_ids, count_diff)

    save_files_w_video_urls(ch_videos_ids, pls_videos_ids, exp_ch_videos_urls)


if __name__ == '__main__':
    exec_logic(user_url_part=USER_URL_PART, use_scrapper_only=False)