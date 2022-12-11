install: requirements.txt
	python3 -m pip install -U pip
	python3 -m pip install -U -r requirements.txt

test:
	#python -m pytest -vv test_application.py

lint:
	pylint --disable=R,C application.py

deploy:
	echo "Deploying app"
	eb deploy hello-env

all: install lint test 