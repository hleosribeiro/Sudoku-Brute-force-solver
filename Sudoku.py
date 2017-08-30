import os


mat = [[0 for i in range(9)] for j in range(9)]

for i in range(9):
	for j in range(9):
		while True:
			entry = input("Enter number at position: " + str(i) + " , " + str(j) + " or 0 if no number: ")
			try:
				entry = int(entry)
				if entry in [0,1,2,3,4,5,6,7,8,9]:
					mat[i][j] = entry
					break
				else:
					print("Not a valid entry")
			except:
				print("Not a valid entry")
		

#gera matriz original
ormat = []
aux = 0
for i in range(9):
    for j in range(9):
        if mat[i][j] != 0:
            ormat.append([i,j])
            aux+=1

			
#prints the current sudoku
def printmatrix(matrix):
    
    for i in range(9):
        for j in range(9):
            print(str(matrix[i][j]) + ',', end='')
        print('')
    return

#check if an element is valid given a position
def isValid(n, i, j, matrix):
    if n > 9:
        return False
    #check lines and columns
    for v in range(9):
        if matrix[v][j] == n:
            return False
        if matrix[i][v] == n:
            return False

    #check square
    cx1 = []
    cx2 = []
    cx3 = []
    cx4 = []
    cx5 = []
    cx6 = []
    cx7 = []
    cx8 = []
    cx9 = []
    for k in range(9):
        for q in range(9):
            if k <= 2:
                if q <= 2:
                    cx1.append(mat[k][q])
                elif q <= 5:
                    cx2.append(mat[k][q])
                else:
                    cx3.append(mat[k][q])
            elif k <= 5:
                if q <= 2:
                    cx4.append(mat[k][q])
                elif q <= 5:
                    cx5.append(mat[k][q])
                else:
                    cx6.append(mat[k][q])
            else:
                if q <= 2:
                    cx7.append(mat[k][q])
                elif q <= 5:
                    cx8.append(mat[k][q])
                else:
                    cx9.append(mat[k][q])
    if i<= 2:
        if j <= 2:
            if n in cx1: return False
        elif j <= 5:
            if n in cx2: return False
        else:
            if n in cx3: return False
    elif i<=5:
        if j <= 2:
            if n in cx4: return False
        elif j <= 5:
            if n in cx5: return False
        else:
            if n in cx6: return False
    else:
        if j <= 2:
            if n in cx7: return False
        elif j <= 5:
            if n in cx8: return False
        else:
            if n in cx9: return False
    return True
#

#start tests  
i = 0
j = 0
recede = 0
while i < 9:
    j = 0
    while j < 9:
        track = 0
        #print('i: '+str(i)+', j: '+str(j))
        if [i,j] not in ormat:
            if recede == 0:
                for m in range(1,10):                    
                    if isValid(m, i, j, mat):
                        track = 1
                        mat[i][j] = m
                        break
                if track == 0:
                    mat[i][j] = 0
                    recede = 1
            else:
                aux = mat[i][j]
                mat[i][j] = 0
                while aux < 9:
                    aux += 1
                    if isValid(aux, i, j, mat):
                        track = 1
                        mat[i][j]= aux
                        recede = 0
                        break
        if recede == 0:
            j += 1
        else:
            if j == 0:
                if i == 0:
                    recede = 0
                else:
                    i -= 1
                    j = 8
            else:
                j -= 1
        os.system('cls')
        printmatrix(mat)
        print('')
    i += 1
print('solution:')
printmatrix(mat)
