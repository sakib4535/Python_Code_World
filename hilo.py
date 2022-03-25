low = 1
high = 1000

print("Tell a Number Between {} and {}".format(low,high))
input("Press Enter to Run")

guess = 1
while True:
    print("\t Guessing in the Range of between {} and {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I Guess Higher or Lower ? "
    "Enter h or l, or c if my Guess was Correct ".format(guess)).casefold()

    if high_low == "h":
        # Guess Higher.
       low = guess + 1
    elif high_low == "l":
        #Guess Lower.
       high = guess - 1
    elif high_low == "c":
        print("I got in {}".format(guess))
        break
    else:
        print("Please enter h, l or c")

    guess = guess + 1
    
else:
    print("You Got the Number {}".format(low))
    print("I got it in {} guess".format(guess))
