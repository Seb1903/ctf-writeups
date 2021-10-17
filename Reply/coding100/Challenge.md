You're given the 3 text files, description of the challenge didn't give any hints. 

# Solution : 

 In the map, every "block" describes a position. You first find where the string of the first line of the blocks is in the maze. Once you know it, the next line (a number) specifies how much lines further down is the character that you need to find. The next line says how much characters to the right is the character you need to find (in relation to the first char of the string you first found in the maze).   
 See example.txt
 
 The python file is the scripted solution, once you run it, you obtain a long string which includes the flag :   
 {FLG:y0U_L34rNt-Th3.l4ngUa6e-0f_tHe*4nC13nt5-Ord0s}
