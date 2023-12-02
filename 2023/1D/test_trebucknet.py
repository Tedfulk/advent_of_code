import re
from trebucknet import (
    find_first_last_number,
    replace_first_spelled_out_number,
    replace_last_spelled_out_number,
)


def test_replace_last_spelled_out_number():
    # Test case 1: Replace "one" with "1"
    assert replace_last_spelled_out_number("zoneight234zoneight") == "zoneight234zon8"

    # Test case 2: Replace "three" with "3"
    assert (
        replace_first_spelled_out_number("zoneight234zoneight") == "z1ight234zoneight"
    )

    print("All test cases pass")


test_replace_last_spelled_out_number()
