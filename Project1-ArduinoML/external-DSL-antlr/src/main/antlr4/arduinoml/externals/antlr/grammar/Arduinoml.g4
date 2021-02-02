grammar Arduinoml;

/******************
 ** Parser rules **
 ******************/

root            :   declaration bricks states EOF;

declaration     :   'application' name=IDENTIFIER;

bricks          :   (sensor|actuator)+;
    sensor      :   'sensor'   location ;
    actuator    :   'actuator' location ;
    location    :   id=IDENTIFIER ':' port=NUMBER;

states          :   state+;
    state       :   initial? name=IDENTIFIER '{'  beep* action+ transition '}';
    beep        :   actuatorId=IDENTIFIER type=BEEP_TYPE quantity=NUMBER?;
    action      :   receiver=IDENTIFIER '<=' value=SIGNAL;
    transition  :   trigger=IDENTIFIER 'is' value=SIGNAL condition* '=>' next=IDENTIFIER ;
    condition   :   booleanOperator=BOOL trigger=IDENTIFIER 'is' value=SIGNAL ;
    initial     :   '->';

/*****************
 ** Lexer rules **
 *****************/

NUMBER     :   [1-9] | [1][0-3];
IDENTIFIER      :   LOWERCASE (LOWERCASE|UPPERCASE|DIGIT)+;
BEEP_TYPE       :   'LONGBEEP' | 'SHORTBEEP';

SIGNAL          :   'HIGH' | 'LOW';
BOOL            :   '&'    | '|';

/*************
 ** Helpers **
 *************/

fragment LOWERCASE  : [a-z];                                 // abstract rule, does not really exists
fragment UPPERCASE  : [A-Z];
fragment DIGIT     : [0-9];
NEWLINE             : ('\r'? '\n' | '\r')+      -> skip;
WS                  : ((' ' | '\t')+)           -> skip;     // who cares about whitespaces?
COMMENT             : '#' ~( '\r' | '\n' )*     -> skip;     // Single line comments, starting with a #