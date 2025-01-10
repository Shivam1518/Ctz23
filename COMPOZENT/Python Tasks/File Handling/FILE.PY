def count_words_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()
            word_count = len(text.split())
        
        with open(output_file, 'w') as file:
            file.write(f"Word Count: {word_count}\n")
        
        print(f"Word count written to {output_file}.")
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")

# Example usage
count_words_in_file('input.txt', 'output.txt')