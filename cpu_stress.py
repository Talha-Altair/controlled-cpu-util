from cpu_load_generator import load_all_cores

def stress(load=0.2):

    load_all_cores(target_load=load) # generates load on all cores