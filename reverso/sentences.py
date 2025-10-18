from reverso_context_api import Client
from itertools import islice

def get_sentences_with_word(word, from_lang, to_lang, number_of_sentences):

    client = Client(from_lang, to_lang)
    pairs = client.get_translation_samples(word, cleanup=True)
    pairs = list(islice(pairs, number_of_sentences))

    return pairs