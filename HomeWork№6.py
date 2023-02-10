
import sqlite3


conn = sqlite3.connect("students.db")

# Create the table for the students
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hobby TEXT,
    first_name TEXT,
    last_name TEXT,
    birth_year INTEGER,
    homework_score INTEGER
)
""")


students = [
  (1, 'Music', 'Kesha', 'Traktorist', 2000, 8),
  (2, 'Sports', 'Lena', 'Golovach' , 2003, 8),
  (3, 'Reading', 'Vova', 'KimChenPut', 2001, 9),
  (4, 'Gaming', 'Byvshaya', 'Brevno', 1999, 7),
  (5, 'Drawing', 'Penis', 'Dyshilin', 2002, 8),
  (6, 'Writing', 'Idyschii', 'K_Reke', 1998, 10),
  (7, 'Photography', 'Vasya', 'Pupkin', 2000, 11),
  (8, 'Dancing', 'Son', 'MaminoiPodrygi', 2001, 12),
  (9, 'Singing', 'Vania', 'Erohin', 1999, 9),
  (10, 'Cooking', 'Frog', 'Pepe', 2002, 7)
]
conn.executemany("""
INSERT INTO students (hobby, first_name, last_name, birth_year, homework_score)
VALUES (?, ?, ?, ?, ?)
""", students)
conn.commit()


cursor = conn.execute("""
SELECT * FROM students WHERE LENGTH(last_name) > 10
""")
for row in cursor:
    print(row)


conn.execute("""
UPDATE students SET first_name = 'genius' WHERE homework_score > 10
""")
conn.commit()


cursor = conn.execute("""
SELECT * FROM students WHERE first_name = 'genius'
""")
for row in cursor:
    print(row)


conn.execute("""
DELETE FROM students WHERE id % 2 = 0
""")
conn.commit()


conn.close()
