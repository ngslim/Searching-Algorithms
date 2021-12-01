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

## With bonus points

The number of bonus points is 2.
Bonus points are saved in the following format in separates lines: <x> <y> <value>.

2
9 18 -10
15 18 -10
x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x x   x   x   xx                       x
x x x x x x x xx x xxxxxxxxxxxxxxxxxxx x
x x x x x x x x  x x                   x
x x x x x x x xx x x xxxxxxxxxxxxxxxxxxx
x   x x x x x xx x x                   x
x xxx   x   x     x xxxxxxxxxxxxxxxxxx x
x  xxxxxxxxxxxxx xx x                  x
x x    x  x    xxxx x xx  x xxxxxxxxxxxx
xxx xx x  x xx      x    xx xx    x  xxx
x           x x xx    xx xxx           x
x  xxxxxxxxxxxxx              xxx  x   x
x                xxxxxxxxxx xxx xx xx  x
x xxxxxxxxxxxxxxxxx       x   x x      x
x                xx xxxxx xxxxx xxxxx  x
x xxxxxxxxxxxxxx      xxx              x
x x            x  xxx xx  xxx xxxxxxxxxx
x x xxxx xx xx xx xxx xxxxxxx          x
x xxxxxx xx xx xx xxx       xxxxxxxxxxxx
x              xx    xxxxx            Sx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  
## Algorithms
 
BFS and DFS are not written to take bonus points into account. Therefore, they can solve the maze but will not consider those bonus points.
  
Greedy Best First Search, A* and Dijkstra can be used to solve mazes with bonus points, though they do not always find the best solution.
  
## Run

Read the readme.txt or watch the instruction video in src folder to see how to run the code.
