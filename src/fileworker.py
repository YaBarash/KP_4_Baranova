import json

from vacancy import JSONWorker
with open('..//data/vacancies.json', 'w') as file:
    file_name =file.dump(file, indent=4, ensure_ascii=False)

