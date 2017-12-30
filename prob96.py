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
	inFile = open(sudokuText, 'r');
	line = inFile.readline();
	sudokuList = [];
	while line:
		if line[0] == 'G':
			newPuzzle = [];
			count = 0;
		if count > 0:
			newPuzzle.append(line[:9]);
		count += 1;
		if count >= 8:
			if newPuzzle not in sudokuList:
				sudokuList.append(newPuzzle);
		line = inFile.readline();
	inFile.close();
	return sudokuList;

puzzleList = loadSuccesses();
# when it works, load all 50 puzzles, for now, just the first one
# puzzleList = [['003020600', '900305001', '001806400', '008102900', '700000008', '006708200', '002609500', '800203009', '005010300']];
# print puzzleList;

puzzleCount = 1;
solutionsList = [];
for p in puzzleList:
	# print ('puzzle number ', puzzleCount);
	puzzleCount += 1;
	# iterate through each puzzle from the text file
	startIndex = 0;
	workingPuzzle = p;
	possiblySolved = [];
	possibleDigits = '123456789'
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
 		return [peers, gridPeers];

 	def singler(values):
 		# goes through values and finds squares that have only one possibility
 		changeMade = False;
 		noErrors = False;
 		rowIndex = 0;
	  	while rowIndex < 9:
	  		colIndex = 0;
		  	while colIndex < 9:
		  		if len(values[rowIndex][colIndex]) == 1:
		  			# If a square has only one possible value, 
		  			# then eliminate that value from the square's peers.
		  			onlyVal = values[rowIndex][colIndex];
		  			peersGotten = getPeers(rowIndex, colIndex);
		  			peers = peersGotten[0];
		  			for p in peers:
		  				peerVal = values[p[0]][p[1]];
		  				if onlyVal in peerVal:
		  					values[p[0]][p[1]] = peerVal[:peerVal.index(onlyVal)] + peerVal[peerVal.index(onlyVal)+1:];
		  					if len(values[p[0]][p[1]]) < 1:
		  						noErrors = False;
		  					changeMade = True;
		  		colIndex += 1;
	  		rowIndex += 1;
	  	return [values, changeMade, noErrors];

 	def unitChecker(values):
		# If a unit has only one possible place for a value, then put the value there.
		changeMade = False;
		rowIndex = 0;
		digits = '123456789';
		while rowIndex < 9:
		  	for d in digits:
		  		digitCount = 0;
		  		digitIndex = 0;
		  		digitCountCol = 0;
		  		digitIndexCol = 0;
		  		colIndex = 0;
			  	while colIndex < 9:
			  		if d in values[rowIndex][colIndex]:
			  			digitCount += 1;
			  			digitIndex = colIndex;
			  		if d in values[colIndex][rowIndex]:
			  			digitCountCol += 1;
			  			digitIndexCol = colIndex;
			  		colIndex += 1;
			  	if digitCount == 1 and len(values[rowIndex][digitIndex]) > 1:
			  		values[rowIndex][digitIndex] = d;
			  		changeMade = True;
			  	if digitCountCol == 1 and len(values[digitIndexCol][rowIndex]) > 1:	
			  		values[digitIndexCol][rowIndex] = d;
			  		changeMade = True;
	  		rowIndex += 1;

	  	gridCheck = 0;
	  	while gridCheck < 7:
		  	peersGotten = getPeers(gridCheck,gridCheck);
		  	gridPeers = peersGotten[1];
		  	gridPeers.append([gridCheck, gridCheck]);
		  	
		  	for d in digits:
		  		digitCount = 0;
		  		pVal = 0;
		  		for p in gridPeers:
		  			peerVal = values[p[0]][p[1]];
		  			if d in peerVal:
				  		digitCount += 1;
			  			pVal = p;
			  	if digitCount == 1 and len(values[pVal[0]][pVal[1]]) > 1:
		  			values[pVal[0]][pVal[1]] = d;
			  		changeMade = True;
		  	gridCheck += 3;

	  	return [values, changeMade];

	def checkAllErrors(possibleSolution):
		# checks grids and columns, rows are error free by design
		def gridChecker(rowStart, colStart):
			gridNums = '';
			count = 0;
			line = possibleSolution[rowStart];
			colCount = 0;
			errors = 0;

			while count < 9:
				if count == 3:
					line = possibleSolution[rowStart+1];
					colCount = 0;
				elif count == 6: 
					line = possibleSolution[rowStart+2];
					colCount = 0;

				digit = line[colStart+colCount];
				if digit in gridNums:
					errors += 1;
				else:
					gridNums += digit;
				count += 1;
				colCount += 1;
			return errors;

		def colChecker():
			errors = 0;
			colIndex = 0;
			rowIndex = 0
			while colIndex < 9:
				colNums = '';
				while rowIndex < 9:
					if possibleSolution[rowIndex][colIndex] not in colNums:
						colNums += possibleSolution[rowIndex][colIndex];
					else: 
						errors += 1;
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

	def twoStrategySolver(values):
		# (1) If a square has only one possible value, then eliminate that value from the square's peers. 
		# (2) If a unit has only one possible place for a value, then put the value there.
		notDone = True;
		while notDone:
			singled = singler(values);
			values = singled[0];
			notDone = singled[1];
			error = singled[2];
			if error:
				return error;
			unitChecked = unitChecker(values);
			values = unitChecked[0];
			notDone = unitChecked[1];
		return values;		

	def solutionChecker(values):
		solved = True;
		solution = [];
		index = 0;
		while index < 9:
			line = ''.join(values[index]);
			if len(line) > 9:
				# randomGuess(maybeSolved);
				# print ('index', index);
				solved = False;
				break;
			else: 
				solution.append(line);
			index += 1;
		# print ('solution', solution);
		# if :
		if solved:
			return [solution, solved];
			# maybe return place where it failed?
		return [index, solved];

	def randomGuess(rowIndex, values):
		# (3) if no more squares can be filled in with 1 and 2, guess by trying one possibility out of 2, 
		# check for errors and if that one doesn't work out, fix the other possibility
		# print ('random guess index', index);
		# index of place where it failed (i.e. had too many values still)
		colIndex = 0;
		otherGuess = 0;
		guessed = False
		while colIndex < 9:
			if len(values[rowIndex][colIndex]) == 2:
				# print v;
				otherGuess = values[rowIndex][colIndex][1];
				values[rowIndex][colIndex] = values[rowIndex][colIndex][0];
				# check errors, 
				 # if checkAllErrors(solution) == 0:
				# checkSolution(values);
				# twoStrategySolver(values)
				guessed = True;
				break;
			colIndex += 1;
		return [values, otherGuess];


	def checkSolution(values):
		done = False
		otherGuess = 0;
		newValues = [];
		guessed = False;

		while not done:
			twoStrategied = twoStrategySolver(values);

			if twoStrategied:
				maybeSolved = solutionChecker(twoStrategied);
			else:
				# values ended up with '' 
				print 'ERROR';
				done = True;

			if maybeSolved[1]:
				print maybeSolved[0];
				solutionsList.append(maybeSolved[0]);
				done = True;
				break;
			elif not guessed: 
				print 'guessing!'
				randomGuessed = randomGuess(maybeSolved[0], values);
				newValues = randomGuessed[0];
				otherGuess = randomGuessed[1];
				guessed = True;
				# now use singler and unitChecker to see if we can get a solution
				# if errors occur, come back and get the other number instead
				# possible errors: 1) no possible values for a square 2) more than one of a digit in a unit 
				# 3)  needs another guess? 
			else:
				# already guessed once
				print 'guess again?'
				done = True;


				

				
				# newValues = twoStrategySolver(values);
				# if newValues and checkAllErrors() == 0:

				# else: 
					# there was an error with values, so go back and pick the other guess
					# values[rowIndex][colIndex] = otherGuess;


	checkSolution(possibleValues);





