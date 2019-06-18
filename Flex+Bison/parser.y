%{
extern int yylex();
extern int yyparse();
extern FILE* yyin;
void yyerror(const char* s); { printf("ERROR: %sn", s); }
%}

%union {
  int number;
  string *strType; // goes with string_const in lex
}

%token<number> NUMBER

%token<strType> IDENTIFIER

%token TRUE FALSE PRINT OPENPAR CLOSEPAR PLUS MINUS MULT DIV ASSIGN END IF ELSE GREATERTHAN LESSTHAN COMMA COLON AND OR NOT DEF VOID INTEGER BOOLEAN WHILE WEND INPUT AS CALL

%left PLUS MINUS
%left MULT DIV

%start Program
%%
Program: VOID SubDec | DEF FuncDec;

SubDec: VOID IDENTIFIER OPENPAR ArgDec CLOSEPAR Stmts END VOID;

FuncDec: DEF IDENTIFIER OPENPAR ArgDec CLOSEPAR AS Type Stmts END DEF;

Statement: IDENTIFIER ASSIGN RelExpression | PRINT OPENPAR RelExpression CLOSEPAR | Type IDENTIFIER | WHILE OPENPAR RelExpression CLOSEPAR COLON Stmts WEND | IF OPENPAR RelExpression CLOSEPAR COLON Stmts END IF | IF OPENPAR RelExpression CLOSEPAR COLON Stmts ELSE Stmts END IF | CALL IDENTIFIER OPENPAR ArgDec CLOSEPAR;

RelExpression: Expression | Expression ASSIGN Expression | Expression GREATERTHAN Expression | Expression LESSTHAN Expression;

Expression: Term | Term PLUS Term | Term MINUS Term | Term OR Term ;

Term: Factor | Factor MULT Factor | Factor DIV Factor | Factor AND Factor;

Factor: NUMBER | TRUE | FALSE | INPUT | OPENPAR RelExpression CLOSEPAR | PLUS Factor | MINUS Factor | NOT Factor | IDENTIFIER | IDENTIFIER OPENPAR LoopRel CLOSEPAR ;

Type: INTEGER | BOOLEAN;

ArgDec: | Type IDENTIFIER | Type IDENTIFIER COMMA ArgDec;

LoopRel: | RelExpression | RelExpression COMMA LoopRel;

Stmts: Statement Stmts | Statement;
%%

int main() {
	yyin = stdin;
	do {
		yyparse();
	} while(!feof(yyin));
	return 0;
}
void yyerror(const char* s) {
	fprintf(stderr, "Parse error: %s\n", s);
	exit(1);
}
