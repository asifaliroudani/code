customer = {
    'name': 'Asif',
    'age': 30,
    'is_verified': True
}

print(customer)
print(customer['name'])
print(customer.get('name'))
print(customer.get('birthdate'))
print(customer.get('birthdate', 'Dec 19 1988'))

customer['birthday'] = 'Jan 1 1990'
print(customer['birthday'])