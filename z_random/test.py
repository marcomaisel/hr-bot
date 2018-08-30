jobs = [
    {"name": "Werkstudent Software-Entwicklung", "formOfEmployment": "student",
     "jobTask": "entwicklung", "domain": ["web", "mobile"], "technology": ["java ee", "java"]},

    {"name": "Webdesigner", "formOfEmployment": "vollzeit", "jobTask": "design",
     "domain": ["web"], "technology": ["photoshop", "html", "css", "javascript"]},

    {"name": "Praktikant Webdesign", "formOfEmployment": "praktikum", "jobTask": "design",
     "domain": ["web"], "technology": "photoshop"},

    {"name": "Senior UX Designer", "formOfEmployment": "vollzeit", "jobTask": "design",
     "domain": ["web", "mobile"], "technology": ["html"]}
]

foundJobs = []
technologySlot = ["photoshop", "html"]
domainSlot = ["web", "mobile"]
taskSlot = "design"
formOfEmploymentSlot = "vollzeit"

for job in jobs:
    tech = job["technology"]
    print(tech)
    task = job["jobTask"]
    metatech = job["domain"]
    employment = job["formOfEmployment"]

    if [i for i in technologySlot if i in tech] and \
            [i for i in domainSlot if i in metatech] and \
            taskSlot in task and \
            formOfEmploymentSlot in employment:
        foundJobs.append(job)

description = ", ".join([c["name"] for c in foundJobs])
print(description)
