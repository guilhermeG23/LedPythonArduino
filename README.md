# LedPythonArduino

### Utilizado

* Python 2.7 ou 3(Depende mais do que você utiliza)
* Arduino IDE
* Lib do python: Pyserial

### Link

Vi num tutorial e resolvi duplicar e testar um timer

Link: http://www.potilivre.org/hudsonbrendon/383-controlando-o-arduino-com-python

### Para fazer funcionar:

* Monte o arduino com o led ligado na porta 13 e no GND(Pé maior do led na porta 13)
* Grave o script arduino no equipamento
* Instale as libs no Python 2 ou 3(depende de você)
* Execute o python

### Teste 

* No linux a porta COM3 é outra, tem que procurar qual é a porta, você tem que procurar onde o arduino é montado
* Montado a porta: conexao = serial.Serial('COM3', 9600)
* Para garantir que a conexao funciona use o comando: conexao.isOpen(), se sair um True de resultado, está funcionando
* Para fazer acender ou apagar, só altere os valores aqui: conexao.write('1')