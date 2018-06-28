# Urban Broccoli

Integration test for the [Event-Formation-Unit](https://github.com/ess-dmsc/event-formation-unit), [EPICS Forwarder](https://github.com/ess-dmsc/forward-epics-to-kafka) and [NeXus File Writer](https://github.com/ess-dmsc/kafka-to-nexus).

The tests are scripted in Python using PyTest. A PyTest [test fixture](https://docs.pytest.org/en/latest/fixture.html) is responsible for launching the containerised software using docker-compose. All required components of the system are launched in this way, such that the only required step in running the tests is to launch PyTest.

[Architecture diagram]
