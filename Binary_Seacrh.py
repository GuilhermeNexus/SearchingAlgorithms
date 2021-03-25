import random
list = [1,5,9,20,26,31,50,60,79];

print(list);


beginning_index = 0
ending_index = len(list)-1
search_value =  list[random.randint(0,len(list)-1)]
print(f"search value: {search_value}")
search_value_index = 0

while beginning_index <= ending_index:

	mid_index = beginning_index + (ending_index - beginning_index) // 2
	mid_value = list[mid_index]
	if mid_value == search_value:
		search_value_index = mid_index
		break
	elif search_value < mid_value:
		ending_index = mid_index - 1

	elif search_value > mid_value:
		beginning_index = mid_index + 1
print(list)
print(f"search value index {search_value_index}")
