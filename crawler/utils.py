from collections import namedtuple
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import requests

Episode = namedtuple('Episode', ['no', 'img_url', 'title', 'rating', 'creation_date'])

def get_webtoon_episode_list(webtoon_id, page=1):
    '''

    :param webtoon_id:
    :return: List of namedtuples that contain information on webtoon that matches id
    '''
    episode_list = []

    param = {'titleId': webtoon_id, 'page': page}
    r = requests.get('http://comic.naver.com/webtoon/list.nhn', params=param)
    source = r.text
    soup = BeautifulSoup(source, "html.parser")

    webtoon_table = soup.select_one('table.viewList')
    tr_list = webtoon_table.find_all('tr', recursive=False)
    for tr in tr_list:
        td_list = tr.find_all('td')
        if len(td_list) < 4:
            continue
        td_thumbnail = td_list[0]
        td_title = td_list[1]
        td_rating = td_list[2]
        td_creation_date = td_list[3]

        url_episode = td_thumbnail.a.get('href')
        parse_result = urlparse(url_episode)
        queryset = parse_qs(parse_result.query)
        no = queryset['no'][0]

        img_url = td_thumbnail.a.img.get('src')
        title = td_title.get_text(strip=True)
        rating = td_rating.strong.get_text(strip=True)
        creation_date = td_creation_date.get_text(strip=True)

        episode = Episode(no=no, img_url=img_url, title=title, rating=rating, creation_date=creation_date)
        episode_list.append(episode)


    return episode_list