
#include <stdio.h>

void FUN_0010127f(void);

unsigned int DAT_00104060[] = {
    0x24, 0x9c, 0x6a, 0x2a, 
    0x78, 0xa2, 0x1a, 0x0e, 
    0x8c, 0x6c, 0x0a, 0x0a, 
    0x88, 0x54, 0xb2, 0x2e, 
    0x1e, 0x0e, 0x78, 0x58, 
    0x06, 0xaa, 0x78, 0x96, 
    0xbe, 0xae, 0x40, 0xc8, 
    0x42, 0x68, 0x0a, 0x08, 
    0x6e, 
    };
  
unsigned int DAT_00104100[] = {
    0x5f, 0x2b, 0x41, 0x74, 
    0x7f, 0x05, 0x4b, 0x7c, 
    0x11, 0x05, 0x69, 0x69, 
    0x1b, 0x6e, 0x69, 0x79, 
    0x3c, 0x58, 0x68, 0x44, 
    0x32, 0x26, 0x63, 0x3c, 
    0x6b, 0x24, 0x7f, 0x33, 
    0x15, 0x46, 0x68, 0x71, 
    0x67, 0x7d, };
int main()
{
    int iVar1;
    int local_c;

    iVar1 = 0;

    if (iVar1 == 0)
    {
        printf("Access Granted!\n");

        for (local_c = 0; local_c < 0x22; local_c = local_c + 1)
        {
            *((int *)(&DAT_00104060) + local_c) = *((int *)(&DAT_00104060) + local_c) / 2;
        }
        FUN_0010127f();
    }

    return 0;
}

void FUN_0010127f(void)
{
    int local_c;
    unsigned int DAT_001041c0[0x22] = {0};

    for (local_c = 0; local_c < 0x22; local_c = local_c + 1)
    {
        *((unsigned int *)(&DAT_001041c0) + local_c) =
            *((unsigned int *)(&DAT_00104100) + local_c) ^ *((unsigned int *)(&DAT_00104060) + local_c);

        putchar(*((int *)(&DAT_001041c0) + local_c));
    }

    return;
}