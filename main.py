#!/usr/bin/env python3
import argparse
from anki import model, generate_card, generate_reverse_card
from reverso import get_sentences_with_word, get_word_translation
from audio import generate_sentence_audio
from dictionary import get_german_word_article
import genanki
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("words", nargs="+")
    parser.add_argument("-f", "--from-lang", default="es")
    parser.add_argument("-t", "--to-lang", default="en")
    parser.add_argument("-n", "--number-of-words", default=3)
    parser.add_argument("-a", action="store_true")
    parser.add_argument("-d", "--deck", default="test")
    args = parser.parse_args()

    my_deck = genanki.Deck(
        2059400110,
        args.deck)
    
    media_files = []
    for word in args.words:
        pairs = get_sentences_with_word(word, args.from_lang, args.to_lang, args.number_of_words)
        translation = get_word_translation(word, args.from_lang, args.to_lang)

        word_with_article = word
        if args.from_lang == "de":
            article = get_german_word_article(word)
            if article:
                word_with_article = article + " " + word_with_article

        generate_sentence_audio(word_with_article, args.from_lang)
        for pair in pairs:
            sentence = pair[0]
            generate_sentence_audio(sentence, args.from_lang)

        my_note = generate_card(word_with_article, translation, pairs, audio=True)
        reversed_note = generate_reverse_card(word, translation, pairs, audio=True)


        media_files += [word_with_article + ".mp3" ]+ [
            pair[0]+".mp3" for pair in pairs
        ]

        my_deck.add_note(my_note)
        my_deck.add_note(reversed_note)

    pkg = genanki.Package(my_deck)
    pkg.media_files = media_files
    pkg.write_to_file(args.deck+".apkg")

    for p in Path(".").glob("*.mp3"):
        if p.is_file():
            p.unlink()



if __name__ == '__main__':
    main()