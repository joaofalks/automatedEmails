Descrição do Projeto

Este projeto consiste em um script Python que funciona como um lembrete de reunião, enviando um e-mail com o link da reunião. Ele foi projetado para ser usado em conjunto com o Agendador de Tarefas do Windows para automatizar o processo de lembrete de reuniões.

Funcionamento

O script utiliza a biblioteca smtplib para enviar e-mails através de um servidor SMTP. Ele é configurado para enviar um e-mail contendo o link da reunião para os participantes em um horário específico. Os detalhes da reunião, como o link e a hora da reunião, podem ser configurados diretamente no código ou passados como argumentos para o script.

Conexão com o Agendador de Tarefas do Windows

Para automatizar o processo de envio de lembretes de reunião, este script está conectado ao Agendador de Tarefas do Windows. O Agendador é configurado para executar o script em um horário pré-definido, garantindo que os lembretes sejam enviados pontualmente. Isso permite que os usuários configurem e gerenciem facilmente o agendamento de lembretes sem intervenção manual.

Conversão para Executável (.exe)

Para simplificar ainda mais o processo de execução do script, os arquivos .py foram convertidos em executáveis .exe. Isso permite que o script seja executado em qualquer sistema Windows sem a necessidade de ter o Python instalado. A conversão foi realizada utilizando a ferramenta PyInstaller, que empacota o script Python e suas dependências em um único arquivo executável.

Utilização

Para usar este script, basta configurar as variáveis necessárias no código, como o endereço de e-mail do remetente, o servidor SMTP e as informações da reunião. Em seguida, configure o Agendador de Tarefas do Windows para executar o script no horário desejado.
