import math

class Calculator:
    def __init__(self):
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else "Hata: Sıfıra bölme",
            '^': lambda x, y: x ** y,
            '√': lambda x: math.sqrt(x) if x >= 0 else "Hata: Negatif sayının karekökü alınamaz",
            '%': lambda x: x / 100,
            'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x)),
            'log': lambda x: math.log10(x) if x > 0 else "Hata: Geçersiz logaritma"
        }

    def calculate(self, expression):
        try:
            # Özel fonksiyonları işle
            for func in ['sin', 'cos', 'tan', 'log', '√']:
                if func in expression:
                    parts = expression.split(func)
                    if len(parts) == 2:
                        num = float(parts[1])
                        result = self.operations[func](num)
                        return str(result)
            for op in ['^', '*', '/', '+', '-']:
                if op in expression:
                    left, right = expression.split(op)
                    left, right = float(left), float(right)
                    return str(self.operations[op](left, right))
            if '%' in expression:
                num = float(expression.replace('%', ''))
                return str(self.operations['%'](num))
            return expression
        except ValueError:
            return "Hata: Geçersiz giriş"
        except ZeroDivisionError:
            return "Hata: Sıfıra bölme"
        except Exception as e:
            return f"Hata: {str(e)}"
