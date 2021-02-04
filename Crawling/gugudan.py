def gugudan(num):
    quo = 9//num
    n = 2
    print(quo)
    for k in range(1, quo+2):
        for i in range(1, 10):
            if (k * num) + 2 > 9:
                for j in range (n, 10):
                    print("{0} x {1} = {2}".format(j, i, j * i), end="\t")
                print(" ")
            else:
                for j in range(n, (k*num)+2):
                    print("{0} x {1} = {2}".format(j, i, j*i), end="\t")
                print(" ")
        n = (k * num) + 2
        print(" ")

num = int(input("숫자를 입력하세요."))
gugudan(num)
