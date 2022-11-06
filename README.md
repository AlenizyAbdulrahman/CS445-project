# CS445-project

## This is grammar before making it LL (1):

PROGRAM → STMTS \n
STMTS → STMT| STMT ; STMTS
STMT → id = EXPR
EXPR → EXPR + TERM | EXPR - TERM | TERM
TERM → TERM * FACTOR | TERM / FACTOR | FACTOR
FACTOR → ( EXPR ) | id | integer

## After modifying the grammar to add the power operator (^) and unary sign operators + and -:

PROGRAM -> STMTS
STMTS -> STMT | STMT ; STMTS
STMT -> id = EXPR
EXPR -> EXPR + TERM | EXPR - TERM | TERM
TERM -> TERM * CURR | TERM / CURR | CURR
CURR -> TEMP ^ CURR | TEMP
TEMP -> ++ FACTOR | -- FACTOR | FACTOR
FACTOR -> ( EXPR ) | id | integer

## After elimination of left-recursion:

PROGRAM -> STMTS
STMTS -> STMT | STMT ; STMTS
STMT -> id = EXPR
EXPR -> TERM EXPR'
TERM -> FACTOR TERM'
FACTOR -> CURR ^ FACTOR | CURR
CURR -> ++ TEMP | -- TEMP | TEMP
TEMP -> ( EXPR ) | id | integer
EXPR' -> + TERM EXPR' | - TERM EXPR' | ϵ
TERM' -> * FACTOR TERM' | / FACTOR TERM' | ϵ
