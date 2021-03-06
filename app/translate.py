import requests

from app import current_app


def translate(text, source_language, dest_language) -> str:
    if not current_app.config.get('TRANSLATOR_KEY'):
        return 'Error: the translation service is not configured.'

    url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    trans_option = {
        'key': current_app.config.get('TRANSLATOR_KEY'),
        'lang': f'{source_language}-{dest_language}',
    }
    data = {'text': text}
    response = requests.post(url_trans, params=trans_option, data=data)
    if response.status_code != 200:
        return 'Error: the translation service failed.'
    return response.json().get('text')[0]
