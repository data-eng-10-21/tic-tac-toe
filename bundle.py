class Bundle():
    def __init__(self, weight = None):
        self.weight = None

    def price(self):
        if not self.__dict__.get('weight'):
            return 'must provide a weight'
        if self.weight < 5:
            return 10
        else:
            return 12

