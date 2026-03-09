import random
print("Enter two number to start the game")

n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))

print(f"You have 3 tries to guess the number from {n1} to {n2}")
print("Start")

num = random.randint(n1, n2)
tries = 3
gc = 0

while gc <= tries:
    
    gc += 1 
    g = int(input("Your guess: "))
    
    if gc == tries and g != num:
        print(f"the number was {num}. GG!")
        break
    
    elif g > num:
        print("Too High")
    
    elif g < num: 
        print("Too Low")
    
    

    elif g == num:
        print(f"You got it in {gc} tries")
        break 