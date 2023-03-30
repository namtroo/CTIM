**C**omputer **T**emperature **I**nformation **M**anagement **S**ystem

## Features

- [ ] Live update web interface (headless vs web mode)
- [ ] Support Windows, Linux, MacOS
- [ ] Text file config
- [ ] SQLite3 history
- [ ] Report export (csv, html, image, pdf)
- [ ] Support remote node management
- [ ] Support Telegram notification

## How to run

You can use the default `config.ini` to run this software or change as need.

`[mode]`:
- `run` is equal to `web` for web client, `headless` for headless client, or `desktop` for desktop client. If this is not specified, `run = web` by default.
- `role` is equal to `branch` for branches, `head` to manage other branches. Section `[node_X]` (described below) works only with `head` role. Section `[api]` (described below) works only with `branch` role.
- `interval` is a positive integer for number of seconds between two consecutive update of data. By default, `interval = 5`. Smallest possible value of `interval` is 1.

`[spec]`:
- `cpu` is enabled for monitor or not. By default, the value is True.
- `gpu` is enabled for monitor or not. By default, the value is True.
- `hdd` is enabled for monitor or not. By default, the value is True.

`[sqlite]`:
- `path` is equal to the path you want to store the history database

`[telegram]`: (optional)
- `token` is equal to the token of your Telegram bot.
- `chat_id` is equal to the group chat ID you specified for your own bot.

`[api]`: (optional, for clusters' usage)
- `api_key` is equal to the key to call from 

`[node_X]`: (optional, for manager to manage data from multiple nodes)
- `node_ip` is equal to target IP of the node
- `node_port` is equal to target open port of the node
- `node_key` is equal to `api_key` of the node

## FAQ

1. Error on Windows

## Contributors

- Nguyen Viet Hoang (BI11-099)
- Chu Van Nam (BA11-076)
- Nguyen Quang Vinh (BA11-103)
- Dang Duc Anh (BA11-002)
- Pham Truong Son (BA11-086)