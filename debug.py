from lib import *

# code here
# e.g.
# Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
#   vc1 = VentureCapitalist( 'Peter Gregory', 100000000 )
#   fr1 = FundingRound( s1, vc1, 'Pre-Seed', 200000.99 )




st1 = Startup('flatiron' , 'adam', 'flatiron.com')
st2 = Startup('raver, inc' , 'adam', 'burningman.com')
st3 = Startup('potatoes' , 'emiley', 'idaho.com')

vc1 = VentureCapitalist('sadaf', 1000000000000)
vc2 = VentureCapitalist('nolan', 30)
vc3 = VentureCapitalist('frankie', 1000000000)

fr1 = FundingRound(st1, vc1, 'Pre-Seed', 5000000.50)
fr4 = FundingRound(st1, vc1, 'Pre-Seed', 10000000.50)
fr2 = FundingRound(st1, vc2, 'Series A', 3.50)
fr3 = FundingRound(st2, vc1, 'Angel', 99999999.99)

# Startup.find_by_founder('adam')

# st1.pivot('table 5 academy', 'crazyaboutcars.com')

# do not remove
import ipdb; ipdb.set_trace()
