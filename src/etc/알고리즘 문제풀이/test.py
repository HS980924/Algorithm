from datetime import datetime
from time import time

N = datetime.strptime('07:59',"%H:%M")
S = datetime.strptime('17:09',"%H:%M");

result = abs(N - S)

print(result.hour)

print(result)