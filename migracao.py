#!/usr/bin/python
#
# Inicio do programa de migracao interna esta parte e onde o usuario entra com os dados
# faz o tratamento de erros chamando o shell script para utilizacao de ssh
#
# Feito por Alisson Menezes - alisson.copyleft@gmail.com
# Github: https://github.com/kernelcrash
#
 
import os
 
print '''
###############################################################################
Script para migracao interna de contas do cpanel
feito por Alisson Menezes - alisson.copyleft@gmail.com
Github: https://github.com/kernelcrash
 
###############################################################################
 
Este script e a parte principal da migricao, onde voce entra com todas as contas
separadas por <enter> ao terminar de colar as contas e necessario apertar um enter vazio
feito isso o script vai pedir os servidores de origem e destino
 
A senha dos servidores deve ser adicionada no arquivo auto.sh na variavel senha
 
#################################################################################
'''
 
 
print "entre com as contas uma abaixo da outra"
 
var = ""
 
while True:
        line = raw_input()
        if not line: break
        var += line+"\n"
 
contas = []
for c in var.strip().split("\n"):
        contas.append(c)
origem = raw_input("digite o servidor de origem: ").strip()
destino = raw_input("digite o servidor destino: ").strip()
 
 
print "==================================================="
print "###     Iniciando migracao de "+origem+"  ###"
print "##      para "+destino+"                  ###"
print "==================================================="
 
os.system("sleep 1")
os.system("echo \n\n\n")
 
for c in contas:
        try:
                os.system("./auto.sh criar %s %s %s "% (c, origem, destino))
        except Exception, e:
                print "erro -> ",e
                continue
        try:
                os.system("./auto.sh copiar %s %s %s "% (c, origem, destino))
        except Exception, e:
                print "erro -> ",e
        try:
                os.system("./auto.sh restaurar %s %s %s "% (c, origem, destino))
        except Exception, e:
                print "erro -> ",e
 
print "\n\n\n\nMIGRACAO FINALIZADA!"
