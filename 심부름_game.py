print("원하시는 물품을 심부름 목록으로 설정해 주십시오.(최대 5개)")
input("물품의 이름 : ")
A=int(input("물품의 가격(원) : "))
B=input("선택한 물품을 심부름 목록으로 설정하시겠습니까? yes or no : ")
if B=="yes":
    print("심부름 목록으로 설정되었습니다. (현재 누적 금액:",A,"원)")
    C=input("다른 물품을 추가하시겠습니까? yes or no : ")
    if C=="yes":
        input("물품의 이름 : ")
        A_2=int(input("물품의 가격(원) : "))
        B_2=input("선택한 물품을 심부름 목록으로 설정하시겠습니까? yes or no : ")
        if B_2=="yes":
            print("심부름 목록으로 설정되었습니다. (현재 누적 금액:",A+A_2,"원)")
            C_2=input("다른 물품을 추가하시겠습니까? yes or no : ")
            if C_2=="yes":
                input("물품의 이름 : ")
                A_3=int(input("물품의 가격(원) : "))
                B_3=input("선택한 물품을 심부름 목록으로 설정하시겠습니까? yes or no : ")
                if B_3=="yes":
                    print("심부름 목록으로 설정되었습니다. (현재 누적 금액:",A+A_2+A_3,"원)")
                    C_3=input("다른 물품을 추가하시겠습니까? yes or no : ")
                    if C_3=="yes":
                        input("물품의 이름 : ")
                        A_4=int(input("물품의 가격(원) : "))
                        B_4=input("선택한 물품을 심부름 목록으로 설정하시겠습니까? yes or no : ")
                        if B_4=="yes":
                            print("심부름 목록으로 설정되었습니다. (현재 누적 금액:",A+A_2+A_3+A_4,"원)")
                            C_4=input("다른 물품을 추가하시겠습니까? yes or no : ")
                            if C_4=="yes":
                                input("물품의 이름 : ")
                                A_5=int(input("물품의 가격(원) : "))
                                B_5=input("선택한 물품을 심부름 목록으로 설정하시겠습니까? yes or no : ")
                                if B_5=="yes":
                                    print("심부름 목록으로 설정되었습니다. (현재 누적 금액:",A+A_2+A_3+A_4+A_5,"원)")
                                    print("더이상 목록 추가가 불가능 합니다.")
                                    print("최종금액:",A+A_2+A_3+A_4+A_5,"원")
                                    while True:
                                        D=int(input("지불할 금액을 입력해주십시오(원) : "))
                                        E=(D-(A+A_2+A_3+A_4+A_5))
                                        if E>=0:
                                            print("거스름돈은",E,"원 입니다.")
                                            break
                                        else:
                                            print("금액이 부족합니다.")
                                if B_5=="no":
                                    print("취소되었습니다.")
                                    print("최종금액:",A+A_2+A_3+A_4,"원")
                                    while True:
                                        D=int(input("지불할 금액을 입력해주십시오(원) : "))
                                        E=(D-(A+A_2+A_3+A_4))
                                        if E>=0:
                                            print("거스름돈은",E,"원 입니다.")
                                            break
                                        else:
                                            print("금액이 부족합니다.")
                            if C_4=="no":
                                print("취소되었습니다.")
                                print("최종금액:",A+A_2+A_3+A_4,"원")
                                while True:
                                    D=int(input("지불할 금액을 입력해주십시오(원) : "))
                                    E=(D-(A+A_2+A_3+A_4))
                                    if E>=0:
                                        print("거스름돈은",E,"원 입니다.")
                                        break
                                    else:
                                        print("금액이 부족합니다.")
                        if B_4=="no":
                            print("최종금액:",A+A_2+A_3,"원")
                            while True:
                                D=int(input("지불할 금액을 입력해주십시오(원) : "))
                                E=(D-(A+A_2+A_3))
                                if E>=0:
                                    print("거스름돈은",E,"원 입니다.")
                                    break
                                else:
                                    print("금액이 부족합니다.")
                    if C_3=="no":
                        print("취소되었습니다.")
                        print("최종금액:",A+A_2+A_3,"원")
                        while True:
                            D=int(input("지불할 금액을 입력해주십시오(원) : "))
                            E=(D-(A+A_2+A_3))
                            if E>=0:
                                print("거스름돈은",E,"원 입니다.")
                                break
                            else:
                                print("금액이 부족합니다.")
                if B_3=="no":
                    print("최종금액:",A+A_2,"원")
                    while True:
                        D=int(input("지불할 금액을 입력해주십시오(원) : "))
                        E=(D-(A+A_2))
                        if E>=0:
                            print("거스름돈은",E,"원 입니다.")
                            break
                        else:
                            print("금액이 부족합니다.")
            if C_2=="no":
                print("취소되었습니다.")
                print("최종금액:",A+A_2,"원")
                while True:
                    D=int(input("지불할 금액을 입력해주십시오(원) : "))
                    E=(D-(A+A_2))
                    if E>=0:
                        print("거스름돈은",E,"원 입니다.")
                        break
                    else:
                        print("금액이 부족합니다.")
        if B_2=="no":
            print("취소되었습니다.")
            print("최종금액:",A,"원")
            while True:
                D=int(input("지불할 금액을 입력해주십시오(원) : "))
                E=(D-A)
                if E>=0:
                    print("거스름돈은",E,"원 입니다.")
                    break
                else:
                    print("금액이 부족합니다.")
    if C=="no":
        print("심부름 목록 설정을 종료합니다.")
        print("최종금액:",A,"원")
        while True:
            D=int(input("지불할 금액을 입력해주십시오(원) : "))
            E=int(D-A)
            if E>=0:
                print("거스름돈은",E,"원 입니다.")
                break
            else:
                print("금액이 부족합니다.")
if B=="no":
    print("취소되었습니다")
