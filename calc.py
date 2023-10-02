##*data*##
h=True # Bool Ciclo
lang="" # Valore lingua (ABBASTANZA INUTILE)


##*code*##
print("Select your language:/Seleziona la tua lingua:\n\n1. FOR/PER Italiano\n2. FOR/PER English") # Print selezione lingua
xvdortsonotineb=input() # Input selezione lingua
if xvdortsonotineb=="1" or xvdortsonotineb=="1.": # Controlla se lingua selezionata è IT
    lang="IT" # Inizzializza lingua selezionata
    print("Lingua Scelta:",lang) # Printa lingua selezionata
    while h==True: # Ciclo Calcolatrice
        h=True # Valore Ciclo
        print("Inserire 1° valore:") # Print Input 1
        a=input() # Input 1
        if "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.-+*/_!£$%&/()?'ì^|\\" in a: # Controllo Input 1
            print("ERRORE! Non è stato inserito un valore corretto nel 1° valore") # Print Errore Input 1
        print("Inserire operazione (Se non sai cosa fare inserisci S):") # Print Input 2
        cal=input() # Input 2
        if "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" in cal: # Controllo Input 2
            print("ERRORE! Non è stato inserito un valore corretto nell'operazione") # Print Errore Input 2
        print("Inserire 2° valore:") # Print Input 3
        b=input() # Input 3
        if "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.-+*/_!£$%&/()?'ì^|\\" in b: # Controllo Input 3
            print("ERRORE! Non è stato inserito un valore corretto nel 2° valore") # Print Errore Input 3
        a=int(a) # Conversione String - Int valore 1
        b=int(b) # Conversione String - Int valore 2
        if cal=="s"or cal=="S": # Controllo selezione aiuto
            print("LISTA OPERAZIONI DISPONIBILI:\n+ -> Addizione\n- -> Sottrazione\nx -> Moltiplicazione\n: -> Divisione") # Print lista aiuto
            print("Per uscire premi E altrimenti inserisci qualsiasi altro valore:") # Print uscita
            ex=input() # Input uscita
            if "E" in ex or "e" in ex: # Controllo uscita
                h=False # Cambio valore ciclo
                break # Uscita programma
        elif cal=="+": # Controllo selezione +
            print(a,"+",b,"=",a+b) # Print operazione
            print("Per uscire premi E altrimenti inserisci qualsiasi altro valore:") # Print uscita
            ex=input() # Input uscita
            if "E" in ex or "e" in ex: # Controllo Uscita
                h=False # cambio valore ciclo
                break # Uscita programma
        elif cal=="-": # Controllo selezione -
            print(a,"-",b,"=",a-b) # Print operazione
            print("Per uscire premi E altrimenti inserisci qualsiasi altro valore:") # Print uscita
            ex=input() # Input uscita
            if "E" in ex or "e" in ex: # Controllo uscita
                h=False # Cambio valore ciclo
                break # Uscita programma
        elif cal=="*" or cal=="x" or cal=="X" or cal=="•": # Controllo selezione x
            print(a,"•",b,"=",a*b) # Print operazione
            print("Per uscire premi E altrimenti inserisci qualsiasi altro valore:") # Print uscita
            ex=input() # Input uscita
            if "E" in ex or "e" in ex: # Controllo uscita
                h=False # Cambio valore ciclo
                break # Uscita programma
        elif cal==":" or cal=="/": # Controllo selezione :
            print(a,":",b,"=",a/b) # Print operazione
            print("Per uscire premi E altrimenti inserisci qualsiasi altro valore:") # Print uscita
            ex=input() # Input uscita
            if "E" in ex or "e" in ex: # Controllo uscita
                h=False # Cambio valore ciclo
                break # Uscita programma
elif xvdortsonotineb=="2" or xvdortsonotineb=="2.": # Controlla se lingua selezionata è EN
    lang="EN" #Inizzializza lingua selezionata
    print("Chosen Language:",lang) # Printa lingua selezionata
    while h==True: # Ciclo Calcolatrice
        h=True # Valore Ciclo
        print("Insert 1° value:") # Print Input 1
        a=input() # Input 1
        if "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.-+*/_!£$%&/()?'ì^|\\" in a: # Controllo Input 1
            print("ERROR! Incorrect value in the 1st value") # Print Errore Input 1
        print("Insert operation (To print the operation list press S):") # Print Input 2
        cal=input() # Input 2
        if "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" in cal: # Controllo Input 2
            print("ERROR! Incorrect value in the operation") # Print Errore Input 2
        print("Insert 2° value:") # Print Input 3
        b=input() # Input 3
        if "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.-+*/_!£$%&/()?'ì^|\\" in b: # Controllo Input 3
            print("ERROR! Incorrect value in the 2nd value") # Print Errore Input 3
        a=int(a) # Conversione String - Int valore 1
        b=int(b) # Conversione String - Int valore 2
        if cal=="s"or cal=="S": # Controllo selezione aiuto
            print("AVAILABLE OPERATIONS LIST:\n+ -> Addiction\n- -> Subctraction\nx -> Moltiplication\n: -> Division") # Print lista aiuto
            print("To exit press E, otherwise press any other value:") # Print uscita
            ex=input() # Input uscita
            if "E" in ex or "e" in ex: # Controllo uscita
                h=False # Cambio valore ciclo
                break # Uscita programma
        elif cal=="+": # Controllo selezione +
            print(a,"+",b,"=",a+b) # Print operazione
            print("To exit press E, otherwise press any other value:") # Print uscita
            ex=input() # Input uscita
            if "E" in ex or "e" in ex: # Controllo Uscita
                h=False # cambio valore ciclo
                break # Uscita programma
        elif cal=="-": # Controllo selezione -
            print(a,"-",b,"=",a-b) # Print operazione
            print("To exit press E, otherwise press any other value:") # Print uscita
            ex=input() # Input uscita
            if "E" in ex or "e" in ex: # Controllo uscita
                h=False # Cambio valore ciclo
                break # Uscita programma
        elif cal=="*" or cal=="x" or cal=="X" or cal=="•": # Controllo selezione x
            print(a,"•",b,"=",a*b) # Print operazione
            print("To exit press E, otherwise press any other value:") # Print uscita
            ex=input() # Input uscita
            if "E" in ex or "e" in ex: # Controllo uscita
                h=False # Cambio valore ciclo
                break # Uscita programma
        elif cal==":" or cal=="/": # Controllo selezione :
            print(a,":",b,"=",a/b) # Print operazione
            print("To exit press E, otherwise press any other value:") # Print uscita
            ex=input() # Input uscita
            if "E" in ex or "e" in ex: # Controllo uscita
                h=False # Cambio valore ciclo
                break # Uscita programma
else: # Se selezione è sbagliata
    print("ERROR! Unknown Language\nERRORE! LINGUA SCONOSCIUTA") # Print selezione sbagliata

# WRITTEN BY MARCO LO GIUDICE
# https://github.com/Bordless-ita