FILES :=              \
    .travis.yml       \
    models.html       \
    IDB.log           \
    models.py         \
    tests.py          \
    apiary.apib       \
    UML.pdf           \

IP := 104.239.231.99

all:

check:
	@for i in $(FILES);                                         \
    do                                                          \
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
    done

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  models.html
	rm -f  IDB.log
	rm -rf __pycache__

config:
	git config -l

test: 

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

tools:
	sudo apt-get -y install git python-pip python-virtualenv
	virtualenv my-venv
	source my-venv/bin/activate

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

ip:
	echo ${IP}
