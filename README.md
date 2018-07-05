# Mohican Yak

An automated test for the [NeXus File Writer](https://github.com/ess-dmsc/kafka-to-nexus).

The tests are scripted in Python using PyTest. A PyTest [test fixture](https://docs.pytest.org/en/latest/fixture.html) is responsible for launching the containerised software using docker-compose. All required components of the system are launched in this way, such that the only required step to run the tests is to launch PyTest.

The [start command](https://github.com/ess-dmsc/mohican-yak/blob/master/commands/example-json-command.json) for initiating file writing, which contains the NeXus file structure definition was created by preparing a sample file using [python-nexus-utilities](https://github.com/ess-dmsc/python-nexus-utilities) and generating json based on that file using [nexus-json](https://github.com/ess-dmsc/nexus-json).

The File Writer is provided with streams of fake neutron data events and sample environment log data by the [NeXus-Streamer](https://github.com/ess-dmsc/NeXus-Streamer) and the [Forwarder](https://github.com/ess-dmsc/forward-epics-to-kafka) respectively. 

## To run

Docker, Python 3 and PyPi are required. The required python packages can be installed with
```
pip install -r requirements.txt
```

Then simply run `pytest` and look in `output-files` for the file output by the writer. Note that the first time this is run may take a few minutes as Docker will need to download several images. 
