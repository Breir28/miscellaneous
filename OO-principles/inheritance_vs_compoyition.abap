" --- Vererbung: Fisch ist ein Tier ---

CLASS lcl_tier DEFINITION.
  PUBLIC SECTION.
    METHODS: bewegung RETURNING VALUE(rv_text) TYPE string.
ENDCLASS.

CLASS lcl_tier IMPLEMENTATION.
  METHOD bewegung.
    rv_text = 'bewegt sich'.
  ENDMETHOD.
ENDCLASS.

CLASS lcl_fisch_inherit DEFINITION INHERITING FROM lcl_tier.
  PUBLIC SECTION.
    METHODS: schwimmen RETURNING VALUE(rv_text) TYPE string.
ENDCLASS.

CLASS lcl_fisch_inherit IMPLEMENTATION.
  METHOD schwimmen.
    rv_text = 'schwimmt'.
  ENDMETHOD.
ENDCLASS.

" --- Komposition: Fisch hat eine Flosse ---

CLASS lcl_flosse DEFINITION.
  PUBLIC SECTION.
    METHODS: schlagen RETURNING VALUE(rv_text) TYPE string.
ENDCLASS.

CLASS lcl_flosse IMPLEMENTATION.
  METHOD schlagen.
    rv_text = 'Flosse schlägt'.
  ENDMETHOD.
ENDCLASS.

CLASS lcl_fisch_komposit DEFINITION.
  PUBLIC SECTION.
    METHODS:
      constructor,
      schwimmen RETURNING VALUE(rv_text) TYPE string.
  PRIVATE SECTION.
    DATA: mo_flosse TYPE REF TO lcl_flosse.
ENDCLASS.

CLASS lcl_fisch_komposit IMPLEMENTATION.
  METHOD constructor.
    mo_flosse = NEW lcl_flosse( ).
  ENDMETHOD.

  METHOD schwimmen.
    rv_text = mo_flosse->schlagen( ) && ' → schwimmt'.
  ENDMETHOD.
ENDCLASS.

" --- Ausführung ---

START-OF-SELECTION.

  " Vererbung
  DATA(lo_fisch1) = NEW lcl_fisch_inherit( ).
  WRITE: / lo_fisch1->bewegung( ).   " bewegt sich
  WRITE: / lo_fisch1->schwimmen( ).  " schwimmt

  " Komposition
  DATA(lo_fisch2) = NEW lcl_fisch_komposit( ).
  WRITE: / lo_fisch2->schwimmen( ).  " Flosse schlägt → schwimmt
