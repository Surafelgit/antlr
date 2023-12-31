grammar Expr;

prog: expr EOF;

expr: left=expr op='^' right=expr             #infixExpr
    | left=expr op=('+'|'-') right=expr       #infixExpr
    | left=expr op=('*'|'/') right=expr       #infixExpr
    | 'log(' expr ')'                        #logExpr
    | 'sin(' expr ')'                        #sinExpr
    | 'cos(' expr ')'                        #cosExpr
    | 'tan(' expr ')'                        #tanExpr
    | 'asin(' expr ')'                       #asinExpr
    | 'acos(' expr ')'                       #acosExpr
    | 'atan(' expr ')'                       #atanExpr
    | 'fac(' expr ')'                        #facExpr
    | 'sqrt(' expr ')'                       #sqrtExpr
    | 'cmtoin(' expr ')'                     #cmtoinExpr
    | 'mtoft(' expr ')'                      #mtoftExpr
    | 'kgtolb(' expr ')'                     #kgtolbExpr
    | INT                                     #numberExpr
    | '(' expr ')'                            #parensExpr
    ;

OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_POW: '^';

NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);
