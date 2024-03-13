# Braden Jackson
# CIS261
# Lab Submission: Country

from itertools import count


def display_menu():
    print("Command MENU")
    print("view - View contry name")
    print("add  - Add a country")
    print("del  - Delete a country")
    print("exit - Exit program")
    
def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country codes: "
    for code in codes:
        codes_line += code + " "   
    print(codes_line)
    
def view(countries):
    display_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}.\n")
    else:
        print("There is no country with that code.\n")
        
def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code.\n")
    else:
        name = input("Enter country name: ")
        name = name.titile()
        countries[code] = name
        print(f"{name} was added.\n")
        
def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted.\n")
    else:
        print("There is no country with that code.\n")
        
def main():
    countries = {"AF" : "Afghannistan", "DE" : "Germany", "US": "United States"}
    display_menu()
    while True:
        command = input("Command: ")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "del":
            delete(countries)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")
            
if __name__ == "__main__":
    main()
        