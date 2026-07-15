# Nested While Loop Assignment
# Print number pattern using nested while loops

rows = 5
i = 1

while i <= rows:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1