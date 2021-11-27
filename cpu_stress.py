import os

def stress():

    cmd = "stress --cpu 1 --timeout 10s"

    os.system(cmd)

    return 0

if __name__ == '__main__':

    stress()