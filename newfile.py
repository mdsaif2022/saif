#generate password witch is tough to breakkfor

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols="@#৳%&*/\?"

use_for = lower_case + upper_case + number + symbols
length_for_pass = 8

password = "".join(random.sample(use_for, length_for_password))

print("Your Generated Password is :")