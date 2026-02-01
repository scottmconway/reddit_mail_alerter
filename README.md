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

### 2026 Addendum
Reddit sucks. They have killed the above simple workflow. The Devvit app workflow does not create applications with the type `script`, so they cannot be used with this program.

To attempt to make a script app now, you have to beg for one to be created for you by filling out [this form](https://support.reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164&tf_14867328473236=api_request_type_research).

Then maybe if you're approved you can plug in your credentials and use this program as intended.

## Configuration Setup
See `config.json.example` for an example configuration file.

The `auth_info` section should contain a valid dictinary of arguments to provide to the `praw.Reddit` constructor, as detailed [here](https://praw.readthedocs.io/en/stable/getting_started/authentication.html).
If the `user_agent` attribute is not provided, it will be set to `"reddit_mail_alerter"`.

## Arguments
|Short Name|Long Name|Type|Description|
|-|-|-|-|
||`--config`|`str`|Path to config file - defaults to `./config.json`|
|N/A|`--avoid-marking-read`|`bool`|If set, do not mark messages as read after alerting on them|
