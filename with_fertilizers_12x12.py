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
	while (get_water()<0.50):
			use_item(Items.Water)
def check_pumpkin():
	if get_entity_type()==Entities.Dead_Pumpkin:
		need_water()
		plant(Entities.Pumpkin)
		
f=12
g=10
move_to(0,0)
while True:
	if can_harvest():
		harvest()
	else:
		for i in range(f):
			for j in range(f):	
				if ((i<j) and (i<g) and (j<g)):
					move_to(i,j)
					if get_ground_type()!=Grounds.Soil:
						till()
					else:
						if can_harvest():
							use_item(Items.Weird_Substance)
							harvest()
							need_water()
							plant(Entities.Pumpkin)
							use_item(Items.Fertilizer)
							check_pumpkin()
						else:
							need_water()
							plant(Entities.Pumpkin)
							check_pumpkin()
							
							
							
				elif ((i==j) and (i<g) and (j<g)):
					move_to(i,j)
					if can_harvest():
						harvest()
						need_water()
						plant(Entities.Tree)
					else:
						need_water()
						plant(Entities.Tree)
				elif ((i>j) and (i<g) and (j<g)):
					move_to(i,j)
					if get_ground_type()!=Grounds.Soil:
						till()
						harvest()
						need_water()
						plant(Entities.Carrot)
					else:
						if can_harvest():
							harvest()
							need_water()
							plant(Entities.Carrot)
						else:
							need_water()
							plant(Entities.Carrot)
				else:
					move_to(i,j)
					if can_harvest():
						harvest()
						need_water()
						plant(Entities.Grass)
				
