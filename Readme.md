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
python3 -m rasa_core.run -d models/dialogue -u models/nlu/current/ --endpoints config/endpoints.yml
``` -->

To start interactive learning
```
cd actions
```

```
python3 -m rasa_core_sdk.endpoint --actions actions
```

```
python3 -m rasa_core.train interactive -c config/policy_config.yml -u models/nlu/default/current/ -o models/dialogue -d domain.yml -s data/core/stories.md --endpoints config/endpoints_offline.yml
```

To run the bot on the website install rasa-addons:
```
pip install rasa-addons (currently not working with master branch)
```

Start the action webserver
```
cd actions
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

## Train with Docker on Windows

Train Core
```
docker run -v ${pwd}:/app/project -v ${pwd}/models/dialogue:/app/models rasa/rasa_core:latest train -c project/config/policy_config.yml --domain project/domain.yml --stories project/data/core/stories.md --out models

Train NLU
```
docker run -v ${pwd}:/app/project -v ${pwd}/models/nlu:/app/models -v ${pwd}/config:/app/config rasa/rasa_nlu:latest run python -m rasa_nlu.train -c config/config_tensorflow.yml -d project/data/nlu/nlu.json -o models --fixed_model_name current
```

## Deploy
- Train NLU
- Train Core
- Starte NLU, Core, MongoDB:
```
docker-compose up
```
- Starte Frontend
- Starte Logging