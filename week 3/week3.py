#question 1

def descending(l):
	for i in range(len(l) - 1):
		if (l[i] < l[i+1]):
			return False
			
	return True
	

#question 2
def alternating(l):
	return (updown(l) or downup(l) )
	
def updown(l):
	if(len(l) == 0 or len(l) == 1 ) :	
		return True
	return ( l[0] <l[1] and downup(l[1:]))
	
def downup(l):
	if(len(l) == 0 or len(l) == 1 ) :	
		return True
	return ( l[0] > l[1] and updown(l[1:]))
	
#question 3
def matmult(m1,m2):
	m3 = []
	for i in range(len(m1)):
		m4 = []
		for j in range(len(m2[0])):
			t = 0
			for k in range(len(m2)):
				t += m1[i][k] * m2[k][j]
			m4.append(t)
		m3.append(m4)
			
	return m3
				
	
	
