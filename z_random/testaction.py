jobs = [
            {"name": "Werkstudent Software-Entwicklung", "formOfEmployment": ["werkstudent"],
             "jobTask": ["entwickeln"], "domain": ["web", "mobile"], "technology": ["java ee", "java"]},

            {"name": "Webdesigner", "formOfEmployment": ["vollzeit"], "jobTask": ["designen"],
             "domain": ["web"], "technology": ["photoshop", "html", "css", "javascript"]},

            {"name": "Praktikant Webdesign", "formOfEmployment": ["praktikum"], "jobTask": ["designen"],
             "domain": ["web"], "technology": ["photoshop"]},

            {"name": "Frontend Developer", "formOfEmployment": ["vollzeit"], "jobTask": [
                "entwickeln", "designen"], "domain": ["web", "mobile", "frontend"], "technology": ["angular", "typescript", "javascript", "html", "css", "sass", "less", "react", "vue", "jquery", "npm", "buildtools", "photoshop", "illustrator", "sketch", "invision", "ui-test"]}


        ]

foundJobs = []

# Store the values of slots given by the user with the tracker object
taskSlot = ['entwickeln']
domainSlot = ['Web']
technologySlot = ['Angular', "typescript", "html", "css"]
formOfEmploymentSlot = ['Vollzeit']

for job in jobs:
            # Store the values of each key for all job dictionaries in the jobs list
    tech = job["technology"]
    task = job["jobTask"]
    domain = job["domain"]
    employment = job["formOfEmployment"]

            # Search for matches between slots sent by the user and stored jobs in the jobs list.
            # If a job has at least one value for each key in the dictionary the job is appended to the foundJobs list.
    if [i.lower() for i in technologySlot if i.lower() in tech] and \
    [i.lower() for i in domainSlot if i.lower() in domain] and \
    [i.lower() for i in taskSlot if i.lower() in task] and \
    [i.lower() for i in formOfEmploymentSlot if i.lower() in employment]:
        foundJobs.append(job)


        # Create a message for the user with a list of names of all found jobs, separated by comma
jobMessage = ", ".join([c["name"] for c in foundJobs])

        # Send message with all found jobs to the user with the dispatcher object
print("Found: " + jobMessage)