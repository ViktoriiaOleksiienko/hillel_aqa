class TrainCar:
    def __init__(self, number, max_passengers):
        self.number = number
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
        else:
            print("This traincar is full!")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f"TrainCar {self.number}: {len(self.passengers)} passengers"


class Train:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def __len__(self):
        return len(self.cars) - 1

    def __str__(self):
        return f"Train with {len(self.cars) - 1} traincars"


traincar1 = TrainCar(number=1, max_passengers=10)
traincar2 = TrainCar(number=2, max_passengers=10)
traincar3 = TrainCar(number=3, max_passengers=10)

traincar1.add_passenger({"name": "Lilly Couper", "destination": "First station", "place": 8})
traincar1.add_passenger({"name": "Ann Black", "destination": "Second station", "place": 7})
traincar2.add_passenger({"name": "Maria Olis", "destination": "Third station", "place": 6})

train = Train()
train.add_car(traincar1)
train.add_car(traincar2)
train.add_car(traincar3)

print(str(traincar1))
print(str(traincar2))
print(str(train))

for passenger in traincar1.passengers:
    print(f'Passenger data:\n"name": "{passenger["name"]}", "destination": "{passenger["destination"]}", "place": {passenger["place"]}')
