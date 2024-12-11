section .data
    msg db 'Hello, World!', 0xA  ; پیام به همراه کاراکتر جدید

section .text
    global _start                  ; نقطه شروع برنامه

_start:
    ; نوشتن پیام به stdout
    mov rax, 1                    ; شماره سیستم‌کال برای نوشتن (write)
    mov rdi, 1                    ; فایل هندل 1 برای stdout
    mov rsi, msg                  ; آدرس پیام برای خروجی
    mov rdx, 13                   ; تعداد بایت‌هایی که باید نوشته شود
    syscall                       ; فراخوانی سیستم

    ; خروج از برنامه
    mov rax, 60                   ; شماره سیستم‌کال برای خروج (exit)
    xor rdi, rdi                  ; کد خروج 0
    syscall                       ; فراخوانی سیستم
