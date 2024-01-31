def read_file(path_of_file):
    try:
        with open(path_of_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {path_of_file}")
        return None

def count_word_frequency(text):
    if text is None:
        return None
    
    word_frequency = {}
    words = text.split()

    for word in words:
        word = word.strip(".!:").lower()
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency

path_of_file = input("Please enter the path of file: ")

input_data = read_file(path_of_file)

result = count_word_frequency(input_data)

if result is not None:
    for word, count in result.items():
        print(f"{word} : {count}")