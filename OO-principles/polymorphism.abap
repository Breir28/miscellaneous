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

CLASS lcl_ausgabe DEFINITION.
  PUBLIC SECTION.
    CLASS-METHODS: tier_spricht IMPORTING io_tier TYPE REF TO lcl_tier.
ENDCLASS.

CLASS lcl_ausgabe IMPLEMENTATION.
  METHOD tier_spricht.
    WRITE: / io_tier->sprich( ).
  ENDMETHOD.
ENDCLASS.

START-OF-SELECTION.
  lcl_ausgabe=>tier_spricht( NEW lcl_tier( ) ).
  lcl_ausgabe=>tier_spricht( NEW lcl_hund( ) ).
  lcl_ausgabe=>tier_spricht( NEW lcl_katze( ) ).
