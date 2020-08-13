import json
import os
import matplotlib.pyplot as plt
import pandas as pd

print('where are your .json files?')
ans = input

workoutsFiles = os.listdir(ans)
#print(workoutsFile)

workouts = []
for workoutFile in workoutsFiles:
    workouts.append(json.loads(open(ans+"/"+workoutFile).read()))
#print(workouts)
time = []
distance = []
spm = []
speed = []
date = []
splits = []

def calcSpeed(d, t):
    return(int(t/(d/500)))

def calcSplits(tm):
    minn = tm/60
    sec = (float(minn)-int(minn))*60
    if len(str(int(sec))) == 1:
        sec = "0{seconds}".format(seconds = int(sec))
    else:
        sec = int(sec)
    splt = "{minutes}:{seconds}/500m".format(minutes= int(minn), seconds = sec)
    return(splt)

for workout in workouts:
    if workout.get("outdoor") == True:
        Time = int(workout.get("runTime"))
        Distance = int(workout.get("distance"))
        Spm = int(workout.get("meanSPM"))
        Date = workout.get("startTime")[:10]
        #Date = datetime.datetime(int(Date[:4]), int(Date[5:7]), int(Date[8:10]))
        if Time != 0 and Distance != 0 and Spm != 0:
            time.append(Time/60)
            distance.append(Distance/1000)
            spm.append(Spm)
            date.append(Date)
            speed.append(calcSpeed(Distance, Time))
            splits.append(calcSplits(calcSpeed(Distance, Time)))
    

print(len(time), len(distance), len(time), len(splits), len(date), len(speed))

workoutsAnalitics = {
    "date": date,
    "distance": distance,
    "time": time,
    "splits": splits,
    "date": date,
    "speed": speed
}


with open('results.json', 'w') as f:
    json.dump(workoutsAnalitics, f)



analitics = pd.DataFrame(workoutsAnalitics)
analitics = analitics.sort_values(by='date',ascending=True)
analitics = analitics.reset_index()
analitics.pop("index")

analitics.to_json(r'analized.json')


while 1:
    print('What will you like to analize?')
    print("write 1 to see date")
    print("write 2 to see distance")
    print("write 3 to see time")
    print("write 4 to see splits")
    print("write 5 to see date")
    print("write 6 to see speed")
    ans = int(input())

    if(ans == 1): 
        plt.plot([1,2,3,4])
        plt.ylabel("date")
        plt.show()

    if(ans == 2):
        plt.plot(distance)
        plt.ylabel("distance")
        plt.show()

    if(ans == 3):
        plt.plot(time)
        plt.ylabel("time")
        plt.show()

    if(ans == 4):
        plt.plot(splits)
        plt.ylabel("splits")
        plt.show()

    if(ans == 5):
        plt.plot(date)
        plt.ylabel("date")
        plt.show()

    if(ans == 6):
        plt.plot(speed)
        plt.ylabel("speed")
        plt.show()
