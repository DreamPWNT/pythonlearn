# Список стран (НЕ МЕНЯТЬ ЕГО):
raw_names = ["peru", "cANADA", "australia", "austria",
             "slovenia", "slovakia", "sweden", "switzerland",
             "new zealand", "uae", "usa"]

# Нужно в список normalized_names записать эти названия согласно
# правилам написания: Peru, Canada, New Zealand, USA  <- пример
normalized_names = []
# abrr_list это вспомогательный список с образцами. НЕ МЕНЯТЬ ЕГО!
abrr_list = ["USA", "UAE", "GBR"]

for name in raw_names:
    if ' ' in name or name.upper() not in abrr_list:
        normalized_names.append(name.title())
    else:
        normalized_names.append(name.upper())

print(normalized_names)
