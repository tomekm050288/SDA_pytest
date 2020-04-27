class Server:

    def validate_card(self, arg):
        pass


class Card:

    def __init__(self, account, pin):
        self.account = account
        self.validation = Server().validate_card(pin)
        if self.validation:
            self.pin = pin

    @property
    def card_owner(self):
        return self.account.owner

    def get_account(self):
        return str(self.account)

    def is_pin_number(self):
        try:
            int(self.pin)
            return True
        except ValueError:
            return "Validation error"
