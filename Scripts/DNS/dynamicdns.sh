#bin/bash
domain=<domain>
secret=<secret>
ip=$(curl "http://ipinfo.io/ip")

curl -4 "https://$domain:$secret@dyn.dns.he.net/nic/update?hostname=$domain&myip=$ip"
