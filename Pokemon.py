from requests import get
from LinkedList import LinkedList


class Pokemon():

    def __init__(self, name):
        self.name = name
        self.abilities = []
        self.types = []
        self.weight = None
        self.image = None
        self.call_poke_api()
        self.pokes = []
        self.evolve_chain = LinkedList()

    def call_poke_api(self):
        if isinstance(self.name, str) and self.name.isalpha():
            self.name = self.name.lower()
        response = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        if response.status_code == 200:
            print('Success')
            data = response.json()
            self.name = data['name']
            self.abilities = [ability_object['ability']['name']
                              for ability_object in data['abilities']]
            self.types = [type_object['type']['name']
                          for type_object in data['types']]
            self.weight = data['weight']

            self.image = data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
            if not self.image:
                self.image = data['sprites']['front_default']
            self.species_url = data['species']['url']
        else:
            print(f'Error status code {response.status_code}')

    def get_evolution_chain(self):
        response = get(self.species_url)
        if response.status_code == 200:
            data = response.json()
        evolution_chain_url = data['evolution_chain']['url']
        evolution_chain = get(evolution_chain_url)
        if evolution_chain.status_code == 200:
            return evolution_chain.json()['chain']

    def evolve_pokemon(self, evolution_chain):
        if not evolution_chain['evolves_to']:
            print(f'This is the final form')
            return self.evolve_chain
        current_pokemon_in_chain = evolution_chain['species']['name']
        next_pokemon_in_chain = evolution_chain['evolves_to'][0]['species']['name']
        if current_pokemon_in_chain == self.name:
            self.name = next_pokemon_in_chain
            # self.call_poke_api()
            return self.evolve_chain
        else:
            return self.evolve_pokemon(evolution_chain['evolves_to'][0])

    def evolve_chain(self, pokname):
        self.evolve_chain.add_node(pokname.title())


arceus = Pokemon('arceus')
evolve = arceus.evolve_pokemon(arceus.get_evolution_chain())
print(evolve)


charmander = Pokemon('charmander')
evolve = charmander.evolve_pokemon(charmander.get_evolution_chain())
print(evolve)
evolve = charmander.evolve_pokemon(charmander.get_evolution_chain())
print(evolve)
evolve = charmander.evolve_pokemon(charmander.get_evolution_chain())
print(evolve)
