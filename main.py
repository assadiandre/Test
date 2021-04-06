
import sys

filepath = sys.argv[1]
input_file = open(filepath,"r")
input_string = input_file.read()

gc_count = 0
for c in input_string:
	if c.lower() in "gc":
		gc_count += 1
gc_percentage = (gc_count / len(input_string)) * 100

print(gc_percentage)

input_file.close()
