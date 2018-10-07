## Generated Story -5038818765405399512
* introduction

## Generated Story 7655486924184811530
* introduction
    - utter_greet
* find_job{"jobTask": "designen"}
    - slot{"jobTask": ["designen"]}
    - action_match_job_slots
    - slot{"possibleTechnologies": ["photoshop", "design thinking", "sketch", "indesign", "accessibility", "invison", "usability", "prozessdesign", "illustrator"]}
    - slot{"possibleDomains": ["frontend", "web", "business", "mobile"]}
    - followup{"name": "utter_askTechnology"}
    - utter_askTechnology
* enter_data{"technology": "Photoshop"}
    - slot{"technology": ["Illustrator", "Photoshop"]}
    - action_match_job_slots
    - slot{"possibleDomains": ["frontend", "mobile", "web"]}
    - followup{"name": "utter_askDomain"}
    - utter_askDomain
* enter_data{"domain": "Frontend"}
    - slot{"domain": ["Frontend"]}
    - action_find_job
    - slot{"jobs": []}

