import requests

class State :
    
    def __init__(self, d, header) :
        self.__dict__ = d
        self.districts = requests.get(f'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{self.state_id}', headers=header).json()['districts']


class States :
    
    def __init__(self) :
        self.header = {'content-type' : 'application/json', 'user-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
        self.states = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states', headers=self.header).json()['states']
    
    @property
    def all(self) :

        for state in self.states :
            state['districts'] = State(state, self.header).districts

        return self.__dict__




