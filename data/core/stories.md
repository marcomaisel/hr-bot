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
* enterData{"jobTask": "design"}
    - slot{"jobTask": "design"}
    - utter_askMetatechnology
* enterData{"metatechnology": "web"}
    - slot{"metatechnology": "web"}
    - utter_askTechnology
* enterData{"technology": "photoshop"}
    - slot{"technology": "photoshop"}
    - utter_askFormOfEmployment
* enterData{"formOfEmployment": "praktikum"}
    - slot{"formOfEmployment": "praktikum"}
    - action_find_job
    - slot{"jobs": [{"name": "Praktikant Webdesign", "formOfEmployment": "praktikum", "jobTask": "design", "metatechnology": ["web"], "technology": "photoshop"}]}

## FindJob
* findJob
    - utter_askJobTask
* enterData{"jobTask": "entwicklung"}
    - slot{"jobTask": "entwicklung"}
    - utter_askMetatechnology
* enterData{"metatechnology": "mobile"}
    - slot{"metatechnology": "mobile"}
    - utter_askTechnology
* enterData{"technology": "html"}
    - slot{"technology": ["photoshop", "html"]}
    - utter_askFormOfEmployment
* enterData{"formOfEmployment": "vollzeit"}
    - slot{"formOfEmployment": "vollzeit"}
    - action_find_job
