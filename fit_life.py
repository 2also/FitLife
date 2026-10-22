# Проект FitLife - MVP версия 1.0


print('Здравствуйте!')
user_name = input("Ваше имя:")
user_name = user_name.title()
user_age = input("Ваш возраст(полных лет):")
user_age = int(user_age)


user_weight = input("Укажите ваш вес в килограммах. : ")
user_height = input("Укажите ваш рост в метрах : ")
user_weight = float(user_weight.replace(',', '.'))
user_height = float(user_height.replace(',', '.'))


bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)


water_ml = user_weight * 30
ml_to_liters = 1000
water_l = water_ml / ml_to_liters


print(f'Отчет для {user_name} ({user_age} г.)')
print(f'Твой индекс массы тела: {bmi}')
print(f'Рекомендуемая норма употребления воды: {water_l:.1f} л.')
