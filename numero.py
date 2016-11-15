# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, random
app = Flask(__name__)
 
# el decorator (@) estableix la ruta (URL). A mes, activem el mètode POST
@app.route("/numero", methods=["GET","POST"])
def adivinarNumero():
    # inicialitzem missatge
    miss = "No has enviat cap numero"
    if request.method == "POST":
        # si entrem aquí és que ja hem enviat alguna dada del formulari (POST)
        envnumero = request.form["num"]
        numero = random.randint(1, 20)
        while intentosRealizados < 6:
			
			print('Intenta adivinar el número:')
			estimacion = input()
			estimacion = int(estimacion)
			intentosRealizados = intentosRealizados + 1
			
			if estimacion == numero:
				break
			if estimacion < numero:
				print('Tu estimación es muy baja.')
			if estimacion > numero:
				print('Tu estimación es muy alta.')
			
		if estimacion == numero:
			intentosRealizados = str(intentosRealizados)
			print ('¡Buen trabajo! Has adivinado el número'+intentosRealizados+'intentos!')
		if estimacion != numero:
			numero = str(numero)
		print ('El número que estaba pensando era'+numero)	
		
		#renderitzem el template amb el missatge pertinent
		return render_template ('numero.html',missatge=miss)
		
		if __name__ == "__main__":
			app.run()
