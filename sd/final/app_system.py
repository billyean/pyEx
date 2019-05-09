import sqlite3
from datetime import date, timedelta


class Appointment:
    def __init__(self, conn):
        self.curs = conn.cursor()

        try:
            self.curs.execute('SELECT * FROM schedule_grommer')
            self.grommers = self.curs.fetchall()

            self.allocations = {g.name: self.__next_two_week__() for g in self.grommers}

            self.curs.execute('SELECT * FROM schedule_service')
            self.services = self.curs.fetchall()

            self.curs.execute('SELECT * FROM schedule_customer')
            self.customers = self.curs.fetchall()

            self.curs.execute('SELECT * FROM schedule_appointment')
            self.appoints = self.curs.fetchall()
        except sqlite3.Error as err:
            print(err)
            raise err

    def add_customer(self, name, pet,credit_card, name_on_card, expired_date, security_code):
        self.curs.execute('INSERT INTO schedule_customer(name, pet, credit_card, name_on_card, expired_date, security_code) VALUES ')

    def __next_two_week__(self):
        today = date.today()
        d = today
        two_week_later = today + timedelta(weeks=2)
        working_dates = []

        while d < two_week_later:
            if d.weekday() < 5:
                working_dates.append(d)

        return working_dates





