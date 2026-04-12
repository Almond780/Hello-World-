section .data
    msg db 'Hello World! from assembly!', 10, 0   ; null‑terminated string

section .text
    global print_hello

print_hello:
    ; uses write syscall (no libc) – preserves registers
    mov rax, 1          ; write
    mov rdi, 1          ; stdout
    mov rsi, msg
    mov rdx, 28;length of string (count characters)
    syscall
    ret