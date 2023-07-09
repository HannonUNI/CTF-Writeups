
import marshal
import base64
import dis

bytecode = marshal.loads(base64.b64decode("4wAAAAAAAAAAAAAAAAAAAAAFAAAAQAAAAHNgAAAAZABkAWwAWgBlAWQCgwFaAmQDWgNlAkQAXRJaBGUFZQSDAWQEQQBaBmUGZAUXAFoHZQNlCGUHgwE3AFoDcQxlAKAJZQplA2QGgwKhAVoDZQtlA6AMZAahAYMBAQBkAVMAKQfpAAAAAE56EWVudGVyIHRoZSBzYXVjZTog2gBpNxMAAOlBAAAAegV1dGYtOCkN2gZiYXNlNjTaBWlucHV02gRmbGFnWgNlbmPaAWnaA29yZNoFZmlyc3RaBnNlY29uZNoDY2hy2gliNjRlbmNvZGXaBWJ5dGVz2gVwcmludNoGZGVjb2RlqQByDwAAAHIPAAAA+ghjaGFsbC5wedoIPG1vZHVsZT4BAAAAcxIAAAAIAAgCBAIIAgwBCAEOARACEgI="))
dis.dis(bytecode)


# 1           0 LOAD_CONST               0 (0)
#               2 LOAD_CONST               1 (None)
#               4 IMPORT_NAME              0 (base64)
#               6 STORE_NAME               0 (base64)

#   3           8 LOAD_NAME                1 (input)
#              10 LOAD_CONST               2 ('enter the sauce: ')
#              12 CALL_FUNCTION            1
#              14 STORE_NAME               2 (flag)

#   5          16 LOAD_CONST               3 ('')
#              18 STORE_NAME               3 (enc)

#   7          20 LOAD_NAME                2 (flag)
#              22 GET_ITER
#         >>   24 FOR_ITER                18 (to 62)
#              26 STORE_NAME               4 (i)

#   8          28 LOAD_NAME                5 (ord)
#              30 LOAD_NAME                4 (i)
#              32 CALL_FUNCTION            1
#              34 LOAD_CONST               4 (4919)
#              36 BINARY_XOR
#              38 STORE_NAME               6 (first)

#   9          40 LOAD_NAME                6 (first)
#              42 LOAD_CONST               5 (65)
#              44 BINARY_ADD
#              46 STORE_NAME               7 (second)

#  10          48 LOAD_NAME                3 (enc)
#              50 LOAD_NAME                8 (chr)
#              52 LOAD_NAME                7 (second)
#              54 CALL_FUNCTION            1
#              56 INPLACE_ADD
#              58 STORE_NAME               3 (enc)
#              60 JUMP_ABSOLUTE           12 (to 24)

#  12     >>   62 LOAD_NAME                0 (base64)
#              64 LOAD_METHOD              9 (b64encode)
#              66 LOAD_NAME               10 (bytes)
#              68 LOAD_NAME                3 (enc)
#              70 LOAD_CONST               6 ('utf-8')
#              72 CALL_FUNCTION            2
#              74 CALL_METHOD              1
#              76 STORE_NAME               3 (enc)

#  14          78 LOAD_NAME               11 (print)
#              80 LOAD_NAME                3 (enc)
#              82 LOAD_METHOD             12 (decode)
#              84 LOAD_CONST               6 ('utf-8')
#              86 CALL_METHOD              1
#              88 CALL_FUNCTION            1
#              90 POP_TOP
#              92 LOAD_CONST               1 (None)
#              94 RETURN_VALUE
