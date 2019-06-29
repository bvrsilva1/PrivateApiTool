import os
from helper import DecompileHelper
from helper import ReadLibraryHelper
from database import Database
import pathlib


class PrivateApi:

    def __init__(self):
        pass

    def analyze(self):

        vetted = []
        database = Database()
        database.build_database()

        decompiler = DecompileHelper()

        if decompiler.decompile(self.path):
            self._update_path()

            try:
                architectures = self.get_architectures();
                reader_helper = ReadLibraryHelper()

                print('Analyzing app...')

                for architecture in architectures:
                    libraries = self.get_libraries(architecture)
                    for library in libraries:
                        path = architecture + '/' + library
                        dependencies = reader_helper.read_library_so(path)

                        for dependency in dependencies:
                            if not database.is_public_library(dependency) and dependency not in libraries:
                                vetted.append(path + '/' + dependency)
            except Exception as error:
                print(repr(error))

        return vetted

    def _update_path(self):
        current_dir = str(pathlib.Path(__file__).parent)
        current_dir = current_dir[:current_dir.rfind('/')]
        self.path = current_dir + self.path[self.path.rfind('/'):]

    def get_architectures(self):

        architectures = []

        decompile = DecompileHelper()
        decompiled_folder = decompile.decompiled_apk(self.path) + 'lib/'

        if decompile.has_path(decompiled_folder):
            for root, directory, files in os.walk(decompiled_folder):
                for folder in directory:
                    architectures.append(os.path.join(root, folder))
            return architectures
        else:
            raise Exception('Decompiled folder does not exist or does not contain lib folder')

    def get_libraries(self, architecture):
        libraries = set()
        for root, directory, files in os.walk(architecture):
            for file in files:
                if '.so' in file:
                    libraries.add(file)
        return libraries
