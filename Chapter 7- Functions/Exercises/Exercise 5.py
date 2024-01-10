#function with parameters of cities and the set value/argument for country "japan"
def describe_city(city, country="japan"):
    #message with f-string and .title 
    message = f"{city.title()} is in {country.title()}."
    print(message)

#cities without a country assigned will automatically be set to default parameter value "japan"
describe_city("seoul", "korea")
describe_city("tokyo")
describe_city("shibuya")