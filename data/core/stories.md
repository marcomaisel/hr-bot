## path 1
* introduction{"nameApplicant":"Marco"}
  - utter_greet
* findExistingJob{"desiredJob":"iOS-Entwicklung"}
  - utter_findJob

## path 2
* introduction{"nameApplicant":"Mona", "universityCourse":"BWL"}
  - utter_greet
* findExistingJob{"desiredJob":"Projektmanagement", "formOfEmployment":"Student"}
  - utter_findJob

## path 3
* findExistingJob{"desiredJob":"Software-Entwicklung", "formOfEmployment":"Werkstudent"}
  - utter_findJob
* importanceOfExperience{"desiredJob":"Software-Entwicklung", "formOfEmployment":"Werkstudent"}
  - utter_bye

## path 4
* introduction{"nameApplicant":"Jan", "university":"Hochschule der Medien", "universityCourse":"Medieninformatik"}
  - utter_greet
* findExistingJob{"desiredJob":"DevOps Spezialist", "formOfEmployment":"Werkstudent"}
  - utter_findJob
* importanceOfExperience{"amountOfExp":"wenig", "technology":"Berufserfahrung"}
  - utter_bye
