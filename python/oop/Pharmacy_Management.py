class Drug:
    def __init__(self, name: str, amount: int, price: int):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name: str):
        self.name = name
        self.employees = []
        self.drugs = []

    def add_drug(self, drug: Drug):
        self.drugs.append(drug)

    def add_employee(self, first_name: str, last_name: str, age: int):
        self.employees.append(
            {"first_name": first_name, "last_name": last_name, "age": age}
        )

    def total_value(self) -> int:
        totalValue = 0
        for drug in range(len(self.drugs)):
            totalValue = self.drugs[drug].amount * self.drugs[drug].price + totalValue
        return totalValue

    def employees_summary(self) -> str:
        result = "Employees:\n"

        for i, employee in enumerate(self.employees, start=1):
            result += (
                f"The employee number {i} is "
                f"{employee["first_name"]} {employee["last_name"]} "
                f"who is {employee["age"]} years old.\n"
            )

        return result


drug1 = Drug("Aspirin", 100, 25000)
drug2 = Drug("Ibuprofen", 50, 40000)
drug3 = Drug("Vitamin C", 200, 100000)

my_pharmacy = Pharmacy("City Pharmacy")

print(f"Created Pharmacy: {my_pharmacy.name}")
print("-" * 20)


my_pharmacy.add_drug(drug1)
my_pharmacy.add_drug(drug2)
my_pharmacy.add_drug(drug3)

print(f"Number of drugs in {my_pharmacy.name}: {len(my_pharmacy.drugs)}")
print("-" * 20)

my_pharmacy.add_employee("Alice", "Smith", 25)
my_pharmacy.add_employee("Bob", "Johnson", 30)

total_inventory_value = my_pharmacy.total_value()
print(f"Total value of drugs in {my_pharmacy.name}: {total_inventory_value}")
print("-" * 20)

employee_list_summary = my_pharmacy.employees_summary()
print(employee_list_summary)
