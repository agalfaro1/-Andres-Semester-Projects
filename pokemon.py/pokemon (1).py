
import random

#init
pokemonLevel = 0 # global
pokemonEvolution = 0
pokemonXP = 0
pokemonName = "squirtle"
quit = 0
day = 1

# Main
print("Welcome to Pokemon Evolution!")
while quit == 0:
    XPreq = 100 + (3 * pokemonLevel)
    print(f"It is day {day}")
    print(f"Your {pokemonName} is level {pokemonLevel} with {pokemonXP} XP")
    print("Pick an activity:")

    print("""1. Train
    2. Battle
    3. Rest
    4. Quit""")

    activity = int(input("Select an option (1-4): "))

    if activity == 1:
        squirtleSitUps = random.randint(4, 9)
        pokemonXP += squirtleSitUps * 10
        print(f"Congrats, Your Pokemon did {squirtleSitUps} Squirtle Sit-ups and gained {squirtleSitUps * 10} XP!")
        day += 1
        if pokemonXP >= XPreq:
            pokemonLevel += 1
            print(f"Congrats, Your {pokemonName} leveled up to level {pokemonLevel}")
        XPreq = 100 + (3 * pokemonLevel)

    elif activity == 2:
        opponentLevel = pokemonLevel + random.randint(-9, 9)
        if opponentLevel < 1:
            opponentLevel = 1

        print(f"Quick! A level {opponentLevel} Pokemon has appeared! Fight?")
        battle = int(input("Select 1 to battle: "))

        if battle == 1:
            print("Quick! What is your attack?")
            print("""1. Bubble
2. AquaTail""")
            attack = int(input("Select attack (1-2): "))

            successChance = (90 - (attack * 20)) + (5 * pokemonLevel - opponentLevel) + (pokemonLevel ** 0.5) + (5 * pokemonEvolution)  # Attack success chance formula
            successChance = min(successChance, 90)  # Cap at 90 for max success chance

            successNumber = random.randint(1, 100)
            print(f"Your opponent got a roll of {successNumber}")

            if successChance >= successNumber:
                print("Congrats, you won!")
                pokemonXP += ((attack * 90) + (20 * (opponentLevel - pokemonLevel)))

                # Level up if necessary
                while pokemonXP >= XPreq:
                    pokemonXP -= XPreq
                    pokemonLevel += 1
                    XPreq = 100 + (3 * pokemonLevel)
                    print(f"Your Pokemon leveled up to level {pokemonLevel}")
            else:
                print("Tough luck, you lost the battle.")

    elif activity == 3:
        print(f"Pokemon stats for {pokemonName}:")
        print(f"Level: {pokemonLevel}")
        print(f"XP: {pokemonXP}")

        # You can add the draw functions here, or just comment them out for now
        if pokemonEvolution == 0:
            print("Drawing Squirtle...")
        elif pokemonEvolution == 1:
            print("Drawing Wartortle...")
        elif pokemonEvolution == 2:
            print("Drawing Blastoise...")

        input("Press ENTER to continue.")

    elif activity == 4:
        quit = 1

    if pokemonEvolution == 0 and pokemonLevel >= 30:
        pokemonLevel -= 30
        pokemonXP = 0
        pokemonEvolution = 1
        pokemonName = "Wartortle"  # Assuming this is the evolution name
        print(f"{pokemonName} evolved!")
