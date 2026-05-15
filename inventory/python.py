import sqlite3
conn = sqlite3.connect("morphology.db")

# Check columns exist
cur = conn.cursor()
cur.execute("PRAGMA table_info(word_morphology)")
print("Columns:", [row[1] for row in cur.fetchall()])

# Check sample data
rows = conn.execute("""
    SELECT sura, ayah, word, root, morphology_text, grammar_text
    FROM word_morphology 
    WHERE sura=1 AND ayah=2
""").fetchall()
for r in rows:
    print(r)
conn.close()