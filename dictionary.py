countryDB={}
while True:
    print("1. Insert a country")
    print("2. Display all countries")
    print("3. Display all capitals")
    print("4. Get capitals")
    print("5. Delete an entry")
    choice=int(input("Enter your choice(1-5)"))
    if choice==1:
        country=input("Enter a country: ").upper()
        capital=input("Enter a capital: ").upper()
        countryDB[country]=capital
    elif choice==2:
        print(list(countryDB.keys()))
    elif choice==3:
        print(list(countryDB.values()))
    elif choice==4:
        country=input("Enter country: ").upper()
        print(countryDB.get(country))
    elif choice==5:
        country=input("Enter country: ").upper()
        del countryDB[country]
    else:
        break