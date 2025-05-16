from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg in ['oi', 'olá', 'menu', 'início', 'inicio']:
        menu = (
            "👋 Olá! Bem-vindo ao Chatbot do Departamento de Computação.\n\n"
            "Digite o número da opção desejada:\n"
            "1️⃣ Data das provas e feriados\n"
            "2️⃣ Informações sobre Estágio\n"
            "3️⃣ Atividades complementares\n"
            "4️⃣ XV Semana de Computação\n"
            "5️⃣ Sair"
        )
        msg.body(menu)

    elif incoming_msg == '1':
        msg.body("📚 As datas das provas e feriados estão no calendário acadêmico:\nhttps://www.unifacef.com.br/wp-content/uploads/2025/02/calendario_academico_unifacef_2025-.pdf")

    elif incoming_msg == '2':
        msg.body("💼 O estágio obrigatório começa a partir do 5º semestre. Veja detalhes em:\nhttps://www.unifacef.com.br/centro-de-carreiras/estagios-supervisionados/")

    elif incoming_msg == '3':
        msg.body("🧾 Os certificados de atividades complementares devem ser enviados para daniel@facef.br, totalizando no mínimo 140 horas.")

    elif incoming_msg == '4':
        msg.body("🎓 As palestras e minicursos da XV Semana de Computação estão disponíveis em:\nhttps://eventos.unifacef.com.br/fem/2025/site/programacao#347")

    elif incoming_msg == '5':
        msg.body("👋 Até logo! Se precisar, é só chamar digitando 'menu'.")

    else:
        msg.body("❌ Opção inválida. Por favor, digite 'menu' para ver as opções disponíveis.")

    return str(resp)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)