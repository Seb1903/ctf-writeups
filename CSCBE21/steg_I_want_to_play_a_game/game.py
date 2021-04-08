state = 48578

def roll_die() : 
    global state
    state =state*107 % 233
    return (state % 6 )+1 


numberlist = [43763,
47401,
48578,
53393,
54570,
67517,
68694,
72332,
73509,
78324,
79501,
92448,
93625,
97263,
98440,
103255,
104432,
117379,
118556,
122194,
123371,
128186,
129363,
]
for e in range(30) : 
    state = numberlist[e]
    move_list = []
    for i in range(100) : 
        move_list.append(roll_die())
    if move_list[0] == 5 and move_list[1] == 1 :       
        print(move_list)



