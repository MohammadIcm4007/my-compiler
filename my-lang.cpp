#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    std::string command_one = "./nasm -f elf64 " + std::string(argv[1]) + ".asm -o " + std::string(argv[1]) + ".o";
    std::string command_two = "./ld " + std::string(argv[1]) + ".o -o " + std::string(argv[1]);
    int result_one = system(command_one.c_str());
    int result_two = system(command_two.c_str());
    return 0;
}
