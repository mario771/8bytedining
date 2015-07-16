FILES :=              \
    .travis.yml       \
    models.html       \
    IDB.log           \
    models.py         \
    tests.py          \
    apiary.apib       \
    UML.pdf           \
    .gitignore

IP := 104.239.231.99

all:

final:
	pydoc3 -w models
	git log>IDB.log
	git rev-parse HEAD

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  models.html
	rm -f  IDB.log
	rm -rf __pycache__

config:
	git config -l

test: 
	python3 food/manage.py test foodApp

models.html: models.py
	pydoc3 -w models

IDB.log:
	git log > IDB.log

#RunCollatz.out: RunCollatz.py
#	cat RunCollatz.in
#	./RunCollatz.py < RunCollatz.in > RunCollatz.out
#	cat RunCollatz.out

#TestCollatz.out: TestCollatz.py
#	coverage3 run    --branch TestCollatz.py >  TestCollatz.out 2>&1
#	coverage3 report -m                      >> TestCollatz.out
#	cat TestCollatz.out

login:
	ssh -i .ssh/id_rsa_rackspace test@${IP}

secure:
	wget https://raw.githubusercontent.com/everett-toews/rackspace-developer-doubleplusgood/gh-pages/scripts/secure.sh
	chmod u+x secure.sh
	./secure.sh

get:
	sudo apt-get -y install git python-pip python-virtualenv

v1:
	virtualenv my-venv
v2:
	. my-venv/bin/activate

lego:
	git clone https://github.com/MDamien/legoit.git
	cd legoit
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py retrieve_data
	python manage.py runserver

food:
	echo 'git clone https://github.com/wongpeterp/cs373-idb.git'
	echo 'cd cs373-idb/foodApp'
	pip3 install -r requirements.txt
	python manage.py migrate
	python manage.py retrieve_data
	echo 'now make fgrun'

fgrun:
	python manage.py runserver 0.0.0.0:8000

bgrun:
	python manage.py runserver 0.0.0.0:8000>/home/test/log.txt &2>1 &

openport:
	sudo ufw allow 8000
	python manage.py runserver 0.0.0.0:8000
migrate:
	./manage.py flush
	./manage.py makemigrations foodApp
	./manage.py migrate
	ls foodApp/fixtures
load:
	./manage.py loaddata ingredients_list_models.json
	./manage.py loaddata cuisine_models.json 
	./manage.py loaddata Recipe_addedID_models_data.json

reload: migrate load

ip:
	echo ${IP}
