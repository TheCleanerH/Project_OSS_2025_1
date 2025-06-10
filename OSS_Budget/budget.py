import datetime
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

    
