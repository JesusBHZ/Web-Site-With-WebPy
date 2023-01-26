import web

urls = (
    '/', 'Index'
    )

render = web.template.render('templates',base='layout')
app = web.application(urls, globals())


class Index:
    def GET(self):
        datos = [
            ["1","Dejah"],
            ["2","Jhon"],
        ]
        return render.tablas(datos)
    

if __name__ == "__main__":
    #web.config.debug = False
    app.run()