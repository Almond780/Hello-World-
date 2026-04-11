cmake_minimum_required(VERSION 3.16)

project(C_Hello_World LANGUAGES C)

add_executable(C_Hello_World main.c)

include(GNUInstallDirs)
install(TARGETS C_Hello_World
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
