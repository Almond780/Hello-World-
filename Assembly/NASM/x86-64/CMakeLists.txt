cmake_minimum_required(VERSION 3.16)

# Enable C++ and ASM_NASM languages
project(NASM_Hello_World_Cmake LANGUAGES CXX ASM_NASM)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add both C++ and assembly source files
add_executable(NASM_Hello_World_Cmake main.cpp
    hello.asm)

# On Linux, CMake may try to pass -fPIC to NASM (which fails).
# This macro removes -fPIC from the assembler flags for NASM only.
if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
    set(CMAKE_ASM_NASM_FLAGS "${CMAKE_ASM_NASM_FLAGS} -f elf64")
    # Remove any -fPIC that might be added automatically
    string(REPLACE "-fPIC" "" CMAKE_ASM_NASM_FLAGS "${CMAKE_ASM_NASM_FLAGS}")
endif()

include(GNUInstallDirs)
install(TARGETS NASM_Hello_World_Cmake
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)