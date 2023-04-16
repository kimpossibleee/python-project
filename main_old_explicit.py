#main code for execution
import floor as fl, ticket as tk, vehicle as vh, datetime as dt
from os import system, name

class ParkingGarage:

    def __init__(self, all_tickets={"active":{}, "paid":{}}, spaces_remaining = 20):
        self.all_tickets = all_tickets
        self.spaces_remaining = spaces_remaining
        self.sales = 0

    def park(self):
        self.full_lot_check()
        this_plate = input("Please enter your plate number: ")
        if this_plate in self.all_tickets["active"]:
            print("This car already has an active ticket")
            self.main()
        self.add_ticket(tk.Ticket(this_plate, start_time = dt.datetime.now()))

    def add_ticket(self, this_ticket):
        self.all_tickets["active"][this_ticket.plate_num] = this_ticket
        self.spaces_remaining -= 1
        this_ticket.print_ticket()
        self.main()

    def leave_garage(self):
        this_plate = input("Please enter plate number for car leaving: ")
        try:
            self.all_tickets["active"][this_plate].begin_checkout()
        except:
            print("This license plate does not exist in the garage")
            self.main()
        self.spaces_remaining +=1
        self.sales += float(self.all_tickets["active"][this_plate].total)
        self.all_tickets["paid"][this_plate] = self.all_tickets["active"][this_plate]
        del(self.all_tickets["active"][this_plate])
        self.main()

    def full_lot_check(self):
        if self.spaces_remaining < 1:
            print("This lot is full, you'll have to park elsewhere.")
            self.main()

    def leave_check(self):
        if self.all_tickets["active"]:
            self.leave_garage()
        else:
            print("No cars present.")
            self.main()

    def garage_status(self):
        print(f'Number of spots remaining: {self.spaces_remaining}\n')
        if not self.all_tickets["active"]:
            print("No active tickets.")
        else:
            print("Active tickets:")
            for plate, ticket_data in self.all_tickets["active"].items():
                print(f'  License plate: {plate}')
                print(f'    Entry time: {ticket_data.format_start_time}')

    def ticket_history(self):
        if not self.all_tickets["paid"]:
            print("No paid tickets, yet.")
        else:
            print("Paid tickets:")
            for plate, ticket_data in self.all_tickets["paid"].items():
                print(f'  License plate: {plate}')
                print(f'    Entry time: {ticket_data.format_start_time}')
                print(f'    Exit time: {ticket_data.format_end_time}')
                print(f'    Ticket value: ${ticket_data.total:.2f}')
            print(f"\nTotal Sales: ${self.sales:.2f}")
            print("\n______________________________________________")

# The master log is the record that is going to show when you quit the garage.
    def master_log(self):
        print("---MASTER LOG---\n")
        self.garage_status()
        self.ticket_history()
        print("\n")

    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


    def main(self):
        next_action = input("\nDoes the next car wish to 'enter' or 'exit' the parking garage?\n'Status' to view garage spots and tickets info,\n'history' to view paid tickets, or 'quit' to stop managing garage: ").lower()
        self.clear()
        if "enter" in next_action:
            self.park()
        elif "exit" in next_action:
            self.leave_check()
        elif "status" in next_action:
            self.garage_status()
            self.main()
        elif "history" in next_action:
            self.ticket_history()
            self.main()
        elif "quit" in next_action:
            print("Thanks for managing the garage.\n")
            self.master_log()
            return self.all_tickets
        else:
            print("Please enter a vaild key")
            self.main()

startThings = ParkingGarage()
startThings.main()
