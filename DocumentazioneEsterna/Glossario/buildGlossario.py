# Script che prende le definizioni scritte in glossario.csv
# e le inserisce all'interno dell'opportuno file LETTERA.tex.
# glossario.csv contiene due parametri (Termine,Definizione) divisi dalla virgola 
# (se nella definizione o nel termine è presenta una virgola, scrivere la frase fra "")

import csv, string

def clean_file():
    for i in string.ascii_uppercase:
        with open("res/Alfabeto/"+i+".tex", "r+") as letter_file:
            letter_file.truncate(0)
            letter_file.write("\section{"+i+"}\n")

def append_to_letter_file(termine,definizione):
    latex_code="\TermineGlossario{"+termine+"}\n\DefinizioneGlossario{"+definizione+"}\n\\\\\n"
    with open("res/Alfabeto/"+termine.split("\\")[-1][0].upper()+".tex", "a") as letter_file:
       letter_file.write(latex_code)

def main():
    clean_file()
    definizioni = sorted(csv.DictReader(open('glossario.csv')), key=lambda termine: termine['Termine'].split("\\")[-1])
    
    for row in definizioni:
        #print for test
        #print(row['Termine']+'\n'+row['Definizione']+'\n\n')
        append_to_letter_file(row['Termine'],row['Definizione'])

main()