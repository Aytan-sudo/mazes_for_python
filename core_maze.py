import random
import algo_maze
from PIL import Image, ImageDraw
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
    def __init__(self, col:int = 20, lines:int = 20):
        self.col = col
        self.lines = lines
        self.cells = []

    def create(self):

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

        #algo_maze.binary_tree(self)
        #algo_maze.aldous_broder(self)
        algo_maze.hunt_and_kill(self)

    def _draw_PNG(self, cell_size:int = 50, bg_color = (255,255,255), wall_color = (0,0,0)):
        
        image_width = cell_size * self.col
        image_height = cell_size * self.lines

        image = Image.new("RGBA", (image_width + 20, image_height + 20), (255,255,255))
        draw = ImageDraw.Draw(image)

        for i in range(2):
            for cell in self.cells:
                x1 = 10 + cell.x * cell_size
                y1 = 10 + cell.y * cell_size
                x2 = 10 + (cell.x + 1) * cell_size
                y2 = 10 + (cell.y + 1) * cell_size

                if i == 0:
                    draw.rectangle([(x1, y1), (x2, y2)], outline=wall_color, fill = bg_color, width=1)
                else:
                    if cell.north_cell is not None:
                        if cell.north_cell.coord in cell.links:
                            draw.line([(x1+1,y1),(x2-1,y1)], fill=bg_color, width=1)
                    if cell.south_cell is not None:
                        if cell.south_cell.coord in cell.links:
                            draw.line([(x1+1,y2),(x2-1,y2)], fill=bg_color, width=1)
                    if cell.east_cell is not None:                        
                        if cell.east_cell.coord in cell.links:
                            draw.line([(x2,y1+1),(x2,y2-1)], fill=bg_color, width=1)
                    if cell.west_cell is not None:        
                        if cell.west_cell.coord in cell.links:
                            draw.line([(x1,y1+1),(x1,y2-1)], fill=bg_color, width=1)
        return image

    def create_PNG(self):
        filename = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
        image = self._draw_PNG()
        image.save("{}.png".format(filename), "PNG", optimize=True)

if __name__ == "__main__":
    #Test processing
    test = Grid()
    test.create()
    #test.cells[4].dig(test.cells[4].west_cell)
    #test.cells[27].dig(test.cells[27].south_cell)
    #test.cells[52].dig(test.cells[52].east_cell)
    #test.cells[33].dig(test.cells[33].west_cell)
    test.create_PNG()
    #for i in test.cells:
        #print(f'La cellule {i} a comme coordonnées Nord {i.north_cell}, Sud {i.south_cell}, Ouest {i.west_cell} et Est {i.east_cell}') 
    
    #result = [i.coord for i in test.cells if i.coord == (2,3)]
    #print(result[0])


    #print(test.map)
