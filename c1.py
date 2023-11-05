# Höfundur: Milos Petrovic
# Dagsetning: 31.10.2023
# Verkefni: Forritun 1C - Spurning 1

def readFlights(filename: str):
  with open(filename, 'r') as flights:
    return flights.readlines()

def groupTravelers(flights: list[str]):
    travelers = {}

    for flight in flights:
        # strip removes whitespace from start and end
        # split splits a string by a space
        name, country = flight.strip().split(" ")
        # if name is in travelers, add country to their list
        if name in travelers:
            # if country is not in the list, add it
            if country not in travelers[name]:
                travelers[name].append(country)
        else:
            # if name is not in travelers
            # add it with a list containing country
            travelers[name] = [country]

    # convert list of dictionarie and sort countries alphabetically
    return [{"name": name, "countries": sorted(countries)} for name, countries in travelers.items()]

def printTravelers(travelers: list):
  # sort by name alphabetically
  travelers.sort(key=lambda x: x['name'])

  for traveler in travelers:
      name = traveler['name']

      print(f'{name}:\n\t' + '\n\t'.join(traveler['countries']))

def getPersonWithMostCountries(travelers: list):
  # get first traveler
  traveler = travelers[0]

  # loop through travelers and compare
  # who has the most countries
  for t in travelers:
    if len(t['countries']) > len(traveler['countries']):
      traveler = t

  return traveler


try:
  filename = str(input("Enter filename: "))
  flights = readFlights(filename)
  travelers = groupTravelers(flights)
  printTravelers(travelers)
  personWithMostCountries = getPersonWithMostCountries(travelers)
  print(f"{personWithMostCountries['name']} has been to {len(personWithMostCountries['countries'])} countries")
except:
   print('Something went wrong, try again')
