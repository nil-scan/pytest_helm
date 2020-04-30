requirements.txt: Pipfile.lock
	pipenv run pip freeze > requirements.txt

test: requirements.txt
	pipenv run tox