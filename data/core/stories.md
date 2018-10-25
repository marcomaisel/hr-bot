## Start
* start_dialogue
    - utter_greet

## happy
* thankyou
    - utter_askFormOfEmployment

## goodbye
* goodbye
    - utter_bye

## Start + find_job
* start_dialogue
    - utter_greet
* find_job
    - utter_askJobTask
* enter_data{"jobTask": "designen"}
    - slot{"jobTask": "designen"}
    - utter_askDomain
* enter_data{"domain": "web"}
    - slot{"domain": "web"}
    - utter_askTechnology
* enter_data{"technology": "photoshop"}
    - slot{"technology": "photoshop"}
    - utter_askFormOfEmployment
* enter_data{"formOfEmployment": "praktikum"}
    - slot{"formOfEmployment": "praktikum"}
    - action_find_job
    - slot{"jobs": [{"name": "Praktikant Webdesign", "formOfEmployment": "praktikum", "jobTask": "designen", "domain": ["web"], "technology": "photoshop"}]}

## FindJob
* find_job
    - utter_askJobTask
* enter_data{"jobTask": "entwickeln"}
    - slot{"jobTask": "entwickeln"}
    - utter_askDomain
* enter_data{"domain": "mobile"}
    - slot{"domain": "mobile"}
    - utter_askTechnology
* enter_data{"technology": "html"}
    - slot{"technology": ["photoshop", "html"]}
    - utter_askFormOfEmployment
* enter_data{"formOfEmployment": "vollzeit"}
    - slot{"formOfEmployment": "vollzeit"}
    - action_find_job
