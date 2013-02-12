#!/usr/bin/python
#
# Script feito para migracao interna de contas do cpanel
# ele realiza os mesmos procedimentos manuais, porem automatizados usando o modulo pexpect
#
# Qualquer bug ou duvida na utilizacao podem me perguntar (:
#
# Feito por Alisson Menezes - alisson.copyleft@gmail.com
# Github: https://github.com/kernelcrash
#

import os
import pexpect


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
passwd = "3u0d310tr0c4rS3nh4@#"

for c in contas:
	script = '''
	if [ -f /home/*'''+c+'''.tar.gz ]; then
        	echo "esta no home"
	elif [ -f /home2/*'''+c+'''.tar.gz ]; then
        	echo "ta no home2
	else
	        echo "'''+c+''' ta no home3"
	fi

	'''
	try:
		print "######## GERANDO ARQUIVO FULLBACKUP #############"
		p = pexpect.spawn("ssh root@"+origem+" /scripts/pkgacct-disable "+c)
		p.waitnoecho()
		#child.expect('Password:')
		p.sendline(passwd)
		p.sendline("exit")
		p.interact()
	except Exception, e:
		print e
	try:
		print "###### COPIANDO ARQUIVO ###########"
		try:
			p = pexpect.spawn("scp root@"+origem+":/home/*"+c+".tar.gz root@"+destino+":/home/")
			p.waitnoecho()
	                #child.expect('Password:')
        	        p.sendline(passwd)
                	p.sendline("exit")
	                p.interact()
		except Exception, e:
			print e
			try:
				p = pexpect.spawn("scp root@"+origem+":/home2/*"+c+".tar.gz root@"+destino+":/home/")
				p.waitnoecho()
                		#child.expect('Password:')
                		p.sendline(passwd)
                		p.sendline("exit")
                		p.interact()
			except Exception, e:
				print e
				print "###### O arquivo nao existe ###################"
	except Exception, e:
		print "ERRO ",e
	try:
		print "############ RESTAURANDO ARQUIVO ##################"
		p = pexpect.spawn("ssh root@"+destino+" /scripts/restorepkg /home/*"+c+".tar.gz")
		p.waitnoecho()
                #child.expect('Password:')
                p.sendline(passwd)
                p.sendline("exit")
                p.interact()

	except Exception, e:
		print "ERRO ",e


# PARTE EM SHELL DA ANTIGA VERSAO, SUBSTITUIDA PELO PEXPECT
#	try:
#		os.system("./auto.sh criar %s %s %s "% (c, origem, destino))
#	except Exception, e:
#		print "erro -> ",e
#		continue
#	try:
#		os.system("./auto.sh copiar %s %s %s "% (c, origem, destino))
#	except Exception, e:
#		print "erro -> ",e
#	try: 
#		os.system("./auto.sh restaurar %s %s %s "% (c, origem, destino))
#	except Exception, e:
#		print "erro -> ",e

print "\n\n\n\nMIGRACAO FINALIZADA!"
