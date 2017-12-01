#
# Day 1: Inverse Captcha
#
import sys

class Day1:

	def new_captcha(captcha):
		# The total count to return.
		total_count = 0

		# Get the length of the captcha.
		length_captcha = len(captcha)

		# Get the exact halfway.
		captcha_halfway = length_captcha // 2

		# Iterate over the captcha.
		for index, value in enumerate(captcha):
			# Get the index in the next half of the sequence.
			in_next_half = (index + captcha_halfway) % length_captcha

			# Get the value in the next half.
			valueInNextHalf = captcha[in_next_half]

			# If it's the same, sum it up!
			if valueInNextHalf == value:
				total_count += int(valueInNextHalf)

		return total_count

	if __name__ == '__main__':
		# Get the input file.
		my_captcha = open(sys.argv[1]).read()

		print new_captcha(my_captcha)