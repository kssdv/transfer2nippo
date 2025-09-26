# Create and write to a text file
with open("./data/example.txt", "w") as file:
    file.write("Hello, this is a new text file!")
    for i in range(10):
        file.write(f'{i}\n')