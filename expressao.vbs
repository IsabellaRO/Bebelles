Def Soma(Integer x, Integer y) as Integer
    Integer a
    a = x + y
    Print (a)
    Soma = a
End Def
Void Main()
    Integer a
    Integer b
    Boolean c
    a = 0
    while (a < 3):
        a = a + 1
    wend
    b = Soma(a, 4)
    c = True
    Print(a)
    Print(b)
    if (c):
        Print (not c)
    end if
End Void