human_weight = int(input("Введіть вагу людини:"))
human_height = float(input("Введіть зріст людини в метрах(наприклад 1.84):"))

body_mass_index = (human_weight /
                  (human_height *
                   human_height))

if body_mass_index < 18.5:
    print("Індекс маси тіла = "
          ,body_mass_index
          , ", що свідчить про недостатню вагу")
elif body_mass_index >= 18.5 and body_mass_index <= 24.9:
    print("Індекс маси тіла = "
          ,body_mass_index
          , ", це еквівалент нормальної маси тіла")
elif body_mass_index >= 25.0 and body_mass_index <= 29.9:
    print("Індекс маси тіла = "
          ,body_mass_index
          , ", що вказує на наявність зайвої ваги")
elif body_mass_index >= 30.0:
    print("Індекс маси тіла = "
          ,body_mass_index
          , " є ознакою ожиріння")
else:
    print("Некорректно введені дані!")

                                            
