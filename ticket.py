import datetime
from datetime import datetime as dt
import getpass

import ascii


class Ticket:
    # *** Enter 'start_time' in "HH:MM:SS" military time format ***
    #  'rate' and 'maximum' default is set. <-- useful to add these parameters in the case of special events or holidays
    def __init__(self, plate_num = input("Enter your plate #: "),start_time = datetime.datetime.now(), rate=.001, maximum=24):
        self.plate_num = plate_num
        self.start_time = start_time
        # self.end_time = dummy value that will be replaced when driver pays
        self.end_time = "23:59:59"
        self.rate = rate
        self.maximum = maximum

    # *** Enter 'end_time' in "HH:MM:SS" military time format ***
    def begin_checkout(self):
        card = getpass.getpass('Swipe/Insert/Tap your card: ')
        end_time = datetime.datetime.now()
        self.end_time = end_time

    def calculate_hours(self):
        difference = self.end_time - self.start_time
        return difference.total_seconds()

    def calculate_price(self):
        total = self.calculate_hours() * self.rate
        if total >= self.maximum:
            return self.maximum
        return total

    def print_ticket(self):
        print(ascii.car_art)
        print(ascii.ticket_art)
        print(f"License Plate Number: {self.plate_num}")
        print(f"Enter: {self.start_time}")
        print("Leave: --:--:--")
        print("Rate: $3.00 per hour up to a maximum of $24.00")

    def print_receipt(self):
        print(ascii.receipt_art)
        print(f"License Plate Number: {self.plate_num}")
        print(f"Enter: {self.start_time}")
        print(f"Leave: {self.end_time}")
        print(f"Paid: ${self.calculate_price():.2f}")


# 1) Create Ticket
my_ticket = Ticket()

# 2) Print Initial Ticket
my_ticket.print_ticket()


# 3) Begin Checkout
my_ticket.begin_checkout()

my_ticket.calculate_hours()

# 4) Print Receipt
my_ticket.print_receipt()
