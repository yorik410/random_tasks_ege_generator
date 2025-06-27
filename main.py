from sdamgia import SdamGIA
from kompege import KompEGE
import random as rnd

tasks_generate = 5
get_url = True
tasks_count_in_subject = {"math": 19,
                          "phys": 26,
                          "rus": 27,
                          "inf": 27}
subjects = list(tasks_count_in_subject.keys())

sdamgia = SdamGIA()
kompege = KompEGE()

for i in range(tasks_generate):
    subject = rnd.choice(subjects)
    task_number = rnd.randint(1, tasks_count_in_subject[subject])
    try:
        if subject != "inf":
            task_dict = {task_number: 1}  # нужно для библиотеки,чтобы сгенерировать тест из одного задания с нужным номером
            id = sdamgia.generate_test(subject, task_dict)
            if get_url:
                url = f"{sdamgia._SUBJECT_BASE_URL[subject]}/test?id={id}&nt=True&pub=False"
                print(f"{subject}: {url}")
            else:
                print(f"{subject}: {id}")
        elif subject == "inf":
            url = kompege.get_random_task_by_number(task_number if task_number not in [20, 21] else 19, url=get_url)
            print(f"inf: {url}")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Subject: {subject}; Task: {task_number};")

