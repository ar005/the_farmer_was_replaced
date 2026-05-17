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

def need_water():
	while (get_water()<0.25):
			print(get_water()," hence watering")
			use_item(Items.Water)
move_to(0,0)
while True:
	if can_harvest():
		harvest()
	else:
		for i in range(6):
			for j in range(6):
				if (i<j):
					move_to(i,j)
					if get_ground_type()!=Grounds.Soil:
						till()
					else:
						if can_harvest():
							harvest()
							need_water()
							plant(Entities.Pumpkin)
						else:
							if get_entity_type()==Entities.Dead_Pumpkin:
								need_water()
								plant(Entities.Pumpkin)
							need_water()
							plant(Entities.Pumpkin)
				elif (i==j):
					move_to(i,j)
					if can_harvest():
						harvest()
						need_water()
						plant(Entities.Tree)
					else:
						need_water()
						plant(Entities.Tree)
				else:
					move_to(i,j)
					if get_ground_type()!=Grounds.Soil:
						till()
					else:
						if can_harvest():
							harvest()
							need_water()
							plant(Entities.Carrot)
						else:
							need_water()
							plant(Entities.Carrot)
			for i in range(8):
				for j in range(8):
					move_to(i,j)
					if ((i>6) or (j>6)):
						if can_harvest():
							harvest()
							need_water()
							plant(Entities.Grass)
						else:
							need_water()
							plant(Entities.Grass)
