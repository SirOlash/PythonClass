def get_Countries():

    countries = {"USA" : {"CALIFORNIA" : {"Los Angeles" : 4000000, "San Francisco" : 870000}},
             "CANADA" : {"ONTARIO" : {"Toronto" : 2930000, "Ottawa" : 994837}}
             }

    while True:
        new_country = input("Enter country: ").upper()
        if new_country not in countries:
            countries[new_country] = {}
        new_state = input("Enter state: ").upper()
        if new_state not in countries[new_country]:
            countries[new_country][new_state] = {}
        new_city1 = input("Enter city: ").upper()
        new_city1_population = int(input(f"Enter population of {new_city1} : "))
        countries[new_country][new_state][new_city1] = new_city1_population
        new_city2 = input("Enter a new city: ").upper()
        new_city2_population = int(input(f"Enter population of {new_city2} : "))
        countries[new_country][new_state][new_city2] = new_city2_population
        break

    return countries

print(get_Countries())