#!/bash/bin
#para rodar o script eh so fazer no terminal o comando:
#bash scriptInitial.sh
#nisso as rotas e ativacao do multicast sao feitas

#link legal: https://alexandrebbarbosa.wordpress.com/2014/09/27/configurando-uma-interface-de-rede-no-linux/

sudo ifconfig eth0 multicast
sudo route -n add -net 224.0.0.0 netmask 240.0.0.0 dev eth0

echo -e 'Multicast ativado e rota adicionada!\nPronto para uso! =)'
#inicar o send em uma maquina e o recive nas outras

#script para iniciar a configuracao do multicast
