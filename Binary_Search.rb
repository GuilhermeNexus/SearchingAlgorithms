list = Array[3,6,9,39,40,59,259,609,709]


beginning_index = 0
endind_index = (list.size) - 1
search_value = list[rand(list.size-1)]
seach_value_index = 0
puts "Search Value: " + String(search_value) 


while beginning_index <= endind_index

	mid_index = beginning_index + (endind_index - beginning_index / 2).floor
  puts "Beginning_index: " + String(beginning_index)
  puts "Ending_index: " + String(endind_index)
  puts"-"
  mid_value = list[mid_index]
	if mid_value == search_value
		search_value_index = mid_index
    break
  	elsif search_value < mid_value
			endind_index = mid_index-1
  	elsif search_value > mid_value
			beginning_index = mid_index + 1
	end
end

puts "Search Value Index: " + String(search_value_index)