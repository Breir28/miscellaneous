CLASS lcl_fahrzeug DEFINITION ABSTRACT. " Abstrakte Klasse
  PUBLIC SECTION.
    METHODS:
      starten ABSTRACT,                " Abstrakte Methode
      fahren.
ENDCLASS.

CLASS lcl_fahrzeug IMPLEMENTATION.
  METHOD fahren.
    WRITE: / 'Auto fährt los...'.
  ENDMETHOD.
ENDCLASS.

CLASS lcl_auto DEFINITION INHERITING FROM lcl_fahrzeug.
  PUBLIC SECTION.
    METHODS: starten REDEFINITION.
ENDCLASS.

CLASS lcl_auto IMPLEMENTATION.
  METHOD starten.
    WRITE: / 'Auto startet'.
  ENDMETHOD.
ENDCLASS.

START-OF-SELECTION.
  DATA(lo_fahrzeug) = NEW lcl_auto( ).
  lo_fahrzeug->starten( ).
  lo_fahrzeug->fahren( ).
