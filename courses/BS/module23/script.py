def sum_nums(*args):
    print(args)
    print(type(args))
    print(args[1])

    return sum(args)


print(sum_nums(3, 5, 7, 3, 267, 87, 32, 32, 56, 67))


def get_posts_info(name, posts_qty):
    info = f'{name} wrote {posts_qty} posts'

    return info


info = get_posts_info('Vasisualiy', 33)

print(info)

info = get_posts_info(name='Fedor', posts_qty=222)

print(info)


def get_posts_info_2(**person):
    print(person)
    print(type(person))

    info = (
        f'{person['name']} wrote '
        f'{person['posts_qty']} posts'
    )

    return info


info = get_posts_info_2(name='Muhamed', posts_qty=13131, id=5353)

print(info)
