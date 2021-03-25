import random
def Fill_List(vector):
	for i in range(0,(random.randint(2,20))):
		random_number = random.randint(0,99);
		vector.append(random_number);
	return vector


