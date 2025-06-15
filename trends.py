import pandas as pd                        
from pytrends.request import TrendReq

pytrend = TrendReq()
# df = pytrend.trending_searches(pn='india')
# df.head()
# print(df)

# pytrend.build_payload(kw_list=['Technology'])
# # Related Queries, returns a dictionary of dataframes
# related_queries = pytrend.related_queries()

# print(related_queries.values())


# p = pytrend.realtime_trending_searches(pn='US') # realtime search trends for United States
# print(p)

p = pytrend.realtime_trending_searches(pn='IN', cat="785") # India
print(p)