def merge_lists_to_dict(first_list_to_pack, second_list_to_pack):
    merged_list = zip(first_list_to_pack,
                      second_list_to_pack)

    return dict(merged_list)


print(merge_lists_to_dict([3, 5, 7, 2, 6, 10], second_list_to_pack=[
      'a', 'vodka', 'seledka', 'huyodka', 'shaverma', 'shshlik-mashlik']))


def update_car_info(**car):
    car['is_available'] = True

    return car


print(update_car_info(brand='Mercedes', price='5500000$'))
