grammar myLanguage;

// --- СИНТАКСИЧЕСКИЙ АНАЛИЗАТОР (Парсер) ---

// Начальный символ (<программа>)
program
    : statement EOF
    ;

// <оператор>
statement
    : 'if' '(' condition ')' statement                     # IfStat
    | 'if' '(' condition ')' statement 'else' statement    # IfElseStat
    | 'print' '(' expression ')' ';'                       # PrintStat
    ;

// <условие>
condition
    : left=expression '<' right=expression                 # LessCond
    | left=expression '==' right=expression                # EqualCond
    ;

// <выражение>
expression
    : INT                                                  # IntExpr
    ;

// --- ЛЕКСИЧЕСКИЙ АНАЛИЗАТОР (Сканер) ---

IF    : 'if' ;
ELSE  : 'else' ;
PRINT : 'print' ;
INT   : [0-9]+ ; // Терминал I (целое число)

// Пропуск пробелов, табуляций и переносов строк
WS    : [ \t\r\n]+ -> skip ;