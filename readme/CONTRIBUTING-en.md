# How to Contribute

Your contribution is the most important thing for us!!

We are a community, and without your help and the help of contributors, we can't do anything :)

So, first of all: THANK YOU!

If you want to contribute to this repository, please check these requirements first:

- We suggest working on Linux systems; this template is not designed to work on Windows at the moment. Therefore, we recommend using: `wsl2`, `linux`, or `macos`.
- Have `python` and `uv` installed: check the `pyproject.toml` file to find the correct versions used in this project.
- Have `makefile`.

We recommend using Visual Studio Code. You can find a list of useful extensions and a dedicated Python profile inside the `.vscode` folder.

## Development and Updates

If you want to start the project and test it, you need to:

1. Fork the project into your GitHub profile. Then clone it locally.
2. Create a new branch, for example: `develop`.
3. Install the libraries: `uv sync`. This command will create a `.venv` folder inside the project directory with all the updated dependencies.
4. Then you can start editing the files inside the folder.
5. If you want to test if everything works, you need to "cookiecutterize" the project. You can do this using `just` or the Makefile with the command: `make bake-test` or `just bake-test`. This function can generate a test project called **testone** inside the project folder. If Visual Studio Code does not open automatically, you can use `code testone` to open the project in a new Visual Studio Code window and check if it works.
6. After modifying something in the testone project, unfortunately, you need to copy and paste the updates into the `cookiecutter.directory_name`.
7. After updating everything, remember to create a pull request from your GitHub project to the original project so we can review the changes and update the public code.
