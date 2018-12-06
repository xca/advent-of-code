import re
from datetime import datetime, timedelta
from collections import OrderedDict

with open('input.txt') as f:
    lines = f.readlines()
# lines are out of order need to put all lines in order based on time

events = dict()
for line in lines:
    dates = re.match(r'\[(\d+-\d+-\d+\s\d+:\d+)\]', line, re.M | re.I)
    if dates:
        date = datetime.strptime(dates.group(1), '%Y-%m-%d %H:%M')
        # print(date)
        if date.hour == 23:
            # print("update date to the next day")
            date += timedelta(days=1)
            date = date.replace(hour=0, minute=0)
        events[date] = line.split('] ')[1]
        events[date] = line.split('] ')[1]

sortedEvents = OrderedDict(sorted(events.items()))
# print(sortedEvents)

gSleepTime = dict()
gSleepList = dict()
eventsTime = list(sortedEvents.keys())
totalEvents = len(eventsTime)
# print(eventsTime)
i = 0
while i < totalEvents:
    if 'Guard' in sortedEvents[eventsTime[i]]:
        # print(sortedEvents[eventsTime[i]])
        idMatch = re.match(
            r'Guard #(\d+)', sortedEvents[eventsTime[i]], re.M | re.I)
        if idMatch:
            id = idMatch.group(1)
            if id not in gSleepTime:
                gSleepTime[id] = 0
                gSleepList[id] = [0] * 60
            i += 1
            while i < totalEvents and 'Guard' not in sortedEvents[eventsTime[i]]:
                # print(sortedEvents[eventsTime[i]])
                if 'falls asleep' in sortedEvents[eventsTime[i]] :
                    start = eventsTime[i].minute
                    i += 1
                    if 'wakes up' in sortedEvents[eventsTime[i]]:
                        end = eventsTime[i].minute
                    # print(start,end)
                    gSleepTime[id] += end-start
                    for m in range(start,end):
                        gSleepList[id][m] += 1
                i += 1
            if i < totalEvents and 'Guard' in sortedEvents[eventsTime[i]]:
                i -= 1
    i += 1
maxId = 0
maxSleepTime = 0
for k,v in gSleepTime.items():
    if v > maxSleepTime:
        maxSleepTime = v
        maxId = k
print("Max ID:",maxId)
maxMinutes = 0
maxIndex = 0
for m in range(0,60):
    if gSleepList[maxId][m] > maxMinutes:
        maxIndex = m
        maxMinutes = gSleepList[maxId][m]
print("Max Minute:",maxIndex)
product = float(maxId) * maxIndex
print("Part 1:",product)

mID = 0
mMinutes = 0
mIndex = 0
for k in gSleepList.keys():
    maxOfk = max(gSleepList[k])
    if maxOfk > mMinutes:
        mID = k
        mMinutes = maxOfk
        mIndex = gSleepList[k].index(maxOfk)
print("Part 2:",mID,mIndex,mMinutes)
print("Part 2:",int(float(mID) * mIndex))
