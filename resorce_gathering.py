pet_the_piggy()
while True:
	if can_harvest():
		harvest()
	if get_ground_type()!=Grounds.Grassland:
		till()
	elif get_ground_type()==Grounds.Soil:
		if can_harvest():
			harvest()
			plant(Entities.Pumpkin)
			move(East)
		else:
			plant(Entities.Pumpkin)
			move(East)
	else:
		plant(Entities.Bush)
		move(North)
		if can_harvest():
			harvest()
		else:
			move(East)
			till()
			plant(Entities.Carrot)
			move(North)
			plant(Entities.Tree)
			move(East)
			plant(Entities.Pumpkin)
			if can_harvest():
				harvest()
			else:
				do_a_flip()
				
