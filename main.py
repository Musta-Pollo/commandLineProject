from distutils.log import error


def getAnswer():
    while True:
        answer = input("y or n: ")
        if answer == "y":
            return "1"
        elif answer == "n":
            return "0"
        else:
            error("Invalid input")


def game():
    score = "0"
    print("Welcome on adventure game, where you can die or get a huge wealth")

    print("After a weeks of tiring road you see a cave. There is total darkness and nothing could be seen. Go inside or move forward.")
    score += getAnswer()

    if score == "01":
        print("After a moment of searching you find heavy treasure with gold.")
        print("Continue in searching or move on?")
        score += getAnswer()
        if score == "011":
            print("Wild beast killed you. Game over")
            return
        elif score == "010":
            print("Better not tempt my luck")

    elif score == "00":
        print("It's not worth risking it. Better to move on.")

    print("On the road you met a old man struggling. Help him or go home")
    score += getAnswer()

    if(score[len(score)-1] == "0"):
        print("You go around and arrived in home town. Happy ever after.")
        if score[1] == "1":
            print("With treasure of gold and fame")
    elif score[len(score)-1] == "1":
        print("It was a trap. He was a vampire and killed you.")


game()
