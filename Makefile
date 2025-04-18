####----Cookiecutter commands----####
.PHONY: cookiecutter
bake: ## bake without inputs and overwrite if exists.
	@uv run cookiecutter . --no-input -f

bake-clear: ## remove a previous cookiecutter bake
	@rm -rf testone || true

bake-test: ## bake the python project to test
	@rm -rf testone || true
	@uv run cookiecutter . --no-input -f --config-file config.yaml
	@code testone

####----Basic configurations----####
.PHONY: pre-commit
install_pre_commit: ## configure and install pre commit tool
	@uv run pre-commit install

uninstall_pre_commit: ## configure and install pre commit tool
	@uv run pre-commit uninstall

.PHONY: install
install: ## Install the uv and python environment
	@echo "🚀 Creating virtual environment using uv"
	@uv run --env-file .env -- uv sync --all-groups && uv pip install -e .

update: ## Update the uv environment
	@echo "🚀 Updating virtual environment using uv"
	@uv run --env-file .env -- uv lock --upgrade && uv sync --all-groups && uv pip install -e .

.PHONY: check_project
check_project: secrets ## Run code quality tools.
	@echo "🚀 Checking uv lock file consistency with 'pyproject.toml': Running uv lock --locked"
	@uv lock --locked
	@echo "🚀 Linting code: Running pre-commit"
	@uv run pre-commit run -a

	# # This is different from the gitleaks pre-commit since it checks also unstaged files
	# @gitleaks protect --no-banner --verbose

.PHONY: test
test: ## Test the code with pytest.
	@echo "🚀 Testing code: Running pytest"
	@uv run pytest --cov --cov-config=pyproject.toml --cov-report=xml tests

### Project specific tasks
.PHONY: project
launch_py3: # Launch the main file with python 3
	@export PYTHONPATH=$(pwd) && python3 app/main.py
launch_py: # Launch the main file with python
	@export PYTHONPATH=$(pwd) && python app/main.py

####----Documentation----####
.PHONY: docs
docs: ## Launch mkdocs documentation locally
	uv run mkdocs serve

docs_build: ## Build mkdocs for local test
	uv run mkdocs build

docs_launch_local: ## Launch mkdocs documentation locally with the local building artefacts
	uv run mkdocs build
	uv run mkdocs serve -v --dev-addr=0.0.0.0:8000

docs_deploy: ## Deploy mkdocs documentation to github pages
	uv run mkdocs build -c -v --site-dir public
	uv run mkdocs gh-deploy --force

docs_public: ## Build mkdocs for official online release
	uv run mkdocs build -c -v --site-dir public

####----Package Release----####
.PHONY: package
package_build: ## Build the python package
	poetry build

pypi: ## Build and upload the python package to pypi
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*

####----Docker----####
.PHONY: docker

launch: ## launch the python application containers
	docker compose -p bear up --build -d

launch_all: ## launch the backend project containers only
	docker compose -p bear up --build -d app

launch_db: ## launch the database container only
	docker compose -p bear up --build -d db

launch_dremio: ## launch the dremio container only
	docker compose -p bear up --build -d dremio

check: ## check the status of the docker containers
	docker ps -a | grep "bear"

check_logs: ## check the logs of the application container
	docker logs -t app

check_exec: ## exec bash in the python app container
	docker exec -it app /bin/bash

stop: ## stop all containers
	docker compose -p bear down
	# docker compose down -v

stop_clear: ## stop containers and clean the volumes
	docker compose -p bear down -v

clean_volumes: ## clean the docker volumes
	docker volume prune

####----Project----####
.PHONY: help
help: ## Ask for help in the Makefile
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: project
clean: ## Clean the projects of unwanted cached folders
	@rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ ./notebooks/ipynb_checkpoints .pytest_cache ./dist ./volumes
	@rm -rf {{cookiecutter.directory_name}} readmes cookiecutter.json hooks replay .gitlab

restore: ## Restore the projects to the start (hard clean)
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ ./notabooks/ipynb_checkpoints .pytest_cache ./dist .venv pdm.lock

.DEFAULT_GOAL := help
