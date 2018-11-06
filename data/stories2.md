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

## Generated Story -8320867140332627399
* find_job{"jobTask": "entwickeln"}
    - slot{"jobTask": ["entwickeln"]}
    - action_match_job_slots
    - slot{"possibleTechnologies": ["html", "azure", "usability", "softwarearchitektur", "design thinking", "typescript", "arc42", "requirements engineering", "javascript", "sql", "scrum", "nosql", "kanban", "mysql", "css", "sqlite", "postgresql", "swift", "sass", "mongodb", "couchdb", "less", "nofs", "react", "verschl\u00fcsselung", "vue", "docker", "jquery", "openshift", "nodejs", "continuous integration", "continuous deployment", "npm", "python", "releasemanagement", "c", "konfigurationsmanagement", "build tools", "systemadministration", "ios", "c#", "systemintegration", "Natural Language Understanding", "software_testing", "Natural Language Processing", "teststrategie", "tensorflow", "testautomatisierung", "scikit-learn", "cucumber", "android", "rasa", "mocha", "angular", "cui", "chai", "dialogflow", "supertest", "alexa", "unit test", "kotlin", "snips", "integrationstest", "java", "clustering", "end-to-end test", "spring", "watson", "accessibility"]}
    - slot{"possibleDomains": ["agile", "mobile", "web", "security", "testing", "machine learning", "backend", "devops", "fullstack", "frontend"]}
    - followup{"name": "utter_askTechnology"}
    - utter_askTechnology
* enter_data{"technology": "Angular"}
    - slot{"technology": ["Angular"]}
    - action_match_job_slots
    - slot{"possibleDomains": ["fullstack", "frontend", "web"]}
* enter_data{"domain": "web"}
    - slot{"domain": ["web"]}
    - utter_askFormOfEmployment
* enter_data{"formOfEmployment": "vollzeit"}
    - slot{"formOfEmployment": "vollzeit"}
    - action_find_job
    - slot{"jobs": [{"domain": ["web", "mobile", "frontend"], "formOfEmployment": "vollzeit", "jobTask": ["entwickeln", "designen"], "name": "Frontend Developer", "technology": ["angular", "typescript", "javascript", "html", "css", "sass", "less", "react", "vue", "jquery", "npm", "buildtools", "photoshop", "illustrator", "sketch", "invision", "ui-test"]}]}

