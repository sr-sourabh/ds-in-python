'''
Write three Python functions as specified below. Paste the text for all three functions together into the submission  window. 

    You may define additional auxiiary functions as needed.  
    In all cases you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
    Ignore warnings about "Presentation errors". 

    Define a Python function "descending(l)" that returns True if each element in its input list is at most as big as the one before it

    For instance:

    >>> descending([])
    True

    >>> descending([4,4,3])
    True

    >>> descending([19,17,18,7])
    False

    Define a Python function "alternating(l)" that returns True if the values in the input list alternately go up and down (in a strict manner).

    For instance:

    >>> alternating([])
    True

    >>> alternating([1,3,2,3,1,5])
    True

    >>> alternating([3,2,3,1,5])
    True

    >>> alternating([3,2,2,1,5])
    False

    >>> alternating([3,2,1,3,5])
    False

    A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix.  For instance, the matrix

    1  2  3
    4  5  6 

    would be represented as [[1,2,3],[4,5,6]].

    Write a Python function "matmult(m1,m2)" that takes as input two matrices using this row-wise representation and returns the matrix product m1*m2 using the same representation.

    You may assume that the input matrices are well-formed and have compatible dimensions.

    For instance:

    >>> matmult([[1,2],[3,4]],[[1,0],[0,1]])
    [[1,2],[3,4]]

    >>> matmult([[1,2,3],[4,5,6]],[[1,4],[2,5],[3,6]])
    [[14, 32], [32, 77]]


'''



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
				
	
	
