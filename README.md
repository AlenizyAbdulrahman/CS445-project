# CS445-project

## This is grammar before making it LL (1):

 
PROGRAM → STMTS <br>
STMTS → STMT| STMT ; STMTS <br>
STMT → id = EXPR <br>
EXPR → EXPR + TERM | EXPR - TERM | TERM <br>
TERM → TERM * FACTOR | TERM / FACTOR | FACTOR <br>
FACTOR → ( EXPR ) | id | integer


## After modifying the grammar to add the power operator (^) and unary sign operators (+, -):

PROGRAM -> STMTS <br>
STMTS -> STMT | STMT ; STMTS <br>
STMT -> id = EXPR <br>
EXPR -> EXPR + TERM | EXPR - TERM | TERM <br>
TERM -> TERM * CURR | TERM / CURR | CURR <br>
CURR -> TEMP ^ CURR | TEMP <br>
TEMP -> ++ FACTOR | -- FACTOR | FACTOR <br>
FACTOR -> ( EXPR ) | id | integer <br>

## After elimination of left-recursion:

PROGRAM -> STMTS <br>
STMTS -> STMT | STMT ; STMTS <br>
STMT -> id = EXPR <br>
EXPR -> TERM EXPR' <br>
TERM -> FACTOR TERM' <br>
FACTOR -> CURR ^ FACTOR | CURR <br>
CURR -> ++ TEMP | -- TEMP | TEMP <br>
TEMP -> ( EXPR ) | id | integer <br>
EXPR' -> + TERM EXPR' | - TERM EXPR' | ϵ <br>
TERM' -> * FACTOR TERM' | / FACTOR TERM' | ϵ <br>

## After left-factoring:

PROGRAM -> STMTS <br>
STMTS -> STMT STMTS' <br>
STMT -> id = EXPR <br>
EXPR -> TERM EXPR' <br>
TERM -> FACTOR TERM' <br>
FACTOR -> CURR FACTOR' <br>
CURR -> ++ TEMP | -- TEMP | TEMP <br>
TEMP -> ( EXPR ) | id | integer <br>
EXPR' -> + TERM EXPR' | - TERM EXPR' | ϵ <br>
TERM' -> * FACTOR TERM' | / FACTOR TERM' | ϵ <br>
STMTS' -> ϵ | ; STMTS <br>
FACTOR' -> ^ FACTOR | ϵ <br>
