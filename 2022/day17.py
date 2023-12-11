import time
import numpy as np

def main(input):
    class shape:
        def __init__(self,) -> None:
            self.coordinates:list[tuple[int,int]] = []

            

        def reset_shape(self, shape:str,y:int) ->None:
            self.y = y
            if shape =="+":
                self.coordinates = [(y+1,2),(y,3),(y+1,4),(y+2,3),(y+1,3)]
                # left,bot,right,top,middle
            elif shape =="-":
                self.coordinates=[(y,2),(y,3),(y,4),(y,5)]
            elif shape == "_I":
                self.coordinates= [(y,2),(y,3),(y,4),(y+1,4),(y+2,4)]
            elif shape == "I":
                self.coordinates =[(y,2),(y+1,2),(y+2,2),(y+3,2)]
            elif shape == "sq":
                self.coordinates = [(y,2),(y,3),(y+1,3),(y+1,2)]
        
        def get_move_coords(self,direction):
            res = []
            
            if direction == "<":
                for coord in self.coordinates:
                    res.append((coord[0], coord[1]-1))
            if direction == ">":
                 for coord in self.coordinates:
                    res.append((coord[0], coord[1]+1))
            if direction =="down1":
                for coord in self.coordinates:
                    res.append((coord[0]-1, coord[1]))
            return res

        def move(self,direction):
            res = []
            if direction == "<":
                print("<")
                for coord in self.coordinates:
                    res.append((coord[0], coord[1]-1))
            if direction == ">":
                print(">")
                for coord in self.coordinates:
                    res.append((coord[0], coord[1]+1))
            if direction == "down":
                for coord in self.coordinates:
                    res.append((coord[0]-1, coord[1]))
            
            self.coordinates = res

        def max_y(self):
            max_y = 0
            for coord in self.coordinates:
                if coord[1] >= max_y:

                    max_y = coord[1]
        
    
    class map_class:
        def __init__(self, width:int) -> None:
            array =  np.full((4,width), 1)
            floor = np.full((1,width), 2)
            array = np.append(array, floor, axis=0)
            wall = np.full((5), 2)
            array = np.insert(array,0, wall, axis = 1)
            array = np.insert(array,width+1, wall, axis = 1)
            self.array = array
            self.block_start = 3

        def check_collison(self, coords)-> bool:
            for coord in coords:
                if self.array[coord[0]][coord[1]] in [2,0]:
                    print(coord)
                    return True
                
            return False

        def set_shape(self,coords):
            for coord in coords:
                self.array[coord[0]][coord[1]] = 0

    map_obj = map_class(7)
    shape_obj = shape()
    # shape_obj.reset_shape("-",map_obj.block_start)
    shape_variants = ["-", "+","_I", "I", "sq" ]
    shape_counter = 0
    pattern = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    pattern_counter = 0
    

    while shape_counter < 1:
        shape_obj.reset_shape(shape_variants[shape_counter % 6],map_obj.block_start)
        moving = True
        hor_move = True
        while moving:
            if hor_move:
                hor_move_direction = pattern[pattern_counter % len(pattern)]
                collision =map_obj.check_collison(shape_obj.get_move_coords(hor_move_direction))
                
                if not collision:
                    
                    shape_obj.move(hor_move_direction)

                
                hor_move = False
                pattern_counter = pattern_counter +1
            else:
                collision = map_obj.check_collison(shape_obj.get_move_coords("down"))
                
                if not collision:
                    shape_obj.move(shape_obj.move("down"))

            if map_obj.check_collison(shape_obj.get_move_coords("down")):
                moving = False
                map_obj.set_shape(shape_obj.coordinates)

        shape_counter = shape_counter +1
   
    print(map_obj.array)
   


    








if __name__ == "__main__":
    st = time.time()
    # with open("day16 sample.txt") as f:
    #     input = f.readlines()
    input =""
    main(input)
    et = time.time()
    print("Time: " + str(et-st))