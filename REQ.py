import requests
from pprint import pprint


marvel_hero = ["Hulk", "Captain America", "Thanos"]


def get_intelligence():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    res = requests.get(url)
    resp = {}
    for s in res.json():
        if s['name'] in marvel_hero:
            resp[s['name']] = s['powerstats']['intelligence']

    intelligence = max(resp.values())
    for key, value in resp.items():
        if value == intelligence:
            result = f"Name: {key} | Intelligence: {value}"
            print(result)

if __name__ == "__main__":
    get_intelligence()

# Могу я пока второе задания отложить , а так в принцепе тему более менее освоил
# Просто и так сильно отстаю , хочу до нового года нагнать 




