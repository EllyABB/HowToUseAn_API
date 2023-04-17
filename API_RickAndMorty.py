import requests
from datetime import datetime
import json

url="https://rickandmortyapi.com/api/"
character_url=url+"character/"

class info():
    
    def __init__(self,id=None):
        if id==None:
            print('Necesitas un id para obtener información!')
        else:
            self.id=str(id)
            self.info=requests.get(character_url+self.id).json()
            self.ep=self.info['episode'][0]

    def name(self):
        return self.info['name']
    
    def Species(self):
        return self.info['species']
    
    def First_Episode(self):
        name_ep=requests.get(self.ep).json()['name']
        return name_ep
    
    def Date_First_Episode(self):
        date_ep=requests.get(self.ep).json()['air_date']
        return datetime.strptime(date_ep, '%B %d, %Y').strftime('%d/%m/%Y')
    

class json_class(info):
    def __init__(self,id=None):
        super().__init__(id)
    
    def file(self):
        json_file={}
        json_file['name']=self.name()
        json_file['species']=self.Species()
        json_file['episode_name']=self.First_Episode()
        json_file['air_date']=self.Date_First_Episode()
        
        return json.dumps(json_file)

    
    
Task=['1','2','13','26','32','11']
url2 = 'https://api4pluto.dudewhereismy.com.mx/rickandmorty'




