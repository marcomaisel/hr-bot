## greet
* greet
    - utter_greet

## happy
* thankyou
    - utter_youarewelcome

## goodbye
* goodbye
    - utter_bye

## path 1
* introduction{"nameApplicant":"Marco"}
  - utter_greet
* findExistingJob
  - action_find_job

## Generated Story 2557009174438235936
* greet
    - utter_greet
* findExistingJob
    - action_find_job
    - slot{"jobs": [{"name": "Werkstudent Software-Entwicklung", "type": "student"}, {"name": "DevOps Spezialist", "type": "fulltime"}]}
* goodbye
    - utter_bye

## Generated Story 7245999155665718207
* findExistingJob
    - action_find_job
    - slot{"jobs": [{"name": "Werkstudent Software-Entwicklung", "type": "student"}, {"name": "DevOps Spezialist", "type": "fulltime"}]}