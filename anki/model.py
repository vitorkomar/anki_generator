import genanki

# ⚠️ If you want Anki to treat this as the *same* note type,
# replace MODEL_ID below with your real model id (from AnkiConnect).
# Otherwise, pick any unique 32-bit int.
MODEL_ID = 1234567890

model = genanki.Model(
    MODEL_ID,
    'My Custom Note Type',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'frase_1'},
        {'name': 'frase_2'},
        {'name': 'frase_3'},
        {'name': 'frase_1_trad'},
        {'name': 'frase_2_trad'},
        {'name': 'frase_3_trad'},
    ],
    templates=[
        {
        'name': 'Card 1',
        'qfmt': """{{Front}}

        <div style='font-family: "Liberation Sans"; font-size: 20px;'>{{frase_1}}</div>

        <div style='font-family: "Liberation Sans"; font-size: 20px;'>{{frase_2}}</div>

        <div style='font-family: "Liberation Sans"; font-size: 20px;'>{{frase_3}}</div>
        """,
                    'afmt': """{{FrontSide}}

        <hr id=answer>

        {{Back}}
        <div style='font-family: "Liberation Sans"; font-size: 20px;'>{{frase_1_trad}}</div>

        <div style='font-family: "Liberation Sans"; font-size: 20px;'>{{frase_2_trad}}</div>

        <div style='font-family: "Liberation Sans"; font-size: 20px;'>{{frase_3_trad}}</div>
        """,
        }
    ],
    css="""
.card {
    font-family: arial;
    font-size: 20px;
    text-align: center;
    color: black;
    background-color: white;
}
"""
)

# Example note (fill the fields in the SAME order as defined above):
note = genanki.Note(
    model=model,
    fields=[
        'Front text here',           # Front
        'Back text here',            # Back
        'frase 1',                   # frase_1
        'frase 2',                   # frase_2
        'frase 3',                   # frase_3
        'frase 1 tradução',          # frase_1_trad
        'frase 2 tradução',          # frase_2_trad
        'frase 3 tradução',          # frase_3_trad
    ],
)

# # (Optional) Build a deck/package:
# deck = genanki.Deck(9876543210, 'My Deck')
# deck.add_note(note)
# genanki.Package(deck).write_to_file('my_deck.apkg')
