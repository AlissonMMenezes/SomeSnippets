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
import cgi

print "Content-type: text/html\n\n";

#x01 - dados do servidor de ftp
ftpuser = "ftp_user"
ftppass = "senha_de_ftp"
ftphost = "host_ftp"
ftpmode = "ftp" 
ftpport = "21"
ftprdir = '/'
email = "email de notificacao"
#--------------------------------

form = cgi.FieldStorage()
senha = form.getvalue('senha').strip()
host = form.getvalue('rserver').strip()
ssl = form.getvalue('ssl')
protocolo = 'http'
porta = '2082'
contas = []
cont = form.getvalue('contas')
for c in cont.split('\n'):
	contas.append(c.strip())

if ssl == 'ssl':
	protocolo = 'https'
	porta = '2083'


def acessa_cpanel(conta):
        req = urllib2.Request(protocolo+'://'+host+':'+porta+'/frontend/x3/backup/dofullbackup.html?'+"dest="+ftpmode+"&email="+email+"&server="+ftphost+"&user="+ftpuser+"&pass="+ftppass+"&port="+ftpport+"&rdir="+ftprdir+"&submit=Generate Backup")
        base64string = base64.encodestring('%s:%s' % (conta, senha))[:-1]
        authheader =  "Basic %s" % base64string
        req.add_header("Authorization", authheader)
        try:
            print 'Acessando: '+conta
            handle = urllib2.urlopen(req)
            handle.read() #lol
	    print 'host -> '+host
            print 'Acessou com sucesso!'
            print 'Enviando por ftp<br>'
        except IOError, e:
	    print 'erro -> ',e 
            print "Login Falhou, Por favor verifique os dados de acesso.<br>"
            #sys.exit(1)


if __name__ == "__main__":
	try:	
		print 'senha -> '+senha+'<br>'
		print 'host -> '+host+'<br>' 
		for c in contas:
			acessa_cpanel(c)

		print '<br>voce pode acompanhar o recebimento dos arquivos usando o comando <b>while ( du -h *.tar.gz ); do sleep 1; clear; done </b>no diretorio do ftp - obs. o comando so funciona se ja existir pelo menos um .tar.gz no diretorio'
	except Exception, e:
		print e
