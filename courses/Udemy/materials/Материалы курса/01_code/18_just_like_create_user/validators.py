def validate_username(text: str):
    prompt = ""
    status = False

    if len(text) == 0 or text.isspace():
        prompt = "Имя не может быть пустой строкой"

    elif not text.isidentifier():
        prompt = "Имя должно начинаться с букв ..."
    
    else:
        status = True

    return prompt, status


def validate_password(text: str):
    prompt = ""
    status = False

    if len(text) < 8:
        prompt = "Пароль не может быть менее 8 символов"

    elif text.isalpha():
        prompt = "Пароль должен содержать еще и числа, как минимум"
    
    else:
        status = True

    return prompt, status