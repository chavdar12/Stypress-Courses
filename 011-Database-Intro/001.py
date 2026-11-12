# Schema for the ER diagram from the lecture:
# Courses (name, lessons) - taught by 1 Teacher (name, position), a teacher teaches n courses;
# Students (name, study year) m:n Courses via enrollment with a grade;
# Courses m:n Courses - "is required for" (prerequisites).
import sqlite3
import sys

SCHEMA = """
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT
);
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    lessons_count INTEGER CHECK (lessons_count > 0),
    teacher_id INTEGER REFERENCES teachers(id)
);
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    study_year INTEGER CHECK (study_year > 0)
);
CREATE TABLE IF NOT EXISTS enrollments (
    student_id INTEGER NOT NULL REFERENCES students(id),
    course_id INTEGER NOT NULL REFERENCES courses(id),
    grade REAL CHECK (grade BETWEEN 2 AND 6),
    PRIMARY KEY (student_id, course_id)
);
CREATE TABLE IF NOT EXISTS prerequisites (
    course_id INTEGER NOT NULL REFERENCES courses(id),
    required_course_id INTEGER NOT NULL REFERENCES courses(id),
    PRIMARY KEY (course_id, required_course_id),
    CHECK (course_id <> required_course_id)
);
"""


def create(path):
    connection = sqlite3.connect(path)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.executescript(SCHEMA)
    return connection


db = create(":memory:")
db.executescript("""
INSERT INTO teachers VALUES (1, 'Filip Andonov', 'Lecturer');
INSERT INTO courses VALUES (1, 'Python Basics', 10, 1), (2, 'Databases', 8, 1);
INSERT INTO students VALUES (1, 'Maria', 2);
INSERT INTO enrollments VALUES (1, 2, 6);
INSERT INTO prerequisites VALUES (2, 1);
""")
assert db.execute("""
    SELECT s.name, c.name, e.grade, t.name FROM enrollments e
    JOIN students s ON s.id = e.student_id
    JOIN courses c ON c.id = e.course_id
    JOIN teachers t ON t.id = c.teacher_id
""").fetchall() == [("Maria", "Databases", 6.0, "Filip Andonov")]

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "school.db"
    create(path).close()
    print("Schema created in", path)
