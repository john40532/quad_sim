import quadcopter,gui,controller,math
import numpy as np

class World(object):
	"""docstring for World"""
	def __init__(self):
		# Set goals to go to
		GOALS = [(1,1,2)]
		YAWS = [0]
		self.STEPSIZE = 0.002
		# Define the quadcopters
		QUADCOPTER={'q1':{'position':[1,0,4],'orientation':[0,0,0],'L':0.3,'r':0.1,'prop_size':[10,4.5],'weight':1.2}}
		# Controller parameters
		CONTROLLER_PARAMETERS = {'Motor_limits':[4000,9000],
		                'Tilt_limits':[-10,10],
		                'Yaw_Control_Limits':[-900,900],
		                'Z_XY_offset':500,
		                'Linear_PID':{'P':[300,300,7000],'I':[0.04,0.04,4.5],'D':[450,450,5000]},
		                'Linear_To_Angular_Scaler':[1,1,0],
		                'Yaw_Rate_Scaler':0.18,
		                'Angular_PID':{'P':[22000,22000,1500],'I':[0,0,1.2],'D':[12000,12000,0]},
		                }

		self.quad = quadcopter.Quadcopter(QUADCOPTER)
		self.gui_object = gui.GUI(quads=QUADCOPTER)
		self.random_seed = None

	def reset(self):
		if self.random_seed != None:
			if self.random_seed != 0:
				random.seed(self.random_seed)
			x = random.uniform(-1,1)
			y = random.uniform(-1,1)
			z = random.uniform(4,6)
			theta = random.uniform(-0.5*math.pi,0.5*math.pi)
			phi = random.uniform(-0.5*math.pi,0.5*math.pi)
			gamma = random.uniform(-0.5*math.pi,0.5*math.pi)
			x_dot = random.uniform(-1,1)
			y_dot = random.uniform(-1,1)
			z_dot = random.uniform(-1,1)
			theta_dot = random.uniform(-1,1)
			phi_dot = random.uniform(-1,1)
			gamma_dot = random.uniform(-1,1)

		else:
			x = 0
			y = 0
			z = 5
			x_dot = 0
			y_dot = 0
			z_dot = 0
			theta = 0
			phi = 0
			gamma = 0
			theta_dot = 0
			phi_dot = 0
			gamma_dot = 0

		return self.quad.set_state('q1',[x,y,z,x_dot,y_dot,z_dot,theta,phi,gamma,theta_dot,phi_dot,gamma_dot])

	def step(self,action):
		action = np.clip(action,0,6)
		# print action
		self.quad.set_motor_force('q1',action)
		self.quad.update(self.STEPSIZE)
		return self.quad.get_state('q1')

	def render(self):
		self.gui_object.quads['q1']['position'] = self.quad.get_position('q1')
		self.gui_object.quads['q1']['orientation'] = self.quad.get_orientation('q1')
		self.gui_object.update()
		