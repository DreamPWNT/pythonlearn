## Схема операторов обработки ошибок
```python
try:
    # Основной код, где может произойти ошибка
except ExceptionType:
    # Выполняется, если в try произошла ошибка данного типа
else:
    # Выполняется, если в try НЕ было ошибок
finally:
    # Выполняется ВСЕГДА (ошибка была или нет)

```


## Иерархия исключений

```
BaseException
├── BaseExceptionGroup
│
├── GeneratorExit
│
├── KeyboardInterrupt
│
├── SystemExit
│
└── Exception
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    │
    ├── AssertionError
    │
    ├── AttributeError
    │
    ├── BufferError
    │
    ├── EOFError
    │
    ├── ExceptionGroup
    │
    ├── ImportError
    │   └── ModuleNotFoundError
    │
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    │
    ├── MemoryError
    │
    ├── NameError
    │   └── UnboundLocalError
    │
    ├── OSError
    │   ├── BlockingIOError
    │   ├── ChildProcessError
    │   ├── ConnectionError
    │   │   ├── BrokenPipeError
    │   │   ├── ConnectionAbortedError
    │   │   ├── ConnectionRefusedError
    │   │   └── ConnectionResetError
    │   ├── FileExistsError
    │   ├── FileNotFoundError
    │   ├── InterruptedError
    │   ├── IsADirectoryError
    │   ├── NotADirectoryError
    │   ├── PermissionError
    │   ├── ProcessLookupError
    │   ├── TimeoutError
    │   ├── UnsupportedOperation  (из модуля io)
    │   └── itimer_error          (Unix-specific)
    │
    ├── ReferenceError
    │
    ├── RuntimeError
    │   ├── BrokenBarrierError    (из threading)
    │   ├── NotImplementedError
    │   └── RecursionError
    │
    ├── StopIteration
    │
    ├── StopAsyncIteration
    │
    ├── SyntaxError
    │   └── IndentationError
    │       └── TabError
    │
    ├── SystemError
    │
    ├── TypeError
    │
    ├── ValueError
    │   └── UnicodeError
    │       ├── UnicodeDecodeError
    │       ├── UnicodeEncodeError
    │       └── UnicodeTranslateError
    │
    ├── Warning
    │   ├── BytesWarning
    │   ├── DeprecationWarning
    │   ├── EncodingWarning
    │   ├── FutureWarning
    │   ├── ImportWarning
    │   ├── PendingDeprecationWarning
    │   ├── ResourceWarning
    │   ├── RuntimeWarning
    │   ├── SyntaxWarning
    │   ├── UnicodeWarning
    │   └── UserWarning
    │
    └── EnvironmentError  (устарел, alias OSError)

```

| Категория                                              | Описание                                                                              |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **BaseException**                                      | Корневой класс всех исключений в Python. Его обычно не ловят напрямую.                |
| **Exception**                                          | Корень всех "нормальных" ошибок, которые можно обрабатывать через `try/except`.       |
| **SystemExit, KeyboardInterrupt, GeneratorExit**       | Особые исключения, сигнализирующие об окончании работы интерпретатора или генератора. |
| **ExceptionGroup / BaseExceptionGroup (Python 3.11+)** | Позволяет группировать несколько исключений и обрабатывать их вместе.                 |
| **OSError и наследники**                               | Ошибки, связанные с операционной системой (файлы, сокеты, процессы).                  |
| **RuntimeError / TypeError / ValueError**              | Наиболее часто встречающиеся ошибки общего характера.                                 |
| **Warning**                                            | Не “фатальные” предупреждения; генерируются через `warnings.warn()`.                  |


