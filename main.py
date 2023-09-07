import random

choose = input('Enter number of task ')
match int(choose):
    case 1:
        print(1001)  # task 1
    case 2:

        enter = input('Enter str ')  # task 2
        print(enter)
        for i in enter:
            if i.isdigit():
                print(i)
    case 3:
        list = []
        for i in range(10):
            list.append(random.randint(-9, 9))
        print(list)
        min = max = list[0]
        for i in range(10):
            if list[i] % 2 == 1:
                if max < list[i]:
                    max = list[i]
            if abs(min) > abs(list[i]):
                min = list[i]

        print('maximal even element ', max)
        print('minimal modulo element', min)
    case 4:
        string = 'Enjoy every moment'
        dictionary = {}

        for char in string:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1

        print(dictionary)
    case 5:
        list_bouquet = [['roses', 20, 100], ['chamomile and violet', 15, 25], ['tulips', 19, 100]]
        range_produce = {'101rose': list_bouquet[0], 'romance from field': list_bouquet[1], '8 march': list_bouquet[2]}
        print('1- print description\n', '2- print price\n', '3- print count\n', '4- print all info\n',
              '5- make order\n')
        choise = input("Enter number or 'n' for escape \n")
        while (choise != 'n'):

            match int(choise):
                case 1:
                    j = 0
                    for i in range_produce:
                        print(i, ' consists of: ', list_bouquet[j][0])
                        j += 1
                case 2:
                    j = 0
                    for i in range_produce:
                        print(i, ' price: ', list_bouquet[j][1])
                        j += 1
                case 3:
                    j = 0
                    for i in range_produce:
                        print(i, ' count: ', list_bouquet[j][2])
                        j += 1
                case 4:
                    j = 0
                    for i in range_produce:
                        print(i, ' consists of ', list_bouquet[j][0], ' price: ', list_bouquet[j][1], ' count: ',
                              list_bouquet[j][2])
                        j += 1
                case 5:
                    list_choise = []
                    while (choose != 'n'):
                        bouquet = input('Enter name of bouquet ')
                        kol = input('Enter amount ')
                        list_choise.append(bouquet)
                        list_choise.append(int(kol))
                        choose = input('Press n for escape or press anything to continue\n')
                    price = 0
                    i = 0
                    while (i < len(list_choise)):
                        price += range_produce[list_choise[i]][1] * list_choise[i + 1]
                        range_produce[list_choise[i]][2] = range_produce[list_choise[i]][2] - list_choise[i + 1]
                        i += 2

                    print('give me ', price, ' $')

            print('\n1- print description\n', '2- print price\n', '3- print count\n', '4- print all info\n',
                  '5- make order\n')
            choose = input("Enter number or 'n' for escape \n")
    case 6:
        c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
        c_2 = (45, 21, 124, 76, 5, 23, 91, 234)
        count_1 = 0
        count_2 = 0
        min_1 = max_1 = c_1[0]
        min_2 = max_2 = c_2[0]

        for i in c_2:
            count_2 += i
            if (min_2 > i): min_2 = i
            if (max_2 < i): max_2 = i
        for i in c_1:
            count_1 += i
            if (min_1 > i): min_1 = i
            if (max_1 < i): max_1 = i
        if count_1 >= count_2:
            print('c_1 > c_2')
        else:
            print('c_1 < c_2')
        print('maximal element c_1: ', max_1,' minimal element: ', min_1,
              '\nmaximal element c_2: ', max_2,' minimal element: ', min_2)
