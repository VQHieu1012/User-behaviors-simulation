# main.py
from simulation import Simulation
from constants import NUM_USERS, DURATION

if __name__ == "__main__":
    simulation = Simulation(num_users=NUM_USERS, duration=DURATION)
    simulation.run()
