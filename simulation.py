# simulation.py
import simpy
from website import Website
from log_system import LogSystem
from constants import NUM_USERS, DURATION

class Simulation:
    """User behavior simulation"""
    
    def __init__(self, num_users=NUM_USERS, duration=DURATION):
        self.num_users = num_users
        self.duration = duration
        self.env = simpy.Environment()
        self.log_system = LogSystem(self.env)
        self.website = Website(self.env, self.num_users, self.log_system)

    def run(self):
        """Run simulation"""
        self.env.process(self.website.generate_user())
        self.env.run(until=self.duration)
        # logging
        print(f"Simulation completed for {self.num_users} users over {self.duration} time units.")
