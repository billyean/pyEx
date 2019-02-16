import sqlite3
from os import path
import shutil


def main():
    # Copy backup db
    if path.lexists('BCE_database.db.bak'):
        shutil.copy('BCE_database.db.bak', 'BCE_database.db')
    shutil.copy('BCE_database.db', 'BCE_database.db.bak')

    conn = sqlite3.connect('BCE_database.db')
    curs = conn.cursor()

    # Show the values of all of the fields in the table ‘Trainer’.
    curs.execute('SELECT * from Trainer')
    trainers = curs.fetchall()
    print(trainers)
    # Add two lines to Trainer.
    curs.execute("INSERT INTO Trainer VALUES(7, 'Stefan', 'stefan@mpc.com')")
    curs.execute("INSERT INTO Trainer VALUES(8, 'Ping', 'Yi25@mystyle.com')")
    # Remove the trainers who have the email, ‘muscly@workU.org’.
    curs.execute("DELETE FROM Trainer WHERE email='muscly@workU.org'")
    curs.execute('SELECT * from Trainer')
    trainers = curs.fetchall()
    print(trainers)

    curs.execute('SELECT * from Skill ORDER BY id DESC')
    skills = curs.fetchall()
    print(skills)
    curs.execute("INSERT INTO Skill VALUES(9, 'Aqua Aerobics')")
    curs.execute("INSERT INTO Skill VALUES(10, 'U-Jam')")
    curs.execute('SELECT * from Skill ORDER BY id DESC')
    skills = curs.fetchall()
    print(skills)

    curs.execute('SELECT * from Lesson')
    lessons = curs.fetchall()
    print(lessons)
    curs.execute("INSERT INTO Lesson VALUES(7,  9, 17.00)")
    curs.execute("INSERT INTO Lesson VALUES(8,  2, 28.50)")
    curs.execute("INSERT INTO Lesson VALUES(8, 10, 12.00)")
    curs.execute("DELETE FROM Lesson WHERE rate < 15.00")
    curs.execute('SELECT * from Lesson')
    lessons = curs.fetchall()
    print(lessons)

    curs.execute('SELECT Trainer.name, Skill.name, Lesson.rate from Trainer, Skill, Lesson where Trainer.ID = Lesson.trainer_id AND Skill.id = Lesson.skill_id')
    trainer_skill_rates = curs.fetchall()
    print(trainer_skill_rates)


if __name__ == "__main__":
    main()