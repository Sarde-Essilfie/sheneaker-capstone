# api request
# The Sneaker Database API
import requests
import pprint

# get response
response = requests.get('https://the-sneaker-database.p.rapidapi.com/sneakers', headers={"X-RapidAPI-Key": "a7f0d72c4emshc06616986d50ecep1b54e5jsn3f9c98fcc3f6",
                        "X-RapidAPI-Host": "the-sneaker-database.p.rapidapi.com"},
                        params={"limit": "10"})
# print(response)  # <Response [200]>
# print(type(response.text))  # <class 'str'>=raw response
# print(response.text)


# get a random sneaker
def get_sneaker():
    # parse JSON object into a dictionary
    sneakers_dictionary = response.json()
    # print(type(json_dict))  # <class 'dict'>
    # print(sneakers_dict)
    # print('My keys-->', sneakers_dict.keys())
    # sneaker_keys(['count', 'results'])
    the_sneaker_list = sneakers_dictionary['results']
    # print('THE SNEAKER LIST', the_sneaker_list)
    # print(type(the_sneaker_list))  # <class 'list'>

    # iterate over the_sneaker_list
    for sneaker in the_sneaker_list:
        # print(sneaker)
        sneaker_id = sneaker['id']
        sneaker_image = sneaker['image']
        sneaker_brand = sneaker['brand']
        sneaker_gender = sneaker['gender']
        sneaker_price = sneaker['retailPrice']
        sneaker_links = sneaker['links']
        # print('SNEAKER ID:', sneaker_id)
        # print('SNEAKER IMAGE', sneaker_image)
        # print('SNEAKER BRAND:', sneaker_brand)
        # print('SNEAKER GENDER:', sneaker_gender)
        # print('SNEAKER PRICE', sneaker_price)
        # print('SNEAKER LINKS:', sneaker_links)


get_sneaker()
# I only want sneakers that come with  images
# I only want womens sneakers
# get by Gender
