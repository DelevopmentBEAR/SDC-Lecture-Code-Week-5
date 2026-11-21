try:
    with open('data.txt') as data_file:
        conents = data_file.read()
        print(conents)
    # data_file.close()
except FileNotFoundError:
    print('Sorry, file not found.')