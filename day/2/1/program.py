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
				all_numbers = [int(a) for a in line.split()]

				# Init the smallest and biggest.
				smallest = sys.maxint
				biggest = 0

				# Iterate over each value, and check
				# for biggest and smallest.
				for next_value in all_numbers:
					if next_value < smallest:
						smallest = next_value
					if next_value > biggest:
						biggest = next_value

				# Add it up!
				full_sum += (biggest - smallest)

		return full_sum

	if __name__ == '__main__':
		print get_sum_checksum(sys.argv[1])