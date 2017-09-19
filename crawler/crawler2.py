import utils
import pickle

class NaverWebtoonCrawler:
    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id
        self.episode_list = list()

    @property
    def total_episode_count(self):
        el = utils.get_webtoon_episode_list(self.webtoon_id)
        return int(el[0].no)

    @property
    def up_to_date(self):
        """
        현재 가지고있는 episode_list가 웹상의 최신 episode까지 가지고 있는지
        :return: boolean값
        """
        if len(self.episode_list) == 0:
            return False
        if self.total_episode_count == int(self.episode_list[0].no):
            return True
        else:
            return False

    def update_episode_list(self, force_update=False):
        """
        self.episode_list에 존재하지 않는 episode들을 self.episode_list에 추가
        :param force_update: 이미 존재하는 episode도 강제로 업데이트
        :return: 추가된 episode의 수 (int)
        """
        if self.up_to_date:
            return 0

        if len(self.episode_list) == 0:
            self.episode_list = utils.get_webtoon_episode_list(self.webtoon_id, 10000)
        recent_episode_list = []
        recent_episode_list += utils.get_webtoon_episode_list(self.webtoon_id)
        page = 1
        while int(self.episode_list[0].no) < int(recent_episode_list[-1].no):
            page += 1
            recent_episode_list += utils.get_webtoon_episode_list(self.webtoon_id, page)

        if force_update:
            self.episode_list = recent_episode_list
            return len(recent_episode_list)

        # force_update 아닐 경우에는 어떻게 할지 고민..
        else:
            episode_number_to_update = int(recent_episode_list[0].no) - int(self.episode_list[0].no)
            self.episode_list = recent_episode_list[:episode_number_to_update] + self.episode_list
            return episode_number_to_update


    def save(self, path=None):
        """
        현재폴더를 기준으로 db/<webtoon_id>.txt 파일에
        pickle로 self.episode_list를 저장
        :return: 성공여부
        """
        filename = 'db/{}.txt'.format(self.webtoon_id)
        try:
            pickle.dump(self.episode_list, open(filename, 'wb'))
            return True
        except:
            return False

    def load(self, path=None):
        """
        현재폴더를 기준으로 db/<webtoon_id>.txt 파일의 내용을 불러와
        pickle로 self.episode_list를 복원
        :return:
        """
        filename = 'db/{}.txt'.format(self.webtoon_id)
        self.episode_list = pickle.load(open(filename, 'rb'))

#crawler1 = NaverWebtoonCrawler('690020')
#crawler1.update_episode_list(True)
#for ep in crawler1.episode_list:
    print(ep)
