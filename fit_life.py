# Проект FitLife - MVP версия 1.0


print('Здравствуйте!')
user_name = input("Ваше имя:")
user_age = input("Ваш возраст:")
user_age = int(user_age)
# Обозначаем переменные на имя и возраст
# Данные переменной user_age переводим в числовое значение

user_weight = input("Укажите ваш вес в килограммах. : ")
user_height = input("Укажите ваш рост в метрах : ")
user_weight = float(user_weight)
user_height = float(user_height)
# Обозначаем переменные на рост и вес
# Данные обеих переменных переводим в числовое значение.
# float дает нам работать с дробными числами.


# Расчитываем ИМТ по формуле из ТЗ
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)


# Расчитываем норму воды по формуле из ТЗ
water_ml = user_weight * 30
# Переводим переменную water_ml в литры
water_l = water_ml / 1000


# Выводим итоговые данные как указано в ТЗ
print(f'Отчет для {user_name} ({user_age} г.)')
print(f'Твой индекс массы тела: {bmi}')
print(f'Рекомендуемая норма употребления воды: {water_l:.1f} л.')
