sudo nmap -sP -n 192.168.10.0/24 | awk '/Nmap scan/{gsub(/[()]/,"",$NF); print $NF > "scanned_ips.txt"}'
