my_list = [10, 20, 30, 40, 50]

print("List Elements:")
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Slice [1:4]:", my_list[1:4])
print()

my_tuple = ('apple', 'banana', 'cherry', 'date', 'elderberry')

print("Tuple Elements:")
print("Second element:", my_tuple[1])
print("Last element:", my_tuple[-1])
print("Slice [2:]:", my_tuple[2:])
print()

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "job": "Engineer",
    "hobby": "Photography"
}

print("Dictionary Elements:")
print("Value for 'name':", my_dict["name"])
print("Value for 'job':", my_dict.get("job"))
print("All keys:", my_dict.keys())
print("All values:", my_dict.values())
