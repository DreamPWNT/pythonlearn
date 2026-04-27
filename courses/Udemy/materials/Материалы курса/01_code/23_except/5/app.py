

import subprocess
import sys

host = "google.com"
is_windows = sys.platform.startswith("win")
count_flag = "-n" if is_windows else "-c"

try:
    proc = subprocess.run(
        ["ping", count_flag, "1", host],
        capture_output=True,
        check=True  # если процесс завершится с sys.exit(не ноль) то CalledProcessError
    )
except FileNotFoundError:
    print("❌ Команда ping не найдена в системе")
except subprocess.CalledProcessError as e:
    print("❌ Хост недоступен, код ошибки:", e.returncode)
else:
    print("✅ Хост доступен, вывод:")
    print(proc.stdout.decode("utf-8") if not is_windows else proc.stdout.decode("cp866"))
finally:
    print("🏁 Проверка завершена")

