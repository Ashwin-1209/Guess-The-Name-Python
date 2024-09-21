import random as r

lst1 = ["IRON MAN", "CAPTAIN AMERICA", "THOR", "HULK", "BLACK WIDOW", "HAWKEYE", "SPIDER MAN", "SCARLET WITCH", "VISION", "DOCTOR STRANGE", "BLACK PANTHER", "ANT MAN", "WASP", "FALCON", "WAR MACHINE", "QUICK SILVER", "WINTER SOLDIER", "STARLORD", "GAMORA", "DRAX", "ROCKET RACCOON", "GROOT", "CAPTAIN MARVEL", "VALKYRIE", "SHANG CHI", "MOON KNIGHT", "SHE HULK", "DAREDEVIL", "WOLVERINE", "CYCLOPS", "JEAN GREY", "STORM", "BEAST", "ROGUE", "GAMBIT", "NIGHT CRAWLER", "COLOSSUS", "PROFESSOR X", "MAGNETO", "DOCTOR DOOM", "THANOS", "LOKI", "MYSTIQUE", "DEADPOOL", "CABLE", "LOGAN", "TONY STARK", "STEVE ROGERS", "WADE WILSON", "PETER PARKER", "PETER QUILL", "WANDA MAXIMOFF", "NATASHA", "CLINT BARTON", "SAM WILSON", "KING TCHALLA", "KILLMONGER", "BUCKY BARNES", "SHURI"]

l = len(lst1)

a1 = lst1[r.randrange(0, l)]
a2 = list(a1)

a1_lst = a1.split()

b1 = ""

for i in a1_lst:
    b1 += len(i) * "_" + " "

b2 = list(b1)

lives = 6

print("-" * 40)
print("GUESS THE SUPERHERO")
print("-" * 40)

print("You have 6 lives!")
print("Your word: ", b1)

while True:
    print("-" * 40)

    guess = input("Enter a letter: ").upper()

    c = ""

    if guess in a2:
        print("Correct guess!")
        print("Lives left: ", lives)

        for i in range(len(a2)):

            if a2[i] == guess:
                b2[i] = guess

    else:
        lives -= 1

        print("Wrong guess!")
        print("Lives left: ", lives)

    for j in b2:
        c += j

    print(c)

    if "_" not in c:
        print("-" * 40)

        print("Congratulations! You found the word!")

        break

    elif lives == 0:
        print("-" * 40)

        print("Game Over!")
        print("You ran out of lives!")

        print("Correct word: ", a1)

        break

print("Thank you for playing")

print("-" * 40)