**C**omputer **T**emperature **I**nformation **M**anagement **S**ystem

## Features

- [x] Live update web interface (headless vs web mode)
- [x] Support Windows, Linux
- [x] Text file config
- [x] SQLite3 history
- [ ] Report export (csv)
- [x] Remote nodes management

## How to install

Run `pip install -r requirements.txt` inside the repo folder with your own proper virtual environment before running the application.

## How to run

You can use the default `config.ini` to run this software or change as need.

`[mode]`:
- `run` is equal to `web` for web client, `headless` for headless client, or `desktop` for desktop client. If this is not specified, `run = web` by default.
- `port` is equal to `port` for API that can be accessed inside network.
- `interval` is a positive integer for number of seconds between two consecutive update of data. By default, `interval = 5`. Smallest possible value of `interval` is 1.

`[sqlite]`: (optional, for branches' usage)
- `path` is equal to the path you want to store the history database
- `history` is number of line kept in history database before the oldest line get removed. By default, the history is set to 500. If you keep multiple branches in config, the history will store sensors' results from all configured branches.

`[branch_X]`: (must have at least 1, to manage data from other branch)
- `branch_name` is the name you assign for the branch.
- `branch_ip` is equal to target IP of the branch.
- `branch_port` is equal to target open port of the branch.
- `branch_key` is equal to `api_key` of the branch.

## Contributors

- Nguyen Viet Hoang (BI11-099)
- Chu Van Nam (BA11-076)
- Nguyen Quang Vinh (BA11-103)
- Dang Duc Anh (BA11-002)
- Pham Truong Son (BA11-086)