CLASS lcl_konto DEFINITION.
  PRIVATE SECTION.
    DATA: mv_saldo TYPE i.

  PUBLIC SECTION.
    METHODS: constructor,
             einzahlen     IMPORTING iv_betrag TYPE i RETURNING VALUE(rv_success) TYPE abap_bool,
             auszahlen     IMPORTING iv_betrag TYPE i RETURNING VALUE(rv_success) TYPE abap_bool,
             saldo_anzeigen RETURNING VALUE(rv_saldo) TYPE i.
ENDCLASS.

CLASS lcl_konto IMPLEMENTATION.

  METHOD constructor.
    mv_saldo = 0.
  ENDMETHOD.

  METHOD einzahlen.
    IF iv_betrag > 0.
      mv_saldo = mv_saldo + iv_betrag.
      rv_success = abap_true.
    ELSE.
      rv_success = abap_false.
    ENDIF.
  ENDMETHOD.

  METHOD auszahlen.
    IF iv_betrag <= mv_saldo.
      mv_saldo = mv_saldo - iv_betrag.
      rv_success = abap_true.
    ELSE.
      rv_success = abap_false.
    ENDIF.
  ENDMETHOD.

  METHOD saldo_anzeigen.
    rv_saldo = mv_saldo.
  ENDMETHOD.

ENDCLASS.

START-OF-SELECTION.
  DATA(lo_konto) = NEW lcl_konto( ).
  DATA(lv_ok) TYPE abap_bool.
  DATA(lv_saldo) TYPE i.

  lv_ok = lo_konto->einzahlen( 100 ).
  lv_ok = lo_konto->auszahlen( 25 ).
  lv_saldo = lo_konto->saldo_anzeigen( ).

  WRITE: / 'Saldo:', lv_saldo.
