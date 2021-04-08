x = 24
ans = x *107 % 233

def roll_die(state) : 
    state =state*107 % 233
    return (state % 6 )+1 

state2_list = []
for i in range(1000) :  
   if roll_die(i) == 1 : 
       state2_list.append(i)

for elem in state2_list : 
    state1 = (elem +233) * 107 
    if roll_die(state1) == 5 : 
        print(state1)

#print(anstest)
#print(ans)
#print((ans % 6) + 1)

