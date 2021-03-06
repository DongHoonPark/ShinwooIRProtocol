** Infrared signal is transmitted in reversed binary form.

```
C = Checksum --> sum of #3 ~ #17 hex value
U = Turbo 
O = ON/OF
I = Timer
T = Temperature
B = Blade
W = Wind (L/M/H)
M = Mode
S = Start
```


```
[Turbo OFF, Power ON, Timer unlimited, Temperature 05 celcius, Blade fixed, Wind midium, Cooling mode]
0x  2  9  8  1  8  1  0  0  0  c  0  0  0  5  1  4  1  c  c
#   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
?   C  C     U     O           I  I  I  T  T  B  W  M  S  S
```

### Options to be figured out

1. ON/ OFF Field
```
ON  : 0x298181000c0005141cc (1)
OFF : 0x308188000c0005141cc (8)
             v
```
--> #6 

2. Mode Field

```
Cooling : 0x278181000c0005121cc (1)
Heating : 0x298181000c0005123cc (3)
Fan     : 0x2d8181000c0005127cc (7)
                            v
```
--> #17 

3. Wind Field (AUTO, TURBO 포함)

```
Auto : 0x268181000c0005111cc (1)
Low  : 0x278181000c0005121cc (2)
Mid  : 0x298181000c0005141cc (4)
High : 0x2d8181000c0005181cc (8)
                        v
--> #16

Turbo: 0x348881000c0005181cc
            v
```

4. Temperature Field 


```
5 : 0x298181000c0005141cc (05)
6 : 0x2a8181000c0006141cc (06)
7 : 0x2b8181000c0007141cc (07)
18: 0x2d8181000c0018141cc (18)
                  vv
--> #13, 14
```

5. Timer Field

```
2 : 0x30818100007805181cc (h'078 -> 120)
3 : 0x3081810000b405181cc (h'0B4 -> 180)
4 : 0x3081810000f005181cc (h'0F0 -> 240)
5 : 0x30818100012c05181cc (h'12C -> 300)
               vvv
--> #10, 11, 12
```

6. Blade moving

```
Fixed  : 0x2d8181000c0005181cc (1)
Moving : 0x2f8181000c0005381cc (3)
                         v
--> #15
```