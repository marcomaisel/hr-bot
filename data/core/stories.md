## Start
* start_dialogue
    - utter_greet

## happy
* thankyou
    - utter_askFormOfEmployment

## goodbye
* goodbye
    - utter_bye

## Generated Story 7034160589158999056
* find_job{"jobTask": "entwickeln"}
    - slot{"jobTask": ["entwickeln"]}
    - action_match_job_slots
    - slot{"possibleTechnologies": ["typescript", "arc42", "requirements engineering", "sql", "scrum", "javascript", "nosql", "kanban", "mysql", "sqlite", "html", "postgresql", "css", "mongodb", "sass", "couchdb", "less", "nofs", "react", "verschl\u00fcsselung", "vue", "docker", "jquery", "ios", "openshift", "nodejs", "continuous integration", "npm", "continuous deployment", "python", "releasemanagement", "konfigurationsmanagement", "c", "build tools", "systemadministration", "c#", "systemintegration", "Natural Language Understanding", "software_testing", "Natural Language Processing", "teststrategie", "tensorflow", "testautomatisierung", "scikit-learn", "cucumber", "angular", "rasa", "mocha", "cui", "chai", "swift", "dialogflow", "supertest", "kotlin", "alexa", "unit test", "snips", "integrationstest", "java", "clustering", "end-to-end test", "android", "watson", "accessibility", "spring", "azure", "usability", "softwarearchitektur", "design thinking"]}
    - slot{"possibleDomains": ["web", "backend", "devops", "frontend", "testing", "security", "machine learning", "mobile", "fullstack", "agile"]}
    - followup{"name": "utter_askTechnology"}
    - utter_askTechnology
* enter_data{"technology": "CSS"}
    - slot{"technology": ["Angular", "TypeScript", "html", "CSS"]}
    - action_match_job_slots
    - slot{"possibleDomains": ["web", "frontend", "fullstack", "mobile", "backend"]}
    - followup{"name": "action_listen"}
* enter_data{"domain": "web"}
    - slot{"domain": ["web"]}
    - utter_askFormOfEmployment
* enter_data{"formOfEmployment": "vollzeit"}
    - slot{"formOfEmployment": "vollzeit"}
    - action_find_job
    - slot{"jobs": [{"domain": ["web", "mobile", "frontend"], "formOfEmployment": "vollzeit", "jobTask": ["entwickeln", "designen"], "name": "Frontend Developer", "technology": ["angular", "typescript", "javascript", "html", "css", "sass", "less", "react", "vue", "jquery", "npm", "buildtools", "photoshop", "illustrator", "sketch", "invision", "ui-test"]}]}

## Generated Story 2867705280703038743
* find_job{"jobTask": "entwickeln"}
    - slot{"jobTask": ["entwickeln"]}
    - action_match_job_slots
    - slot{"possibleTechnologies": ["watson", "softwarearchitektur", "design thinking", "arc42", "requirements engineering", "clustering", "sql", "scrum", "snips", "nosql", "kanban", "mysql", "alexa", "sqlite", "dialogflow", "postgresql", "cui", "mongodb", "android", "rasa", "couchdb", "nofs", "scikit-learn", "verschl\u00fcsselung", "swift", "tensorflow", "docker", "Natural Language Processing", "openshift", "Natural Language Understanding", "continuous integration", "continuous deployment", "releasemanagement", "azure", "c#", "konfigurationsmanagement", "build tools", "systemadministration", "spring", "c", "systemintegration", "python", "angular", "software_testing", "npm", "teststrategie", "kotlin", "nodejs", "testautomatisierung", "java", "jquery", "cucumber", "vue", "mocha", "typescript", "css", "chai", "supertest", "sass", "unit test", "html", "integrationstest", "react", "end-to-end test", "less", "accessibility", "ios", "javascript", "usability"]}
    - slot{"possibleDomains": ["web", "testing", "fullstack", "machine learning", "agile", "mobile", "security", "backend", "devops", "frontend"]}
    - followup{"name": "utter_askTechnology"}
    - utter_askTechnology
* enter_data{"technology": "React"}
    - slot{"technology": ["Vue", "React"]}
    - action_match_job_slots
    - slot{"possibleDomains": ["web", "frontend", "fullstack", "mobile", "backend"]}
    - followup{"name": "action_listen"}
* enter_data{"domain": "frontend"}
    - slot{"domain": ["frontend"]}
    - utter_askFormOfEmployment
* enter_data{"formOfEmployment": "vollzeit"}
    - slot{"formOfEmployment": "vollzeit"}
    - action_find_job
    - slot{"jobs": [{"domain": ["web", "mobile", "frontend"], "formOfEmployment": "vollzeit", "jobTask": ["entwickeln", "designen"], "name": "Frontend Developer", "technology": ["angular", "typescript", "javascript", "html", "css", "sass", "less", "react", "vue", "jquery", "npm", "buildtools", "photoshop", "illustrator", "sketch", "invision", "ui-test"]}]}
