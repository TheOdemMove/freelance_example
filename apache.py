import os
x=0
while x!=6:
	print('***************************Hello user!************************\n\t\t Install Apache - press [1]\n\t\t Configure Apache - press [2]\n\t\t Open local page  - press [3]\n\t\t Show status Apache - press [4]\n\t\t Remove Apache- press [5]\n\t\t Close - press [6] \n***************************************************************')
	x=int(input('\t\tYour choise '))
	if x==1:
		os.system('apt-get update')
		os.system('apt-get install apache2')
	elif x==2:
		y=0
		while y!=4:
			print('**********************Cofiguration Apache**************\n\t\t\n[1] - Create Web-page and VirtualHost\n[2] - Edit web-page\n[3] - Delete web-page and VirtualHost\n[4] - List web-site\n[5] - Close menu')
			y=int(input('\nYour choise: '))
			if y==1:
				print("\nDear user, enter your main (first) group to answer.\nList groups your user show down:\n")
				os.system("groups")
				ans=str(input("\nEnter group: "))
				os.system("sudo usermod -a -G %s www-data" % ans)
				os.chdir("/home")
				if not os.path.exists("www"): os.mkdir("www")
				os.chdir("/home/www")
				names=str(input("\nEnter DNS your future site: "))
				os.mkdir("%s" % names)
				os.chdir("%s" % names)
				os.system("echo 'Hello world' > index.html")
				os.system("sudo chmod -R 777 /home/www")
				os.chdir("/home/www")
				if not os.path.exists("logs"): os.mkdir("logs")
				os.system("sudo chmod 775 logs")
				os.chdir("/etc/apache2/sites-available")
				os.system("cp 000-default.conf %s.conf" % names)
				f1 = open("%s.conf" % names, "w")
				f1.write("<VirtualHost *:80>\nServerAdmin test@mail\nServerName %s\nServerAlias www.%s\nDocumentRoot /home/www/%s\nErrorLog /home/www/logs/%s.error.log\nCustomLog /home/www/logs/%s.accsess.log combined\n<Directory /home/www/%s>\nOptions Indexes FollowSymLinks MultiViews\nAllowOverride All\nRequire all granted\n</Directory>\n</VirtualHost>\n" % (names, names, names, names, names, names))
				f1.close()
				os.system("echo '127.0.0.1 %s' >> /etc/hosts" % names)
				os.system("sudo a2ensite %s" % names)
				os.system("sudo systemctl reload apache2")
				print("\n\nYour web-site: %s\nSuccsesful created.\n\n" % names)
			elif y==2:
				ans2=str(input("\n\nEnter DNS your web site: "))
				os.system("nano /home/www/%s/index.html" % ans2)
			elif y==3:
				ans3=str(input("\nEnter DNS your web-site: "))
				os.system("sudo a2dissite %s" % ans3)
				os.system("rm -rf /home/www/%s" % ans3)
				os.system("rm -rf /etc/apache2/site-available/%s.conf" % ans3)
				os.system("sudo systemctl reload apache2")
				print("Web-site: %s\nWas removed.\n" % ans3)
			elif y==4: 
				print("\nList web-site:\n")
				os.system("ls /home/www")			
			elif y==5:
				print('\t\tOK')
				break

			else:
				print('\t\t------Incorrect!!!---------')
	elif x==3:
		print ("\t\t For exit print 'Q'")
		s=input('\t\t Press ENTER')
		os.system('apt install links')
		os.system('links 127.0.0.1')
	elif x==4:
		os.system('systemctl status apache2')	
	elif x==5:
		os.system('apt-get purge apache2')
	elif x==6:
		print('\t\tOKAY')
		break
	else:
		print('\t\t------Incorrect!!!---------')

