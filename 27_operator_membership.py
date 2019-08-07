a = [10, 20, 30, 40]
b = (1, 2, 3, 4)
c = {"name": "aasem"}

# List
if 10 in a:
    print("Available")
else:
    print("Not Available")

if 50 not in a:
    print("Not Available")
else:
    print("Available")

# Tuple
if 1 in b:
    print("True")
else:
    print("False")

if 6 not in b:
    print("Absent")
else:
    print("Present")

# Dictionary
if "name" in c:
    print("Name is Available")

if "age" is not c:
    print("Age is Not Available")
