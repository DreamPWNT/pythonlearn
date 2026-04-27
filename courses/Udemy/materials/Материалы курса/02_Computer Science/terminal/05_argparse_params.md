
## `ArgumentParser().add_argument()` - объяснение параметров

Метод:

```python
add_argument(
    *name_or_flags,
    action=None,
    nargs=None,
    const=None,
    default=None,
    type=None,
    choices=None,
    required=False,
    help=None,
    metavar=None,
    dest=None,
    version=None,
    **kwargs
)
```
---

# `*name_or_flags`

Имя аргумента, это *args, то есть можно несколько.

### Может быть:

✔ позиционный аргумент
```python
parser.add_argument("filename")
```

✔ флаг (короткий)
```python
parser.add_argument("-v")
```

✔ флаг (длинный)
```python
parser.add_argument("--verbose")
```

✔ оба варианта
```python
parser.add_argument("-v", "--verbose")
```

Если имя **не начинается с `-`** , это **позиционный аргумент**, если начинается то **флаг**.

---

# `action`

Указывает как обрабатывать аргумент.

Самые важные значения:

### `store` (по умолчанию)

Сохраняет значение аргумента.

### `store_true`

Булевый флаг:
```python
parser.add_argument("--debug", action="store_true")
```

```
--debug  → True
(нет)    → False
```

### `store_false`

Обратное:

```python
--debug → False
```

### `count`

Считает количество повторений:
```python
parser.add_argument("-v", action="count")
```

```
(no -v) → None
-v      → 1
-vv     → 2
```

### `append`

Сохраняет много значений в список:
```python
parser.add_argument("--ip", action="append")
```

```
--ip 1.2.3.4 --ip 5.6.7.8
→ ["1.2.3.4", "5.6.7.8"]
```

---

# `nargs`

Сколько аргументов ожидает этот параметр.

## Основные значения:

### ✔ число

```python
parser.add_argument("--coords", nargs=2)
```

```
--coords 10 20
→ ["10", "20"]
```

### `?` - максимум один (или default, если нет)
```python
parser.add_argument("file", nargs="?")
```

### `*` - сколько угодно (может быть пусто)
```python
parser.add_argument("files", nargs="*")
```

### `+` - минимум один
```python
parser.add_argument("files", nargs="+")
```

---

# `const`

Используется:
* когда аргумент имеет действие без значения
* то есть, если его передать просто, то будет значение по умолчанию

Пример:
```python
parser.add_argument("--mode", nargs="?", const="auto")
```

```
--mode       → "auto"
--mode slow  → "slow"
```

---

# `default`

Значение по умолчанию, если аргумент НЕ указан.

```python
parser.add_argument("--threads", default=4)
```

---

# `type`

Тип, к которому нужно преобразовать значение:

```python
parser.add_argument("--limit", type=int)
```

Если пользователь введёт не `int`, argparse выдаст ошибку сам.

Можно передавать свои функции:

```python
def port(s):
    p = int(s)
    if not 0 < p < 65536:
        raise ValueError("Wrong port")
    return p

parser.add_argument("--port", type=port)
```

---

# `choices`

Ограничивает допустимые значения:
```python
parser.add_argument("--level", choices=["info", "debug", "warning"])
```

Если пользователь введёт что-то другое, то argparse выдаст ошибку.

---

## `required`

Используется только для флагов.

Сделать флаг обязательным:

```python
parser.add_argument("--config", required=True)
```

Для позиционных аргументов `required` не нужен - позиционные итак обязательные.

---

## `help`

Описание аргумента, которое появляется в `--help` для кокретного аргумента.

```python
parser.add_argument("--debug", help="Enable debug mode")
```

---

## `metavar`

Имя, отображаемое в `--help`. Как подсказка по ожидаемому типу значения.

Пример:

```python
parser.add_argument("--output", metavar="FILE")
```

```
--output FILE
```

Полезно для красивой документации.

---

## `dest`

Имя атрибута, под которым значение будет доступно в `args`.

Пример:

```python
parser.add_argument("--output", dest="outfile")
```

```python
args.outfile
```

Используется редко, в основном если названия конфликтуют.

---

## `version`

Используется, если вы делаете параметр `--version`.

Но обычно делают через:

```python
parser.add_argument("--version", action="version", version="1.0")
```

---

# **Краткая таблица**

| Параметр        | Что делает                                    |
| --------------- | --------------------------------------------- |
| `name_or_flags` | имя аргумента (`-v`, `--verbose`, `filename`) |
| `action`        | как обрабатывать этот аргумент                |
| `nargs`         | сколько значений ожидается                    |
| `const`         | константа при отсутствии значения             |
| `default`       | значение по умолчанию                         |
| `type`          | в какой тип преобразовать                     |
| `choices`       | допустимые значения                           |
| `required`      | обязателен ли флаг                            |
| `help`          | текст в `--help`                              |
| `metavar`       | как отображать в help                         |
| `dest`          | имя переменной для `args.xxx`                 |

---

