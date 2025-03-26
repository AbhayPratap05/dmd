import unittest
from format_profile import format_profile

class TestFormatProfile(unittest.TestCase):
    def test_format_profile(self):
        input_lines = [
            "bytes allocated",
            "1024  10  int  somefile.d:42",
            "2048  5   float  somefile.d:56"
        ]
        expected_output = [
            "Memory Allocation Report",
            "=======================",
            "",
            "Bytes Allocated  | Allocations  | Type                       | Function  | File                 | Line",
            "-----------------+-------------+-----------------------------+-----------+----------------------+------",
            "1024             | 10          | int                         | (unknown)  | somefile.d           | 42  ",
            "2048             | 5           | float                       | (unknown)  | somefile.d           | 56  "
        ]

        result = format_profile(input_lines)

        # Debugging Output
        print("Result Output:\n", repr("\n".join(result)))
        print("Expected Output:\n", repr("\n".join(expected_output)))

        # Compare as single string to highlight differences
        self.assertEqual("\n".join(result), "\n".join(expected_output))

if __name__ == "__main__":
    unittest.main()