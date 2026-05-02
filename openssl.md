# Description files namings and their usage

### Message signing with using PSS padding (5-6 task)
#### msg.hash/enc/txt - files connected to  tasks 5-6 all about encryption text massage and signing by publick key.pub or personal server.key
msg.txt - "give my friend 2 bitcoins for a pizza" message for hash encryption and sign

msg.hash - creation a hash value of text message to try sign it up by simple RSA (doesn't need it in future due to other utilite made it in one command)

msg.enc - file which encrypted by key.pub public key

sign.bin - binary file with signed info which cannot be readed simply by using eyes


### Personal certificates and keys for signing (3 task)
server.csr - not signed certificate for sending to other team to sign

server.crt - created as a signed cerver.crs by personal server.key

### Task 4 
server.csr - file from our team to sent on signing

server.crt - signed certificate by our server.key personal key

server.csr - not signed certificate that colleagues sent us to sign

signed_sertificate.crt - signed certificate for another team

certificate_details.txt - read txt format to check Issuer and Subject

### Certificates namings from other team sent to us

signed_certificate_for_us.txt/.crt - files from other team on signing th certificate. Issuer and Subject flips as it must be
