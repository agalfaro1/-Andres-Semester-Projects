def name_generator():
    # Ask if the user is an introvert or extrovert
    personality = input("Are you an introvert or extrovert? ").lower()

    if personality == "introvert":
        # If introvert, choose a country (Mexico or Japan)
        country = input("Choose a country: Mexico or Japan? ").lower()

        if country == "mexico":
            # Choose between pistachio or butter pecan
            flavor = input("Choose a flavor: pistachio or butter pecan? ").lower()
            if flavor == "pistachio":
                print("Your name is: Lord Farquaad")
            elif flavor == "butter pecan":
                print("Your name is: Shrek")
            else:
                print("Invalid flavor choice.")

        elif country == "japan":
            # Choose between chocolate or vanilla
            flavor = input("Choose a flavor: chocolate or vanilla? ").lower()
            if flavor == "chocolate":
                print("Your name is: Fiona")
            elif flavor == "vanilla":
                print("Your name is: Donkey")
            else:
                print("Invalid flavor choice.")

        else:
            print("Invalid country choice.")

    elif personality == "extrovert":
        # If extrovert, choose a country (France or Australia)
        country = input("Choose a country: France or Australia? ").lower()

        if country == "france":
            # Choose between strawberry or coffee
            flavor = input("Choose a flavor: strawberry or coffee? ").lower()
            if flavor == "strawberry":
                print("Your name is: Muffin Man")
            elif flavor == "coffee":
                print("Your name is: Gingerbread Man")
            else:
                print("Invalid flavor choice.")

        elif country == "australia":
            # Choose between rum and raisin or cookies and cream
            flavor = input("Choose a flavor: rum and raisin or cookies and cream? ").lower()
            if flavor == "rum and raisin":
                print("Your name is: Pinocchio")
            elif flavor == "cookies and cream":
                print("Your name is: Dragon")
            else:
                print("Invalid flavor choice.")

        else:
            print("Invalid country choice.")

    else:
        print("Invalid personality choice.")
#main
name_generator()
