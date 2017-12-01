#
# Day 1: Inverse Captcha
#

import sys

class Day1:

	def inverse_captcha(captcha):

		# The total count to return.
		total_count = 0

		# Paste first character at the end of the sequence.
		captcha = captcha + captcha[0]

		# Iterate and get for each element the index and value.
		for index, value in enumerate(captcha):

			# String to Integer conversion.
			number = int(value)

			# Check for end of sequence.
			if index + 1 < len(captcha):

				# Get the next number and check if next value is the same.
				next_number = int(captcha[index + 1])
				if number == next_number:
					# If so, add it up.
					total_count += number

		return total_count

	if __name__ == '__main__':
		# Get the input file.
		my_captcha = open(sys.argv[1]).read()

		print inverse_captcha(my_captcha)