TARGET = myexit shellcode_one shellcode_two shellcode_64

all: $(TARGET)

myexit: myexit.s
	nasm -f elf32 $@.s -o $@.o
	ld -m elf_i386 $@.o -o $@

shellcode_one: shellcode_one.s
	nasm -f elf32 $@.s -o $@.o
	ld -m elf_i386 $@.o -o $@

shellcode_two: shellcode_two.s
	nasm -f elf32 $@.s -o $@.o
	ld --omagic -m elf_i386 $@.o -o $@

shellcode_64: shellcode_64
	nasm -f elf64 $@.s -o $@.o
	ld $@.o -o $@

clean:
	rm -f *.o *.out $(TARGET)
