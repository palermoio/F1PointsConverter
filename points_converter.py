'''
File: points_converter.py
By: Francesco Palermo
Description: Program calculates points total for Formula One driver's championship in specified year using selected
points scoring system.
Usage: Program prompts user for season and points scoring system. Program reads season results from a text file,
with one driver and their results per line.
'''

#User input: season
user_input = input("Select a Formula One season from 1950 to 2018: ")

#check that user input is valid
while((user_input.isdigit() == False) or (int(user_input) < 1950 or int(user_input) > 2018)):
    user_input = input("Invalid input. Select a Formula One season from 1950 to 2018: ")
season = user_input

#User input: points system
user_input = input("Select a points scoring system. \n"
                   "1. 2010-present (Top 10)\n2. 2003-2009 (Top 8)\n"
                   "3. 1991-2002 (Top 6)\n4. 1961-1990 (Top 6)\n"
                   "5. 1960 (Top 6)\n6. 1950-1959 (Top 5)\n")

#check that user input is valid
while((user_input.isdigit() == False) or (int(user_input) < 1 or int(user_input) > 6)):
    user_input = input("Invalid input. Select a points scoring system. \n"
                       "1. 2010-present (Top 10)\n2. 2003-2009 (Top 8)\n"
                       "3. 1991-2002 (Top 6)\n4. 1961-1990 (Top 6)\n"
                       "5. 1960 (Top 6)\n6. 1950-1959 (Top 5)\n")
system = int(user_input)

results = []    #list of results
x = 0   #counter for going through results
lowest_finish = 0

#open csv file with season results
file_name = (season + ".csv")
file = open(file_name, "r")
for line in file:
    results.append([line.split(',')[0], {}, 0])     #add driver to list of results. Each results element has the driver name, hash table of finishes and points total to be calculated later.
    for i in line.split(',')[1:]:       #go through all of driver's results for the year
        if (i.rstrip().isdigit() and (int(i.rstrip()) > lowest_finish)):
            lowest_finish = int(i.rstrip())     #track lowest finish for tie comparison later
        if i.rstrip() in results[x][1]:
            results[x][1][i.rstrip()] = results[x][1][i.rstrip()] + 1   #if driver already has a finish in this position in hash table, add to it.
        else:
            results[x][1][i.rstrip()] = 1   #first finish in this position, add new entry to hash table.
    x += 1

#tabulate points
'''
1. 2010 to present system.
1st = 25 pts, 2nd = 18 pts, 3rd = 15 pts, 4th = 12 pts, 5th = 10 pts, 6th = 8 pts, 7th = 6 pts, 8th = 4 pts, 9th = 2 pts
10 = 1 pt
'''
if system == 1:
    for y in results:
        if '1' in y[1]:
            y[2] += 25 * y[1]['1']
        if '2' in y[1]:
            y[2] += 18 * y[1]['2']
        if '3' in y[1]:
            y[2] += 15 * y[1]['3']
        if '4' in y[1]:
            y[2] += 12 * y[1]['4']
        if '5' in y[1]:
            y[2] += 10 * y[1]['5']
        if '6' in y[1]:
            y[2] += 8 * y[1]['6']
        if '7' in y[1]:
            y[2] += 6 * y[1]['7']
        if '8' in y[1]:
            y[2] += 4 * y[1]['8']
        if '9' in y[1]:
            y[2] += 2 * y[1]['9']
        if '10' in y[1]:
            y[2] += 1 * y[1]['10']
'''
2. 2003 to 2009 system.
1st = 10 pts, 2nd = 8 pts, 3rd = 6 pts, 4th = 5 pts, 5th = 4 pts, 6th = 3 pts, 7th = 2 pts, 8th = 1 pt
'''
if system == 2:
    for y in results:
        if '1' in y[1]:
            y[2] += 10 * y[1]['1']
        if '2' in y[1]:
            y[2] += 8 * y[1]['2']
        if '3' in y[1]:
            y[2] += 6 * y[1]['3']
        if '4' in y[1]:
            y[2] += 5 * y[1]['4']
        if '5' in y[1]:
            y[2] += 4 * y[1]['5']
        if '6' in y[1]:
            y[2] += 3 * y[1]['6']
        if '7' in y[1]:
            y[2] += 2 * y[1]['7']
        if '8' in y[1]:
            y[2] += 1 * y[1]['8']
'''
3. 1991 to 2002 system.
1st = 10 pts, 2nd = 6 pts, 3rd = 4 pts, 4th = 3 pts, 5th = 2 pts, 6th = 1 pt
'''
if system == 3:
    for y in results:
        if '1' in y[1]:
            y[2] += 10 * y[1]['1']
        if '2' in y[1]:
            y[2] += 6 * y[1]['2']
        if '3' in y[1]:
            y[2] += 4 * y[1]['3']
        if '4' in y[1]:
            y[2] += 3 * y[1]['4']
        if '5' in y[1]:
            y[2] += 2 * y[1]['5']
        if '6' in y[1]:
            y[2] += 1 * y[1]['6']
'''
4. 1961 to 1990 system.
1st = 9 pts, 2nd = 6 pts, 3rd = 4 pts, 4th = 3 pts, 5th = 2 pts, 6th = 1 pt
'''
if system == 4:
    for y in results:
        if '1' in y[1]:
            y[2] += 9 * y[1]['1']
        if '2' in y[1]:
            y[2] += 6 * y[1]['2']
        if '3' in y[1]:
            y[2] += 4 * y[1]['3']
        if '4' in y[1]:
            y[2] += 3 * y[1]['4']
        if '5' in y[1]:
            y[2] += 2 * y[1]['5']
        if '6' in y[1]:
            y[2] += 1 * y[1]['6']
'''
5. 1960 system.
1st = 8 pts, 2nd = 6 pts, 3rd = 4 pts, 4th = 3 pts, 5th = 2 pts, 6th = 1 pt
'''
if system == 5:
    for y in results:
        if '1' in y[1]:
            y[2] += 8 * y[1]['1']
        if '2' in y[1]:
            y[2] += 6 * y[1]['2']
        if '3' in y[1]:
            y[2] += 4 * y[1]['3']
        if '4' in y[1]:
            y[2] += 3 * y[1]['4']
        if '5' in y[1]:
            y[2] += 2 * y[1]['5']
        if '6' in y[1]:
            y[2] += 1 * y[1]['6']
'''
6. 1950 to 1959 system.
1st = 8 pts, 2nd = 6 pts, 3rd = 4 pts, 4th = 3 pts, 5th = 2 pts
'''
if system == 6:
    for y in results:
        if '1' in y[1]:
            y[2] += 8 * y[1]['1']
        if '2' in y[1]:
            y[2] += 6 * y[1]['2']
        if '3' in y[1]:
            y[2] += 4 * y[1]['3']
        if '4' in y[1]:
            y[2] += 3 * y[1]['4']
        if '5' in y[1]:
            y[2] += 2 * y[1]['5']

#sort results
standings = []
for j in results:
    if len(standings) == 0:         #no entries yet, add first entry
        standings.append([j[0], j[2], j[1]])
    else:
        for m in range(0,len(standings)):
            if(int(j[2]) > standings[m][1]):    #if driver has more points, insert in front of current and break loop
                standings.insert(m, [j[0], j[2], j[1]])
                break
            elif(j[2] == standings[m][1]):     #drivers are tied, use line 45 for reference.
                flag_added = 0  #if a driver was added in this tiebreaker, set to 1. Required to break out of loop this one is nested in
                for n in range(1, lowest_finish + 1):
                    if(str(n) not in standings[m][2] and str(n) not in j[1]):   #both haven't finished in this position, advance
                        continue
                    elif(str(n) in standings[m][2] and str(n) not in j[1]): #current driver hasn't finished in this position, other has
                        break
                    elif(str(n) not in standings[m][2] and str(n) in j[1]): #current driver has finished in this position, other hasn't
                        standings.insert(m, [j[0], j[2], j[1]])
                        flag_added = 1
                        break
                    elif(str(n) in standings[m][2] and str(n) in j[1]): #both drivers finished in this position
                        if(standings[m][2][str(n)] == j[1][str(n)]):    #equal amount of finishes at this position
                            continue
                        elif(standings[m][2][str(n)] > j[1][str(n)]):   #other driver has more finishes at higher position
                            break
                        elif(standings[m][2][str(n)] < j[1][str(n)]):   #current driver has more finishes at higher position
                            standings.insert(m, [j[0], j[2], j[1]])
                            flag_added = 1
                            break

                if(flag_added == 1):
                    break
                elif(m+1 == len(standings)):    #make sure current driver isn't in provisional last. If they are, they won't be counted unless added here.
                    standings.append([j[0], j[2], j[1]])
                    break
                else:
                    continue
            elif(m+1 == len(standings)):     #driver last amongst ones currently sorted,
                standings.append([j[0], j[2], j[1]])

x=1
for z in standings:
    print('{:<5}{:<25}{:<4}'.format(x, z[0], z[1]))
    x+=1