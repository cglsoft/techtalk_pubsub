#!/usr/bin/env python

#
# TECH TALK - Dolphin Maio/2020
#
# Projeto para demonstracao das funcionalidade do PUBSUB
# Autor : Claudio Lisboa
#
# Referencias: https://cloud.google.com/pubsub/docs

import time

# [START pubsub_quickstart_sub_all]
import argparse

# [START pubsub_quickstart_sub_deps]
from google.cloud import pubsub_v1

# [END pubsub_quickstart_sub_deps]

# TODO project_id = "Your Google Cloud Project ID"
# TODO subscription_name = "Your Pub/Sub subscription name"

# def callback(message):
#     print("Received message: {}".format(message))
#     message.ack()
#
# subscriber.subscribe(subscription_path, callback=callback)
# # The subscriber is non-blocking. We must keep the main thread from
# # exiting to allow it to process messages asynchronously in the background.
# print("Listening for messages on {}".format(subscription_path))
# while True:
#     time.sleep(60)


def sub(project_id, subscription_name):
    """Receives messages from a Pub/Sub subscription."""
    # [START pubsub_quickstart_sub_client]
    # Initialize a Subscriber client
    subscriber_client = pubsub_v1.SubscriberClient()
    # [END pubsub_quickstart_sub_client]
    # Create a fully qualified identifier in the form of
    # `projects/{project_id}/subscriptions/{subscription_name}`
    subscription_path = subscriber_client.subscription_path(
        project_id, subscription_name
    )

    def callback(message):
        print(
            "Received message {} of message ID {}\n".format(
                message, message.message_id
            )
        )
        # Acknowledge the message. Unack'ed messages will be redelivered.
        message.ack()
        print("Acknowledged message {}\n".format(message.message_id))

    streaming_pull_future = subscriber_client.subscribe(
        subscription_path, callback=callback
    )
    print("Listening for messages on {}..\n".format(subscription_path))
    while True:
        time.sleep(60)

    try:
        # Calling result() on StreamingPullFuture keeps the main thread from
        # exiting while messages get processed in the callbacks.
        streaming_pull_future.result()
    except:  # noqa
        streaming_pull_future.cancel()

    subscriber_client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("project_id", help="Google Cloud project ID")
    parser.add_argument("subscription_name", help="Pub/Sub subscription name")

    args = parser.parse_args()

    sub(args.project_id, args.subscription_name)
# [END pubsub_quickstart_sub_all]
