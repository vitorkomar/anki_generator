import duden 

def get_german_word_article(word):
    w = duden.get(word.capitalize())
    if w is None:
        return None
    return w.article