HR-Bot with Rasa NLU and Rasa Core

## Introduction

This version of the bot  supports:
- xy
- yz

## Installation + Running of the bot

To install the bot, please clone the repo and run:

```
pip install rasa_nlu
pip install rasa_nlu[tensorflow]
pip install rasa_core
```
This will install the bot and all of its requirements.

To train the core model: 

```
python3 bot.py train-dialogue
```

To train the NLU model: 

```
python3 bot.py train-nlu
```

To evaluate the NLU model: 

```
python3 -m rasa_nlu.evaluate --config config_tensorflow.yml --data data/nlu/nlu.json --mode crossvalidation
```

<!-- To run the bot with both these models:
```
python3 -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml
``` -->

To start interactive learning
```
cd custom_actions
```

```
python3 -m rasa_core_sdk.endpoint --actions actions
```

```
python3 -m rasa_core.train --interactive -u models/nlu/default/current/ -o models/dialogue -d domain.yml -s data/core/stories.md --endpoints endpoints.yml --skip_visualization

```

To run the bot on the website install rasa-addons:
```
pip install rasa-addons (currently not working with master branch)
```

Start the action webserver
```
cd custom_actions
```
```
python3 -m rasa_core_sdk.endpoint --actions actions
```

Serve the website containing the chat widget:
```
cd static
```
```
python3 -m http.server 5100
```

Launch the website backend:
```
python3 website.py
```

The website can be found on http://localhost:5100/index.html

## Overview of the files

`data/core/` - contains stories for Rasa Core

`data/nlu` - contains example NLU training data

`domain.yml` - the domain file for Core

`nlu_tensorflow.yml` - the NLU config file