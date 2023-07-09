#!/usr/bin/env python3

import argparse
import json
import logging

import praw

APP_NAME = "reddit_mail_alerter"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        default="config.json",
        help="Path to config file - defaults to ./config.json",
    )
    parser.add_argument(
        "--avoid-marking-read",
        action="store_true",
        help="If set, do not mark messages as read after alerting on them"
    )
    args = parser.parse_args()

    with open(args.config, "r") as f:
        config = json.load(f)

    # logging setup
    logger = logging.getLogger(APP_NAME)
    logging_conf = config.get("logging", dict())
    logger.setLevel(logging_conf.get("log_level", logging.INFO))
    if "gotify" in logging_conf:
        from gotify_handler import GotifyHandler

        logger.addHandler(GotifyHandler(**logging_conf["gotify"]))

    reddit_auth_info = config.get("auth_info", dict())
    if "user_agent" not in reddit_auth_info:
        reddit_auth_info["user_agent"] = APP_NAME

    try:
        # authenticate to reddit
        reddit = praw.Reddit(**reddit_auth_info)

        for message in reddit.inbox.unread():
            in_reply_to = (
                f'In reply to "{message.parent.subject}"\n' if message.parent else ""
            )
            msg = f"Sender: {message.author.name}\nSubject: {message.subject}\n{in_reply_to}\n{message.body}"
            logger.info(msg)

            if not args.avoid_marking_read:
                message.mark_read()

    except BaseException as be:
        logger.error(f"{type(be).__module__}.{type(be).__name__} - {be}")


if __name__ == "__main__":
    main()
