from helpers.kafkahelpers import create_producer
from time import sleep


def send_writer_command(filepath, producer):
    with open(filepath, "r") as cmd_file:
        data = cmd_file.read().replace('\n', '')
    producer.produce("TEST_writerCommand", data)


def test_data_reaches_file(test_environment):
    """
    This 'test' performs the job which NICOS will do in the production
    system at the ESS; sending the 'command' messages for the file writer.

    :param test_environment: This is the test fixture which launches the containers
    """
    producer = create_producer()
    sleep(10)

    # Start file writing
    send_writer_command("commands/example-json-command.json", producer)
    producer.flush()

    # Give it some time to accumulate data
    sleep(10)

    # Stop file writing
    send_writer_command("commands/stop-command.json", producer)
    sleep(1)
    send_writer_command("commands/writer-exit.json", producer)
    producer.flush()

    # Allow time for the file writing to complete
    sleep(5)
