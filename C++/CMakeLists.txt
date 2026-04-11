cmake_minimum_required(VERSION 3.16)

project(Cpp_Hello_World LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(Cpp_Hello_World main.cpp)

include(GNUInstallDirs)
install(TARGETS Cpp_Hello_World
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
