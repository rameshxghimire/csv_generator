import random
import string
import csv

# define how many rows of csv data is needed
ROWS_NEEDED = 200

letters = string.ascii_lowercase[:22]
domains = ['hotmail.com', 'yahoo.com', 'aol.com', 'gmail.com', 'aol.com', 'mail.com', 'msn.com', 'live.com', 'outlook.com', 'gmx.xom', 'facebook.com', 'protonmail.com']
cities = ['Rock Church', 'Market Square', 'Alvar Alto Museum', ' Sibelius Monument and Park', 'Uspensky Cathedral', ' Linnanmäki', 'Kiasma', 'Railway Station',
          'Velodrome', 'Kumpula swimming pool', 'Laakso riding hall', 'Tennispalatsi', 'Olympiaterminaali']

# print(letters)
# print(domains)

# get random domains, needed to generate random emails
def get_random_domain(domains):
    return random.choice(domains)

# get random city
def get_random_city(cities):
    return random.choice(cities)

# generate random name of defined size
def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))

# generate random age between 0 - 100
def generate_random_age():
    return random.choice([x for x in range(100)])


# generate random phone number in Finnish format
def generate_random_phone():
    return '+358 ' + ''.join(str(random.choice([x for x in range(1,10)])) for _ in range(8))

# generate random emails
def generate_random_emails(number, length):
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(number)]

# generate random yes/no
def generate_yes_no():
    return random.choice(['Yes', 'No'])

# generate random role from customer/organiser
def generate_role():
    return random.choice(['Customer', 'Organiser'])

# generate random rating / feedback
def generate_rating_category():
    return random.choice(['Highly recommend', 'enjoyable', 'okay', 'only as a filler', 'would never visit'])

# generate the csv using all of the above
with open('da_file.csv', 'w+') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['customerId',
                     'firstName',
                     'lastName',
                     'email',
                     'phoneNumber',
                     'age',
                     'profileConsent',
                     'role',
                     'clubName',
                     'city',
                     'ContactEmail',
                     'riderId',
                     'customerId',
                     'IsCompleted',
                     'finishingTime',
                     'cancelResv',
                     'evaluationNumber',
                     'tourId',
                     'riderId',
                     'RatingCategory',
                     'comment',
                     'sharingConsent',
                     'tourId',
                     'riderId',
                     'tourName',
                     'description',
                     'tourDate',
                     'startingLocation',
                     'distance',
                     'climbingDistance',
                     'cancellationId',
                     'tourId',
                     'notificationSent',
                     'cancellationDate',
                     'waitingNumber',
                     'customerId',
                     'reservationDate',
                     'reservationTime'])

    for _ in range(ROWS_NEEDED):
        writer.writerow([str(_), get_random_name(letters, 5), get_random_name(letters, 8), str(generate_random_emails(1, 15)[0]), generate_random_phone(), str(generate_random_age()),
                         generate_yes_no(), generate_role(), get_random_name(letters, 4), get_random_city(cities), str(generate_random_emails(1, 15)[0]), str(_+1), str(_),
                         generate_yes_no(), str(generate_random_age()+20), generate_yes_no(), str(generate_random_age()+2), str(_+2), str(_+1), generate_rating_category(),
                         '', generate_yes_no(), str(_+2), str(_+1), get_random_name(letters, 8), '', str(generate_random_age()+40), get_random_city(cities), str(_+4)+' KM', str(_+130)+' m',
                         str(100+_), str(_+2), generate_yes_no(), '', str(_-1), str(_), '', '' ])
    








    
