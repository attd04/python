
def decode(message_file):
    with open (message_file) as qual:
        data = qual.readlines()

    message_dict = {}
    final_message = []

    for message in data:
        number = (message.split())[0]
        number = (int(number))
        word = (message.split())[1]
        message_dict.update({number: word})

    word_number = 1
    count = 2
    while word_number < len(message_dict):
        final_message.append(message_dict[word_number])
        word_number += count
        count += 1

    decoded_message = ' '.join(final_message)
    return(decoded_message)

result = decode(message_file="coding_qual_input.txt")
print(result)

