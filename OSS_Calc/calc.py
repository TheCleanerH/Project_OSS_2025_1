import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("과학적 계산기")
        self.root.geometry("500x600")
        self.root.configure(bg='#2b2b2b')

        self.expression = ""
        self.result_var = tk.StringVar()
        self.history = []
        self.memory = 0

        self.create_widgets()

    def create_widgets(self):
        # 영역 보이기
        display_frame = tk.Frame(self.root, bg='#2b2b2b')
        display_frame.pack(fill="x", padx=10, pady=10)

        # 메인 모니터
        self.entry = tk.Entry(
            display_frame, 
            font=("Arial", 24), 
            justify="right", 
            textvariable=self.result_var,
            bg='#404040',
            fg='white',
            insertbackground='white',
            bd=0
        )
        self.entry.pack(fill="both", ipady=15)

        # 과거 기록을 보면
        self.history_label = tk.Label(
            display_frame,
            text="과거 기록:없음",
            font=("Arial", 10),
            bg='#2b2b2b',
            fg='gray',
            anchor='e'
        )
        self.history_label.pack(fill="x", pady=(5, 0))

        # 과학 계산 단추 영역입니다
        sci_frame = tk.Frame(self.root, bg='#2b2b2b')
        sci_frame.pack(fill="x", padx=10, pady=5)
        
        sci_buttons = [
            ['sin', 'cos', 'tan', 'log', 'ln'],
            ['√', 'x²', 'x³', 'xʸ', '1/x'],
            ['π', 'e', '(', ')', 'n!']
        ]
        
        for row in sci_buttons:
            frame = tk.Frame(sci_frame, bg='#2b2b2b')
            frame.pack(fill="x")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 12),
                    command=lambda ch=char: self.on_scientific_click(ch),
                    width=8,
                    height=1,
                    bg='#404040',
                    fg='white',
                    activebackground='#505050',
                    bd=1,
                    relief='raised'
                )
                btn.pack(side="left", expand=True, fill="both", padx=1, pady=1)

        #기본 계산 단추 영역입니다
        basic_frame = tk.Frame(self.root, bg='#2b2b2b')
        basic_frame.pack(expand=True, fill="both", padx=10, pady=5)

        buttons = [
            ['제거', '삭제', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]

        for row in buttons:
            frame = tk.Frame(basic_frame, bg='#2b2b2b')
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == '=':
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 18),
                        command=lambda ch=char: self.on_click(ch),
                        bg='#ff9500',
                        fg='white',
                        activebackground='#ffad33',
                        bd=1,
                        relief='raised'
                    )
                elif char in ['제거', '삭제', '%', '÷', '×', '-', '+']:
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 14),
                        command=lambda ch=char: self.on_click(ch),
                        bg='#505050',
                        fg='white',
                        activebackground='#606060',
                        bd=1,
                        relief='raised'
                    )
                else:
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 16),
                        command=lambda ch=char: self.on_click(ch),
                        bg='#666666',
                        fg='white',
                        activebackground='#777777',
                        bd=1,
                        relief='raised'
                    )
                btn.pack(side="left", expand=True, fill="both", padx=1, pady=1)

        # 메모리 기능 단추
        memory_frame = tk.Frame(self.root, bg='#2b2b2b')
        memory_frame.pack(fill="x", padx=10, pady=5)
        
        memory_buttons = ['MC', 'MR', 'M+', 'M-', 'MS']
        
        for char in memory_buttons:
            btn = tk.Button(
                memory_frame,
                text=char,
                font=("Arial", 10),
                command=lambda ch=char: self.on_memory_click(ch),
                width=8,
                bg='#404040',
                fg='yellow',
                activebackground='#505050',
                bd=1,
                relief='raised'
            )
            btn.pack(side="left", expand=True, fill="both", padx=1, pady=1)

    def on_click(self, char):
        if char == '제거':
            self.expression = ""
        elif char == '삭제':
            self.expression = self.expression[:-1]
        elif char == '=':
            self.calculate()
        elif char == '%':
            try:
                if self.expression:
                    result = float(self.expression) / 100
                    self.expression = str(result)
            except:
                self.expression = "오류"
        elif char == '±':
            try:
                if self.expression and self.expression != "오류":
                    if self.expression.startswith('-'):
                        self.expression = self.expression[1:]
                    else:
                        self.expression = '-' + self.expression
            except:
                pass
        elif char == '÷':
            self.expression += '/'
        elif char == '×':
            self.expression += '*'
        else:
            self.expression += str(char)

        self.result_var.set(self.expression)

    def on_scientific_click(self, char):
        try:
            current_val = self.expression
            
            if char == 'sin':
                if current_val:
                    result = math.sin(math.radians(float(current_val)))
                    self.expression = str(result)
            elif char == 'cos':
                if current_val:
                    result = math.cos(math.radians(float(current_val)))
                    self.expression = str(result)
            elif char == 'tan':
                if current_val:
                    result = math.tan(math.radians(float(current_val)))
                    self.expression = str(result)
            elif char == 'log':
                if current_val and float(current_val) > 0:
                    result = math.log10(float(current_val))
                    self.expression = str(result)
            elif char == 'ln':
                if current_val and float(current_val) > 0:
                    result = math.log(float(current_val))
                    self.expression = str(result)
            elif char == '√':
                if current_val and float(current_val) >= 0:
                    result = math.sqrt(float(current_val))
                    self.expression = str(result)
            elif char == 'x²':
                if current_val:
                    result = float(current_val) ** 2
                    self.expression = str(result)
            elif char == 'x³':
                if current_val:
                    result = float(current_val) ** 3
                    self.expression = str(result)
            elif char == 'xʸ':
                self.expression += '**'
            elif char == '1/x':
                if current_val and float(current_val) != 0:
                    result = 1 / float(current_val)
                    self.expression = str(result)
            elif char == 'π':
                self.expression += str(math.pi)
            elif char == 'e':
                self.expression += str(math.e)
            elif char == 'n!':
                if current_val:
                    num = int(float(current_val))
                    if 0 <= num <= 20:
                        result = math.factorial(num)
                        self.expression = str(result)
                    else:
                        self.expression = "범위가 제한을 초과하다."
            elif char in ['(', ')']:
                self.expression += char
            
            self.result_var.set(self.expression)
            
        except Exception as e:
            self.expression = "오류"
            self.result_var.set(self.expression)

    def on_memory_click(self, char):
        try:
            current_val = float(self.expression) if self.expression and self.expression != "오류" else 0
            
            if char == 'MC':  # Memory Clear
                self.memory = 0
            elif char == 'MR':  # Memory Recall
                self.expression = str(self.memory)
            elif char == 'M+':  # Memory Add
                self.memory += current_val
            elif char == 'M-':  # Memory Subtract
                self.memory -= current_val
            elif char == 'MS':  # Memory Store
                self.memory = current_val
            
            self.result_var.set(self.expression)
            
        except:
            pass

    def calculate(self):
        try:
            # 과거 기록
            original_expr = self.expression
            
            # 특수 부호 처리
            expr = self.expression.replace('π', str(math.pi))
            expr = expr.replace('e', str(math.e))
            expr = expr.replace('×', '*')
            expr = expr.replace('÷', '/')
            
            result = eval(expr)
            
            # 결과 포맷
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)
            
            # 역사기록에 추가합니다
            self.history.append(f"{original_expr} = {result}")
            if len(self.history) > 5:
                self.history.pop(0)
            
            self.expression = str(result)
            self.update_history_display()
            
        except Exception as e:
            self.expression = "오류"
        
        self.result_var.set(self.expression)

    def update_history_display(self):
        if self.history:
            recent = self.history[-1]
            self.history_label.config(text=f"역사: {recent}")
        else:
            self.history_label.config(text="과거 기록:없음")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
