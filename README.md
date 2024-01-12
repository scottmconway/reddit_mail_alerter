# Reddit Mail Alerter
A simple script to run as a cronjob to log unread reddit messages to any number of logging handlers

## Requirements
* python3
* see requirements.txt

## Quickstart
* Create a "script" application for Reddit's API [here](https://old.reddit.com/prefs/apps/)
* Enter your user and API credentials in `config.json`, using `config.json.example` as a template
* Configure logging as you wish
* Simply run `./reddit_mail_alerter.py`

## Configuration Setup
See `config.json.example` for an example configuration file.

The `auth_info` section should contain a valid dictinary of arguments to provide to the `praw.Reddit` constructor, as detailed [here](https://praw.readthedocs.io/en/stable/getting_started/authentication.html).
If the `user_agent` attribute is not provided, it will be set to `"reddit_mail_alerter"`.

## Arguments
|Short Name|Long Name|Type|Description|
|-|-|-|-|
||`--config`|`str`|Path to config file - defaults to `./config.json`|
|N/A|`--avoid-marking-read`|`bool`|If set, do not mark messages as read after alerting on them|
