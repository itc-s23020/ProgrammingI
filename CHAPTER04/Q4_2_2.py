def pern_sequence(limit=100):
    sequence = [3, 0, 2]

    while True:
        next_number = sequence[-2] + sequence[-3]
        if next_number >= limit:
            break
        sequence.append(next_number)

    return sequence


result = pern_sequence()
print(result)
