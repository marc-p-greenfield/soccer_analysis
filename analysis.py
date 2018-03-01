import csv

count_of_wrong = 0
num_matches = 0

with open('spi_matches.csv','r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    reader_list = list(reader)
    num_matches = len(reader_list)
    for index in range(1,num_matches):
        match = reader_list[index]
        if match[11] is not None and match[12] is not None:
            try:
            projected_one_win = float(match[6]) > float(match[7])
            actual_two_win = float(match[12]) > float(match[11])
            actual_tie = float(match[12]) == float(match[11])
            if projected_one_win:
                if actual_two_win or actual_tie:
                    count_of_wrong += 1

percent_wrong = count_of_wrong/num_matches
print (percent_wrong)
