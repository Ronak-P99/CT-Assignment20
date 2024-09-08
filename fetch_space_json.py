import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
   
    try:
        response = requests.get(url)
        planets = response.json()['bodies']
        for planet in planets:
                if planet['isPlanet']:
                    name = planet.get("name", "No name")
                    mass = planet.get("mass", {"No content"})
                    orbit_period = planet.get("sideralOrbit", "No Orbit")
                    print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

        #process each planet info
        return planets
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def find_heaviest_planet(planets):
    for planet in planets:
                if planet['isPlanet']:
                    name = planet.get("name", "No name")
                    mass = planet.get("mass", {"No content"})
                    orbit_period = planet.get("sideralOrbit", "No Orbit")
                    print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
                    return name, mass


planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")

