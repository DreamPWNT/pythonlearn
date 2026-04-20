def route_info(route):

    if 'distance' in route and isinstance(route['distance'], int):
        return f'Distance to your destination is {route['distance']}'
    elif 'time' in route and 'speed' in route:
        return f'Distance to your destination is {route['time'] * route['speed']}'
    else:
        return 'No distance info is available'


print(route_info({'a': 1}))
print(route_info({'distance': 1000}))
print(route_info({'speed': 110, 'time': 23}))
