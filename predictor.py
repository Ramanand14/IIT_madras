### Custom definitions and classes if any ###
import pandas as pd
import numpy as np

def predictRuns(testInput):
    prediction = 0

    ### Your Code Here ###
    #Open both the csv file in read mode:
    file1 = pd.read_csv(r'inputFile.csv', squeeze = True)
    file2 = pd.read_csv(r'dataset.csv', squeeze = True)

    #Take bating team name from inutFile.csv and store it into bt:
    team1 = file1['batting team']
    bt1 = team1[0]

    #Taking bowling team name from inputFile.csv and store it into bt2:
    team2 = file1['bowling team']
    bt2 = team2[0]

    #Check the score1 when both the teams are against to each other into dataset.csv file:
    ck1 = file2['score']

    if(bt1 == 'Chennai Super Kings'):
        set1 = file2[0:7]['team2']
        count = 0
        for name in set1:
            if(str(bt2) == name):
                break
            else:
                count += 1
        score1 = ck1[count]
    elif(bt1 == 'Royal Challengers Bangalore'):
        count = 8
        set2 = file2[8:14]['team2']
        for name in set2:
            if(str(bt2) == name):
                break
            else:
                count += 1
        score1 = ck1[count]
    elif(bt1 == 'Delhi Capitals'):
        count = 15
        set3 = file2[15:21]['team2']
        for name in set3:
            if(str(bt2) == name):
                break
            else:
                count += 1
        score1 = ck1[count]
    elif(bt1 == 'Mumbai Indians'):
        count = 22
        set4 = file2[22:28]['team2']
        for name in set4:
            if(str(bt2) == name):
                break
            else:
                count += 1
        score1 = ck1[count]
    elif(bt1 == 'Sunrisers Hyderabad'):
        count = 29
        set5 = file2[29:35]['team2']
        for name in set5:
            if(str(bt2) == name):
                break
            else:
                count += 1
        score1 = ck1[count]
    elif(bt1 == 'Kolkata Knight Riders'):
        count = 36
        set6 = file2[36:42]['team2']
        for name in set6:
            if(str(bt2) == name):
                break
            else:
                count += 1
        score1 = ck1[count]
    elif(bt1 == 'Rajasthan Royals'):
        count = 43
        set7 = file2[43:49]['team2']
        for name in set7:
            if(str(bt2) == name):
                break
            else:
                count += 1
        score1 = ck1[count]
    elif(bt1 == 'Punjab Kings'):
        count = 50
        set8 = file2[50:56]['team2']
        for name in set8:
            if(str(bt2) == name):
                break
            else:
                count += 1
        score1 = ck1[count]
    else:
        print('Incorrect or improper team name!!!')
        prediction = 0
        return prediction

    #Generate the random number to predict the score:
    num = np.random.randint(low=1, high=8, size=1)

    #Set total number of balls:
    tb = 36
    wb = 0
    lb = 0
    nb = 0
    #Check for the extra runs scored:
    if(num<4):
        wb = 1
        tb += 1
        nb = 1
    
    if(num>4):
        wb = 2
        tb += 2
        nb = 1
        lb = 1

    #Find the score2:
    score2 = wb + tb + nb + lb

    #Check for the possibility of the wickets:
    wicket = np.random.randint(low=0, high=4, size=1)

    #Check the condition for score1:
    if(wicket <= 1):
        score1 = score1 - (wicket * 3.5)

    if(wicket > 1):
        score1 = score1 + (wicket * 3.5)

    #Predict the score and return to main:
    prediction = (score1 + score2)/2

    return prediction