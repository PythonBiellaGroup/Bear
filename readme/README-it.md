<a name="readme-top"></a>
<div align="center">

[![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url] [![MIT License][license-shield]][license-url]
</div>
<div align="center">

  <h1 align="center">Python Biella Group: Bear</h1>
  <p align="center">
    <h3> Ambiente Base per Qualsiasi Progetto Ragionevole</h3>
    <br />
    <a href="https://github.com/PythonBiellaGroup/Bear/issues">Segnala un Bug</a>
    ·
    <a href="https://github.com/PythonBiellaGroup/Bear/pulls">Richiedi una Funzionalità</a>
  </p>
</div>

<details>
  <summary>Indice</summary>
  <ol>
    <li><a href="#about-the-project">Informazioni sul Progetto</a></li>
    <li><a href="#built-with">Costruito con</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#usage">Utilizzo</a></li>
    <li><a href="#how-to-mantain-it">Come mantenerlo</a></li>
    <li><a href="#technical-documentation">Documentazione Tecnica</a></li>
    <li><a href="#contributing">Contributi</a></li>
    <li><a href="#license">Licenza</a></li>
    <li><a href="#known-issues">Problemi Conosciuti</a></li>
    <li><a href="#contacts">Contatti</a></li>
    <li><a href="#references">Riferimenti</a></li>
  </ol>
</details>

## Informazioni sul Progetto

Questo progetto è il modello base per un progetto Python che utilizziamo in PythonBiellaGroup per creare i nostri strumenti, librerie e progetti.

Lo chiamiamo **Bear** perché è un **B**ase **E**nvironment for **A**ny **R**easonable project e anche perché l'orso è il simbolo della città di Biella (Piemonte), Italia.

### Requisiti

Per questo progetto è necessario avere installato:

- Python: >=3.10 <=3.12
- uv

### Costruito con

Si basa su **Strumenti Moderni per Python** come:

- cookiecutter: per il templating
- uv: per la gestione delle dipendenze
- mypy: per il controllo statico dei tipi
- ruff: per formattazione del codice, linting, controllo, sicurezza, ecc.
- pytest: per i test
- pre-commit: per i pre-commit hook
- pydantic: per il controllo dei tipi
- pydantic-settings: per la gestione delle impostazioni

Suggeriamo di utilizzare **VSCode** come IDE per questo progetto poiché puoi trovare molte configurazioni già pronte per:

- debug
- test
- impostazioni
- estensioni
- testone

Puoi trovare un'ampia documentazione creata con **mkdocs** a [questo link della pagina GitHub](https://pythonbiellagroup.github.io/bear/)

## Roadmap

- [x] Aggiornare il progetto con uv
- [x] Correggere cookiecutter per l'uso con Windows PowerShell
- [x] Aggiungere implementazione mkdocs nel pacchetto base con un esempio di codice Python
- [x] Correggere pre-commit
- [x] Aggiungere una migliore implementazione di detect-secrets
- [x] Migliorare la documentazione README e CONTRIBUTING
- [x] Correggere il docker con poetry
- [x] Correggere il devcontainer
- [x] Aggiungere un container Docker con installazione di PDM
- [x] Aggiungere build del pacchetto

Consulta le [issue aperte](https://github.com/PythonBiellaGroup/Bear/issues) per un elenco completo delle funzionalità proposte (e dei problemi noti).

<p align="right">(<a href="#readme-top">torna in alto</a>)</p>

## Utilizzo

Puoi utilizzare questo repository come modello per creare il tuo progetto con **cookiecutter**

Ricorda di aggiungere **cookiecutter** come dipendenza nella tua installazione locale di Python utilizzando pip (o altro).

```bash
pip install cookiecutter

# Se stai usando https
cookiecutter https://github.com/PythonBiellaGroup/Bear.git

# Se stai usando ssh
cookiecutter git@github.com:PythonBiellaGroup/Bear.git
```

Una volta lanciati questi comandi, segui la guida e compila i campi richiesti.

Puoi anche creare un Alias per questo comando per renderlo più facile da usare nel tuo terminale

```bash
# Se stai usando https
alias pbg-project="cookiecutter https://github.com/PythonBiellaGroup/Bear.git --overwrite-if-exists"

# Se stai usando ssh
alias pbg-project="cookiecutter git@github.com:PythonBiellaGroup/Bear.git --overwrite-if-exists"
```

## Come mantenerlo

Così potrai semplicemente usare il comando: pbg-project dopo aver riavviato il terminale per scaricare e creare un nuovo progetto.

<p align="right">(<a href="#readme-top">torna in alto</a>)</p>

Come mantenerlo
Purtroppo non esiste ancora un modo automatico per aggiornare i modelli all'interno di cookiecutter, devi farlo manualmente.

Clona il repository
Lancia l'installazione delle dipendenze usando uv: uv sync
Modifica qualcosa
Se vuoi testare un modello interno specifico puoi usare il comando: make bake-test, creerà una nuova cartella con il nome testone e copierà il modello al suo interno.
Dopo di ciò puoi lanciare e modificare il modello
Quando hai finito le modifiche devi copiare e incollare manualmente tutte le modifiche nella cartella di generazione di cookiecutter
Ricorda poi di aprire una pull request o di fare il push nel repository (prima in develop) se hai i permessi.
Ricorda anche di seguire un flusso di lavoro Gitflow e di utilizzare il branch develop come branch principale per lo sviluppo.

<p align="right">(<a href="#readme-top">torna in alto</a>)</p>

## Problemi conosciuti

Su Mac, se vuoi utilizzare devcontainer con vscode probabilmente sperimenterai un lungo tempo di build la prima volta. Questo è dovuto all'immagine Docker base amd64 che stiamo utilizzando come base.

<p align="right">(<a href="#readme-top">torna in alto</a>)</p>

## References

Useful links and other documentation website you can check

- [Our website with the documentation](https://pythonbiellagroup.it)
- [The repository for our documentation](https://github.com/PythonBiellaGroup/doc-website)
- [Hypermodern python repository](https://github.com/cjolowicz/hypermodern-python)
- [The hypermodern python official medium article](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769)
- [Modern Python repository](https://github.com/rhettinger/modernpython)
- [Awesome Pyproject](https://github.com/carlosperate/awesome-pyproject/blob/master/README.md)
- [Python developer roadmap](https://roadmap.sh/python/)
- [Creating a modern python development environment medium article](https://itnext.io/creating-a-modern-python-development-environment-3d383c944877)
- [Modern python interesting practices](https://www.stuartellis.name/articles/python-modern-practices/)
- [4 Keys to write modern python in 2022](https://www.infoworld.com/article/3648061/4-keys-to-writing-modern-python-in-2022.html)
- [cookiecutter-poetry good implementation](https://github.com/fpgmaas/cookiecutter-poetry)
- [dev container video tutorial](https://www.youtube.com/watch?v=0H2miBK_gAk)
- [Ruff official documentation](https://github.com/charliermarsh/ruff/blob/main/README.md)
- [Ruff vscode extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- [Chef repository with some more modern tooling](https://github.com/baggiponte/chef)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/PythonBiellaGroup/Bear.svg?style=for-the-badge
[contributors-url]: https://github.com/PythonBiellaGroup/Bear/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PythonBiellaGroup/Bear.svg?style=for-the-badge
[forks-url]: https://github.com/PythonBiellaGroup/Bear/forks
[stars-shield]: https://img.shields.io/github/stars/PythonBiellaGroup/Bear.svg?style=for-the-badge
[stars-url]: https://github.com/PythonBiellaGroup/Bear/stargazers
[issues-shield]: https://img.shields.io/github/issues/PythonBiellaGroup/Bear.svg?style=for-the-badge
[issues-url]: https://github.com/PythonBiellaGroup/Bear/issues
[license-shield]: https://img.shields.io/github/license/PythonBiellaGroup/Bear.svg?style=for-the-badge
[license-url]: https://github.com/PythonBiellaGroup/Bear/blob/main/LICENSE
[contacts-shield]: https://img.shields.io/badge/linktree-39E09B?style=for-the-badge&logo=linktree&logoColor=white
[contacts-url]: https://linktr.ee/PythonBiellaGroup