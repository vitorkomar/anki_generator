from reverso_context_api import Client
from itertools import islice

def get_word_translation(word, from_lang, to_lang):

    client = Client(from_lang, to_lang)
    translation = client.get_translations(word)
    translation = list(islice(translation, 3))
    translation = "/ ".join(translation) #separating different options with slash
    return translation