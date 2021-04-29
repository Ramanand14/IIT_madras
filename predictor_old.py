### Custom definitions and classes if any ###
import pandas as pd

def predictRuns(testInput):
    prediction = 0

    ### Your Code Here ###
    data = pd.read_csv(r'C:\Users\Ramanand\OneDrive\Desktop\Python\inputFile.csv', squeeze = True)
    
    #calculation of total runs of bat
    r1 = data['runs_off_bat'].sum()
    #print('r1: '+str(r1))

    #batting team name taken from csv file and stored in 'name'
    bt = data['batting team']
    name = bt[0]

    #check for the batting team and set score1
    if(name == 'Chennai Super Kings'):
            score1 = 112.5
    elif(name == 'Delhi Capitals'):
            score1 = 110
    elif(name == 'Kolkata Knight Riders'):
            score1 = 101.33
    elif(name == 'Mumbai Indians'):
            score1 = 113.5
    elif(name == 'Punjab Kings'):
            score1 = 120
    elif(name == 'Rajasthan Royals'):
            score1 = 100
    elif(name == 'Royal Challengers Bangalore'):
            score1 = 95
    elif(name == 'Sunrisers Hyderabad'):
            score1 = 108.66
    else:
        print('Incorrect or improper team name!!!')
        prediction = 0
        return prediction

    #sum of other type of runs
    r2 = data['extras'].sum() + data['wides'].sum() + data['noballs'].sum() + data['byes'].sum() + data['legbyes'].sum()
    #print('r2: '+str(r2))

    #average run rate from 6 overs
    avg_r = (r1 + r2)/6
    #print(avg_r)

    #predicted score for next 14 overs
    score2 = avg_r * 28
    #print(score2)

    #total number of wickets
    count = 0
    w = data['wicket_type']
    for n in w:
        if(isinstance(n, str) == True):
                count += 1
    #print(count)

    #check how wicket affect the scoreboard
    if(count < 4):
        dn = count * 3
        score2 = score2 - dn
        #print(dn)
        #print(score2)

    if(count >= 4):
        dn = count * 3
        score2 = score2 + dn
        #print(dn)
        #print(score2)

    #predict the score and return to main
    prediction = (score1 + score2)/2
    return prediction
