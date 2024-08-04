grammar Calculantlr;

// non-terminals expressed as context-free grammar (BNF)
expr:  '(' expr ')'             # ParenExpr
    |   '!' expr                 # NotExpr
    |   atom                     # AtomExpr
    |   expr op=('*'|'/') expr   # MulDivExpr
    |   expr op=('+'|'-') expr   # AddSubExpr
    |   expr op=('>'|'>='|'<'|'<=') expr  # ComparisonExpr
    |   expr op=('=='|'!=') expr  # EqualityExpr
    |   expr '&&' expr            # AndExpr
    |   expr '||' expr            # OrExpr
    |   expr '~' expr             # NandExpr
    |   expr '?' expr             # XorExpr
    ;

atom: INT
    | 'true'
    | 'false'
    ;

// tokens expressed as regular expressions
INT : [0-9]+ ;
WS  : [ \t]+ -> skip ;




