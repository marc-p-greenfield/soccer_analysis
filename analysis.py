import csv

#Function to check accuracy of the five-thirty-eight projections
def check_accuracy():
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
                    projected_two_win = float(match[7]) > float(match[6])
                    actual_one_win = float(match[11]) > float(match[12])
                    actual_two_win = float(match[12]) > float(match[11])
                    actual_tie = float(match[12]) == float(match[11])
                    if projected_one_win:
                        if actual_two_win or actual_tie:
                            count_of_wrong += 1
                    if projected_two_win:
                        if actual_one_win or actual_tie:
                            count_of_wrong += 1
                except ValueError:
                    continue

    percent_wrong = count_of_wrong/num_matches
    accuracy = (1 - percent_wrong)*100
    print ("These match predictions are " + str("%.2f" % accuracy) + "% accurate for " + str(num_matches) + " matches.")

#Function to determine teams that upset the most
def find_underdogs():
    underdog_dict = {}
    count = 0
    with open('spi_matches.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        reader_list = list(reader)
        num_matches = len(reader_list)
        for index in range(1,num_matches):
            match = reader_list[index]
            if match[11] is not None and match[12] is not None:
                try:
                    projected_one_win = float(match[6]) > float(match[7])
                    projected_two_win = float(match[7]) > float(match[6])
                    actual_one_win = float(match[11]) > float(match[12])
                    actual_two_win = float(match[12]) > float(match[11])
                    actual_tie = float(match[12]) == float(match[11])
                    if projected_one_win:
                        if actual_two_win:
                            if not match[3] in underdog_dict:
                                underdog_dict[match[3]] = 1
                            else:
                                underdog_dict[match[3]] += 1
                    if projected_two_win:
                        if actual_one_win:
                            if not match[2] in underdog_dict:
                                underdog_dict[match[2]] = 1
                            else:
                                underdog_dict[match[2]] += 1
                except ValueError:
                    continue
    sorted_list = sorted(underdog_dict.items(), key=lambda x: x[1], reverse = True)
    print ("These are the top 3 teams that upset the most: ")
    for x in sorted_list:
            print (x[0], x[1])
            count += 1
            if count == 3:
                break

check_accuracy()
find_underdogs()
