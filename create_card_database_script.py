import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('cards_pool.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Cards (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Strength INTEGER,
                    Color TEXT,
                    Tier TEXT
                )''')
    
    data = [
        ("Newcomer", 1, "teal", "S"),
        ("Make-Up Artist", 1, "green", "A"),
        ("Movie Star", 2, "green", "A"),
        ("Gangster", 2, "green", "A"),
        ("Cat", 3, "green", "A"),
        ("Clown", 1, "yellow", "A"),
        ("Vendor", 2, "yellow", "A"),
        ("Juggler", 2, "yellow", "A"),
        ("Pony", 3, "yellow", "A"),
        ("Butler", 1, "orange", "A"),
        ("Skeleton", 2, "orange", "A"),
        ("Spider", 3, "orange", "A"),
        ("Rescue Pod", 1, "red", "A"),
        ("Shapeshifter", 2, "red", "A"),
        ("A.I.", 2, "red", "A"),
        ("Cow", 3, "red", "A"),
        ("Jester", 1, "blue", "A"),
        ("Stable Boy", 2, "blue", "A"),
        ("Hermit", 2, "blue", "A"),
        ("Pig", 3, "blue", "A"),
        ("Merman", 1, "purple", "A"),
        ("Sailor", 2, "purple", "A"),
        ("Treasure", 2, "purple", "A"),
        ("Parrot", 3, "purple", "A"),
        ("Reporter", 2, "teal", "A"),
        ("Talent", 2, "teal", "A"),
        ("UFO", 3, "red", "B"),
        ("Band", 3, "red", "B"),
        ("Clones", 4, "red", "B"),
        ("Alien", 5, "red", "B"),
        ("Ghost", 1, "orange", "B"),
        ("Teenager", 2, "orange", "B"),
        ("Necromancer", 3, "orange", "B"),
        ("Bat", 5, "orange", "B"),
        ("Mime", 1, "yellow", "B"),
        ("Pyrotechnician", 4, "yellow", "B"),
        ("Clairvoyant", 4, "yellow", "B"),
        ("Rubber Duck", 5, "yellow", "B"),
        ("Cowboy", 3, "green", "B"),
        ("Comic Character", 4, "green", "B"),
        ("Director", 4, "green", "B"),
        ("Lion", 4, "green", "B"),
        ("Blacksmith", 3, "blue", "B"),
        ("Knight", 3, "blue", "B"),
        ("Wizard", 4, "blue", "B"),
        ("Horse", 5, "blue", "B"),
        ("Cook", 2, "purple", "B"),
        ("Navigator", 4, "purple", "B"),
        ("Lifegaurd", 4, "purple", "B"),
        ("Shark", 5, "purple", "B"),
        ("Mascot", 2, "teal", "B"),
        ("Dog", 3, "teal", "B"),
        ("Hologram", 4, "red", "C"),
        ("Sci-Fi Geek", 6, "red", "C"),
        ("Slime", 7, "red", "C"),
        ("Vampire", 4, "orange", "C"),
        ("Vacuum Cleaner", 5, "orange", "C"),
        ("Werewolf", 7, "orange", "C"),
        ("Illusionist", 5, "yellow", "C"),
        ("Bumper Car", 6, "yellow", "C"),
        ("Teddy Bear", 7, "yellow", "C"),
        ("Heroine", 5, "green", "C"),
        ("T-Rex", 7, "green", "C"),
        ("Villian", 10, "green", "C"),
        ("Bard", 4, "blue", "C"),
        ("Prince", 5, "blue", "C"),
        ("Dragon", 7, "blue", "C"),
        ("Siren", 6, "purple", "C"),
        ("Kraken", 7, "purple", "C"),
        ("Submarine", 9, "purple", "C"),
        ("Champion", 4, "teal", "C"),
        ("Fan-Bus", 6, "teal", "C")
    ]
    
    cursor.executemany("INSERT INTO Cards (Name, Strength, Color, Tier) VALUES (?, ?, ?, ?)", data)

    conn.commit()

    cursor.execute("SELECT * FROM Cards")
    rows = cursor.fetchall()

    for row in rows:
        print(row[1:4])

    conn.close()