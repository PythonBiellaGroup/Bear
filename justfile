# Intro recap about just
help:
	@echo """\nRun just -h if you want some help on the commands \n\
	Type:\tjust --list if you want a list of available recipes. \n\
	Launch:\tjust <recipe_name> if you want to launch a specific recipe.\n"""

# bake without inputs and overwrite if exists.
bake:
	@cookiecutter --no-input . --overwrite-if-exists

# remove a previous cookiecutter bake
bake-clear:
	@rm -rf testone || true
	@rm -rf python-skeleton || true

# bake the base project to test
bake-test:
	@rm -rf testone || true
	@poetry run cookiecutter --no-input . --overwrite-if-exists --config-file config.yaml
	@code testone

# Configure and install pre commit tool
install_pre_commit: 
	poetry run pre-commit install

# Configure and install pre commit tool
uninstall_pre_commit: 
	poetry run pre-commit uninstall

# Install the poetry and python environment
install:
	echo "🚀 Creating virtual environment using pyenv and poetry"
	poetry install
	poetry shell

# Install the poetry environment
install-poetry:
	echo "🚀 Creating virtual environment using pyenv and poetry"
	poetry install
	poetry shell

# Install the poetry environment
install-pdm:
	echo "🚀 Creating virtual environment using pyenv and PDM"
	pdm install
	pdm use

# Run code quality tools.
check_project:
	echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	poetry lock --check
	echo "🚀 Linting code: Running pre-commit"
	poetry run pre-commit run -a
# echo "🚀 Checking for obsolete dependencies: Running deptry"
# poetry run deptry .

# Install and configure the poetry plugins
poetry_plugins_install:
	echo "Install poetry-plugin-sort"
	poetry self add poetry-plugin-sort
	poetry self add poetry-plugin-up

# Update the poetry environment
poetry_update:
	echo "🚀 Updating virtual environment using poetry"
	poetry self update

# Launch the poetry plugins
poetry_plugins:
	echo "Launching poetry-plugin-sort"
	poetry sort

# Test the code with pytest.
test:
	echo "🚀 Testing code: Running pytest"
	poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml tests

# Launch the app/main.py with python3
launch_py3:
	python3 app/main.py

# Launch the app/main.py with normal python
launch_py:
	python app/main.py

# Build wheel file using poetry
build: clean-build #
	echo "🚀 Creating wheel file"
	poetry build

# Clean build artifacts
clean-build:
	rm -rf dist

# Publish a release to pypi.
publish:
	echo "🚀 Publishing: Dry run."
	poetry config pypi-token.pypi $(PYPI_TOKEN)
	poetry publish --dry-run
	echo "🚀 Publishing."
	poetry publish

# Test if mkdocs documentation can be built without warnings or errors
docs-test:
	poetry run mkdocs build -s

# Build and serve the documentation
docs:
	poetry run mkdocs serve

# Launch mkdocs documentation locally with the local building artefacts
docs_launch_local:
	@poetry run mkdocs build
	@poetry run mkdocs serve -v --dev-addr=0.0.0.0:8000

# Deploy mkdocs documentation to github pages
docs_deploy:
	@poetry run mkdocs build
	@poetry run mkdocs gh-deploy --force

# Build mkdocs for official online release
docs_public:
	@poetry run mkdocs build -c -v --site-dir public

# Create the docker network for the project
create_network:
	docker network create tempy

# Launch the python application containers
launch:
	docker-compose -p tempy up --build -d 

# Launch the backend project containers only
launch_all:
	docker-compose -p tempy up --build -d app

# Launch the database container only
launch_db:
	docker-compose -p tempy up --build -d db

# Check the status of the docker containers
check:
	docker ps -a | grep "tempy"

# Check the logs of the application container
check_logs:
	docker logs -t app

# Exec bash in the python app container
check_exec:
	docker exec -it app /bin/bash

# Stop all containers
stop:
	docker-compose -p tempy down
	# docker-compose down -v

# Stop containers and clean the volumes
stop_clear:
	docker-compose -p tempy down -v

# Clean the docker volumes
clean_volumes:
	docker volume prune

# Clean the projects of unwanted cached folders
clean:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ ./notebooks/ipynb_checkpoints .pytest_cache ./dist ./volumes

# Restore the projects to the start (hard clean)
restore:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ ./notabooks/ipynb_checkpoints .pytest_cache ./dist .venv poetry.lock