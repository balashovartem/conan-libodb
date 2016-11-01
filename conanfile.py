from conans import ConanFile, CMake, tools, ConfigureEnvironment
import os

channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "balashovartem")

class LibOdbConan(ConanFile):
    name = "libodb"
    version = "2.4.0"
    license = "MIT"
    url = "https://github.com/balashovartem/conan-libodb"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    source_tgz = "http://www.codesynthesis.com/download/odb/2.4/libodb-2.4.0.tar.gz"

    def source(self):
        self.output.info("Downloading %s" % self.source_tgz)
        tools.download(self.source_tgz, "libodb-2.4.0.tar.gz")
        tools.unzip("libodb-2.4.0.tar.gz", ".")
        os.unlink("libodb-2.4.0.tar.gz")

    def build(self):
	env = ConfigureEnvironment(self.deps_cpp_info, self.settings)
	self.run(" cd %s/libodb-2.4.0 && %s ./configure --prefix=%s/install" % (self.conanfile_directory, env.command_line, self.conanfile_directory ) )
	self.run(" cd %s/libodb-2.4.0 && %s make install"  % (self.conanfile_directory, env.command_line)  )

    def package(self):
        self.copy("*", dst="./", src="install", keep_path=True)
	
    def package_info(self):
        self.cpp_info.libs = ['odb'] 
