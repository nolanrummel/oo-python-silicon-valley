from .funding_round import FundingRound

class VentureCapitalist:
    all = []

    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

    def get_name(self):
        return self._name
   
    def set_name(self, new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            raise Exception("Name must be a string")
    
    name = property(get_name, set_name)

    def get_total_worth(self):
        return self._total_worth
    
    def set_total_worth(self, new_total_worth):
        if type(new_total_worth) == int:
            self._total_worth = new_total_worth
        else:
            raise Exception("Not an integer")
        
    total_worth = property(get_total_worth, set_total_worth)
        
    @classmethod
    def tres_commas_club(cls):
        return [investor for investor in VentureCapitalist.all if investor.total_worth > 1000000000]

    def offer_contract(self, startup, type, investment):
        FundingRound(startup, self, type, investment)

    def funding_rounds(self):
      return [funding for funding in FundingRound.all if funding.venture_capitalist == self]
    
    def portfolio(self):
      return list({funding.startup for funding in self.funding_rounds()})
    
    def biggest_investment(self):
        return sorted(self.funding_rounds(), key=lambda round: round.investment, reverse=True)[0]
    
    def invested(self, domain):
        return sum([funding.investment for funding in self.funding_rounds() if funding.startup.domain == domain])

    
    # def __repr__(self):
    #     return 'name:' +

    # bigger_round = lambda round1, round2: round1.investment > round2.investment
    #     bigger_round(round1, round2)