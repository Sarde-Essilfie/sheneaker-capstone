import requests
import pprint
import json
from django.core.management.base import BaseCommand

from sneaker_app.models import Sneaker


class Command(BaseCommand):

    def handle(self, *args, **options):

    #clear existing sneakers
        Sneaker.objects.all().delete()

        #request to API
        #if I only want WOMEN'S sneakers, should I filter those here?????
        response = requests.get('https://the-sneaker-database.p.rapidapi.com/sneakers', headers={"X-RapidAPI-Key": "a7f0d72c4emshc06616986d50ecep1b54e5jsn3f9c98fcc3f6",
                            "X-RapidAPI-Host": "the-sneaker-database.p.rapidapi.com"},
                            params= {
                                "limit": "92",
                                "gender": "WOMEN"
                                }
                            )
        #print(response) 
        # # print(type(response.text))  
        # print(response.text)

        #Loop through Sneaker to add to the database(DB)
        sneakers_dictionary = response.json()
        # print('SNEAKERS DICTIONARY', sneakers_dictionary)
        the_sneaker_list = sneakers_dictionary['results']
        # print(the_sneaker_list)

        for sneaker in the_sneaker_list:
            # print('SNEAKER', sneaker)

            #add Sneaker to database(DB)
            sneaker_obj = Sneaker()
                # id = sneaker['id'],
            sneaker_obj.name = sneaker['name']
            sneaker_obj.brand = sneaker['brand']
            sneaker_obj.color = sneaker['colorway']
            sneaker_obj.gender = sneaker['gender']
            sneaker_obj.image = sneaker['image']
            sneaker_obj.price = sneaker['retailPrice']
            sneaker_obj.links = sneaker['links']
            sneaker_obj.save()
            print('SNEAKER_OBJ', sneaker_obj)
   

    




