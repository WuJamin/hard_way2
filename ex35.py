from sys import exit

def gold_room():
    print("How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greety, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("""
There is a bear here.
move the bear?
""")
    bear_move = False

    while True:
        choice = input("> ")
        if choice == "take honney":
            print("slap your face off")
        elif choice == "taun bear" and not bear_move:
            print("go")
            bear_move = True
        elif choice == "taun bear" and bear_move:
            dead("off")
        elif choice == "open door" and bear_move:
            gold_room()
        else:
            print("no means")
