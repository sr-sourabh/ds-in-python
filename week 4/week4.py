'''

1.  We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:

    {'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}

    Each match is identified by a string, as is each player.  The scores are all integers.  The names associated with the matches are not 
    fixed (here they are 'match1','match2','match3'), nor are the names of the players.  A player need not have a score recorded in all 
    matches

    Define a Python function "orangecap(d)" that reads a dictionary d of this form and identifies the player with the highest total 
    score.  Your function should return a pair (playername,topscore) where playername is a string, the name of the player with the highest 
    score, and topscore is an integer, the total score of playername.

    The input will be such that there are never any ties for highest total score.

    For instance:

    >>> orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 
    'player3':91}})
    ('player3', 100)

    >>> orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})
    ('Kohli', 120)

    Let us consider polynomials in a single variable x with integer coefficients: for instance, 3x^4 - 17x^2 - 3x + 5.  Each term of the 
    polynomial can be represented as a pair of integers (coefficient,exponent).  The polynomial itself is then a list of such pairs. 

    We have the following constraints to guarantee that each polynomial has a unique representation:

    -- Terms are sorted in descending order of exponent
    -- No term has a zero cofficient
    -- No two terms have the same exponent
    -- Exponents are always nonnegative

    For example, the polynomial introduced earlier is represented as

       [(3,4),(-17,2),(-3,1),(5,0)]

    The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.
    
    
    
    

 2. Write Python functions for the following operations:

    addpoly(p1,p2)
    multpoly(p1,p2)

    that add and multiply two polynomials, respectively.

    You may assume that the inputs to these functions follow the representation given above.  Correspondingly, the outputs from these 	      functions should also obey the same constraints.

    Hint: You are not restricted to writing just the two functions asked for.  You can write auxiliary functions to "clean up"
    polynomials	--- e.g., remove zero coefficient terms, combine like terms, sort by exponent etc.  Build a library of functions that can
    be 	combined to achieve the desired format.

    You may also want to convert the list representation to a dictionary representation and manipulate the dictionary representation, and
    then convert back. 

    Some examples:

    >>> addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
    [(2, 1),(3, 0)]

    Explanation: (4x^3 + 3) + (-4x^3 + 2x) = 2x + 3

    >>> addpoly([(2,1)],[(-2,1)])
    []

    Explanation: 2x + (-2x) = 0

    >>> multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
    [(1, 3),(-1, 0)]

    Explanation: (x - 1) * (x^2 + x + 1) = x^3 - 1

'''




#{'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}}

def orangecap(d):
	a={}
	for match in d.keys():
		for player in d[match]:
			if player not in a:
				a[player] = d[match][player]
			else :
				a[player] += d[match][player]
	big = 0
	for player in a.keys():
		if big < a[player]:
			big = a[player]
			capholder = player
	return (capholder,big)
	

#addpoly([(4,3),(3,0)],[(-4,3),(2,1)]) = [(2, 1),(3, 0)]

def addpoly(a,b):
	c=a+b
	f={}
	d=[]
	for i in range(len(c)):
		f[c[i][1]] = 0 
	
	for i in range(len(c)):
		total = c[i][0]
		for j in range(i+1,len(c)):
			if c[i][1] == c[j][1] :
				total += c[j][0]
		if not f[c[i][1]] :
			d.append(( total,c[i][1] ))
			f[c[i][1]] = 1
			
	#print (d)
	
	for ed in d:		
		for ed in d:
			if ed[0]==0:
				d.remove(ed)
	d.sort(key = lambda l : l[1] , reverse = True)
	#print (d)
	return (d)
	
	
	
	
def multpoly(a,b):
	cc=[]
	d=[]
	
	for ea in a:
		for eb in b:
			cc.append((ea[0]*eb[0] , ea[1] + eb[1]))
			
	#print (cc)
	d = addpoly(cc[:1] , cc[1:])
	return (d)
	
			
	







	

		
