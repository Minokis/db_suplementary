from mimesis import Generic
from mimesis.builtins import RussiaSpecProvider
g = Generic('ru')

# SUPPLIER
# name:
print('Имя поставщика:', g.business.company())
# INN (10 цифр)
print('ИНН:', g.code.custom_code(mask='##########'))
#
# Product:
# name
# g.food.spices()
# g.food.dish()
# g.food.drink()
# g.food.fruit()
# g.food.vegetable()

# PRICE
# cost or costsale:
print('Цена:', g.business.price())

# CARD
# card number:
print('Номер кредитки:', g.personal.credit_card_number())
# FirstName
print('Имя:', g.personal.name(gender='female'))
# MiddleName - а зачем?
g.add_provider(RussiaSpecProvider)
print('Отчество:', g.russia_provider.patronymic(gender='female'))
# LastName
print('Фамилия:', g.personal.surname(gender='female'))
# Full name (as on card):
print('Имя и фамилия, как на карте:', g.personal.full_name())

# BirthDate:
print(g.datetime.date(start=1950, end=2001, fmt='%Y-%m-%d'))
# есть еще day_of_month(), month() % year(), time()
