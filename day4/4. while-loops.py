i = 0
while i < 4:
    print(i)
    i += 1


# break statement
i = 0
while i < 6:
    print(i)
    if i == 4:
       break
    i += 1


# continue statement
i = 0
while i < 6:
    i += 1
    if i == 4:
       continue
    print(i)


# else statement
i = 0
while i < 4:
    print(i)
    i += 1
else: 
   print("i is not less than 6 anymore")


# nested while loops
count = 0 
while count < 2:
    inner_count = 0
    while inner_count < 3:
        print("in and out")
        inner_count += 1
    count += 1	