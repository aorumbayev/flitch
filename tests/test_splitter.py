"""This module contains core scripts for splitting files"""

# Standard Library
from os import path, listdir
from shutil import rmtree
from tempfile import NamedTemporaryFile, mkdtemp

# Third Party
from pytest import mark, fixture

# Local
from flitch import split_into_parts

# pylint: disable=redefined-outer-name


@fixture(autouse=True)
def test_file():
    """Fixture creating temporary file of 40mb size

    Yields:
        str: path file
    """
    temp_file_path = ""
    with NamedTemporaryFile(suffix=".txt", prefix=path.basename(__file__)) as fout:
        fout.write(b"0" * 1024 * 1024 * 4)
        temp_file_path = fout.name
        yield temp_file_path
    if path.exists(temp_file_path):
        rmtree(temp_file_path)


@fixture(autouse=True)
def test_folder():
    """Fixture creating temporary folder for output chunks

    Yields:
        str: path to output folder
    """
    temp_directory = path.join(mkdtemp(), "temp_folder")
    yield temp_directory
    rmtree(temp_directory)


@mark.parametrize("parts", [(20), (40), (60)])
def test_split_into_parts(parts, test_folder, test_file):
    """Tests split by parts function
    """
    split_into_parts(test_file, test_folder, parts)

    splitted_files_count = len(
        [name for name in listdir(test_folder) if path.isfile(test_folder + "/" + name)]
    )
    assert splitted_files_count == parts + 1
