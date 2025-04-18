# Come contribuire

Il tuo contributo è la cosa più importante per noi!!

Siamo una comunità e senza il tuo aiuto e l'aiuto dei contributori non possiamo fare nulla :)

Quindi, prima di tutto: GRAZIE!

Se desideri contribuire a questo repository, controlla questi requisiti prima:

- Suggeriamo di lavorare su sistemi linux, questo template non è fatto per funzionare su windows al momento, suggeriamo quindi di utilizzare: `wsl2`, `linux`, `macos`.
- Avere `python`e `uv` installati: controlla il `pyproject.toml` per trovare le versioni corrette utilizzate in questo progetto
- Avere `makefile`.

Consigliamo di utilizzare Visual Studio Code, puoi trovare un elenco di estensioni utili e un profilo Python dedicato all'interno della cartella `.vscode`.

## Sviluppo e aggiornamento

Se desideri avviare il progetto e testarlo, devi:

1. Forkare il progetto nel tuo profilo GitHub. Quindi clonalo in locale.
2. Crea un nuovo branch, ad esempio: `develop`
3. Installa le librerie: `uv sync`. Questo comando creerà una cartella .venv all'interno della cartella del progetto con tutte le dipendenze aggiornate.
4. Quindi puoi iniziare a modificare i file all'interno della cartella.
5. Se desideri testare se tutto funziona, devi "cookiecutterizzare" il progetto, puoi farlo utilizzando just o Makefile con il comando: `make bake-test` o `just bake-test`. Questa funzione può generare un progetto di test chiamato **testone** all'interno della cartella del progetto, se Visual Studio Code non si apre automaticamente, puoi utilizzare `code testone` per aprire il progetto in una nuova finestra di Visual Studio Code e verificare se funziona.
6. Dopo aver modificato qualcosa nel progetto di testone, purtroppo devi copiare e incollare gli aggiornamenti all'interno della `cookiecutter.directory_name`.
7. Dopo aver aggiornato tutto, ricorda di creare una pull request dal tuo progetto GitHub al progetto originale in modo che possiamo esaminare le modifiche e aggiornare il codice pubblico.
