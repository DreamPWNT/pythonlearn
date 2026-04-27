"""Примитивы по работе с прямоугольниками.

В модуле определены функции расчитывающие площади, объемы
прямоугольников и прямоугольных параллелепипедов.
И второстепенные функции.
"""


def rectangle_volume(
    length: int | float, width: int | float, /, *, height: int | float
) -> int | float:
    """Возвращает объём прямоугольного параллелепипеда."""

    area = rectangle_area(length, width)
    volume = area * abs(height)
    return volume


def rectangle_area(length: int | float, width: int | float) -> int | float:
    """Возвращает площадь прямоугольника"""

    area = abs(length) * abs(width)
    return area


def with_gap(
    size: tuple, gap: int | float, *, minus_gap: bool = False
) -> tuple[int | float, ...]:
    """Добавляет зазор + или - к размерам описанного в кортеже."""

    new_size = []
    gap = abs(gap)

    if minus_gap:
        gap = -gap

    for side in size:
        new = abs(side) + gap
        new_size.append(new)
    return tuple(new_size)
