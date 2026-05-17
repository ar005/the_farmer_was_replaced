def move_to(a,b):
	x=get_pos_x()
	y=get_pos_y()
	
	if y!=b:
		if (b-y>0):
			for i in range(b-y):
				move(North)
		elif (b-y<0):
			for i in range(y-b):
				move(South)
	if x!=a:
		if (a-x>0):
			for i in range(a-x):
				move(East)
		elif (a-x<0):
			for i  in range(x-a):
				move(West)
