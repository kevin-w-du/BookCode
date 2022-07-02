all:
	gcc -o udp_client udp_client.c
	gcc -o spoof_icmp spoof_icmp.c checksum.c send_raw_ip_packet.c
	gcc -o spoof_udp  spoof_udp.c  checksum.c send_raw_ip_packet.c
	gcc -o spoof_tcp  spoof_tcp.c  checksum.c send_raw_ip_packet.c
	gcc -o sniff_spoof_udp sniff_spoof_udp.c  checksum.c send_raw_ip_packet.c -lpcap

clean:
	rm -f udp_client spoof_icmp spoof_udp spoof_tcp *.o *.out
	rm -f sniff_spoof_udp
