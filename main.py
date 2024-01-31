class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_started = False

    def start_engine(self):
        if not self.engine_started:
            print("Двигун автомобіля запущено.")
            self.engine_started = True
        else:
            print("Двигун вже запущено.")

    def stop_engine(self):
        if self.engine_started:
            print("Двигун автомобіля зупинено.")
            self.engine_started = False
        else:
            print("Двигун вже зупинено.")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

    def __eq__(self, other):
        return (
            self.brand == other.brand
            and self.model == other.model
            and self.year == other.year
        )

    def __ne__(self, other):
        return not self.__eq__(other)


car1 = Car("Volkswagen", "T4", 2000)
car2 = Car("Volkswagen", "T4", 2000)

print("Car 1:", car1)
print("Car 2:", car2)

if car1 == car2:
    print("Автомобілі однакові.")
else:
    print("Автомобілі різні.")

car1.start_engine()
car2.start_engine()
car1.stop_engine()
car2.stop_engine()
