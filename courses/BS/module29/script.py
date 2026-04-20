button = {
    'width': 200,
    'text': 'Buy',
    'color': 'grey'
}

red_button = {
    **button,
    'color': 'red'
}

print(button)
print(red_button)

red_button = {
    'color': 'red',
    **button
}

print(red_button)

button_info = {
    'text': 'Buy',
    'color': 'black',
    'width': 0,
    'height': 0
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300
}

button = {
    **button_info,
    **button_style
}

print(button)
print(button_info | button_style)
print(button_style | button_info)
