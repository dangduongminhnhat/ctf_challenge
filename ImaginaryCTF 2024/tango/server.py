from Crypto.Cipher import Salsa20
from Crypto.Util.number import bytes_to_long, long_to_bytes
import json
from secrets import token_bytes, token_hex
from zlib import crc32

# from secret import FLAG

KEY = b'[\r\xec=<\xb1\xef\x05\xf3\xdc\x11\x9ci\xcc\x88\x91\xb4\x03\xb3#\xa9\x8a\xbf:\x82\xdeZ\xea#\xf2Q\xe3'


def encrypt_command(command):
    if len(command) != 3:
        print('Nuh uh.')
        return
    cipher = Salsa20.new(key=KEY)
    nonce = cipher.nonce
    data = json.dumps({'user': 'user', 'command': command, 'nonce': token_hex(8)}).encode('ascii')
    checksum = long_to_bytes(crc32(data))
    ciphertext = cipher.encrypt(data)
    print('Your encrypted packet is:', (nonce + checksum + ciphertext).hex())


def run_command(packet):
    packet = bytes.fromhex(packet)
    nonce = packet[:8]
    checksum = bytes_to_long(packet[8:12])
    ciphertext = packet[12:]

    try:
        cipher = Salsa20.new(key=KEY, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext)

        if crc32(plaintext) != checksum:
            print('Invalid checksum. Aborting!')
            return

        data = json.loads(plaintext.decode('ascii'))
        user = data.get('user', 'anon')
        command = data.get('command', 'nop')

        if command == 'nop':
            print('...')
        elif command == 'sts':
            if user not in ['user', 'root']:
                print('o_O')
                return
            print('The server is up and running.')
        elif command == 'flag':
            if user != 'root':
                print('You wish :p')
            else:
                print(FLAG)
        else:
            print('Unknown command.')
    except (json.JSONDecodeError, UnicodeDecodeError):
        print('Invalid data. Aborting!')


def menu():
    print('[E]ncrypt a command')
    print('[R]un a command')
    print('[Q]uit')


def main():
    print('Welcome to the Tango server! What would you like to do?')
    while True:
        menu()
        option = input('> ').upper()
        if option == 'E':
            command = input('Your command: ')
            encrypt_command(command)
        elif option == 'R':
            packet = input('Your encrypted packet (hex): ')
            run_command(packet)
        elif option == 'Q':
            exit(0)
        else:
            print('Unknown option:', option)


# if __name__ == '__main__':
#     main()

dum =       b'{"user": "user", "command": "sts", '
dum_flag =  b'{"user": "root", "command": "flag"}'

from pwn import *

r = remote("tango.chal.imaginaryctf.org", 1337)

print(r.recvline())
print(r.recvline())

print(r.recvuntil(b"> "))
r.sendline(b"E")
print(r.recvuntil(b"Your command: "))
r.sendline(b"sts")

enc = r.recvline()[:-1].split(b"Your encrypted packet is: ")[1].decode()
packet = bytes.fromhex(enc)
nonce = packet[:8]
checksum = bytes_to_long(packet[8:12])
ciphertext = packet[12:]

new_ciphertext = b""
for i in range(len(dum)):
    new_ciphertext += int.to_bytes(ciphertext[i] ^ dum[i] ^ dum_flag[i])

checksum = crc32(dum_flag)
r.recvuntil(b"> ")
r.sendline(b"R")

r.recvuntil(b"Your encrypted packet (hex): ")
packet = nonce + long_to_bytes(checksum) + new_ciphertext

r.sendline(packet.hex().encode())
print(r.recvline())
