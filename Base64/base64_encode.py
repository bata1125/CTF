import sys
import base64

def main():
    before_encode = input()
    after_encode = base64.b64encode(before_encode.encode('utf-8'))
    print(after_encode)

if __name__ == '__main__':
    main()