class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType


    def __eq__(self, other):
        if isinstance(other, Building):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        return False

building1 = Building(7, "Resisdential")
building2 = Building(7, "Resisdential")
building3 = Building(3, "Commercial")


print(f"building1 == building2: {building1 == building2}")
print(f"building1 == building3: {building1 == building3}")
