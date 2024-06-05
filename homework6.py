my_dict = {"квартира 31": "Петров", "квартра 34": "Васильев", "квартира 39": "Олейник" }
print(my_dict)
print(my_dict["квартира 31"])
print(my_dict.get("квартира 32"))
my_dict.update({"квартира 1": "Иванов",
                "квартира 84": "Караулов"})
debtor=my_dict.pop("квартира 31")
print(debtor)

my_set = {1, 2, 8, "дом", "список", "дом", 1, (56, 34, 35), "список", (56, 34, 35)}
print(my_set)
my_set.discard("список")
print((my_set))