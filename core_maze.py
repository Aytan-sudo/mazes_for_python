import random
import algo_maze
import print_maze
from time import gmtime, strftime

class Cell:

    def __init__(self, x:int, y:int):
        self.coord = (x,y)
        self.x = x
        self.y = y
        self.links = []
        self.north_cell = None
        self.south_cell = None
        self.east_cell = None
        self.west_cell = None
        self.neighbors = []

    def __repr__(self):
        return str(self.coord)

    def dig(self, cell):
        self.links.append(cell.coord)
        cell.links.append(self.coord)

    def neighbors_create(self):
        if self.north_cell is not None:
            self.neighbors.append(self.north_cell)
        if self.south_cell is not None:
            self.neighbors.append(self.south_cell)
        if self.east_cell is not None:
            self.neighbors.append(self.east_cell)
        if self.west_cell is not None:
            self.neighbors.append(self.west_cell)
        

class Grid:
    def __init__(self, col:int = 20, lines:int = 20, algo:str = "ab"):
        self.col = col
        self.lines = lines
        self.algo = algo
        self.cells = []

        for i in range(self.col): #create grid.cells (list of cells)
            for ii in range(self.lines):
                self.cells.append(Cell(i,ii))

        for i in self.cells: #define coordinates of neighborgs cells only if in the grid
            if 0 < i.y < self.lines:
                for ii in self.cells:
                    if ii.coord == (i.x,i.y-1):
                        i.north_cell = ii
            if 0 < i.y+1 < self.lines:
                for ii in self.cells:
                    if ii.coord == (i.x,i.y+1):
                        i.south_cell = ii
            if 0 < i.x < self.col:
                for ii in self.cells:
                    if ii.coord == (i.x-1,i.y):
                        i.west_cell = ii
            if 0 < i.x+1 < self.col:
                for ii in self.cells:
                    if ii.coord == (i.x+1,i.y):
                        i.east_cell = ii
            i.neighbors_create()
        
        algo_maze.creation_algorithms[algo](self)
    
    def create_png(self):
        print_maze.draw_PNG(self)

if __name__ == "__main__":
    #Test processing
    test = Grid(algo = "bt")
    #test.create()
    test.create_png()
    #test.cells[4].dig(test.cells[4].west_cell)
    #test.cells[27].dig(test.cells[27].south_cell)
    #test.cells[52].dig(test.cells[52].east_cell)
    #test.cells[33].dig(test.cells[33].west_cell)
    #test.create_PNG()
    #for i in test.cells:
        #print(f'La cellule {i} a comme coordonnées Nord {i.north_cell}, Sud {i.south_cell}, Ouest {i.west_cell} et Est {i.east_cell}') 
    
    #result = [i.coord for i in test.cells if i.coord == (2,3)]
    #print(result[0])


    #print(test.map)
