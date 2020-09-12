# Buzzkoning
_A Discord bot for time-synced / standardized Online Quizbowl buzzing._

This is the official Arizona Quizbowl and ASU Sun Devil Quizbowl buzzer bot for Discord, written in Python.
**Bot token blocked for privacy.**

If you'd like to make use of this or have any questions, send me an [email](mailto:hlakamsani.gmail.com) or leave an [issue](https://github.com/hlakams/buzzkoning/issues).

Here's a command guide for proper usage:
- ```/buzz``` sends a message in format (currently hardcoded to America/Phoenix timezone via pytz):
```
"@[user nickname] buzzed at 10-Aug-2020 (01:29:43.179615)"
```
- ```/[number]C``` initializes a text channel for a round of questions (reset on call) with this output:
```
"*Round for Room #[number] has been Reset*"
```
- ```/[number]``` increments the question number (```[countNumber]```) and prints an output to this format:
```
Room [number]
----------
Question [countNumber]
----------
```

Update/Version log:
- Version 08/10/2020: initial working model, with sole ```/buzz``` command
- Version 09/10/2020: added commands ```/[number]``` and ```[number]C``` for round maintenance
