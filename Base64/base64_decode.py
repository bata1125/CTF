import sys
import base64

def main():
    before_decode = input()
    after_decode = base64.b64decode(before_decode)
    print(after_decode)

if __name__ == '__main__':
    main()