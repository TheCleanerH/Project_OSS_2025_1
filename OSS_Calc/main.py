import tkinter as tk
from calc import Calculator

def test_calculator_functions():
    print("=== 과학적 계산기 기능 시험 ===")
    print("1. 기본 연산: 2+3×4-1 = 13")
    print("2. 과학적 계산:")
    print("   - 제곱근: √16 = 4")
    print("   - 제곱: 5² = 25")
    print("   - 큐 브: 2³ = 8")
    print("   - 삼각 함수: sin(30°) ≈ 0.5")
    print("   - 로그: log(100) = 2")
    print("   - 자연 로그: ln(e) = 1")
    print("   - 계승: 5! = 120")
    print("3. 메모리 기능:ms (메모리) → mr (호출)")
    print("4.과거 기록:최근 계산을 표시합니다")

if __name__ == "__main__":
    test_calculator_functions()
    
    try:
        root = tk.Tk()
        calc = Calculator(root)
        root.mainloop()
        
    except Exception as e:
        print(f"계산기를 시작하는 중 오류 발생:{e}")
