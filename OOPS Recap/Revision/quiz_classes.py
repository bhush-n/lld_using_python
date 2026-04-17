"""
Create a class Movie with the following:

Attributes:
movie_name -> name of the movie
total_seats -> total seats available in the theatre
ticket_price -> price per ticket
booked_seats -> starts at 0

Methods:
book_ticket(num_tickets) -> books the given number of tickets. If enough seats are available,
confirm the booking and show the total amount to pay. If not,
show "Sorry, not enough seats available"

show_status() -> displays movie name, seats available, and seats booked so far
"""


class Movie:
    def __init__(self, movie_name: str, total_seats: int, ticket_price: int):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_ticket(self, num_tickets: int):
        available = self.total_seats - self.booked_seats
        if num_tickets > available:
            print("Sorry, not enough seats available")
            return

        self.booked_seats += num_tickets
        total_amount = num_tickets * self.ticket_price
        print(
            f"Booking confirmed for {num_tickets} ticket(s) to '{self.movie_name}'. "
            f"Total amount to pay: {total_amount}"
        )

    def show_status(self):
        available = self.total_seats - self.booked_seats
        print(
            f"Movie: {self.movie_name} | Seats available: {available} | "
            f"Seats booked: {self.booked_seats}"
        )


m = Movie("Inception", 100, 250)
m.show_status()
m.book_ticket(3)
m.book_ticket(150)
m.show_status()
