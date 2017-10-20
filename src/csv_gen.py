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

timestamp_fmt = '%Y-%m-%d %H:%M:%S.%f'
card_numbers = set()
# Ensures that card numbers are unique in the file
def create_card_csv(n, filename):
    timestamp = dt.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    genders = ['male', 'female']
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        i = 0
        for j in range(10000):
            card_number = '4'+ g.code.custom_code(mask='###')+' '+g.code.custom_code(mask='####')+' '+g.code.custom_code(mask='####')+' '+g.code.custom_code(mask='####')
            if card_number in card_numbers:
                continue
            else:
                card_numbers.add(card_number)
                genderstr=genders[random.randint(0, 1)]
                row = [card_number,
                       g.personal.name(gender=genderstr),
                       g.russia_provider.patronymic(gender=genderstr),
                       g.personal.surname(gender=genderstr),
                       g.datetime.date(start=1950, end=2001, fmt='%Y-%m-%d'),
                       timestamp, timestamp]
                writer.writerow(row)
                i += 1
                if i == n:
                    break

create_card_csv(100, 'card.csv')
