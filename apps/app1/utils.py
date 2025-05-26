import time

def compute_timer(initial, final):
	start_time = time.time()

	for i in range(initial, final + 1):
		pass

	end_time = time.time()

	computation_time = end_time - start_time
	timer_dict = {'time': computation_time}
	return timer_dict
