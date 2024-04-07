# ChainBot
basic fishing bot for doodle world
## Usage
1. download all dependancies (listed in `setup.py`)
2. customize `config.toml` based on your setup
3. setup images
    1. add screenshots of the ui elements present in `/images`. make sure the screenshots are taken in the same configuration you'll be running the game in, since the image recognition works through comparing pixels directly
    2. add a small screenshot of the doodle you're trying to chain to `/images/target` following the same rules as above
5. setup your .env file with the two fields `DISCORD_TOKEN` and `CHANNEL_ID`
6. run `chainbot.py`
