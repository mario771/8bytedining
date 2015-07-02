FILES :=              \
    .travis.yml       \
    models.html       \
    IDB.log           \
    models.py         \
    tests.py          \
    apiary.apib       \
    UML.pdf           \

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

