class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def update_instance_variables(self):
        return self.brand.lower()
c1 = Car("TATA", "Scorpio", 2020)
print(c1.update_instance_variables())
print(c1.brand)
print(c1.model)
print(c1.year)
c1.brand = "KIA"
print(c1.brand)
print(c1.update_instance_variables())