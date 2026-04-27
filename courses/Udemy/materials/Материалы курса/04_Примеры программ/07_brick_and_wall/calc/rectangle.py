"""Более высокоуровневые функции по работе с прямоугольниками.

В модуле определены функции рассчитывающие разницу объемов
прямоугольников и прямоугольных параллелепипедов в разных
компановках.
Использует функции модуля calc.primitives.rectangle в
большинстве случаев (почти).
"""


from calc.primitives.rectangle import rectangle_volume


def count_v_in_v(a: int | float, b: int | float) -> int | float:
    """Сколько объемов в объеме.
    Принимает уже рассчитанные объемы.
    """
    if b > a:
        a, b = b, a
    return a // b


def count_v_in_v_sizes(a: tuple, b: tuple, *, coef: float = 1.0) -> int | float:
    """Сколько объемов в объеме.
    Принимает параметры сторон прямоугольников в
    формате (Длина, Ширина, Высота)
    """
    one = rectangle_volume(*a[:2], height=a[2])
    two = rectangle_volume(*b[:2], height=b[2]) * coef
    if two > one:
        one, two = two, one
    return one // two


def v_diff_mul(*args: int | float) -> int | float:
    """Разница (дельта) в объемах.
    Принимает рассчитанные объемы.
    Вычитает из первого остальные.
    """
    diff = args[0] - sum(args[1:])
    return abs(diff)


def v_diff(a: tuple, b: tuple) -> int | float:
    """Разница (дельта) в объемах.
    Принимает параметры сторон прямоугольников в
    формате (Длина, Ширина, Высота)
    """
    one = rectangle_volume(*a[:2], height=a[2])
    two = rectangle_volume(*b[:2], height=b[2])
    return abs(one - two)
