ten_things = "Apples Oranges Crows Telephone Light Sugar"

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", 
"F", "C", "B", "gir", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There wo go: ", stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
print(stuff[3:5])
