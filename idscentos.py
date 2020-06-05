import os
a=0
while a!=4:
	print('--------------------INSTALL & CONFIG SURICATA---------------------\n 1 - install Suricada IDS\n 2 - config Suricata IDS\n 3 - show log-file\n 4 - exit\n')
	a=int(input('Enter your choise > '))
	if a==1:
		os.system('yum -y install epel-release')
		os.system('yum -y install jq cargo openssl-devel PyYAML lz4-devel gcc libpcap-devel pcre-devel libyaml-devel file-devel zlib-devel jansson-devel nss-devel libcap-ng-devel libnet-devel tar make libnetfilter_queue-devel lua-devel')
		os.system('wget https://www.openinfosecfoundation.org/download/suricata-4.1.2.tar.gz')
		os.system('tar -xvzf suricata-4.1.2.tar.gz')
		os.chdir('/home/user/suricata-4.1.2')
		os.system('./configure --libdir=/usr/lib64 --prefix=/usr --sysconfdir=/etc --localstatedir=/var --enable-nfqueue --enable-lua --enable-rust')
		os.system('make')
		os.system('sudo make install-full')
	elif a==2:
		print("\n1 - Log HTTP\n2 - Log TLS\n3 - Log DNS\n4 - Log PCAP\n5 - Log Mixed (HTTP, TLS, DNS, PCAP)\n")
		bb=int(input("Answer: "))
		if bb==1:
			os.system("sudo suricata -c /home/user/suricata/http/suricata.yaml -i enp0s3")
		elif bb==2:
			os.system("sudo suricata -c /home/user/suricata/dns/suricata.yaml -i enp0s3")
		elif bb==3:
			os.system("sudo suricata -c /home/user/suricata/tls/suricata.yaml -i enp0s3")
		elif bb==4:
			os.system("sudo suricata -c /home/user/suricata/pcap/suricata.yaml -i enp0s3")
		elif bb==5:
			os.system("sudo suricata -c /home/user/suricata/mixed/suricata.yaml -i enp0s3")
		else:
			print("\nNumber does not exist.\n")
	elif a==3:
		ans=int(input("\n\nChoose your answer:\n1 - Show file http.log\n2 - Show file dns.log\n3 - Show file tls.log\n4 - Show file log.pcap\n5 - Down to main menu\nEnter number >"))
		if ans==1:
			os.system("cat /var/log/suricata/http.log")
		elif ans==2:
			os.system("cat /var/log/suricata/dns.log")
		elif ans==3:
			os.system("cat /var/log/suricata/tls.log")
		elif ans==4:
			os.system("cat /var/log/suricata/log.pcap*")
		elif ans==5:
			print("\n")
		else:
			print("\nNumber does not exist.\n")
				
	elif a==4:
		print('\n[X] EXIT of main menu. \nGoodbye.\n')
		break
	else:
		print('Number does not exist.')
else:
	print('Number does not exist.')
