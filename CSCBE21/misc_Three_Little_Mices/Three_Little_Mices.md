# Context 

Three Little Mices ran up the clock... Can you find all the flags ? 

Challenge 1 :   
host = '3.248.160.188'
port = 2554
 
Challenge 2 :  
host = '46.137.38.11' 
port = 2555

Challenge 3 :   
host = '54.155.193.84'
port = 2556

# Solving
We have no particular info on the servers. Therefore we will be launching blind attacks. The hints were suggesting time attacks. 

1. Mice 1  

For the first challenge, the response wasn't the same for every sent password. Indeed, for a specific character, the response would be longer. In this case, the server was sending "Validating.." instead of "Validating.". The more correct characters were found, the more dots were printed. Script can be found in Mice_1.py.  
Once you've founded the password, you send it to the server and it gives you the flag. 

2. Mice 2  

For this challenge we did a time attack. We checked the response time for every character, the one that took the longest was the good one. It was the added to a string and then we would test all the next characters. Script can be found in Mice_2.py.

3. Mice 3 

This one was quite the same as the previous one but you needed to test special characters (and had to play with the python encoding).  

sock.send(b'\r\xec\xaf')  would give you the solution. 



