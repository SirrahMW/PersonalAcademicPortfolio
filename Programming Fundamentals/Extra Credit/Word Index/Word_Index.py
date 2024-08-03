def word_index():
    # Dictionary for the words #
    indexDict = {}
    # Write each line to a list #
    with open('Kennedy.txt', 'r') as text:
        lineList = []
        for line in text:
            lineList.append(line.split())

    # Add the words to the dict using the index of the list as the line number #
    for i in range(len(lineList)):
        for word in lineList[i]:
            if word not in indexDict:
                indexDict[word] = [i+1]
            else:
                indexDict[word].append(i+1)

    # Change the lists to sets, to avoid duplicate line numbers #
    for key in indexDict:
        indexDict[key] = set(indexDict[key])

    # Sort the dict and write the formatted data to the new file #
    with open('KennedyIndex.txt', 'w') as newText:
        for key in sorted(indexDict):
            newText.write(key + ': ' + str(indexDict[key]).strip('{ , }') + '\n')


word_index()