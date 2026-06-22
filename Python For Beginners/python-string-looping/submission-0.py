def print_string_characters(my_string: str) -> None:
    length = len(my_string)
    for i in range(length):
        print(my_string[i])

# do not modify below this line
my_string = "Hello, World!\nGood Job!"
print_string_characters("Hello, World!")
print_string_characters("Good Job!")