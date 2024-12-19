import socket

def check_blacklist(ip_address):
    # Define DNSBL domain suffixes for three different DNSBL services
    domains = ["b.barracudacentral.org", "bl.spamcop.net","blacklist.woody.ch", "cbl.abuseat.org", "combined.abuse.ch", "combined.rbl.msrbl.net", "db.wpbl.info", "dnsbl.cyberlogic.net","dnsbl.sorbs.net", "drone.abuse.ch","dul.dnsbl.sorbs.net","dynip.rothen.com","http.dnsbl.sorbs.net", "images.rbl.msrbl.net","ips.backscatterer.org", "ix.dnsbl.manitu.net","misc.dnsbl.sorbs.net","noptr.spamrats.com","pbl.spamhaus.org", "phishing.rbl.msrbl.net","rbl.interserver.net","relays.bl.gweep.ca", "relays.nether.net", "smtp.dnsbl.sorbs.net","socks.dnsbl.sorbs.net", "spam.abuse.ch", "spam.dnsbl.sorbs.net","spam.rbl.msrbl.net", "spam.spamrats.com", "spamrbl.imp.ch","tor.dnsbl.sectoor.de","torserver.tor.dnsbl.sectoor.de","ubl.unsubscore.com", "virus.rbl.jp", "virus.rbl.msrbl.net","web.dnsbl.sorbs.net", "wormrbl.imp.ch", "xbl.spamhaus.org","zen.spamhaus.org", "zombie.dnsbl.sorbs.net","dnsbl-1.uceprotect.net"]

    # Check if the IP address is blacklisted in any of the DNSBL services
    for domain in domains:
        # Convert IP address to reversed octet format and append DNSBL domain suffix
        query = '.'.join(reversed(str(ip_address).split("."))) + "." + domain

        try:
            # Perform a DNS query to check if the IP address is blacklisted
            socket.gethostbyname(query)
            return True
            # If the DNS query returs any value then the IP is blacklisted
        except socket.error:
            # If the DNS query returns an error, the IP address is not blacklisted in this service
            continue


ip_address= input("IP address to check:")
Blacklist_result = check_blacklist(ip_address)
if Blacklist_result == True:
    print ("the IP address is blacklisted")
else:
    print( "You are OK")




