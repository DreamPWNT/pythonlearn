# Политика выполнения PowerShell (Execution Policy)

## Почему появляется ошибка
При попытке запуска `.ps1` может появиться:
```

File C:\path\myscript.ps1 cannot be loaded because running scripts is disabled on this system.

````
Это значит, что **Execution Policy** запрещает выполнение скриптов в текущем контексте.  
По умолчанию в Windows у новых пользователей - `Restricted` или `RemoteSigned`.

---

## Виды политик выполнения

```powershell
Get-ExecutionPolicy
Get-ExecutionPolicy -List  # Показать все уровни
````

| Политика         | Описание                                                      |
| ---------------- | ------------------------------------------------------------- |
| **Restricted**   | Запрет всех скриптов. Можно только команды вручную.           |
| **AllSigned**    | Разрешены только подписанные скрипты доверенным издателем.    |
| **RemoteSigned** | Локальные скрипты без подписи, скачанные — только с подписью. |
| **Unrestricted** | Любые скрипты, но скачанные — с предупреждением.              |
| **Bypass**       | Нет проверок и предупреждений.                                |
| **Undefined**    | Политика не задана (наследуется).                             |

---

## Уровни применения политики

* **Process** — только для текущей сессии PowerShell.
* **CurrentUser** — для конкретного пользователя.
* **LocalMachine** — для всех пользователей системы.

---

## Как временно обойти ограничение

**Для одного запуска:**

```powershell
powershell -ExecutionPolicy Bypass -File .\myscript.ps1
```

**В текущей сессии:**

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Перемены исчезнут после закрытия окна.

---

## Как поменять политику “навсегда” (для себя)

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

* `RemoteSigned` — безопасный компромисс: локальные `.ps1` без подписи, скачанные — с подписью.

---

## Что лучше делать

| Ситуация                  | Рекомендация                                           |
| ------------------------- | ------------------------------------------------------ |
| Один раз запустить скрипт | `-ExecutionPolicy Bypass -File` или `Scope Process`    |
| Часто пишете свои скрипты | `RemoteSigned` для `CurrentUser`                       |
| Корпоративная среда       | `AllSigned` с сертификатами                            |
| Автоматизация на сервере  | `Unrestricted` или `Bypass` **только в закрытой сети** |

---

## Рекомендации

* **Не трогайте** глобальную политику `LocalMachine` без крайней необходимости.
* Для личной машины — `RemoteSigned` на уровне `CurrentUser`.
* Для единичного запуска — `Bypass` через `Process` или параметр `-ExecutionPolicy`.
