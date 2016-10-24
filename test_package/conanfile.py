from conans import ConanFile, CMake
import os

channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "balashovartem")

class CutlTest(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "libodb/2.4.0@%s/%s" % (username, channel)

    def build(self):
	cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)
    def test(self):
        self.run("cd bin && .%slibodb-test" % os.sep)