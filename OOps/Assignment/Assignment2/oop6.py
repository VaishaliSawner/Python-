class Movie:
    def __init__(self, movie_name, total_seats):
        self.__movie_name = movie_name
        self.__total_seats = total_seats
        self.__available_seats = total_seats

    
    def book_tickets(self, number_of_tickets):
        if number_of_tickets <= 0:
            print("Invalid tickets.")
        elif number_of_tickets > self.__available_seats:
            print("Booking failed")
        else:
            self.__available_seats -= number_of_tickets
            print(f"{number_of_tickets} ticket booked successfully.")

    
    def cancel_tickets(self, number_of_tickets):
        if number_of_tickets <= 0:
            print("Invalid tickets.")
        elif self.__available_seats + number_of_tickets > self.__total_seats:
            print("Cancellation failed")
        else:
            self.__available_seats += number_of_tickets
            print(f"{number_of_tickets} ticket(s) cancelled successfully.")


    def display_availability(self):
        print("Movie Name:", self.__movie_name)
        print("Total Seats:", self.__total_seats)
        print("Available Seats:", self.__available_seats)



movie1 = Movie("Roy", 100)
movie2 = Movie("Avatar", 50)


movie1.book_tickets(5)
movie1.cancel_tickets(2)
movie1.display_availability()


movie2.book_tickets(10)
movie2.cancel_tickets(5)
movie2.display_availability()