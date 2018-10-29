class Neuron:
	“““The class to define a given neuron in the neural network.”””
	def __init__(self, sensitivity, releaseFactor, uptakeFactor, excitatory, connections_out, connections_in):
		self.synapses_out = {}
		self.synapses_in = {}
		self.excitatory = excitatory
		self.sensitivity = sensitivity
		for connection in connections_out:
			self.synapses_out[connection] = releaseFactor[connection]
		for connection in connections_in:
			self.synapses_in[connection] = uptakeFactor[connection]
	
	def respond():
		response = 0.0
		# compute the response as a sum of the product of the normalized sum of release and uptake factors and the sensitivity of the connection 
		for connection in connections_in:
			response = response + (self.sensitivity * (self.synapses_in[connection] + connection.synapses_out[self]) * 0.5)
		
		if response >= sensitivity && excitatory:
			return true
		elif response < sensitivity && excitatory:
			return false
		elif response >= sensitivity && !excitatory:
			return false
		else
			return true
	
	def fire():
		