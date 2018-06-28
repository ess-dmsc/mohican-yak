# Urban Broccoli

Integration test for the [Event-Formation-Unit](https://github.com/ess-dmsc/event-formation-unit), [EPICS Forwarder](https://github.com/ess-dmsc/forward-epics-to-kafka) and [NeXus File Writer](https://github.com/ess-dmsc/kafka-to-nexus).

Software is launched in Docker containers using docker-compose. The tests are scripted in Python using PyTest, with a [test fixture](https://docs.pytest.org/en/latest/fixture.html) responsible for launching the containerised software using docker-compose. All required components of the system are launched in this way, therefore running the tests

[Architecture diagram]
