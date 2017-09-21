import utils
import pickle
import os


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
        return len(self.episode_list) == self.total_episode_count

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

        if force_update:
            while int(recent_episode_list[-1].no) != 1:
                page += 1
                recent_episode_list += utils.get_webtoon_episode_list(self.webtoon_id, page)

            self.episode_list = recent_episode_list
            return len(self.episode_list)

        else:
            while int(self.episode_list[0].no) < int(recent_episode_list[-1].no):
                page += 1
                recent_episode_list += utils.get_webtoon_episode_list(self.webtoon_id, page)

            episode_number_to_update = int(recent_episode_list[0].no) - int(self.episode_list[0].no)
            self.episode_list = recent_episode_list[:episode_number_to_update] + self.episode_list
            return episode_number_to_update

    def save(self, path=None):
        """
        현재폴더를 기준으로 db/<webtoon_id>.txt 파일에
        pickle로 self.episode_list를 저장
        :return: 성공여부
        """
        if not path:
            try:
                if not os.path.isdir('db'):
                    os.mkdir('db')
                filename = 'db/{}.txt'.format(self.webtoon_id)
                pickle.dump(self.episode_list, open(filename, 'wb'))
                return True
            except:
                return False
        else:
            try:
                if not os.path.isdir(path):
                    os.mkdir(path)
                filename = '{}/{},txt'.format(path, self.webtoon_id)
                pickle.dump(self.episode_list, open(filename, 'wb'))
                return True
            except:
                return False

    def load(self, path=None, init = False):
        """
        현재폴더를 기준으로 db/<webtoon_id>.txt 파일의 내용을 불러와
        pickle로 self.episode_list를 복원
        :return:
        """
        if not path:
            try:
                filename = 'db/{}.txt'.format(self.webtoon_id)
                self.episode_list = pickle.load(open(filename, 'rb'))
            except FileNotFoundError:
                print('파일이 없습니다.')
        else:
            try:
                filename = '{}/{},txt'.format(path, self.webtoon_id)
                self.episode_list = pickle.load(open(filename, 'rb'))
            except FileNotFoundError:
                if not init:
                    print('파일이 없습니다.')


crawler1 = NaverWebtoonCrawler('690020')
crawler1.load('db23')
for ep in crawler1.episode_list:
    print(ep)


