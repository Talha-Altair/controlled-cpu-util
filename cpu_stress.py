from cpu_load_generator import load_all_cores

def stress(load=10):

    load_all_cores(duration_s = 45,target_load=load) # generates load on all cores

if __name__ == '__main__':

    stress()