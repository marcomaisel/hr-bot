# Tasks
entwickeln = Task(name='entwickeln')
designen = Task(name='designen')
administrieren = Task(name='administrieren')
coachen = Task(name='coachen')
analysieren = Task(name='analysieren')

# Domains
web = Domain(name="web", tasks=[entwickeln,
                                designen, coachen], otherDomains=[])
mobile = Domain(name="mobile", tasks=[
    entwickeln, designen, coachen], otherDomains=[])
backend = Domain(name="backend", tasks=[
    entwickeln, coachen], otherDomains=[])
devops = Domain(name="devops", tasks=[
    entwickeln, coachen], otherDomains=[])
frontend = Domain(name="frontend", tasks=[
    entwickeln, designen, coachen], otherDomains=[web, mobile])
fullstack = Domain(name="fullstack", tasks=[entwickeln, coachen], otherDomains=[
    web, mobile, backend, frontend])
agile = Domain(name="agile", tasks=[coachen, entwickeln], otherDomains=[])
data_science = Domain(name="data science", tasks=[
    analysieren, ], otherDomains=[])
security = Domain(name="security", tasks=[
    analysieren, entwickeln], otherDomains=[])
personal = Domain(name="personal", tasks=[administrieren], otherDomains=[])
business = Domain(name="business", tasks=[
    administrieren, designen, analysieren], otherDomains=[])
finanzen = Domain(name="finanzen", tasks=[
    administrieren, analysieren], otherDomains=[])
machine_learning = Domain(name="machine learning", tasks=[
    entwickeln, analysieren], otherDomains=[])
testing = Domain(name="testing", tasks=[
    entwickeln, analysieren], otherDomains=[])
recht = Domain(name="recht", tasks=[administrieren], otherDomains=[])
consulting = Domain(name="consulting", tasks=[], otherDomains=[])
marketing = Domain(name="marketing", tasks=[], otherDomains=[])

# Technologies
angular = Technology(name='angular', tasks=[
    entwickeln], domains=[frontend, web, fullstack])
java = Technology(name='java', tasks=[entwickeln], domains=[
    frontend, backend, fullstack, mobile, web])
spring = Technology(name='spring', tasks=[entwickeln], domains=[
    frontend, backend, fullstack, web])
kotlin = Technology(name='kotlin', tasks=[entwickeln], domains=[
    backend, fullstack, mobile])
android = Technology(name='android', tasks=[entwickeln], domains=[
    backend, fullstack, mobile])
swift = Technology(name='swift', tasks=[entwickeln], domains=[
    backend, fullstack, mobile])
ios = Technology(name='ios', tasks=[entwickeln], domains=[
    backend, fullstack, mobile])
typescript = Technology(name='typescript', tasks=[entwickeln], domains=[
    frontend, backend, fullstack, mobile, web])
javascript = Technology(name='javascript', tasks=[entwickeln], domains=[
    frontend, backend, fullstack, mobile, web])
html = Technology(name='html', tasks=[entwickeln], domains=[
    frontend, fullstack, mobile, web])
css = Technology(name='css', tasks=[entwickeln], domains=[
    frontend, fullstack, mobile, web])
sass = Technology(name='sass', tasks=[entwickeln], domains=[
    frontend, fullstack, mobile, web])
less = Technology(name='less', tasks=[entwickeln], domains=[
    frontend, fullstack, mobile, web])
react = Technology(name='react', tasks=[entwickeln], domains=[
    frontend, fullstack, mobile, backend, web])
vue = Technology(name='vue', tasks=[entwickeln], domains=[
    frontend, fullstack, mobile, backend, web])
jquery = Technology(name='jquery', tasks=[entwickeln], domains=[
    frontend, fullstack, mobile, web])
nodejs = Technology(name='nodejs', tasks=[entwickeln], domains=[
    frontend, backend, fullstack, mobile, web, machine_learning])
npm = Technology(name='npm', tasks=[entwickeln], domains=[
    frontend, backend, fullstack, mobile, web])
python = Technology(name='python', tasks=[entwickeln], domains=[
    frontend, backend, fullstack, web, machine_learning, data_science])
c = Technology(name='c', tasks=[entwickeln], domains=[backend, fullstack])
build_tools = Technology(name='build tools', tasks=[entwickeln], domains=[
    frontend, backend, fullstack, mobile, web])
csharp = Technology(name='c#', tasks=[entwickeln], domains=[
    backend, fullstack])
nlu = Technology(name='Natural Language Understanding', tasks=[
    entwickeln], domains=[machine_learning])
nlp = Technology(name='Natural Language Processing', tasks=[
    entwickeln], domains=[machine_learning])
tensorflow = Technology(name='tensorflow', tasks=[entwickeln], domains=[
    machine_learning, data_science])
scikit_learn = Technology(
    name='scikit-learn', tasks=[entwickeln], domains=[data_science, machine_learning])
rasa = Technology(name='rasa', tasks=[entwickeln], domains=[
    mobile, backend, fullstack, machine_learning])
cui = Technology(name='cui', tasks=[entwickeln], domains=[
    mobile, backend, fullstack, machine_learning])
dialogflow = Technology(name='dialogflow', tasks=[entwickeln], domains=[
    mobile, backend, fullstack, machine_learning])
alexa = Technology(name='alexa', tasks=[entwickeln], domains=[
    mobile, backend, fullstack, machine_learning])
snips = Technology(name='snips', tasks=[
    entwickeln], domains=[machine_learning])
clustering = Technology(name='clustering', tasks=[entwickeln], domains=[
    machine_learning, data_science])
watson = Technology(name='watson', tasks=[
    entwickeln], domains=[machine_learning])
azure = Technology(name='azure', tasks=[
    entwickeln], domains=[machine_learning])

softwarearchitektur = Technology(name='softwarearchitektur', tasks=[
    entwickeln], domains=[backend, fullstack, mobile, web, frontend, testing])
arc42 = Technology(name='arc42', tasks=[entwickeln], domains=[
    backend, fullstack, mobile, web, frontend, testing])

sql = Technology(name='sql', tasks=[entwickeln], domains=[
    backend, fullstack, mobile, web, testing, data_science])
nosql = Technology(name='nosql', tasks=[entwickeln], domains=[
    backend, fullstack, mobile, web, testing, data_science])
mysql = Technology(name='mysql', tasks=[entwickeln], domains=[
    backend, fullstack, mobile, web, testing, data_science])
sqlite = Technology(name='sqlite', tasks=[entwickeln], domains=[
    backend, fullstack, mobile, web, testing, data_science])
postgresql = Technology(name='postgresql', tasks=[entwickeln], domains=[
    backend, fullstack, mobile, web, testing, data_science])
mongodb = Technology(name='mongodb', tasks=[entwickeln], domains=[
    backend, fullstack, mobile, web, testing, data_science])
couchdb = Technology(name='couchdb', tasks=[entwickeln], domains=[
    backend, fullstack, mobile, web, testing, data_science])
nofs = Technology(name='nofs', tasks=[entwickeln], domains=[
    backend, fullstack, mobile, web, testing, data_science])

verschlüsselung = Technology(name='verschlüsselung', tasks=[
    entwickeln], domains=[security])

docker = Technology(name='docker', tasks=[entwickeln], domains=[devops])
openshift = Technology(name='openshift', tasks=[
    entwickeln], domains=[devops])
ci = Technology(name='continuous integration', tasks=[
    entwickeln], domains=[devops])
cd = Technology(name='continuous deployment', tasks=[
    entwickeln], domains=[devops])
config_management = Technology(name='releasemanagement', tasks=[
    entwickeln], domains=[devops])
release_management = Technology(name='konfigurationsmanagement', tasks=[
    entwickeln], domains=[devops])
systemadministration = Technology(name='systemadministration', tasks=[
    entwickeln, administrieren], domains=[devops])
systemintegration = Technology(name='systemintegration', tasks=[
    entwickeln], domains=[devops])

software_testing = Technology(name='softwaretesting', tasks=[
    entwickeln], domains=[testing])
teststrategie = Technology(name='teststrategie', tasks=[
    entwickeln], domains=[testing])
testautomatisierung = Technology(name='testautomatisierung', tasks=[
    entwickeln], domains=[testing])
cucumber = Technology(name='cucumber', tasks=[
    entwickeln], domains=[testing])
mocha = Technology(name='mocha', tasks=[
    entwickeln], domains=[testing])
chai = Technology(name='chai', tasks=[
    entwickeln], domains=[testing])
supertest = Technology(name='supertest', tasks=[
    entwickeln], domains=[testing])
unit_test = Technology(name='unit test', tasks=[
    entwickeln], domains=[testing])
integrationstest = Technology(name='integrationstest', tasks=[
    entwickeln], domains=[testing])
end_to_end_test = Technology(name='end-to-end test', tasks=[
    entwickeln], domains=[testing])

accessibility = Technology(name='accessibility', tasks=[
    designen, entwickeln, coachen], domains=[web, mobile, frontend, fullstack, testing])
usability = Technology(name='usability', tasks=[
    designen, entwickeln, coachen], domains=[web, mobile, frontend, fullstack, testing])
design_thinking = Technology(name='design thinking', tasks=[
    designen, entwickeln, coachen, analysieren], domains=[web, mobile, frontend, fullstack, testing])

photoshop = Technology(name='photoshop', tasks=[
    designen], domains=[web, mobile, frontend])
illustrator = Technology(name='illustrator', tasks=[
    designen], domains=[web, mobile, frontend])
indesign = Technology(name='indesign', tasks=[
    designen], domains=[web, mobile, frontend])
sketch = Technology(name='sketch', tasks=[
    designen], domains=[web, mobile, frontend])
invison = Technology(name='invison', tasks=[
    designen], domains=[web, mobile, frontend])

office = Technology(name='office', tasks=[
    administrieren], domains=[personal, business, finanzen, recht])
word = Technology(name='word', tasks=[
    administrieren], domains=[personal, business, finanzen, recht])
excel = Technology(name='excel', tasks=[
    administrieren], domains=[personal, business, finanzen, recht])
powerpoint = Technology(name='powerpoint', tasks=[
    administrieren], domains=[personal, business, finanzen, recht])

prozessdesign = Technology(name='prozessdesign', tasks=[
    administrieren, designen], domains=[business])
prozessanalyse = Technology(name='prozessanalyse', tasks=[
    administrieren, analysieren], domains=[business])
businessanalyse = Technology(name='businessanalyse', tasks=[
    administrieren, analysieren], domains=[business])
geschäftsmodell = Technology(name='geschäftsmodell', tasks=[
    administrieren, analysieren], domains=[business])
strategieberatung = Technology(name='strategieberatung', tasks=[
    administrieren, analysieren], domains=[business])
bewerbermanagement = Technology(name='bewerbermanagement', tasks=[
    administrieren], domains=[personal])
weiterbildungsmanagement = Technology(name='weiterbildungsmanagement', tasks=[
    administrieren], domains=[personal])
personalverwaltung = Technology(name='personalverwaltung', tasks=[
    administrieren], domains=[personal])
projektplan = Technology(name='projektplan', tasks=[
    administrieren], domains=[business])
gantt = Technology(name='gantt', tasks=[
    administrieren], domains=[business])
requirements_engineering = Technology(name='requirements engineering', tasks=[
    administrieren, analysieren, entwickeln], domains=[business])
projektmanagement = Technology(name='projektmanagement', tasks=[
    administrieren], domains=[business])

controlling = Technology(name='controlling', tasks=[
    administrieren], domains=[finanzen])
buchführung = Technology(name='buchführung', tasks=[
    administrieren], domains=[finanzen])
buchhaltung = Technology(name='buchhaltung', tasks=[
    administrieren], domains=[finanzen])

arbeitsrecht = Technology(name='arbeitsrecht', tasks=[
    administrieren], domains=[recht])
steuerrecht = Technology(name='steuerrecht', tasks=[
    administrieren], domains=[recht])
sozialversicherungsrecht = Technology(name='sozialversicherungsrecht', tasks=[
    administrieren], domains=[recht])

workshop = Technology(name='workshop', tasks=[
    coachen], domains=[agile])
schulung = Technology(name='schulung', tasks=[
    coachen], domains=[agile])
scrum = Technology(name='scrum', tasks=[
    coachen, entwickeln], domains=[agile])
kanban = Technology(name='kanban', tasks=[
    coachen, entwickeln], domains=[agile])
