from OpenSSL.crypto import load_certificate_request, FILETYPE_PEM, TYPE_RSA

file = open("CTF_Challenge/picoctf/ReadMyCert/readmycert.csr", "r")
data = file.read()

csr_request = load_certificate_request(FILETYPE_PEM, data.encode())
print(csr_request.get_subject())
