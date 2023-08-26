score = float(input("이번 외국어 영역의 점수를 숫자만 입력해주세요."))

if score > 100 or score < 0:
    print("값을 제대로 입력해주세요.")

elif score >= 90:
    print("a반으로 가세요.")

elif score >= 80:
    print("b반으로 가세요.")

elif score >= 70:
    print("c반으로 가세요.")

elif score >= 60:
    print("d반으로 가세요.")

else:
    print("e반으로 가세요.")
