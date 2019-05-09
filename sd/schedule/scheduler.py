import sqlite3
from datetime import datetime, date, time, timedelta


class Scheduler:
    """
    A scheduler system for make appointments.
    """
    def __init__(self, conn):
        self.conn = conn
        curs = conn.cursor()

        try:
            self.groomers = ['Rachel', 'Raul', 'Renata', 'Ringo']

            self.wash_services = [('fancy', 45), ('no nonsense', 20)]
            self.cut_services = [('teddy', 45), ('lion', 45), ('summer', 35), ('weed whacker', 20)]

            self.services = {service[0]: service[1] for service in (self.wash_services + self.cut_services)}

            curs.execute('SELECT * FROM schedule_customer')
            self.customers = curs.fetchall()

            # availabilities is a list contains a 2 weeks available service slot start from next weekday.
            # every element in availabilities is a list as well, it contains all available service slot
            # start from 8:00am, the length of the list is 16.
            # in every slot, distinct groomer name will be stored. When one appointment is made; the scheduler will
            # look up the available slot by given date and time. If the slot if full, scheduler raises a error.
            # otherwise rest of groomers will be picked from the slot and register
            self.availabilities = []
            for day in range(10):
                day_slots = []
                for slot in range(16):
                    day_slots.append([])
                self.availabilities.append(day_slots)

            curs.execute('SELECT * FROM schedule_appointment WHERE service_date >= ' + date.today().strftime('%Y-%m-%d'))
            self.appointments = curs.fetchall()
            for appointment in self.appointments:
                groomer = appointment[1]
                service_date = appointment[2]
                service_slot = appointment[4]
                service_date_pos = Scheduler.__available_day_index__(service_date)
                self.availabilities[service_date_pos][service_slot].append(groomer)

        except sqlite3.Error as err:
            print(err)
            raise err

    def lookup_customer(self, customer):
        lookup = [x for x in self.customers if x[0] == customer.lower()]
        if len(lookup) == 0:
            return None
        else:
            return lookup[0]

    def show_all_customers(self):
        return self.customers

    def add_customer(self, name, pet, credit_card, name_on_card, expired_date, security_code):
        try:
            curs = self.conn.cursor()
            curs.execute('INSERT INTO schedule_customer(name, pet, credit_card, name_on_card, expired_date, '
                              'security_code) VALUES (?, ?, ?, ?, ?, ?)',
                         (name.lower(), pet.lower(), credit_card, name_on_card.lower(), expired_date, security_code))
            curs.execute('SELECT * FROM schedule_customer')
            self.customers = curs.fetchall()
            self.conn.commit()
        except sqlite3.Error as err:
            print(f'Database error: {err}')
            self.conn.rollback()

    def available(self):
        # first consecutive slot
        available_slots = []
        for day_index, day_availabilities in enumerate(self.availabilities):
            slot_len = len(day_availabilities)
            for index, slot in enumerate(day_availabilities):
                if index < slot_len - 1 and len(slot) < 4 and len(day_availabilities[index + 1]) < 4:
                    for groomer1 in self.groomers:
                        if groomer1 not in slot:
                            available_slots.append((Scheduler.__index_to_datetime__(day_index, index), groomer1))
                            break
                    for groomer2 in self.groomers:
                        if groomer2 not in day_availabilities[index + 1]:
                            available_slots.append((Scheduler.__index_to_datetime__(day_index, index + 1), groomer2))
                            break
                    return available_slots

        # not consecutive slot
        for day_index, day_availabilities in enumerate(self.availabilities):
            for index, slot in enumerate(day_availabilities):
                if len(slot) < 4:
                    for groomer in self.groomers:
                        if groomer not in slot:
                            available_slots.append((Scheduler.__index_to_datetime__(day_index, index), groomer))
                if len(available_slots) == 2:
                    return available_slots

        return []

    def amount_due(self, customer):
        curs = self.conn.cursor()
        curs.execute('SELECT service, service_date FROM schedule_appointment '
                     'WHERE schedule_appointment.customer_id = ? AND schedule_appointment.paid = FALSE', [customer[0]])
        due_services = curs.fetchall()
        total_due = sum([self.services[s[0]] for s in due_services])
        return total_due

    def make_appointment(self, customer, wash_datetime, wash, cut_datetime, cut):
        wash_index = Scheduler.__available_index__(wash_datetime)
        cut_index = Scheduler.__available_index__(cut_datetime)

        wash_slot = self.availabilities[wash_index[0]][wash_index[1]]
        cut_slot = self.availabilities[cut_index[0]][cut_index[1]]

        if len(wash_slot) == 4:
            raise ValueError("No available wash service at given time")
        if len(cut_slot) == 4:
            raise ValueError("No available cut service at given time")

        wash_groomer = Scheduler.__available_groomer__(self.groomers, wash_slot)
        cut_groomer = Scheduler.__available_groomer__(self.groomers, cut_slot)

        print(f'wash_groomer = {wash_groomer}; cut_groomer = {cut_groomer}')
        self.availabilities[wash_index[0]][wash_index[1]].append(wash_groomer)
        self.availabilities[cut_index[0]][cut_index[1]].append(cut_groomer)

        print(self.availabilities)

        try:
            curs = self.conn.cursor()

            curs.execute('INSERT INTO schedule_appointment(service, groomer, service_date, service_slot, customer_id) '
                              'VALUES (?, ?, ?, ?, ?)',
                              (wash, wash_groomer, wash_datetime.strftime('%Y-%m-%d'), wash_index[1], customer[0]))
            curs.execute('INSERT INTO schedule_appointment(service, groomer, service_date, service_slot, customer_id) '
                              'VALUES (?, ?, ?, ?, ?)',
                              (cut, cut_groomer, cut_datetime.strftime('%Y-%m-%d'), cut_index[1], customer[0]))
            self.conn.commit()
        except sqlite3.Error as err:
            print(f'Database error: {err}')
            self.conn.rollback()

    @staticmethod
    def __available_groomer__(groomers, slot):
        for groomer in groomers:
            if groomer not in slot:
                return groomer

        return None

    @staticmethod
    def __available_index__(service_datetime):
        service_date = service_datetime.date()

        # Every service is 30 minutes
        in_day_pos = (service_datetime - datetime.combine(service_date, time(hour=8))).seconds // 1800

        # No service available from 12pm to 1pm
        if in_day_pos > 8:
            in_day_pos -= 2

        return Scheduler.__available_day_index__(service_date), in_day_pos

    @staticmethod
    def __available_day_index__(service_date):
        today = date.today()
        day_delta = (service_date - today).days
        # Only weekday can make appointment, 5 days a week
        weeks = day_delta // 7
        day_of_week = day_delta % 7
        return weeks * 5 + day_of_week - 1

    @staticmethod
    def __index_to_datetime__(day_index, hour_index):
        today = date.today()
        if today.weekday() == 4:
            next_week_day = today + timedelta(days=3)
        else:
            next_week_day = today + timedelta(days=1)

        week_p = day_index // 5
        week_day_p = day_index % 5
        t_date = next_week_day + timedelta(weeks=week_p, days=week_day_p)

        if hour_index > 8:
            t_time = time(hour=8 + hour_index // 2 + 1, minute=hour_index % 2 * 30)
        else:
            t_time = time(hour=8 + hour_index // 2, minute=hour_index % 2 * 30)

        return datetime.combine(t_date, t_time)
