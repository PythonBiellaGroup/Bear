####----Basic configurations----####
.PHONY: pre-commit
install_pre_commit: ## configure and install pre commit tool
	@poetry run pre-commit install

uninstall_pre_commit: ## configure and install pre commit tool
	@poetry run pre-commit uninstall

.PHONY: install
install: ## Install the poetry and python environment
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install
	@poetry shell

install-poetry: ## Install the poetry environment
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install
	@poetry shell

install-pdm: ## Install the poetry environment
	@echo "🚀 Creating virtual environment using pyenv and PDM"
	@pdm install
	@pdm use

.PHONY: check_project
check_project: ## Run code quality tools.
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry lock --check
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
# echo "🚀 Checking for obsolete dependencies: Running deptry"
# poetry run deptry .

.PHONE: poetry_plugins
# poetry self add poetry-git-version-plugin
poetry_plugins_install: ## Install and configure the poetry plugins
	@echo "Install poetry-plugin-sort"
	@poetry self add poetry-plugin-sort
	@poetry self add poetry-plugin-up

poetry_plugins: ## Launch the poetry plugins
	@echo "Launching poetry-plugin-sort"
	@poetry sort


.PHONY: test
test: ## Test the code with pytest.
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml tests

### Project specific tasks
.PHONY: project
launch_py3:
	python3 app/main.py

.PHONY: project
launch_py:
	python app/main.py

####----Package Release----####
.PHONY: build
build: clean-build ## Build wheel file using poetry
	@echo "🚀 Creating wheel file"
	@poetry build

.PHONY: clean-build
clean-build: ## clean build artifacts
	@rm -rf dist

.PHONY: publish
publish: ## publish a release to pypi.
	@echo "🚀 Publishing: Dry run."
	@poetry config pypi-token.pypi $(PYPI_TOKEN)
	@poetry publish --dry-run
	@echo "🚀 Publishing."
	@poetry publish

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.

####----Documentation----####
.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@mkdocs serve

####----Docker----####
.PHONY: docker
create_network: ## create the docker network for the project
	docker network create template

launch: ## launch the python application containers
	docker-compose -p template up --build -d 

launch_all: ## launch the backend project containers only
	docker-compose -p template up --build -d app

launch_db: ## launch the database container only
	docker-compose -p template up --build -d db

check: ## check the status of the docker containers
	docker ps -a | grep "template"

check_logs: ## check the logs of the application container
	docker logs -t app

check_exec: ## exec bash in the python app container
	docker exec -it app /bin/bash

stop: ## stop all containers
	docker-compose -p template down
	# docker-compose down -v

stop_clear: ## stop containers and clean the volumes
	docker-compose -p template down -v

clean_volumes: ## clean the docker volumes
	docker volume prune

####----Project----####
.PHONY: help
help: ## Ask for help in the Makefile
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: project_clean
clean: ## Clean the projects of unwanted cached folders
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ ./notebooks/ipynb_checkpoints .pytest_cache ./dist ./volumes

.PHONY: project_restore
restore: ## Restore the projects to the start (hard clean)
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ ./notabooks/ipynb_checkpoints .pytest_cache ./dist .venv poetry.lock

.DEFAULT_GOAL := help
