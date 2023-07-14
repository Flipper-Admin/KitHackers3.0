import os

while True:
    # Visualizza il prompt del terminale
    user_input = input("$ ")

    # Dividi l'input dell'utente in comando e argomenti
    parts = user_input.split()
    command = parts[0]
    args = parts[1:]

    # Esegui il comando appropriato
    if command == "cd":
        # Cambia la directory corrente
        try:
            os.chdir(args[0])
        except FileNotFoundError:
            print("La directory non esiste.")
    elif command == "ls":
        # Elenco dei file nella directory corrente
        files = os.listdir()
        for file in files:
            print(file)
    elif command == "pwd":
        # Visualizza la directory corrente
        print(os.getcwd())
    elif command == "help":
        # Mostra l'elenco dei comandi disponibili
        print("Comandi disponibili:")
        print("- cd <directory>: Cambia la directory corrente")
        print("- ls: Elenco dei file nella directory corrente")
        print("- pwd: Visualizza la directory corrente")
        print("- help: Mostra l'elenco dei comandi disponibili")
        print("- exit: Esci dal terminale")
    elif command == "exit":
        # Esci dal terminale
        break
    else:
        # Comando sconosciuto
        print("Comando sconosciuto.")

print("Terminale chiuso.")
