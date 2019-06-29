import sys
from engine import Checker


def main():
    if len(sys.argv) != 2:
        print("Please use this tool as follow: python app.py <path to apk>")
    else:

        apk_path = sys.argv[1]

        checker = Checker().build('private_api')
        checker.path = apk_path
        result = checker.analyze()

        if len(result) > 0:
            print('APK should be vetted. It executes the following non public libraries ')
            for libs in result:
                print(libs)
        else:
            print('No problem with this APK')


if __name__== "__main__":
  main()