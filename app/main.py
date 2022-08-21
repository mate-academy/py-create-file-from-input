def main():
    file_name = input('Enter name of the file: ')
    with open(f'{file_name}.txt', 'w') as f:
        while True:
            content = input('Enter new line of content: ')
            if content == 'stop':
                break
            print(content, file=f)


if __name__ == "__main__":
    main()
