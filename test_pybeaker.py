import pybreaker

breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=10)

@breaker
def unreliable_service():
    import random
    if random.random() < 0.7:
        raise Exception("Service failed!")
    return "Success!"

for _ in range(10):
    try:
        print("successs", unreliable_service())
    except pybreaker.CircuitBreakerError:
        print(" Circuit is OPEN")
    except Exception as e:
        print("failure", e)