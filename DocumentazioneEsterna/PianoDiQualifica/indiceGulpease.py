# Script che calcola l'indice di Gulpease di un pdf

import textract, re, sys

def indiceGulpease(parole,lettere,frasi):
    indiceG=int(89+((300*frasi)-(10*lettere))/parole)
    return 100 if indiceG > 100 else indiceG
    
def main():
    if len(sys.argv) > 1:
        pdf=str(sys.argv[1])

        text = textract.process(pdf, method='pdftotext', encoding='utf-8')
        #print(text.decode('utf-8'))

        parole = len(re.findall(r'[^\W_]+', str(text)))
        lettere = len(re.findall(r'[^\W_]', str(text)))
        frasi = len(re.findall('[.]+\s',  str(text)))+len(re.findall('[;]+\s',  str(text))) - len(re.findall('[.]+\s+[.]',  str(text)))

        print("File "+pdf.split("/")[-1])
        print(f"Numero di parole presenti nel documento: {parole}")
        print(f"Numero di lettere presenti nel documento: {lettere}")
        print(f"Numero di frasi presenti nel documento: {frasi}")
        print(f"Indice di Gulpease: {indiceGulpease(parole,lettere,frasi)}")

    else:
        raise "Argomento non passato dalla linea di comando."
    
main()