   
#!/bin/bash
# Parte do script de automatizacao da migracao interna
# este script faz a parte de conexao via ssh automatizando os processos
#
# Feito por Alisson Menezes - alisson.copyleft@gmail.com
# Github: https://github.com/kernelcrash
 
 
if [ $# -lt 1 ]; then
        clear
        echo "###############################################################################"
        echo "Script para migracao interna de contas do cpanel"
        echo "feito por Alisson Menezes - alisson.copyleft@gmail.com"
        echo "Github: https://github.com/kernelcrash"
        echo "###############################################################################"
        echo "O script foi desenvolvido no para ser usado como modulo do migracao.py"
        echo "#################################################################################"
        echo "Uso do script:"
        echo "Argumentos: funcao login_cpanel origem destino"
        echo "Ex:"
        echo "./auto.sh criar alisson servidor1.net servidor2.net"
        echo "./auto.sh copiar alisson servidor1.net servidor2.net"
        echo "./auto.sh restaurar alisson servidor.net servidor2.net"
        echo "Essas sao todas as funcoes"
        exit 1
fi
 
 
senha="SENHA_DO_SERVIDOR_AQUI"
 
 
if [ $1 ==  "criar" ]; then
        expect -c "spawn ssh root@$3 /scripts/pkgacct $2 ; expect password; send \"$senha\n\" ; interact ;"
 
elif [ $1 == "copiar" ] ; then
        echo "escolheu copiar backup ";
        expect -c "spawn scp root@$3:/home/*$2*.tar.gz root@$4:/home ; expect password; send \"$senha\n\" ; interact ;"
 
elif [ $1 == "restaurar" ]; then
        echo "escolhe restaurar backup";
        expect -c "spawn ssh root@$4 /scripts/restorepkg /home/cpmove-$2.tar.gz ; expect password; send \"$senha\n\" ; interact ;"
else
        echo "nenhuma das opcoes"
fi
