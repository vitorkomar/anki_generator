import genanki

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

{{#frase_1}}<div class="frase">{{frase_1}}</div>{{/frase_1}}
{{#frase_2}}<div class="frase">{{frase_2}}</div>{{/frase_2}}
{{#frase_3}}<div class="frase">{{frase_3}}</div>{{/frase_3}}""",

        'afmt': """{{FrontSide}}
<hr id=answer>
{{Back}}

{{#frase_1_trad}}<div class="frase trad">{{frase_1_trad}}</div>{{/frase_1_trad}}
{{#frase_2_trad}}<div class="frase trad">{{frase_2_trad}}</div>{{/frase_2_trad}}
{{#frase_3_trad}}<div class="frase trad">{{frase_3_trad}}</div>{{/frase_3_trad}}""",
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

/* Add space *between* frases */
.frase {
  font-family: "Liberation Sans";
  font-size: 20px;
  margin-top: 0.5em;   /* space above each line */
  margin-bottom: 0.5em;/* space below each line */
  line-height: 1.4;
}

/* Optional: tweak translated frases separately if you want */
.frase.trad {
  opacity: 0.95;      /* or leave this out */
}
"""
)

# Example note (fields in the same order as defined above):
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
