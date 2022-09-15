from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	result = list(range(number))
	random.seed(seed)
	random.shuffle(result)
	return result

def generate():
	number = 10
	seed = 200
	array = gen_random_int(10,200)
	# call gen_random_int() with the given number and seed
	# store it to the variable array
	array_str=""


	for i in range(len(array)):
		if i == len(array)-1:
			array_str += str(array[i]) +"."
		else:
			array_str += str(arrayx[i]) +", "

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	new_str = "1, 15, 8, 10, 11."
#   random_str = None
#   document.getElementById("generate").innerHTML = random_str
  # remove full stop
	new_str = new_str	.strip(".")
  	# make array
	random_array = new_str.split(",")
  	# #bubble sort algo
	n = len(random_array)
	for bi in range(n-1):
		swapped = False
		for si in range(1, n-bi):
			if random_array[si-1] > random_array[si]:
				swapped = True
				random_array[si-1], random_array[si] = random_array[si], random_array[si-1] 
		if not(swapped):
			break
  # '''  This function is used in Exercise 1.
  #   The function is called when the sort button is clicked.

  #   You need to do the following:
  #   - get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
  #   - create a list of integers from the string of numbers
  #   - call your sort function, either bubble sort or insertion sort
  #   - create a string of the sorted numbers and store it in array_str
  
  # '''
  #turn array into string and store into array str

	array_str = ''.join(str(e) for e in random_array)
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value
	new_array= value.split(',')
	n = len(new_array)
	swapping = True
	while swapping is True:
		swapping = False
		m = 0
		for i in range(1,n):
			x = new_array[i-1]
			y = new_array[i]
			if x>y:
				new_array[i-1] , new_array[i] = new_array[i] , new_array[i-1]
				swapping = True
				m = i
		n = m
	
	# Your code should start from here
	# store the final string to the variable array_str
	
	document.getElementById("sorted").innerHTML = str(new_array)


