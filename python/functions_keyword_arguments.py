def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')


greet_user(last_name="Roudani", first_name="Asif")
greet_user("asif", last_name="Roudani")
# keyword arguments comes after positional arguments


def square(num):
    return num * num


result = square(3)
print(result)

print(square(4))
