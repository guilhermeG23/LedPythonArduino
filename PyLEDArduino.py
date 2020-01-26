#Python 2.7

import serial
import time

conexao = serial.Serial('COM6', 9600)

print('Acender o LED')
if conexao.isOpen() == True:
    def tempoL():
        time.sleep(1)
        conexao.write(str(1))
    def tempoD():
        time.sleep(1)
        conexao.write(str(2))
    while True:
        tempoL()
        tempoD()
else:
    print('Nao Funcionou')
        
    
