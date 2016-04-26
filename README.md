## DNSchecker

Simple python script that shows DNS information from a Domain or Subdomain.
   - Start of Authority
   - DNS Servers
   - Check DNS Zone transfer
   - Mail Servers
   - Online IP Reputation
   - IP & Domain Whois

```
$ python3 DNSchecker.py tsxx.com
[ ]   DNS Domain Checker   
[ ]   belane 2016   
[ ] --------------------------
[i]  Domain 
[+]  tsxx.com
[+]  199.8.34.2
[ ] --------------------------
[ ] 
[i]  SOA for tsxx.com 
[+]  ns3.isoc.net.
[ ] 
[i]  Name Servers for tsxx.com 
[+]  ns4.isoc.net.
[+]  ns3.isoc.net.
[ ] 
[i]  Checking DNS Zone Transfer for tsxx.com 
[+]  DNS Transfer from ns4.isoc.net. 
[+]   @ 	3600 	IN 	SOA 	ns3.isoc.net. 	anthony\.mullins.tsxxtech.com. 	19689 14400 7200 2419200 3600 
[+]   @ 	3600 	IN 	NS 	ns3.isoc.net. 
[+]   @ 	3600 	IN 	NS 	ns4.isoc.net. 
[+]   @ 	3600 	IN 	A 	199.8.34.2 
[+]   @ 	3600 	IN 	MX 	0 	mail.tsxxtechnologies.com. 
[+]   ftp 	3600 	IN 	CNAME 	@ 
[+]   stage 	3600 	IN 	A 	199.8.34.2 
[+]   www 	3600 	IN 	CNAME 	@ 
[+]  DNS Transfer from ns3.isoc.net. 
[+]   @ 	3600 	IN 	SOA 	ns3.isoc.net. 	anthony\.mullins.tsxxtech.com. 	19689 14400 7200 2419200 3600 
[+]   @ 	3600 	IN 	MX 	0 	mail.tsxxtechnologies.com. 
[+]   @ 	3600 	IN 	A 	199.8.34.2 
[+]   @ 	3600 	IN 	NS 	ns3.isoc.net. 
[+]   @ 	3600 	IN 	NS 	ns4.isoc.net. 
[+]   ftp 	3600 	IN 	CNAME 	@ 
[+]   stage 	3600 	IN 	A 	199.8.34.2 
[+]   www 	3600 	IN 	CNAME 	@ 
[ ] 
[i]  MX Registers for tsxx.com 
[+]  mail.tsxxtechnologies.com.
[ ] 
[i]  Checking IP Reputation for 199.8.34.2 tsxx.com 
[+]  Bad IP Reputation -> Spam Bot masking himself as a normal user on 24 April 2016
[ ] 
[i]  Whois for 199.8.34.2 
[+]   JCM Consulting JCMCO (NET-199-8-34-0-1) 199.8.34.0 - 199.8.34.255 
[+]   Internet Access Cincinnati NETBLK-IAC-CBLK1 (NET-199-8-32-0-1) 199.8.32.0 - 199.8.63.255 
[ ] 
[i]  Whois for tsxx.com 
[+]      Domain Name: TSXX.COM 
[+]      Registrar: NETWORK SOLUTIONS, LLC. 
[+]      Sponsoring Registrar IANA ID: 2 
[+]      Whois Server: whois.networksolutions.com 
[+]      Referral URL: http://networksolutions.com 
[+]      Name Server: NS3.ISOC.NET 
[+]      Name Server: NS4.ISOC.NET 
[+]      Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited 
[+]      Updated Date: 29-nov-2012 
[+]      Creation Date: 17-mar-1997 
[+]      Expiration Date: 18-mar-2018 
[ ] 
[ ] done!
```

