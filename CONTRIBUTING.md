# How too contribute

Contributions it's the most important things for us!!

We are a community and without your help and the help of the contributors we cannot do nothing :)

So first of all: THANK YOU!

If you want to contribute to this repository please check this requirements before:

- Have poetry and python installed: check the `pyproject.toml` to find the right versions used in this project
- You can install and use also `pdm`, it's configured but not officially supported in this repository
- Have `makefile` or `just` installed. We suggest to use `just` because it's more modern and easily to install also on windows.

We recommend to use Visual Studio Code, you can find a list of useful extensions and a dedicated Python profile inside the `.vscode` folder.

## Develop and update

If you want to launch the project and test it you need to:

1. Fork the project in your github profile. Then clone locally.
2. Create a new branch for example: `develop`
3. Install the libraries (we suggest to use poetry): `poetry install --with dev` . This command will create a .venv inside the project folder with all the dependencies updated.
4. Then you can start modifying the files inside the folder.
5. If you want to test if everything it's working you have to `cookiecutter` the project, you can do it by using just or Makefile with the command: `make bake-test` or `just bake-test`. This function can generate a test project called **testone** inside the project folder, you can use `code testone` to open the project in a new vscode window and check if it's working.
6. After you modify something in testone project unfortunately you need to copy and paste the updates inside the `cookiecutter.directory_name`.
7. After you updated everything remember to create a pull request from your github project to the original project so we can review the modifications and update the public code.

