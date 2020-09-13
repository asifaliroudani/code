message = input(">")
words = message.split(" ")
output_message = ""
months = {
    "jan": "January",
    "feb": "February",
    "mar": "March"
}

for word in words:
    output_message += months.get(word, word) + ' '
print(output_message)