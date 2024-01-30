# Decode message - Data Annotation

def decode(message_file):

    # -- helper functions --
    # removes line break
    def delete_n(pair):
        stretched = list(pair)
        if stretched[-1] == '\n':
            stretched.pop()
        return ''.join(stretched)

    # creates key sequence in pyramid
    def increment_range(start, stop, step):
        value = start
        while value < stop:
            yield value
            value += step
            step += 1

    try:
        # open txt file
        data =  open(f"./{message_file}", "r")

        # parse and clean line breaks
        parsed = []
        for line in data:
            if line != '\n':
                cleansed = delete_n(line)
                parsed.append(cleansed)
            
        # enter key value pairs into dictionary
        data_dict = {}
        for entry in parsed:
            pair = entry.split(' ')
            data_dict[int(pair[0])] = pair[1]

        # generate decode key sequence
        my_keys = list(increment_range(0, len(parsed), 1))

        # decode message
        message = []
        for key in my_keys:
            if key not in data_dict.keys():
                continue
            message.append(data_dict[key])
            message.append(' ')

        # return decoded message
        return ''.join(message)

    # handle error
    except:
        print("Failed.")

print(decode("my_data.txt"))

