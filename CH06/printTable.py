# Print a right justified table of data

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(tData):
    #colWidths = [0]*len(tableData)
    colWidths = []

    for row in tData:
        lengths_of_words = []
        for item in row:
            lengths_of_words.append(len(item))
        colWidths.append(max(lengths_of_words))

    max_width = max(colWidths) + 2 
    print(row,lengths_of_words,colWidths,max_width)

    # Print the data with max width
    print(' Table Data '.center(3*max_width,'='))
    for row in tData:
        for i in range(0,len(row)):
            print(' ', end='')
            print(row[i].rjust(max_width))
    print('/n')

    # Print the data with max width
    print(' Table Data '.center(4*max_width,'='))
    for row in tData:
        #print(' ', end='')
        print(row[0].rjust(max_width) + row[1].rjust(max_width) 
            + row[2].rjust(max_width) + row[3].rjust(max_width))

printTable(tableData)
