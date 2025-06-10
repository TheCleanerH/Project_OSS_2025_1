from budget import Budget

def main():
    budget = Budget()

    print("데이터 불러오는 중...")
    budget.load_from_file()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        print("4. 지출유형통계") 
        print("5. 월별 지출 통계") 
        print("6. 지출 내역을 검색하다") 
        print("7. 删除支出记录")  # 신규 증가
        print("8. 保存数据")      # 신규 증가
        print("9. 加载数据")      # 신규 증가
        print("10. 导出CSV")     # 신규 증가
        print("11. 创建备份")    # 신규 증가
        print("12. 退出")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()
            
        elif choice == "4":
            budget.category_summary()

        elif choice == "5":
            budget.monthly_summary()

        elif choice == "6":
            keyword = input("검색어를 입력하세요: ").strip()
            if keyword:
                budget.search_expenses(keyword)
            else:
                print("키워드는 비어 있으면 안 됩니다.\n")
                
        elif choice == "7":
            budget.list_expenses()
            if budget.expenses:
                try:
                    index = int(input("삭제할 레코드 번호를 입력하십시오: "))
                    budget.delete_expense(index)
                except ValueError:
                    print("올바른 번호를 입력하십시오.\n")

        elif choice == "8":
            filename = input("파일 이름 저장 (기본값:budget_data.json): ").strip()
            if not filename:
                filename = "budget_data.json"
            budget.save_to_file(filename)

        elif choice == "9":
            filename = input("파일 이름 불러오기 (기본값:budget_data.json):").strip()
            if not filename:
                filename = "budget_data.json"
            budget.load_from_file(filename)

        elif choice == "10":
            filename = input("csv 파일 이름 (기본값:budget_export.csv):").strip()
            if not filename:
                filename = "budget_export.csv"
            budget.export_to_csv(filename)

        elif choice == "11":
            budget.backup_data()

        elif choice == "12":
            # 종료하기 전에 자동으로 저장합니다
            print("데이터를 저장하는 중...")
            budget.save_to_file()
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
