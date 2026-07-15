v2.1 Segments
=============

.. _hl7-v2_1-ACC:

ACC: ACCIDENT
~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.segments.ACC.ACC
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
     - 19
     - str
     - O
     -
     - 00182
     - ACCIDENT DATE/TIME
   * - 2
     - ``acc_2``
     - 2
     - str
     - O
     - 0050
     - 00184
     - ACCIDENT CODE
   * - 3
     - ``acc_3``
     - 25
     - str
     - O
     -
     - 00185
     - ACCIDENT LOCATION

.. _hl7-v2_1-ADD:

ADD: ADDENDUM
~~~~~~~~~~~~~

Section 2.5.1

.. py:class:: hl7types.hl7.v2_1.segments.ADD.ADD
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
     - 60
     - str
     - O
     -
     - 00641
     - ADDENDUM CONTINUATION POINTER

.. _hl7-v2_1-BHS:

BHS: BATCH HEADER
~~~~~~~~~~~~~~~~~

Section 2.5.2

.. py:class:: hl7types.hl7.v2_1.segments.BHS.BHS
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
     - 00685
     - BATCH FIELD SEPARATOR
   * - 2
     - ``bhs_2``
     - 3
     - str
     - R
     -
     - 00686
     - BATCH ENCODING CHARACTERS
   * - 3
     - ``bhs_3``
     - 15
     - str
     - O
     -
     - 00687
     - BATCH SENDING APPLICATION
   * - 4
     - ``bhs_4``
     - 20
     - str
     - O
     -
     - 00688
     - BATCH SENDING FACILITY
   * - 5
     - ``bhs_5``
     - 15
     - str
     - O
     -
     - 00689
     - BATCH RECEIVING APPLICATION
   * - 6
     - ``bhs_6``
     - 20
     - str
     - O
     -
     - 00690
     - BATCH RECEIVING FACILITY
   * - 7
     - ``bhs_7``
     - 19
     - str
     - O
     -
     - 00655
     - BATCH CREATION DATE/TIME
   * - 8
     - ``bhs_8``
     - 40
     - str
     - O
     -
     - 00691
     - BATCH SECURITY
   * - 9
     - ``bhs_9``
     - 20
     - str
     - O
     -
     - 00656
     - BATCH NAME/ID/TYPE
   * - 10
     - ``bhs_10``
     - 80
     - str
     - O
     -
     - 00657
     - BATCH COMMENT
   * - 11
     - ``bhs_11``
     - 20
     - str
     - O
     -
     - 00658
     - BATCH CONTROL ID
   * - 12
     - ``bhs_12``
     - 20
     - str
     - O
     -
     - 00659
     - REFERENCE BATCH CONTROL ID

.. _hl7-v2_1-BLG:

BLG: BILLING
~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.segments.BLG.BLG
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
     - 15
     - str
     - O
     - 0100
     - 00066
     - WHEN TO CHARGE
   * - 2
     - ``blg_2``
     - 50
     - str
     - O
     - 0122
     - 00729
     - CHARGE TYPE
   * - 3
     - ``blg_3``
     - 100
     - str
     - O
     -
     - 00730
     - ACCOUNT ID

.. _hl7-v2_1-BTS:

BTS: BATCH TRAILER
~~~~~~~~~~~~~~~~~~

Section 2.5.3

.. py:class:: hl7types.hl7.v2_1.segments.BTS.BTS
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
     - 00664
     - BATCH MESSAGE COUNT
   * - 2
     - ``bts_2``
     - 80
     - str
     - O
     -
     - 00665
     - BATCH COMMENT
   * - 3
     - ``bts_3``
     - 100
     - str
     - O
     -
     - 00666
     - BATCH TOTALS

.. _hl7-v2_1-DG1:

DG1: DIAGNOSIS
~~~~~~~~~~~~~~

Section 6.3.2

.. py:class:: hl7types.hl7.v2_1.segments.DG1.DG1
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
     - 00506
     - SET ID - DIAGNOSIS
   * - 2
     - ``dg1_2``
     - 2
     - str
     - R
     - 0053
     - 00394
     - DIAGNOSIS CODING METHOD
   * - 3
     - ``dg1_3``
     - 8
     - str
     - O
     - 0051
     - 00293
     - DIAGNOSIS CODE
   * - 4
     - ``dg1_4``
     - 40
     - str
     - O
     -
     - 00294
     - DIAGNOSIS DESCRIPTION
   * - 5
     - ``dg1_5``
     - 19
     - str
     - O
     -
     - 00295
     - DIAGNOSIS DATE/TIME
   * - 6
     - ``dg1_6``
     - 2
     - str
     - R
     - 0052
     - 00297
     - DIAGNOSIS/DRG TYPE
   * - 7
     - ``dg1_7``
     - 4
     - str
     - O
     - 0118
     - 00298
     - MAJOR DIAGNOSTIC CATEGORY
   * - 8
     - ``dg1_8``
     - 4
     - str
     - O
     - 0055
     - 00299
     - DIAGNOSTIC RELATED GROUP
   * - 9
     - ``dg1_9``
     - 2
     - str
     - O
     -
     - 00373
     - DRG APPROVAL INDICATOR
   * - 10
     - ``dg1_10``
     - 2
     - str
     - O
     - 0056
     - 00374
     - DRG GROUPER REVIEW CODE
   * - 11
     - ``dg1_11``
     - 2
     - str
     - O
     - 0083
     - 00375
     - OUTLIER TYPE
   * - 12
     - ``dg1_12``
     - 3
     - str
     - O
     -
     - 00300
     - OUTLIER DAYS
   * - 13
     - ``dg1_13``
     - 12
     - str
     - O
     -
     - 00376
     - OUTLIER COST
   * - 14
     - ``dg1_14``
     - 4
     - str
     - O
     -
     - 00781
     - GROUPER VERSION AND TYPE

.. _hl7-v2_1-DSC:

DSC: CONTINUATION POINTER
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.3.1

.. py:class:: hl7types.hl7.v2_1.segments.DSC.DSC
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
     - 60
     - str
     - O
     -
     - 00167
     - CONTINUATION POINTER

.. _hl7-v2_1-DSP:

DSP: DISPLAY DATA
~~~~~~~~~~~~~~~~~

Section 5.3.2

.. py:class:: hl7types.hl7.v2_1.segments.DSP.DSP
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
     - 00570
     - SET ID - DISPLAY DATA
   * - 2
     - ``dsp_2``
     - 4
     - str
     - O
     -
     - 00571
     - DISPLAY LEVEL
   * - 3
     - ``dsp_3``
     -
     - str
     - R
     -
     - 00153
     - DATA LINE
   * - 4
     - ``dsp_4``
     - 2
     - str
     - O
     -
     - 00154
     - LOGICAL BREAK POINT
   * - 5
     - ``dsp_5``
     -
     - str
     - O
     -
     - 00599
     - RESULT ID

.. _hl7-v2_1-ERR:

ERR: ERROR
~~~~~~~~~~

Section 2.5.4

.. py:class:: hl7types.hl7.v2_1.segments.ERR.ERR
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
     - 80
     - list[str]
     - R
     - 0060
     - 00080
     - ERROR CODE AND LOCATION

.. _hl7-v2_1-EVN:

EVN: EVENT TYPE
~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_1.segments.EVN.EVN
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
     - 00029
     - EVENT TYPE CODE
   * - 2
     - ``evn_2``
     - 19
     - str
     - R
     -
     - 00030
     - DATE/TIME OF EVENT
   * - 3
     - ``evn_3``
     - 19
     - str
     - O
     -
     - 00032
     - DATE/TIME PLANNED EVENT
   * - 4
     - ``evn_4``
     - 3
     - str
     - O
     - 0062
     - 00369
     - EVENT REASON CODE

.. _hl7-v2_1-FHS:

FHS: FILE HEADER
~~~~~~~~~~~~~~~~

Section 2.5.5

.. py:class:: hl7types.hl7.v2_1.segments.FHS.FHS
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
     - 00692
     - FILE FIELD SEPARATOR
   * - 2
     - ``fhs_2``
     - 4
     - str
     - R
     -
     - 00693
     - FILE ENCODING CHARACTERS
   * - 3
     - ``fhs_3``
     - 15
     - str
     - O
     -
     - 00694
     - FILE SENDING APPLICATION
   * - 4
     - ``fhs_4``
     - 20
     - str
     - O
     -
     - 00695
     - FILE SENDING FACILITY
   * - 5
     - ``fhs_5``
     - 15
     - str
     - O
     -
     - 00696
     - FILE RECEIVING APPLICATION
   * - 6
     - ``fhs_6``
     - 20
     - str
     - O
     -
     - 00697
     - FILE RECEIVING FACILITY
   * - 7
     - ``fhs_7``
     - 19
     - str
     - O
     -
     - 00660
     - DATE/TIME OF FILE CREATION
   * - 8
     - ``fhs_8``
     - 40
     - str
     - O
     -
     - 00698
     - FILE SECURITY
   * - 9
     - ``fhs_9``
     - 20
     - str
     - O
     -
     - 00661
     - FILE NAME/ID
   * - 10
     - ``fhs_10``
     - 80
     - str
     - O
     -
     - 00662
     - FILE HEADER COMMENT
   * - 11
     - ``fhs_11``
     - 20
     - str
     - O
     -
     - 00663
     - FILE CONTROL ID
   * - 12
     - ``fhs_12``
     - 20
     - str
     - O
     -
     - 00768
     - REFERENCE FILE CONTROL ID

.. _hl7-v2_1-FT1:

FT1: FINANCIAL TRANSACTION
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.3.3

.. py:class:: hl7types.hl7.v2_1.segments.FT1.FT1
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
     - 00507
     - SET ID - FINANCIAL TRANSACTION
   * - 2
     - ``ft1_2``
     - 12
     - str
     - O
     -
     - 00366
     - TRANSACTION ID
   * - 3
     - ``ft1_3``
     - 5
     - str
     - O
     -
     - 00503
     - TRANSACTION BATCH ID
   * - 4
     - ``ft1_4``
     - 8
     - str
     - R
     -
     - 00351
     - TRANSACTION DATE
   * - 5
     - ``ft1_5``
     - 8
     - str
     - O
     -
     - 00352
     - TRANSACTION POSTING DATE
   * - 6
     - ``ft1_6``
     - 8
     - str
     - R
     - 0017
     - 00353
     - TRANSACTION TYPE
   * - 7
     - ``ft1_7``
     - 20
     - str
     - R
     - 0096
     - 00354
     - TRANSACTION CODE
   * - 8
     - ``ft1_8``
     - 40
     - str
     - O
     -
     - 00356
     - TRANSACTION DESCRIPTION
   * - 9
     - ``ft1_9``
     - 40
     - str
     - O
     -
     - 00706
     - TRANSACTION DESCRIPTION - ALT
   * - 10
     - ``ft1_10``
     - 12
     - str
     - O
     -
     - 00358
     - TRANSACTION AMOUNT - EXTENDED
   * - 11
     - ``ft1_11``
     - 4
     - str
     - O
     -
     - 00357
     - TRANSACTION QUANTITY
   * - 12
     - ``ft1_12``
     - 12
     - str
     - O
     -
     - 00782
     - TRANSACTION AMOUNT - UNIT
   * - 13
     - ``ft1_13``
     - 16
     - str
     - O
     - 0049
     - 00355
     - DEPARTMENT CODE
   * - 14
     - ``ft1_14``
     - 8
     - str
     - O
     - 0072
     - 00359
     - INSURANCE PLAN ID
   * - 15
     - ``ft1_15``
     - 12
     - str
     - O
     -
     - 00360
     - INSURANCE AMOUNT
   * - 16
     - ``ft1_16``
     - 12
     - str
     - O
     - 0079
     - 00361
     - PATIENT LOCATION
   * - 17
     - ``ft1_17``
     - 1
     - str
     - O
     - 0024
     - 00362
     - FEE SCHEDULE
   * - 18
     - ``ft1_18``
     - 2
     - str
     - O
     - 0018
     - 00363
     - PATIENT TYPE
   * - 19
     - ``ft1_19``
     - 8
     - str
     - O
     - 0051
     - 00364
     - DIAGNOSIS CODE
   * - 20
     - ``ft1_20``
     - 60
     - str
     - O
     - 0084
     - 00377
     - PERFORMED BY CODE
   * - 21
     - ``ft1_21``
     - 60
     - str
     - O
     -
     - 00783
     - ORDERED BY CODE
   * - 22
     - ``ft1_22``
     - 12
     - str
     - O
     -
     - 00784
     - UNIT COST

.. _hl7-v2_1-FTS:

FTS: FILE TRAILER
~~~~~~~~~~~~~~~~~

Section 2.5.6

.. py:class:: hl7types.hl7.v2_1.segments.FTS.FTS
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
     - 00667
     - FILE BATCH COUNT
   * - 2
     - ``fts_2``
     - 80
     - str
     - O
     -
     - 00668
     - FILE TRAILER COMMENT

.. _hl7-v2_1-GT1:

GT1: GUARANTOR
~~~~~~~~~~~~~~

Section 6.3.4

.. py:class:: hl7types.hl7.v2_1.segments.GT1.GT1
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
     - 00321
     - SET ID - GUARANTOR
   * - 2
     - ``gt1_2``
     - 20
     - str
     - O
     -
     - 00322
     - GUARANTOR NUMBER
   * - 3
     - ``gt1_3``
     - 48
     - str
     - R
     -
     - 00323
     - GUARANTOR NAME
   * - 4
     - ``gt1_4``
     - 48
     - str
     - O
     -
     - 00707
     - GUARANTOR SPOUSE NAME
   * - 5
     - ``gt1_5``
     - 106
     - str
     - O
     -
     - 00324
     - GUARANTOR ADDRESS
   * - 6
     - ``gt1_6``
     - 40
     - str
     - O
     -
     - 00329
     - GUARANTOR PH. NUM.- HOME
   * - 7
     - ``gt1_7``
     - 40
     - str
     - O
     -
     - 00330
     - GUARANTOR PH. NUM-BUSINESS
   * - 8
     - ``gt1_8``
     - 8
     - str
     - O
     -
     - 00331
     - GUARANTOR DATE OF BIRTH
   * - 9
     - ``gt1_9``
     - 1
     - str
     - O
     - 0001
     - 00332
     - GUARANTOR SEX
   * - 10
     - ``gt1_10``
     - 2
     - str
     - O
     - 0068
     - 00333
     - GUARANTOR TYPE
   * - 11
     - ``gt1_11``
     - 2
     - str
     - O
     - 0063
     - 00334
     - GUARANTOR RELATIONSHIP
   * - 12
     - ``gt1_12``
     - 11
     - str
     - O
     -
     - 00335
     - GUARANTOR SSN
   * - 13
     - ``gt1_13``
     - 8
     - str
     - O
     -
     - 00338
     - GUARANTOR DATE - BEGIN
   * - 14
     - ``gt1_14``
     - 8
     - str
     - O
     -
     - 00339
     - GUARANTOR DATE - END
   * - 15
     - ``gt1_15``
     - 2
     - str
     - O
     -
     - 00340
     - GUARANTOR PRIORITY
   * - 16
     - ``gt1_16``
     - 45
     - str
     - O
     -
     - 00341
     - GUARANTOR EMPLOYER NAME
   * - 17
     - ``gt1_17``
     - 106
     - str
     - O
     -
     - 00342
     - GUARANTOR EMPLOYER ADDRESS
   * - 18
     - ``gt1_18``
     - 40
     - str
     - O
     -
     - 00347
     - GUARANTOR EMPLOY PHONE #
   * - 19
     - ``gt1_19``
     - 20
     - str
     - O
     -
     - 00391
     - GUARANTOR EMPLOYEE ID NUM
   * - 20
     - ``gt1_20``
     - 2
     - str
     - O
     - 0066
     - 00392
     - GUARANTOR EMPLOYMENT STATUS

.. _hl7-v2_1-IN1:

IN1: INSURANCE
~~~~~~~~~~~~~~

Section 6.3.5

.. py:class:: hl7types.hl7.v2_1.segments.IN1.IN1
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
     - 00234
     - SET ID - INSURANCE
   * - 2
     - ``in1_2``
     - 8
     - str
     - R
     - 0072
     - 00378
     - INSURANCE PLAN ID
   * - 3
     - ``in1_3``
     - 6
     - str
     - R
     -
     - 00235
     - INSURANCE COMPANY ID
   * - 4
     - ``in1_4``
     - 45
     - str
     - O
     -
     - 00236
     - INSURANCE COMPANY NAME
   * - 5
     - ``in1_5``
     - 106
     - str
     - O
     -
     - 00237
     - INSURANCE COMPANY ADDRESS
   * - 6
     - ``in1_6``
     - 48
     - str
     - O
     -
     - 00242
     - INSURANCE CO. CONTACT PERS
   * - 7
     - ``in1_7``
     - 40
     - str
     - O
     -
     - 00243
     - INSURANCE CO PHONE NUMBER
   * - 8
     - ``in1_8``
     - 12
     - str
     - O
     -
     - 00248
     - GROUP NUMBER
   * - 9
     - ``in1_9``
     - 35
     - str
     - O
     -
     - 00249
     - GROUP NAME
   * - 10
     - ``in1_10``
     - 12
     - str
     - O
     -
     - 00250
     - INSURED'S GROUP EMP. ID
   * - 11
     - ``in1_11``
     - 45
     - str
     - O
     -
     - 00251
     - INSURED'S GROUP EMP. NAME
   * - 12
     - ``in1_12``
     - 8
     - str
     - O
     -
     - 00252
     - PLAN EFFECTIVE DATE
   * - 13
     - ``in1_13``
     - 8
     - str
     - O
     -
     - 00253
     - PLAN EXPIRATION DATE
   * - 14
     - ``in1_14``
     - 55
     - str
     - O
     -
     - 00254
     - AUTHORIZATION INFORMATION
   * - 15
     - ``in1_15``
     - 2
     - str
     - O
     - 0086
     - 00260
     - PLAN TYPE
   * - 16
     - ``in1_16``
     - 48
     - str
     - O
     -
     - 00261
     - NAME OF INSURED
   * - 17
     - ``in1_17``
     - 2
     - str
     - O
     - 0063
     - 00262
     - INSURED'S RELATIONSHIP TO PATIENT
   * - 18
     - ``in1_18``
     - 8
     - str
     - O
     -
     - 00708
     - INSURED'S DATE OF BIRTH
   * - 19
     - ``in1_19``
     - 106
     - str
     - O
     -
     - 00709
     - INSURED'S ADDRESS
   * - 20
     - ``in1_20``
     - 2
     - str
     - O
     -
     - 00263
     - ASSIGNMENT OF BENEFITS
   * - 21
     - ``in1_21``
     - 2
     - str
     - O
     -
     - 00264
     - COORDINATION OF BENEFITS
   * - 22
     - ``in1_22``
     - 2
     - str
     - O
     -
     - 00265
     - COORD OF BEN. PRIORITY
   * - 23
     - ``in1_23``
     - 2
     - str
     - O
     - 0081
     - 00266
     - NOTICE OF ADMISSION CODE
   * - 24
     - ``in1_24``
     - 8
     - str
     - O
     -
     - 00267
     - NOTICE OF ADMISSION DATE
   * - 25
     - ``in1_25``
     - 2
     - str
     - O
     - 0094
     - 00268
     - RPT OF ELIGIBILITY CODE
   * - 26
     - ``in1_26``
     - 8
     - str
     - O
     -
     - 00269
     - RPT OF ELIGIBILITY DATE
   * - 27
     - ``in1_27``
     - 2
     - str
     - O
     - 0093
     - 00270
     - RELEASE INFORMATION CODE
   * - 28
     - ``in1_28``
     - 15
     - str
     - O
     -
     - 00271
     - PRE-ADMIT CERT. (PAC)
   * - 29
     - ``in1_29``
     - 8
     - str
     - O
     -
     - 00272
     - VERIFICATION DATE
   * - 30
     - ``in1_30``
     - 60
     - str
     - O
     -
     - 00273
     - VERIFICATION BY
   * - 31
     - ``in1_31``
     - 2
     - str
     - O
     - 0098
     - 00277
     - TYPE OF AGREEMENT CODE
   * - 32
     - ``in1_32``
     - 2
     - str
     - O
     - 0022
     - 00278
     - BILLING STATUS
   * - 33
     - ``in1_33``
     - 4
     - str
     - O
     -
     - 00280
     - LIFETIME RESERVE DAYS
   * - 34
     - ``in1_34``
     - 4
     - str
     - O
     -
     - 00281
     - DELAY BEFORE L. R. DAY
   * - 35
     - ``in1_35``
     - 8
     - str
     - O
     - 0042
     - 00282
     - COMPANY PLAN CODE
   * - 36
     - ``in1_36``
     - 15
     - str
     - O
     -
     - 00283
     - POLICY NUMBER
   * - 37
     - ``in1_37``
     - 12
     - str
     - O
     -
     - 00284
     - POLICY DEDUCTIBLE
   * - 38
     - ``in1_38``
     - 12
     - str
     - O
     -
     - 00285
     - POLICY LIMIT - AMOUNT
   * - 39
     - ``in1_39``
     - 4
     - str
     - O
     -
     - 00286
     - POLICY LIMIT - DAYS
   * - 40
     - ``in1_40``
     - 12
     - str
     - O
     -
     - 00287
     - ROOM RATE - SEMI-PRIVATE
   * - 41
     - ``in1_41``
     - 12
     - str
     - O
     -
     - 00288
     - ROOM RATE - PRIVATE
   * - 42
     - ``in1_42``
     - 1
     - str
     - O
     - 0066
     - 00710
     - INSURED'S EMPLOYMENT STATUS
   * - 43
     - ``in1_43``
     - 1
     - str
     - O
     - 0001
     - 00711
     - INSURED'S SEX
   * - 44
     - ``in1_44``
     - 106
     - str
     - O
     -
     - 00713
     - INSURED'S EMPLOYER ADDRESS

.. _hl7-v2_1-MRG:

MRG: MERGE PATIENT INFORMATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.segments.MRG.MRG
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
     - 16
     - str
     - R
     - 0061
     - 00576
     - PRIOR PATIENT ID - INTERNAL
   * - 2
     - ``mrg_2``
     - 16
     - str
     - O
     - 0061
     - 00577
     - PRIOR ALTERNATE PATIENT ID
   * - 3
     - ``mrg_3``
     - 20
     - str
     - O
     - 0061
     - 00578
     - PRIOR PATIENT ACCOUNT NUMBER

.. _hl7-v2_1-MSA:

MSA: MESSAGE ACKNOWLEDGMENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.5.7

.. py:class:: hl7types.hl7.v2_1.segments.MSA.MSA
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
     - 00002
     - ACKNOWLEDGMENT CODE
   * - 2
     - ``msa_2``
     - 20
     - str
     - R
     -
     - 00003
     - MESSAGE CONTROL ID
   * - 3
     - ``msa_3``
     - 80
     - str
     - O
     -
     - 00004
     - TEXT MESSAGE
   * - 4
     - ``msa_4``
     - 15
     - str
     - O
     -
     - 00598
     - EXPECTED SEQUENCE NUMBER
   * - 5
     - ``msa_5``
     - 1
     - str
     - O
     - 0102
     - 00632
     - DELAYED ACKNOWLEDGMENT TYPE

.. _hl7-v2_1-MSH:

MSH: MESSAGE HEADER
~~~~~~~~~~~~~~~~~~~

Section 2.5.8

.. py:class:: hl7types.hl7.v2_1.segments.MSH.MSH
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
     - 00005
     - FIELD SEPARATOR
   * - 2
     - ``msh_2``
     - 4
     - str
     - R
     -
     - 00509
     - ENCODING CHARACTERS
   * - 3
     - ``msh_3``
     - 15
     - str
     - O
     -
     - 00006
     - SENDING APPLICATION
   * - 4
     - ``msh_4``
     - 20
     - str
     - O
     -
     - 00512
     - SENDING FACILITY
   * - 5
     - ``msh_5``
     - 15
     - str
     - O
     -
     - 00009
     - RECEIVING APPLICATION
   * - 6
     - ``msh_6``
     - 30
     - str
     - O
     -
     - 00513
     - RECEIVING FACILITY
   * - 7
     - ``msh_7``
     - 19
     - str
     - O
     -
     - 00010
     - DATE/TIME OF MESSAGE
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
     - 7
     - str
     - R
     - 0076
     - 00012
     - MESSAGE TYPE
   * - 10
     - ``msh_10``
     - 20
     - str
     - R
     -
     - 00013
     - MESSAGE CONTROL ID
   * - 11
     - ``msh_11``
     - 1
     - str
     - R
     - 0103
     - 00014
     - PROCESSING ID
   * - 12
     - ``msh_12``
     - 8
     - str
     - R
     - 0104
     - 00015
     - VERSION ID
   * - 13
     - ``msh_13``
     - 15
     - str
     - O
     -
     - 00633
     - SEQUENCE NUMBER
   * - 14
     - ``msh_14``
     - 180
     - str
     - O
     -
     - 00699
     - CONTINUATION POINTER

.. _hl7-v2_1-NCK:

NCK: SYSTEM CLOCK
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.segments.NCK.NCK
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
     - 19
     - str
     - R
     -
     - 00742
     - SYSTEM DATE/TIME

.. _hl7-v2_1-NK1:

NK1: NEXT OF KIN
~~~~~~~~~~~~~~~~

Section 6.3.6

.. py:class:: hl7types.hl7.v2_1.segments.NK1.NK1
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
     - 00712
     - SET ID - NEXT OF KIN
   * - 2
     - ``nk1_2``
     - 48
     - str
     - O
     -
     - 00048
     - NEXT OF KIN NAME
   * - 3
     - ``nk1_3``
     - 15
     - str
     - O
     - 0063
     - 00047
     - NEXT OF KIN RELATIONSHIP
   * - 4
     - ``nk1_4``
     - 106
     - str
     - O
     -
     - 00225
     - NEXT OF KIN - ADDRESS
   * - 5
     - ``nk1_5``
     - 40
     - list[str]
     - O
     -
     - 00230
     - NEXT OF KIN - PHONE NUMBER

.. _hl7-v2_1-NPU:

NPU: NON-PATIENT UPDATE
~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.5

.. py:class:: hl7types.hl7.v2_1.segments.NPU.NPU
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
     - 12
     - str
     - R
     - 0079
     - 00785
     - BED LOCATION
   * - 2
     - ``npu_2``
     - 1
     - str
     - O
     - 0116
     - 00671
     - BED STATUS

.. _hl7-v2_1-NSC:

NSC: STATUS CHANGE
~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.segments.NSC.NSC
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
     - NETWORK CHANGE TYPE
   * - 2
     - ``nsc_2``
     - 30
     - str
     - O
     -
     - 00759
     - CURRENT CPU
   * - 3
     - ``nsc_3``
     - 30
     - str
     - O
     -
     - 00760
     - CURRENT FILESERVER
   * - 4
     - ``nsc_4``
     - 30
     - str
     - O
     -
     - 00761
     - CURRENT APPLICATION
   * - 5
     - ``nsc_5``
     - 30
     - str
     - O
     -
     - 00762
     - CURRENT FACILITY
   * - 6
     - ``nsc_6``
     - 30
     - str
     - O
     -
     - 00763
     - NEW CPU
   * - 7
     - ``nsc_7``
     - 30
     - str
     - O
     -
     - 00764
     - NEW FILESERVER
   * - 8
     - ``nsc_8``
     - 30
     - str
     - O
     -
     - 00765
     - NEW APPLICATION
   * - 9
     - ``nsc_9``
     - 30
     - str
     - O
     -
     - 00766
     - NEW FACILITY

.. _hl7-v2_1-NST:

NST: STATISTICS
~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.segments.NST.NST
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
     -
     - 00743
     - STATISTICS AVAILABLE
   * - 2
     - ``nst_2``
     - 30
     - str
     - O
     -
     - 00744
     - SOURCE IDENTIFIER
   * - 3
     - ``nst_3``
     - 3
     - str
     - O
     -
     - 00745
     - SOURCE TYPE
   * - 4
     - ``nst_4``
     - 19
     - str
     - O
     -
     - 00746
     - STATISTICS START
   * - 5
     - ``nst_5``
     - 19
     - str
     - O
     -
     - 00747
     - STATISTICS END
   * - 6
     - ``nst_6``
     - 10
     - str
     - O
     -
     - 00748
     - RECEIVE CHARACTER COUNT
   * - 7
     - ``nst_7``
     - 10
     - str
     - O
     -
     - 00749
     - SEND CHARACTER COUNT
   * - 8
     - ``nst_8``
     - 10
     - str
     - O
     -
     - 00750
     - MESSAGES RECEIVED
   * - 9
     - ``nst_9``
     - 10
     - str
     - O
     -
     - 00751
     - MESSAGES SENT
   * - 10
     - ``nst_10``
     - 10
     - str
     - O
     -
     - 00752
     - CHECKSUM ERRORS RECEIVED
   * - 11
     - ``nst_11``
     - 10
     - str
     - O
     -
     - 00753
     - LENGTH ERRORS RECEIVED
   * - 12
     - ``nst_12``
     - 10
     - str
     - O
     -
     - 00754
     - OTHER ERRORS RECEIVED
   * - 13
     - ``nst_13``
     - 10
     - str
     - O
     -
     - 00755
     - CONNECT TIMEOUTS
   * - 14
     - ``nst_14``
     - 10
     - str
     - O
     -
     - 00756
     - RECEIVE TIMEOUTS
   * - 15
     - ``nst_15``
     - 10
     - str
     - O
     -
     - 00757
     - NETWORK ERRORS

.. _hl7-v2_1-NTE:

NTE: NOTES AND COMMENTS
~~~~~~~~~~~~~~~~~~~~~~~

Section 2.5.9

.. py:class:: hl7types.hl7.v2_1.segments.NTE.NTE
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
     - 00573
     - SET ID - NOTES AND COMMENTS
   * - 2
     - ``nte_2``
     - 8
     - str
     - O
     - 0105
     - 00574
     - SOURCE OF COMMENT
   * - 3
     - ``nte_3``
     -
     - list[str]
     - R
     -
     - 00575
     - COMMENT

.. _hl7-v2_1-OBR:

OBR: OBSERVATION REQUEST
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.segments.OBR.OBR
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
     - 00520
     - SET ID - OBSERVATION REQUEST
   * - 2
     - ``obr_2``
     - 75
     - str
     - O
     -
     - 00732
     - PLACER ORDER #
   * - 3
     - ``obr_3``
     - 75
     - str
     - O
     -
     - 00733
     - FILLER ORDER #
   * - 4
     - ``obr_4``
     -
     - :ref:`CE <hl7-v2_1-CE>`
     - R
     -
     - 00523
     - UNIVERSAL SERVICE IDENT.
   * - 5
     - ``obr_5``
     - 2
     - str
     - O
     -
     - 00524
     - PRIORITY
   * - 6
     - ``obr_6``
     - 19
     - str
     - O
     -
     - 00529
     - REQUESTED DATE-TIME
   * - 7
     - ``obr_7``
     - 19
     - str
     - R
     -
     - 00530
     - OBSERVATION DATE/TIME
   * - 8
     - ``obr_8``
     - 19
     - str
     - R
     -
     - 00531
     - OBSERVATION END DATE/TIME
   * - 9
     - ``obr_9``
     - 20
     - str
     - R
     - 0036
     - 00532
     - COLLECTION VOLUME
   * - 10
     - ``obr_10``
     - 60
     - list[str]
     - O
     -
     - 00533
     - COLLECTOR IDENTIFIER
   * - 11
     - ``obr_11``
     - 1
     - str
     - O
     - 0065
     - 00534
     - SPECIMEN ACTION CODE
   * - 12
     - ``obr_12``
     - 60
     - str
     - O
     - 0047
     - 00535
     - DANGER CODE
   * - 13
     - ``obr_13``
     - 300
     - str
     - O
     -
     - 00536
     - RELEVANT CLINICAL INFO.
   * - 14
     - ``obr_14``
     - 19
     - str
     - R
     -
     - 00537
     - SPECIMEN RECEIVED DATE/TIME
   * - 15
     - ``obr_15``
     - 300
     - str
     - O
     - 0070
     - 00538
     - SPECIMEN SOURCE
   * - 16
     - ``obr_16``
     - 60
     - list[str]
     - O
     - 0010
     - 00539
     - ORDERING PROVIDER
   * - 17
     - ``obr_17``
     - 40
     - list[str]
     - O
     -
     - 00540
     - ORDER CALL-BACK PHONE NUM
   * - 18
     - ``obr_18``
     - 60
     - str
     - O
     -
     - 00541
     - PLACERS FIELD #1
   * - 19
     - ``obr_19``
     - 60
     - str
     - O
     -
     - 00542
     - PLACERS FIELD #2
   * - 20
     - ``obr_20``
     - 60
     - str
     - O
     -
     - 00543
     - FILLERS FIELD #1
   * - 21
     - ``obr_21``
     - 60
     - str
     - O
     -
     - 00544
     - FILLERS FIELD #2
   * - 22
     - ``obr_22``
     - 19
     - str
     - R
     -
     - 00546
     - RESULTS RPT/STATUS CHNG - DATE/T
   * - 23
     - ``obr_23``
     - 40
     - str
     - O
     -
     - 00547
     - CHARGE TO PRACTICE
   * - 24
     - ``obr_24``
     - 10
     - str
     - O
     - 0074
     - 00548
     - DIAGNOSTIC SERV SECT ID
   * - 25
     - ``obr_25``
     - 1
     - str
     - O
     - 0123
     - 00734
     - RESULT STATUS
   * - 26
     - ``obr_26``
     -
     - :ref:`CE <hl7-v2_1-CE>`
     - O
     -
     - 00550
     - LINKED RESULTS
   * - 27
     - ``obr_27``
     - 200
     - list[str]
     - O
     -
     - 00735
     - QUANTITY/TIMING
   * - 28
     - ``obr_28``
     - 80
     - list[str]
     - O
     -
     - 00551
     - RESULT COPIES TO
   * - 29
     - ``obr_29``
     - 150
     - str
     - O
     -
     - 00737
     - PARENT ACCESSION #
   * - 30
     - ``obr_30``
     - 20
     - str
     - O
     - 0124
     - 00625
     - TRANSPORTATION MODE
   * - 31
     - ``obr_31``
     -
     - list[:ref:`CE <hl7-v2_1-CE>`]
     - O
     -
     - 00626
     - REASON FOR STUDY
   * - 32
     - ``obr_32``
     - 60
     - str
     - O
     -
     - 00627
     - PRINCIPAL RESULT INTERPRETER
   * - 33
     - ``obr_33``
     - 60
     - str
     - O
     -
     - 00628
     - ASSISTANT RESULT INTERPRETER
   * - 34
     - ``obr_34``
     - 60
     - str
     - O
     -
     - 00630
     - TECHNICIAN
   * - 35
     - ``obr_35``
     - 60
     - str
     - O
     -
     - 00629
     - TRANSCRIPTIONIST
   * - 36
     - ``obr_36``
     - 19
     - str
     - O
     -
     - 00736
     - SCHEDULED - DATE/TIME

.. _hl7-v2_1-OBX:

OBX: RESULT
~~~~~~~~~~~

Section 7.3.1

.. py:class:: hl7types.hl7.v2_1.segments.OBX.OBX
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
     - 00559
     - SET ID - OBSERVATION SIMPLE
   * - 2
     - ``obx_2``
     - 2
     - str
     - O
     - 0125
     - 00676
     - VALUE TYPE
   * - 3
     - ``obx_3``
     -
     - :ref:`CE <hl7-v2_1-CE>`
     - R
     -
     - 00560
     - OBSERVATION IDENTIFIER
   * - 4
     - ``obx_4``
     - 20
     - str
     - O
     -
     - 00769
     - OBSERVATION SUB-ID
   * - 5
     - ``obx_5``
     - 65
     - str
     - R
     -
     - 00561
     - OBSERVATION RESULTS
   * - 6
     - ``obx_6``
     - 20
     - str
     - O
     -
     - 00562
     - UNITS
   * - 7
     - ``obx_7``
     - 60
     - str
     - O
     -
     - 00563
     - REFERENCES RANGE
   * - 8
     - ``obx_8``
     - 10
     - list[str]
     - O
     - 0078
     - 00564
     - ABNORMAL FLAGS
   * - 9
     - ``obx_9``
     - 5
     - str
     - O
     -
     - 00639
     - PROBABILITY
   * - 10
     - ``obx_10``
     - 5
     - str
     - O
     - 0080
     - 00565
     - NATURE OF ABNORMAL TEST
   * - 11
     - ``obx_11``
     - 2
     - str
     - O
     - 0085
     - 00566
     - OBSERV RESULT STATUS
   * - 12
     - ``obx_12``
     - 19
     - str
     - O
     -
     - 00567
     - DATE LAST OBS NORMAL VALUES

.. _hl7-v2_1-ORC:

ORC: COMMON ORDER
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.segments.ORC.ORC
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
     - 00714
     - ORDER CONTROL
   * - 2
     - ``orc_2``
     - 75
     - str
     - O
     -
     - 00715
     - PLACER ORDER #
   * - 3
     - ``orc_3``
     - 75
     - str
     - O
     -
     - 00716
     - FILLER ORDER #
   * - 4
     - ``orc_4``
     - 75
     - str
     - O
     -
     - 00717
     - PLACER GROUP #
   * - 5
     - ``orc_5``
     - 2
     - str
     - O
     - 0038
     - 00718
     - ORDER STATUS
   * - 6
     - ``orc_6``
     - 1
     - str
     - O
     - 0121
     - 00719
     - RESPONSE FLAG
   * - 7
     - ``orc_7``
     - 200
     - str
     - O
     -
     - 00720
     - TIMING/QUANTITY
   * - 8
     - ``orc_8``
     - 200
     - str
     - O
     -
     - 00721
     - PARENT
   * - 9
     - ``orc_9``
     - 19
     - str
     - O
     -
     - 00722
     - DATE/TIME OF TRANSACTION
   * - 10
     - ``orc_10``
     - 80
     - str
     - O
     -
     - 00723
     - ENTERED BY
   * - 11
     - ``orc_11``
     - 80
     - str
     - O
     -
     - 00724
     - VERIFIED BY
   * - 12
     - ``orc_12``
     - 80
     - str
     - O
     -
     - 00725
     - ORDERING PROVIDER
   * - 13
     - ``orc_13``
     - 80
     - str
     - O
     -
     - 00726
     - ENTERER'S LOCATION
   * - 14
     - ``orc_14``
     - 40
     - list[str]
     - O
     -
     - 00727
     - CALL BACK PHONE NUMBER

.. _hl7-v2_1-ORO:

ORO: ORDER OTHER
~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.segments.ORO.ORO
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
     - ``oro_1``
     -
     - :ref:`CE <hl7-v2_1-CE>`
     - O
     -
     - 00731
     - ORDER ITEM ID
   * - 2
     - ``oro_2``
     - 1
     - str
     - O
     -
     - 00120
     - SUBSTITUTE ALLOWED
   * - 3
     - ``oro_3``
     - 80
     - list[str]
     - O
     -
     - 00586
     - RESULTS COPIES TO
   * - 4
     - ``oro_4``
     - 2
     - str
     - O
     - 0012
     - 00068
     - STOCK LOCATION

.. _hl7-v2_1-PID:

PID: PATIENT IDENTIFICATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.3

.. py:class:: hl7types.hl7.v2_1.segments.PID.PID
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
     - 00572
     - SET ID - PATIENT ID
   * - 2
     - ``pid_2``
     - 16
     - str
     - O
     - 0061
     - 00581
     - PATIENT ID EXTERNAL (EXTERNAL ID)
   * - 3
     - ``pid_3``
     - 16
     - str
     - R
     - 0061
     - 00034
     - PATIENT ID INTERNAL (INTERNAL ID)
   * - 4
     - ``pid_4``
     - 12
     - str
     - O
     -
     - 00038
     - ALTERNATE PATIENT ID
   * - 5
     - ``pid_5``
     - 48
     - str
     - R
     -
     - 00041
     - PATIENT NAME
   * - 6
     - ``pid_6``
     - 30
     - str
     - O
     -
     - 00582
     - MOTHER'S MAIDEN NAME
   * - 7
     - ``pid_7``
     - 8
     - str
     - O
     -
     - 00043
     - DATE OF BIRTH
   * - 8
     - ``pid_8``
     - 1
     - str
     - O
     - 0001
     - 00042
     - SEX
   * - 9
     - ``pid_9``
     - 48
     - list[str]
     - O
     -
     - 00597
     - PATIENT ALIAS
   * - 10
     - ``pid_10``
     - 1
     - str
     - O
     - 0005
     - 00044
     - ETHNIC GROUP
   * - 11
     - ``pid_11``
     - 106
     - str
     - O
     -
     - 00020
     - PATIENT ADDRESS
   * - 12
     - ``pid_12``
     - 4
     - str
     - O
     -
     - 00026
     - COUNTY CODE
   * - 13
     - ``pid_13``
     - 40
     - list[str]
     - O
     -
     - 00049
     - PHONE NUMBER - HOME
   * - 14
     - ``pid_14``
     - 40
     - list[str]
     - O
     -
     - 00050
     - PHONE NUMBER - BUSINESS
   * - 15
     - ``pid_15``
     - 25
     - str
     - O
     -
     - 00464
     - LANGUAGE - PATIENT
   * - 16
     - ``pid_16``
     - 1
     - str
     - O
     - 0002
     - 00046
     - MARITAL STATUS
   * - 17
     - ``pid_17``
     - 3
     - str
     - O
     - 0006
     - 00045
     - RELIGION
   * - 18
     - ``pid_18``
     - 20
     - str
     - O
     - 0061
     - 00035
     - PATIENT ACCOUNT NUMBER
   * - 19
     - ``pid_19``
     - 16
     - str
     - O
     -
     - 00457
     - SSN NUMBER - PATIENT
   * - 20
     - ``pid_20``
     - 25
     - str
     - O
     -
     - 00453
     - DRIVER'S LIC NUM - PATIENT

.. _hl7-v2_1-PR1:

PR1: PROCEDURES
~~~~~~~~~~~~~~~

Section 6.3.7

.. py:class:: hl7types.hl7.v2_1.segments.PR1.PR1
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
     - list[str]
     - R
     -
     - 00304
     - SET ID - PROCEDURE
   * - 2
     - ``pr1_2``
     - 2
     - str
     - R
     - 0089
     - 00393
     - PROCEDURE CODING METHOD.
   * - 3
     - ``pr1_3``
     - 10
     - str
     - R
     - 0088
     - 00305
     - PROCEDURE CODE
   * - 4
     - ``pr1_4``
     - 40
     - str
     - O
     -
     - 00306
     - PROCEDURE DESCRIPTION
   * - 5
     - ``pr1_5``
     - 19
     - str
     - R
     -
     - 00307
     - PROCEDURE DATE/TIME
   * - 6
     - ``pr1_6``
     - 2
     - str
     - R
     - 0090
     - 00309
     - PROCEDURE TYPE
   * - 7
     - ``pr1_7``
     - 4
     - str
     - O
     -
     - 00310
     - PROCEDURE MINUTES
   * - 8
     - ``pr1_8``
     - 60
     - str
     - O
     - 0010
     - 00311
     - ANESTHESIOLOGIST
   * - 9
     - ``pr1_9``
     - 2
     - str
     - O
     - 0019
     - 00313
     - ANESTHESIA CODE
   * - 10
     - ``pr1_10``
     - 4
     - str
     - O
     -
     - 00314
     - ANESTHESIA MINUTES
   * - 11
     - ``pr1_11``
     - 60
     - str
     - O
     - 0010
     - 00315
     - SURGEON
   * - 12
     - ``pr1_12``
     - 60
     - str
     - O
     - 0010
     - 00318
     - RESIDENT CODE
   * - 13
     - ``pr1_13``
     - 2
     - str
     - O
     - 0059
     - 00317
     - CONSENT CODE

.. _hl7-v2_1-PV1:

PV1: PATIENT VISIT
~~~~~~~~~~~~~~~~~~

Section 3.3.4

.. py:class:: hl7types.hl7.v2_1.segments.PV1.PV1
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
     - 00458
     - SET ID - PATIENT VISIT
   * - 2
     - ``pv1_2``
     - 1
     - str
     - R
     - 0004
     - 00052
     - PATIENT CLASS
   * - 3
     - ``pv1_3``
     - 12
     - str
     - R
     - 0079
     - 00053
     - ASSIGNED PATIENT LOCATION
   * - 4
     - ``pv1_4``
     - 2
     - str
     - O
     - 0007
     - 00218
     - ADMISSION TYPE
   * - 5
     - ``pv1_5``
     - 20
     - str
     - O
     -
     - 00219
     - PRE-ADMIT NUMBER
   * - 6
     - ``pv1_6``
     - 12
     - str
     - O
     - 0079
     - 00056
     - PRIOR PATIENT LOCATION
   * - 7
     - ``pv1_7``
     - 60
     - str
     - O
     - 0010
     - 00057
     - ATTENDING DOCTOR
   * - 8
     - ``pv1_8``
     - 60
     - str
     - O
     - 0010
     - 00579
     - REFERRING DOCTOR
   * - 9
     - ``pv1_9``
     - 60
     - list[str]
     - O
     - 0010
     - 00580
     - CONSULTING DOCTOR
   * - 10
     - ``pv1_10``
     - 3
     - str
     - O
     - 0069
     - 00059
     - HOSPITAL SERVICE
   * - 11
     - ``pv1_11``
     - 12
     - str
     - O
     - 0079
     - 00060
     - TEMPORARY LOCATION
   * - 12
     - ``pv1_12``
     - 2
     - str
     - O
     - 0087
     - 00220
     - PRE-ADMIT TEST INDICATOR
   * - 13
     - ``pv1_13``
     - 2
     - str
     - O
     - 0092
     - 00221
     - RE-ADMISSION INDICATOR
   * - 14
     - ``pv1_14``
     - 3
     - str
     - O
     - 0023
     - 00063
     - ADMIT SOURCE
   * - 15
     - ``pv1_15``
     - 2
     - str
     - O
     - 0009
     - 00064
     - AMBULATORY STATUS
   * - 16
     - ``pv1_16``
     - 2
     - str
     - O
     - 0099
     - 00193
     - VIP INDICATOR
   * - 17
     - ``pv1_17``
     - 60
     - str
     - O
     - 0010
     - 00189
     - ADMITTING DOCTOR
   * - 18
     - ``pv1_18``
     - 2
     - str
     - O
     - 0018
     - 00191
     - PATIENT TYPE
   * - 19
     - ``pv1_19``
     - 4
     - str
     - O
     -
     - 00194
     - VISIT NUMBER
   * - 20
     - ``pv1_20``
     - 11
     - list[str]
     - O
     - 0064
     - 00195
     - FINANCIAL CLASS
   * - 21
     - ``pv1_21``
     - 2
     - str
     - O
     - 0032
     - 00199
     - CHARGE PRICE INDICATOR
   * - 22
     - ``pv1_22``
     - 2
     - str
     - O
     - 0045
     - 00386
     - COURTESY CODE
   * - 23
     - ``pv1_23``
     - 2
     - str
     - O
     - 0046
     - 00200
     - CREDIT RATING
   * - 24
     - ``pv1_24``
     - 2
     - list[str]
     - O
     - 0044
     - 00201
     - CONTRACT CODE
   * - 25
     - ``pv1_25``
     - 8
     - list[str]
     - O
     -
     - 00202
     - CONTRACT EFFECTIVE DATE
   * - 26
     - ``pv1_26``
     - 12
     - list[str]
     - O
     -
     - 00203
     - CONTRACT AMOUNT
   * - 27
     - ``pv1_27``
     - 3
     - list[str]
     - O
     -
     - 00204
     - CONTRACT PERIOD
   * - 28
     - ``pv1_28``
     - 2
     - str
     - O
     - 0073
     - 00387
     - INTEREST CODE
   * - 29
     - ``pv1_29``
     - 1
     - str
     - O
     - 0110
     - 00205
     - TRANSFER TO BAD DEBT CODE
   * - 30
     - ``pv1_30``
     - 8
     - str
     - O
     -
     - 00388
     - TRANSFER TO BAD DEBT DATE
   * - 31
     - ``pv1_31``
     - 10
     - str
     - O
     - 0021
     - 00206
     - BAD DEBT AGENCY CODE
   * - 32
     - ``pv1_32``
     - 12
     - str
     - O
     -
     - 00389
     - BAD DEBT TRANSFER AMOUNT
   * - 33
     - ``pv1_33``
     - 12
     - str
     - O
     -
     - 00390
     - BAD DEBT RECOVERY AMOUNT
   * - 34
     - ``pv1_34``
     - 1
     - str
     - O
     - 0111
     - 00207
     - DELETE ACCOUNT INDICATOR
   * - 35
     - ``pv1_35``
     - 8
     - str
     - O
     -
     - 00208
     - DELETE ACCOUNT DATE
   * - 36
     - ``pv1_36``
     - 2
     - str
     - O
     - 0112
     - 00613
     - DISCHARGE DISPOSITION
   * - 37
     - ``pv1_37``
     - 2
     - str
     - O
     - 0113
     - 00614
     - DISCHARGED TO LOCATION
   * - 38
     - ``pv1_38``
     - 2
     - str
     - O
     - 0114
     - 00615
     - DIET TYPE
   * - 39
     - ``pv1_39``
     - 2
     - str
     - O
     - 0115
     - 00616
     - SERVICING FACILITY
   * - 40
     - ``pv1_40``
     - 1
     - str
     - O
     - 0116
     - 00617
     - BED STATUS
   * - 41
     - ``pv1_41``
     - 2
     - str
     - O
     - 0117
     - 00703
     - ACCOUNT STATUS
   * - 42
     - ``pv1_42``
     - 12
     - str
     - O
     - 0079
     - 00704
     - PENDING LOCATION
   * - 43
     - ``pv1_43``
     - 12
     - str
     - O
     - 0079
     - 00705
     - PRIOR TEMPORARY LOCATION
   * - 44
     - ``pv1_44``
     - 19
     - str
     - O
     -
     - 00775
     - ADMIT DATE/TIME
   * - 45
     - ``pv1_45``
     - 19
     - str
     - O
     -
     - 00776
     - DISCHARGE DATE/TIME
   * - 46
     - ``pv1_46``
     - 12
     - str
     - O
     -
     - 00777
     - CURRENT PATIENT BALANCE
   * - 47
     - ``pv1_47``
     - 12
     - str
     - O
     -
     - 00778
     - TOTAL CHARGES
   * - 48
     - ``pv1_48``
     - 12
     - str
     - O
     -
     - 00779
     - TOTAL ADJUSTMENTS
   * - 49
     - ``pv1_49``
     - 12
     - str
     - O
     -
     - 00780
     - TOTAL PAYMENTS

.. _hl7-v2_1-QRD:

QRD: QUERY DEFINITION
~~~~~~~~~~~~~~~~~~~~~

Section 5.3.3

.. py:class:: hl7types.hl7.v2_1.segments.QRD.QRD
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
     - 19
     - str
     - R
     -
     - 00156
     - QUERY DATE/TIME
   * - 2
     - ``qrd_2``
     - 1
     - str
     - R
     - 0106
     - 00158
     - QUERY FORMAT CODE
   * - 3
     - ``qrd_3``
     - 1
     - str
     - R
     - 0091
     - 00159
     - QUERY PRIORITY
   * - 4
     - ``qrd_4``
     - 10
     - str
     - R
     -
     - 00160
     - QUERY ID
   * - 5
     - ``qrd_5``
     - 1
     - str
     - O
     - 0107
     - 00161
     - DEFERRED RESPONSE TYPE
   * - 6
     - ``qrd_6``
     - 19
     - str
     - O
     -
     - 00162
     - DEFERRED RESPONSE DATE/TIME
   * - 7
     - ``qrd_7``
     - 5
     - str
     - R
     - 0126
     - 00164
     - QUANTITY LIMITED REQUEST
   * - 8
     - ``qrd_8``
     - 20
     - list[str]
     - R
     -
     - 00168
     - WHO SUBJECT FILTER
   * - 9
     - ``qrd_9``
     - 3
     - list[str]
     - R
     - 0048
     - 00169
     - WHAT SUBJECT FILTER
   * - 10
     - ``qrd_10``
     - 20
     - list[str]
     - R
     -
     - 00170
     - WHAT DEPARTMENT DATA CODE
   * - 11
     - ``qrd_11``
     - 20
     - list[str]
     - O
     -
     - 00171
     - WHAT DATA CODE VALUE QUAL.
   * - 12
     - ``qrd_12``
     - 1
     - str
     - O
     - 0108
     - 00701
     - QUERY RESULTS LEVEL

.. _hl7-v2_1-QRF:

QRF: QUERY FILTER
~~~~~~~~~~~~~~~~~

Section 5.3.4

.. py:class:: hl7types.hl7.v2_1.segments.QRF.QRF
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
     - 00173
     - WHERE SUBJECT FILTER
   * - 2
     - ``qrf_2``
     - 19
     - str
     - O
     -
     - 00174
     - WHEN DATA START DATE/TIME
   * - 3
     - ``qrf_3``
     - 19
     - str
     - O
     -
     - 00176
     - WHEN DATA END DATE/TIME
   * - 4
     - ``qrf_4``
     - 20
     - list[str]
     - O
     -
     - 00178
     - WHAT USER QUALIFIER
   * - 5
     - ``qrf_5``
     - 20
     - list[str]
     - O
     -
     - 00179
     - OTHER QRY SUBJECT FILTER

.. _hl7-v2_1-RX1:

RX1: PHARMACY ORDER
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.segments.RX1.RX1
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
     - ``rx1_1``
     -
     - str
     - O
     -
     - 00770
     - UNUSED
   * - 2
     - ``rx1_2``
     -
     - str
     - O
     -
     - 00771
     - UNUSED
   * - 3
     - ``rx1_3``
     - 8
     - str
     - O
     - 0033
     - 00129
     - ROUTE
   * - 4
     - ``rx1_4``
     - 20
     - str
     - O
     - 0034
     - 00130
     - SITE ADMINISTERED
   * - 5
     - ``rx1_5``
     - 10
     - str
     - O
     -
     - 00131
     - IV SOLUTION RATE
   * - 6
     - ``rx1_6``
     - 14
     - str
     - O
     -
     - 00133
     - DRUG STRENGTH
   * - 7
     - ``rx1_7``
     - 10
     - str
     - O
     -
     - 00137
     - FINAL CONCENTRATION
   * - 8
     - ``rx1_8``
     - 10
     - str
     - O
     -
     - 00138
     - FINAL VOLUME IN ML.
   * - 9
     - ``rx1_9``
     - 10
     - str
     - O
     -
     - 00135
     - DRUG DOSE
   * - 10
     - ``rx1_10``
     - 1
     - str
     - O
     -
     - 00139
     - DRUG ROLE
   * - 11
     - ``rx1_11``
     - 3
     - str
     - O
     -
     - 00469
     - PRESCRIPTION SEQUENCE #
   * - 12
     - ``rx1_12``
     - 4
     - str
     - O
     -
     - 00470
     - QUANTITY DISPENSED
   * - 13
     - ``rx1_13``
     -
     - str
     - O
     -
     - 00772
     - UNUSED
   * - 14
     - ``rx1_14``
     -
     - :ref:`CE <hl7-v2_1-CE>`
     - O
     - 0057
     - 00473
     - DRUG ID
   * - 15
     - ``rx1_15``
     - 5
     - list[str]
     - O
     -
     - 00474
     - COMPONENT DRUG IDS
   * - 16
     - ``rx1_16``
     - 2
     - str
     - O
     -
     - 00479
     - PRESCRIPTION TYPE
   * - 17
     - ``rx1_17``
     - 1
     - str
     - O
     -
     - 00480
     - SUBSTITUTION STATUS
   * - 18
     - ``rx1_18``
     - 2
     - str
     - O
     - 0038
     - 00588
     - RX ORDER STATUS
   * - 19
     - ``rx1_19``
     - 3
     - str
     - O
     -
     - 00481
     - NUMBER OF REFILLS
   * - 20
     - ``rx1_20``
     -
     - str
     - O
     -
     - 00773
     - UNUSED
   * - 21
     - ``rx1_21``
     - 3
     - str
     - O
     -
     - 00482
     - REFILLS REMAINING
   * - 22
     - ``rx1_22``
     - 5
     - str
     - O
     -
     - 00619
     - DEA CLASS
   * - 23
     - ``rx1_23``
     - 10
     - str
     - O
     -
     - 00620
     - ORDERING MD'S DEA NUMBER
   * - 24
     - ``rx1_24``
     -
     - str
     - O
     -
     - 00774
     - UNUSED
   * - 25
     - ``rx1_25``
     - 19
     - str
     - O
     -
     - 00483
     - LAST REFILL DATE/TIME
   * - 26
     - ``rx1_26``
     - 20
     - str
     - O
     -
     - 00596
     - RX NUMBER
   * - 27
     - ``rx1_27``
     - 5
     - str
     - O
     -
     - 00621
     - PRN STATUS
   * - 28
     - ``rx1_28``
     -
     - list[str]
     - O
     -
     - 00484
     - PHARMACY INSTRUCTIONS
   * - 29
     - ``rx1_29``
     -
     - list[str]
     - O
     -
     - 00489
     - PATIENT INSTRUCTIONS
   * - 30
     - ``rx1_30``
     -
     - list[str]
     - O
     -
     - 00618
     - INSTRUCTIONS (SIG)

.. _hl7-v2_1-UB1:

UB1: UB82 DATA
~~~~~~~~~~~~~~

Section 6.3.8

.. py:class:: hl7types.hl7.v2_1.segments.UB1.UB1
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
     - 00459
     - SET ID - UB82
   * - 2
     - ``ub1_2``
     - 1
     - str
     - O
     -
     - 00279
     - BLOOD DEDUCTIBLE
   * - 3
     - ``ub1_3``
     - 2
     - str
     - O
     -
     - 00396
     - BLOOD FURN.-PINTS OF (40)
   * - 4
     - ``ub1_4``
     - 2
     - str
     - O
     -
     - 00397
     - BLOOD REPLACED-PINTS (41)
   * - 5
     - ``ub1_5``
     - 2
     - str
     - O
     -
     - 00398
     - BLOOD NOT RPLCD-PINTS(42)
   * - 6
     - ``ub1_6``
     - 2
     - str
     - O
     -
     - 00399
     - CO-INSURANCE DAYS (25)
   * - 7
     - ``ub1_7``
     - 2
     - list[str]
     - O
     - 0043
     - 00400
     - CONDITION CODE
   * - 8
     - ``ub1_8``
     - 3
     - str
     - O
     -
     - 00405
     - COVERED DAYS - (23)
   * - 9
     - ``ub1_9``
     - 3
     - str
     - O
     -
     - 00406
     - NON COVERED DAYS - (24)
   * - 10
     - ``ub1_10``
     - 12
     - list[str]
     - O
     -
     - 00407
     - VALUE AMOUNT & CODE
   * - 11
     - ``ub1_11``
     - 2
     - str
     - O
     -
     - 00424
     - NUMBER OF GRACE DAYS (90)
   * - 12
     - ``ub1_12``
     - 2
     - str
     - O
     -
     - 00425
     - SPEC. PROG. INDICATOR(44)
   * - 13
     - ``ub1_13``
     - 1
     - str
     - O
     -
     - 00426
     - PSRO/UR APPROVAL IND. (87)
   * - 14
     - ``ub1_14``
     - 8
     - str
     - O
     -
     - 00427
     - PSRO/UR APRVD STAY-FM(88)
   * - 15
     - ``ub1_15``
     - 8
     - str
     - O
     -
     - 00428
     - PSRO/UR APRVD STAY-TO(89)
   * - 16
     - ``ub1_16``
     - 20
     - list[str]
     - O
     -
     - 00429
     - OCCURRENCE (28-32)
   * - 17
     - ``ub1_17``
     - 2
     - str
     - O
     -
     - 00435
     - OCCURRENCE SPAN (33)
   * - 18
     - ``ub1_18``
     - 8
     - str
     - O
     -
     - 00446
     - OCCURRENCE SPAN START DATE(33)
   * - 19
     - ``ub1_19``
     - 8
     - str
     - O
     -
     - 00447
     - OCCUR. SPAN END DATE (33)
   * - 20
     - ``ub1_20``
     - 30
     - str
     - O
     -
     - 00448
     - UB-82 LOCATOR 2
   * - 21
     - ``ub1_21``
     - 7
     - str
     - O
     -
     - 00449
     - UB-82 LOCATOR 9
   * - 22
     - ``ub1_22``
     - 8
     - str
     - O
     -
     - 00450
     - UB-82 LOCATOR 27
   * - 23
     - ``ub1_23``
     - 17
     - str
     - O
     -
     - 00451
     - UB-82 LOCATOR 45

.. _hl7-v2_1-URD:

URD: RESULTS/UPDATE DEFINITION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.3.5

.. py:class:: hl7types.hl7.v2_1.segments.URD.URD
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
     - 19
     - str
     - O
     -
     - 00600
     - R/U DATE/TIME
   * - 2
     - ``urd_2``
     - 1
     - str
     - O
     - 0109
     - 00601
     - REPORT PRIORITY
   * - 3
     - ``urd_3``
     - 20
     - list[str]
     - R
     -
     - 00602
     - R/U WHO SUBJECT DEFINITION
   * - 4
     - ``urd_4``
     - 3
     - list[str]
     - O
     - 0048
     - 00603
     - R/U WHAT SUBJECT DEFINITION
   * - 5
     - ``urd_5``
     - 20
     - list[str]
     - O
     -
     - 00605
     - R/U WHAT DEPARTMENT CODE
   * - 6
     - ``urd_6``
     - 20
     - list[str]
     - O
     -
     - 00607
     - R/U DISPLAY/PRINT LOCATIONS
   * - 7
     - ``urd_7``
     - 1
     - str
     - O
     - 0108
     - 00702
     - R/U RESULTS LEVEL

.. _hl7-v2_1-URS:

URS: UNSOLICITED SELECTION
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.3.6

.. py:class:: hl7types.hl7.v2_1.segments.URS.URS
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
     - 00608
     - R/U WHERE SUBJECT DEFINITION
   * - 2
     - ``urs_2``
     - 19
     - str
     - O
     -
     - 00609
     - R/U WHEN DATA START DATE/TIME
   * - 3
     - ``urs_3``
     - 19
     - str
     - O
     -
     - 00610
     - R/U WHEN DATA END DATE/TIME
   * - 4
     - ``urs_4``
     - 20
     - list[str]
     - O
     -
     - 00611
     - R/U WHAT USER QUALIFIER
   * - 5
     - ``urs_5``
     - 20
     - list[str]
     - O
     -
     - 00612
     - R/U OTHER RESULTS SUBJECT DEFINI
