
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGIN CLOSE_PAREN COLON COMMA CYCLE END EQUAL FLOAT_DIGIT FLOAT_TYPE INTEGER_TYPE INT_DIGIT MINUS NEGATION OPEN_PAREN PRINT SEMI_COLON SUM VAR VARIABLEvar : VAR variable COLON INTEGER_TYPE SEMI_COLON body\n           | VAR variable COLON FLOAT_TYPE SEMI_COLON bodybody :\n            | body lines colons\n            | BEGIN lines colons ENDcolons : SEMI_COLON\n              | colons SEMI_COLONlines : assign\n             | while\n             | PRINT argsassign : VARIABLE EQUAL exprexpr : fact\n            | expr SUM fact\n            | expr MINUS factfact : termterm : arg\n            | OPEN_PAREN expr CLOSE_PARENwhile : CYCLE OPEN_PAREN args CLOSE_PAREN BEGIN lines ENDargs :\n            | expr\n            | args COMMA exprarg : variable\n           | FLOAT_DIGIT\n           | INT_DIGITvariable : VARIABLE\n           | VARIABLE COMMA variable\n           |'
    
_lr_action_items = {'VAR':([0,],[2,]),'$end':([1,10,11,12,14,22,23,36,43,],[0,-3,-3,-1,-2,-4,-6,-7,-5,]),'VARIABLE':([2,6,10,11,12,13,14,18,22,23,29,33,34,36,37,38,39,43,49,],[4,4,-3,-3,19,19,19,4,-4,-6,4,4,4,-7,4,4,4,-5,19,]),'COLON':([2,3,4,6,9,],[-27,5,-25,-27,-26,]),'SUM':([4,6,9,18,25,26,27,28,29,30,31,32,33,34,37,38,39,40,41,44,45,46,47,],[-25,-27,-26,-27,38,-12,-15,-16,-27,-22,-23,-24,-27,-27,-27,-27,-27,38,38,38,-13,-14,-17,]),'MINUS':([4,6,9,18,25,26,27,28,29,30,31,32,33,34,37,38,39,40,41,44,45,46,47,],[-25,-27,-26,-27,39,-12,-15,-16,-27,-22,-23,-24,-27,-27,-27,-27,-27,39,39,39,-13,-14,-17,]),'COMMA':([4,6,9,18,24,25,26,27,28,30,31,32,34,37,38,39,42,44,45,46,47,],[6,-27,-26,-19,37,-20,-12,-15,-16,-22,-23,-24,-19,-27,-27,-27,37,-21,-13,-14,-17,]),'SEMI_COLON':([4,6,7,8,9,15,16,17,18,21,22,23,24,25,26,27,28,30,31,32,33,35,36,37,38,39,41,44,45,46,47,51,],[-25,-27,10,11,-26,23,-8,-9,-19,23,36,-6,-10,-20,-12,-15,-16,-22,-23,-24,-27,36,-7,-27,-27,-27,-11,-21,-13,-14,-17,-18,]),'END':([4,6,9,16,17,18,23,24,25,26,27,28,30,31,32,33,35,36,37,38,39,41,44,45,46,47,50,51,],[-25,-27,-26,-8,-9,-19,-6,-10,-20,-12,-15,-16,-22,-23,-24,-27,43,-7,-27,-27,-27,-11,-21,-13,-14,-17,51,-18,]),'CLOSE_PAREN':([4,6,9,25,26,27,28,29,30,31,32,34,37,38,39,40,42,44,45,46,47,],[-25,-27,-26,-20,-12,-15,-16,-27,-22,-23,-24,-19,-27,-27,-27,47,48,-21,-13,-14,-17,]),'INTEGER_TYPE':([5,],[7,]),'FLOAT_TYPE':([5,],[8,]),'PRINT':([10,11,12,13,14,22,23,36,43,49,],[-3,-3,18,18,18,-4,-6,-7,-5,18,]),'CYCLE':([10,11,12,13,14,22,23,36,43,49,],[-3,-3,20,20,20,-4,-6,-7,-5,20,]),'BEGIN':([10,11,48,],[13,13,49,]),'OPEN_PAREN':([18,20,29,33,34,37,38,39,],[29,34,29,29,29,29,29,29,]),'FLOAT_DIGIT':([18,29,33,34,37,38,39,],[31,31,31,31,31,31,31,]),'INT_DIGIT':([18,29,33,34,37,38,39,],[32,32,32,32,32,32,32,]),'EQUAL':([19,],[33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'var':([0,],[1,]),'variable':([2,6,18,29,33,34,37,38,39,],[3,9,30,30,30,30,30,30,30,]),'body':([10,11,],[12,14,]),'lines':([12,13,14,49,],[15,21,15,50,]),'assign':([12,13,14,49,],[16,16,16,16,]),'while':([12,13,14,49,],[17,17,17,17,]),'colons':([15,21,],[22,35,]),'args':([18,34,],[24,42,]),'expr':([18,29,33,34,37,],[25,40,41,25,44,]),'fact':([18,29,33,34,37,38,39,],[26,26,26,26,26,45,46,]),'term':([18,29,33,34,37,38,39,],[27,27,27,27,27,27,27,]),'arg':([18,29,33,34,37,38,39,],[28,28,28,28,28,28,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> var","S'",1,None,None,None),
  ('var -> VAR variable COLON INTEGER_TYPE SEMI_COLON body','var',6,'p_var','parser.py',21),
  ('var -> VAR variable COLON FLOAT_TYPE SEMI_COLON body','var',6,'p_var','parser.py',22),
  ('body -> <empty>','body',0,'p_body','parser.py',26),
  ('body -> body lines colons','body',3,'p_body','parser.py',27),
  ('body -> BEGIN lines colons END','body',4,'p_body','parser.py',28),
  ('colons -> SEMI_COLON','colons',1,'p_colons','parser.py',37),
  ('colons -> colons SEMI_COLON','colons',2,'p_colons','parser.py',38),
  ('lines -> assign','lines',1,'p_lines','parser.py',41),
  ('lines -> while','lines',1,'p_lines','parser.py',42),
  ('lines -> PRINT args','lines',2,'p_lines','parser.py',43),
  ('assign -> VARIABLE EQUAL expr','assign',3,'p_assign','parser.py',51),
  ('expr -> fact','expr',1,'p_expr','parser.py',55),
  ('expr -> expr SUM fact','expr',3,'p_expr','parser.py',56),
  ('expr -> expr MINUS fact','expr',3,'p_expr','parser.py',57),
  ('fact -> term','fact',1,'p_fact','parser.py',64),
  ('term -> arg','term',1,'p_term','parser.py',71),
  ('term -> OPEN_PAREN expr CLOSE_PAREN','term',3,'p_term','parser.py',72),
  ('while -> CYCLE OPEN_PAREN args CLOSE_PAREN BEGIN lines END','while',7,'p_while','parser.py',79),
  ('args -> <empty>','args',0,'p_args','parser.py',83),
  ('args -> expr','args',1,'p_args','parser.py',84),
  ('args -> args COMMA expr','args',3,'p_args','parser.py',85),
  ('arg -> variable','arg',1,'p_arg','parser.py',95),
  ('arg -> FLOAT_DIGIT','arg',1,'p_arg','parser.py',96),
  ('arg -> INT_DIGIT','arg',1,'p_arg','parser.py',97),
  ('variable -> VARIABLE','variable',1,'p_variable','parser.py',101),
  ('variable -> VARIABLE COMMA variable','variable',3,'p_variable','parser.py',102),
  ('variable -> <empty>','variable',0,'p_variable','parser.py',103),
]
