.PHONY: code-check
code-check:
	poetry run black .
	poetry run flake8 .

.PHONY: project_test
test:
	poetry run pytest .

.PHONY: poetry_install
install-dev:
	poetry config virtualenvs.in-project true
	poetry install
	poetry show -v

.PHONY: install_pipeline
install-pipeline:
	pip install --upgrade pip
	pip install poetry==1.1.13
	poetry config virtualenvs.in-project false
	poetry install --no-root --no-dev --no-interaction --no-ansi
	poetry show -v

.PHONY: project_clean
clean:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ ./notabooks/ipynb_checkpoints .pytest_cache ./dist ./volumes

.PHONY: project_restore
restore:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ ./notabooks/ipynb_checkpoints .pytest_cache ./dist .venv poetry.lock

.PHONY: poetry_build
package_build:
	poetry build

.PHONY: publish_pypi
pypi:
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*


### Project specific tasks
.PHONY: project
launch_py3:
	python3 app/main.py

.PHONY: project
launch_py:
	python app/main.py

## Docker
.PHONY: docker
# remember to change: template in the -p flag
# remember to be connected to the vpn
docker_launch:
	docker-compose -p template up --build -d

docker_build:
	docker-compose -p template build

docker_launch_prod:
	./lauch.sh

docker_check:
	docker ps -a | grep "template"

docker_stop:
	docker-compose down
	# docker-compose down -v