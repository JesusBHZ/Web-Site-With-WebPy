import web

urls = (
    '/', 'numeros',
    '/add', 'add'
)

app = web.application(urls, globals())
render = web.template.render('templates')

class numeros:
    def GET(self):
        return render.numeros()

    def POST(self):
        numeros = dict(web.input())
        
        if(len(numeros["n1"])!=0 and len(numeros["n2"])!=0):
            if(numeros["n1"].isdigit() and numeros["n2"].isdigit()):
                if (numeros["suma"] == "Sumar"):
                    suma = int(numeros["n1"]) + int(numeros["n2"])
                    respuesta = "La suma de %s + %i es %f" %(int(numeros["n1"]), int(numeros["n2"]), suma)
                elif (numeros["suma"] == "Restar"):
                    resta = int(numeros["n1"]) - int(numeros["n2"])
                    respuesta = "La resta de %s - %i es %f" %(int(numeros["n1"]), int(numeros["n2"]), resta)
                elif(numeros["suma"] == "Multiplicar"):
                    multiplicacion = int(numeros["n1"]) * int(numeros["n2"])
                    respuesta = "La multiplicacion de %s * %i es %f" %(int(numeros["n1"]), int(numeros["n2"]), multiplicacion)
                elif (numeros["suma"] == "Dividir"):
                    divicion = int(numeros["n1"]) / int(numeros["n2"])
                    respuesta = "La divicion de %s / %i es %f" %(int(numeros["n1"]), int(numeros["n2"]), divicion)
            else:
                respuesta = "Los valores deben ser numeros"
        else:
            respuesta = "Los valores no deben estar vacios"

        return respuesta
        
    

if __name__ == "__main__":
    web.config.debug = False
    app.run()