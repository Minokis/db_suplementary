import csv
from mimesis import Generic
from mimesis.builtins import RussiaSpecProvider
from datetime import datetime as dt
import random
g = Generic('ru')
g.add_provider(RussiaSpecProvider)
# Card table
# Card SERIAL PRIMARY KEY,
#     Number VARCHAR(10) UNIQUE NOT NULL,
#     FirstName VARCHAR(50),
#     MiddleName VARCHAR(50),
#     LastName VARCHAR(50),
#     BirthDate DATE,
#     CreateDatetime TIMESTAMP NOT NULL,
#     ModifyDatetime TIMESTAMP

random.seed()


def Card(counter=[0]):
    counter[0] += 1
    return counter[0]

timestamp_fmt = '%Y-%m-%d %H:%M:%S.%f'

def card_create_row(genderstr):
    timestamp = dt.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    row = [g.personal.credit_card_number(),
           g.personal.name(gender=genderstr),
           g.russia_provider.patronymic(gender=genderstr),
           g.personal.surname(gender=genderstr),
           g.datetime.date(start=1950, end=2001, fmt='%Y-%m-%d'),
           timestamp, timestamp]
    return row

def create_card_csv(n, filename):
    genders = ['male', 'female']
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for j in range(n):
            writer.writerow(card_create_row(genders[random.randint(0, 1)]))

create_card_csv(100, 'card.csv')


# COPY card(Number, FirstName, MiddleName, LastName, BirthDate, CreateDatetime)
# FROM 'C:\Users\owl_a\PycharmProjects\db_suplementary\src\card.csv' DELIMITER ',';
