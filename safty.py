def calculate_mildo(mass, volume):
    mildo = mass / volume
    return mildo

def calculate_molar(mass, moles):
    molar = mass / moles
    return molar

def main():
    print("화학물질 특성 계산기")

    while True:
        print("1. 밀도 계산")
        print("2. 몰 질량 계산")
        print("3. 종료")

        choice = input("선택 (1/2/3): ")

        if choice == '1':
            mass = float(input("질량(g): "))
            volume = float(input("부피(L): "))

            mildo = calculate_mildo(mass, volume)
            print(f"밀도(g/L): {mildo}")

        elif choice == '2':
            mass = float(input("질량(g): "))
            moles = float(input("몰 개수(mol): "))

            molar = calculate_molar(mass, moles)
            print(f"몰 질량(g/mol): {molar}")

        elif choice == '3':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 1, 2, 3 중에서 선택하세요.")

if __name__ == "__main__":
    main()
