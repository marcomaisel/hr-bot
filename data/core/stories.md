## greet
* greet
    - utter_greet

## happy
* thankyou
    - utter_youarewelcome

## goodbye
* goodbye
    - utter_bye

## Greet + findJob
* greet
    - utter_greet
* findJob
    - utter_askJobTask
* enterData{"jobTask": "designen"}
    - slot{"jobTask": "designen"}
    - utter_askDomain
* enterData{"domain": "web"}
    - slot{"domain": "web"}
    - utter_askTechnology
* enterData{"technology": "photoshop"}
    - slot{"technology": "photoshop"}
    - utter_askFormOfEmployment
* enterData{"formOfEmployment": "praktikum"}
    - slot{"formOfEmployment": "praktikum"}
    - action_find_job
    - slot{"jobs": [{"name": "Praktikant Webdesign", "formOfEmployment": "praktikum", "jobTask": "designen", "domain": ["web"], "technology": "photoshop"}]}

## FindJob
* findJob
    - utter_askJobTask
* enterData{"jobTask": "entwickeln"}
    - slot{"jobTask": "entwickeln"}
    - utter_askDomain
* enterData{"domain": "mobile"}
    - slot{"domain": "mobile"}
    - utter_askTechnology
* enterData{"technology": "html"}
    - slot{"technology": ["photoshop", "html"]}
    - utter_askFormOfEmployment
* enterData{"formOfEmployment": "vollzeit"}
    - slot{"formOfEmployment": "vollzeit"}
    - action_find_job
