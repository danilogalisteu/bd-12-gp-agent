import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


class TestFilesInfo(unittest.TestCase):
    def test_cwd(self):
        info = get_files_info("calculator", ".")
        print(info)
        self.assertFalse(info.startswith("Error:"), f"Expected valid directory info, got:\n{info}")

    def test_relative(self):
        info = get_files_info("calculator", "pkg")
        self.assertFalse(info.startswith("Error:"), f"Expected valid directory info, got:\n{info}")
        print(info)

    def test_outside(self):
        info = get_files_info("calculator", "/bin")
        print(info)
        self.assertTrue(info.startswith("Error:"), f"Expected error, got valid directory info:\n{info}")

    def test_relative_outside(self):
        info = get_files_info("calculator", "../")
        print(info)
        self.assertTrue(info.startswith("Error:"), f"Expected error, got valid directory info:\n{info}")


class TestFileRead(unittest.TestCase):
    def test_cwd(self):
        content = get_file_content("calculator", "main.py")
        print(content)
        self.assertFalse(content.startswith("Error:"), f"Expected valid content, got:\n{content}")

    def test_relative(self):
        content = get_file_content("calculator", "pkg/calculator.py")
        print(content)
        self.assertFalse(content.startswith("Error:"), f"Expected valid content, got:\n{content}")

    def test_outside(self):
        content = get_file_content("calculator", "/bin/cat")
        print(content)
        self.assertTrue(content.startswith("Error:"), f"Expected error, got valid content:\n{content}")


class TestFileWrite(unittest.TestCase):
    def test_cwd(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
        self.assertFalse(result.startswith("Error:"), f"Expected valid result, got:\n{result}")

    def test_relative(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
        self.assertFalse(result.startswith("Error:"), f"Expected valid result, got:\n{result}")

    def test_outside(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
        self.assertTrue(result.startswith("Error:"), f"Expected error, got valid result:\n{result}")


if __name__ == "__main__":
    unittest.main()