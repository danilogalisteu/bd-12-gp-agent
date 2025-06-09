import unittest
from functions.get_files_info import get_files_info


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


if __name__ == "__main__":
    unittest.main()