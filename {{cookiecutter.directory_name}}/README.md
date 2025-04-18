# {{cookiecutter.project}}

## Description

{{cookiecutter.project}} is a python project

## Getting Started

### Prerequisites

- Python 3.10 or higher
- uv

### How to use it

1. Clone the repository
2. Create a new `.env` based on `.env.example`:

   ```bash
   cp .env.example .env
   ```

3. Configure the `.env` variables if it's necessary:

   ```bash
    LOG_VERBOSITY=INFO
    APP_NAME=bakky
    APP_VERSION=0.0.1
    DEBUG=True
   ```

4. Install the dependencies with python uv: `uv sync`
5. Run the project: you have different method to use
   1. Use vscode debugger configured inside the repo
   2. Use the command `uv run app/main.py` to run the project manually
   3. Use the bash script: `./scripts/launch.sh`
   4. User Makefile: `make run`
6. You can launch the docker-compose by doing: `make launch`

Remember that you can use `vscode` to run the project with `devcontainer`
