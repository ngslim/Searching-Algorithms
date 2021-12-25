# Searching-Algorithms

The source code includes 5 searching algorithms: Depth First Search, Breadth First Search, Greedy Best First Search, A* and Dijkstra.

The point of these algorithms is to find the path to solve mazes.

# Input file example

There are 2 types of maze: with or without bonus points.

Start point is marked by S.
The obstables are marked by x.
The first interger in each input is the number of bonus points in the maze.
End point is marked by a blank space at the borders of the maze. There can only be 1 end point.

## Without bonus points

The number of bonus points is 0.
*Example input:*
```
0
xxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx        x
x     x     xxxxxxxxxx
x x   xxx  xxxx xxx xx
  x   x x xx   xxxx Sx
x          xxx xx    x
xxxxxxx x      xx  x x
xxxxxxxxx  x x  xx   x
x          x x  x x  x
xxxxx x  x x x       x
xxxxxxxxxxxxxxxxxxxxxx
```
## With bonus points

The number of bonus points is 2.
Bonus points are saved in the following format in separates lines: x y value.
*Example input:*
```
5
3 12 -5
2 7 -10
4 3 -5
9 7 -5
2 2 -7
xxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx        x
x     x+    xxxxxxxxxx
x x   xxx  x+ x xxx xx
  x   x x xx   xxxx Sx
x          xxx xx    x
xxxxxxx x      xx  x x
xxxxxxxxx  x x  xx   x
x          x x  x x  x
xxxxx x  x x x       x
xxxxxxxxxxxxxxxxxxxxxx
```
## Algorithms
 
BFS and DFS are not written to take bonus points into account. Therefore, they can solve the maze but will not consider those bonus points.
  
Greedy Best First Search, A* and Dijkstra can be used to solve mazes with bonus points, though they do not always find the best solution.
  
## Run

Read the readme.txt or watch the instruction video in src folder to see how to run the code.
