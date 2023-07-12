class FundingRound:
    all = []

    def __init__(self, startup, venture_capitalist, type, investment):
        self.startup = startup
        self.venture_capitalist = venture_capitalist
        self.type = type
        self.investment = investment
        FundingRound.all.append(self)

    def get_startup(self):
        return self._startup

    def set_startup(self, new_startup):
        from .startup import Startup
        if isinstance(new_startup, Startup):
            self._startup = new_startup
        elif hasattr(self, '_startup'):
            raise Exception("Startup cannot be changed")
        else:
            raise Exception("Must include startup instance")
    
    startup = property(get_startup, set_startup)

    def get_venture_capitalist(self):
        return self._venture_capitalist
    
    def set_venture_capitalist(self, new_venture_capitalist):
        from .venture_capitalist import VentureCapitalist
        if isinstance(new_venture_capitalist, VentureCapitalist):
            self._venture_capitalist = new_venture_capitalist
        elif hasattr(self, '_venture_capitalist'):
            raise Exception("VC cannot be changed")
        else:
            raise Exception("Must include VC instance")

    venture_capitalist = property(get_venture_capitalist, set_venture_capitalist)

    def get_type(self):
        return self._type
    
    def set_type(self, new_type):
        if type(new_type) == str:
            self._type = new_type
        else:
            raise Exception("Type must be a string")

    type = property(get_type, set_type)

    def get_investment(self):
        return self._investment
    
    def set_investment(self, new_investment):
        if type(new_investment) == float and new_investment >= 0:
            self._investment = new_investment
        else:
            raise Exception("Should be a float that is not a negative number")

    investment = property(get_investment, set_investment)