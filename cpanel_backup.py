#!/usr/bin/python

# Transfere fullbackup por ftp cpanel
#
# Feito por Alisson Menezes - GR1L0S3C0 - culturadocaracter.com.br
#
# Data: 12/10/2012
#
# Agradecimentos - Herderson Boechat - Guilherme Chagas - Thiago Siqueira - Walter Augusto - Andre Zarlenga - Alex Moreno - Talliny Dalla Nora - Gustavo Kishima - Liliane Alves - Leandro Santos
# e principalmente ao google.com.br
#-------------------------------------------------------------------------------------------

import urllib
import urllib2
import base64
import sys
import time


#x01 - dados do servidor de ftp
ftpuser = "usuario_ftp"
ftppass = "senha_ftp"
ftphost = "servidor_ftp"
ftpmode = "ftp" 
ftpport = "21"
ftprdir = '/'
email = "seu_email"
#--------------------------------

senha = ""
host = ""

def acessa_cpanel(conta):
        req = urllib2.Request('https://'+host+':2083/frontend/x3/backup/dofullbackup.html?'+"dest="+ftpmode+"&email="+email+"&server="+ftphost+"&user="+ftpuser+"&pass="+ftppass+"&port="+ftpport+"&rdir="+ftprdir+"&submit=Generate Backup")
        base64string = base64.encodestring('%s:%s' % (conta, senha))[:-1]
        authheader =  "Basic %s" % base64string
        req.add_header("Authorization", authheader)
        try:
            print 'Acessando: '+conta
            handle = urllib2.urlopen(req)
            handle.read() #lol
	    print 'host -> '+host
            print 'Acessou com sucesso!'
            print 'Enviando por ftp'
        except IOError, e:
	    print 'erro -> ',e 
            print "Login Falhou, Por favor verifique os dados de acesso."
            sys.exit(1)


banner = """
Script que envia backups do CPanel por ftp

Feito por Alisson Menezes - GR1L0S3C0 - culturadocaracter.com.br

################################################################

Edite os dados do seu servidor de FTP dentro do script:

################################################################



Se a senha tiver caracteres especiais coloque entre aspas ""

Uso:

python backup_ftp.py ip_do_host login senha

Ex:

python backup_ftp.py 191.168.0.2 conta1 "!@!23axc"


"""


print banner


if __name__ == "__main__":
	try:	
		args = sys.argv
		for a in args:
			print a
		host = args[1]
		senha = args[3]
		acessa_cpanel(args[2])
		print 'agora verifique se chegou no seu ftp, a transferencia demora algum tempo dependendo do tamanho do arquivo'
	except:
		if len(args) < 3 :
			print banner
