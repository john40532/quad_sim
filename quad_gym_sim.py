from quad_gym import World

env = World()

for loop in xrange(1,10):
	env.reset()
	for i in range(10):
		env.render()	#this takes lots of time
		for a in range(200):
			env.step([4,4,4,4])	#Unit: Newton