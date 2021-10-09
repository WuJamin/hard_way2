from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())

print("Type the filename again:")
file_name = input("> ")

txt_again = open(file_name)

print(txt_again.read())