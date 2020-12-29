# Script che prende le definizioni scritte in glossario.csv
# e le inserisce all'interno dell'opportuno file LETTERA.tex.
# glossario.csv contiene due parametri (Termine,Definizione) divisi dalla virgola (se nella definizione o nel termine è presenta una virgola, scrivere la frase fra "")

import csv

def append_to_letter_file(termine,definizione):
    latex_code="\TermineGlossario{"+termine+"}\n\DefinizioneGlossario{"+definizione+"}\\\\\n\n"
    with open("res/Alfabeto/"+termine[0].upper()+".tex", "a") as letter_file:
       letter_file.write(latex_code)

def main():
    definizioni = csv.DictReader(open('glossario.csv'))
    for row in definizioni:
        append_to_letter_file(row['Termine'],row['Definizione'])

main()