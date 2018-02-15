"""
조금 쉬운 레스토랑 시뮬레이션 하기 길라잡이.

quiz1.py 에서 작성한 레스토랑을 조금 더 세빌하게 수정합니다.

매 분 마다 레스토랑은 틱을 발생시킵니다.
매 틱 마다 레스토랑은 아래와 같이 출력합니다.
# TODO - 레스토랑 오픈 후 n분이 지났습니다.

3분마다 손님이 한 명씩 도착합니다.
아래와 같이 출력합니다.

# TODO - n번째 손님이 도착했습니다.

해당 손님은 1~10분 후 무작위로 돌아갑니다.

# TODO - n번째 손님이 도착한지 x분 만에 돌아갑니다.


"""

from raven import Client
import random


class Restaurant:
    def __init__(self):

        self.__guest_number = 1
        self.__list = {}
        self.__continue = True

    def run(self):
        turn = 0
        while self.__continue:
            turn += 1
            print(f"레스토랑 오픈 후 {turn}분 지났습니다. ")

            for key, value in self.__list.items():

                value.tick()

                if value.check_tick() is False:
                    del self.__list[key]
                    time = value.get_staying_time()
                    print(f"{key}번째 손님이 도착한지 {time}분만에 돌아갑니다.")
                    break

            if turn % 3 == 0:
                number = self.__guest_number

                self.__list.update({self.__guest_number: Guest()})

                print(f"{number}번째 손님이 도착했습니다")

                self.__guest_number += 1

            if turn == 720:
                self.__continue = False
                print("레스토랑을 종료합니다")



class Guest:

    def __init__(self):
        self.__time = random.randrange(1, 11)
        self.__current_turn = 0
        self.staying_time = 0

    def get_staying_time(self):
        return self.__time

    def tick(self):
        self.__current_turn += 1

    def check_tick(self):
        if self.__time == self.__current_turn:
            return False
        else:
            return True

client = Client(
    'https://65d575d59e1748299f322af362a6b529'
    ':c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')

if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        print("레스토랑을 시작합니다")
        r = Restaurant()
        r.run()

    except Exception:
        client.captureException()