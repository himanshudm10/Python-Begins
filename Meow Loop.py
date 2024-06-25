def main():
    hello()
    number=get_number()
    meow(number)


def get_number():
        while True:
            n = int(input("How much meow do you want? "))
            if n>0:
                break
        return n


def meow(n):
    for i in range(n):
        print("meow")

def hello():
    print("Hello")


main()