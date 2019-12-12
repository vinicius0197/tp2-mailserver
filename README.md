## Configurações
É necessário usar o `Python 3.5` no servidor de email.

O servidor está configurado para rodar na porta 1025 do `localhost`. Esse é um servidor
de e-mail bastante simples, que recebe e-mails e guarda dentro da pasta `emails/`. Não
há nenhum tipo de autenticação implementado, mas os e-mails são organizados em pastas
diferentes para cada destinatário, e os e-mails individuais são salvos em arquivos
do tipo `.eml`, que podem ser lidos em clientes de e-mails como Outlook e Thunderbird.

### Rodando o servidor
O servidor pode ser rodado com o seguinte comando:

```
  python3.5 mailserver.py
```

(obs: é importante especificar a versão 3.5 do Python para que o servidor funcione)

### Cliente de E-mail
Há um cliente de e-mail muito simples configurado dentro da pasta `src/Client/client.py`. Ele 
pode ser usado para testar o servidor de e-mail. O programa pode ser rodado utilizando o seguinte
comando:

```
  python3 client.py
```

O client iniciará uma comunicação com o servidor de e-mail e enviará uma mensagem de e-mail pré-configurada.
Se o e-mail for enviado com sucesso via protocolo SMTP, então o seu terminal irá receber uma mensagem
do seguinte formato:

```
send: 'ehlo [127.0.1.1]\r\n'
reply: b'250-vinicius\r\n'
reply: b'250-SIZE 33554432\r\n'
reply: b'250 HELP\r\n'
reply: retcode (250); Msg: b'vinicius\nSIZE 33554432\nHELP'
send: 'mail FROM:<mary@email.com> size=204\r\n'
reply: b'250 OK\r\n'
reply: retcode (250); Msg: b'OK'
send: 'rcpt TO:<carlos@email.com>\r\n'
reply: b'250 OK\r\n'
reply: retcode (250); Msg: b'OK'
send: 'data\r\n'
reply: b'354 End data with <CR><LF>.<CR><LF>\r\n'
reply: retcode (354); Msg: b'End data with <CR><LF>.<CR><LF>'
data: (354, b'End data with <CR><LF>.<CR><LF>')
send: b'Content-Type: text/plain; charset="us-ascii"\r\nMIME-Version: 1.0\r\nContent-Transfer-Encoding: 7bit\r\nTo: Carlos <carlos@email.com>\r\nFrom: Mary <mary@email.com>\r\nSubject: this is a test\r\n\r\nthis is the message\r\n.\r\n'
reply: b'250 OK\r\n'
reply: retcode (250); Msg: b'OK'
data: (250, b'OK')
send: 'quit\r\n'
reply: b'221 Bye\r\n'
reply: retcode (221); Msg: b'Bye'

```


### Rodando os testes
Há uma série de testes unitários dentro da pasta `tests/`. Esses testes foram escritos utilizando
a biblioteca `unittest` padrão do Python, e podem ser rodados através do seguinte comando:

```
  python3.5 -m unittest -v tests/output_tests.py
```