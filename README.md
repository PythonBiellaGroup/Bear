
<a name="readme-top"></a>
<div align="center">

[![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url] [![MIT License][license-shield]][license-url]
</div>
<div align="center">

  <h1 align="center">Python Biella Group: Bear</h1>
  <p align="center">
    <h3> Base Environment for Any Reasonable project</h3>
    <br />
    <br />
    ·
    <a href="https://github.com/PythonBiellaGroup/Bear/issues">Riporta un bug</a>
    ·
    <a href="https://github.com/PythonBiellaGroup/Bear/pulls">Richiedi una feature o un miglioramento</a>
  </p>
</div>

<details>
  <summary>Elenco dei contenuti</summary>
  <ol>
    <li><a href="#il-progetto">Il progetto</a></li>
    <li><a href="#requisiti">Il progetto</a></li>
    <li><a href="#costruito-con">Costruito con</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#utilizzo">Utilizzo</a></li>
    <li><a href="#come-mantenerlo">Come mantenerlo</a></li>
    <li><a href="#documentazione-tecnica">Documentazione tecnica</a></li>
    <li><a href="#contribuire">Contribuire</a></li>
    <li><a href="#licenza">Licenza</a></li>
    <li><a href="#problemi-riscontrati">Problemi riscontrati</a></li>
    <li><a href="#contatti">Contatti</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>

## Il progetto

Questo progetto è un template base per ogni Progetto Python che utilizziamo in tutte le repository di Python Biella Group per creare strumenti, librerie e progetti.

Lo abbiamo chiamato: **Bear** come acronimo di: **B**ase **E**nvironment for **A**ny **R**easonable project e anche perchè bear (l'orso) è il simbolo della città di Biella in Italia (Piemonte).

### Requisiti

Per questo progetto sono necessari i seguenti requisiti che devono essere installati:

- Python: >=3.10 <=3.12
- Poetry: >= 1.8.1

Raccomandiamo di installare **Poetry** utilizzando **Pyenv**, seguendo la guida ufficiale sul sito.

### Costruito con

Il progetto è basato sullo **stack tecnologico moderno di Python** come:

- **cookiecutter**: per la gestione del template
- **poetry**: per la gestione delle dipendenze
- **ruff**: per il linting e il controllo del codice
- **mypy**: per lo static type checking
- **black**: per la formattazione del codice (anche se può farlo ruff)
- **bandit**: per i controlli di sicurezza del codice (anche se può farlo ruff)
- **pre-commit**: per la gestione dei test e dei controlli pre-commit.
- **pydantic**: per il type checking evoluto
- **pydantic-settings**: per la gestione delle configurazioni

Suggeriamo di utilizzare **VSCode** come IDE per questo progetto in quanto puoi trovare una serie di configurazioni pronte per:

- debugging
- testing
- settings
- extensions
- sviluppo nei containers

Puoi trovare un'estensiva documentazione aggiuntiva creata con **mkdocs** disponibile sul [nostro sito](https://pythonbiellagroup.github.io/bear/)

## Roadmap

- [x] Aggiornare cookiecutter in modo che possa funzionare anche su windows con powershell
- [ ] Aggiornare l'implementazione di mkdocs sul pacchetto Base con gli esempi di codice Python
- [ ] Pubblicare l'esempio della documentazione di mkdocs su github page
- [ ] Aggiungere l'implementazione e i comandi di sphynx in modo da scegliere tra mkdocs e sphynx durante l'installazione
- [x] Aggiungere e migliorare pre-commit
- [ ] Migliore implementazione di detect-secrets
- [ ] Aggiungere un sistema per controllare l'update delle dipendenze, vulnerabilità e problemi di sicurezza
- [x] Miglioramento del README e nuova sezione su come contribuire
- [x] Aggiornare il docker dell'applicazione con Poetry
- [x] Aggiornare il devcontainer
- [ ] Esempio di pipeline con gitlab
- [ ] Esempio di pipeline con github
- [x] Possibilità di fare la build del pacchetto con Poetry
- [ ] Test incrociati su diverse versioni di Python utilizzando tox

Guarda le [open issues](https://github.com/PythonBiellaGroup/Bear/issues) per la lista di feature e miglioramenti proposti (oltre ai problemi degli altri utenti).

<p align="right">(<a href="#readme-top">torna all'inizio</a>)</p>

## Utilizzo

Puoi utilizzare questa repository come template per creare i tuoi progetti Python con **cookiecutter**

Come prima cosa ricordati di installare **cookiecutter** come dipendenza nella tua versione locale di Python utilizzando pip.

```bash
pip install cookiecutter
```

Puoi utilizzare i seguenti comandi per scaricare e configurare il progetto in locale (funziona sia su Windows che sistemi Posix)

```bash
# Se usi https
cookiecutter https://github.com/PythonBiellaGroup/Bear.git

# Se usi ssh
cookiecutter git@github.com:PythonBiellaGroup/Bear.git
```

Una volta lanciato il comando segui la guida nel terminale per riempire i campi e configurare il progetto.

Puoi anche creare un alias per questo comando nel tuo terminale, rendendo più facile il download:

```bash
# Se stai utilizzando https
alias pbg-project="cookiecutter https://github.com/PythonBiellaGroup/Bear.git --overwrite-if-exists"

# Se hai configurato ssh
alias pbg-project="cookiecutter git@github.com:PythonBiellaGroup/Bear.git --overwrite-if-exists"
```

Una volta configurato l'alias e riaperto il terminale puoi usare semplicemente il comando: `pbg-project` per scaricare il template e creare il nuovo progetto.

<p align="right">(<a href="#readme-top">Torna all'inizio</a>)</p>

## Come mantenerlo

Sfortunatamente non c'è un modo automatico per aggiornare il template cookiecutter, quindi è necessario fare gli aggiornamenti manualmente.

1. Clona la repository (oppure fai un fork e successivamente una pull request)
2. Lancia l'installazione delle dipendenze utilizzando poetry
   1. `poetry install`
3. Modifica quello che è necessario
4. Se vuoi testare il template interno puoi lanciare il comando: `make bake-test` per testare la generazione del progetto con cookiecutter, dopo di che:
   1. Modifica il template nella nuova finestra di vscode che si aprirà
   2. Quando hai finito le modifiche ricordati di copiare (a mano) i cambiamenti nella repository originale all'interno del template
5. Infine apri una pull request oppure fai un push nella repository (meglio prima in develop) se hai i permessi.

Ricordati di seguire il Gitlflow workflow e di usare la branch **develop** per sviluppare invece di main.

Prima di pubblicare una nuova versione su main o di fare una pull request cerca di testare che tutto funzioni bene.

<p align="right">(<a href="#readme-top">Torna all'inizio</a>)</p>

### Documentazione tecnica

Utilizziamo **mkdocs** per creare la documentazione di questo progetto

per lanciare la documentazione in locale usa il comando:

```bash
mkdocs serve
```

Se vuoi prepare la build degli artefatti prima di rilasciare su **github pages** puoi lanciare:

```bash
mkdocs build
```

Per altre informazioni su mkdocs rimandiamo alla repository del nostro sito realizzata interamente in mkdocs e un buon esempio di come si può configurare [website](https://github.com/PythonBiellaGroup/website)

<p align="right">(<a href="#readme-top">Torna all'inizio</a>)</p>

## Contribuire

Puoi contribuire a questo progetto aprendo delle issue su github o facendo delle pull request per aggiungere nuove funzionalità o correggere alcuni bugs.

Per favore segui le linee guide [Contributing guidelines](CONTRIBUTING.md) per contribuire al progetto.

<p align="right">(<a href="#readme-top">Torna all'inizio</a>)</p>

## Licenza

Questa repository utilizza la licenza MIT. Guarda il file: LICENSE per ulteriori dettagli.

Se utilizzi questa repository per il tuo lavoro per favore citaci oppure scrivi solamente un messaggio sui nostri canali di comunicazione per ringraziarci e darci un feedback sulla tua esperienza :)


<p align="right">(<a href="#readme-top">Torna all'inizio</a>)</p>

## Problemi riscontrati

Su mac se vuoi utilizzare `devcontainer` con `vscode` probabilmente dovrai aspettare parecchio la prima volta. Questo è causato da `amd64` docker base image che stiamo utilizzando come baseline e perchè il mac la deve virtualizzare utilizzando Rosetta.

<p align="right">(<a href="#readme-top">Torna all'inizio</a>)</p>

## Contatti

Reach out the community of PythonBiellaGroup!

[![Contacts][contacts-shield]][contacts-url]

<p align="right">(<a href="#readme-top">Torna all'inizio</a>)</p>

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
