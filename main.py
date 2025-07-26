def format_indian_currency(amount):
    num_parts = str(amount).split('.')
    integer = num_parts[0]
    decimal = '.' + num_parts[1] if len(num_parts) > 1 else ''
    
    if len(integer) <= 3:
        return integer + decimal

    # First group is last 3 digits
    last_three = integer[-3:]
    rest = integer[:-3]
    rest_groups = []
    while len(rest) > 2:
        rest_groups.insert(0, rest[-2:])
        rest = rest[:-2]
    if rest:
        rest_groups.insert(0, rest)

    return ','.join(rest_groups + [last_three]) + decimal

# Example
# print(format_indian_currency(123456.7891))  # Output: 1,23,456.7891
