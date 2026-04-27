# Основной файл как скрипт (по простому):
brick_lwh = (250, 120, 65)       # Размеры кирпича: длина, ширина, высота (мм).
mortar = 10                      # Толщина слоя раствора для кладки (мм).
wall_lwh = (10000, 510, 3000)    # Размеры стены: длина, толщина, высота (мм).
coefficient = 1.1
# Площадь поверхности 250 мм * 120 мм = 30_000 мм2 (квадратных миллиметров).
# Объем 250 мм * 120 мм * 65 мм = 1_950_000 мм3 (кубических миллиметров).
# В 1 метре 1000 миллиметров.
# Чтоб перевести квадратные мм в квадратные метры нужно результат / 1_000_000
# Чтоб перевести кубические мм в кубические метры нужно результат / 1_000_000_000
import math

from calc.primitives.rectangle import rectangle_volume, with_gap
from calc.rectangle import count_v_in_v_sizes


wall_v = rectangle_volume(*wall_lwh[:2], height=wall_lwh[2])
print(f"Объем стены {wall_v / 1_000_000_000:.2f} м3.")

bricks_count = count_v_in_v_sizes(wall_lwh, with_gap(brick_lwh, mortar), coef=0.98)
print(f"Нужно {math.ceil(bricks_count*coefficient)} кирпичей.")

bricks_v = bricks_count * rectangle_volume(*brick_lwh[:2], height=brick_lwh[2])
mortar_v = wall_v - bricks_v
print(f"Нужно {mortar_v / 1_000_000_000:.2f} м3 раствора.")
