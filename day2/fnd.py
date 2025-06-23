a = [4, 7, 1, 9, 3]

# Smallest number
sml = a[0]
for i in a:
    if i < sml:
        sml = i
print("Smallest number:", sml)

# Greatest number
big = a[0]
for i in a:
    if i > big:
        big = i
        print("gratest number:",big)

# Second greatest number
second_big = a[0]
for i in a:
    if i > second_big and i < big:
        second_big = i
print("Second greatest number:", second_big)

# Second smallest number
second_sml = None
for i in a:
    if i > sml:
        if second_sml is None or i < second_sml:
            second_sml = i
print("Second smallest number:", second_sml)
