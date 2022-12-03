from countries import COUNTRIES
from pprint import pprint

ans = []

for i in COUNTRIES:
    ans.append((i.lower(), i))
    
pprint(ans)