import datetime
import json
import os
from datetime import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def category_summary(self):
        """종류별 지출 통계를 보여준다"""
        if not self.expenses:
            print("잠시 지출 기록이 없다.\n")
            return
    
        # 지출내역을 분류하다
        category_totals = {}
        for expense in self.expenses:
        if expense.category in category_totals:
            category_totals[expense.category] += expense.amount
        else:
            category_totals[expense.category] = expense.amount
    
        total_amount = sum(category_totals.values())
    
        print("\n[지출유형통계]")
        print("-" * 40)
        for category, amount in sorted(category_totals.items()):
            percentage = (amount / total_amount) * 100 if total_amount > 0 else 0
            print(f"{category}: {amount:,}元 ({percentage:.1f}%)")
        print("-" * 40)
        print(f"총지출: {total_amount:,}원\n")

    def monthly_summary(self):
        """월별 지출 통계를 보이다"""
        if not self.expenses:
        print("잠시 지출 기록이 없다.\n")
        return
    
        monthly_totals = {}
        for expense in self.expenses:
        month = expense.date[:7]  # YYYY-MM 
        if month in monthly_totals:
            monthly_totals[month] += expense.amount
        else:
            monthly_totals[month] = expense.amount
    
        print("\n[월별 지출 통계]")
        print("-" * 30)
        for month, amount in sorted(monthly_totals.items()):
        print(f"{month}: {amount:,}원")
        print("-" * 30)
        print()

    def search_expenses(self, keyword):
        """지출 내역을 검색하다"""
        if not self.expenses:
            print("잠시 지출 기록이 없다.\n")
            return
    
        matching_expenses = []
        for expense in self.expenses:
            if (keyword.lower() in expense.category.lower() or 
                keyword.lower() in expense.description.lower()):
                matching_expenses.append(expense)
        
        if not matching_expenses:
            print(f"'{keyword}'가 포함된 지출 기록을 찾을 수 없습니다.\n")
            return
    
        print(f"\n[검색 결과: '{keyword}']")
        for idx, expense in enumerate(matching_expenses, 1):
            print(f"{idx}. {expense}")
        print()
        
    def save_to_file(self, filename="budget_data.json"):
        """지출 자료를 파일로 저장한다"""
        try:
            data = []
            for expense in self.expenses:
                data.append({
                    'date': expense.date,
                    'category': expense.category,
                    'description': expense.description,
                    'amount': expense.amount
                })
        
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        
            print(f"데이터가 저장되었습니다 {filename}。\n")
        except Exception as e:
            print(f"저장 실패: {e}\n")

    def load_from_file(self, filename="budget_data.json"):
        """파일에서 지출 데이터를 불러옵니다"""
        try:
            if not os.path.exists(filename):
                print(f"파일 {filename}이 존재하지 않는다.\n")
                return False
        
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
        
            self.expenses = []
            for item in data:
                expense = Expense(
                    item['date'],
                    item['category'], 
                    item['description'],
                    item['amount']
                )
                self.expenses.append(expense)
        
            print(f"{filename}에서 {len(self-expenses)} 항목의 지출 레코드를 성공적으로 불러왔습니다.\n")
            return True
        except Exception as e:
            print(f"불러오는 데 실패했습니다: {e}\n")
            return False

    def export_to_csv(self, filename="budget_export.csv"):
        """데이터를 csv 형식으로 내보낸다"""
        try:
            with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow([날짜, 분류, 설명, 금액.])
            
                for expense in self.expenses:
                    writer.writerow([
                        expense.date,
                        expense.category,
                        expense.description,
                        expense.amount
                    ])
            
            print(f"데이터가 {filename}로 내보내졌다.\n")
        except Exception as e:
            print(f"내보내기 실패: {e}\n")

    def backup_data(self):
        """데이터 백업 만들기"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"budget_backup_{timestamp}.json"
            self.save_to_file(backup_filename)
            print(f"백업이 생성됨: {backup_filename}\n")
        except Exception as e:
            print(f"백업 실패: {e}\n")

    def delete_expense(self, index):
        """지정된 지출 기록을 삭제합니다"""
        try:
            if 1 <= index <= len(self.expenses):
                deleted_expense = self.expenses.pop(index - 1)
                print(f"지출 기록이 삭제되었습니다: {deleted_expense}\n")
                return True
            else:
                print("레코드 번호가 잘못되었습니다.\n")
                return False
        except Exception as e:
            print(f"삭제 실패: {e}\n")
            return False

    
