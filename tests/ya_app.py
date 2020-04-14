import requests
import os


# функция перевода текста
def translate_it(text):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    API = 'trnsl.1.1.20200414T142315Z.82f7f234a435ac4f.5c0f9da21d5fd976283bc1c8447d85d38d7c6109'
    
    params = {
        'key': API,
        'text': text,
        'lang': 'en-ru',
    }

    response = requests.get(URL, params=params)
    text = response.json()
    
    return text


if __name__ == '__main__':
    print(translate_it('good'))