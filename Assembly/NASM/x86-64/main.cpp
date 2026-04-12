#include <iostream>

extern "C" void print_hello();

int main() {
    std::cout << "Hello World! from C++!" << std::endl;
    print_hello();
    return 0;
}