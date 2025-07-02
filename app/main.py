def main() -> None:
    # - When the app is launched, ask
    # the user to enter the file name.
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "a") as file:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file.write(content + "\n")

    # - When the name is provided,
    # ask to enter next line of the content
    # in a while loop until user enters `stop`.


if __name__ == "__main__":
    main()

# - When the user completes interaction,
# create a file with name and
# fill it with content provided by user.
# File extension should be `txt`.
#
# Example:
# ```python
# Enter name of the file: name1
# Enter new line of content:
# This is the first line of content
# Enter new line of content:
# This is the second
# Enter new line of content: stop
# # File name: "name1.txt"
# # File content:
# # This is the first line of content
# # This is the second
# ```
