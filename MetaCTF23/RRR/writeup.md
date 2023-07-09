## RRRRR (ez for the wrong reasons)

1337 pts

```
Author: NaturalT
```

you start an instans that gives u a netcat connection

when u connect u get the following

```python
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

Enter secret to get flag :) 

```

when u connect it sends the code of the file and then runs the code (how convenient)
basically what the code does is it checks if the input matches the regex and if it does it prints the flag

lets figure out what the regex does, there's this small website u might have herd of called [ChatGPT](chat.openai.com) that can help us with that lets ask it for help

```
what can i enter to pass the regex + the code
```

> The provided regular expression pattern is quite complex and has specific requirements for the input to pass. To pass the regex and obtain the flag, the input needs to satisfy the following conditions:

> The input should start with "METACTF{".
> It should contain at least 8 characters.
> It should consist of a combination of uppercase letters, lowercase letters, digits, and the following special characters: !@#$%^&*()-_=+[]{};':\"\\|,.<>?.
> It should not contain consecutive uppercase letters (2 or more uppercase letters in a row).
> It should contain at least 3 consecutive digits.
> It should contain at least one of the following special characters: !@#$%^&*()-_=+[]{};':\"\\|,.<>?.
> Here's an example of an input that satisfies the regular expression pattern:
>
> ```
> METACTF{Abc123!@#}
> ```

> Keep in mind that the actual flag value may be different and depends on the value of the environment variable "FLAG" that is set in your execution environment.

yeah yeah whatever, lets test `METACTF{Abc123!@#}`

no surprise it works and we get the flag (i lost the flag)
i wonder how it got so many solves 🤔

### **i would like to say a few words**

this is a challenge that i would've sunk my teeth into, and squeezed my tiny brainz to solve, then get a high like no other, but unfortunately there is no point in doing that, since theres a part of me that knows that AI would do it effortlessly and i would be left with nothing but a feeling of emptiness after eventually surrendering to get help from AI, todays kids will grow spoiled with AI tools, its real painful to think that my little nephew will not use his smarts (which he has a lot of) because he doesn't have to, resulting in him not developing his problem solving skills, i wish that microsoft would make chatgpt a paid service, else we will get an era of inexperienced junior developers, we still need smart people, there are a lot of problems unsolved, and at some point AI won't cut it.

lastly, small brain small pepe.
