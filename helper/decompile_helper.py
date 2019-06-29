import subprocess
import pathlib


class DecompileHelper:

    def decompile(self, apk_path):
        if self.has_path(apk_path):
            print('Decompiling the APK, it might take a few seconds.')
            output = subprocess.call(['./apktool', 'd', '-f', apk_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print('Decompilation completed')
            return True
        else:
            print('APK not found in the given path')
            return False

    def has_path(self, apk_path):
        return pathlib.Path(apk_path).exists()

    def decompiled_apk(self, apk_path):
        return apk_path[:apk_path.rfind('.')] + '/'

    def _delete_decompiled(self, decompiled_path):
        output = subprocess.call(['rm', '-R', decompiled_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)