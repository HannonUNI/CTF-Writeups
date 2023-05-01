# My God, it's full of .- ... -.-. .. .. (ez)

### Discription

If sound can't travel in a vacuum then how did a microphone pick this up in space unless space is a made up concept designed to make us fear leaving Earth and joining with Xenu and the Galactic Confederacy?

### Files

[signal.wav](https://drive.google.com/file/d/1IUiOTpiKNK5aGk0xX8bb7QcD_eN3EZN-/view?usp=share_link)

### Solution

I opened the file in Audacity applyed the spectogram view reduced the frequemcy to zoom in on the notes, and manually went over them and wrote them down:

![wordle](https://i.imgur.com/ifsokcz.png)

> .---..-- .--.-... .--...-- .---.-.. .--..--. .----.-- .-..---. ..--... ..-..... ..--...- ..-..... .--...-- ..--.-.. .--.---. ..-..... .-..-... ..--..-- ..--.-.. .---..-. ..-..... .---.-.- ..-..... ..---... ..--..-- ..--..-- .-.-.... .-.----- ..---... ..--.... ..--.... .---.... ..-.-... .-..-..- .--.---. ..-.-..- ..-..... ..----.. ..-..... ..-.---- .--..-.. .--..-.- .---.--. ..-.---- .--.---. .---.-.- .--.--.. .--.--.. .---..-- .---.... .--.----. .--...-- .--..-.- .-----.-

i went to [mores code decoder](https://www.dcode.fr/morse-code) and tried that but it didnt work so i assumed its binary, so i replaced every `.` with `0` and every `-` with a `1` and decoded that:

```python
with open('mores.txt','r') as f:
    text = f.readlines()
for i in text:
    print(chr(int(i, 2)), end='')
```

and that prints the flag :)
