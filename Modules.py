import random
import sys

try:
    print("Hello my name is", sys.argv[1])
except IndexError:
    print("Too few agreement")

#Handling all the errors using if and else

if len(sys.argv)<2:
    print("few arguments")
elif len(sys.argv)>2:
    print("Too many arguments")
else:
    print("Hello my name is", sys.argv[1])


#More refinenment

if len(sys.argv)<2:
   sys.exit("few arguments")
elif len(sys.argv)>2:
    sys.exit("Too many arguments")

print("Hello my name is", sys.argv[1])


coin = random.choice(["heads", "tails"])
print(coin)


cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)