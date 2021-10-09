print("Let's practice everything.")
print('you\' need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely wold
with logic so
cannot \n the
\n\twhere.
"""



print("------")
print(poem)
print("-" * 10)


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)


print("With a of: {}".format(start_point))

print(f"We'd hanve {beans} beans, {jars} jars, and {crates} crates.")




formula = secret_formula(start_point)

print("We'd have {} beans, {} jars, and {} crates.".format(*formula))