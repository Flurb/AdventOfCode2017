#
# Day 2: Corruption Checksum
#

import sys

class Day2:

	def get_sum_checksum(input_file):

		# Full sum to return.
		full_sum = 0

		# Open file..
		with open(input_file) as f:
			# For each line in the file..
			for line in f:
				# Get all values in an array of integers.
				all_numbers = [int(n) for n in line.split()]
				# For each value in the array.
				for index, value in enumerate(all_numbers):
					# Check with every other element in the array.
					for next_value in all_numbers[index+1:]:
						# And compare.
						a, b = max(value,next_value), min(value,next_value)
						if a % b == 0:
							full_sum += a // b
							break

		return full_sum

	if __name__ == '__main__':
		print get_sum_checksum(sys.argv[1])