This simple program does a rainbow attack!
How it works?
It takes a CSV file which contains some usernames and their hashed passwords (Passwords are 4-digit numbers which have been hashed with SHA-256).
Then it gives you a CSV file which contains usernames and their original passwords.
Just put your input and ouput csv files path in function arguments.

Sample input CSV file:
hamed,99b057c8e3461b97f8d6c461338cf664bc84706b9cc2812daaebf210ea1b9974
elham,85432a9890aa5071733459b423ab2aff9f085f56ddfdb26c8fae0c2a04dce84c

Function output:
hamed,5104
elham,9770
