import random

words = ["python", "programming", "code", "computer"]

secret_word = random.choice(words)

display_word = []
for letter in secret_word:
    display_word.append('_')

attempt = 6
while attempt > 0 and '_' in display_word:
    print(' '.join(display_word))
    print(f"Attempts remaining: {attempt}")

    guess = input("enter a letter: ").lower()

    if guess in secret_word:
        print("Correct guess")

        for i in range (len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess

    else :
        print("Incorrect guess")
        attempt = attempt - 1

if '_' not in display_word:
    print("Congratulations! You won!")
    print(f"The correct word was {' '.join(display_word)}")

else:
    print("Sorry, you lost")
    print(f"The correct word was {secret_word}")