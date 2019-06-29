import os


def extract():
    base_path = '/Users/bruno/Library/Android/sdk/ndk-bundle/platforms/'
    android_versions = ['android-24/', 'android-26/', 'android-27/', 'android-28/', 'android-29/']
    architectures = ['arch-arm/usr/lib/', 'arch-arm64/usr/lib/', 'arch-x86/usr/lib/', 'arch-x86_64/usr/lib64/']

    for version in android_versions:
        set_so = set()
        for architecture in architectures:
            path = base_path + version + architecture
            files = os.listdir(path)
            for file in files:
                if '.so' in file:
                    set_so.add(file)
        print(version + ', size: ' + str(len(set_so)))
        print(set_so)


extract()