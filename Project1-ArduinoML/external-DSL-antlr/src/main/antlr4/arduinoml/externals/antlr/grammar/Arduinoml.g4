grammar Arduinoml;


/******************
 ** Parser rules **
 ******************/

root            :   declaration bricks states EOF;

declaration     :   'application' name=IDENTIFIER;

bricks          :   (sensor|actuator)+;
    sensor      :   'sensor'   location ;
    actuator    :   'actuator' location ;
    location    :   id=IDENTIFIER ':' port=PORT_NUMBER;

states          :   state+;
    state       :   initial? name=IDENTIFIER '{'  beep* action+ transition '}';
    action      :   receiver=IDENTIFIER '<=' value=SIGNAL;
    beep        :   BEEP_TYPE value=NB_BEEPS;
    transition  :   trigger=IDENTIFIER 'is' value=SIGNAL condition* '=>' next=IDENTIFIER ;
    condition   :   booleanOperator=BOOL trigger=IDENTIFIER 'is' value=SIGNAL ;
    initial     :   '->';

/*****************
 ** Lexer rules **
 *****************/

PORT_NUMBER     :   [1-9] | '11' | '12';
IDENTIFIER      :   LOWERCASE (LOWERCASE|UPPERCASE|NUMBER)+;
SIGNAL          :   'HIGH' | 'LOW';
BOOL            :   '&'    | '|';
BEEP_TYPE       :   'longbeep' | 'shortbeep';
NB_BEEPS        :   [1-9]?;

/*************
 ** Helpers **
 *************/

fragment LOWERCASE  : [a-z];                                 // abstract rule, does not really exists
fragment UPPERCASE  : [A-Z];
fragment NUMBER     : [0-9];
NEWLINE             : ('\r'? '\n' | '\r')+      -> skip;
WS                  : ((' ' | '\t')+)           -> skip;     // who cares about whitespaces?
COMMENT             : '#' ~( '\r' | '\n' )*     -> skip;     // Single line comments, starting with a #
