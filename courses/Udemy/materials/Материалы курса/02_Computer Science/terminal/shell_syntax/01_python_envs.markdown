# Переменные окружения Python: Полный справочник

> Все переменные можно задать в оболочке перед запуском:
>
> ```bash
> export PYTHONPATH=/my/libs
> python my_script.py
> ```

---

> Стрелкой `<--` помечены те, которые вам скорее всего пригодятся в работе.
> Остальные используются очень редко, а некоторые только при разработке самого python.

## 1. Пути и загрузка модулей

| Переменная        | Назначение | Пример использования |
|-------------------|------------|-----------------------|
| `PYTHONPATH` `<--` | Дополнительные пути поиска модулей (`sys.path`). | `PYTHONPATH=./libs python script.py` |
| `PYTHONHOME` `<--?` | Указывает альтернативный `prefix`/`exec_prefix`. | `PYTHONHOME=/opt/custom_python` |
| `PYTHONUSERBASE` | Меняет каталог `--user` установки пакетов. | `PYTHONUSERBASE=~/.local_custom pip install --user package` |
| `PYTHONNOUSERSITE` | Отключает загрузку пользовательских `site-packages`. | `PYTHONNOUSERSITE=1 python script.py` |
| `PYTHONPYCACHEPREFIX` | Меняет путь для `.pyc` файлов. | `PYTHONPYCACHEPREFIX=/tmp/pycache python script.py` |

---

## 2. Поведение интерпретатора

| Переменная | Назначение | Пример использования |
|------------|------------|----------------------|
| `PYTHONDONTWRITEBYTECODE` `<--` | Отключает создание `.pyc`. | `PYTHONDONTWRITEBYTECODE=1 python script.py` |
| `PYTHONUNBUFFERED` `<--`  | Отключает буферизацию stdout/stderr. | `PYTHONUNBUFFERED=1 python script.py > log.txt` |
| `PYTHONINSPECT` | Открывает интерактивную консоль после выполнения скрипта. | `PYTHONINSPECT=1 python script.py` |
| `PYTHONOPTIMIZE` | Аналог `-O` или `-OO`. | `PYTHONOPTIMIZE=1 python script.py` |
| `PYTHONNOOPT` | Отключает оптимизации (перекрывает `PYTHONOPTIMIZE`). | `PYTHONNOOPT=1 python script.py` |
| `PYTHONDEBUG` | Аналог `-d`, включает отладочные сообщения. | `PYTHONDEBUG=1 python script.py` |
| `PYTHONVERBOSE` | Аналог `-v`, показывает импорты. | `PYTHONVERBOSE=1 python script.py` |
| `PYTHONIOENCODING` `<--`  | Устанавливает кодировку ввода/вывода. | `PYTHONIOENCODING=utf-8 python script.py` |
| `PYTHONBREAKPOINT` | Меняет функцию `breakpoint()`. | `PYTHONBREAKPOINT=ipdb.set_trace python script.py` |
| `PYTHONHASHSEED` | Контролирует инициализацию хешей. | `PYTHONHASHSEED=42 python script.py` |
| `PYTHONSTARTUP` | Загружает скрипт при старте REPL. | `PYTHONSTARTUP=~/.pythonrc.py python` |

---

## 3. Отладка и профилирование

| Переменная | Назначение | Пример использования |
|------------|------------|----------------------|
| `PYTHONFAULTHANDLER` | Включает fault handler. | `PYTHONFAULTHANDLER=1 python script.py` |
| `PYTHONTRACEMALLOC` | Включает трассировку аллокаций. | `PYTHONTRACEMALLOC=5 python script.py` |
| `PYTHONPROFILEIMPORTTIME` | Показывает время импорта модулей. | `PYTHONPROFILEIMPORTTIME=1 python script.py` |
| `PYTHONASYNCIODEBUG` | Включает отладку `asyncio`. | `PYTHONASYNCIODEBUG=1 python script.py` |
| `PYTHONDEVMODE` | Включает режим разработки (`-X dev`). | `PYTHONDEVMODE=1 python script.py` |

---

## 4. Управление памятью и безопасностью

| Переменная | Назначение | Пример использования |
|------------|------------|----------------------|
| `PYTHONMALLOC` | Меняет стратегию аллокации (`pymalloc`, `malloc`, `debug`). | `PYTHONMALLOC=debug python script.py` |
| `PYTHONINTMAXSTRDIGITS` | Лимит на длину int→str (защита от DoS). | `PYTHONINTMAXSTRDIGITS=1000 python script.py` |

---

## 5. Расширенные и экспериментальные опции (`-X`)

| Переменная | Назначение | Пример использования |
|------------|------------|----------------------|
| `PYTHONXOPTIONS` | Параметры как `-X`: `dev`, `utf8`, `tracemalloc`, и др. | `PYTHONXOPTIONS="utf8,tracemalloc=2"` |

---

## 6. Виртуальные окружения и фреймворки

| Переменная | Назначение | Пример использования |
|------------|------------|----------------------|
| `PYTHONEXECUTABLE` | Указывает путь к Python в виртуалке. | `PYTHONEXECUTABLE=/my/venv/bin/python` |
| `VIRTUAL_ENV` `<--` | Путь к активированному виртуальному окружению. | `VIRTUAL_ENV=~/venv` |
| `PYTHONFROZEN` | Отметка "замороженного" приложения. | `PYTHONFROZEN=1 ./myapp.exe` |

---

## 7. Управление предупреждениями

| Переменная | Назначение | Пример использования |
|------------|------------|----------------------|
| `PYTHONWARNINGS` | Уровни предупреждений (`error`, `ignore`, `default` и пр). | `PYTHONWARNINGS=ignore::DeprecationWarning` |

---

## 8. Специфично для модулей (внешние инструменты)

### pip

| Переменная | Назначение |
|------------|------------|
| `PIP_INDEX_URL` | Указывает основной PyPI-репозиторий. |
| `PIP_EXTRA_INDEX_URL` | Дополнительные источники пакетов. |
| `PIP_NO_CACHE_DIR` `<--` | Отключает кэширование скачаных/установленных библиотек |
| `PIP_DISABLE_PIP_VERSION_CHECK` | Не проверять обновления. |

### pytest

| Переменная | Назначение |
|------------|------------|
| `PYTEST_ADDOPTS` | Аргументы, добавляемые ко всем запускам. |
| `PYTEST_DISABLE_PLUGIN_AUTOLOAD` | Отключает автозагрузку плагинов. |

---

## Пример использования нескольких переменных(sh/bash/zsh):
См. ниже объяснение.

```bash
PYTHONPATH=./libs \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
python my_script.py
```


## Как устанавливать переменные окружения

Переменные окружения можно задавать **временно для одной команды** или **постоянно для текущей сессии**. Способ зависит от используемой оболочки.

---

### Bash / Zsh / sh (Linux, macOS, WSL)

#### Временно для одной команды (все в одной команде):
```bash
PYTHONPATH=./libs PYTHONDONTWRITEBYTECODE=1 python my_script.py
````

Или с переносами строк:

```bash
PYTHONPATH=./libs \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
python my_script.py
```

Переменные действуют **только для этой команды**. После выполнения не сохраняются.

---

#### Постоянно для текущей сессии:

```bash
export PYTHONPATH=./libs
export PYTHONDONTWRITEBYTECODE=1
python my_script.py
```

Переменные сохраняются до выхода из терминала. Чтобы удалить:

```bash
unset PYTHONPATH
```

---

### CMD (Windows)

#### Временно для одной команды НЕЛЬЗЯ.
Можно только в строку как последовательность команд, но переменные окружения будут созданы для текущей сессии терминала и в процесс python будут просто унаследованы.


```cmd
set PYTHONPATH=.\libs && set PYTHONDONTWRITEBYTECODE=1 && python my_script.py
```

---

#### То же самое, просто поочереди:

```cmd
set PYTHONPATH=.\libs
set PYTHONDONTWRITEBYTECODE=1
python my_script.py
```

Переменные сохраняются до закрытия окна `cmd`. Чтобы удалить:

```cmd
set PYTHONPATH=
```

---

### PowerShell (Windows)

#### Временно для одной команды НЕЛЬЗЯ.
Можно только в строку как последовательность команд, но переменные окружения будут созданы для текущей сессии терминала и в процесс python будут просто унаследованы.

```powershell
$env:PYTHONPATH = ".\libs"; $env:PYTHONDONTWRITEBYTECODE = "1"; python my_script.py
```

---

#### Тоже самое, просто поочереди:

```powershell
$env:PYTHONPATH = ".\libs"
$env:PYTHONDONTWRITEBYTECODE = "1"
python my_script.py
```

Переменные сохраняются до закрытия окна PowerShell. Чтобы удалить:

```powershell
Remove-Item Env:PYTHONPATH
```

---

