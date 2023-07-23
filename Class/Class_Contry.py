class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

if __name__ == "__main__":
    canada = Country("Canada", 22222222, 3333333)
    print("Name: ", canada.name)
    print("Population: ", canada.population)
    print("Area: ", canada.area)