#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# DNS Checker in Python - belane 2016
# Show DNS information from a domain or subdomain
#
#   - Start of Authority
#   - DNS Servers
#   - Check DNS Zone transfer
#   - Mail Servers
#   - Online IP Reputation
#   - IP & Domain Whois
#

import dns.resolver # pip3 install dnspython3
import dns.query
import dns.zone
import socket
import re
import urllib.request
import sys

class color:
    ''' Class for terminal colors'''
    RESET = '\033[0m'
    BOLD = '\033[1m'
    BLUE = '\033[94m'
    GREY = '\033[90m'
    RED = '\033[91m'
    PURPLE = '\033[95m'

class host:
    ''' Class for Host dns information '''
    NameServers = []
    MailServers = []

    def __init__(self, domain):
        self.domain = domain
        self.ip = socket.gethostbyname(domain)
        if len(self.domain.split(".")) > 2:
            self.rootdomain = host(str(self.domain.split(".")[-2]+"."+self.domain.split(".")[-1]))

    def get_dns_register(self, type):
        ''' Method for dns querys '''
        try:
            return dns.resolver.query(self.domain, type)
        except:
            return False

    def get_MX(self):
        ''' Method to get and print MX servers'''
        answers = self.get_dns_register("MX")
        for r in answers:
            print("[+] ", str(r.exchange))
            self.MailServers.append(str(r.exchange))

    def get_SOA(self):
        ''' Method to print Start of Authority'''
        soa_answer = self.get_dns_register("SOA")
        print("[+] ", soa_answer[0].mname)

    def get_NS(self):
        ''' Method to get and print DNS servers'''
        ns_answer = self.get_dns_register("NS")
        for r in ns_answer:
            print("[+] ", str(r.target))
            self.NameServers.append(str(r.target))

    def get_WhoisIP(self):
        ''' Method to print IP Whois'''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("whois.arin.net", 43))
        s.send((self.ip + "\r\n").encode())
        response = b""
        while True:
            data = s.recv(4096)
            response += data
            if not data:
                break
        s.close()
        pattern = re.compile("^[A-Z].*")
        for line in (response.decode().split("\n")):
            if pattern.match(line):
                print("[+] ",color.GREY, line, color.RESET)

    def get_Whois(self):
        ''' Method to print domain whois'''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("whois.verisign-grs.com", 43))
        s.send(("="+self.domain + "\r\n").encode())
        response = b""
        while True:
            data = s.recv(4096)
            response += data
            if not data:
                break
        s.close()
        pattern = re.compile("^ +[A-Z].*")
        for line in (response.decode().split("\n")):
            if pattern.match(line):
                print("[+] ",color.GREY, line, color.RESET)

    def check_ZoneTransfer(self):
        ''' Method to check and print DNS Zone Transfers'''
        for ns in self.NameServers:
            try:
                z = dns.zone.from_xfr(dns.query.xfr(ns,self.domain))
                print("[+]",color.RED,"DNS Transfer from", ns, color.RESET)
                names = z.nodes.keys()
                for n in names:
                    line = z[n].to_text(n).split("\n")
                    for l in line:
                        print("[+] ", color.GREY, l.replace(" "," \t"), color.RESET)
            except:
                print("[+]  NO zone transfer from", ns)

    def check_Reputation(self):
        ''' Method to check online IP reputation'''
        page = urllib.request.urlopen('http://blacklist.myip.ms/'+self.ip)
        response = page.read()
        page.close()
        pattern = re.compile("Listed in Myip.ms Blacklist .*\((.*)\)")
        if pattern.search(response.decode()):
            print("[+]",color.RED,"Bad IP Reputation ->", re.search(pattern, response.decode()).group(1),color.RESET)
        else:
            print("[+]  Good IP Reputation")

# MAIN
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[i] Show dns information from Host\n[ ] ")
        print("[!] Syntax error.\n[i]  use:\n[+]",color.BOLD,"python3",sys.argv[0],"<domain|subdomain>", color.RESET)
        exit()
    try:
        g1 = host(str(sys.argv[1]))
    except:
        print("[i] Show dns information from Host\n[ ] ")
        print("[!] Domain not found")
        exit()

    print("[ ]",color.PURPLE," DNS Domain Checker  ", color.RESET)
    print("[ ]",color.PURPLE," Belane 2016  ", color.RESET)
    print("[ ] --------------------------")
    print("[i]",color.BLUE,"Domain", color.RESET)
    print("[+] ", g1.domain)
    print("[+] ", g1.ip)
    if hasattr(g1, "rootdomain"):
        print("[i]",color.BLUE,"Root domain", color.RESET)
        print("[+] ", g1.rootdomain.domain)
        print("[+] ", g1.rootdomain.ip)
    print("[ ] --------------------------")

    print("[ ] ") # SOA
    try:
        print("[i]",color.BLUE,"SOA for", g1.domain, color.RESET)
        g1.get_SOA()
    except:
        if hasattr(g1, "rootdomain"):
            print("[i]  trying SOA for root", g1.rootdomain.domain)
            try:
                g1.rootdomain.get_SOA()
            except:
                print("[!]  No SOA found for", g1.rootdomain.domain)

    print("[ ] ") # DNS SERVERS
    try:
        print("[i]",color.BLUE,"Name Servers for", g1.domain, color.RESET)
        g1.get_NS()
    except:
        if hasattr(g1, "rootdomain"):
            try:
                g1.rootdomain.get_NS()
            except:
                print("[!]  No Name Servers found for", g1.rootdomain.domain)

    print("[ ] ") # ZONE TRANSFER
    print("[i]",color.BLUE,"Checking DNS Zone Transfer for", g1.domain, color.RESET)
    g1.check_ZoneTransfer()

    print("[ ] ") # MX REGISTERS
    try:
        print("[i]",color.BLUE,"MX Registers for", g1.domain, color.RESET)
        g1.get_MX()
    except:
        print("[!]  No MX found for", g1.domain)
        if hasattr(g1, "rootdomain"):
            print("[i]  trying MX for root", g1.rootdomain.domain)
            try:
                g1.rootdomain.get_MX()
            except:
                print("[!]  No MX found for", g1.rootdomain.domain)

    print("[ ] ") # IP REPUTTION
    print("[i]",color.BLUE,"Checking IP Reputation for", g1.ip, g1.domain, color.RESET)
    g1.check_Reputation()
    if hasattr(g1, "rootdomain"):
        print("[i]",color.BLUE,"Checking IP Reputation for", g1.rootdomain.ip, g1.rootdomain.domain, color.RESET)
        g1.rootdomain.check_Reputation()

    print("[ ] ") # IP WHOIS
    print("[i]",color.BLUE,"Whois for", g1.ip, color.RESET)
    g1.get_WhoisIP()

    print("[ ] ") # DOMAIN WHOIS
    if hasattr(g1, "rootdomain"):
        print("[i]",color.BLUE,"Whois for", g1.rootdomain.domain, color.RESET)
        g1.rootdomain.get_Whois()
    else:
        print("[i]",color.BLUE,"Whois for", g1.domain, color.RESET)
        g1.get_Whois()

    print("[ ] ")
    print("[ ] done!")