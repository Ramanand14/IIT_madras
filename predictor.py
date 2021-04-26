### Custom definitions and classes if any ##
import pandas as pd

def predictRuns(testInput):
    prediction = 0
    ### Your Code Here ###
    
    #IPL team names list:
    #team = ['Chennai Super Kings', 'Delhi Capitals', 'Kolkata Knight Riders','Mumbai Indians', 'Punjab Kings', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad']

    data = pd.read_csv(r'C:\Users\Ramanand\OneDrive\Desktop\Python\inputFile.csv', squeeze = True)
    #calculation of total runs of bat
    r1 = data['runs_off_bat'].sum()
    #print('r1: '+str(r1))

    #batting team name taken from csv file and stored in 'name'
    bt = data['batting team']
    name = bt[0]

    #check for the batting team and set score1
    if(name == 'Chennai Super Kings'):
            score1 = 0
    elif(name == 'Delhi Capitals'):
            score1 = 0
    elif(name == 'Kolkata Knight Riders'):
            score1 = 0
    elif(name == 'Mumbai Indians'):
            score1 = 0
    elif(name == 'Punjab Kings'):
            score1 = 0
    elif(name == 'Rajasthan Royals'):
            score1 = 0
    elif(name == 'Royal Challengers Bangalore'):
            score1 = 0
    elif(name == 'Sunrisers Hyderabad'):
            score1 = 0

    #check for venue

    #sum of other type of runs
    r2 = data['extras'].sum() + data['wides'].sum() + data['noballs'].sum() + data['byes'].sum() + data['legbyes'].sum()
    #print('r2: '+str(r2))

    #average run rate from 6 overs
    avg_r = (r1 + r2)/6
    #print(avg_r)

    #predicted score for next 14 overs
    score2 = avg_r * 28
    #print(score2)

    #wicket factor

    prediction = (score1 + score2)/2
    return prediction
