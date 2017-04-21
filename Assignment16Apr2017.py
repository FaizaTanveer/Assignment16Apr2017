# Chapter 8 , Question no.8-3. T-shirts:

def make_shirt(size,message):
    print("Well Done ! You Proved\n'"+message.title()+"'.")
    print("I hope shirt size '"+size.title()+"' fit you.\n")

make_shirt('medium',"dreams don't work unless you do")
#make_shirt(message='a goal without a plan is just a wish',size='large')

# Chapter 8 , Question no.8-4. Large shirts:

def make_shirt(size='large',message='i love python'):
    print('Message written on '+size.title()+" shirt \n'"+message.upper()+"'.\n")

make_shirt()

def make_shirt(size,message='i love python'):
    print('Message written on '+size.title()+" shirt \n'"+message.upper()+"'.\n")

make_shirt('large')
make_shirt(size='medium')
make_shirt(message='I will be the best data scientist in future',size='any size')

# Chapter 8 , Question no.8-5. Cities:

def describe_city(cityname,country='pakistan'):
    print(cityname.title()+" is Beautiful city to visit. It's in "+country.title()+".\n")


describe_city('kaghan')
describe_city(cityname='balakut')
describe_city('malam jabba')
describe_city('auckland','new zealand')

# Chapter 8 , Question no.8-6. City Names:

def city_country(city,country='america'):
    full_info= '"'+city+', '+country+'"'
    return full_info.title()

print(city_country('karachi','pakistan'))

names= city_country('sydney','australia')
print(names)

names=city_country('boston')
print(names)
print("\n")

# Chapter 8 , Question no.8-7. Album:Part -1

def make_album(artist_name,album_title):
    '''here is a dictionary that describes a music album'''
    full_album={'artist':artist_name,'album':album_title}
    return full_album


album_1 = make_album('Zia khan','Deep learning')
album_2 = make_album('Zeeshan hanif','Java')
album_3 = make_album('Salah uddin','Python')

print(album_1)
print(album_2)
print(album_3)
print("\n")

# Chapter 8 , Question no.8-7. Album:Part -2

def make_album(artist_name,album_title,no_tracks=""):
    '''here is a dictionary that describes a music album'''
    full_album_1={'artist':artist_name,'album':album_title,'track':no_tracks}
    if no_tracks:
        full_album_1 = {'artist': artist_name, 'album': album_title, 'track': no_tracks}
    else:
        full_album_1 = {'artist': artist_name, 'album': album_title}

    return full_album_1

album_1 = make_album('Zia khan','Deep learning',3)
album_2 = make_album('Zeeshan hanif','Java')


print(album_1)
print(album_2)
print("\n")


# Chapter 8 , Question no.8-8. User Albums:

def make_album(artist_name,album_title):
    '''here is a dictionary that describes a music album'''
    full_album_1={'artist':artist_name,'album':album_title}
    return full_album_1

while True:
    option = input("Press 'q' to quit or 'y' to continue ")
    if option=='q':
        print('Bye')
        break

    else:
        #info_1 = input()
        artist = input("Enter Artist Name: ")
        title = input("Enter Album Title: ")
        continue


    modify_album=make_album(artist,title)
    print(modify_album)

print("\n")

# Chapter 8 , Question no.8-12. Sandwiches:

def sandwich(*items):
    print("\nMaking a sandwich with the following item: ")
    for item in items:
        print("- "+item)

sandwich('mayonnaise','chicken')
sandwich('bbq tikka flavor','ketchup','tomatoes')
sandwich('egg with cheese')
print("\n")

# Chapter 8 , Question no.8-13. User Profile:

def build_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key, value in user_info.items():
        profile[key]=value
    return profile

user_profile=build_profile('faiza','tanveer',field='computer',location='Sir Syed University')

print(user_profile)
print('\n')

# Chapter 8 , Question no.8-14. Cars:

def car_info(manufacturer, model_name, **other_info):
    """Build a dictionary containing everything we know about a cars."""
    car_Profile = {}
    car_Profile['manufacturer'] = manufacturer.title()
    car_Profile['model'] = model_name.title()
    for key, value in other_info.items():
        car_Profile[key] = value
    return car_Profile

car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)
print('\n')

# Project Euler:Problem No#3

num = 600851475143
x = 2
factors = []

while (x <= num):
    while (num % x == 0):
        num = num / x
        factors.append(x)
    x = x + 1
print("The Largest Prime Factors Of '600851475143' are :")
print (factors)









