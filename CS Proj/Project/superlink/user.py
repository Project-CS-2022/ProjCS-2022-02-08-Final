import requests

apiurl = f'https://randomuser.me/api/'
req = requests.get(apiurl).json()

def name():
    Slice = req['results'][0]
    title = Slice["name"]["title"]
    firstName = Slice["name"]["first"]
    lastName = Slice["name"]["last"]
    return title +" "+firstName +" "+ lastName

def gender():
    Slice = req['results'][0]
    a = Slice["gender"]
    return a

def location():
    Slice = req['results'][0]
    locationNo = str(Slice["location"]["street"]["number"])
    locationName = Slice["location"]["street"]["name"]
    fullLocation = Slice["location"]["city"]+", "+Slice["location"]["state"]
    postcode = str(Slice["location"]["postcode"])
    return locationNo+", "+locationName+", "+fullLocation+" - "+postcode

def country():
    Slice = req['results'][0]
    country = Slice["location"]["country"]
    return country

def email():
    Slice = req['results'][0]
    email = Slice["email"]
    return email

def mobileNo():
    Slice = req['results'][0]
    no = Slice["phone"]
    return no

def registeredOn():
    Slice = req['results'][0]
    date = Slice["registered"]["date"]
    x = date.replace("T",", ")
    reg = x[:-5]
    return reg
