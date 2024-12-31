# log_system.py
from datetime import datetime

class LogSystem:
    def __init__(self, env):
        self.env = env
        self.logs = []

    def log_action_with_time(self, session_id, action_type, referer=None):
        # print("log_action_with_time called")  # Debug print
        # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"Session ID: {session_id} | Action: {action_type} | Time: {self.env.now}"
        if referer:
            log_entry += f" | Referer: {referer}"
        # self.logs.append(log_entry)
        print(log_entry)  
