from lib import get_user_space, recent_files

def main(prompt):
    time_stamp = (int(input(prompt) or 5) + 5) * 60  # +5 на запас

    for path in get_user_space():
        recent_files(path, time_stamp)


if __name__ == "__main__":
    prompt = """Введите сколько минут назад был создан файл (примерно),"""\
    """\nили пустой ввод если 5 минут.\n>> """
    main(prompt)
