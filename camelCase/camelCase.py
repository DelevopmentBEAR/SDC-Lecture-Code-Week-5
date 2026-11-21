def camel_case(sentence):
    # Convert sentence into camel case and return
    words = sentence.split()
    return ''.join(word.lower() for word in words)
    
def main():
    sentence = input('Enter your sentence: ')
    camel_case = camel_case(sentence)
    print(camel_case)

if __name__ == '__main__':
    main()