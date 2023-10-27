def average(*args):
    avg = sum(args) / len(args)
    return avg


if __name__ == "__main__":
    print('Средгее арифметическое аргументов: ',
          average(1, 5, 8, 2345, 0, -689))