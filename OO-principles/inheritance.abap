CLASS lcl_tier DEFINITION.
  PUBLIC SECTION.
    METHODS: sprich RETURNING VALUE(rv_laut) TYPE string.
ENDCLASS.

CLASS lcl_tier IMPLEMENTATION.
  METHOD sprich.
    rv_laut = 'Laut'.
  ENDMETHOD.
ENDCLASS.

CLASS lcl_hund DEFINITION INHERITING FROM lcl_tier.
  PUBLIC SECTION.
    METHODS: sprich REDEFINITION.
ENDCLASS.

CLASS lcl_hund IMPLEMENTATION.
  METHOD sprich.
    rv_laut = 'Wuff'.
  ENDMETHOD.
ENDCLASS.

CLASS lcl_katze DEFINITION INHERITING FROM lcl_tier.
  PUBLIC SECTION.
    METHODS: sprich REDEFINITION.
ENDCLASS.

CLASS lcl_katze IMPLEMENTATION.
  METHOD sprich.
    rv_laut = 'Miau'.
  ENDMETHOD.
ENDCLASS.

START-OF-SELECTION.
  DATA(lo_tier)  = NEW lcl_tier( ).
  DATA(lo_hund)  = NEW lcl_hund( ).
  DATA(lo_katze) = NEW lcl_katze( ).

  WRITE: / 'Tier:',  lo_tier->sprich( ).
  WRITE: / 'Hund:',  lo_hund->sprich( ).
  WRITE: / 'Katze:', lo_katze->sprich( ).
