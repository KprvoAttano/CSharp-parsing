from AST_classes.ast_expr_stmt_nodes import *


class ArrayNode(StmtNode):
    def __init__(self, vars_type: StmtNode,
                 row: Optional[int] = None, line: Optional[int] = None, **props):
        super().__init__(row=row, line=line, **props)
        self.vars_type = vars_type

    @property
    def childs(self) -> Tuple[ExprNode]:
        # return self.vars_type, (*self.vars_list)
        return (self.vars_type, )

    def __str__(self) -> str:
        return '[]'
