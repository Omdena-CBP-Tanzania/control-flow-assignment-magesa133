import unittest

class TestControlStructures(unittest.TestCase):

    def test_while_loop(self):
        i = 0
        while i <= 20:
            if i % 2 == 0:
                print(f"The even number is {i}")
                if i == 16:
                        break
            i += 1
        pass
    def test_for_loop_continue(self):
        for i in range(1, 10):
            if i % 3 == 0:
                continue
            print(f"The number divisible by 3 is skipped, and the remaining number is {i}")
        pass

    def test_if_else(self):
        for i in range(1, 10):
            if i % 2 == 0:
                print(f"{i} is an even number")
            else:
                print(f"{i} is an odd number")
        pass

    def test_nested_loops(self):
        for i in range(1, 13):
                for j in range(1, 13):
                        print(f"{i} x {j} = {i*j}, ", end=" \t")
                print("\n")
        pass

if __name__ == "__main__":
    unittest.main()