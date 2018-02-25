def determinants():
    print("Szukanie rozwiązań układu równań o posataci:\n/ Ax+By=C\n\ Dx+Ex=F\n")
    A = float(input("Podaj A: "))
    B = float(input("Podaj B: "))
    C = float(input("Podaj C: "))
    D = float(input("Podaj D: "))
    E = float(input("Podaj E: "))
    F = float(input("Podaj F: "))
    main_determinant=A*E-B*D
    x_determinant=C*E-F*B
    y_determinant=A*F-D*C

    if main_determinant == 0 and x_determinant == y_determinant == 0:
        print("Układ nieoznaczony")
    elif main_determinant == 0 and (x_determinant != 0 or y_determinant != 0):
        print("Układ sprzeczny")
    else:
        print("X wynosi {0}\nY wynosi {1}".format(round(x_determinant/main_determinant,3),round(y_determinant/main_determinant,3)))

determinants()
