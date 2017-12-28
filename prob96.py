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

import random;

print 'derp'
sudokuText= "p096_sudoku.txt"
def loadSuccesses():
	inFile = open(sudokuText, 'r')
	line = inFile.readline()
	sudokuList = []
	while line:
		if line[0] == 'G':
			newPuzzle = [];
			count = 0;
		if count > 0:
			newPuzzle.append(line[:9]);
		count += 1
		if count >= 8:
			sudokuList.append(newPuzzle);
		line = inFile.readline()
	inFile.close()
	return sudokuList

# puzzleList = loadSuccesses()
# when it works, load all 50 puzzles, for now, just the first one
puzzleList = [['003020600', '900305001', '001806400', '008102900', '700000008', '006708200', '002609500', '800203009', '005010300']];
# print puzzleList;

solutionsList = [];
for p in puzzleList:
	# iterate through each puzzle from the text file
	startIndex = 0;
	workingPuzzle = p;
	possiblySolved = [];
	possibleDigits = '123456789';

	# # readded old code to fill in some digits by logic method
	# print workingPuzzle;
	# def getGrid(index):
 # 		firstGrid = [0,1,2];
 # 		secondGrid = [3,4,5];
 # 		thirdGrid = [6,7,8];
 # 		if index in firstGrid:
 # 			return firstGrid;
 # 		elif index in secondGrid:
 # 			return secondGrid;
 # 		elif index in thirdGrid:
 # 			return thirdGrid;
 # 		else:
 # 			print('something has gone terribly, terribly wrong');
 
 # 	currentGrid = [0,1,2];
 # 	checkIndex = 0;
 
 # 	def rowDigitChecker(digit):
 # 		noNew = True;
 # 		def currentCheck(line):	
 # 			return line.index(digit);

 # 		def currentGridChecker(line, grid):			
 # 			newGrid = grid;
 # 			if workingPuzzle.index(line) not in grid:
 # 				newGrid = getGrid(workingPuzzle.index(line));
 # 			return newGrid;

 # 		line = 0;
 # 		currentGrid = getGrid(line);
 
 # 		lineIndex = 0;
 # 		while lineIndex < 7:
 # 			workingLine = workingPuzzle[lineIndex]
 # 			first = [digit in workingLine, 0];
 # 			second = [digit in workingPuzzle[workingPuzzle.index(workingLine)+1], 1];
 # 			third = [digit in workingPuzzle[workingPuzzle.index(workingLine)+2], 2];
 # 			found = [first, second, third];
 # 			successes = [f[1] for f in found if f[0]]
 # 			# print ('successes', successes)
 
 # 			if len(successes) == 2:
 # 				line1 = workingPuzzle[workingPuzzle.index(workingLine)+successes[0]];
 # 				index1 = line1.index(digit);
 # 				grid1 = getGrid(index1);
 
 # 				line2 = workingPuzzle[workingPuzzle.index(workingLine)+successes[1]];
 # 				index2 = line1.index(digit);
 # 				grid2 = getGrid(index2);
 
 # 				if (0 in grid1 or 0 in grid2 and (3 in grid1 or 3 in grid2)):
 # 					grid3 = [6,7,8];
 # 				elif (0 in grid1 or 0 in grid2 and (6 in grid1 or 6 in grid2)):
 # 					grid3 = [3,4,5];
 # 				else:
 # 					grid3 = [0,1,2];
 
 # 				# print ('lines',workingPuzzle.index(line1), workingPuzzle.index(line2))
 # 				if (successes[1] - successes[0] == 2):
 # 					line3 = workingPuzzle[workingPuzzle.index(workingLine)+1];
 # 				elif (workingPuzzle.index(line1) == 0 or workingPuzzle.index(line1) == 3 or workingPuzzle.index(line1) == 6):
 # 					line3 = workingPuzzle[workingPuzzle.index(workingLine)+2];
 # 				else:
 # 					line3 = workingPuzzle[workingPuzzle.index(workingLine)];
 # 				# print ('3s ', line3, grid3);
 # 				zeroes = []
 # 				for g in grid3:
 # 					# print line3[g]
 # 					# maybe filter grid3 somehow?
 # 					if (str(line3[g]) == '0'):
 # 						zeroes.append(g);
 						
 # 				matches = [];
 # 				for z in zeroes:
 # 					# print ('z? ',z)
 # 					for testLine in workingPuzzle:
 # 						if testLine[z] == digit:
 # 							zeroes.remove(z);
 # 				if len(zeroes) == 1:
 # 					# print 'YEAY'
 # 					# print (line3, digit, zeroes[0])
 # 					noNew = False;
 
 # 					newLine = line3[:zeroes[0]] + str(digit) + line3[zeroes[0]+1:];
 # 					# newLine[zeroes[0]] = str(digit);
 # 					workingPuzzle[workingPuzzle.index(line3)] = newLine;
  
 # 			lineIndex += 3;
 # 		return noNew;
  
  
 # 	done = False;
 # 	while not done:
 # 		allDone = True;
 # 	 	for digit in possibleDigits:
 # 	 		if rowDigitChecker(digit) == False:
 # 	 			allDone = False;
 # 	 	if allDone == True:
 # 	 		done = True;
	# print ('workingPuzzle before ', workingPuzzle);
  	possibleValues = [['123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789'], ['123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789'], ['123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789'], ['123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789'], ['123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789'], ['123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789'], ['123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789'], ['123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789'], ['123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789']];
  	# print possibleValues;
  	rowIndex = 0;
  	while rowIndex < 9:
  		colIndex = 0;
	  	while colIndex < 9:
	  		# print workingPuzzle[rowIndex];
	  		# print workingPuzzle[rowIndex][colIndex];
	  		if workingPuzzle[rowIndex][colIndex] != '0':
	  			# eliminate all but that value 
	  			# print workingPuzzle[rowIndex][colIndex];
	  			# print possibleValues[rowIndex][colIndex];
	  			possibleValues[rowIndex][colIndex] = workingPuzzle[rowIndex][colIndex];
	  		colIndex += 1;
  		rowIndex += 1;

 	# rowDigitChecker(possibleDigits[0]);
 	# print ('workingPuzzle after ', workingPuzzle);
 	# print possibleValues;

 	# get peers and eliminate single choices from all peers
 	def getPeers(row, column):
 		# takes in row index and col index and returns all 20 peers of that square
 		peers = [];
 		# all in same row, all in same column, and grid
 		# no repeats
 		
 		index = 0
 		while index < 9:
 			if [row, index] not in peers and index != column:
	 			peers.append([row, index]);
	 		if [index, column] not in peers and index != row:
		 		peers.append([index, column]);
	 		index += 1;

	 	def modifier(index):
 			mod1 = 1;
 			mod2 = 2;
 			if index == 1 or index == 4 or index == 7:
	 			mod2 = -1;
	 		elif index == 2 or index == 5 or index == 8:
	 			mod1 = -1;
	 			mod2 = -2;
	 		return [mod1, mod2];
	
	 	rowMods = modifier(row);
	 	colMods = modifier(column);
	 	modifierRow1 = rowMods[0];
 		modifierRow2 = rowMods[1];
 		modifierCol1 = colMods[0];
 		modifierCol2 = colMods[1];
 		gridPeers = [[row, column+modifierCol1], [row, column+modifierCol2], [row+modifierRow1, column], [row+modifierRow1, column+modifierCol1], [row+modifierRow1, column+modifierCol2], [row+modifierRow2, column],  [row+modifierRow2, column+modifierCol1],  [row+modifierRow2, column+modifierCol2]];
 		for g in gridPeers:
 			if g not in peers:
	 			peers.append(g);
 		# peers = set(peers);
 		# peers.remove([row, column]);
 		return peers;

 	def singler(values):
 		# goes through values and finds squares that have only one possibility
 		changeMade = False;
 		rowIndex = 0;
	  	while rowIndex < 9:
	  		colIndex = 0;
		  	while colIndex < 9:
		  		if len(values[rowIndex][colIndex]) == 1:
		  			# If a square has only one possible value, then eliminate that value from the square's peers.
		  			onlyVal = values[rowIndex][colIndex];
		  			# if currentPuzzle[rowIndex][colIndex] == '0':
		  			# 	line = currentPuzzle[rowIndex];
		  			# 	print line;
		  			# 	line = line[:colIndex] + onlyVal + line[colIndex+1:];
		  			# 	currentPuzzle[rowIndex] = line;
		  			peers = getPeers(rowIndex, colIndex);
		  			for p in peers:
		  				# print values[p[0]][p[1]];
		  				peerVal = values[p[0]][p[1]];
		  				# print ('p, p0', p, p[0]);
		  				if onlyVal in peerVal:
		  					values[p[0]][p[1]] = peerVal[:peerVal.index(onlyVal)] + peerVal[peerVal.index(onlyVal)+1:];
		  					changeMade = True;
		  		colIndex += 1;
	  		rowIndex += 1;
	  	return [values, changeMade];

 	def unitChecker(values):
		# If a unit has only one possible place for a value, then put the value there.
		# check all units, place any values, then check singler or getPeers again?
		changeMade = False;
		rowIndex = 0;
		digits = '123456789';
		while rowIndex < 9:
		  	for d in digits:
		  		digitCount = 0;
		  		digitIndex = 0;
		  		colIndex = 0;
			  	while colIndex < 9:
			  		if d in values[rowIndex][colIndex]:
			  			digitCount += 1;
			  			digitIndex = colIndex;
			  		colIndex += 1;
			  	if digitCount == 1 and len(values[rowIndex][digitIndex]) > 1:
			  		values[rowIndex][digitIndex] = d;
			  		changeMade = True;
	  		rowIndex += 1;
	  	return [values, changeMade];

	# rowIndex = 0;
 #  	while rowIndex < 9:
 #  		colIndex = 0;
	#   	while colIndex < 9:
	#   		# if workingPuzzle[rowIndex][colIndex] != '0':

	#   			# possibleValues[rowIndex][colIndex] = workingPuzzle[rowIndex][colIndex];
	#   		colIndex += 1;
 #  		rowIndex += 1;
 	# print getPeers(1,1);

	# for line in workingPuzzle:
	# 	thisLineDigits = '';
	# 	for d in possibleDigits:
	# 		if d not in line:
	# 			thisLineDigits += d;
	# 	# print thisLineDigits;
	# 	for digit in line:
	# 		# print digit
	# 		if digit == '0':
	# 			line = line[:line.index(digit)] + thisLineDigits[startIndex] + line[line.index(digit)+1:]
	# 			# print line
	# 			# line[line.index(digit)] = ;
	# 			thisLineDigits = thisLineDigits[1:];
	# 	# print line;
	# 	possiblySolved.append(line);

	# print possiblySolved;
	# possiblySolved=['123456789', 
	# '456789123', 
	# '789123456', 
	# '223456789', 
	# '356789123', 
	# '589123456', 
	# '623456789', 
	# '856789123', 
	# '989123456'];

	# test solution 
	# possiblySolved=['123456789', 
	# '456789123', 
	# '789123456', 
	# '234567891', 
	# '567891234', 
	# '891234567', 
	# '345678912', 
	# '678912345', 
	# '912345678'];

	def checkAllErrors(possibleSolution):

		def gridChecker(rowStart, colStart):
			gridNums = '';
			count = 0;
			line = possibleSolution[rowStart];
			colCount = 0;
			errors = 0;

			while count < 9:
				# print line, count;
				if count == 3:
					line = possibleSolution[rowStart+1];
					colCount = 0;
				elif count == 6: 
					line = possibleSolution[rowStart+2];
					colCount = 0;

				digit = line[colStart+colCount];
				if digit in gridNums:
					# print digit, gridNums;
					errors += 1;
				else:
					gridNums += digit;
				count += 1;
				colCount += 1;
			# print gridNums;
			return errors;

		def colChecker():
			errors = 0;
			colIndex = 0;
			rowIndex = 0
			while colIndex < 9:
				colNums = '';
				while rowIndex < 9:
					# print possibleSolution[rowIndex][colIndex];
					if possibleSolution[rowIndex][colIndex] not in colNums:
						colNums += possibleSolution[rowIndex][colIndex];
					else: 
						errors += 1;
						# print 'nope'
					
					rowIndex += 1;
				colIndex += 1;
				rowIndex = 0;
			return errors;


		gridRowIndex = 0;
		allErrors = 0;
		while gridRowIndex < 7:
			# check each 3x3 grid for numbers 1-9, no repeats
			gridColIndex = 0;
			while gridColIndex < 7:
				allErrors = gridChecker(gridRowIndex, gridColIndex);
				gridColIndex += 3;
			gridRowIndex += 3;

		allErrors += colChecker();
		return allErrors;

	def threeStrategySolver(values):
		# (1) If a square has only one possible value, then eliminate that value from the square's peers. 
		# (2) If a unit has only one possible place for a value, then put the value there.
		# (3) if no more squares can be filled in with 1 and 2, guess by trying one possibility out of 2, 
		# check for errors and if that one doesn't work out, fix the other possibility
		
		# solved = False;
		notDone = True;

		while notDone:
			print 'not stuck'
			singled = singler(values);
			values = singled[0];
			notDone = singled[1];
			# newPuzzle = singled[1];
			# if newPuzzle == workingPuzzle:
			# 	gotStuck = True;
			# else:
			# 	workingPuzzle = newPuzzle;

			# print values;
			newValued = unitChecker(values);
			values = newValued[0];
			notDone = newValued[1];

			# print ('newValues ', values);

		return values;		

		# print (possibleValues);

		# while totalErrors > 0: 
		# totalErrors = checkAllErrors(possiblySolved);
		# if totalErrors == 0:
		# 	# add to actual solutions
		# 	print 'yay!'
		# 	solved = True;
		# 	# return values? or workingPuzzle?
		# else: 
		# 	print 'nerrrrp'
		# 	print totalErrors;




	# print ('possiblySolved ', workingPuzzle);	
	# print possibleValues;
	maybeSolved = threeStrategySolver(possibleValues);
	# possibleValues = maybeSolved;
	# notDone = maybeSolved[1];

	# print ('maybeSolved ', workingPuzzle);
	# print possibleValues;
	solution = [];
	for m in maybeSolved:
		solution.append(''.join(m));

	print ('solution', solution);
	print checkAllErrors(solution)

	# def mutationMaker(originalPuzzle, currentVersion, errors):
	# 	# could make it have greater mutations based on number of errors?
	# 	# make mutations smaller as it gets closer
	# 	lineCount = 0;
	# 	switchables = [];
	# 	mutatedPuzzle = [];
	# 	while lineCount < 9:
	# 		mutatedLine = '';
	# 		for digit in currentVersion[lineCount]:
	# 			if digit not in originalPuzzle[lineCount]:
	# 				switchables.append(digit);
	# 		if len(switchables) > 1:
	# 			# maybe dont need this?
	# 			for digit in currentVersion[lineCount]:
	# 				done = False;
	# 				if digit in originalPuzzle[lineCount]:
	# 					mutatedLine += digit;
	# 				elif not done:
	# 					randomIndex = random.randint(0,len(switchables)-1)
	# 					mutatedLine += switchables[randomIndex];
	# 					switchables.remove(switchables[randomIndex]);
	# 					done = True;
	# 				else:
	# 					mutatedLine += digit;
	# 					# switchables = switchables[:switchables.index(randomIndex)] + switchables[switchables.index(randomIndex + 1):]
	# 			mutatedPuzzle.append(mutatedLine);
	# 		lineCount += 1;
	# 	# print 'returns?'
	# 	return mutatedPuzzle;

	# # print mutationMaker(workingPuzzle, possiblySolved);

	# # simulated annealing --> tabu: generate multiple versions with mutations and keep one with fewest errors
	
	# def tabuMaker(possiblySolved, errors):
	# 	tabus = [];
	# 	tabuCount = 10;
	# 	while tabuCount > 0:
	# 		tabus.append(mutationMaker(workingPuzzle, possiblySolved, errors));
	# 		tabuCount -= 1;

	# 	tabuErrors = [];
	# 	for t in tabus:
	# 		tabuErrors.append(checkAllErrors(t));

	# 	numErrors = sorted(tabuErrors)[0];
	# 	if numErrors == 0:
	# 		print '0 errors!'
	# 	# only accept mutations that DECREASE number of errors
	# 	# print tabuErrors;
	# 	# check if errors == 0?
	# 	bestMutation = tabus[tabuErrors.index(sorted(tabuErrors)[0])]; 
	# 	# print bestMutation;
	# 	return [bestMutation, numErrors];

	# # mutationMaker()

	# mutations = 0;
	# fewestErrors = 30;
	# tabu = tabuMaker(possiblySolved, fewestErrors);
	# newBest = tabu[0];
	# fewestErrors = tabu[1];

	# while mutations < 100:
	# 	tabu = tabuMaker(newBest, fewestErrors);
	# 	test = tabu[0];
	# 	testErrors = tabu[1];
	# 	if testErrors < fewestErrors:
	# 		fewestErrors = testErrors;
	# 		newBest = test;
	# 		print newBest;
	# 	# else:
	# 		# print 'too many errors'
	# 	mutations += 1;

	# keep checking for errors until equals 0

	# once error has been found, shuffle the numbers
	

# keep track of numbers that have been tested in spots?
# use forced algorithm first and then stochastic?

# for each puzzle, for reach row, indices that are free and which numbers can go in them







