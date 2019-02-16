## BCE 5.1: Team Exercise

Code: [BCE_5_1.py](./BCE_5_1.py)

## BCE 5.2: Team Exercise

Code: [BCE_5_2.py](./BCE_5_2.py)

This exercise is based on the SQL, DB-API, and SQLite sections of chapter 8 (pp. 198-202). As shown in the text, the version of the DBMS that comes with Python 3 is sqlite3.

Copy the sqlite3 database ‘BCE_database.db’ from the files section of Canvas for this course. 

You are being given the database for this exercise, so you will focus on SQL commands 

Use Atom (or another code editor) to create the Python code needed to do the following tasks. Include a comment before the code statements that accomplish each task. Save the code to the file ‘BCE_5_2.py’. When done, upload this file to Canvas to your exercise team’s space for this assignment.

NOTE: All of these things can be accomplished in other ways, with other tools, but you are to write Python code to do them.

HINT: For basic interactions with SQLite, the sample code in the text provides a useful model, but there are quite a few basic tutorials available online.

1. Show the values of all of the fields in the table ‘Trainer’.
 
2. Add the following new trainers to this table.

    | id  | name   | Email          |
    | --- | ------ | --------------- |
    | 7   | Stefan | stefan@mpc.com  |
    | 8   | Ping   | Yi25@mystyle.com|
 
3. Remove the trainers who have the email, ‘muscly@workU.org’.
 
4. Show the values of all of the fields in the table ‘Trainer’ again.
 
5. Show the values of all of the fields in the table ‘Skill’ in descending order.
 
6. Add the following new skills to this table.

    | id   | name         |
    | ---- | -------------|
    | 9    | Aqua Aerobics|
    | 10   | U-Jam        |
    
7. Show the values of all of the fields in the table ‘Skill’ again.
 
8. Show the values of all of the fields in the table ‘Lesson’.
 
8. Add the following new lessons (i.e., skills that trainers can teach) to this table.

    | trainer_id | skill_id|  rate|
    | ---------- | ------- | ---- |
    | 7          |  9      | 17.00|
    | 8          |  2      | 28.50|
    | 8          | 10      | 12.00|
    
10. Remove any lessons that have a rate less than 15.00.
 
11. Show the values of all the fields in the table ‘Lesson’ again.
 
12. Show the values of name (from ‘Trainer’), name (from ‘Skill’), and rate (from ‘Lesson’). Your result should look something like the following.
 

(HINT: You’ll need to JOIN the tables together. If you need to, locate a basic tutorial on

SQL and read about many-to-many JOINing.)

[('Jane', 'pilates', 15), ('Jane', 'Zumba', 20), ('Zoe', 'free weights', 35), ('Zoe', 'pilates', 17.5), ('Zoe', 'Zumba', 22), ('Sue', 'free weights', 31.5), ('Sue', 'pilates', 23.5), ('Bart', 'spinning', 21), ('Bart', 'Peak 10', 18.5), ('Conni', 'Peak 10', 19), ('Conni', 'Total Knockout', 20.5), ('Stefan', 'Aqua aerobics', 17), ('Ping', 'pilates', 28.5)]