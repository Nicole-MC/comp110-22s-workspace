# xs: list[str] = ["a", "b", "c"]
# i: int = 0 
# while i < len(xs):
#     item: str = xs[i]
#     print(item)
#     i += 1

# for item in xs:
#     print(item)

"""An example of for in syntax."""


names: list[str] = ["Nicole", "George", "Louis", "Allie"]

# Example of iterating through names using a while loop
print("while output: ")
i: int = 0 
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for in loop is the same as the while loop above
print("For ... in output: ")
for name in names:
    print(name)