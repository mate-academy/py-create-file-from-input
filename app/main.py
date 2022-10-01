def main():
    filename = input('Enter name of the file: ')

    with open(f'{filename}.txt', 'a') as f:
        while True:
            prompt = input('Enter new line of content: ')

            if prompt == 'stop':
                break

            f.write(prompt + '\n')


if __name__ == "__main__":
    main()
