import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


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


class TestFileContent(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()