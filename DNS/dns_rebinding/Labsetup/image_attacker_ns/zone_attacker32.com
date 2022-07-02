$TTL 3D ; default expiration time of all resource records
        ; without their own TTL
@       IN      SOA   ns.attacker32.com. admin.attacker32.com. (
                2008111001
                8H
                2H
                4W
                1D)

@       IN      NS    ns.attacker32.com. ; nameserver

@       IN      A     192.168.0.101   ; for attacker32.com
www     IN      A     192.168.0.101   ; for www.attacker32.com
xyz     IN      A     192.168.0.102   ; for xyz.attacker32.com
ns      IN      A     10.9.0.153      ; for ns.attacker32.com
*       IN      A     192.168.0.100   ; for other names

