MINUTES_TARIFF_QUANTITY = 50
SMS_TARIFF_QUANTITY = 50
TARIFF_COST = 15.00
ADDITIONAL_MINUTE_COST = 0.25
ADDITIONAL_SMS_COST = 0.15
TAX_911 = 0.44
TAX_GENERAL = 0.05

minutes_quantity = int(input('Enter spent minutes: '))
sms_quantity = int(input('Enter spent sms: '))

additional_minutes = 0
additional_minutes_sum = 0.0
additional_sms = 0
additional_sms_sum = 0.0

overrun = False

if minutes_quantity <= MINUTES_TARIFF_QUANTITY and sms_quantity <= SMS_TARIFF_QUANTITY:
    tariff_sum = TARIFF_COST
elif minutes_quantity > MINUTES_TARIFF_QUANTITY and sms_quantity <= SMS_TARIFF_QUANTITY:
    additional_minutes = minutes_quantity - MINUTES_TARIFF_QUANTITY
    additional_minutes_sum = additional_minutes * ADDITIONAL_MINUTE_COST
    tariff_sum = TARIFF_COST + additional_minutes_sum

    overrun = True
elif minutes_quantity <= MINUTES_TARIFF_QUANTITY and sms_quantity > SMS_TARIFF_QUANTITY:
    additional_sms = sms_quantity - SMS_TARIFF_QUANTITY
    additional_sms_sum = additional_sms * ADDITIONAL_SMS_COST
    tariff_sum = TARIFF_COST + additional_sms_sum

    overrun = True
else:
    additional_minutes = minutes_quantity - MINUTES_TARIFF_QUANTITY
    additional_minutes_sum = additional_minutes * ADDITIONAL_MINUTE_COST
    additional_sms = sms_quantity - SMS_TARIFF_QUANTITY
    additional_sms_sum = additional_sms * ADDITIONAL_SMS_COST
    tariff_sum = TARIFF_COST + additional_minutes_sum + additional_sms_sum

    overrun = True

print(f'Base tariff = {TARIFF_COST}$')

if overrun:
    print(
        f'Additional minutes cost = {additional_minutes_sum}$, additional sms cost = {additional_sms_sum}$')

print(f'Call center 911 tax = {TAX_911}$')
print(f'General tax = {(tariff_sum + TAX_911) * TAX_GENERAL}$')
print(
    f'Full sum = {tariff_sum + TAX_911 + (tariff_sum + TAX_911) * TAX_GENERAL}$')
