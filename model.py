import random
import math

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TSPSolver:
    def __init__(self, cities):
        self.cities = cities

    def calculate_distance(self, city1, city2):
        # Calculate the Euclidean distance between two cities
        x_distance = abs(city1.x - city2.x)
        y_distance = abs(city1.y - city2.y)
        return int(math.sqrt(x_distance**2 + y_distance**2))

    def nearest_neighbor_tsp(self):
        # Implementation of the Nearest Neighbor algorithm for the Traveling Salesman Problem (TSP)
        num_cities = len(self.cities)
        distances = [[self.calculate_distance(city1, city2) for city2 in self.cities] for city1 in self.cities]
        
        best_order = None
        best_distance = float('inf')

        for _ in range(num_cities):
            order = self.run_nearest_neighbor(random.randint(0, num_cities - 1), distances)
            distance = self.calculate_total_distance(order, distances)

            if distance < best_distance:
                best_order = order
                best_distance = distance

        return best_order, best_distance

    def run_nearest_neighbor(self, start_city, distances):
        # Run the Nearest Neighbor algorithm from a given starting city
        num_cities = len(self.cities)
        visited = [False] * num_cities
        order = []
        total_distance = 0

        current_city = start_city
        order.append(current_city)
        visited[current_city] = True

        for _ in range(1, num_cities):
            nearest_city = self.find_nearest_city(current_city, visited, distances)
            order.append(nearest_city)
            visited[nearest_city] = True
            total_distance += distances[current_city][nearest_city]
            current_city = nearest_city

        order.append(order[0])  # Return to the starting city to complete the tour
        total_distance += distances[current_city][order[0]]

        return order

    def find_nearest_city(self, current_city, visited, distances):
        # Find the nearest unvisited city from the current city
        num_cities = len(self.cities)
        nearest_city = -1
        min_distance = float('inf')

        for i in range(num_cities):
            if not visited[i] and distances[current_city][i] < min_distance:
                nearest_city = i
                min_distance = distances[current_city][i]

        return nearest_city

    def calculate_total_distance(self, order, distances):
        # Calculate the total distance of a given tour order
        total_distance = 0
        for i in range(len(order) - 1):
            total_distance += distances[order[i]][order[i + 1]]
        return total_distance