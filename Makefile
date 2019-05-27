test:
	pipenv run pytest -sx

lint:
	pipenv run pre-commit install && pipenv run pre-commit run -a -v && pipenv run pytest --dead-fixtures

pyformat:
	pipenv run black .
