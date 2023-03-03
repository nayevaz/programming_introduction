my_list = [1, "a", 34, False, True]

for element in my_list:
    print(element)

for index, element in enumerate(my_list):
    print(index, " ", element)

for iteration in range(0, 25):
    if iteration <= 10:
        print(iteration)