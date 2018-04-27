##takes input of voting records csv file and outputs results of election##

import csv


with open('election_data_2.csv','r') as csvfile:            #open csv file with voting data
    reader = csv.reader(open('election_data_2.csv'))        #read the file into a way we can manipulate
    VoteDict = {}                                           #empty dictionary for storing unique vote IDs paired with the candidate they voted for
    for row in reader:
        i, c, v = row                                       #split columns into values
        VoteDict[i] = v                                     #don't need county data, dictionary only need contain id : candidate, assign this and add to dictionary for all data
    del VoteDict["Voter ID"]                                #trim off the top row of labels!
    
    TotalVotes = len(VoteDict)                              #count total number of votes from the voter IDs in the dictionary
    VoteCounter = {}                                        #list to be populated with candidate names

    for value in VoteDict.values():                         #search all the votes for unique candidate names. When found, start up a vote counter in the dictionary as a value for the unique candidate's key
        if not value in VoteCounter:
            VoteCounter[value] = 1
        else:
            VoteCounter[value] =  VoteCounter[value] + 1

    Winner = ""
    PopVote = 0
    for key, value in VoteCounter.items():                  #iterate through dictionary to determine the winner, also figure out vote percentages and add to values
        if VoteCounter[key] > PopVote:
            PopVote = VoteCounter[key]
            Winner = key
        VoteCounter[key] = [value] + [round(100*(value/TotalVotes),2)]

    print("Election Results")                               #print results to kernal
    print("-------------------------")
    for candidate in VoteCounter:
        print( candidate + ":  " + str(VoteCounter[candidate][1]) + "% (" + str(VoteCounter[candidate][0]) + ")")
    print("-------------------------")
    print("Winner: " + Winner)
    print("-------------------------")


    resultsfile = "output.txt"                             #output file path

    with open(resultsfile,'w') as textfile:                #write results to new file

        #write text to file 
        textfile.write("-------------------------/n")
        for candidate in VoteCounter:
           textfile.write(candidate + ":  " + str(VoteCounter[candidate][1]) + "% (" + str(VoteCounter[candidate][0] + "/n")
        textfile.write("-------------------------/n")
        textfile.write("Winner: " + Winner + "/n")
        textfile.write("-------------------------")
    
    with open(resultsfile,"r") as textfile:
        print(textfile.read())

    
