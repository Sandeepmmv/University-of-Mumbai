from typing import DefaultDict
import sys

INT_MAX = sys.maxsize
tsp = [
    [-1, 10, 15, 20],
    [10, -1, 35, 25],
    [15, 35, -1, 30],
    [20, 25, 30, -1]
]

num_cities = len(tsp)
sm = 0
visited = [False] * num_cities
route = [-1] * num_cities


current_city = 0
visited[current_city] = True
route[0] = current_city
route_index = 1

while route_index < num_cities:
    min_cost = INT_MAX
    next_city = -1

    
    for j in range(num_cities):
        if not visited[j] and tsp[current_city][j] < min_cost:
            min_cost = tsp[current_city][j]
            next_city = j

    
    visited[next_city] = True
    route[route_index] = next_city
    sm += min_cost
    current_city = next_city
    route_index += 1

sm += tsp[current_city][route[0]]
route.append(route[0])  # Complete the tour by returning to the start

print("Minimum Cost is:", sm)
print("Route is:", [city + 1 for city in route])  # Convert to 1-based indexing