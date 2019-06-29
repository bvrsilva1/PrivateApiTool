import subprocess


class ReadLibraryHelper:

    def read_library_so(self, path):
        libraries = []
        process = subprocess.Popen('./readelf --dynamic ' + path + ' | grep NEEDED', stdout=subprocess.PIPE, shell=True)
        while True:
            line = process.stdout.readline().rstrip()
            if not line:
                break
            line = str(line)
            libraries.append(line[line.find('[') + 1: line.rfind(']')])
        process.kill()
        process.communicate()
        return libraries
