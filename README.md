# LedPythonArduino
Python 2.7

#Vi num tutorial e resolvi duplicar e testar um timer
Link Tutorial: http://www.potilivre.org/hudsonbrendon/383-controlando-o-arduino-com-python

Pra fazer funcionar
#Teste no Windows

Instale um Python 2.7
https://www.python.org/downloads/release/python-2714/

Adicione a biblioteca pyserial
https://pypi.python.org/pypi/pyserial/2.7
#Instale o que preferir

Com isso pronto para testar:

#Para fazer o arduino estar no ponto de bala, conecte um LED na porta GND e 13, sendo o 'Pé' maior no 13

Execute o script arduino Uno na sua IDE e pronto(Grave no Arduino):

#Agora vamos para o Python 2.7
Teste assim:

#No linux a porta COM3 é outra, tem que procurar qual é a porta
-import serial
-conexao = serial.Serial('COM3', 9600)

#Para garantir que a conexao funciona teste
-conexao.isOpen()
#Se der True que dizer que ta certo

#Para fazer o LED acender use:
-conexao.write('1')
#Para apagar o LED:
-conexao.write('2')

#Agora só brincar