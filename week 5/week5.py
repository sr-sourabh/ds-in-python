import operator
import sys

'''

This assignment contains only one problem, and requires you to write a standalone Python program that can be directly executed, not just a 
function.

Here are some basic facts about tennis scoring:

    A tennis match is made up of sets.  A set is made up of games.

    To win a set, a player has to win 6 games with a difference of 2 games.  At 6-6, there is often a special tie-breaker.  In some cases, 
    players go on playing till one of them wins the set with a difference of two games.

    Tennis matches can be either 3 sets or 5 sets.  The player who wins a majority of sets wins the match (i.e., 2 out 3 sets or 3 out of 
    5 sets)

The score of a match lists out the games in each set, with the overall winner's score reported first for each set.  Thus, if the score is 
6-3, 5-7, 7-6 it means that the first player won the first set by 6 games to 3, lost the second one 5 games to 7 and won the third one 7 
games to 6 (and hence won the overall match as well by 2 sets to 1).

You will read input from the keyboard (standard input) containing the results of several tennis matches.  Each match's score is recorded 
on a separate line with the following format:

Winner:Loser:Set-1-score,...,Set-k-score, where 2 <= k <= 5

For example, an input line of the form

Williams:Muguruza:3-6,6-3,6-3

indicates that Williams beat Muguruza 3-6, 6-3, 6-3 in a best of 3 set match.

The input is terminated by a blank line.

You have to write a Python program that reads information about all the matches and compile the following statistics for each player:

    Number of best-of-5 set matches won
    Number of best-of-3 set matches won
    Number of sets won
    Number of games won
    Number of sets lost
    Number of games lost

You should print out to the screen (standard output) a summary in decreasing order of ranking, where the ranking is according to the 
criteria 1-6 in that order (compare item 1, if equal compare item 2, if equal compare item 3 etc, noting that for items 5 and 6 the 
comparison is reversed).

For instance, given the following data

Djokovic:Murray:2-6,6-7,7-6,6-3,6-1
Murray:Djokovic:6-3,4-6,6-4,6-3
Djokovic:Murray:6-0,7-6,6-7,6-3
Murray:Djokovic:6-4,6-4
Djokovic:Murray:2-6,6-2,6-0
Murray:Djokovic:6-3,4-6,6-3,6-4
Djokovic:Murray:7-6,4-6,7-6,2-6,6-2
Murray:Djokovic:7-5,7-5
Williams:Muguruza:3-6,6-3,6-3

your program should print out the following

Djokovic 3 1 13 142 16 143
Murray 2 2 16 143 13 142
Williams 0 1 2 15 1 12
Muguruza 0 0 1 12 2 15

You can assume that there are no spaces around the punctuation marks ":", "-" and ",".  Each player's name will be spelled consistently 
and no two players have the same name.


'''






'''
1. Number of best-of-5 set matches won
2. Number of best-of-3 set matches won
3. Number of sets won
4. Number of games won
5. Number of sets lost
6. Number of games lost

Djokovic:Murray:2-6,6-7,7-6,6-3,6-1

'''


def compute(a,names,winner,looser):
	winnersets =0
	for i in range(len(a)):
		#print (i,end = '')
		if i% 4 == 0:
			names[winner][3] += int(a[i])   #fix the 4th and 6th requirement
			names[looser][5] += int(a[i])
			
			if a[i] < a[i+2]:		#fix 5th and 3rd requirement
				names[winner][4] += 1
				names[looser][2] += 1
			else :	
				winnersets += 1		#calculate wheather best of 5 or 3		
				names[looser][4] += 1    #fix 5th and 3rd requirement
				names[winner][2] += 1
			
			
		elif a[i].isdigit():
			names[looser][3] += int(a[i])   #fix the 4th and 6th requirement
			names[winner][5] += int(a[i])
	
	
	if winnersets == 3:				#increment best of 5 field if true : 1st requirement
		names[winner][0] +=1
	elif winnersets == 2:				#increment best of 3 field if true : 2nd requirement
		names[winner][1] +=1 
			
	
			
	

def process():

    names = {}		 #this will store players and respective 1 2 3 4 5 6 requirements
    while 1:
    	    
	    a = input()
	    
	    
	    if a.strip() == "":  		#termination condition
	    	break
	    count = 0
	    
	    name =''
	    for i in range(len(a)):
	    	if (a[i] != ':') and (count < 2) :	#get the player names
	    	    name += a[i]
	    	if a[i] == ':' and count<2 :
	    	    count += 1
	    	    if  name not in list(names.keys()):
	    	    	names[name] = [0,0,0,0,0,0]
	    	    if count == 1:
	    	    	winner = name			#identify winner from count ==1
	    	    else:
	    	    	looser = name			#identify looser from count ==2
	    	    name=''
	    	if count == 2:
	    		compute(a[i+1 :],names,winner,looser)		#compute the requirements of the players
	    		break
			 
		
    names1 = sorted(names.items(), key=operator.itemgetter(1),reverse =True)	#sort
    		
    for e in names1:
    	print(e[0],e[1][0],e[1][1],e[1][2],e[1][3],e[1][4],e[1][5])		#display 
    
           
           
process()   

