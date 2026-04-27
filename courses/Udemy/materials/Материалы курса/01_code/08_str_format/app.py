name = 'Alex'
rating = 4.95124

# message = f'Hello {name}, your id is: {rating:.2f}'
# print(message)

# message = 'Hello {}, your id is: {:.2f}'.format(name, rating)
# print(message)

# message = 'Hello {n}, your id is: {r:.2f}'.format(n=name, r=rating)
# print(message)

# # Старый стиль
# message = 'Hello %s, your id is: %.2f' % (name, rating)
# print(message)




# message = 'Hello {n}, your id is: {r:.2f}'
message = input()

message = message.format(n=name, r=rating)
print(message)