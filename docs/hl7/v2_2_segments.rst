v2.2 Segments
=============

.. _hl7-v2_2-ACC:

ACC: ACCIDENT
~~~~~~~~~~~~~

Section 6.4.8

.. py:class:: hl7types.hl7.v2_2.segments.ACC.ACC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``acc_1``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00527
     - Accident date / time
   * - 2
     - ``acc_2``
     - 2
     - str
     - O
     - 0050
     - 00528
     - Accident code
   * - 3
     - ``acc_3``
     - 25
     - str
     - O
     -
     - 00529
     - Accident location

.. _hl7-v2_2-ADD:

ADD: ADDENDUM
~~~~~~~~~~~~~

Section 2.10.10

.. py:class:: hl7types.hl7.v2_2.segments.ADD.ADD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``add_1``
     - 65536
     - str
     - O
     -
     - 00066
     - Addendum Continuation Pointer

.. _hl7-v2_2-AL1:

AL1: PATIENT ALLERGY INFORMATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.6

.. py:class:: hl7types.hl7.v2_2.segments.AL1.AL1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``al1_1``
     - 4
     - str
     - R
     -
     - 00203
     - Set ID - Allergy
   * - 2
     - ``al1_2``
     - 2
     - str
     - O
     - 0127
     - 00204
     - Allergy Type
   * - 3
     - ``al1_3``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00205
     - Allergy code / mnemonic / description
   * - 4
     - ``al1_4``
     - 2
     - str
     - O
     - 0128
     - 00206
     - Allergy Severity
   * - 5
     - ``al1_5``
     - 15
     - str
     - O
     -
     - 00207
     - Allergy Reaction
   * - 6
     - ``al1_6``
     - 8
     - str
     - O
     -
     - 00208
     - Identification Date

.. _hl7-v2_2-BHS:

BHS: BATCH HEADER
~~~~~~~~~~~~~~~~~

Section 2.10.13

.. py:class:: hl7types.hl7.v2_2.segments.BHS.BHS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``bhs_1``
     - 1
     - str
     - R
     -
     - 00081
     - Batch Field Separator
   * - 2
     - ``bhs_2``
     - 4
     - str
     - R
     -
     - 00082
     - Batch Encoding Characters
   * - 3
     - ``bhs_3``
     - 15
     - str
     - O
     -
     - 00083
     - Batch Sending Application
   * - 4
     - ``bhs_4``
     - 20
     - str
     - O
     -
     - 00084
     - Batch Sending Facility
   * - 5
     - ``bhs_5``
     - 30
     - str
     - O
     -
     - 00085
     - Batch Receiving Application
   * - 6
     - ``bhs_6``
     - 30
     - str
     - O
     -
     - 00086
     - Batch Receiving Facility
   * - 7
     - ``bhs_7``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00087
     - Batch creation date / time
   * - 8
     - ``bhs_8``
     - 40
     - str
     - O
     -
     - 00088
     - Batch Security
   * - 9
     - ``bhs_9``
     - 20
     - str
     - O
     -
     - 00089
     - Batch name / ID / type
   * - 10
     - ``bhs_10``
     - 80
     - str
     - O
     -
     - 00090
     - Batch Comment
   * - 11
     - ``bhs_11``
     - 20
     - str
     - O
     -
     - 00091
     - Batch Control ID
   * - 12
     - ``bhs_12``
     - 20
     - str
     - O
     -
     - 00092
     - Reference Batch Control ID

.. _hl7-v2_2-BLG:

BLG: BILLING
~~~~~~~~~~~~

Section 4.3.2

.. py:class:: hl7types.hl7.v2_2.segments.BLG.BLG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``blg_1``
     -
     - str
     - O
     - 0100
     - 00234
     - When to Charge
   * - 2
     - ``blg_2``
     - 50
     - str
     - O
     - 0122
     - 00235
     - Charge Type
   * - 3
     - ``blg_3``
     - 100
     - str
     - O
     -
     - 00236
     - Account ID

.. _hl7-v2_2-BTS:

BTS: BATCH TRAILER
~~~~~~~~~~~~~~~~~~

Section 2.10.14

.. py:class:: hl7types.hl7.v2_2.segments.BTS.BTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``bts_1``
     - 10
     - str
     - O
     -
     - 00093
     - Batch Message Count
   * - 2
     - ``bts_2``
     - 80
     - str
     - O
     -
     - 00094
     - Batch Comment
   * - 3
     - ``bts_3``
     -
     - list[str]
     - O
     -
     - 00095
     - Batch Totals

.. _hl7-v2_2-DG1:

DG1: DIAGNOSIS
~~~~~~~~~~~~~~

Section 6.4.2

.. py:class:: hl7types.hl7.v2_2.segments.DG1.DG1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``dg1_1``
     - 4
     - str
     - R
     -
     - 00375
     - Set ID - diagnosis
   * - 2
     - ``dg1_2``
     - 2
     - str
     - R
     - 0053
     - 00376
     - Diagnosis coding method
   * - 3
     - ``dg1_3``
     - 8
     - str
     - O
     - 0051
     - 00377
     - Diagnosis code
   * - 4
     - ``dg1_4``
     - 40
     - str
     - O
     -
     - 00378
     - Diagnosis description
   * - 5
     - ``dg1_5``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00379
     - Diagnosis date / time
   * - 6
     - ``dg1_6``
     - 2
     - str
     - R
     - 0052
     - 00380
     - Diagnosis / DRG type
   * - 7
     - ``dg1_7``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     - 0118
     - 00381
     - Major diagnostic category
   * - 8
     - ``dg1_8``
     - 4
     - str
     - O
     - 0055
     - 00382
     - Diagnostic related group
   * - 9
     - ``dg1_9``
     - 2
     - str
     - O
     -
     - 00383
     - DRG approval indicator
   * - 10
     - ``dg1_10``
     - 2
     - str
     - O
     - 0056
     - 00384
     - DRG grouper review code
   * - 11
     - ``dg1_11``
     - 60
     - str
     - O
     - 0083
     - 00385
     - Outlier type
   * - 12
     - ``dg1_12``
     - 3
     - str
     - O
     -
     - 00386
     - Outlier days
   * - 13
     - ``dg1_13``
     - 12
     - str
     - O
     -
     - 00387
     - Outlier cost
   * - 14
     - ``dg1_14``
     - 4
     - str
     - O
     -
     - 00388
     - Grouper version and type
   * - 15
     - ``dg1_15``
     - 2
     - str
     - O
     -
     - 00389
     - Diagnosis / DRG priority
   * - 16
     - ``dg1_16``
     -
     - str
     - O
     -
     - 00390
     - Diagnosing clinician

.. _hl7-v2_2-DSC:

DSC: CONTINUATION POINTER
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.10.8

.. py:class:: hl7types.hl7.v2_2.segments.DSC.DSC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``dsc_1``
     - 180
     - str
     - O
     -
     - 00060
     - Continuation Pointer

.. _hl7-v2_2-DSP:

DSP: DISPLAY DATA
~~~~~~~~~~~~~~~~~

Section 2.10.9

.. py:class:: hl7types.hl7.v2_2.segments.DSP.DSP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``dsp_1``
     - 4
     - str
     - O
     -
     - 00061
     - Set ID - Display Data
   * - 2
     - ``dsp_2``
     - 4
     - str
     - O
     -
     - 00062
     - Display Level
   * - 3
     - ``dsp_3``
     -
     - str
     - R
     -
     - 00063
     - Data Line
   * - 4
     - ``dsp_4``
     - 2
     - str
     - O
     -
     - 00064
     - Logical Break Point
   * - 5
     - ``dsp_5``
     -
     - str
     - O
     -
     - 00065
     - Result ID

.. _hl7-v2_2-ERR:

ERR: ERROR
~~~~~~~~~~

Section 2.10.3

.. py:class:: hl7types.hl7.v2_2.segments.ERR.ERR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``err_1``
     -
     - list[str]
     - R
     - 0060
     - 00024
     - Error Code and Location

.. _hl7-v2_2-EVN:

EVN: EVENT TYPE
~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_2.segments.EVN.EVN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``evn_1``
     - 3
     - str
     - R
     - 0003
     - 00099
     - Event Type Code
   * - 2
     - ``evn_2``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - R
     -
     - 00100
     - Date / time of event
   * - 3
     - ``evn_3``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00101
     - Date / time planned event
   * - 4
     - ``evn_4``
     - 3
     - str
     - O
     - 0062
     - 00102
     - Event Reason Code
   * - 5
     - ``evn_5``
     - 5
     - str
     - O
     - 0188
     - 00103
     - Operator ID

.. _hl7-v2_2-FHS:

FHS: FILE HEADER
~~~~~~~~~~~~~~~~

Section 2.10.11

.. py:class:: hl7types.hl7.v2_2.segments.FHS.FHS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``fhs_1``
     - 1
     - str
     - R
     -
     - 00067
     - File Field Separator
   * - 2
     - ``fhs_2``
     - 4
     - str
     - R
     -
     - 00068
     - File Encoding Characters
   * - 3
     - ``fhs_3``
     - 15
     - str
     - O
     -
     - 00069
     - File Sending Application
   * - 4
     - ``fhs_4``
     - 20
     - str
     - O
     -
     - 00070
     - File Sending Facility
   * - 5
     - ``fhs_5``
     - 30
     - str
     - O
     -
     - 00071
     - File Receiving Application
   * - 6
     - ``fhs_6``
     - 30
     - str
     - O
     -
     - 00072
     - File Receiving Facility
   * - 7
     - ``fhs_7``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00073
     - File creation date / time
   * - 8
     - ``fhs_8``
     - 40
     - str
     - O
     -
     - 00074
     - File Security
   * - 9
     - ``fhs_9``
     - 20
     - str
     - O
     -
     - 00075
     - File name / ID
   * - 10
     - ``fhs_10``
     - 80
     - str
     - O
     -
     - 00076
     - File Header Comment
   * - 11
     - ``fhs_11``
     - 20
     - str
     - O
     -
     - 00077
     - File Control ID
   * - 12
     - ``fhs_12``
     - 20
     - str
     - O
     -
     - 00078
     - Reference File Control ID

.. _hl7-v2_2-FT1:

FT1: FINANCIAL TRANSACTION
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.1

.. py:class:: hl7types.hl7.v2_2.segments.FT1.FT1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``ft1_1``
     - 4
     - str
     - O
     -
     - 00355
     - Set ID - financial transaction
   * - 2
     - ``ft1_2``
     - 12
     - str
     - O
     -
     - 00356
     - Transaction ID
   * - 3
     - ``ft1_3``
     - 10
     - str
     - O
     -
     - 00357
     - Transaction batch ID
   * - 4
     - ``ft1_4``
     - 8
     - str
     - R
     -
     - 00358
     - Transaction date
   * - 5
     - ``ft1_5``
     - 8
     - str
     - O
     -
     - 00359
     - Transaction posting date
   * - 6
     - ``ft1_6``
     - 8
     - str
     - R
     - 0017
     - 00360
     - Transaction type
   * - 7
     - ``ft1_7``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     - 0132
     - 00361
     - Transaction code
   * - 8
     - ``ft1_8``
     - 40
     - str
     - O
     -
     - 00362
     - Transaction description
   * - 9
     - ``ft1_9``
     - 40
     - str
     - O
     -
     - 00363
     - Transaction description - alternate
   * - 10
     - ``ft1_10``
     - 4
     - str
     - O
     -
     - 00364
     - Transaction quantity
   * - 11
     - ``ft1_11``
     - 12
     - str
     - O
     -
     - 00365
     - Transaction amount - extended
   * - 12
     - ``ft1_12``
     - 12
     - str
     - O
     -
     - 00366
     - Transaction amount - unit
   * - 13
     - ``ft1_13``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     - 0049
     - 00367
     - Department code
   * - 14
     - ``ft1_14``
     - 8
     - str
     - R
     - 0072
     - 00368
     - Insurance plan ID
   * - 15
     - ``ft1_15``
     - 12
     - str
     - O
     -
     - 00369
     - Insurance amount
   * - 16
     - ``ft1_16``
     -
     - str
     - O
     - 0079
     - 00133
     - Assigned Patient Location
   * - 17
     - ``ft1_17``
     - 1
     - str
     - O
     - 0024
     - 00370
     - Fee schedule
   * - 18
     - ``ft1_18``
     - 2
     - str
     - O
     - 0018
     - 00148
     - Patient type
   * - 19
     - ``ft1_19``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     - 0051
     - 00371
     - Diagnosis code
   * - 20
     - ``ft1_20``
     -
     - str
     - O
     - 0084
     - 00372
     - Performed by code
   * - 21
     - ``ft1_21``
     -
     - str
     - O
     -
     - 00373
     - Ordered by code
   * - 22
     - ``ft1_22``
     - 12
     - str
     - O
     -
     - 00374
     - Unit cost
   * - 23
     - ``ft1_23``
     -
     - str
     - C
     -
     - 00217
     - Filler Order Number

.. _hl7-v2_2-FTS:

FTS: FILE TRAILER
~~~~~~~~~~~~~~~~~

Section 2.10.12

.. py:class:: hl7types.hl7.v2_2.segments.FTS.FTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``fts_1``
     - 10
     - str
     - O
     -
     - 00079
     - File Batch Count
   * - 2
     - ``fts_2``
     - 80
     - str
     - O
     -
     - 00080
     - File Trailer Comment

.. _hl7-v2_2-GT1:

GT1: GUARANTOR
~~~~~~~~~~~~~~

Section 6.4.4

.. py:class:: hl7types.hl7.v2_2.segments.GT1.GT1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``gt1_1``
     - 4
     - str
     - R
     -
     - 00405
     - Set ID - guarantor
   * - 2
     - ``gt1_2``
     - 20
     - str
     - O
     -
     - 00406
     - Guarantor number
   * - 3
     - ``gt1_3``
     -
     - :ref:`PN <hl7-v2_2-PN>`
     - R
     -
     - 00407
     - Guarantor name
   * - 4
     - ``gt1_4``
     -
     - :ref:`PN <hl7-v2_2-PN>`
     - O
     -
     - 00408
     - Guarantor spouse name
   * - 5
     - ``gt1_5``
     -
     - :ref:`AD <hl7-v2_2-AD>`
     - O
     -
     - 00409
     - Guarantor address
   * - 6
     - ``gt1_6``
     - 40
     - list[str]
     - O
     -
     - 00410
     - Guarantor phone number - home
   * - 7
     - ``gt1_7``
     - 40
     - list[str]
     - O
     -
     - 00411
     - Guarantor phone number - business
   * - 8
     - ``gt1_8``
     - 8
     - str
     - O
     -
     - 00412
     - Guarantor date of birth
   * - 9
     - ``gt1_9``
     - 1
     - str
     - O
     - 0001
     - 00413
     - Guarantor sex
   * - 10
     - ``gt1_10``
     - 2
     - str
     - O
     - 0068
     - 00414
     - Guarantor type
   * - 11
     - ``gt1_11``
     - 2
     - str
     - O
     - 0063
     - 00415
     - Guarantor relationship
   * - 12
     - ``gt1_12``
     - 11
     - str
     - O
     -
     - 00416
     - Guarantor social security number
   * - 13
     - ``gt1_13``
     - 8
     - str
     - O
     -
     - 00417
     - Guarantor date - begin
   * - 14
     - ``gt1_14``
     - 8
     - str
     - O
     -
     - 00418
     - Guarantor date - end
   * - 15
     - ``gt1_15``
     - 2
     - str
     - O
     -
     - 00419
     - Guarantor priority
   * - 16
     - ``gt1_16``
     - 45
     - str
     - O
     -
     - 00420
     - Guarantor employer name
   * - 17
     - ``gt1_17``
     -
     - :ref:`AD <hl7-v2_2-AD>`
     - O
     -
     - 00421
     - Guarantor employer address
   * - 18
     - ``gt1_18``
     - 40
     - list[str]
     - O
     -
     - 00422
     - Guarantor employ phone number
   * - 19
     - ``gt1_19``
     - 20
     - str
     - O
     -
     - 00423
     - Guarantor employee ID number
   * - 20
     - ``gt1_20``
     - 2
     - str
     - O
     - 0066
     - 00424
     - Guarantor employment status
   * - 21
     - ``gt1_21``
     - 60
     - str
     - O
     -
     - 00425
     - Guarantor organization

.. _hl7-v2_2-IN1:

IN1: INSURANCE
~~~~~~~~~~~~~~

Section 6.4.5

.. py:class:: hl7types.hl7.v2_2.segments.IN1.IN1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``in1_1``
     - 4
     - str
     - R
     -
     - 00426
     - Set ID - insurance
   * - 2
     - ``in1_2``
     - 8
     - str
     - R
     - 0072
     - 00368
     - Insurance plan ID
   * - 3
     - ``in1_3``
     - 9
     - str
     - R
     -
     - 00428
     - Insurance company ID
   * - 4
     - ``in1_4``
     - 45
     - str
     - O
     -
     - 00429
     - Insurance company name
   * - 5
     - ``in1_5``
     -
     - :ref:`AD <hl7-v2_2-AD>`
     - O
     -
     - 00430
     - Insurance company address
   * - 6
     - ``in1_6``
     -
     - :ref:`PN <hl7-v2_2-PN>`
     - O
     -
     - 00431
     - Insurance company contact pers
   * - 7
     - ``in1_7``
     - 40
     - list[str]
     - O
     -
     - 00432
     - Insurance company phone number
   * - 8
     - ``in1_8``
     - 12
     - str
     - O
     -
     - 00433
     - Group number
   * - 9
     - ``in1_9``
     - 35
     - str
     - O
     -
     - 00434
     - Group name
   * - 10
     - ``in1_10``
     - 12
     - str
     - O
     -
     - 00435
     - Insured's group employer ID
   * - 11
     - ``in1_11``
     - 45
     - str
     - O
     -
     - 00436
     - Insured's group employer name
   * - 12
     - ``in1_12``
     - 8
     - str
     - O
     -
     - 00437
     - Plan effective date
   * - 13
     - ``in1_13``
     - 8
     - str
     - O
     -
     - 00438
     - Plan expiration date
   * - 14
     - ``in1_14``
     -
     - str
     - O
     -
     - 00439
     - Authorization information
   * - 15
     - ``in1_15``
     - 5
     - str
     - O
     - 0086
     - 00440
     - Plan type
   * - 16
     - ``in1_16``
     -
     - :ref:`PN <hl7-v2_2-PN>`
     - O
     -
     - 00441
     - Name of insured
   * - 17
     - ``in1_17``
     - 2
     - str
     - O
     - 0063
     - 00442
     - Insured's relationship to patient
   * - 18
     - ``in1_18``
     - 8
     - str
     - O
     -
     - 00443
     - Insured's date of birth
   * - 19
     - ``in1_19``
     -
     - :ref:`AD <hl7-v2_2-AD>`
     - O
     -
     - 00444
     - Insured's address
   * - 20
     - ``in1_20``
     - 2
     - str
     - O
     - 0135
     - 00445
     - Assignment of benefits
   * - 21
     - ``in1_21``
     - 2
     - str
     - O
     - 0173
     - 00446
     - Coordination of benefits
   * - 22
     - ``in1_22``
     - 2
     - str
     - O
     -
     - 00447
     - Coordination of benefits - priority
   * - 23
     - ``in1_23``
     - 2
     - str
     - O
     - 0136
     - 00448
     - Notice of admission code
   * - 24
     - ``in1_24``
     - 8
     - str
     - O
     -
     - 00449
     - Notice of admission date
   * - 25
     - ``in1_25``
     - 4
     - str
     - O
     -
     - 00450
     - Report of eligibility code
   * - 26
     - ``in1_26``
     - 8
     - str
     - O
     -
     - 00451
     - Report of eligibility date
   * - 27
     - ``in1_27``
     - 2
     - str
     - O
     - 0093
     - 00452
     - Release information code
   * - 28
     - ``in1_28``
     - 15
     - str
     - O
     -
     - 00453
     - Pre-admit certification (PAC)
   * - 29
     - ``in1_29``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00454
     - Verification date / time
   * - 30
     - ``in1_30``
     -
     - str
     - O
     -
     - 00455
     - Verification by
   * - 31
     - ``in1_31``
     - 2
     - str
     - O
     - 0098
     - 00456
     - Type of agreement code
   * - 32
     - ``in1_32``
     - 2
     - str
     - O
     - 0022
     - 00457
     - Billing status
   * - 33
     - ``in1_33``
     - 4
     - str
     - O
     -
     - 00458
     - Lifetime reserve days
   * - 34
     - ``in1_34``
     - 4
     - str
     - O
     -
     - 00459
     - Delay before lifetime reserve days
   * - 35
     - ``in1_35``
     - 8
     - str
     - O
     - 0042
     - 00460
     - Company plan code
   * - 36
     - ``in1_36``
     - 15
     - str
     - O
     -
     - 00461
     - Policy number
   * - 37
     - ``in1_37``
     - 12
     - str
     - O
     -
     - 00462
     - Policy deductible
   * - 38
     - ``in1_38``
     - 12
     - str
     - O
     -
     - 00463
     - Policy limit - amount
   * - 39
     - ``in1_39``
     - 4
     - str
     - O
     -
     - 00464
     - Policy limit - days
   * - 40
     - ``in1_40``
     - 12
     - str
     - O
     -
     - 00465
     - Room rate - semi-private
   * - 41
     - ``in1_41``
     - 12
     - str
     - O
     -
     - 00466
     - Room rate - private
   * - 42
     - ``in1_42``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     - 0066
     - 00467
     - Insured's employment status
   * - 43
     - ``in1_43``
     - 1
     - str
     - O
     - 0001
     - 00468
     - Insured's sex
   * - 44
     - ``in1_44``
     -
     - :ref:`AD <hl7-v2_2-AD>`
     - O
     -
     - 00469
     - Insured's employer address
   * - 45
     - ``in1_45``
     - 2
     - str
     - O
     -
     - 00470
     - Verification status
   * - 46
     - ``in1_46``
     - 8
     - str
     - O
     - 0072
     - 00471
     - Prior insurance plan ID

.. _hl7-v2_2-IN2:

IN2: INSURANCE ADDITIONAL INFO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.6

.. py:class:: hl7types.hl7.v2_2.segments.IN2.IN2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``in2_1``
     - 15
     - str
     - O
     -
     - 00472
     - Insured's employee ID
   * - 2
     - ``in2_2``
     - 9
     - str
     - O
     -
     - 00473
     - Insured's social security number
   * - 3
     - ``in2_3``
     -
     - str
     - O
     -
     - 00474
     - Insured's employer name
   * - 4
     - ``in2_4``
     - 1
     - str
     - O
     - 0139
     - 00475
     - Employer information data
   * - 5
     - ``in2_5``
     - 1
     - str
     - O
     - 0137
     - 00476
     - Mail claim party
   * - 6
     - ``in2_6``
     - 15
     - str
     - O
     -
     - 00477
     - Medicare health insurance card number
   * - 7
     - ``in2_7``
     -
     - :ref:`PN <hl7-v2_2-PN>`
     - O
     -
     - 00478
     - Medicaid case name
   * - 8
     - ``in2_8``
     - 15
     - str
     - O
     -
     - 00479
     - Medicaid case number
   * - 9
     - ``in2_9``
     -
     - :ref:`PN <hl7-v2_2-PN>`
     - O
     -
     - 00480
     - Champus sponsor name
   * - 10
     - ``in2_10``
     - 20
     - str
     - O
     -
     - 00481
     - Champus ID number
   * - 11
     - ``in2_11``
     - 1
     - str
     - O
     -
     - 00482
     - Dependent of champus recipient
   * - 12
     - ``in2_12``
     - 25
     - str
     - O
     -
     - 00483
     - Champus organization
   * - 13
     - ``in2_13``
     - 25
     - str
     - O
     -
     - 00484
     - Champus station
   * - 14
     - ``in2_14``
     - 14
     - str
     - O
     - 0140
     - 00485
     - Champus service
   * - 15
     - ``in2_15``
     - 2
     - str
     - O
     - 0141
     - 00486
     - Champus rank / grade
   * - 16
     - ``in2_16``
     - 3
     - str
     - O
     - 0142
     - 00487
     - Champus status
   * - 17
     - ``in2_17``
     - 8
     - str
     - O
     -
     - 00488
     - Champus retire date
   * - 18
     - ``in2_18``
     - 1
     - str
     - O
     - 0136
     - 00489
     - Champus non-availability certification on file
   * - 19
     - ``in2_19``
     - 1
     - str
     - O
     - 0136
     - 00490
     - Baby coverage
   * - 20
     - ``in2_20``
     - 1
     - str
     - O
     - 0136
     - 00491
     - Combine baby bill
   * - 21
     - ``in2_21``
     - 1
     - str
     - O
     -
     - 00531
     - Blood deductible
   * - 22
     - ``in2_22``
     -
     - :ref:`PN <hl7-v2_2-PN>`
     - O
     -
     - 00493
     - Special coverage approval name
   * - 23
     - ``in2_23``
     - 30
     - str
     - O
     -
     - 00494
     - Special coverage approval title
   * - 24
     - ``in2_24``
     - 8
     - list[str]
     - O
     - 0143
     - 00495
     - Non-covered insurance code
   * - 25
     - ``in2_25``
     - 6
     - str
     - O
     -
     - 00496
     - Payor ID
   * - 26
     - ``in2_26``
     - 6
     - str
     - O
     -
     - 00497
     - Payor subscriber ID
   * - 27
     - ``in2_27``
     - 1
     - str
     - O
     - 0144
     - 00498
     - Eligibility source
   * - 28
     - ``in2_28``
     -
     - list[str]
     - O
     - 0145
     - 00499
     - Room coverage type / amount
   * - 29
     - ``in2_29``
     -
     - list[str]
     - O
     - 0147
     - 00500
     - Policy type / amount
   * - 30
     - ``in2_30``
     -
     - str
     - O
     -
     - 00501
     - Daily deductible

.. _hl7-v2_2-IN3:

IN3: INSURANCE ADDITIONAL INFO-CERTIFICATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.7

.. py:class:: hl7types.hl7.v2_2.segments.IN3.IN3
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``in3_1``
     - 4
     - str
     - R
     -
     - 00502
     - Set ID - insurance certification
   * - 2
     - ``in3_2``
     - 25
     - str
     - O
     -
     - 00503
     - Certification number
   * - 3
     - ``in3_3``
     -
     - str
     - O
     -
     - 00504
     - Certified by
   * - 4
     - ``in3_4``
     - 1
     - str
     - O
     - 0136
     - 00505
     - Certification required
   * - 5
     - ``in3_5``
     -
     - str
     - O
     - 0148
     - 00506
     - Penalty
   * - 6
     - ``in3_6``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00507
     - Certification date / time
   * - 7
     - ``in3_7``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00508
     - Certification modify date / time
   * - 8
     - ``in3_8``
     -
     - str
     - O
     -
     - 00509
     - Operator
   * - 9
     - ``in3_9``
     - 8
     - str
     - O
     -
     - 00510
     - Certification begin date
   * - 10
     - ``in3_10``
     - 8
     - str
     - O
     -
     - 00511
     - Certification end date
   * - 11
     - ``in3_11``
     -
     - str
     - O
     - 0149
     - 00512
     - Days
   * - 12
     - ``in3_12``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00513
     - Non-concur code / description
   * - 13
     - ``in3_13``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00514
     - Non-concur effective date / time
   * - 14
     - ``in3_14``
     -
     - str
     - O
     -
     - 00515
     - Physician reviewer
   * - 15
     - ``in3_15``
     - 48
     - str
     - O
     -
     - 00516
     - Certification contact
   * - 16
     - ``in3_16``
     - 40
     - list[str]
     - O
     -
     - 00517
     - Certification contact phone number
   * - 17
     - ``in3_17``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00518
     - Appeal reason
   * - 18
     - ``in3_18``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00519
     - Certification agency
   * - 19
     - ``in3_19``
     - 40
     - list[str]
     - O
     -
     - 00520
     - Certification agency phone number
   * - 20
     - ``in3_20``
     -
     - list[str]
     - O
     - 0150
     - 00521
     - Pre-certification required / window
   * - 21
     - ``in3_21``
     - 48
     - str
     - O
     -
     - 00522
     - Case manager
   * - 22
     - ``in3_22``
     - 8
     - str
     - O
     -
     - 00523
     - Second opinion date
   * - 23
     - ``in3_23``
     - 1
     - str
     - O
     - 0151
     - 00524
     - Second opinion status
   * - 24
     - ``in3_24``
     - 1
     - str
     - O
     - 0152
     - 00525
     - Second opinion documentation received
   * - 25
     - ``in3_25``
     -
     - str
     - O
     -
     - 00526
     - Second opinion practitioner

.. _hl7-v2_2-MFA:

MFA: MASTER FILE ACKNOWLEDGEMENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.4.3

.. py:class:: hl7types.hl7.v2_2.segments.MFA.MFA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``mfa_1``
     - 3
     - str
     - R
     - 0180
     - 00664
     - Record-level event code
   * - 2
     - ``mfa_2``
     - 20
     - str
     - C
     -
     - 00665
     - MFN control ID
   * - 3
     - ``mfa_3``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - C
     -
     - 00668
     - Event completion date / time
   * - 4
     - ``mfa_4``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     - 0181
     - 00669
     - Error return code and/or text
   * - 5
     - ``mfa_5``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - R
     -
     - 00667
     - Primary key value

.. _hl7-v2_2-MFE:

MFE: MASTER FILE ENTRY
~~~~~~~~~~~~~~~~~~~~~~

Section 8.4.2

.. py:class:: hl7types.hl7.v2_2.segments.MFE.MFE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``mfe_1``
     - 3
     - str
     - R
     - 0180
     - 00664
     - Record-level event code
   * - 2
     - ``mfe_2``
     - 20
     - str
     - C
     -
     - 00665
     - MFN control ID
   * - 3
     - ``mfe_3``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00662
     - Effective date / time
   * - 4
     - ``mfe_4``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - R
     -
     - 00667
     - Primary key value

.. _hl7-v2_2-MFI:

MFI: MASTER FILE IDENTIFICATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.4.1

.. py:class:: hl7types.hl7.v2_2.segments.MFI.MFI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``mfi_1``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     - 0175
     - 00658
     - Master file identifier
   * - 2
     - ``mfi_2``
     - 6
     - str
     - O
     - 0176
     - 00659
     - Master file application identifier
   * - 3
     - ``mfi_3``
     - 3
     - str
     - R
     - 0178
     - 00660
     - File-level event code
   * - 4
     - ``mfi_4``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00661
     - Entered date / time
   * - 5
     - ``mfi_5``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00662
     - Effective date / time
   * - 6
     - ``mfi_6``
     - 2
     - str
     - R
     - 0179
     - 00663
     - Response level code

.. _hl7-v2_2-MRG:

MRG: MERGE PATIENT INFORMATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.8

.. py:class:: hl7types.hl7.v2_2.segments.MRG.MRG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``mrg_1``
     -
     - str
     - R
     -
     - 00211
     - Prior Patient ID - Internal
   * - 2
     - ``mrg_2``
     -
     - str
     - O
     -
     - 00212
     - Prior Alternate Patient ID
   * - 3
     - ``mrg_3``
     - 20
     - str
     - O
     -
     - 00213
     - Prior Patient Account Number
   * - 4
     - ``mrg_4``
     - 16
     - str
     - O
     -
     - 00214
     - Prior Patient ID - External

.. _hl7-v2_2-MSA:

MSA: MESSAGE ACKNOWLEDGMENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.10.2

.. py:class:: hl7types.hl7.v2_2.segments.MSA.MSA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``msa_1``
     - 2
     - str
     - R
     - 0008
     - 00018
     - Acknowledgement code
   * - 2
     - ``msa_2``
     - 20
     - str
     - R
     -
     - 00010
     - Message Control ID
   * - 3
     - ``msa_3``
     - 80
     - str
     - O
     -
     - 00020
     - Text Message
   * - 4
     - ``msa_4``
     - 15
     - str
     - O
     -
     - 00021
     - Expected Sequence Number
   * - 5
     - ``msa_5``
     - 1
     - str
     - O
     - 0102
     - 00022
     - Delayed Acknowledgement type
   * - 6
     - ``msa_6``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00023
     - Error Condition

.. _hl7-v2_2-MSH:

MSH: MESSAGE HEADER
~~~~~~~~~~~~~~~~~~~

Section 2.10.1

.. py:class:: hl7types.hl7.v2_2.segments.MSH.MSH
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``msh_1``
     - 1
     - str
     - R
     -
     - 00001
     - Field separator
   * - 2
     - ``msh_2``
     - 4
     - str
     - R
     -
     - 00002
     - Encoding characters
   * - 3
     - ``msh_3``
     - 15
     - str
     - O
     -
     - 00003
     - Sending application
   * - 4
     - ``msh_4``
     - 20
     - str
     - O
     -
     - 00004
     - Sending facility
   * - 5
     - ``msh_5``
     - 30
     - str
     - O
     -
     - 00005
     - Receiving application
   * - 6
     - ``msh_6``
     - 30
     - str
     - O
     -
     - 00006
     - Receiving facility
   * - 7
     - ``msh_7``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00007
     - Date / Time of message
   * - 8
     - ``msh_8``
     - 40
     - str
     - O
     -
     - 00008
     - Security
   * - 9
     - ``msh_9``
     -
     - str
     - R
     - 0076
     - 00009
     - Message type
   * - 10
     - ``msh_10``
     - 20
     - str
     - R
     -
     - 00010
     - Message Control ID
   * - 11
     - ``msh_11``
     - 1
     - str
     - R
     - 0103
     - 00011
     - Processing ID
   * - 12
     - ``msh_12``
     - 8
     - str
     - R
     - 0104
     - 00012
     - Version ID
   * - 13
     - ``msh_13``
     - 15
     - str
     - O
     -
     - 00013
     - Sequence number
   * - 14
     - ``msh_14``
     - 180
     - str
     - O
     -
     - 00014
     - Continuation pointer
   * - 15
     - ``msh_15``
     - 2
     - str
     - O
     - 0155
     - 00015
     - Accept acknowledgement type
   * - 16
     - ``msh_16``
     - 2
     - str
     - O
     - 0155
     - 00016
     - Application acknowledgement type
   * - 17
     - ``msh_17``
     - 2
     - str
     - O
     -
     - 00017
     - Country code

.. _hl7-v2_2-NCK:

NCK: System Clock
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.NCK.NCK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``nck_1``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - R
     -
     - 00742
     - System Date/Time

.. _hl7-v2_2-NK1:

NK1: NEXT OF KIN
~~~~~~~~~~~~~~~~

Section 3.3.5

.. py:class:: hl7types.hl7.v2_2.segments.NK1.NK1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``nk1_1``
     - 4
     - str
     - R
     -
     - 00190
     - Set ID - Next of Kin
   * - 2
     - ``nk1_2``
     -
     - :ref:`PN <hl7-v2_2-PN>`
     - O
     -
     - 00191
     - Name
   * - 3
     - ``nk1_3``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     - 0063
     - 00192
     - Relationship
   * - 4
     - ``nk1_4``
     -
     - :ref:`AD <hl7-v2_2-AD>`
     - O
     -
     - 00193
     - Address
   * - 5
     - ``nk1_5``
     - 40
     - list[str]
     - O
     -
     - 00194
     - Phone Number
   * - 6
     - ``nk1_6``
     - 40
     - str
     - O
     -
     - 00195
     - Business Phone Number
   * - 7
     - ``nk1_7``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     - 0131
     - 00196
     - Contact Role
   * - 8
     - ``nk1_8``
     - 8
     - str
     - O
     -
     - 00197
     - Start Date
   * - 9
     - ``nk1_9``
     - 8
     - str
     - O
     -
     - 00198
     - End Date
   * - 10
     - ``nk1_10``
     - 60
     - str
     - O
     -
     - 00199
     - Next of Kin
   * - 11
     - ``nk1_11``
     -
     - str
     - O
     -
     - 00200
     - Next of kin job code / class
   * - 12
     - ``nk1_12``
     - 20
     - str
     - O
     -
     - 00201
     - Next of Kin Employee Number
   * - 13
     - ``nk1_13``
     - 60
     - str
     - O
     -
     - 00202
     - Organization Name

.. _hl7-v2_2-NPU:

NPU: BED STATUS UPDATE
~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.7

.. py:class:: hl7types.hl7.v2_2.segments.NPU.NPU
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``npu_1``
     -
     - str
     - R
     - 0079
     - 00209
     - Bed Location
   * - 2
     - ``npu_2``
     - 1
     - str
     - O
     - 0116
     - 00170
     - Bed Status

.. _hl7-v2_2-NSC:

NSC: STATUS CHANGE
~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.NSC.NSC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``nsc_1``
     - 4
     - str
     - R
     -
     - 00758
     - Network Change Type
   * - 2
     - ``nsc_2``
     - 30
     - str
     - O
     -
     - 00759
     - Current CPU
   * - 3
     - ``nsc_3``
     - 30
     - str
     - O
     -
     - 00760
     - Current Fileserver
   * - 4
     - ``nsc_4``
     - 30
     - str
     - O
     -
     - 00761
     - Current Application
   * - 5
     - ``nsc_5``
     - 30
     - str
     - O
     -
     - 00762
     - Current Facility
   * - 6
     - ``nsc_6``
     - 30
     - str
     - O
     -
     - 00763
     - New CPU
   * - 7
     - ``nsc_7``
     - 30
     - str
     - O
     -
     - 00764
     - New Fileserver
   * - 8
     - ``nsc_8``
     - 30
     - str
     - O
     -
     - 00765
     - New Application
   * - 9
     - ``nsc_9``
     - 30
     - str
     - O
     -
     - 00766
     - New Facility

.. _hl7-v2_2-NST:

NST: Statistics
~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.NST.NST
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``nst_1``
     - 1
     - str
     - R
     - 0136
     - 00743
     - Statistics Available
   * - 2
     - ``nst_2``
     - 30
     - str
     - O
     -
     - 00744
     - Source Identifier
   * - 3
     - ``nst_3``
     - 3
     - str
     - O
     -
     - 00745
     - Source Type
   * - 4
     - ``nst_4``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00746
     - Statistics Start
   * - 5
     - ``nst_5``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00747
     - Statistics End
   * - 6
     - ``nst_6``
     - 10
     - str
     - O
     -
     - 00748
     - Receive Character Count
   * - 7
     - ``nst_7``
     - 10
     - str
     - O
     -
     - 00749
     - Send Character Count
   * - 8
     - ``nst_8``
     - 10
     - str
     - O
     -
     - 00750
     - Message Received
   * - 9
     - ``nst_9``
     - 10
     - str
     - O
     -
     - 00751
     - Message Sent
   * - 10
     - ``nst_10``
     - 10
     - str
     - O
     -
     - 00752
     - Checksum Errors Received
   * - 11
     - ``nst_11``
     - 10
     - str
     - O
     -
     - 00753
     - Length Errors Received
   * - 12
     - ``nst_12``
     - 10
     - str
     - O
     -
     - 00754
     - Other Errors Received
   * - 13
     - ``nst_13``
     - 10
     - str
     - O
     -
     - 00755
     - Connect Timeouts
   * - 14
     - ``nst_14``
     - 10
     - str
     - O
     -
     - 00756
     - Receive Timeouts
   * - 15
     - ``nst_15``
     - 10
     - str
     - O
     -
     - 00757
     - Network Errors

.. _hl7-v2_2-NTE:

NTE: NOTES AND COMMENTS
~~~~~~~~~~~~~~~~~~~~~~~

Section 2.10.15

.. py:class:: hl7types.hl7.v2_2.segments.NTE.NTE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``nte_1``
     - 4
     - str
     - O
     -
     - 00096
     - Set ID - Notes and Comments
   * - 2
     - ``nte_2``
     - 8
     - str
     - O
     - 0105
     - 00097
     - Source of Comment
   * - 3
     - ``nte_3``
     -
     - list[str]
     - O
     -
     - 00098
     - Comment

.. _hl7-v2_2-OBR:

OBR: OBSERVATION REQUEST
~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.1

.. py:class:: hl7types.hl7.v2_2.segments.OBR.OBR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``obr_1``
     - 4
     - str
     - O
     -
     - 00237
     - Set ID - Observation Request
   * - 2
     - ``obr_2``
     -
     - str
     - C
     -
     - 00216
     - Placer Order Number
   * - 3
     - ``obr_3``
     -
     - str
     - C
     -
     - 00217
     - Filler Order Number
   * - 4
     - ``obr_4``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00238
     - Universal Service ID
   * - 5
     - ``obr_5``
     - 2
     - str
     - O
     -
     - 00239
     - Priority (not used)
   * - 6
     - ``obr_6``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00240
     - Requested date / time (not used)
   * - 7
     - ``obr_7``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - C
     -
     - 00241
     - Observation date / time
   * - 8
     - ``obr_8``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - C
     -
     - 00242
     - Observation end date / time
   * - 9
     - ``obr_9``
     -
     - str
     - C
     -
     - 00243
     - Collection Volume
   * - 10
     - ``obr_10``
     -
     - list[str]
     - O
     -
     - 00244
     - Collector Identifier
   * - 11
     - ``obr_11``
     - 1
     - str
     - O
     - 0065
     - 00245
     - Specimen action code
   * - 12
     - ``obr_12``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00246
     - Danger Code
   * - 13
     - ``obr_13``
     - 300
     - str
     - O
     -
     - 00247
     - Relevant clinical information
   * - 14
     - ``obr_14``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - C
     -
     - 00248
     - Specimen received date / time
   * - 15
     - ``obr_15``
     -
     - str
     - O
     - 0070
     - 00249
     - Specimen source
   * - 16
     - ``obr_16``
     -
     - str
     - O
     -
     - 00226
     - Ordering Provider
   * - 17
     - ``obr_17``
     - 40
     - list[str]
     - O
     -
     - 00250
     - Order Callback Phone Number
   * - 18
     - ``obr_18``
     - 60
     - str
     - O
     -
     - 00251
     - Placer field 1
   * - 19
     - ``obr_19``
     - 60
     - str
     - O
     -
     - 00252
     - Placer field 2
   * - 20
     - ``obr_20``
     - 60
     - str
     - O
     -
     - 00253
     - Filler Field 1
   * - 21
     - ``obr_21``
     - 60
     - str
     - O
     -
     - 00254
     - Filler Field 2
   * - 22
     - ``obr_22``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - C
     -
     - 00255
     - Results report / status change - date / time
   * - 23
     - ``obr_23``
     -
     - str
     - O
     -
     - 00256
     - Charge to Practice
   * - 24
     - ``obr_24``
     - 10
     - str
     - O
     - 0074
     - 00257
     - Diagnostic service section ID
   * - 25
     - ``obr_25``
     - 1
     - str
     - C
     - 0123
     - 00258
     - Result Status
   * - 26
     - ``obr_26``
     -
     - str
     - O
     -
     - 00259
     - Parent Result
   * - 27
     - ``obr_27``
     -
     - list[:ref:`TQ <hl7-v2_2-TQ>`]
     - O
     -
     - 00221
     - Quantity / timing
   * - 28
     - ``obr_28``
     -
     - list[str]
     - O
     -
     - 00260
     - Result Copies To
   * - 29
     - ``obr_29``
     -
     - str
     - O
     -
     - 00261
     - Parent Number
   * - 30
     - ``obr_30``
     - 20
     - str
     - O
     - 0124
     - 00262
     - Transportation Mode
   * - 31
     - ``obr_31``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00263
     - Reason for Study
   * - 32
     - ``obr_32``
     -
     - str
     - O
     -
     - 00264
     - Principal Result Interpreter
   * - 33
     - ``obr_33``
     -
     - list[str]
     - O
     -
     - 00265
     - Assistant Result Interpreter
   * - 34
     - ``obr_34``
     -
     - list[str]
     - O
     -
     - 00266
     - Technician
   * - 35
     - ``obr_35``
     -
     - list[str]
     - O
     -
     - 00267
     - Transcriptionist
   * - 36
     - ``obr_36``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00268
     - Scheduled date / time

.. _hl7-v2_2-OBX:

OBX: OBSERVATION RESULT
~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.2

.. py:class:: hl7types.hl7.v2_2.segments.OBX.OBX
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``obx_1``
     - 4
     - str
     - O
     -
     - 00569
     - Set ID - Observational Simple
   * - 2
     - ``obx_2``
     - 2
     - str
     - R
     - 0125
     - 00570
     - Value Type
   * - 3
     - ``obx_3``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00571
     - Observation Identifier
   * - 4
     - ``obx_4``
     - 20
     - str
     - C
     -
     - 00572
     - Observation Sub-ID
   * - 5
     - ``obx_5``
     -
     - str
     - C
     -
     - 00573
     - Observation Value
   * - 6
     - ``obx_6``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00574
     - Units
   * - 7
     - ``obx_7``
     - 60
     - str
     - O
     -
     - 00575
     - References Range
   * - 8
     - ``obx_8``
     - 10
     - list[str]
     - O
     - 0078
     - 00576
     - Abnormal Flags
   * - 9
     - ``obx_9``
     - 5
     - str
     - O
     -
     - 00577
     - Probability
   * - 10
     - ``obx_10``
     - 5
     - str
     - O
     - 0080
     - 00578
     - Nature of Abnormal Test
   * - 11
     - ``obx_11``
     - 2
     - str
     - R
     - 0085
     - 00579
     - Observation result status
   * - 12
     - ``obx_12``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00580
     - Effective date last observation normal values
   * - 13
     - ``obx_13``
     - 20
     - str
     - O
     -
     - 00581
     - User Defined Access Checks
   * - 14
     - ``obx_14``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00582
     - Date / time of the observation
   * - 15
     - ``obx_15``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00583
     - Producer's ID
   * - 16
     - ``obx_16``
     -
     - str
     - O
     -
     - 00584
     - Responsible Observer

.. _hl7-v2_2-ODS:

ODS: DIETARY ORDERS, SUPPLEMENTS, and PREFERENCES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.6.1

.. py:class:: hl7types.hl7.v2_2.segments.ODS.ODS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``ods_1``
     - 1
     - str
     - R
     - 0159
     - 00269
     - Type
   * - 2
     - ``ods_2``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00270
     - Service Period
   * - 3
     - ``ods_3``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - R
     -
     - 00271
     - Diet, Supplement, or Preference Code
   * - 4
     - ``ods_4``
     - 80
     - list[str]
     - O
     -
     - 00272
     - Text Instruction

.. _hl7-v2_2-ODT:

ODT: DIET TRAY INSTRUCTION
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.6.2

.. py:class:: hl7types.hl7.v2_2.segments.ODT.ODT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``odt_1``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     - 0160
     - 00273
     - Tray Type
   * - 2
     - ``odt_2``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00270
     - Service Period
   * - 3
     - ``odt_3``
     - 80
     - list[str]
     - O
     -
     - 00272
     - Text Instruction

.. _hl7-v2_2-OM1:

OM1: GENERAL - fields that apply to most observations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.4

.. py:class:: hl7types.hl7.v2_2.segments.OM1.OM1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``om1_1``
     - 3
     - str
     - O
     -
     - 00585
     - Segment Type ID
   * - 2
     - ``om1_2``
     - 4
     - str
     - O
     -
     - 00586
     - Sequence Number - Test/ Observation Master File
   * - 3
     - ``om1_3``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00587
     - Producer's test / observation ID
   * - 4
     - ``om1_4``
     - 12
     - list[str]
     - O
     - 0125
     - 00588
     - Permitted Data Types
   * - 5
     - ``om1_5``
     - 1
     - str
     - R
     - 0136
     - 00589
     - Specimen Required
   * - 6
     - ``om1_6``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00590
     - Producer ID
   * - 7
     - ``om1_7``
     -
     - str
     - O
     -
     - 00591
     - Observation Description
   * - 8
     - ``om1_8``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00592
     - Other test / observation IDs for the observation
   * - 9
     - ``om1_9``
     - 200
     - list[str]
     - R
     -
     - 00593
     - Other Names
   * - 10
     - ``om1_10``
     - 30
     - str
     - O
     -
     - 00594
     - Preferred Report Name for the Observation
   * - 11
     - ``om1_11``
     - 8
     - str
     - O
     -
     - 00595
     - Preferred Short Name or Mnemonic for Observation
   * - 12
     - ``om1_12``
     - 200
     - str
     - O
     -
     - 00596
     - Preferred Long Name for the Observation
   * - 13
     - ``om1_13``
     - 1
     - str
     - O
     - 0136
     - 00597
     - Orderability
   * - 14
     - ``om1_14``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00598
     - Identity of instrument used to perform this study
   * - 15
     - ``om1_15``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00599
     - Coded Representation of Method
   * - 16
     - ``om1_16``
     - 1
     - str
     - O
     - 0136
     - 00600
     - Portable
   * - 17
     - ``om1_17``
     - 1
     - list[str]
     - O
     -
     - 00601
     - Observation producing department / section
   * - 18
     - ``om1_18``
     - 40
     - str
     - O
     -
     - 00602
     - Telephone Number of Section
   * - 19
     - ``om1_19``
     - 1
     - str
     - R
     - 0174
     - 00603
     - Nature of test / observation
   * - 20
     - ``om1_20``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00604
     - Report Subheader
   * - 21
     - ``om1_21``
     - 20
     - str
     - O
     -
     - 00605
     - Report Display Order
   * - 22
     - ``om1_22``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - R
     -
     - 00606
     - Date / time stamp for any change in definition for obs
   * - 23
     - ``om1_23``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00607
     - Effective date / time of change
   * - 24
     - ``om1_24``
     - 20
     - str
     - O
     -
     - 00608
     - Typical Turn-around Time
   * - 25
     - ``om1_25``
     - 20
     - str
     - O
     -
     - 00609
     - Processing Time
   * - 26
     - ``om1_26``
     - 40
     - list[str]
     - O
     - 0168
     - 00610
     - Processing Priority
   * - 27
     - ``om1_27``
     - 5
     - str
     - O
     - 0169
     - 00611
     - Reporting Priority
   * - 28
     - ``om1_28``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00612
     - Outside Site(s) Where Observation may be Performed
   * - 29
     - ``om1_29``
     -
     - list[:ref:`AD <hl7-v2_2-AD>`]
     - O
     -
     - 00613
     - Address of Outside Site(s)
   * - 30
     - ``om1_30``
     - 400
     - list[str]
     - O
     -
     - 00614
     - Phone Number of Outside Site
   * - 31
     - ``om1_31``
     - 1
     - str
     - O
     - 0177
     - 00615
     - Confidentiality Code
   * - 32
     - ``om1_32``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00616
     - Observations required to interpret the observation
   * - 33
     - ``om1_33``
     -
     - str
     - O
     -
     - 00617
     - Interpretation of Observations
   * - 34
     - ``om1_34``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00618
     - Contraindications to Observations
   * - 35
     - ``om1_35``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00619
     - Reflex tests / observations
   * - 36
     - ``om1_36``
     - 80
     - str
     - O
     -
     - 00620
     - Rules that Trigger Reflex Testing
   * - 37
     - ``om1_37``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00621
     - Fixed Canned Message
   * - 38
     - ``om1_38``
     -
     - str
     - O
     -
     - 00622
     - Patient Preparation
   * - 39
     - ``om1_39``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00623
     - Procedure Medication
   * - 40
     - ``om1_40``
     -
     - str
     - O
     -
     - 00624
     - Factors that may affect the observation
   * - 41
     - ``om1_41``
     - 60
     - list[str]
     - O
     -
     - 00625
     - Test / observation performance schedule
   * - 42
     - ``om1_42``
     -
     - str
     - O
     -
     - 00626
     - Description of Test Methods

.. _hl7-v2_2-OM2:

OM2: NUMERIC OBSERVATION
~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.5

.. py:class:: hl7types.hl7.v2_2.segments.OM2.OM2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``om2_1``
     - 3
     - str
     - O
     -
     - 00585
     - Segment Type ID
   * - 2
     - ``om2_2``
     - 4
     - str
     - O
     -
     - 00586
     - Sequence Number - Test/ Observation Master File
   * - 3
     - ``om2_3``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00627
     - Units of Measure
   * - 4
     - ``om2_4``
     - 10
     - str
     - O
     -
     - 00628
     - Range of Decimal Precision
   * - 5
     - ``om2_5``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00629
     - Corresponding SI Units of Measure
   * - 6
     - ``om2_6``
     -
     - list[str]
     - R
     -
     - 00630
     - SI Conversion Factor
   * - 7
     - ``om2_7``
     -
     - list[str]
     - O
     -
     - 00631
     - Reference (normal) range - ordinal & continuous observations
   * - 8
     - ``om2_8``
     -
     - str
     - O
     -
     - 00632
     - Critical range for ordinal and continuous observations
   * - 9
     - ``om2_9``
     -
     - str
     - O
     -
     - 00633
     - Absolute range for ordinal and continuous observations
   * - 10
     - ``om2_10``
     -
     - list[str]
     - O
     -
     - 00634
     - Delta Check Criteria
   * - 11
     - ``om2_11``
     - 20
     - str
     - O
     -
     - 00635
     - Minimum Meaningful Increments

.. _hl7-v2_2-OM3:

OM3: CATEGORICAL TEST/OBSERVATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.6

.. py:class:: hl7types.hl7.v2_2.segments.OM3.OM3
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``om3_1``
     - 3
     - str
     - O
     -
     - 00585
     - Segment Type ID
   * - 2
     - ``om3_2``
     - 4
     - str
     - O
     -
     - 00586
     - Sequence Number - Test/ Observation Master File
   * - 3
     - ``om3_3``
     - 5
     - str
     - O
     -
     - 00636
     - Preferred Coding System
   * - 4
     - ``om3_4``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00637
     - Valid coded answers
   * - 5
     - ``om3_5``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00638
     - Normal test codes for categorical observations
   * - 6
     - ``om3_6``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00639
     - Abnormal test codes for categorical observations
   * - 7
     - ``om3_7``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00640
     - Critical test codes for categorical observations
   * - 8
     - ``om3_8``
     - 2
     - str
     - O
     -
     - 00641
     - Data Type

.. _hl7-v2_2-OM4:

OM4: OBSERVATION that require specimens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.7

.. py:class:: hl7types.hl7.v2_2.segments.OM4.OM4
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``om4_1``
     - 3
     - str
     - O
     -
     - 00585
     - Segment Type ID
   * - 2
     - ``om4_2``
     - 4
     - str
     - O
     -
     - 00586
     - Sequence Number - Test/ Observation Master File
   * - 3
     - ``om4_3``
     - 1
     - str
     - O
     - 0170
     - 00642
     - Derived Specimen
   * - 4
     - ``om4_4``
     -
     - str
     - O
     -
     - 00643
     - Container Description
   * - 5
     - ``om4_5``
     - 20
     - str
     - O
     -
     - 00644
     - Container Volume
   * - 6
     - ``om4_6``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00645
     - Container Units
   * - 7
     - ``om4_7``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00646
     - Specimen
   * - 8
     - ``om4_8``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00647
     - Additive
   * - 9
     - ``om4_9``
     -
     - str
     - O
     -
     - 00648
     - Preparation
   * - 10
     - ``om4_10``
     -
     - str
     - O
     -
     - 00649
     - Special Handling Requirements
   * - 11
     - ``om4_11``
     -
     - str
     - O
     -
     - 00650
     - Normal Collection Volume
   * - 12
     - ``om4_12``
     -
     - str
     - O
     -
     - 00651
     - Minimum Collection Volume
   * - 13
     - ``om4_13``
     -
     - str
     - O
     -
     - 00652
     - Specimen Requirements
   * - 14
     - ``om4_14``
     - 60
     - list[str]
     - O
     - 0027
     - 00653
     - Specimen Priorities
   * - 15
     - ``om4_15``
     -
     - str
     - O
     -
     - 00654
     - Specimen Retention Time

.. _hl7-v2_2-OM5:

OM5: OBSERVATION BATTERIES
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.8

.. py:class:: hl7types.hl7.v2_2.segments.OM5.OM5
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``om5_1``
     - 3
     - str
     - O
     -
     - 00585
     - Segment Type ID
   * - 2
     - ``om5_2``
     - 4
     - str
     - O
     -
     - 00586
     - Sequence Number - Test/ Observation Master File
   * - 3
     - ``om5_3``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00655
     - Tests / observations included within an ordered test battery
   * - 4
     - ``om5_4``
     - 200
     - str
     - O
     -
     - 00656
     - Observation ID Suffixes

.. _hl7-v2_2-OM6:

OM6: OBSERVATIONS that are calculated from other obersvations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.9

.. py:class:: hl7types.hl7.v2_2.segments.OM6.OM6
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``om6_1``
     - 3
     - str
     - O
     -
     - 00585
     - Segment Type ID
   * - 2
     - ``om6_2``
     - 4
     - str
     - O
     -
     - 00586
     - Sequence Number - Test/ Observation Master File
   * - 3
     - ``om6_3``
     -
     - str
     - O
     -
     - 00657
     - Derivation Rule

.. _hl7-v2_2-ORC:

ORC: COMMOM ORDER
~~~~~~~~~~~~~~~~~

Section 4.3.1

.. py:class:: hl7types.hl7.v2_2.segments.ORC.ORC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``orc_1``
     - 2
     - str
     - R
     - 0119
     - 00215
     - Order Control
   * - 2
     - ``orc_2``
     -
     - str
     - C
     -
     - 00216
     - Placer Order Number
   * - 3
     - ``orc_3``
     -
     - str
     - C
     -
     - 00217
     - Filler Order Number
   * - 4
     - ``orc_4``
     -
     - str
     - O
     -
     - 00218
     - Placer Group Number
   * - 5
     - ``orc_5``
     - 2
     - str
     - O
     - 0038
     - 00219
     - Order Status
   * - 6
     - ``orc_6``
     - 1
     - str
     - O
     - 0121
     - 00220
     - Response Flag
   * - 7
     - ``orc_7``
     -
     - list[:ref:`TQ <hl7-v2_2-TQ>`]
     - O
     -
     - 00221
     - Quantity / timing
   * - 8
     - ``orc_8``
     -
     - str
     - O
     -
     - 00222
     - Parent
   * - 9
     - ``orc_9``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00223
     - Date / time of transaction
   * - 10
     - ``orc_10``
     -
     - str
     - O
     -
     - 00224
     - Entered By
   * - 11
     - ``orc_11``
     -
     - str
     - O
     -
     - 00225
     - Verified By
   * - 12
     - ``orc_12``
     -
     - str
     - O
     -
     - 00226
     - Ordering Provider
   * - 13
     - ``orc_13``
     -
     - str
     - O
     -
     - 00227
     - Enterer's Location
   * - 14
     - ``orc_14``
     - 40
     - list[str]
     - O
     -
     - 00228
     - Call Back Phone Number
   * - 15
     - ``orc_15``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00229
     - Order effective date / time
   * - 16
     - ``orc_16``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00230
     - Order Control Code Reason
   * - 17
     - ``orc_17``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00231
     - Entering Organization
   * - 18
     - ``orc_18``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00232
     - Entering Device
   * - 19
     - ``orc_19``
     -
     - str
     - O
     -
     - 00233
     - Action by

.. _hl7-v2_2-PID:

PID: PATIENT IDENTIFICATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.2

.. py:class:: hl7types.hl7.v2_2.segments.PID.PID
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``pid_1``
     - 4
     - str
     - O
     -
     - 00104
     - Set ID - Patient ID
   * - 2
     - ``pid_2``
     - 16
     - str
     - O
     -
     - 00105
     - Patient ID (External ID)
   * - 3
     - ``pid_3``
     -
     - list[str]
     - R
     -
     - 00106
     - Patient ID (Internal ID)
   * - 4
     - ``pid_4``
     - 12
     - str
     - O
     -
     - 00107
     - Alternate Patient ID
   * - 5
     - ``pid_5``
     -
     - :ref:`PN <hl7-v2_2-PN>`
     - R
     -
     - 00108
     - Patient Name
   * - 6
     - ``pid_6``
     - 30
     - str
     - O
     -
     - 00109
     - Mother's Maiden Name
   * - 7
     - ``pid_7``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00110
     - Date of Birth
   * - 8
     - ``pid_8``
     - 1
     - str
     - O
     - 0001
     - 00111
     - Sex
   * - 9
     - ``pid_9``
     -
     - list[:ref:`PN <hl7-v2_2-PN>`]
     - O
     -
     - 00112
     - Patient Alias
   * - 10
     - ``pid_10``
     - 1
     - str
     - O
     - 0005
     - 00113
     - Race
   * - 11
     - ``pid_11``
     -
     - list[:ref:`AD <hl7-v2_2-AD>`]
     - O
     -
     - 00114
     - Patient Address
   * - 12
     - ``pid_12``
     - 4
     - str
     - O
     -
     - 00115
     - County code
   * - 13
     - ``pid_13``
     - 40
     - list[str]
     - O
     -
     - 00116
     - Phone Number - Home
   * - 14
     - ``pid_14``
     - 40
     - list[str]
     - O
     -
     - 00117
     - Phone Number - Business
   * - 15
     - ``pid_15``
     - 25
     - str
     - O
     -
     - 00118
     - Language - Patient
   * - 16
     - ``pid_16``
     - 1
     - str
     - O
     - 0002
     - 00119
     - Marital Status
   * - 17
     - ``pid_17``
     - 3
     - str
     - O
     - 0006
     - 00120
     - Religion
   * - 18
     - ``pid_18``
     - 20
     - str
     - O
     -
     - 00121
     - Patient Account Number
   * - 19
     - ``pid_19``
     - 16
     - str
     - O
     -
     - 00122
     - Social security number - patient
   * - 20
     - ``pid_20``
     -
     - str
     - O
     -
     - 00123
     - Driver's license number - patient
   * - 21
     - ``pid_21``
     - 20
     - str
     - O
     -
     - 00124
     - Mother's Identifier
   * - 22
     - ``pid_22``
     - 1
     - str
     - O
     - 0189
     - 00125
     - Ethnic Group
   * - 23
     - ``pid_23``
     - 25
     - str
     - O
     -
     - 00126
     - Birth Place
   * - 24
     - ``pid_24``
     - 2
     - str
     - O
     -
     - 00127
     - Multiple Birth Indicator
   * - 25
     - ``pid_25``
     - 2
     - str
     - O
     -
     - 00128
     - Birth Order
   * - 26
     - ``pid_26``
     - 3
     - list[str]
     - O
     - 0171
     - 00129
     - Citizenship
   * - 27
     - ``pid_27``
     - 60
     - str
     - O
     -
     - 00130
     - Veterans Military Status

.. _hl7-v2_2-PR1:

PR1: PROCEDURES
~~~~~~~~~~~~~~~

Section 6.4.3

.. py:class:: hl7types.hl7.v2_2.segments.PR1.PR1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``pr1_1``
     - 4
     - str
     - R
     -
     - 00391
     - Set ID - procedure
   * - 2
     - ``pr1_2``
     - 2
     - list[str]
     - R
     - 0089
     - 00392
     - Procedure coding method
   * - 3
     - ``pr1_3``
     - 10
     - list[str]
     - R
     - 0088
     - 00393
     - Procedure code
   * - 4
     - ``pr1_4``
     - 40
     - list[str]
     - O
     -
     - 00394
     - Procedure description
   * - 5
     - ``pr1_5``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - R
     -
     - 00395
     - Procedure date / time
   * - 6
     - ``pr1_6``
     - 2
     - str
     - R
     - 0090
     - 00396
     - Procedure type
   * - 7
     - ``pr1_7``
     - 4
     - str
     - O
     -
     - 00397
     - Procedure minutes
   * - 8
     - ``pr1_8``
     -
     - str
     - O
     - 0010
     - 00398
     - Anesthesiologist
   * - 9
     - ``pr1_9``
     - 2
     - str
     - O
     - 0019
     - 00399
     - Anesthesia code
   * - 10
     - ``pr1_10``
     - 4
     - str
     - O
     -
     - 00400
     - Anesthesia minutes
   * - 11
     - ``pr1_11``
     -
     - str
     - O
     - 0010
     - 00401
     - Surgeon
   * - 12
     - ``pr1_12``
     -
     - list[str]
     - O
     - 0010
     - 00402
     - Procedure Practitioner
   * - 13
     - ``pr1_13``
     - 2
     - str
     - O
     - 0059
     - 00403
     - Consent code
   * - 14
     - ``pr1_14``
     - 2
     - str
     - O
     -
     - 00404
     - Procedure priority

.. _hl7-v2_2-PRA:

PRA: practitioner detail
~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.1.2

.. py:class:: hl7types.hl7.v2_2.segments.PRA.PRA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``pra_1``
     - 20
     - str
     - R
     -
     - 00685
     - PRA - primary key value
   * - 2
     - ``pra_2``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00686
     - Practitioner group
   * - 3
     - ``pra_3``
     - 3
     - list[str]
     - O
     - 0186
     - 00687
     - Practitioner Category
   * - 4
     - ``pra_4``
     - 1
     - str
     - O
     - 0187
     - 00688
     - Provider Billing
   * - 5
     - ``pra_5``
     -
     - list[str]
     - O
     -
     - 00689
     - Specialty
   * - 6
     - ``pra_6``
     -
     - list[str]
     - O
     -
     - 00690
     - Practitioner ID Numbers
   * - 7
     - ``pra_7``
     -
     - list[str]
     - O
     -
     - 00691
     - Privileges

.. _hl7-v2_2-PV1:

PV1: PATIENT VISIT
~~~~~~~~~~~~~~~~~~

Section 3.3.3

.. py:class:: hl7types.hl7.v2_2.segments.PV1.PV1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``pv1_1``
     - 4
     - str
     - O
     -
     - 00131
     - Set ID - Patient Visit
   * - 2
     - ``pv1_2``
     - 1
     - str
     - R
     - 0004
     - 00132
     - Patient Class
   * - 3
     - ``pv1_3``
     -
     - str
     - O
     - 0079
     - 00133
     - Assigned Patient Location
   * - 4
     - ``pv1_4``
     - 2
     - str
     - O
     - 0007
     - 00134
     - Admission Type
   * - 5
     - ``pv1_5``
     - 20
     - str
     - O
     -
     - 00135
     - Preadmit Number
   * - 6
     - ``pv1_6``
     -
     - str
     - O
     -
     - 00136
     - Prior Patient Location
   * - 7
     - ``pv1_7``
     -
     - str
     - O
     - 0010
     - 00137
     - Attending Doctor
   * - 8
     - ``pv1_8``
     -
     - str
     - O
     - 0010
     - 00138
     - Referring Doctor
   * - 9
     - ``pv1_9``
     -
     - list[str]
     - O
     - 0010
     - 00139
     - Consulting Doctor
   * - 10
     - ``pv1_10``
     - 3
     - str
     - O
     - 0069
     - 00140
     - Hospital Service
   * - 11
     - ``pv1_11``
     -
     - str
     - O
     - 0079
     - 00141
     - Temporary Location
   * - 12
     - ``pv1_12``
     - 2
     - str
     - O
     - 0087
     - 00142
     - Preadmit Test Indicator
   * - 13
     - ``pv1_13``
     - 2
     - str
     - O
     - 0092
     - 00143
     - Readmission indicator
   * - 14
     - ``pv1_14``
     - 3
     - str
     - O
     - 0023
     - 00144
     - Admit Source
   * - 15
     - ``pv1_15``
     - 2
     - list[str]
     - O
     - 0009
     - 00145
     - Ambulatory Status
   * - 16
     - ``pv1_16``
     - 2
     - str
     - O
     - 0099
     - 00146
     - VIP Indicator
   * - 17
     - ``pv1_17``
     -
     - str
     - O
     - 0010
     - 00147
     - Admitting Doctor
   * - 18
     - ``pv1_18``
     - 2
     - str
     - O
     - 0018
     - 00148
     - Patient type
   * - 19
     - ``pv1_19``
     -
     - str
     - O
     -
     - 00149
     - Visit Number
   * - 20
     - ``pv1_20``
     -
     - list[str]
     - O
     - 0064
     - 00150
     - Financial Class
   * - 21
     - ``pv1_21``
     - 2
     - str
     - O
     - 0032
     - 00151
     - Charge Price Indicator
   * - 22
     - ``pv1_22``
     - 2
     - str
     - O
     - 0045
     - 00152
     - Courtesy Code
   * - 23
     - ``pv1_23``
     - 2
     - str
     - O
     - 0046
     - 00153
     - Credit Rating
   * - 24
     - ``pv1_24``
     - 2
     - list[str]
     - O
     - 0044
     - 00154
     - Contract Code
   * - 25
     - ``pv1_25``
     - 8
     - list[str]
     - O
     -
     - 00155
     - Contract Effective Date
   * - 26
     - ``pv1_26``
     - 12
     - list[str]
     - O
     -
     - 00156
     - Contract Amount
   * - 27
     - ``pv1_27``
     - 3
     - list[str]
     - O
     -
     - 00157
     - Contract Period
   * - 28
     - ``pv1_28``
     - 2
     - str
     - O
     - 0073
     - 00158
     - Interest Code
   * - 29
     - ``pv1_29``
     - 1
     - str
     - O
     - 0110
     - 00159
     - Transfer to bad debt - code
   * - 30
     - ``pv1_30``
     - 8
     - str
     - O
     -
     - 00160
     - Transfer to bad debt - date
   * - 31
     - ``pv1_31``
     - 10
     - str
     - O
     - 0021
     - 00161
     - Bad Debt Agency Code
   * - 32
     - ``pv1_32``
     - 12
     - str
     - O
     -
     - 00162
     - Bad Debt Transfer Amount
   * - 33
     - ``pv1_33``
     - 12
     - str
     - O
     -
     - 00163
     - Bad Debt Recovery Amount
   * - 34
     - ``pv1_34``
     - 1
     - str
     - O
     - 0111
     - 00164
     - Delete Account Indicator
   * - 35
     - ``pv1_35``
     - 8
     - str
     - O
     -
     - 00165
     - Delete Account Date
   * - 36
     - ``pv1_36``
     - 3
     - str
     - O
     - 0112
     - 00166
     - Discharge Disposition
   * - 37
     - ``pv1_37``
     -
     - str
     - O
     - 0113
     - 00167
     - Discharged to Location
   * - 38
     - ``pv1_38``
     - 2
     - str
     - O
     - 0114
     - 00168
     - Diet Type
   * - 39
     - ``pv1_39``
     - 4
     - str
     - O
     - 0115
     - 00169
     - Servicing Facility
   * - 40
     - ``pv1_40``
     - 1
     - str
     - O
     - 0116
     - 00170
     - Bed Status
   * - 41
     - ``pv1_41``
     - 2
     - str
     - O
     - 0117
     - 00171
     - Account Status
   * - 42
     - ``pv1_42``
     -
     - str
     - O
     -
     - 00172
     - Pending Location
   * - 43
     - ``pv1_43``
     -
     - str
     - O
     -
     - 00173
     - Prior Temporary Location
   * - 44
     - ``pv1_44``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00174
     - Admit date / time
   * - 45
     - ``pv1_45``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00175
     - Discharge date / time
   * - 46
     - ``pv1_46``
     - 12
     - str
     - O
     -
     - 00176
     - Current Patient Balance
   * - 47
     - ``pv1_47``
     - 12
     - str
     - O
     -
     - 00177
     - Total Charges
   * - 48
     - ``pv1_48``
     - 12
     - str
     - O
     -
     - 00178
     - Total Adjustments
   * - 49
     - ``pv1_49``
     - 12
     - str
     - O
     -
     - 00179
     - Total Payments
   * - 50
     - ``pv1_50``
     -
     - str
     - O
     - 0192
     - 00180
     - Alternate Visit ID

.. _hl7-v2_2-PV2:

PV2: PATIENT VISIT - additional information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.4

.. py:class:: hl7types.hl7.v2_2.segments.PV2.PV2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``pv2_1``
     -
     - str
     - O
     -
     - 00181
     - Prior Pending Location
   * - 2
     - ``pv2_2``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     - 0129
     - 00182
     - Accommodation Code
   * - 3
     - ``pv2_3``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00183
     - Admit Reason
   * - 4
     - ``pv2_4``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00184
     - Transfer Reason
   * - 5
     - ``pv2_5``
     - 25
     - list[str]
     - O
     -
     - 00185
     - Patient Valuables
   * - 6
     - ``pv2_6``
     - 25
     - str
     - O
     -
     - 00186
     - Patient Valuables Location
   * - 7
     - ``pv2_7``
     - 2
     - str
     - O
     - 0130
     - 00187
     - Visit User Code
   * - 8
     - ``pv2_8``
     - 8
     - str
     - O
     -
     - 00188
     - Expected Admit Date
   * - 9
     - ``pv2_9``
     - 8
     - str
     - O
     -
     - 00189
     - Expected Discharge Date

.. _hl7-v2_2-QRD:

QRD: QUERY DEFINITION
~~~~~~~~~~~~~~~~~~~~~

Section 2.10.4

.. py:class:: hl7types.hl7.v2_2.segments.QRD.QRD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``qrd_1``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - R
     -
     - 00025
     - Query date / time
   * - 2
     - ``qrd_2``
     - 1
     - str
     - R
     - 0106
     - 00026
     - Query Format Code
   * - 3
     - ``qrd_3``
     - 1
     - str
     - R
     - 0091
     - 00027
     - Query Priority
   * - 4
     - ``qrd_4``
     - 10
     - str
     - R
     -
     - 00028
     - Query ID
   * - 5
     - ``qrd_5``
     - 1
     - str
     - O
     - 0107
     - 00029
     - Deferred Response Type
   * - 6
     - ``qrd_6``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00030
     - Deferred response date / time
   * - 7
     - ``qrd_7``
     -
     - str
     - R
     - 0126
     - 00031
     - Quantity Limited Request
   * - 8
     - ``qrd_8``
     - 20
     - list[str]
     - R
     -
     - 00032
     - Who Subject Filter
   * - 9
     - ``qrd_9``
     - 3
     - list[str]
     - R
     - 0048
     - 00033
     - What Subject Filter
   * - 10
     - ``qrd_10``
     - 20
     - list[str]
     - R
     -
     - 00034
     - What Department Data Code
   * - 11
     - ``qrd_11``
     -
     - list[str]
     - O
     -
     - 00035
     - What data code value qualifier
   * - 12
     - ``qrd_12``
     - 1
     - str
     - O
     - 0108
     - 00036
     - Query Results Level

.. _hl7-v2_2-QRF:

QRF: QUERY FILTER
~~~~~~~~~~~~~~~~~

Section 2.10.5

.. py:class:: hl7types.hl7.v2_2.segments.QRF.QRF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``qrf_1``
     - 20
     - list[str]
     - R
     -
     - 00037
     - Where Subject Filter
   * - 2
     - ``qrf_2``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00038
     - When data start date / time
   * - 3
     - ``qrf_3``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00039
     - When data end date / time
   * - 4
     - ``qrf_4``
     - 20
     - list[str]
     - O
     -
     - 00040
     - What User Qualifier
   * - 5
     - ``qrf_5``
     - 20
     - list[str]
     - O
     -
     - 00041
     - Other QRY Subject Filter
   * - 6
     - ``qrf_6``
     - 12
     - list[str]
     - O
     - 0156
     - 00042
     - Which date / time qualifier
   * - 7
     - ``qrf_7``
     - 12
     - list[str]
     - O
     - 0157
     - 00043
     - Which date / time status qualifier
   * - 8
     - ``qrf_8``
     - 12
     - list[str]
     - O
     - 0158
     - 00044
     - Date / time selection qualifier

.. _hl7-v2_2-RQ1:

RQ1: REQUISITION DETAIL-!
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.7.2

.. py:class:: hl7types.hl7.v2_2.segments.RQ1.RQ1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``rq1_1``
     - 10
     - str
     - O
     -
     - 00285
     - Anticipated Price
   * - 2
     - ``rq1_2``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00286
     - Manufacturer ID
   * - 3
     - ``rq1_3``
     - 16
     - str
     - O
     -
     - 00287
     - Manufacturer's Catalog
   * - 4
     - ``rq1_4``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00288
     - Vendor ID
   * - 5
     - ``rq1_5``
     - 16
     - str
     - O
     -
     - 00289
     - Vendor Catalog
   * - 6
     - ``rq1_6``
     - 1
     - str
     - O
     - 0136
     - 00290
     - Taxable
   * - 7
     - ``rq1_7``
     - 1
     - str
     - O
     - 0136
     - 00291
     - Substitute Allowed

.. _hl7-v2_2-RQD:

RQD: REQUISITION DETAIL
~~~~~~~~~~~~~~~~~~~~~~~

Section 4.7.1

.. py:class:: hl7types.hl7.v2_2.segments.RQD.RQD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``rqd_1``
     - 4
     - str
     - O
     -
     - 00275
     - Requisition Line Number
   * - 2
     - ``rqd_2``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00276
     - Item Code - Internal
   * - 3
     - ``rqd_3``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00277
     - Item Code - External
   * - 4
     - ``rqd_4``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00278
     - Hospital Item Code
   * - 5
     - ``rqd_5``
     - 6
     - str
     - O
     -
     - 00279
     - Requisition Quantity
   * - 6
     - ``rqd_6``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00280
     - Requisition Unit of measure
   * - 7
     - ``rqd_7``
     - 30
     - str
     - O
     -
     - 00281
     - Department cost center
   * - 8
     - ``rqd_8``
     - 30
     - str
     - O
     -
     - 00282
     - Item Natural Account Code
   * - 9
     - ``rqd_9``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00283
     - Deliver-to ID
   * - 10
     - ``rqd_10``
     - 8
     - str
     - O
     -
     - 00284
     - Date Needed

.. _hl7-v2_2-RXA:

RXA: PHARMACY AADMINISTRATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.14

.. py:class:: hl7types.hl7.v2_2.segments.RXA.RXA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``rxa_1``
     - 4
     - str
     - R
     -
     - 00342
     - Give Sub-ID Counter
   * - 2
     - ``rxa_2``
     - 4
     - str
     - R
     -
     - 00344
     - Administration Sub-ID Counter
   * - 3
     - ``rxa_3``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - R
     -
     - 00345
     - Date / time start of administration
   * - 4
     - ``rxa_4``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - R
     -
     - 00346
     - Date / time end of administration
   * - 5
     - ``rxa_5``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00347
     - Administered Code
   * - 6
     - ``rxa_6``
     - 20
     - str
     - R
     -
     - 00348
     - Administered Amount
   * - 7
     - ``rxa_7``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - C
     -
     - 00349
     - Administered Units
   * - 8
     - ``rxa_8``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00350
     - Administered Dosage Form
   * - 9
     - ``rxa_9``
     - 200
     - str
     - C
     -
     - 00351
     - Administration Notes
   * - 10
     - ``rxa_10``
     -
     - str
     - O
     -
     - 00352
     - Administering Provider
   * - 11
     - ``rxa_11``
     -
     - str
     - C
     -
     - 00353
     - Administered-at Location
   * - 12
     - ``rxa_12``
     - 20
     - str
     - C
     -
     - 00354
     - Administered Per (Time Unit)

.. _hl7-v2_2-RXC:

RXC: PHARMACY COMPONENT ORDER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.4

.. py:class:: hl7types.hl7.v2_2.segments.RXC.RXC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``rxc_1``
     - 1
     - str
     - R
     - 0166
     - 00313
     - RX Component Type
   * - 2
     - ``rxc_2``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00314
     - Component Code
   * - 3
     - ``rxc_3``
     - 20
     - str
     - R
     -
     - 00315
     - Component Amount
   * - 4
     - ``rxc_4``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00316
     - Component Units

.. _hl7-v2_2-RXD:

RXD: PHARMACY DISPENSE
~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.10

.. py:class:: hl7types.hl7.v2_2.segments.RXD.RXD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``rxd_1``
     - 4
     - str
     - O
     -
     - 00334
     - Dispense Sub-ID Counter
   * - 2
     - ``rxd_2``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00335
     - Dispense / give code
   * - 3
     - ``rxd_3``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00336
     - Date / time dispensed
   * - 4
     - ``rxd_4``
     - 20
     - str
     - R
     -
     - 00337
     - Actual Dispense Amount
   * - 5
     - ``rxd_5``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - C
     -
     - 00338
     - Actual Dispense Units
   * - 6
     - ``rxd_6``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00339
     - Actual Dosage Form
   * - 7
     - ``rxd_7``
     - 20
     - str
     - R
     -
     - 00325
     - Prescription Number
   * - 8
     - ``rxd_8``
     - 20
     - str
     - C
     -
     - 00326
     - Number of Refills Remaining
   * - 9
     - ``rxd_9``
     - 200
     - list[str]
     - C
     -
     - 00340
     - Dispense Notes
   * - 10
     - ``rxd_10``
     -
     - str
     - O
     -
     - 00341
     - Dispensing Provider
   * - 11
     - ``rxd_11``
     - 1
     - str
     - O
     - 0167
     - 00322
     - Substitution Status
   * - 12
     - ``rxd_12``
     -
     - str
     - O
     -
     - 00329
     - Total Daily Dose
   * - 13
     - ``rxd_13``
     -
     - str
     - C
     -
     - 00299
     - Deliver-to location
   * - 14
     - ``rxd_14``
     - 1
     - str
     - O
     -
     - 00307
     - Needs Human Review
   * - 15
     - ``rxd_15``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00330
     - Pharmacy Special Dispensing Instructions

.. _hl7-v2_2-RXE:

RXE: PHARMACY ENCODED ORDER
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.7

.. py:class:: hl7types.hl7.v2_2.segments.RXE.RXE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``rxe_1``
     -
     - list[:ref:`TQ <hl7-v2_2-TQ>`]
     - O
     -
     - 00221
     - Quantity / timing
   * - 2
     - ``rxe_2``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00317
     - Give Code
   * - 3
     - ``rxe_3``
     - 20
     - str
     - R
     -
     - 00318
     - Give Amount - Minimum
   * - 4
     - ``rxe_4``
     - 20
     - str
     - O
     -
     - 00319
     - Give Amount - Maximum
   * - 5
     - ``rxe_5``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00320
     - Give Units
   * - 6
     - ``rxe_6``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00321
     - Give Dosage Form
   * - 7
     - ``rxe_7``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00298
     - Provider's Administration Instructions
   * - 8
     - ``rxe_8``
     -
     - str
     - C
     -
     - 00299
     - Deliver-to location
   * - 9
     - ``rxe_9``
     - 1
     - str
     - O
     - 0167
     - 00322
     - Substitution Status
   * - 10
     - ``rxe_10``
     - 20
     - str
     - C
     -
     - 00323
     - Dispense Amount
   * - 11
     - ``rxe_11``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - C
     -
     - 00324
     - Dispense Units
   * - 12
     - ``rxe_12``
     - 3
     - str
     - O
     -
     - 00304
     - Number of Refills
   * - 13
     - ``rxe_13``
     -
     - str
     - C
     -
     - 00305
     - Ordering Provider's DEA Number
   * - 14
     - ``rxe_14``
     -
     - str
     - C
     -
     - 00306
     - Pharmacist Verifier ID
   * - 15
     - ``rxe_15``
     - 20
     - str
     - R
     -
     - 00325
     - Prescription Number
   * - 16
     - ``rxe_16``
     - 20
     - str
     - C
     -
     - 00326
     - Number of Refills Remaining
   * - 17
     - ``rxe_17``
     - 20
     - str
     - C
     -
     - 00327
     - Number of refills / doses dispensed
   * - 18
     - ``rxe_18``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - C
     -
     - 00328
     - Date / time of most recent refill or dose dispensed
   * - 19
     - ``rxe_19``
     -
     - str
     - O
     -
     - 00329
     - Total Daily Dose
   * - 20
     - ``rxe_20``
     - 1
     - str
     - O
     -
     - 00307
     - Needs Human Review
   * - 21
     - ``rxe_21``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00330
     - Pharmacy Special Dispensing Instructions
   * - 22
     - ``rxe_22``
     - 20
     - str
     - C
     -
     - 00331
     - Give Per (Time Unit)
   * - 23
     - ``rxe_23``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00332
     - Give Rate Amount
   * - 24
     - ``rxe_24``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00333
     - Give Rate Units

.. _hl7-v2_2-RXG:

RXG: PHARMACY GIVE
~~~~~~~~~~~~~~~~~~

Section 4.8.12

.. py:class:: hl7types.hl7.v2_2.segments.RXG.RXG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``rxg_1``
     - 4
     - str
     - R
     -
     - 00342
     - Give Sub-ID Counter
   * - 2
     - ``rxg_2``
     - 4
     - str
     - O
     -
     - 00334
     - Dispense Sub-ID Counter
   * - 3
     - ``rxg_3``
     -
     - list[:ref:`TQ <hl7-v2_2-TQ>`]
     - O
     -
     - 00221
     - Quantity / timing
   * - 4
     - ``rxg_4``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00317
     - Give Code
   * - 5
     - ``rxg_5``
     - 20
     - str
     - R
     -
     - 00318
     - Give Amount - Minimum
   * - 6
     - ``rxg_6``
     - 20
     - str
     - O
     -
     - 00319
     - Give Amount - Maximum
   * - 7
     - ``rxg_7``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00320
     - Give Units
   * - 8
     - ``rxg_8``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00321
     - Give Dosage Form
   * - 9
     - ``rxg_9``
     - 200
     - str
     - C
     -
     - 00351
     - Administration Notes
   * - 10
     - ``rxg_10``
     - 1
     - str
     - O
     - 0167
     - 00322
     - Substitution Status
   * - 11
     - ``rxg_11``
     -
     - str
     - C
     -
     - 00299
     - Deliver-to location
   * - 12
     - ``rxg_12``
     - 1
     - str
     - O
     -
     - 00307
     - Needs Human Review
   * - 13
     - ``rxg_13``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00343
     - Pharmacy Special Administration Instructions
   * - 14
     - ``rxg_14``
     - 20
     - str
     - C
     -
     - 00331
     - Give Per (Time Unit)
   * - 15
     - ``rxg_15``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00332
     - Give Rate Amount
   * - 16
     - ``rxg_16``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00333
     - Give Rate Units

.. _hl7-v2_2-RXO:

RXO: PHARMACY PRESCRIPTION ORDER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.2

.. py:class:: hl7types.hl7.v2_2.segments.RXO.RXO
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``rxo_1``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00292
     - Requested Give Code
   * - 2
     - ``rxo_2``
     - 20
     - str
     - R
     -
     - 00293
     - Requested Give Amount - Minimum
   * - 3
     - ``rxo_3``
     - 20
     - str
     - O
     -
     - 00294
     - Requested Give Amount - Maximum
   * - 4
     - ``rxo_4``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00295
     - Requested Give Units
   * - 5
     - ``rxo_5``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     -
     - 00296
     - Requested Dosage Form
   * - 6
     - ``rxo_6``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00297
     - Provider's Pharmacy Instructions
   * - 7
     - ``rxo_7``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00298
     - Provider's Administration Instructions
   * - 8
     - ``rxo_8``
     -
     - str
     - C
     -
     - 00299
     - Deliver-to location
   * - 9
     - ``rxo_9``
     - 1
     - str
     - O
     - 0161
     - 00300
     - Allow Substitutions
   * - 10
     - ``rxo_10``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - C
     -
     - 00301
     - Requested Dispense Code
   * - 11
     - ``rxo_11``
     - 20
     - str
     - C
     -
     - 00302
     - Requested Dispense Amount
   * - 12
     - ``rxo_12``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - C
     -
     - 00303
     - Requested Dispense Units
   * - 13
     - ``rxo_13``
     - 3
     - str
     - O
     -
     - 00304
     - Number of Refills
   * - 14
     - ``rxo_14``
     -
     - str
     - C
     -
     - 00305
     - Ordering Provider's DEA Number
   * - 15
     - ``rxo_15``
     -
     - str
     - C
     -
     - 00306
     - Pharmacist Verifier ID
   * - 16
     - ``rxo_16``
     - 1
     - str
     - O
     -
     - 00307
     - Needs Human Review
   * - 17
     - ``rxo_17``
     - 20
     - str
     - C
     -
     - 00308
     - Requested Give Per (Time Unit)

.. _hl7-v2_2-RXR:

RXR: PHARMACY ROUTE
~~~~~~~~~~~~~~~~~~~

Section 4.8.3

.. py:class:: hl7types.hl7.v2_2.segments.RXR.RXR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``rxr_1``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     - 0162
     - 00309
     - Route
   * - 2
     - ``rxr_2``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     - 0163
     - 00310
     - Site
   * - 3
     - ``rxr_3``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     - 0164
     - 00311
     - Administration Device
   * - 4
     - ``rxr_4``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - O
     - 0165
     - 00312
     - Administration Method

.. _hl7-v2_2-STF:

STF: staff identification segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.1.1

.. py:class:: hl7types.hl7.v2_2.segments.STF.STF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``stf_1``
     -
     - :ref:`CE <hl7-v2_2-CE>`
     - R
     -
     - 00671
     - STF - primary key value
   * - 2
     - ``stf_2``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00672
     - Staff ID Code
   * - 3
     - ``stf_3``
     -
     - :ref:`PN <hl7-v2_2-PN>`
     - O
     -
     - 00673
     - Staff Name
   * - 4
     - ``stf_4``
     - 2
     - list[str]
     - O
     - 0182
     - 00674
     - Staff Type
   * - 5
     - ``stf_5``
     - 1
     - str
     - O
     - 0001
     - 00111
     - Sex
   * - 6
     - ``stf_6``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00110
     - Date of Birth
   * - 7
     - ``stf_7``
     - 1
     - str
     - O
     - 0183
     - 00675
     - Active / inactive
   * - 8
     - ``stf_8``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     - 0184
     - 00676
     - Department
   * - 9
     - ``stf_9``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00677
     - Service
   * - 10
     - ``stf_10``
     - 40
     - list[str]
     - O
     -
     - 00678
     - Phone
   * - 11
     - ``stf_11``
     -
     - list[:ref:`AD <hl7-v2_2-AD>`]
     - O
     -
     - 00679
     - Office / home address
   * - 12
     - ``stf_12``
     -
     - list[str]
     - O
     -
     - 00680
     - Activation Date
   * - 13
     - ``stf_13``
     -
     - list[str]
     - O
     -
     - 00681
     - Inactivation Date
   * - 14
     - ``stf_14``
     -
     - list[:ref:`CE <hl7-v2_2-CE>`]
     - O
     -
     - 00682
     - Backup Person ID
   * - 15
     - ``stf_15``
     - 40
     - list[str]
     - O
     -
     - 00683
     - E-mail Address
   * - 16
     - ``stf_16``
     - 1
     - str
     - O
     - 0185
     - 00684
     - Preferred method of Contact

.. _hl7-v2_2-UB1:

UB1: UB82 DATA
~~~~~~~~~~~~~~

Section 6.4.9

.. py:class:: hl7types.hl7.v2_2.segments.UB1.UB1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``ub1_1``
     - 4
     - str
     - O
     -
     - 00530
     - Set ID - UB82
   * - 2
     - ``ub1_2``
     - 1
     - str
     - O
     - 0136
     - 00492
     - Blood deductible (43)
   * - 3
     - ``ub1_3``
     - 2
     - str
     - O
     -
     - 00532
     - Blood furnished pints of (40)
   * - 4
     - ``ub1_4``
     - 2
     - str
     - O
     -
     - 00533
     - Blood replaced pints (41)
   * - 5
     - ``ub1_5``
     - 2
     - str
     - O
     -
     - 00534
     - Blood not replaced pints (42)
   * - 6
     - ``ub1_6``
     - 2
     - str
     - O
     -
     - 00535
     - Co-insurance days (25)
   * - 7
     - ``ub1_7``
     - 2
     - list[str]
     - O
     - 0043
     - 00536
     - Condition code (35-39)
   * - 8
     - ``ub1_8``
     - 3
     - str
     - O
     -
     - 00537
     - Covered days (23)
   * - 9
     - ``ub1_9``
     - 3
     - str
     - O
     -
     - 00538
     - Non-covered days (24)
   * - 10
     - ``ub1_10``
     -
     - list[str]
     - O
     - 0153
     - 00539
     - Value amount and code (46-49)
   * - 11
     - ``ub1_11``
     - 2
     - str
     - O
     -
     - 00540
     - Number of grace days (90)
   * - 12
     - ``ub1_12``
     - 2
     - str
     - O
     -
     - 00541
     - Special program indicator (44)
   * - 13
     - ``ub1_13``
     - 1
     - str
     - O
     -
     - 00542
     - PSRO / UR approval indicator (87)
   * - 14
     - ``ub1_14``
     - 8
     - str
     - O
     -
     - 00543
     - PSRO / UR approved stay - from (88)
   * - 15
     - ``ub1_15``
     - 8
     - str
     - O
     -
     - 00544
     - PSRO / UR approved stay - to (89)
   * - 16
     - ``ub1_16``
     -
     - list[str]
     - O
     -
     - 00545
     - Occurrence (28-32)
   * - 17
     - ``ub1_17``
     - 2
     - str
     - O
     -
     - 00546
     - Occurrence span (33)
   * - 18
     - ``ub1_18``
     - 8
     - str
     - O
     -
     - 00547
     - Occurrence span start date (33)
   * - 19
     - ``ub1_19``
     - 8
     - str
     - O
     -
     - 00548
     - Occurrence span end date (33)
   * - 20
     - ``ub1_20``
     - 30
     - str
     - O
     -
     - 00549
     - UB-82 locator 2
   * - 21
     - ``ub1_21``
     - 7
     - str
     - O
     -
     - 00550
     - UB-82 locator 9
   * - 22
     - ``ub1_22``
     - 8
     - str
     - O
     -
     - 00551
     - UB-82 locator 27
   * - 23
     - ``ub1_23``
     - 17
     - str
     - O
     -
     - 00552
     - UB-82 locator 45

.. _hl7-v2_2-UB2:

UB2: UB92 DATA
~~~~~~~~~~~~~~

Section 6.4.10

.. py:class:: hl7types.hl7.v2_2.segments.UB2.UB2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``ub2_1``
     - 4
     - str
     - O
     -
     - 00553
     - Set ID - UB92
   * - 2
     - ``ub2_2``
     - 3
     - str
     - O
     -
     - 00554
     - Co-insurance days (9)
   * - 3
     - ``ub2_3``
     - 2
     - list[str]
     - O
     - 0043
     - 00555
     - Condition code (24-30)
   * - 4
     - ``ub2_4``
     - 3
     - str
     - O
     -
     - 00556
     - Covered days (7)
   * - 5
     - ``ub2_5``
     - 4
     - str
     - O
     -
     - 00557
     - Non-covered days (8)
   * - 6
     - ``ub2_6``
     -
     - list[str]
     - O
     -
     - 00558
     - Value amount and code (39-41)
   * - 7
     - ``ub2_7``
     -
     - list[str]
     - O
     -
     - 00559
     - Occurrence code and date (32-35)
   * - 8
     - ``ub2_8``
     -
     - list[str]
     - O
     -
     - 00560
     - Occurrence span code / dates (36)
   * - 9
     - ``ub2_9``
     - 29
     - list[str]
     - O
     -
     - 00561
     - UB92 locator 2 (state)
   * - 10
     - ``ub2_10``
     - 12
     - list[str]
     - O
     -
     - 00562
     - UB92 locator 11 (state)
   * - 11
     - ``ub2_11``
     - 5
     - str
     - O
     -
     - 00563
     - UB92 locator 31 (national)
   * - 12
     - ``ub2_12``
     - 23
     - list[str]
     - O
     -
     - 00564
     - Document control number (37)
   * - 13
     - ``ub2_13``
     - 4
     - list[str]
     - O
     -
     - 00565
     - UB92 locator 49 (national)
   * - 14
     - ``ub2_14``
     - 14
     - list[str]
     - O
     -
     - 00566
     - UB92 locator 56 (state)
   * - 15
     - ``ub2_15``
     - 27
     - str
     - O
     -
     - 00567
     - UB92 locator 57 (national)
   * - 16
     - ``ub2_16``
     - 2
     - list[str]
     - O
     -
     - 00568
     - UB92 Locator 78 (state)

.. _hl7-v2_2-URD:

URD: RESULTS/UPDATE DEFINITION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.10.6

.. py:class:: hl7types.hl7.v2_2.segments.URD.URD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``urd_1``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00045
     - R/U date / time
   * - 2
     - ``urd_2``
     - 1
     - str
     - O
     - 0109
     - 00046
     - Report Priority
   * - 3
     - ``urd_3``
     - 20
     - list[str]
     - R
     -
     - 00047
     - R/U Who Subject Definition
   * - 4
     - ``urd_4``
     - 3
     - list[str]
     - O
     - 0048
     - 00048
     - R/U What Subject Definition
   * - 5
     - ``urd_5``
     - 20
     - list[str]
     - O
     -
     - 00049
     - R/U What Department Code
   * - 6
     - ``urd_6``
     - 20
     - list[str]
     - O
     -
     - 00050
     - R/U display / print locations
   * - 7
     - ``urd_7``
     - 1
     - str
     - O
     - 0108
     - 00051
     - R/U Results Level

.. _hl7-v2_2-URS:

URS: UNSOLICITED SELECTION
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.10.7

.. py:class:: hl7types.hl7.v2_2.segments.URS.URS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - SEQ
     - Field
     - LEN
     - DT
     - OPT
     - TBL#
     - ITEM#
     - ELEMENT NAME
   * - 1
     - ``urs_1``
     - 20
     - list[str]
     - R
     -
     - 00052
     - R/U Where Subject Definition
   * - 2
     - ``urs_2``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00053
     - R/U when data start date / time
   * - 3
     - ``urs_3``
     -
     - :ref:`TS <hl7-v2_2-TS>`
     - O
     -
     - 00054
     - R/U when data end date / time
   * - 4
     - ``urs_4``
     - 20
     - list[str]
     - O
     -
     - 00055
     - R/U What User Qualifier
   * - 5
     - ``urs_5``
     - 20
     - list[str]
     - O
     -
     - 00056
     - R/U Other Results Subject Definition
   * - 6
     - ``urs_6``
     - 12
     - list[str]
     - O
     - 0156
     - 00057
     - R/U which date / time qualifier
   * - 7
     - ``urs_7``
     - 12
     - list[str]
     - O
     - 0157
     - 00058
     - R/U which date / time status qualifier
   * - 8
     - ``urs_8``
     - 12
     - list[str]
     - O
     - 0158
     - 00059
     - R/U date / time selection qualifier
