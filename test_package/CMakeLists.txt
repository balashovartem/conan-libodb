PROJECT(libodb-test)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

set( PKG_CONFIG_USE_CMAKE_PREFIX_PATH TRUE )
find_package(PkgConfig REQUIRED)
message( "${CMAKE_PREFIX_PATH}" )
pkg_search_module( LIBODB REQUIRED libodb)

IF(LIBODB_FOUND)
    message( " ${LIBODB_INCLUDE_DIRS} ${LIBODB_LIBRARIES}") 
    include_directories( ${LIBODB_INCLUDE_DIRS} )
    ADD_EXECUTABLE( ${PROJECT_NAME} main.cpp )
    TARGET_LINK_LIBRARIES( ${PROJECT_NAME} ${LIBODB_LIBRARIES})
ELSE()
    MESSAGE(FATAL_ERROR "libodb not found")
ENDIF()