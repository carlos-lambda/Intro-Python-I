# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
# YOUR CODE HERE


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
    # constructor. It should inherit from LatLon. Look up the `super` method.
    # YOUR CODE HERE


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    # YOUR CODE HERE
    def __str__(self):  # convert the string when printed
        return f"{self.name} is located at longitude: {self.lon} and latitude: {self.lat}"

    # Make a class Geocache that can be passed parameters `name`, `difficulty`,
    # `size`, `lat`, and `lon` to the constructor. What should it inherit from?


class Geocache(Waypoint, LatLon):
    def __init__(self, name, difficulty, size, lon, lat):
        super().__init__(name, lon, lat)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):  # convert the string when printed
        return f"{self.name} has a difficulty of {self.difficulty}"


    # YOUR CODE HERE
    # Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
waypoint = Waypoint('Catacombs', 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geocache = Geocache('NewBerry Views', 1.5, 2, 44.052137, -121.41556)
# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache)
