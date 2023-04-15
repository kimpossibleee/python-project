from datetime import datetime
import getpass

import ascii


class Ticket:
    # *** Enter 'start_time' in "HH:MM:SS" military time format ***
    #  'rate' and 'maximum' default is set. <-- useful to add these parameters in the case of special events or holidays
    def __init__(self, plate_num = input("Enter your plate #: "), start_time = input("Enter the check-in time in military format - HH:MM:SS: "), rate=3, maximum=24):
        self.plate_num = plate_num
        self.start_time = start_time
        # self.end_time = dummy value that will be replaced when driver pays
        self.end_time = "23:59:59"
        self.rate = rate
        self.maximum = maximum

    # *** Enter 'end_time' in "HH:MM:SS" military time format ***
    def begin_checkout(self):
        end_time = input("Enter the check-out time in military format - HH:MM:SS: ")
        card = getpass.getpass('Swipe/Insert/Tap your card: ')
        self.end_time = end_time

# Calculate the # of hours driver parked at time of payment, returns hours rounded up
    def calculate_hours(self):
        t1 = datetime.strptime(self.start_time, "%H:%M:%S")
        t2 = datetime.strptime(self.end_time, "%H:%M:%S")
        difference = t2 - t1
        exact_hr = difference.total_seconds()/3600
        # Hours rounded up/down
        round_hr = round(exact_hr)
        return round_hr

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
        print(f"Paid: ${self.calculate_price()}.00")


# 1) Create Ticket
my_ticket = Ticket()

# 2) Print Initial Ticket
my_ticket.print_ticket()

# 3) Begin Checkout
my_ticket.begin_checkout()

# 4) Print Receipt
my_ticket.print_receipt()
