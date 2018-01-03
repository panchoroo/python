# A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary 
# to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this).
#  The complexity of the search determines the difficulty of the puzzle; the example above is considered easy 
#  because it can be solved by straight forward direct deduction.

# The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
#  ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

# By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution 
# grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.


# standard naming: columns 1-9, the rows A-I,  collection of nine squares (column, row, or box) a unit
# and the squares that share a unit the peers

# (1) If a square has only one possible value, then eliminate that value from the square's peers. 
# (2) If a unit has only one possible place for a value, then put the value there.
# constraint propagation.

ROWS = [[(r, c) for c in range(9)] for r in range(9)]
COLUMNS = [[(r, c) for r in range(9)] for c in range(9)]
COORDS = [(r,c) for r in range(9) for c in range(9)]
BOXES = [[] for b in range(9)]
for r,c in COORDS:
	if r < 3 and c < 3:
		BOXES[0].append((r,c))
	elif r < 3 and c < 6:
		BOXES[1].append((r,c))
	elif r < 3:
		BOXES[2].append((r,c))
	elif r < 6 and c < 3:
		BOXES[3].append((r,c))
	elif r < 6 and c < 6:
		BOXES[4].append((r,c))
	elif r < 6:
		BOXES[5].append((r,c))
	elif c < 3:
		BOXES[6].append((r,c))
	elif c < 6:
		BOXES[7].append((r,c))
	else:
		BOXES[8].append((r,c))

def solve(puzzle):
	count = 0
	while oneValue(puzzle) == False and count < 100:
		eliminated = eliminateFromPeers(puzzle)
		if eliminated:
			peersChanged = eliminated[1]
			unitChecked = unitChecker(eliminated[0])
			if unitChecked:
				puzzle, unitChanged = unitChecked;
			else: 
				# print "unitChecker failed"
				return False
		else:
			# print "eliminateFromPeers failed"
			return False

		if not peersChanged and not unitChanged:
			guesses = makeGuesses(puzzle)
			# print "guesses made"
			for g in guesses:
				solution = solve(g)
				if solution:
					return solution
			return False 
			# returns false if we don't return a solution, i.e. none of the guesses were solvable 
			# (so the parent was a bad branch, nested guessing)
		count += 1
	return puzzle

def oneValue(puzzle):
	# checking to see if there is only one possible value for each square in the 9x9 grid
	squares = [len(puzzle[key]) == 1 for key in puzzle.keys()]
	return all(squares)

def eliminateFromPeers(puzzle):
	# goes through values and finds squares that have only one possibility 
	# and eliminates that value from all other peers
	changeMade = False

	for coord in puzzle:
		if len(puzzle[coord]) == 1:
			for peer in getPeers(coord):
			# If a square has only one possible value, 
  			# then eliminate that value from the square's peers.
  				if puzzle[coord] in puzzle[peer]:
					puzzle[peer] = puzzle[peer].replace(puzzle[coord], '')
					changeMade = True
					if len(puzzle[peer]) < 1:
						# print "Error in guess due to complete elimination"
						return False
 	return (puzzle, changeMade)

def unitChecker(puzzle):
	# If a unit has only one possible place for a value, then put the value there.
	changeMade = False
	for unit in ROWS + COLUMNS + BOXES:
		puzzle, changeMadeUnit = solidarityChecker(puzzle, unit)
		if changeMadeUnit:
			changeMade = True
	if unitErrorChecker(puzzle):		
		return puzzle, changeMade
	else:
		return False

def unitErrorChecker(puzzle):
	# checks all units for multiples of same digit
	# len of all things with len 1, len of set of those things should be the same
	error = False
	for unit in ROWS + COLUMNS + BOXES:
		singlesList = [u for u in unit if len(u) == 1]
		if singlesList != set(singlesList):
			error = True
	return error 

def solidarityChecker(puzzle, unit):
	# a unit is a row or a column or a box
	changeMade = False
	for digit in '123456789':
		digitCount = 0
  		digitLocation = None
		for coord in unit:
			if digit in puzzle[coord]:
				digitCount += 1
	  			digitLocation = coord
	  	if digitCount == 1 and len(puzzle[digitLocation]) > 1:
	  		puzzle[digitLocation] = digit
	  		# print ('unformatted ', unformat(puzzle))
	  		changeMade = True
	return puzzle, changeMade

def makeGuesses(puzzle):
	guesses = [];
	numPossibilites = 9
	minCoord = None
	for coord in COORDS:
		coordLen = len(puzzle[coord])
		if coordLen > 1 and coordLen < numPossibilites:
			numPossibilites = coordLen
			minCoord = coord
	for i in range(len(puzzle[minCoord])):
		guess = puzzle.copy()
		guess[minCoord] = puzzle[minCoord][i]
		guesses.append(guess)
	return guesses

def getPeers(coord):
	# takes a coord and gets all peers (i.e set of coords in row, column and box)
	row = getRow(coord)
	column = getColumn(coord)
	box = getBox(coord)
	peers = set(row + column + box)
	peers.remove(coord)
	return peers

def getRow(coord):
	return ROWS[coord[0]]

def getColumn(coord):
	return COLUMNS[coord[1]]

def getBox(coord):
	for box in BOXES:
		if coord in box:
			return box
	return 'ERROR: no box found for coordinate'

def loadSudokus(sudokuText):
	inFile = open(sudokuText, 'r')
	line = inFile.readline()
	sudokuList = []
	while line:
		if line[0] == 'G':
			newPuzzle = []
			count = 0
		if count > 0:
			newPuzzle.append(line[:9])
		count += 1
		if count >= 8:
			if newPuzzle not in sudokuList:
				sudokuList.append(newPuzzle)
		line = inFile.readline()
	inFile.close()
	return sudokuList

def formatPuzzle(filePuzzle):
	puzzle = {}
	rowCount = 0
	for row in filePuzzle:
		colCount = 0
		for col in row:
			if filePuzzle[rowCount][colCount] == '0':
				puzzle[(rowCount, colCount)] = '123456789'
			else:
				puzzle[(rowCount, colCount)] = filePuzzle[rowCount][colCount]
			colCount += 1
		rowCount += 1
	# print ('puzzle', puzzle)
	return puzzle

def unformat(puzzle):
	p = []
	for r in range(9):
		line = ''
		for c in range(9):
			# line += '('+puzzle[(r,c)]+')'
			if len(puzzle[(r,c)]) == 1:
				line += puzzle[(r,c)]
			else:
				line += '0'
		p.append(line)
	return p


if __name__ == '__main__':
	
	puzzleList = loadSudokus('p096_sudoku.txt')
	solutionsList = [];
	for i, p in enumerate(puzzleList):
		# print ('puzzle start', p)
		puzzleDict = formatPuzzle(p)
		solved = solve(puzzleDict)
		if oneValue(solved):
			solutionsList.append(solved)
		else:
			print ('bad puzzle', solved)
			print i
			print p

	print ('solutions', solutionsList)
	print len(solutionsList)
	sum = 0;
	for s in solutionsList:
		sum += int(s[(0,0)])*100 + int(s[(0,1)])*10 + int(s[(0,2)])
	print ('sum', sum)

