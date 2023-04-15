#main code for execution
# import floor as fl
# import parking_lot as pl 
# import ticket as tk
# import vehicle as vh

class ParkingGarage:

    def __init__(self, all_tickets={"active":{}, "paid":{}}, spaces_remaining = 20):
        self.all_tickets = all_tickets
        self.spaces_remaining = spaces_remaining

    def park(self):
        self.full_lot_check()
        new_ticket = tk.Ticket()
        self.add_ticket(new_ticket)

    def add_ticket(self, this_ticket):
        self.all_tickets["active"][this_ticket.plate_num] = {"start_park" : this_ticket.start_time}

    def leave_garage(self):
        pass

    def pay_for_parking(self):
        pass

    def full_lot_check(self):
        if self.spaces_remaining < 1:
            print("This lot is full, you'll have to park elsewhere.")
            self.main()


    def main(self):
        next_action = input("What is the next car doing? (park or leave?)")
        if next_action == "park":
            self.park()
        elif next_action == "leave":
            self.leave_garage()
        else:
            print("Thanks for managing the garage.")
            return(self.all_tickets)


startThings = ParkingGarage()

startThings.main()
