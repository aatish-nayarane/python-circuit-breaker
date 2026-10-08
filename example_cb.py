import time
import random
from cb_topology import  CircuitBreaker

def unreliable_service():
    if random.random() < 0.7:
        raise Exception("Service failed!")
    return "Success!"

cb = CircuitBreaker(failure_threshold=3, recovery_timeout=10)

for i in range(10):
    try:
        result = cb.call(unreliable_service)
        print("success result", result)
    except Exception as e:
        print("failure result", e)
    
    time.sleep(1)