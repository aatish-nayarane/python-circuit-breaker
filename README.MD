# Python Circuit Breaker Pattern

A Python project demonstrating the **Circuit Breaker design pattern** for handling failures in distributed systems and preventing repeated calls to an unhealthy service.

The Circuit Breaker pattern helps improve system reliability by temporarily stopping requests to a failing dependency and allowing the dependency time to recover.

## Project Structure

```text
.
├── cb_topology.py
├── example_cb.py
├── test_pybeaker.py
├── __init__.py
└── README.md
```

## Circuit Breaker Pattern

The Circuit Breaker pattern protects an application from continuously calling a service that is failing or unavailable.

Instead of allowing every request to reach the failing service, the circuit breaker monitors failures and changes its state.

### Circuit Breaker States

The circuit breaker generally has three states:

```text
              Successful requests
           +-------------------------+
           |                         |
           v                         |
      +---------+                +---------+
      |  CLOSED |                |  OPEN   |
      +---------+                +---------+
           |                         |
           | Failure threshold       |
           | reached                 |
           +------------------------>|
                                     |
                                     | Timeout
                                     v
                                +------------+
                                | HALF-OPEN  |
                                +------------+
                                     |
                         +-----------+-----------+
                         |                       |
                    Successful               Failure
                         |                       |
                         v                       v
                     CLOSED                    OPEN
```

### CLOSED

The circuit is operating normally.

Requests are allowed to reach the downstream service.

```text
Application
     |
     v
Circuit Breaker
     |
     v
Service
```

If failures remain below the configured threshold, the circuit stays closed.

### OPEN

When failures exceed the configured threshold, the circuit opens.

Requests are no longer sent to the failing service.

```text
Application
     |
     v
Circuit Breaker
     |
     X
  Request blocked
```

This prevents unnecessary load on the unhealthy dependency.

### HALF-OPEN

After a configured recovery period, the circuit breaker allows a limited request to test whether the service has recovered.

```text
Circuit Breaker
      |
      v
   Test Request
      |
   +--+--+
   |     |
Success Failure
   |     |
   v     v
CLOSED  OPEN
```

## Why Use a Circuit Breaker?

Without a circuit breaker, an application may continuously retry an unavailable dependency.

This can result in:

- Increased latency
- Thread or worker exhaustion
- Connection exhaustion
- Increased load on the failing service
- Cascading failures
- Poor application availability

A circuit breaker limits these effects by failing fast when a dependency is unhealthy.

## Example Flow

Consider an application calling an external service:

```text
Application
     |
     v
Circuit Breaker
     |
     v
External Service
```

If the service starts failing:

```text
Request 1  -> Failure
Request 2  -> Failure
Request 3  -> Failure
Request 4  -> Failure
                |
                v
        Failure threshold
                |
                v
             OPEN
```

Further requests are rejected immediately until the recovery timeout expires.

## Project Files

### `cb_topology.py`

Contains the circuit breaker topology/state-related implementation.

It demonstrates how the circuit breaker manages the flow between the application and the dependent service.

### `example_cb.py`

Contains example usage of the circuit breaker implementation.

It can be used to understand how requests, failures, and state transitions are handled.

### `test_pybeaker.py`

Contains tests for the circuit breaker implementation.

Run the tests with:

```bash
python -m pytest
```

## Key Concepts

This project demonstrates:

- Circuit Breaker pattern
- Failure detection
- Failure thresholds
- Fail-fast behavior
- Circuit states
- Recovery timeout
- Half-open state
- Dependency protection
- Fault tolerance
- Resilience in distributed systems

## Benefits

The Circuit Breaker pattern provides several benefits:

### Fail Fast

When a dependency is unavailable, requests can fail immediately instead of waiting for timeouts.

### Prevent Cascading Failures

A failing dependency is isolated from the rest of the application.

### Reduce Load

Repeated requests are stopped while the dependency is unhealthy.

### Automatic Recovery

The half-open state allows the system to automatically check whether the dependency has recovered.

## Running the Project

Clone the repository:

```bash
git clone <repository-url>
cd python-circuit-breaker
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Run the example:

```bash
python example_cb.py
```

Run tests:

```bash
python -m pytest
```

## Learning Goals

The main goal of this project is to understand how the Circuit Breaker pattern can be implemented and used to build more resilient applications.

Key learning areas:

1. Circuit Breaker design pattern
2. Failure detection
3. State transitions
4. Fail-fast mechanisms
5. Service recovery
6. Fault tolerance
7. Distributed system resilience
8. Testing failure scenarios

## Possible Improvements

Future improvements could include:

- Configurable failure thresholds
- Configurable recovery timeout
- Retry with exponential backoff
- Metrics and monitoring
- Logging
- Async support
- Thread-safe implementation
- Integration with REST APIs
- Integration with message queues
- Prometheus metrics

## License

This project is licensed under the terms specified in the `LICENSE` file.