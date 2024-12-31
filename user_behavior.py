from utils import rand_chance
from constants import P_CREATE_ACCOUNT, P_VIEW_PRODUCT, P_PURCHASE, P_ADD_TO_CART, P_REMOVE_FROM_CART, P_LOGIN, P_INTERACT_AD


class User:
    """
        Define user and behavior
        Modify this for more complex behaviors
    """
    
    def __init__(self, session_id, referer, log_system):
        self.session_id = session_id
        self.referer = referer
        self.log_system = log_system
        self.logged_in = False  # user logs in or not
        self.cart = []  # Initialize user's cart
    def simulate_actions(self):
        """
            Simulate behaviors
        """
        # Log web access
        self.log_system.log_action_with_time(self.session_id, "access", self.referer)

        # user logs in
        if rand_chance(P_LOGIN):
            self.log_system.log_action_with_time(self.session_id, "login")
            self.logged_in = True  # mark as logged

        # user creates account
        if not self.logged_in and rand_chance(P_CREATE_ACCOUNT):
            self.log_system.log_action_with_time(self.session_id, "create_account")

            # cart behavior
            if rand_chance(P_ADD_TO_CART):
                self.cart.append("product")  
                self.log_system.log_action_with_time(self.session_id, "add_to_cart")

            if rand_chance(P_REMOVE_FROM_CART):
                if self.cart:  # only can remove products if cart not null
                    self.cart.pop()
                    self.log_system.log_action_with_time(self.session_id, "remove_from_cart")

            # user purchases
            purchase_prob = P_PURCHASE * (1.5 if self.logged_in else 1)
            if rand_chance(purchase_prob):
                self.log_system.log_action_with_time(self.session_id, "purchase")

        # user interacts with ad
        if rand_chance(P_INTERACT_AD):
            self.log_system.log_action_with_time(self.session_id, "interact_ad")

        # view / buy products
        if rand_chance(P_VIEW_PRODUCT):
            self.log_system.log_action_with_time(self.session_id, "view_product")

            if rand_chance(P_PURCHASE):
                self.log_system.log_action_with_time(self.session_id, "purchase")

        # user leaves website
        self.log_system.log_action_with_time(self.session_id, "leave")