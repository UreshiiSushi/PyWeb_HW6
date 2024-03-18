-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(30)
);

-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(30),
  group_id INT,
  FOREIGN KEY (group_id) REFERENCES groups(id)
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(30)
);

-- Table: studyes
DROP TABLE IF EXISTS studyes;
CREATE TABLE studyes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(30),
  teacher_id INT,
  FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

-- Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  grade INT,
  date DATE,
  student_id INT,
  study_id INT,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (study_id) REFERENCES studyes(id)
);