%{
#include <string>
#include "node.h"
#include "parser.hpp"
#define SAVE_TOKEN yylval.string = new std::string(yytext, yyleng)
#define TOKEN(t) (yylval.token = t)
extern "C" int yywrap() { }
%}

%%
"true" {return TRUE;}
"false" {return FALSE;}
"print" {return PRINT;}
"(" {return OPENPAR;}
")" {return CLOSEPAR;}
"+" {return PLUS;}
"-" {return MINUS;}
"*" {return MULT;}
"/" {return DIV;}
"=" {return ASSIGN;}
"end" {return END;}
"if" {return IF;}
"else" {return ELSE;}
">" {return GREATERTHAN;}
"<" {return LESSTHAN;}
"," {return COMMA;}
":" {return COLON;}
"and" {return AND;}
"or" {return OR;}
"not" {return NOT;}
"def" {return DEF;}
"void" {return VOID;}
"integer" {return INTEGER;}
"boolean" {return BOOLEAN;}
"while" {return WHILE;}
"wend" {return WEND;}
"input" {return INPUT;}
"as" {return AS;}
"call" {return CALL;}
[ \t\n];

[a-zA-Z_][a-zA-Z0-9_]*  SAVE_TOKEN; return IDENTIFIER;
[0-9]+                  SAVE_TOKEN; return INTEGER;

. printf("Token desconhecido!n"); yyterminate();

%%
