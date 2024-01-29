def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
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

file_path = input("Please enter the path of the file: ")

input_data = read_file(file_path)

result = count_word_frequency(input_data)

if result is not None:
    for word, count in result.items():
        print(f"{word} : {count}")