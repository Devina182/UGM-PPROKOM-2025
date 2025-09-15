counter = 0
found_flag = False
number = 1

while number <= 20: 
    if number % 2  != 0:
        number += 1
        continue

    if number % 4 == 0: 
        number += 1
        continue

    print(f"Found: {number}")
    counter += 1

    if counter == 5:
        found_flag = True
        break

    number += 1
else:
    print("Loop finished without finding 5 numbers.")

if found_flag:
    print("Succesfully found 5 numbers!")
else:
    print("Did not find enough numbers.")
