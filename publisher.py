#!/usr/bin/env python

#
# TECH TALK - Dolphin Maio/2020
#
# Projeto para demonstracao das funcionalidade do PUBSUB
# Autor : Claudio Lisboa
#
# Referencias: https://cloud.google.com/pubsub/docs
#
#

# Import bibliotecas PYTHON
import argparse
import time

# [Bibilioteca Principal Cloud Pub/Sub]
from google.cloud import pubsub_v1

def get_callback(api_future, data, ref):
    """Wrap message data in the context of the callback function."""

    def callback(api_future):
        try:
            print(
                "Published message {} now has message ID {}".format(
                    data, api_future.result()
                )
            )
            ref["num_messages"] += 1
        except Exception:
            print(
                "A problem occurred when publishing {}: {}\n".format(
                    data, api_future.exception()
                )
            )
            raise
    return callback


def pub(project_id, topic_name):
    """Publishes a message to a Pub/Sub topic."""
    # [START pubsub_quickstart_pub_client]
    # Initialize a Publisher client.
    client = pubsub_v1.PublisherClient()
    # [END pubsub_quickstart_pub_client]
    # Create a fully qualified identifier in the form of
    # `projects/{project_id}/topics/{topic_name}`
    topic_path = client.topic_path(project_id, topic_name)

    for n in range(1, 10):
        # Data sent to Cloud Pub/Sub must be a bytestring.
        data = u"Message number {}".format(n)
        # Data must be a bytestring
        data = data.encode("utf-8")

        # Keep track of the number of published messages.
        ref = dict({"num_messages": 0})

        # When you publish a message, the client returns a future.
        api_future = client.publish(topic_path, data=data)
        api_future.add_done_callback(get_callback(api_future, data, ref))

        # Keep the main thread from exiting while the message future
        # gets resolved in the background.
        while api_future.running():
            time.sleep(0.5)
            print("Published {} message(s).".format(ref["num_messages"]))



# TODO project_id = "Your Google Cloud Project ID"
# TODO topic_name = "Your Pub/Sub topic name"
# project_id = "projeto-pubsub"
# topic_name = "my-topic"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("project_id", help="Google Cloud project ID")
    parser.add_argument("topic_name", help="Pub/Sub topic name")

    args = parser.parse_args()

    pub(args.project_id, args.topic_name)
# [END pubsub_quickstart_pub_all]
