class Database:

    def __init__(self):
        self.map = {}

    def build_database(self):

        self.map['android-24'] = ['libjnigraphics.so', 'libOpenMAXAL.so', 'libGLESv1_CM.so', 'libm.so', 'libEGL.so', 'libandroid.so', 'libz.so', 'libGLESv3.so', 'libvulkan.so', 'libc.so', 'libdl.so', 'libcamera2ndk.so', 'libstdc++.so', 'libGLESv2.so', 'liblog.so', 'libOpenSLES.so', 'libmediandk.so']
        self.map['android-26'] = ['libjnigraphics.so', 'libOpenMAXAL.so', 'libGLESv1_CM.so', 'libm.so', 'libEGL.so', 'libandroid.so', 'libz.so', 'libaaudio.so', 'libGLESv3.so', 'libvulkan.so', 'libc.so', 'libdl.so', 'libcamera2ndk.so', 'libstdc++.so', 'libGLESv2.so', 'liblog.so', 'libsync.so', 'libOpenSLES.so', 'libnativewindow.so', 'libmediandk.so']
        self.map['android-27'] = ['libjnigraphics.so', 'libandroid.so', 'libneuralnetworks.so', 'liblog.so', 'libsync.so', 'libOpenSLES.so', 'libm.so', 'libGLESv3.so', 'libstdc++.so', 'libGLESv1_CM.so', 'libEGL.so', 'libvulkan.so', 'libdl.so', 'libcamera2ndk.so', 'libGLESv2.so', 'libnativewindow.so', 'libmediandk.so', 'libz.so', 'libc.so', 'libaaudio.so', 'libOpenMAXAL.so']
        self.map['android-28'] = ['libjnigraphics.so', 'libandroid.so', 'libneuralnetworks.so', 'liblog.so', 'libsync.so', 'libOpenSLES.so', 'libm.so', 'libGLESv3.so', 'libstdc++.so', 'libGLESv1_CM.so', 'libEGL.so', 'libvulkan.so', 'libdl.so', 'libcamera2ndk.so', 'libGLESv2.so', 'libnativewindow.so', 'libmediandk.so', 'libz.so', 'libc.so', 'libaaudio.so', 'libOpenMAXAL.so']
        self.map['android-29'] = ['libjnigraphics.so', 'libandroid.so', 'libneuralnetworks.so', 'libamidi.so', 'liblog.so', 'libsync.so', 'libOpenSLES.so', 'libm.so', 'libGLESv3.so', 'libstdc++.so', 'libGLESv1_CM.so', 'libEGL.so', 'libbinder_ndk.so', 'libvulkan.so', 'libdl.so', 'libcamera2ndk.so', 'libGLESv2.so', 'libnativewindow.so', 'libmediandk.so', 'libz.so', 'libc.so', 'libaaudio.so', 'libOpenMAXAL.so']

        return self.map

    def is_public_library(self, dependency):
        found = 0
        for versions in self.map:
            if dependency in self.map[versions]:
                found = found + 1
        if found > 0:
            return True
        else:
            return False
