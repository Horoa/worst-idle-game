import random
import time
import math

def game(n,sleepTime):
    number = 1
    count = 0
    max = 1
    maxCount = 1
    while number < n + 1 :
        i = random.randint(1,n)
        print(str(i) + " | " + str(number) + " | " + str(max) + " | " + str(n) + " | " + str(count) + " | " + str(maxCount))
        if i == number :
            number+=1
            if max < number -1 :
                max = number - 1
                maxCount = 1
            if number == max :
                maxCount +=1
        else :
            if i == 1 :
                number = 2
            else :
                number = 1
        count+=1
        time.sleep(sleepTime)
    print("Vous avez gagné en " + str(count) + " coups !")
    return(count)


def main():
    money = 0
    inputText = ""
    maxGame = 2
    time = 3
    priceSpeed = 20
    priceBonusGold = 10
    bonusGold = 1
    priceMaxGame = int(math.pow(maxGame + 1, maxGame +1))

    while inputText != "Quit":
        inputText = ""
        inputGame = 0
        inputUppgrade = 0
        while (inputText != "Quit" and inputText != "Game" and inputText !="Uppgrade" and inputText !="Cheat") :
            inputText = input("hello what you want Uppgrade Game Or Quit | Money = " + str(money))
            if inputText == "Game" :
                while inputGame < 1 or inputGame > maxGame :
                    inputGame = int(input("What is the number for the game ? Max = " + str(maxGame)))
                game(inputGame, time)
                gain = round(math.pow(inputGame,inputGame)*2*bonusGold)
                money += gain
                print("You win " + str(gain) + "! | Money = " + str(money))

            if inputText == "Cheat":
                money = int(input("How much ?"))

            if inputText == "Uppgrade" :
                while inputUppgrade < 1 or inputUppgrade > 3 :
                    print("1 = Speed : " + str(priceSpeed) + " | " + str(time))
                    print("2 = MaxGame : " + str(priceMaxGame) + " | " + str(maxGame))
                    print("3 = BonusGold : " + str(priceBonusGold) + " | " + str(bonusGold))
                    inputUppgrade = int(input("What you want ?"))
                if inputUppgrade == 1 :
                    if money < priceSpeed :
                        print("Not enough money")
                    elif time ==  0 :
                        print("Max speed already")
                    else :
                        money -= priceSpeed
                        priceSpeed = (priceSpeed + 10) * 4
                        time -= 0.4
                        if time < 0 :
                            time =  0
                if inputUppgrade == 2 :
                    if money < priceMaxGame:
                        print("Not enough money")
                    else :
                        money -= priceMaxGame
                        maxGame += 1
                        priceMaxGame = int(math.pow(maxGame + 1, maxGame +1))
                if inputUppgrade == 3 :
                    if money < priceBonusGold:
                        print("Not enough money")
                    else :
                        money -= priceBonusGold
                        bonusGold = bonusGold*bonusGold + 0.1
                        priceBonusGold = (priceBonusGold + 50) * 8
                        

                        
                            

main()
