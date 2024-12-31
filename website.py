# website.py
import uuid
from user_behavior import User
from constants import REFERERS
import random

class Website:
    """Initialize website"""
    
    def __init__(self, env, num_users, log_system):
        self.env = env
        self.num_users = num_users
        self.log_system = log_system

    def generate_user(self):
        """Create users and start the simulation"""
        while True:
            for _ in range(self.num_users):
                session_id = str(uuid.uuid4())
                referer = random.choice(REFERERS)
                user = User(session_id, referer, self.log_system)
                user.simulate_actions()
            print(f"DAY: {self.env.now}")
            yield self.env.timeout(1)