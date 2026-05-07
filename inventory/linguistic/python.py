import sqlite3
conn = sqlite3.connect("morphology.db")
rows = conn.execute("""
    SELECT sura, ayah, word, part_of_speech, lemma, gender, number, 
           case_type, tense, morphology_text
    FROM word_morphology 
    WHERE sura=1 AND ayah=2
""").fetchall()
for r in rows:
    print(r)
conn.close()