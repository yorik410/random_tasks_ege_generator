import requests
import random as rnd


class KompEGE:
    def __init__(self):
        self.BASE_URL = "https://kompege.ru"
        self.BASE_API_URL = f"{self.BASE_URL}/api/v1"

    def get_random_task_by_number(self, num: int | str, url: bool = False) -> int | str:
        """
        Searches random task by its number
        :param num:
        task number
        :param url:
        if True: function returns url to task
        if False: function returns task id
        :return:
        task id or url to task
        """
        data = requests.get(f"{self.BASE_API_URL}/task/number/{num}").json()
        task = rnd.choice(data)
        if not url:
            return task["taskId"]
        else:
            return f"{self.BASE_URL}/task?id={task["taskId"]}"


if __name__ == "__main__":
    kompege = KompEGE()
    print(kompege.get_random_task_by_number(1, url=True))