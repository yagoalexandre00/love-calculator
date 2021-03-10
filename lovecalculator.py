# Love Calculator ---------> Author: Yago Goltara
import time

# Greetings
print("Hello, buddy! Welcome to the Love Calculator!")

# Gets the user's name
your_name = input("First of all, tell me your name: ")

# Gets the crush's name
crush_name = input(f"Ok, {your_name}. Now, tell me your crush's name: ")

# Concatenates both names
totalname = your_name + crush_name

# Turns the concatenated name into lower case
totalname = totalname.lower()

# Counts how many "t""r""u""e" the total name has
t = totalname.count("t")
r = totalname.count("r")
u = totalname.count("u")
e = totalname.count("e")

# Counts how many "l""o""v" the total name has 
l = totalname.count("l")
o = totalname.count("o")
v = totalname.count("v")

true = t+r+u+e      # Sums true
love = l+o+v+e      # Sums love

# Generates a score
score = str(true) + str(love)

# Here is where the magic happens
if int(score) >= 80:
    print(f"OMG, {your_name}! YOU TOOK {score} points! YOU MUST GET MARRIED! GO THERE AND PROPOSE HIM/HER RIGHT NOW!!!!!")
elif int(score) >= 60 and int(score) < 80:
    print(f"You took {score} points! Congratulations, {your_name}! Maybe you are {crush_name}'s soulmate!")
elif int(score) >= 40 and int(score) < 60:
    print(f"You took {score} points. Hmmm, yeah, you might meet your crush better. Going for a dinner could be a good idea!")
elif int(score) >= 20 and int(score) < 40:
    print(f"Hm... you got {score} points. It's not a good result... But you could still try. Who knows?")
else:
    print(f"Your score is {score}. Being real. You better change crush. It's not your soulmate. Go out and meet other people!")

time.sleep(6)   # Freezes the user's screen