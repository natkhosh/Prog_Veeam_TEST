import os
import shutil
import configparser
from lxml import etree
from lxml.etree import XMLSyntaxError
from lxml.etree import XMLSchemaParseError

config = configparser.ConfigParser()
config.read("settings.ini")


def xml_validate(xml_path: str, xsd_path: str) -> bool:
    """
    XML file validation.
    :param xml_path: XML file path
    :param xsd_path: XSD file path, schema file
    :return: True False
    """
    try:
        xmlschema_doc = etree.parse(xsd_path)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        xml_doc = etree.parse(xml_path)
        xmlschema.assertValid(xml_doc)
        return True

    # check for file IO error
    except IOError as err:
        print(str(err))
        return False

    # check for XML syntax errors
    except XMLSyntaxError as err:
        print('XML Syntax Error')
        return False

    except XMLSchemaParseError as err:
        print('Schema validation error')
        return False

    except etree.DocumentInvalid as err:
        print('Validation error: ', err.error_log.filter_from_errors()[0])
        return False


def file_copy(source: str, destination: str) -> bool:
    """
    Copies an existing file to the specified directory.
    :param source: file
    :param destination:directory
    :return: True False
    """
    if not os.path.exists(source):
        print(f"**** File {source} not found")

    if os.path.exists(destination):
        print(f'File {destination} already exist' + '\n ' + 'Overwrite? Yes (y) / No (n)' + '\n ')
        answer = input('-->  ')
        while not (answer == 'y' or 'n'):
            print("Please input 'y' or 'n' ")
            answer = input('-->  ')

        if answer == 'y':
            try:
                shutil.copy(source, destination)
                print("File copied successfully.")
                return True

            # If source and destination are same
            except shutil.SameFileError:
                print("Source and destination represents the same file.")
                return False

            # If there is any permission issue
            except PermissionError:
                print("Permission denied.")
                return False
        else:
            print(f"File {source} copy canceled")
            return False


def main():
    """
    Main function, run project.
    :return:
    """
    if xml_validate(config['COMMON']["XML"], config['COMMON']["XSD"]):

        tree = etree.parse(config['COMMON']["XML"])
        root = tree.getroot()
        for child in root:
            source_path = child.attrib['source_path'] + '/' + child.attrib['file_name']
            destination_path = child.attrib['destination_path'] + '/' + child.attrib['file_name']
            file_copy(source_path, destination_path)

    else:
        print("File not valid! :(")


if __name__ == '__main__':
    main()
