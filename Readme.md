 HR-Bot with Rasa NLU and Rasa Core

## Introduction

This version of the bot  supports:
- xy
- yz

## Installation + Running of the bot

To install the bot, please clone the repo and run:

```
pip install -e .
```
This will install the bot and all of its requirements.

To train the core model: `python -m rasa_core.train -d domain.yml -s data/core/stories.md -o models/dialogue`

To train the NLU model: `python -m rasa_nlu.train -c config_tensorflow.yml --data data/nlu/nlu.json -o models --fixed_model_name nlu --project current --verbose`

To run the bot with both these models:
```
python -m rasa_core.run -d models/dialogue -u models/current/nlu
```


## Overview of the files

`data/core/` - contains stories for Rasa Core

`data/nlu` - contains example NLU training data

`domain.yml` - the domain file for Core

`nlu_tensorflow.yml` - the NLU config file