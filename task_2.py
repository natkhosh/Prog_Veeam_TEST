# Задача 2
# Дан файл, содержащий имена файлов, алгоритм хэширования (один из MD5/SHA1/SHA256) и соответствующие им хэш-суммы,
# вычисленные по соответствующему алгоритму и указанные в файле через пробел. Напишите программу, читающую данный файл
# и проверяющую целостность файлов.
import hashlib
import os
import argparse


def hash_file(filename: str, algorithm: str, bufsize=8192) -> str:
    """
    calculates hashes or checksums in many formats
    :param filename: file path
    :param algorithm: algorithm
    :param bufsize: size of read from the file
    :return: hash
    """
    file_hash = hashlib.new(algorithm)
    with open(filename, 'rb') as f:
        while True:
            data = f.read(bufsize)
            if not data:
                break
            file_hash.update(data)
    return file_hash.hexdigest()


def check_hashsum(path: str, directory_path: str) -> bool:
    """
    Check the hashsum of file
    :param path: check file path
    :param directory_path: path to files directory
    :return: True False
    """
    try:
        with open(path) as file:
            for line in file.readlines():
                file_name, algorithm, hash_sum = line.rstrip('\n').split(' ')

                if not os.path.exists(directory_path + '\\' + file_name):
                    print(f'{file_name} NOT FOUND')

                elif hash_sum == hash_file(directory_path + '\\' + file_name, algorithm):
                    print(f'{file_name} OK')
                else:
                    print(f'{file_name} FAIL')

    # check for file IO error
    except IOError as err:
        print(str(err))
        return False


def createParser():
    """
    Parser for command-line options
    :return: arguments
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('path', type=str, help="Path to file with files to check.")
    arg_parser.add_argument('directory_path', type=str, help="Path to files to check.")

    return arg_parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    check_hashsum(namespace.path, namespace.directory_path)




