#While loop
i = 1
s = 0
while i <= 10:
    s += i
    print(s)
    i += 1
#building a guessing game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit :
        guess = input("Enter guess again: ")
        guess_count += 1
    else:
        out_of_guesses = True
    
if out_of_guesses:
    print("Out of Guesses, You Lose!")
else:
    print("You win!")


#For loop
for index in "Giraffe Academy":
    print(index)
friends = ["Jim", "Kavin", "Oscar"]
len_fri = len(friends) #tra ve do dai
for friend in friends:
    print(friend)
for friend in range(len_fri):
    print(friends[friend])
for index in range(3, 10):
    print(index)