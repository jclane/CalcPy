class Calc(ast.NodeVisitor):
    """
    Evaluates string equation and adheres to order of operations.

    !CURRENTLY UNUSED!
    This was used by do_maths, but I switched to 'eval' since
    I didn't write this and didn't understand how it worked.

    Stolen from:
    https://stackoverflow.com/questions/33029168/how-to-calculate-an-equation-in-a-string-python
    """
    OP_MAP = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.LShift: operator.lshift,
        ast.RShift: operator.rshift,
        ast.Invert: operator.neg,
    }

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return Calc.OP_MAP[type(node.op)](left, right)

    def visit_Num(self, node):
        return node.n

    def visit_Expr(self, node):
        return self.visit(node.value)

    @classmethod
    def evaluate(cls, expression):
        tree = ast.parse(expression)
        calc = cls()
        return calc.visit(tree.body[0])
