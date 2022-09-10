import requests
import json
import time
import re
from colorama import Fore, Style

'''
Если мы вызываем его БЕЗ GET-параметра token, метод заводит новую задачу, а в ответ выдает нам JSON со следующими полями:

* seconds - количество секунд, через сколько задача будет выполнена
* token - тот самый токен, по которому можно получить результат выполнения нашей задачи

Если же вызвать метод, УКАЗАВ GET-параметром token, то мы получим следующий JSON:

* error - будет только в случае, если передать token, для которого не создавалась задача. В этом случае в ответе будет следующая надпись - No job linked to this token
* status - если задача еще не готова, будет надпись Job is NOT ready, если же готова - будет надпись Job is ready
* result - будет только в случае, если задача готова, это поле будет содержать результат '''

'''
1) создавал задачу
2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result '''

new_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job") # 1) создал задачу

count_json = json.loads(new_task.text)
filtr_first_count = {"token": count_json["token"]}
param = {"params": filtr_first_count}

# запрос с token ДО того, как задача готова
task_1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", **param)

st = json.loads(task_1.text)
print('ДО того, как задача готова: ',Fore.YELLOW, st["status"], Style.RESET_ALL)

time_count = count_json["seconds"]
print(f"\nЖдем {time_count} секунд.")
time.sleep(time_count)

task_2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", **param)
st_2 = json.loads(task_2.text)
print('После того, как задача готова: ',Fore.GREEN, st_2["status"], Style.RESET_ALL)
print()
print(task_2.text)

