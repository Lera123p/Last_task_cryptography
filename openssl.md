# Description files namings and their usage

### Message signing with using PSS padding (5-6 task)
#### msg.hash/sig/enc/txt - files connected to  tasks 5-6 all about encryption text massage and signing by publick key.pub or personal server.key
msg.txt - "give my friend 2 bitcoins for a pizza" message for hash encryption and sign

msg.hash - creation a hash value of text message to try sign it up by simple RSA (try failed due to difference in key sizes and version control)

msg.enc - file which signed by key.pub public key

msg.sig - binary file with signed info which cannot be readed simply by using eyes


### Personal certificates and keys for signing (3 task)
server.crs - not signed certificate for sending to other team to sign

server.crt - created as a signed cerver.crs by personal server.key

### Task 4 
server.crs - file from our team to sent on signing

server.crt - signed certificate by our server.key personal key

server_team.crt - signed certificate for another team
