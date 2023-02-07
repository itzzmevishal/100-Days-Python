# Hint
# The lower() function changes all the letters in a string to lowercase.
# The count() function will give you the number of times a letter occurs in a string.


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_1=name1.lower()
name_2=name2.lower()
# print(name1)
name=name_1+name_2
true1=name.count("t")
true2=name.count("r")
true3=name.count("u")
true4=name.count("e")
true=true1+true2+true3+true4

love1=name.count("l")
love2=name.count("o")
love3=name.count("v")
love4=name.count("e")
love=love1+love2+love3+love4

s=str(true)+str(love)
score=int(s)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >40 and score <50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

