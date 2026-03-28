num_tickets = 1001
bus_capacity = 50

num_buses = num_tickets // bus_capacity
num_left_passengers = num_tickets % bus_capacity

print(num_buses, num_left_passengers)
