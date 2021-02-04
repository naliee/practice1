def gugudan(num):

    for i in range(1, 10):
        for j in range(2, 10):
            print("{0} x {1} = {2}".format(j, i, j*i), end="\t")
        print(" ")

num = int(input("숫자를 입력하세요."))
gugudan(num)
