#!/usr/bin/python3

# This program calculates the average seek time for 4 disk scheduling algorithms -
# FCFS, SSF, Elevator, and CSCAN
# I assumed a start position of 10 for all of these algorithms so I could
# demonstrate them fully

import copy
import random
import sys

# First Come First Seeked
def FCFS(r):
	requests = copy.copy(r)
	time = 0
	n = len(requests)
	# assume we are starting at position 10
	position = 10
	for request in requests:
		time += abs(request-position)
		position = request

	# calculate average seek time
	avg_seek = time / n

	print('Algorithm: FCFS\nRequests in buffer: {}\nAvg seek time: {}'.format(n,avg_seek))

# Shortest Seek First
def SSF(r):
	requests = copy.copy(r)
	time = 0
	position = 10
	n = len(requests)
	high = max(requests)
	x = high
	min_seek = abs(position-high)
	requests.sort()
	while len(requests) > 0:
		# find the shortest distance from the current position
		for request in requests:
			seek = abs(position-request)
			if (seek < min_seek):
				min_seek = seek
				x = request
		time += abs(position-x)
		position = x
		requests.remove(x)
		min_seek = abs(position-high)
		x = high

	avg_seek = time / n

	print('Algorithm: SSF\nRequests in buffer: {}\nAvg seek time: {}'.format(n,avg_seek))

def ELEVATOR(r):
	requests = copy.copy(r)
	time = 0
	position = 10
	n = len(requests)

	# seek to end from starting position
	end = max(requests)
	for x in range(10,end):
		if (x in requests):
			time += abs(position-x)
			position = x
			requests.remove(x)
	# seek back up from end to 0
	count = end
	while count >= 0:
		if (count in requests):
			time += abs(position-count)
			position = count
			requests.remove(count)
		count -= 1

	avg_seek = time / n
	print('Algorithm: ELEVATOR\nRequests in buffer: {}\nAvg seek time: {}'.format(n,avg_seek))

# Circular elevator 
def CSCAN(r):
	requests = copy.copy(r)
	time = 0
	position = 10
	n = len(requests)

	# seek to end from starting position
	end = max(requests)
	for x in range(10,end):
		if (x in requests):
			time += abs(position-x)
			position = x
			requests.remove(x)

	# go back to beginning and continue seeking
	end = max(requests)
	for i in range(0,end):
		if (i in requests):
			time += abs(position-i)
			position = i
			requests.remove(i)

	avg_seek = time / n
	print('Algorithm: CSCAN\nRequests in buffer: {}\nAvg seek time: {}'.format(n,avg_seek))

def main():
	args = sys.argv[1:]
	if len(args) < 1:
		print('USAGE: ./disk_scheduling.py <number of requests>')
		exit(-1)
	n = args[0]
	n = int(n)

	# create a random list of n requests
	requests = [0 for x in range(n)]
	for i in range(n):
		requests[i] = random.randint(0,200)

	# perform the simulations
	FCFS(requests)
	print('\n')
	SSF(requests)
	print('\n')
	ELEVATOR(requests)
	print('\n')
	CSCAN(requests)

if __name__ == '__main__':
	main()     
