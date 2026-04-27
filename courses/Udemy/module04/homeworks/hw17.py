phones = ["0-000-0000-005", "0-000-0000-002", "0-000-0000-007",
          "0-000-0000-005", "0-000-0000-005", "0-000-0000-002", "0-000-0000-007",]

unique = []

for phone in phones:
    if not phone in unique:
        unique.append(phone)

print(unique)
