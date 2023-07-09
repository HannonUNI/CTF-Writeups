import re
import os

regularExpression = r"^METACTF{(?!.+([A-Z]{2,})(?=.*\d{3,}).*([!@#$%^&*()\-_=+[\]{};':\"\\|,.<>?]).*$)[A-Za-z\d!@#$%^&*()\-_=+[\]{};':\"\\|,.<>?]{8,}}$"
with open(__file__, "r") as f:
    source_code = f.read()
    print(source_code)

pattern = re.compile(regularExpression)
while 1:
    text = input("Enter secret to get flag :) \n")
    if pattern.match(text) is not None:
        print(os.environ["FLAG"])
        exit(0)