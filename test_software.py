from helpers.kafkahelpers import create_producer
from time import sleep


def send_writer_command(filepath, producer):
    with open(filepath, "r") as cmd_file:
        data = cmd_file.read().replace('\n', '')
    producer.produce("TEST_writerCommand", data)


def test_data_reaches_file(test_environment):
    producer = create_producer()

    sleep(20)

    # Start file writing
    send_writer_command("commands/example-json-command.json", producer)
    producer.flush()

    sleep(20)

    # Stop file writing
    send_writer_command("commands/stop-command.json", producer)
    send_writer_command("commands/writer-exit.json", producer)
    producer.flush()

    sleep(10)
