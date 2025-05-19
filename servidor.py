from flask import *

#instanciador do servidor
app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("index.html")

@app.route("/sugestao", methods=["POST", "GET"])
def receber_sugestao():
    #METODO GET
    sugestao = request.values.get("sugestao")

    #METODO POST
    sugestao = request.form.get("sugestao")

    print(sugestao)
    return render_template("pagina_de_sugestao.html")

@app.route("/informacoes_usuario", methods=["POST"])
def receber_informacoes_usuario():
    nome_usuario = request.form.get("nome_usuario")
    peso_usuario = request.form.get("peso_usuario")
    idade_usuario = request.form.get("idade_usuario")
    return render_template("index.html")

@app.route("/curriculo", methods=["POST"])
def mostrar_curriculo():
    return render_template("curriculo-lattes.html")
app.run()