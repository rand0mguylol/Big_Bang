import json

num_array = []

# The arrangement of the if/elif/else statements is important
# because the statement will be executed on the first condition that is met.

# For example, if we were to put i % 3 == 0 or i % 5 == 0 as the first condition,
# then the program would never reach the condition i % 3 == 0 and i % 5 == 0

for i in range(1, 101, 1):
    if i % 3 == 0 and i % 5 == 0:
        num_array.append("BIGBANG")
    elif i % 3 == 0:
        num_array.append("BIG")
    elif i % 5 == 0:
        num_array.append("BANG")
    else:
        num_array.append(i)

print(num_array)

# Save the array to a dictionary
output = {
    "array": num_array
}

# Write the output to a json file
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)