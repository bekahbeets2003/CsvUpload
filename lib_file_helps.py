import os
import chardet


def get_encoding(filename):
    detector = chardet.UniversalDetector()
    with open(filename, 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break
    detector.close()
    return detector.result['encoding']


def read_file_content(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content


def save_file_as_utf8(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)


def get_index_of_string(string, substring):
    index = string.find(substring)
    if index == -1:
        return 0
    else:
        return index
