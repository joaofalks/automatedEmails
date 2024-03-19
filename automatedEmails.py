import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'remetente@gmail.com'
smtp_password = 'senha de app do remetente'

# Informações do e-mail
sender_email = 'remetente@gmail.com'
receiver_email = 'destinatario@gmail.com'
subject = 'Título do E-mail'
message = 'Olá,\n\nEsta é uma lembrança para a nossa reunião de equipe. Por favor, junte-se a nós no Microsoft Teams usando o seguinte link:\n\nLINK_DA_REUNIAO\n\nObrigado,\nSua Equipe'

# Configuração do e-mail
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Conectando-se ao servidor SMTP e enviando e-mail
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar e-mail: {str(e)}')
