# Solving Sudoku by CSP

The game [Sudoku](https://www.websudoku.com/) can be treated as a search problem with several constraints. So it is a constraint satisfaction problem, and can be solved by basic CSP algorithm.

## Documents

The file `driver.py` is what I wrote totally with basic CSP algorithm. The  following code represents a 9x9  big cubes with each 3x3 sub cubes sudoku, like the gameboard [here](https://www.websudoku.com/):

```python
test_string ='000000000302540000050301070000000004409006005023054790000000050700810000080060009'
```

Here the sudoku is represent row by row, which means the 1st 9 digits in the string represents the 1st 9 row digits in the sudoku. And `0` meas the cube here is empty and needs to figure out!

`sudokus_start.txt` is a file which each line represents a sudoku needed to solve. And `sudokus_finish.txt` is the results after implementing CSP algorithm, which I wrote.

In addition, we know that there is technique called `Arc consistency` in CSP, which I haven't coded here.  But it is enough to solve it.

## Basic CSP

![basic CSP algorithm](D:\DBSX\SOFTWARE\IT\Project\project_to_show\Solving Sudoku by CSP\basic CSP algorithm.png)For more information related to CSP, please take a look at `excerpt.pdf`.