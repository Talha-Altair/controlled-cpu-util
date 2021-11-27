from cpu_load_generator import load_all_cores

def stress(duration = 420, load = 10):

    load_all_cores(duration_s = duration, target_load = load)

if __name__ == '__main__':

    stress()