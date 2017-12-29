#Python 2.7

import serial
import time

conexao = serial.Serial('COM3', 9600)
print('Acender o LED')
if conexao.isOpen() == True:
    def tempoL():
        time.sleep(1)
        conexao.write('1')
    def tempoD():
        time.sleep(1)
        conexao.write('2')
    while True:
        tempoL()
        tempoD()
else:
    print('Não Funcionou')
        
    
