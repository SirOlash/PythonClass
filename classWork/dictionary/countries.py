countries = {"USA" : {"CALIFORNIA" : {"Los Angeles" : 4000000, "San Francisco" : 870000}},
             "CANADA" : {"ONTARIO" : {"Toronto" : 2930000, "Ottawa" : 994837}}
             }

try:
    country = input("Enter country: ").upper()
    if country in countries:
        enteredState = input("Enter state: ").upper()
        if enteredState in countries[country]:
            for city, population in countries[country][enteredState].items():
                print(f"{city}: {population}")
        else:
            print("State not found.")
    else:
        print("Country not found.")
except Exception as e:
    print(f"An error occurred: {e}")