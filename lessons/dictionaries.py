"""Demostrations of Dictionary capabilites."""

# Declaring a type of dictionary
schools: dict[str, int]

#Intialize to an empty dictionary 
schools = dict()

# Set a key-value pairing in the dictionarty
schools["UNC"] = 19_400
schools["Duke"] = 6717
schools["NCSU"] = 26150


# print a dict literal rep

print(schools)

# Access a value by its key - "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dict
# by its key
schools.pop("Duke")

# TEst  for the existance of a key
is_duke_present: bool = "Duke" in schools
print(f"is_duke_present: {is_duke_present}")

# Update / Reassign a key-value pair 
schools["UNC"] = 20000
schools["NCSU"] = schools["NCSU"] + 200 


print(schools)
