import csv
from mimesis import Generic
from mimesis.builtins import RussiaSpecProvider
from datetime import datetime as dt
import random
g = Generic('ru')
g.add_provider(RussiaSpecProvider)
# Check SERIAL PRIMARY KEY,
# 	Card INT FOREIGN KEY,
# 	DateTime TIMESTAMPZ NOT NULL,
# 	Paid BOOLEAN
# 	PaymentForm enum ?,
# 	CreateDatetime TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT clock_timestamp();
# 	ModifyDatetime

random.seed()
card_ids = set()
for i in range(101,200):
    card_ids.add(i)


def create_check_csv(n, filename, cards):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for i in range(n):
            card = random.sample(cards, 1) if random.randint(1,10)>= 5 else ['NULL']
            random_datetime = g.datetime.date(start=2017, end=2017, fmt='%Y-%m-%d') + ' ' + g.datetime.time(fmt='%H:%M:%S') + '.' + g.code.custom_code(mask='######')
            current_timestamp = dt.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            pform = '2' if card[0] != 'NULL' else '1'
            row = [card[0],  # card number
                   random_datetime,         # datetime of the check
                   '1',                     # paid
                   pform,                   # cash or card
                   current_timestamp,       # created
                   current_timestamp]       # modified
            writer.writerow(row)

create_check_csv(100, 'checks.csv', card_ids)


