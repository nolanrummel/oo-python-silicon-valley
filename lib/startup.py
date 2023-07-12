from .funding_round import FundingRound

class Startup:
   all = []

   def __init__(self, name, founder, domain):
      self.name = name
      self.founder = founder
      self.domain = domain
      Startup.all.append(self)

   def get_name(self):
      return self._name
   
   def set_name(self, new_name):
      if type(new_name) == str:
         self._name = new_name
      else:
         raise Exception("Name must be a string")
      
   name = property(get_name, set_name)

   def get_founder(self):
      return self._founder
   
   def set_founder(self, new_founder):
      if hasattr(self, "_founder"):
         raise Exception("Name cannot be changed")
      elif type(new_founder) == str:
         self._founder = new_founder
      else:
         raise Exception("Name must be a string")
      
   founder = property(get_founder, set_founder)

   def get_domain(self):
      return self._domain
   
   def set_domain(self, new_domain):
      if hasattr(self, "_domain"):
         raise Exception("Name cannot be changed")
      elif type(new_domain) == str:
         self._domain = new_domain
      else:
         raise Exception("Name must be a string")
      
   domain = property(get_domain, set_domain)

   def pivot(self, new_name, new_domain):
      if not hasattr(self, "_domain") and hasattr(self, "_name") and type(new_name) == str and type(new_domain) == str:
         raise Exception("Must enter both domain and name to change")
      else:
         self._name = new_name
         self._domain = new_domain

   @classmethod
   def find_by_founder(cls, new_founder):
      import ipdb; ipdb.set_trace()
      return [startup for startup in Startup.all if startup.founder == new_founder][0]
   
   @classmethod
   def domains(cls):
      return [startup.domain for startup in Startup.all]
   
   def sign_contract(self, venture_capitalist, type, investment):
      FundingRound(self, venture_capitalist, type, investment)

   def num_funding_rounds(self):
      return len([funding for funding in FundingRound.all if funding.startup == self])
   
   def total_funds(self):
      return sum([funding.investment for funding in FundingRound.all if funding.investment == self])

   def investors(self):
      return list({funding.venture_capitalist for funding in FundingRound.all if funding.startup == self})
   
   def big_investors(self):
      from .venture_capitalist import VentureCapitalist
      return [investors for investors in self.investors() if investors in VentureCapitalist.tres_commas_club()]