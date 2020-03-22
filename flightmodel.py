# Amazon is launching an airline and wants to perform some simulations of the boarding process.
# Your high-level inputs are a flight and a list of passengers.
# - Passengers have carry-on luggage, seat assignment, and optional special status.
# - Flights have a unique identifier, a seat map, and carry-on capacity.
# Write a function that accepts these inputs and updates each passenger according to their ultimate
# boarding/luggage status.

'''
flight here is a dictionary with key values pairs containing information about the flight
flight_id, number_of_seats, seats_assigned, carry_on_capacity

passengers is a list of dictionaries containing information about the each passenger
passenger_id, seat_number, status, carry_on_luggage

Some assumptions made;
1. If there are pregnant women, they should be checked in first and assigned a seat
2. If there are women with little kids, they should be checked in second
'''


def check_in_passengers(flight, passengers):
    seats_available = flight.number_of_seats
    # sort passengers according to status, those with status of priority are checked in first
    for passenger in passengers:
        if len(flight.number_of_seats) < len(flight.seats_assigned) and flight.carry_on_capacity > 0:
            if seat_number not in flight.seats_assigned:
                assign = {seat_number: [
                    passenger_id: passenger.passenger_id, seat_number: passenger.seat_number, luggage: passenger.carry_on_luggage]}
