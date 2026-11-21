miles_driven = 30
gallons_of_gas_used = 0

try:
    mpg = miles_driven/gallons_of_gas_used
    print(f'Your MPG is {mpg}')
except ZeroDivisionError:
    print('Do you drive an electric car?')

#--------------------------------------------------------------------------------

from urllib import request, error
from time import sleep

# A URL for a website that we expect to be available, if we are online
url = 'https://www.google.com'

seconds_to_sleep_between_checks = 3

while True:
    print('Checking if you are online...')
    
    try: 
        # Open the URL. This will error/fail if you are not online.
        request.urlopen(url).read()
        print('You seem to be online.')
    except error.URLError:
        print('You are NOT online.')
        
        print(f'Sleeping for {seconds_to_sleep_between_checks} seconds...')
        print()
        sleep(seconds_to_sleep_between_checks) 
        
#--------------------------------------------------------------------------------

from datetime import datetime

current_year = datetime.today().year

while True:
    
    try:
        birth_year = int(input('Enter the year you were born: '))
        break
    except ValueError:
        print('Please enter a number.')
        
age = current_year - birth_year

print(f'Thank you, you were born in {birth_year} which makes you about {age} years old.')

#--------------------------------------------------------------------------------

from datetime import datetime

current_year = datetime.today().year
oldest_year = current_year - 120

while True:
    
    try:
        birth_year = int(input('Enter the year you were born: '))
        if birth_year > current_year or birth_year < oldest_year:
            raise ValueError
        break
    except ValueError:
        print(f'Please enter a number between {oldest_year} and {current_year}.')
        
age = current_year - birth_year

print(f'Thank you, you were born in {birth_year} which makes you about {age} years old.')