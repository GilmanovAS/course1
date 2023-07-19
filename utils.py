import json, random
from classes.basic_word import BasicWord
from config_file import PATH_DATA_JSON


def load_random_word():
    with open(PATH_DATA_JSON, "r", encoding="utf-8") as fp:
        data_json = json.load(fp)
        # print(data_json)
        random.shuffle(data_json)
    return BasicWord(data_json[0]["word"], data_json[0]["subwords"])

# print(load_random_word())
