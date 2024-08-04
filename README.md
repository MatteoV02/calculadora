Integrantes: Juan Felipe Rojas, Daniel Leonardo Mora, Andres Felipe Garcia, Eduardo Mateo Vanegas

Pasos para correr calculaodra python-antlr4.

1. Tener instalado antlr4
2. Instalar python para antlr4 comando ->pip3 install antlr4-python3-runtime
3. Generar el parser y lexer  comando-> vantlr4 -Dlanguage=Python3 Calculantlr.g4 -visitor -o dist (va generar un directorio)
4. Cada vez que se modifique el archivo Calculantlr.g4 volver hacer el paso 3 
5. Crear archivo _init_.py
6. Crear main.py 
5. ejecutar: python3 main.py


Estas son las expresiones que se pueden utilizar en la calculadora: 

expr ('*'|'/')   # MulDivExpr
expr ('+'|'-')    # AddSubExpr
expr ('>'|'>='|'<'|'<=') expr  # ComparisonExpr
expr('=='|'!=') # EqualityExpr
expr '&&' # AndExpr
expr '||' # OrExpr
expr '~' # NandExpr
expr '?' # XorExpr
