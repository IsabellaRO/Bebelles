global table
global dec
table = {}
dec = {}

class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

class Ident():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print("passei por aqui")
        print(table)
        print("->{}".format(table[self.value]))
        return table[str(self.value)]


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mult(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() // self.right.eval()

class GreaterThan(BinaryOp):
    def eval(self):
        return self.left.eval() > self.right.eval()

class LessThan(BinaryOp):
    def eval(self):
        return self.left.eval() < self.right.eval()

class Equal(BinaryOp):
    def eval(self):
        print("entrei no equal")
        return self.left.eval() == self.right.eval()
    
class Assign(BinaryOp):
    def eval(self):
        table[self.left.value] = self.right.eval()
        print("dei assign")
        print(table)
        return self.right.eval()

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print("printando")
        print("resultado: {}".format(self.value.eval()))