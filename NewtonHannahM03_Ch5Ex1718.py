Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_prime( user_number ):
	even_divisions = 0
	if user_number <= 1:
		return False
	for current_number in range(1, user_number + 1):
		if user_number % current_number == 0:
			even_divisions = even_divisions + 1
			if even_divisions > 2:
				return False
	return True

>>> def main():
	for current_number in range( 1, 101 ):
		if is_prime( current_number ):
			print( current_number, end=" ")

			
>>> main()
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
>>> 