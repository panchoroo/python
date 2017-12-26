# A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary 
# to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this).
#  The complexity of the search determines the difficulty of the puzzle; the example above is considered easy 
#  because it can be solved by straight forward direct deduction.

# The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
#  ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

# By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution 
# grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

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
	for line in workingPuzzle:
		thisLineDigits = '';
		for d in possibleDigits:
			if d not in line:
				thisLineDigits += d;
		# print thisLineDigits;
		for digit in line:
			# print digit
			if digit == '0':
				line = line[:line.index(digit)] + thisLineDigits[startIndex] + line[line.index(digit)+1:]
				# print line
				# line[line.index(digit)] = ;
				thisLineDigits = thisLineDigits[1:];
				# what happens when it finds an error?  maybe inc start index by 1? 
				# or shuffle digits around? but dont let start digit end up in same place? 
		# print line;
		possiblySolved.append(line);
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

	# while totalErrors > 0: 
	totalErrors = checkAllErrors(possiblySolved);
	if totalErrors == 0:
		# add to actual solutions
		print 'yay!'
	else: 
		print 'nerrrrp'
		print totalErrors;

	def mutationMaker(originalPuzzle, currentVersion, errors):
		# could make it have greater mutations based on number of errors?
		# make mutations smaller as it gets closer
		lineCount = 0;
		switchables = [];
		mutatedPuzzle = [];
		while lineCount < 9:
			mutatedLine = '';
			for digit in currentVersion[lineCount]:
				if digit not in originalPuzzle[lineCount]:
					switchables.append(digit);
			if len(switchables) > 1:
				# maybe dont need this?
				for digit in currentVersion[lineCount]:
					done = False;
					if digit in originalPuzzle[lineCount]:
						mutatedLine += digit;
					elif not done:
						randomIndex = random.randint(0,len(switchables)-1)
						mutatedLine += switchables[randomIndex];
						switchables.remove(switchables[randomIndex]);
						done = True;
					else:
						mutatedLine += digit;
						# switchables = switchables[:switchables.index(randomIndex)] + switchables[switchables.index(randomIndex + 1):]
				mutatedPuzzle.append(mutatedLine);
			lineCount += 1;
		# print 'returns?'
		return mutatedPuzzle;

	# print mutationMaker(workingPuzzle, possiblySolved);

	# simulated annealing --> tabu: generate multiple versions with mutations and keep one with fewest errors
	
	def tabuMaker(possiblySolved, errors):
		tabus = [];
		tabuCount = 10;
		while tabuCount > 0:
			tabus.append(mutationMaker(workingPuzzle, possiblySolved, errors));
			tabuCount -= 1;

		tabuErrors = [];
		for t in tabus:
			tabuErrors.append(checkAllErrors(t));

		numErrors = sorted(tabuErrors)[0];
		if numErrors == 0:
			print '0 errors!'
		# only accept mutations that DECREASE number of errors
		# print tabuErrors;
		# check if errors == 0?
		bestMutation = tabus[tabuErrors.index(sorted(tabuErrors)[0])]; 
		# print bestMutation;
		return [bestMutation, numErrors];

	# mutationMaker()

	mutations = 0;
	fewestErrors = 30;
	tabu = tabuMaker(possiblySolved, fewestErrors);
	newBest = tabu[0];
	fewestErrors = tabu[1];

	while mutations < 100:
		tabu = tabuMaker(newBest, fewestErrors);
		test = tabu[0];
		testErrors = tabu[1];
		if testErrors < fewestErrors:
			fewestErrors = testErrors;
			newBest = test;
			print newBest;
		else:
			print 'too many errors'
		mutations += 1;

	# keep checking for errors until equals 0

	# once error has been found, shuffle the numbers
	

# keep track of numbers that have been tested in spots?
# use forced algorithm first and then stochastic?

# for each puzzle, for reach row, indices that are free and which numbers can go in them




