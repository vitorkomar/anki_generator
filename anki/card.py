from .model import model 
import genanki

def generate_card(word, translation, pairs, audio=False):
    if audio:
        note = genanki.Note(
        model=model,
        fields=[
            word,
            translation,
            pairs[0][0]+"<br>[sound:"+pairs[0][0]+".mp3]",
            pairs[1][0]+"<br>[sound:"+pairs[1][0]+".mp3]",
            pairs[2][0]+"<br>[sound:"+pairs[2][0]+".mp3]",
            pairs[0][1],
            pairs[1][1],
            pairs[2][1]
        ]
    )
        
    else:
        note = genanki.Note(
            model=model,
            fields=[
                word,
                translation,
                pairs[0][0],
                pairs[1][0],
                pairs[2][0],
                pairs[0][1],
                pairs[1][1],
                pairs[2][1]
            ]
        )

    return note