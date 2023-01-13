import web

urls = (
    '/', 'Index',
    '/welcome','Welcome'
)

app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()


class Welcome:
    def GET(self):
        return render.welcome()

if __name__ == "__main__":
    app.run()