from PIL import Image, ImageDraw
from time import localtime, strftime

def draw_PNG(Grid, cell_size:int = 50, bg_color = (255,255,255), wall_color = (0,0,0)):  
    image_width = cell_size * Grid.col
    image_height = cell_size * Grid.lines

    image = Image.new("RGBA", (image_width + 20, image_height + 50), (255,255,255))
    draw = ImageDraw.Draw(image)

    for i in range(2):
        for cell in Grid.cells:
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
    draw.text((10,image_height+15), f"Labyrinthe produit avec l'algorithme {Grid.algo}", fill = wall_color, anchor = "ma")

    filename = strftime("%Y_%m_%d_%H_%M_%S", localtime())
    image.save("{}.png".format(filename), "PNG", optimize=True)

