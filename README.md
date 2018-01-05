# sudoku-solver

I wrote this Sudoku solver for Project Euler problem number 96.  This is the description of the problem:

       A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it 
       may be necessary to employ "guess and test" methods in order to eliminate options (there is much 
       contested opinion over this).  The complexity of the search determines the difficulty of the puzzle;

       The 6K text file, sudoku.txt contains fifty different Su Doku puzzles ranging in difficulty, but 
       all with unique solutions.

       By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of 
       each solution grid.

I use some of the standard naming conventions I found on Peter Norvig's essay (http://norvig.com/sudoku.html) about this problem.  I use the term 'unit' to mean a collection of 9 squares in the 9x9 grid wherein that unit can only contain each digit 1-9 once.  Units can be a row, column, or box (one of the nine 3x3 subgrids).  For every square, it's 'peers' are the set of the squares in its row, its column, and its box.

Peter Norvig uses constraint propogation for easy puzzles, and then a search algorithm for hard puzzles (i.e. ones that 
involve guessing.)  For such puzzles, I decided to use a recursive method that branches on a square with the minimum number of possibilities.

The constraint propogation works on the two main principals of the game of Sudoku:
(1) If a square has only one possible value, then eliminate that value from the square's peers. 
(2) If a unit has only one possible place for a value, then place it there.
The solver alternates between these two strategies until no more changes can be made.  If the puzzle is not solved, then it branches (which is equivalent to a human guessing when solving a Sudoku.)  When it finds an error in a branch, it discards it.  If it's able to solve that branch, it returns the solution. It is possible to have nested branches (i.e. multiple guesses, and in fact is necessary for at least one of the Project Euler Sudokus.)
