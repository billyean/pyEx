import sqlite3
from datetime import datetime, date, time, timedelta


class Scheduler:
    """
    A scheduler system for make appointments.
    """
    def __init__(self, conn):
        self.curs = conn.cursor()

        try:
            self.grommers = ['Rachel', 'Raul', 'Renata', 'Ringo']

            self.wash_services = [('fancy', 45), ('no nonsense', 20)]
            self.cut_services = [('teddy', 45), ('lion', 45), ('summer', 35), ('weed whacker', 20)]

            self.curs.execute('SELECT * FROM schedule_customer')
            self.customers = self.curs.fetchall()

            self.curs.execute('SELECT * FROM schedule_appointment WHERE service_date >= date(?)', date.today())
            self.appoints = self.curs.fetchall()

            # availabilities is a list contains a 2 weeks available service slot start from next weekday.
            # every element in availabilities is a list as well, it contains all available service slot
            # start from 8:00am, the length of the list is 16.
            # in every slot, distinct groomer name will be stored. When one appointment is made; the scheduler will
            # look up the available slot by given date and time. If the slot if full, scheduler raises a error.
            # otherwise rest of groomers will be picked from the slot and register
            self.availabilities = []
        except sqlite3.Error as err:
            print(err)
            raise err

    def add_customer(self, name, pet,credit_card, name_on_card, expired_date, security_code):
        self.curs.execute('INSERT INTO schedule_customer(name, pet, credit_card, name_on_card, expired_date, '
                          'security_code) VALUES (?, ?, ?, ?, ?, ?)', (name, pet,credit_card, name_on_card,
                                                                       expired_date, security_code))
        self.curs.execute('SELECT * FROM schedule_customer')
        self.customers = self.curs.fetchall()

    def available(self):
        # first consecutive slot
        available_slots = []
        for day_index, day_availibities in enumerate(self.availabilities):
            slot_len = len(day_availibities)
            for index, slot in enumerate(day_availibities):
                if index < slot_len + 1 and len(slot[index]) < 4 and len(slot[index]):
                    for grommer1 in self.grommers:
                        if grommer1 not in slot[index]:
                            available_slots.append((day_index, index, grommer1))
                    for grommer2 in self.grommers:
                        if grommer2 not in slot[index + 1]:
                            available_slots.append((day_index, index + 1, grommer2))
                    return available_slots

        # not consecutive slot
        for day_index, day_availibities in enumerate(self.availabilities):
            for index, slot in enumerate(day_availibities):
                if len(slot[index]) < 4:
                    for grommer in self.grommers:
                        if grommer not in slot[index]:
                            available_slots.append((day_index, index, grommer))
                if len(available_slots) == 2:
                    return available_slots

        return []

    def make_appointment(self, wash_datetime, wash, cut_datetime, cut):
        today = date.today()

        wash_index = Scheduler.__available_index__(wash_datetime)
        cut_index = Scheduler.__available_index__(wash_datetime)

        wash_slot = self.availabilities[wash_index[0]][wash_index[1]]
        cut_slot = self.availabilities[cut_index[0]][cut_index[1]]

        if len(wash_slot) == 4:
            raise ValueError("No available wash service at given time")
        if len(cut_slot) == 4:
            raise ValueError("No available cut service at given time")


    def __next_two_week__(self):
        today = date.today()
        d = today
        two_week_later = today + timedelta(weeks=2)
        working_dates = []

        while d < two_week_later:
            if d.weekday() < 5:
                working_dates.append(d)

        return working_dates

    @staticmethod
    def __available_grommer__(grommers, slot):
        for grommer in grommers:
            if grommer not in slot:
                return grommer

        return None

    @staticmethod
    def __available_index__(service_datetime):
        service_date = service_datetime.date()
        today = date.today()

        day_delta = (service_date - today).days
        # Only weekday can make appointment, 5 days a week
        weeks = day_delta // 7
        day_of_week = day_delta % 7
        day_pos = weeks * 5 + day_of_week - 1

        # Every service is 30 minutes
        in_day_pos = (service_datetime - datetime.combine(service_date, time(hour=8))).seconds // 1800
        print(in_day_pos)
        # No service from 12pm to 1pm
        if in_day_pos > 8:
            in_day_pos -= 2

        return (day_pos, in_day_pos)









