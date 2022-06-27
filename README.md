# stevan-bot
click [here](https://top.gg/bot/980883944729890847) to add Stevan to your discord server.

### what is this?
Stevan is a mental health discord bot built in Python with [Nextcord](https://github.com/nextcord/nextcord) and hosted on [Heroku](https://www.heroku.com).

This is a new and improved version of [carebot](https://github.com/prach19/carebot)! 

Stevan's functions include: 
  * setting reminders (for yourself, everyone in the server, and a specific user)
  * giving random journal prompts, written and art (from my own list of prompts)
  * giving breathing exercises to calm down (a list of gifs found on the internet)
  * giving a random activity to do if you're bored (using [Bored API](http://www.boredapi.com/))
  * giving a Bob Ross quote (using [Bob Ross API](https://api.bobross.dev/))

### what's in this repo?
* `Procfile`, `runtime.txt`, `requirements.txt` are files required by Heroku
* `app.py` is the main code, includes all the comands
* `journal.json` and `gifs.json` are the lists of links/prompts used by the respective commands
