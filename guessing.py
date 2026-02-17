secrets = [10,23,45,69]
while True:
    guess = int(input("please enter your guess number from (1-10): "))
    for i in range(len(secrets)):
        if secrets[i] == guess:
            print("correct 🎉🎉✨🎇")
    break