if __name__ == '__main__':
    with open('standard_input.txt', 'r') as file:
        inputData = file.read().split('\n')
    word_field = inputData[:8]
    word_count = int(inputData[8])
    dictionary = inputData[9:]
    output = []

    for i in range(word_count):
        for j in range(len(dictionary)):
            if word_field[i] == dictionary[j] or word_field[i] == dictionary[j][::-1]:
                row = ' '.join([str(j + 1) for _ in word_field])
                output.append(row)

    with open('standard_output.txt', 'w') as file:
        file.write('\n'.join(output))
