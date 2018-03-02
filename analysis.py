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
    print ("\nThese match predictions are " + str("%.2f" % accuracy) + "% accurate for " + str(num_matches) + " matches.")

#Function to determine teams that have the highest upset rate
def find_underdogs():
    underdog_dict = {}
    count = 0
    count_max = 5
    slated_to_lose = {}
    underdog_ratio_dict = {}
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
                        if not match[3] in slated_to_lose:
                            slated_to_lose[match[3]] = 1
                        else:
                            slated_to_lose[match[3]] += 1
                        if actual_two_win:
                            if not match[3] in underdog_dict:
                                underdog_dict[match[3]] = 1
                            else:
                                underdog_dict[match[3]] += 1
                    if projected_two_win:
                        if not match[2] in slated_to_lose:
                            slated_to_lose[match[2]] = 1
                        else:
                            slated_to_lose[match[2]] += 1
                        if actual_one_win:
                            if not match[2] in underdog_dict:
                                underdog_dict[match[2]] = 1
                            else:
                                underdog_dict[match[2]] += 1
                except ValueError:
                    continue
    for team in underdog_dict:
        underdog_ratio_dict[team] = (underdog_dict[team]/slated_to_lose[team])*100
    sorted_list = sorted(underdog_ratio_dict.items(), key=lambda x: x[1], reverse = True)
    print ("\nThese are the " + str(count_max) + " teams that have the highest upset percentage : ")
    for loop in sorted_list:
            print (str(loop[0]), "with a " + str("%.2f" %loop[1]) + "% upset rate, out of " + str(slated_to_lose[loop[0]]), "matches tbey were predicted to lose.")
            count += 1
            if count == count_max:
                break

check_accuracy()
find_underdogs()
