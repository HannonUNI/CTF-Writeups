# Cryptographic Space Rover (kinda hard)

### Description

NASA has sent this custom program off to a remote space rover, luckily it already had Python and all the dependencies installed so we don't have to worry about transferring those. It will print the CPU usage and some fun other facts about the system when it's run. It seems to run an equal number of time to the number of characters entered. For some reason, certain characters at certain indexes cause new processes to spawn... can you help us find what characters to avoid at certain indexes?

### Files

```python
from pwn import * 
p=remote("spaceheroes-cryptographic-space-rover.chals.io", 443, ssl=True, sni="spaceheroes-cryptographic-space-rover.chals.io")
p.interactive()
```

**nasa_crypto.py**

```python
import psutil
import datetime
import os
import signal
import subprocess
import uuid
import setproctitle

#python3 -m pip install setproctitle

def get_dashes(perc):
    dashes = "|" * int((float(perc) / 10 * 4))
    empty_dashes = " " * (40 - len(dashes))
    return dashes, empty_dashes

def print_top(guess, uuid):
    cat_check = 0
    if(guess == True):
        setproctitle.setproctitle(str(uuid))
        setproctitle.setthreadtitle(str(uuid))

    print(f"top - {str(datetime.timedelta(seconds=psutil.boot_time()))}")
    percs = psutil.cpu_percent(interval=0, percpu=True)
    for cpu_num, perc in enumerate(percs):
        dashes, empty_dashes = get_dashes(perc)
        line = " CPU%-2s [%s%s] %5s%%" % (cpu_num, dashes, empty_dashes, perc)
        print(line)

    virtual_memory = psutil.virtual_memory()
    print(f"MiB Swap :\t{virtual_memory.total / 1024 / 1024:.2f} total\t{virtual_memory.free / 1024 / 1024:.2f} free\t{virtual_memory.used / 1024 / 1024:.2f} used\t{virtual_memory.active / 1024 / 1024:.2f} active")
    swap_memory = psutil.swap_memory()
    print(f"MiB Swap :\t{swap_memory.total / 1024 / 1024:.2f} total\t{swap_memory.free / 1024 / 1024:.2f} free\t{swap_memory.used / 1024 / 1024:.2f} used")

    listOfProcessNames = []
    for proc in psutil.process_iter():
        pInfoDict = proc.as_dict(attrs=['pid', 'username', 'cpu_percent', 'memory_percent', 'status', 'name']) # Get process detail as dictionary
        listOfProcessNames.append(pInfoDict) # Add to list

    print(f'{"PID":>6}{"USER":>10}{"%CPU":>6}{"%MEM":>6}{"STATUS":>15}{"NAME":>45}')
    for elem in listOfProcessNames:
        print(f'{elem["pid"]:>6}{elem["username"]:>10}{elem["cpu_percent"]:>6}{elem["memory_percent"]:>6.2f}{elem["status"]:>15}{elem["name"]:>45}')

    if (guess == True):
        setproctitle.setproctitle("python3")
        setproctitle.setthreadtitle("python3")


def logo(uuid):
    ascii_art = """
             ____________________________________________________
            /                                                    \\
           |    _____________________________________________     |
           |   |                                             |    |
           |   |  Welcome to the NASA Lunar Rover.           |    |
           |   |                                             |    |
           |   |  Session UUID:                              |    |
           |   |    {0}     |    |
           |   |                                             |    |
           |   |  This program should help us track CPU      |    |
           |   |      usage but it seems to spawn extra      |    |
           |   |      processes when we give it certain      |    |
           |   |      characters.                            |    |
           |   |                                             |    |
           |   |  Can you help us narrow down what           |    |
           |   |      characters to avoid at each index?     |    |
           |   |                                             |    |
           |   |  Enter your characters below.               |    |
           |   |  Thanks, The Space Heroes                   |    |
           |   |_____________________________________________|    |
           |                                                      |
            \_____________________________________________________/
                   \_______________________________________/
    """.format(uuid)
    print(ascii_art)

def main():
    session_uuid = uuid.uuid4()
    flag = open('flag.txt', 'r').readline().strip('\n').lower()

    logo(session_uuid)
    print("Please enter characters:: ")

    user_guess = input().lower().strip("\n")

    for i in range(0, len(flag)):
        if i+1 > len(user_guess):
            print_top(guess=None, uuid=session_uuid)
            exit(-1)
        elif (user_guess[i] != flag[i]):
            print_top(guess=False, uuid=session_uuid)
        else:
            print_top(guess=True,uuid=session_uuid)

    if user_guess == flag:
        print(f"Thanks; we'll avoid these characters: {flag}")

if __name__ == "__main__":
    main()

```

## Solution

Alright first thing to do is understand the code, then try to run it and see what it does.

##### * understand the code

navigating to `main()` creates a random uuid, calls `logo()`, it just prints a fancy ascii art welcome page but, it contains a key value that we will use later on, which is the uuid, after that it asks the user to input a string, it runs a loop over the letters you input, for each letter it checks wether it matches the corresponding letter in the flag, if it does it calls `print_top()` with `guess` parameter as `True` else as `False` and in one edge case `None` (same as `False`), now what does `print_top()` do?

it prints a lot of data related to the os of the server, stuff that doesn't seem relevant, but if look closer you'll find that if `guess == True` it does the following:

```python
setproctitle.setproctitle(str(uuid))
setproctitle.setthreadtitle(str(uuid))
```

google what `setproctitle.setproctitle` does to find that it starts a new process and sets its title to our `uuid,` hmm when does it do that when guess is `True` and when is guess `True`? whn the character you enter is the same as the character corresponding to it in the flag, so if i find a process with the title as  your `uuid` value, then its the right letter from the flag.

Ok lets do some testing:

If we connect to the remote and send a random letter, `G` for example the output would be:

```python
top - 19463 days, 13:40:21
 CPU0  [                                        ]   0.0%
 CPU1  [                                        ]   0.0%
MiB Swap :      3931.66 total   669.49 free     1433.36 used    1976.44 active
MiB Swap :      0.00 total      0.00 free       0.00 used
   PID      USER  %CPU  %MEM         STATUS                                         NAME
     1      root   0.0  0.08       sleeping                                     start.sh
     6      root   0.0  0.09       sleeping                                           su
     7      root   0.0  0.11       sleeping                                        socat
 32992      root   0.0  0.02       sleeping                                        socat
 32993      root   0.0  0.31        running                                      python3
```

 We know that the flag starts with `s` lets try that:

```python
top - 19463 days, 13:40:21
 CPU0  [||||||||||||||||||||||||                ]  60.4%
 CPU1  [|||||||||||||||||||||||                 ]  57.8%
MiB Swap :      3931.66 total   669.49 free     1433.36 used    1976.44 active
MiB Swap :      0.00 total      0.00 free       0.00 used
   PID      USER  %CPU  %MEM         STATUS                                         NAME
     1      root   0.0  0.08       sleeping                                     start.sh
     6      root   0.0  0.09       sleeping                                           su
     7      root   0.0  0.11       sleeping                                        socat
 32992      root   0.0  0.02       sleeping                                        socat
 32993      root   0.0  0.31        running         3dd6ca89-d0be-4b9c-b94f-c6e7605ce516
```

HOLLY MOLLY, works as expected, lets try more, something like `shctf{`

```python
top - 19463 days, 13:40:21
 CPU0  [||||||||||||||||||||||||                ]  60.4%
 CPU1  [|||||||||||||||||||||||                 ]  57.8%
MiB Swap :      3931.66 total   669.49 free     1433.36 used    1976.44 active
MiB Swap :      0.00 total      0.00 free       0.00 used
   PID      USER  %CPU  %MEM         STATUS                                         NAME
     1      root   0.0  0.08       sleeping                                     start.sh
     6      root   0.0  0.09       sleeping                                           su
     7      root   0.0  0.11       sleeping                                        socat
 32992      root   0.0  0.02       sleeping                                        socat
 32993      root   0.0  0.31        running         3dd6ca89-d0be-4b9c-b94f-c6e7605ce516
top - 19463 days, 13:40:21
 CPU0  [                                        ]   0.0%
 CPU1  [                                        ]   0.0%
MiB Swap :      3931.66 total   669.49 free     1433.36 used    1976.44 active
MiB Swap :      0.00 total      0.00 free       0.00 used
   PID      USER  %CPU  %MEM         STATUS                                         NAME
     1      root   0.0  0.08       sleeping                                     start.sh
     6      root   0.0  0.09       sleeping                                           su
     7      root   0.0  0.11       sleeping                                        socat
 32992      root   0.0  0.02       sleeping                                        socat
 32993      root   0.0  0.31        running         3dd6ca89-d0be-4b9c-b94f-c6e7605ce516
top - 19463 days, 13:40:21
 CPU0  [||||||||||||||||||||||||||||||||||||||||] 100.0%
 CPU1  [                                        ]   0.0%
MiB Swap :      3931.66 total   669.49 free     1433.36 used    1976.44 active
MiB Swap :      0.00 total      0.00 free       0.00 used
   PID      USER  %CPU  %MEM         STATUS                                         NAME
     1      root   0.0  0.08       sleeping                                     start.sh
     6      root   0.0  0.09       sleeping                                           su
     7      root   0.0  0.11       sleeping                                        socat
 32992      root   0.0  0.02       sleeping                                        socat
 32993      root   0.0  0.31        running         3dd6ca89-d0be-4b9c-b94f-c6e7605ce516
top - 19463 days, 13:40:21
 CPU0  [                                        ]   0.0%
 CPU1  [||||||||||||||||||||||||||||||||||||||||] 100.0%
MiB Swap :      3931.66 total   669.49 free     1433.36 used    1976.44 active
MiB Swap :      0.00 total      0.00 free       0.00 used
   PID      USER  %CPU  %MEM         STATUS                                         NAME
     1      root   0.0  0.08       sleeping                                     start.sh
     6      root   0.0  0.09       sleeping                                           su
     7      root   0.0  0.11       sleeping                                        socat
 32992      root   0.0  0.02       sleeping                                        socat
 32993      root 432.9  0.31        running         3dd6ca89-d0be-4b9c-b94f-c6e7605ce516
top - 19463 days, 13:40:21
 CPU0  [                                        ]   0.0%
 CPU1  [                                        ]   0.0%
MiB Swap :      3931.66 total   669.49 free     1433.36 used    1976.44 active
MiB Swap :      0.00 total      0.00 free       0.00 used
   PID      USER  %CPU  %MEM         STATUS                                         NAME
     1      root   0.0  0.08       sleeping                                     start.sh
     6      root   0.0  0.09       sleeping                                           su
     7      root   0.0  0.11       sleeping                                        socat
 32992      root   0.0  0.02       sleeping                                        socat
 32993      root   0.0  0.31        running         3dd6ca89-d0be-4b9c-b94f-c6e7605ce516
top - 19463 days, 13:40:21
 CPU0  [||||||||||||||||||||||||||||||||||||||||] 100.0%
 CPU1  [||||||||||||||||||||||||||||||||||||||||] 100.0%
MiB Swap :      3931.66 total   669.49 free     1433.36 used    1976.44 active
MiB Swap :      0.00 total      0.00 free       0.00 used
   PID      USER  %CPU  %MEM         STATUS                                         NAME
     1      root   0.0  0.08       sleeping                                     start.sh
     6      root   0.0  0.09       sleeping                                           su
     7      root   0.0  0.11       sleeping                                        socat
 32992      root   0.0  0.02       sleeping                                        socat
 32993      root   0.0  0.31        running         3dd6ca89-d0be-4b9c-b94f-c6e7605ce516
```

Ok Awesome now we can brute force every number, letter (lowercase and uppercase) and every symbol for each character in the flag... no?

that sounds boarding and very time consuming, lets write a big brain script to do it for us:

```python
from pwn import *

chars = 'abcdefghijklmnopqrstuvwxyz0123456789_{}ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()+|'
flag = 'shctf'
last_count = 0
letter = '{'
while True:
    p = remote("spaceheroes-cryptographic-space-rover.chals.io", 443,
               ssl=True, sni="spaceheroes-cryptographic-space-rover.chals.io")
    r = str(p.recvuntil("Please enter characters:: "))
    uuid = r.split("Session UUID:")[1][58:58+37].strip()
  
    guess = flag+letter
    print(guess)
    p.sendline(guess.encode())

    all = p.recvall()
    counter = all.count(uuid.encode())
    if counter > last_count:
        flag += letter
        if letter == '}':
            print(f'{flag = }')
            break
        last_count = counter
        letter = chars[0]
        guess = flag+letter
        continue
    else:
        p.close()
        letter = chars[chars.find(letter)+1]
        guess = flag+letter
        continue

```

Ill it break down just in case:

```python
rom pwn import *

chars = 'abcdefghijklmnopqrstuvwxyz0123456789_{}ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()+|'
flag = 'shctf'
last_count = 0
letter = '{'
while True:
    p = remote("spaceheroes-cryptographic-space-rover.chals.io", 443, ssl=True, sni="spaceheroes-cryptographic-space-rover.chals.io")
```

until here all seems fine and understandable (i hope)

```python
    r = str(p.recvuntil("Please enter characters:: "))
    uuid = r.split("Session UUID:")[1][58:58+37].strip()
```

Now we are hoping to parse the uuid from in between the mixed output, and this is where the power of python excels

`r` reads what the server send us until it finds `"Please enter characters:: "` we got this from the logo() function.

`uuid` has our uuid extracted

```python
guess = flag+letter
    print(guess)
    p.sendline(guess.encode())
```

At the first loop `flag = shctf` and `letter = '{'`,  just send that `guess`, also print `guess` for debugging.

now the output should contain exactly 6 occurrences of my uuid

```python
    counter = all.count(uuid.encode())
    if counter > last_count:
        flag += letter
        if letter == '}':
            print(f'{flag = }')
            break
        last_count = counter
        letter = chars[0]
        guess = flag+letter
        continue
     else:
        p.close()
        letter = chars[chars.find(letter)+1]
        guess = flag+letter
        continue
```

counter counts how many uuids the output has, based on it it determent if the last letter guessed is in the flag or not, if its not then try again with the next letter, keep looping until the letter is `}` and its in the flag.

test run:

```python
.
.
.
shctf{j
[x] Receiving all data
[+] Opening connection to spaceheroes-cryptographic-space-rover.chals.io on port 443: Done
shctf{k
[x] Receiving all data
[+] Opening connection to spaceheroes-cryptographic-space-rover.chals.io on port 443: Done
shctf{l
[x] Receiving all data
[+] Opening connection to spaceheroes-cryptographic-space-rover.chals.io on port 443: Done
shctf{m
[x] Receiving all data
[+] Opening connection to spaceheroes-cryptographic-space-rover.chals.io on port 443: Done
shctf{ma # last_count now equels 7
[x] Receiving all data
[+] Opening connection to spaceheroes-cryptographic-space-rover.chals.io on port 443: Done
shctf{mb
[x] Receiving all data
[+] Opening connection to spaceheroes-cryptographic-space-rover.chals.io on port 443: Done
shctf{mc
.
.
etc
```

Flag ---> shctf{met30rs_4r3nt_as_b4d_4s_sl0w_cpu}
