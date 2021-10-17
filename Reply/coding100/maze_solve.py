# In the map, every "block" describes a position. You first find where the string of the first line of the blocks
# is in the maze. Once you know it, the next line (a number) specifies how much lines further down is the
# next charcter. The next line says how much characters to the right is the character you need to find (in relation to the first char of the first line). 
# see exmaple.txt
def find_char(place, maze, map, i) :
    index = 0
    char = ""
    for j in range(len(maze)) : 
        # a = re.search(r'\b({})\b'.format(place), maze[j])
        a = maze[j].find(place)
        if a != -1 : 
            string_index  = j
            char_index = a
            char = maze[string_index + int(map[i + 1])][char_index + int(map[i+2]) ]
            return char
        else : 
            pass
 
    


with open("maze.txt") as f :  
    #First format the maze and the map correctly, so I can access lines easily.
    secret = ""
    text = f.readlines()
    maze = []
    for elem in text : 
        maze.append(elem.strip())   #deletes spaces and \n at the end of lines
    with open("map.txt") as g : 
        tmp_map = g.readlines()
        map = []
        for elem in tmp_map : 
            map.append(elem.strip())
        i = 0 
        # For every block in the map, find the corresponding characte 
        while i < len(map) : 
            secret += find_char(map[i], maze, map, i)
            i += 6
        print(secret)


    
