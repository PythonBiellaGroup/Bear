.PHONY: install
install: ## Install the environment using poetry as default
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

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Configure pre-commit hooks"
	@pre-commit install
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry lock --check
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@poetry run mypy
	@echo "🚀 Checking for obsolete dependencies: Running deptry"
	@poetry run deptry .

.PHONY: test
test: ## Test the code with pytest.
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml tests

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

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@mkdocs serve

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

#### Remove anwanted python stuff
.PHONY: project_clean
clean:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ ./notabooks/ipynb_checkpoints .pytest_cache ./dist ./volumes

.PHONY: project_restore
restore:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ ./notabooks/ipynb_checkpoints .pytest_cache ./dist .venv poetry.lock

### Project specific tasks
.PHONY: project
launch_py3:
	python3 app/main.py

.PHONY: project
launch_py:
	python app/main.py

#### Docker
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

.DEFAULT_GOAL := help
