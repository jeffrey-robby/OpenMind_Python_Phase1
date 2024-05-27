notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

moyenne = sum(notes) / len(notes)

notes_superieures_a_la_moyenne = [note for note in notes if note >= 10]

print(notes_superieures_a_la_moyenne)