counting = 1
n1 = 0
n2 = 1

print("fibonacci sequence:")
print("1. 0")
while counting <= 29:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    
    counting += 1
    count = str(counting)
    print(count + ".", n1)