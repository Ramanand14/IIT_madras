### Custom definitions and classes if any ###
import pandas as pd

def predictRuns(testInput):
    prediction = 0
    ### Your Code Here ###
    
    #IPL team names list:
    team = ['Chennai Super Kings', 'Delhi Capitals', 'Kolkata Knight Riders','Mumbai Indians', 'Punjab Kings', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad']

    data = pd.read_csv(r'C:\Users\Ramanand\OneDrive\Desktop\Python\inputFile.csv', squeeze = True)
    #Total runs calculation and display
    sum = data['runs_off_bat'].sum()
    print('Addition: '+str(sum))

    #batting team name stored in name
    bt = data['batting team']
    name = bt[0]

    for n in team:
        if(n == name):
            print(name)
    
    return prediction