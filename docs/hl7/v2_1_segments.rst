v2.1 Segments
=============

.. _hl7-v2_1-ACC:

.. py:class:: hl7types.hl7.v2_1.segments.ACC.ACC
   :noindex:

   HL7 v2 ACC segment.

ACC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``acc_1``
     - ACC.1
     - Optional[str]
     - optional
     - 
     - ACCIDENT DATE/TIME: Item #182
   * - ``acc_2``
     - ACC.2
     - Optional[str]
     - optional
     - 
     - ACCIDENT CODE: Item #184 | Table HL70050
   * - ``acc_3``
     - ACC.3
     - Optional[str]
     - optional
     - 
     - ACCIDENT LOCATION: Item #185

.. _hl7-v2_1-ADD:

.. py:class:: hl7types.hl7.v2_1.segments.ADD.ADD
   :noindex:

   HL7 v2 ADD segment.

ADD
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``add_1``
     - ADD.1
     - Optional[str]
     - optional
     - 
     - ADDENDUM CONTINUATION POINTER: Item #641

.. _hl7-v2_1-BHS:

.. py:class:: hl7types.hl7.v2_1.segments.BHS.BHS
   :noindex:

   HL7 v2 BHS segment.

BHS
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``bhs_1``
     - BHS.1
     - str
     - optional
     - 
     - BATCH FIELD SEPARATOR: Item #685
   * - ``bhs_2``
     - BHS.2
     - str
     - optional
     - 
     - BATCH ENCODING CHARACTERS: Item #686
   * - ``bhs_3``
     - BHS.3
     - Optional[str]
     - optional
     - 
     - BATCH SENDING APPLICATION: Item #687
   * - ``bhs_4``
     - BHS.4
     - Optional[str]
     - optional
     - 
     - BATCH SENDING FACILITY: Item #688
   * - ``bhs_5``
     - BHS.5
     - Optional[str]
     - optional
     - 
     - BATCH RECEIVING APPLICATION: Item #689
   * - ``bhs_6``
     - BHS.6
     - Optional[str]
     - optional
     - 
     - BATCH RECEIVING FACILITY: Item #690
   * - ``bhs_7``
     - BHS.7
     - Optional[str]
     - optional
     - 
     - BATCH CREATION DATE/TIME: Item #655
   * - ``bhs_8``
     - BHS.8
     - Optional[str]
     - optional
     - 
     - BATCH SECURITY: Item #691
   * - ``bhs_9``
     - BHS.9
     - Optional[str]
     - optional
     - 
     - BATCH NAME/ID/TYPE: Item #656
   * - ``bhs_10``
     - BHS.10
     - Optional[str]
     - optional
     - 
     - BATCH COMMENT: Item #657
   * - ``bhs_11``
     - BHS.11
     - Optional[str]
     - optional
     - 
     - BATCH CONTROL ID: Item #658
   * - ``bhs_12``
     - BHS.12
     - Optional[str]
     - optional
     - 
     - REFERENCE BATCH CONTROL ID: Item #659

.. _hl7-v2_1-BLG:

.. py:class:: hl7types.hl7.v2_1.segments.BLG.BLG
   :noindex:

   HL7 v2 BLG segment.

BLG
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``blg_1``
     - BLG.1
     - Optional[str]
     - optional
     - 
     - WHEN TO CHARGE: Item #66 | Table HL70100
   * - ``blg_2``
     - BLG.2
     - Optional[str]
     - optional
     - 
     - CHARGE TYPE: Item #729 | Table HL70122
   * - ``blg_3``
     - BLG.3
     - Optional[str]
     - optional
     - 
     - ACCOUNT ID: Item #730

.. _hl7-v2_1-BTS:

.. py:class:: hl7types.hl7.v2_1.segments.BTS.BTS
   :noindex:

   HL7 v2 BTS segment.

BTS
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``bts_1``
     - BTS.1
     - Optional[str]
     - optional
     - 
     - BATCH MESSAGE COUNT: Item #664
   * - ``bts_2``
     - BTS.2
     - Optional[str]
     - optional
     - 
     - BATCH COMMENT: Item #665
   * - ``bts_3``
     - BTS.3
     - Optional[str]
     - optional
     - 
     - BATCH TOTALS: Item #666

.. _hl7-v2_1-DG1:

.. py:class:: hl7types.hl7.v2_1.segments.DG1.DG1
   :noindex:

   HL7 v2 DG1 segment.

DG1
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``dg1_1``
     - DG1.1
     - str
     - required
     - 
     - SET ID - DIAGNOSIS: Item #506
   * - ``dg1_2``
     - DG1.2
     - str
     - required
     - 
     - DIAGNOSIS CODING METHOD: Item #394 | Table HL70053
   * - ``dg1_3``
     - DG1.3
     - Optional[str]
     - optional
     - 
     - DIAGNOSIS CODE: Item #293 | Table HL70051
   * - ``dg1_4``
     - DG1.4
     - Optional[str]
     - optional
     - 
     - DIAGNOSIS DESCRIPTION: Item #294
   * - ``dg1_5``
     - DG1.5
     - Optional[str]
     - optional
     - 
     - DIAGNOSIS DATE/TIME: Item #295
   * - ``dg1_6``
     - DG1.6
     - str
     - required
     - 
     - DIAGNOSIS/DRG TYPE: Item #297 | Table HL70052
   * - ``dg1_7``
     - DG1.7
     - Optional[str]
     - optional
     - 
     - MAJOR DIAGNOSTIC CATEGORY: Item #298 | Table HL70118
   * - ``dg1_8``
     - DG1.8
     - Optional[str]
     - optional
     - 
     - DIAGNOSTIC RELATED GROUP: Item #299 | Table HL70055
   * - ``dg1_9``
     - DG1.9
     - Optional[str]
     - optional
     - 
     - DRG APPROVAL INDICATOR: Item #373
   * - ``dg1_10``
     - DG1.10
     - Optional[str]
     - optional
     - 
     - DRG GROUPER REVIEW CODE: Item #374 | Table HL70056
   * - ``dg1_11``
     - DG1.11
     - Optional[str]
     - optional
     - 
     - OUTLIER TYPE: Item #375 | Table HL70083
   * - ``dg1_12``
     - DG1.12
     - Optional[str]
     - optional
     - 
     - OUTLIER DAYS: Item #300
   * - ``dg1_13``
     - DG1.13
     - Optional[str]
     - optional
     - 
     - OUTLIER COST: Item #376
   * - ``dg1_14``
     - DG1.14
     - Optional[str]
     - optional
     - 
     - GROUPER VERSION AND TYPE: Item #781

.. _hl7-v2_1-DSC:

.. py:class:: hl7types.hl7.v2_1.segments.DSC.DSC
   :noindex:

   HL7 v2 DSC segment.

DSC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``dsc_1``
     - DSC.1
     - Optional[str]
     - optional
     - 
     - CONTINUATION POINTER: Item #167

.. _hl7-v2_1-DSP:

.. py:class:: hl7types.hl7.v2_1.segments.DSP.DSP
   :noindex:

   HL7 v2 DSP segment.

DSP
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``dsp_1``
     - DSP.1
     - Optional[str]
     - optional
     - 
     - SET ID - DISPLAY DATA: Item #570
   * - ``dsp_2``
     - DSP.2
     - Optional[str]
     - optional
     - 
     - DISPLAY LEVEL: Item #571
   * - ``dsp_3``
     - DSP.3
     - str
     - required
     - 
     - DATA LINE: Item #153
   * - ``dsp_4``
     - DSP.4
     - Optional[str]
     - optional
     - 
     - LOGICAL BREAK POINT: Item #154
   * - ``dsp_5``
     - DSP.5
     - Optional[str]
     - optional
     - 
     - RESULT ID: Item #599

.. _hl7-v2_1-ERR:

.. py:class:: hl7types.hl7.v2_1.segments.ERR.ERR
   :noindex:

   HL7 v2 ERR segment.

ERR
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``err_1``
     - ERR.1
     - List[str]
     - required
     - 
     - ERROR CODE AND LOCATION: Item #80 | Table HL70060

.. _hl7-v2_1-EVN:

.. py:class:: hl7types.hl7.v2_1.segments.EVN.EVN
   :noindex:

   HL7 v2 EVN segment.

EVN
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``evn_1``
     - EVN.1
     - str
     - required
     - 
     - EVENT TYPE CODE: Item #29 | Table HL70003
   * - ``evn_2``
     - EVN.2
     - str
     - required
     - 
     - DATE/TIME OF EVENT: Item #30
   * - ``evn_3``
     - EVN.3
     - Optional[str]
     - optional
     - 
     - DATE/TIME PLANNED EVENT: Item #32
   * - ``evn_4``
     - EVN.4
     - Optional[str]
     - optional
     - 
     - EVENT REASON CODE: Item #369 | Table HL70062

.. _hl7-v2_1-FHS:

.. py:class:: hl7types.hl7.v2_1.segments.FHS.FHS
   :noindex:

   HL7 v2 FHS segment.

FHS
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``fhs_1``
     - FHS.1
     - str
     - optional
     - 
     - FILE FIELD SEPARATOR: Item #692
   * - ``fhs_2``
     - FHS.2
     - str
     - optional
     - 
     - FILE ENCODING CHARACTERS: Item #693
   * - ``fhs_3``
     - FHS.3
     - Optional[str]
     - optional
     - 
     - FILE SENDING APPLICATION: Item #694
   * - ``fhs_4``
     - FHS.4
     - Optional[str]
     - optional
     - 
     - FILE SENDING FACILITY: Item #695
   * - ``fhs_5``
     - FHS.5
     - Optional[str]
     - optional
     - 
     - FILE RECEIVING APPLICATION: Item #696
   * - ``fhs_6``
     - FHS.6
     - Optional[str]
     - optional
     - 
     - FILE RECEIVING FACILITY: Item #697
   * - ``fhs_7``
     - FHS.7
     - Optional[str]
     - optional
     - 
     - DATE/TIME OF FILE CREATION: Item #660
   * - ``fhs_8``
     - FHS.8
     - Optional[str]
     - optional
     - 
     - FILE SECURITY: Item #698
   * - ``fhs_9``
     - FHS.9
     - Optional[str]
     - optional
     - 
     - FILE NAME/ID: Item #661
   * - ``fhs_10``
     - FHS.10
     - Optional[str]
     - optional
     - 
     - FILE HEADER COMMENT: Item #662
   * - ``fhs_11``
     - FHS.11
     - Optional[str]
     - optional
     - 
     - FILE CONTROL ID: Item #663
   * - ``fhs_12``
     - FHS.12
     - Optional[str]
     - optional
     - 
     - REFERENCE FILE CONTROL ID: Item #768

.. _hl7-v2_1-FT1:

.. py:class:: hl7types.hl7.v2_1.segments.FT1.FT1
   :noindex:

   HL7 v2 FT1 segment.

FT1
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ft1_1``
     - FT1.1
     - Optional[str]
     - optional
     - 
     - SET ID - FINANCIAL TRANSACTION: Item #507
   * - ``ft1_2``
     - FT1.2
     - Optional[str]
     - optional
     - 
     - TRANSACTION ID: Item #366
   * - ``ft1_3``
     - FT1.3
     - Optional[str]
     - optional
     - 
     - TRANSACTION BATCH ID: Item #503
   * - ``ft1_4``
     - FT1.4
     - str
     - required
     - 
     - TRANSACTION DATE: Item #351
   * - ``ft1_5``
     - FT1.5
     - Optional[str]
     - optional
     - 
     - TRANSACTION POSTING DATE: Item #352
   * - ``ft1_6``
     - FT1.6
     - str
     - required
     - 
     - TRANSACTION TYPE: Item #353 | Table HL70017
   * - ``ft1_7``
     - FT1.7
     - str
     - required
     - 
     - TRANSACTION CODE: Item #354 | Table HL70096
   * - ``ft1_8``
     - FT1.8
     - Optional[str]
     - optional
     - 
     - TRANSACTION DESCRIPTION: Item #356
   * - ``ft1_9``
     - FT1.9
     - Optional[str]
     - optional
     - 
     - TRANSACTION DESCRIPTION - ALT: Item #706
   * - ``ft1_10``
     - FT1.10
     - Optional[str]
     - optional
     - 
     - TRANSACTION AMOUNT - EXTENDED: Item #358
   * - ``ft1_11``
     - FT1.11
     - Optional[str]
     - optional
     - 
     - TRANSACTION QUANTITY: Item #357
   * - ``ft1_12``
     - FT1.12
     - Optional[str]
     - optional
     - 
     - TRANSACTION AMOUNT - UNIT: Item #782
   * - ``ft1_13``
     - FT1.13
     - Optional[str]
     - optional
     - 
     - DEPARTMENT CODE: Item #355 | Table HL70049
   * - ``ft1_14``
     - FT1.14
     - Optional[str]
     - optional
     - 
     - INSURANCE PLAN ID: Item #359 | Table HL70072
   * - ``ft1_15``
     - FT1.15
     - Optional[str]
     - optional
     - 
     - INSURANCE AMOUNT: Item #360
   * - ``ft1_16``
     - FT1.16
     - Optional[str]
     - optional
     - 
     - PATIENT LOCATION: Item #361 | Table HL70079
   * - ``ft1_17``
     - FT1.17
     - Optional[str]
     - optional
     - 
     - FEE SCHEDULE: Item #362 | Table HL70024
   * - ``ft1_18``
     - FT1.18
     - Optional[str]
     - optional
     - 
     - PATIENT TYPE: Item #363 | Table HL70018
   * - ``ft1_19``
     - FT1.19
     - Optional[str]
     - optional
     - 
     - DIAGNOSIS CODE: Item #364 | Table HL70051
   * - ``ft1_20``
     - FT1.20
     - Optional[str]
     - optional
     - 
     - PERFORMED BY CODE: Item #377 | Table HL70084
   * - ``ft1_21``
     - FT1.21
     - Optional[str]
     - optional
     - 
     - ORDERED BY CODE: Item #783
   * - ``ft1_22``
     - FT1.22
     - Optional[str]
     - optional
     - 
     - UNIT COST: Item #784

.. _hl7-v2_1-FTS:

.. py:class:: hl7types.hl7.v2_1.segments.FTS.FTS
   :noindex:

   HL7 v2 FTS segment.

FTS
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``fts_1``
     - FTS.1
     - Optional[str]
     - optional
     - 
     - FILE BATCH COUNT: Item #667
   * - ``fts_2``
     - FTS.2
     - Optional[str]
     - optional
     - 
     - FILE TRAILER COMMENT: Item #668

.. _hl7-v2_1-GT1:

.. py:class:: hl7types.hl7.v2_1.segments.GT1.GT1
   :noindex:

   HL7 v2 GT1 segment.

GT1
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``gt1_1``
     - GT1.1
     - str
     - required
     - 
     - SET ID - GUARANTOR: Item #321
   * - ``gt1_2``
     - GT1.2
     - Optional[str]
     - optional
     - 
     - GUARANTOR NUMBER: Item #322
   * - ``gt1_3``
     - GT1.3
     - str
     - required
     - 
     - GUARANTOR NAME: Item #323
   * - ``gt1_4``
     - GT1.4
     - Optional[str]
     - optional
     - 
     - GUARANTOR SPOUSE NAME: Item #707
   * - ``gt1_5``
     - GT1.5
     - Optional[str]
     - optional
     - 
     - GUARANTOR ADDRESS: Item #324
   * - ``gt1_6``
     - GT1.6
     - Optional[str]
     - optional
     - 
     - GUARANTOR PH. NUM.- HOME: Item #329
   * - ``gt1_7``
     - GT1.7
     - Optional[str]
     - optional
     - 
     - GUARANTOR PH. NUM-BUSINESS: Item #330
   * - ``gt1_8``
     - GT1.8
     - Optional[str]
     - optional
     - 
     - GUARANTOR DATE OF BIRTH: Item #331
   * - ``gt1_9``
     - GT1.9
     - Optional[str]
     - optional
     - 
     - GUARANTOR SEX: Item #332 | Table HL70001
   * - ``gt1_10``
     - GT1.10
     - Optional[str]
     - optional
     - 
     - GUARANTOR TYPE: Item #333 | Table HL70068
   * - ``gt1_11``
     - GT1.11
     - Optional[str]
     - optional
     - 
     - GUARANTOR RELATIONSHIP: Item #334 | Table HL70063
   * - ``gt1_12``
     - GT1.12
     - Optional[str]
     - optional
     - 
     - GUARANTOR SSN: Item #335
   * - ``gt1_13``
     - GT1.13
     - Optional[str]
     - optional
     - 
     - GUARANTOR DATE - BEGIN: Item #338
   * - ``gt1_14``
     - GT1.14
     - Optional[str]
     - optional
     - 
     - GUARANTOR DATE - END: Item #339
   * - ``gt1_15``
     - GT1.15
     - Optional[str]
     - optional
     - 
     - GUARANTOR PRIORITY: Item #340
   * - ``gt1_16``
     - GT1.16
     - Optional[str]
     - optional
     - 
     - GUARANTOR EMPLOYER NAME: Item #341
   * - ``gt1_17``
     - GT1.17
     - Optional[str]
     - optional
     - 
     - GUARANTOR EMPLOYER ADDRESS: Item #342
   * - ``gt1_18``
     - GT1.18
     - Optional[str]
     - optional
     - 
     - GUARANTOR EMPLOY PHONE #: Item #347
   * - ``gt1_19``
     - GT1.19
     - Optional[str]
     - optional
     - 
     - GUARANTOR EMPLOYEE ID NUM: Item #391
   * - ``gt1_20``
     - GT1.20
     - Optional[str]
     - optional
     - 
     - GUARANTOR EMPLOYMENT STATUS: Item #392 | Table HL70066

.. _hl7-v2_1-IN1:

.. py:class:: hl7types.hl7.v2_1.segments.IN1.IN1
   :noindex:

   HL7 v2 IN1 segment.

IN1
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``in1_1``
     - IN1.1
     - str
     - required
     - 
     - SET ID - INSURANCE: Item #234
   * - ``in1_2``
     - IN1.2
     - str
     - required
     - 
     - INSURANCE PLAN ID: Item #378 | Table HL70072
   * - ``in1_3``
     - IN1.3
     - str
     - required
     - 
     - INSURANCE COMPANY ID: Item #235
   * - ``in1_4``
     - IN1.4
     - Optional[str]
     - optional
     - 
     - INSURANCE COMPANY NAME: Item #236
   * - ``in1_5``
     - IN1.5
     - Optional[str]
     - optional
     - 
     - INSURANCE COMPANY ADDRESS: Item #237
   * - ``in1_6``
     - IN1.6
     - Optional[str]
     - optional
     - 
     - INSURANCE CO. CONTACT PERS: Item #242
   * - ``in1_7``
     - IN1.7
     - Optional[str]
     - optional
     - 
     - INSURANCE CO PHONE NUMBER: Item #243
   * - ``in1_8``
     - IN1.8
     - Optional[str]
     - optional
     - 
     - GROUP NUMBER: Item #248
   * - ``in1_9``
     - IN1.9
     - Optional[str]
     - optional
     - 
     - GROUP NAME: Item #249
   * - ``in1_10``
     - IN1.10
     - Optional[str]
     - optional
     - 
     - INSURED'S GROUP EMP. ID: Item #250
   * - ``in1_11``
     - IN1.11
     - Optional[str]
     - optional
     - 
     - INSURED'S GROUP EMP. NAME: Item #251
   * - ``in1_12``
     - IN1.12
     - Optional[str]
     - optional
     - 
     - PLAN EFFECTIVE DATE: Item #252
   * - ``in1_13``
     - IN1.13
     - Optional[str]
     - optional
     - 
     - PLAN EXPIRATION DATE: Item #253
   * - ``in1_14``
     - IN1.14
     - Optional[str]
     - optional
     - 
     - AUTHORIZATION INFORMATION: Item #254
   * - ``in1_15``
     - IN1.15
     - Optional[str]
     - optional
     - 
     - PLAN TYPE: Item #260 | Table HL70086
   * - ``in1_16``
     - IN1.16
     - Optional[str]
     - optional
     - 
     - NAME OF INSURED: Item #261
   * - ``in1_17``
     - IN1.17
     - Optional[str]
     - optional
     - 
     - INSURED'S RELATIONSHIP TO PATIENT: Item #262 | Table HL70063
   * - ``in1_18``
     - IN1.18
     - Optional[str]
     - optional
     - 
     - INSURED'S DATE OF BIRTH: Item #708
   * - ``in1_19``
     - IN1.19
     - Optional[str]
     - optional
     - 
     - INSURED'S ADDRESS: Item #709
   * - ``in1_20``
     - IN1.20
     - Optional[str]
     - optional
     - 
     - ASSIGNMENT OF BENEFITS: Item #263
   * - ``in1_21``
     - IN1.21
     - Optional[str]
     - optional
     - 
     - COORDINATION OF BENEFITS: Item #264
   * - ``in1_22``
     - IN1.22
     - Optional[str]
     - optional
     - 
     - COORD OF BEN. PRIORITY: Item #265
   * - ``in1_23``
     - IN1.23
     - Optional[str]
     - optional
     - 
     - NOTICE OF ADMISSION CODE: Item #266 | Table HL70081
   * - ``in1_24``
     - IN1.24
     - Optional[str]
     - optional
     - 
     - NOTICE OF ADMISSION DATE: Item #267
   * - ``in1_25``
     - IN1.25
     - Optional[str]
     - optional
     - 
     - RPT OF ELIGIBILITY CODE: Item #268 | Table HL70094
   * - ``in1_26``
     - IN1.26
     - Optional[str]
     - optional
     - 
     - RPT OF ELIGIBILITY DATE: Item #269
   * - ``in1_27``
     - IN1.27
     - Optional[str]
     - optional
     - 
     - RELEASE INFORMATION CODE: Item #270 | Table HL70093
   * - ``in1_28``
     - IN1.28
     - Optional[str]
     - optional
     - 
     - PRE-ADMIT CERT. (PAC): Item #271
   * - ``in1_29``
     - IN1.29
     - Optional[str]
     - optional
     - 
     - VERIFICATION DATE: Item #272
   * - ``in1_30``
     - IN1.30
     - Optional[str]
     - optional
     - 
     - VERIFICATION BY: Item #273
   * - ``in1_31``
     - IN1.31
     - Optional[str]
     - optional
     - 
     - TYPE OF AGREEMENT CODE: Item #277 | Table HL70098
   * - ``in1_32``
     - IN1.32
     - Optional[str]
     - optional
     - 
     - BILLING STATUS: Item #278 | Table HL70022
   * - ``in1_33``
     - IN1.33
     - Optional[str]
     - optional
     - 
     - LIFETIME RESERVE DAYS: Item #280
   * - ``in1_34``
     - IN1.34
     - Optional[str]
     - optional
     - 
     - DELAY BEFORE L. R. DAY: Item #281
   * - ``in1_35``
     - IN1.35
     - Optional[str]
     - optional
     - 
     - COMPANY PLAN CODE: Item #282 | Table HL70042
   * - ``in1_36``
     - IN1.36
     - Optional[str]
     - optional
     - 
     - POLICY NUMBER: Item #283
   * - ``in1_37``
     - IN1.37
     - Optional[str]
     - optional
     - 
     - POLICY DEDUCTIBLE: Item #284
   * - ``in1_38``
     - IN1.38
     - Optional[str]
     - optional
     - 
     - POLICY LIMIT - AMOUNT: Item #285
   * - ``in1_39``
     - IN1.39
     - Optional[str]
     - optional
     - 
     - POLICY LIMIT - DAYS: Item #286
   * - ``in1_40``
     - IN1.40
     - Optional[str]
     - optional
     - 
     - ROOM RATE - SEMI-PRIVATE: Item #287
   * - ``in1_41``
     - IN1.41
     - Optional[str]
     - optional
     - 
     - ROOM RATE - PRIVATE: Item #288
   * - ``in1_42``
     - IN1.42
     - Optional[str]
     - optional
     - 
     - INSURED'S EMPLOYMENT STATUS: Item #710 | Table HL70066
   * - ``in1_43``
     - IN1.43
     - Optional[str]
     - optional
     - 
     - INSURED'S SEX: Item #711 | Table HL70001
   * - ``in1_44``
     - IN1.44
     - Optional[str]
     - optional
     - 
     - INSURED'S EMPLOYER ADDRESS: Item #713

.. _hl7-v2_1-MRG:

.. py:class:: hl7types.hl7.v2_1.segments.MRG.MRG
   :noindex:

   HL7 v2 MRG segment.

MRG
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``mrg_1``
     - MRG.1
     - str
     - required
     - 
     - PRIOR PATIENT ID - INTERNAL: Item #576 | Table HL70061
   * - ``mrg_2``
     - MRG.2
     - Optional[str]
     - optional
     - 
     - PRIOR ALTERNATE PATIENT ID: Item #577 | Table HL70061
   * - ``mrg_3``
     - MRG.3
     - Optional[str]
     - optional
     - 
     - PRIOR PATIENT ACCOUNT NUMBER: Item #578 | Table HL70061

.. _hl7-v2_1-MSA:

.. py:class:: hl7types.hl7.v2_1.segments.MSA.MSA
   :noindex:

   HL7 v2 MSA segment.

MSA
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``msa_1``
     - MSA.1
     - str
     - required
     - 
     - ACKNOWLEDGMENT CODE: Item #2 | Table HL70008
   * - ``msa_2``
     - MSA.2
     - str
     - required
     - 
     - MESSAGE CONTROL ID: Item #3
   * - ``msa_3``
     - MSA.3
     - Optional[str]
     - optional
     - 
     - TEXT MESSAGE: Item #4
   * - ``msa_4``
     - MSA.4
     - Optional[str]
     - optional
     - 
     - EXPECTED SEQUENCE NUMBER: Item #598
   * - ``msa_5``
     - MSA.5
     - Optional[str]
     - optional
     - 
     - DELAYED ACKNOWLEDGMENT TYPE: Item #632 | Table HL70102

.. _hl7-v2_1-MSH:

.. py:class:: hl7types.hl7.v2_1.segments.MSH.MSH
   :noindex:

   HL7 v2 MSH segment.

MSH
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``msh_1``
     - MSH.1
     - str
     - optional
     - 
     - FIELD SEPARATOR: Item #5
   * - ``msh_2``
     - MSH.2
     - str
     - optional
     - 
     - ENCODING CHARACTERS: Item #509
   * - ``msh_3``
     - MSH.3
     - Optional[str]
     - optional
     - 
     - SENDING APPLICATION: Item #6
   * - ``msh_4``
     - MSH.4
     - Optional[str]
     - optional
     - 
     - SENDING FACILITY: Item #512
   * - ``msh_5``
     - MSH.5
     - Optional[str]
     - optional
     - 
     - RECEIVING APPLICATION: Item #9
   * - ``msh_6``
     - MSH.6
     - Optional[str]
     - optional
     - 
     - RECEIVING FACILITY: Item #513
   * - ``msh_7``
     - MSH.7
     - Optional[str]
     - optional
     - 
     - DATE/TIME OF MESSAGE: Item #10
   * - ``msh_8``
     - MSH.8
     - Optional[str]
     - optional
     - 
     - Security: Item #8
   * - ``msh_9``
     - MSH.9
     - str
     - required
     - 
     - MESSAGE TYPE: Item #12 | Table HL70076
   * - ``msh_10``
     - MSH.10
     - str
     - required
     - 
     - MESSAGE CONTROL ID: Item #13
   * - ``msh_11``
     - MSH.11
     - str
     - required
     - 
     - PROCESSING ID: Item #14 | Table HL70103
   * - ``msh_12``
     - MSH.12
     - str
     - required
     - 
     - VERSION ID: Item #15 | Table HL70104
   * - ``msh_13``
     - MSH.13
     - Optional[str]
     - optional
     - 
     - SEQUENCE NUMBER: Item #633
   * - ``msh_14``
     - MSH.14
     - Optional[str]
     - optional
     - 
     - CONTINUATION POINTER: Item #699

.. _hl7-v2_1-NCK:

.. py:class:: hl7types.hl7.v2_1.segments.NCK.NCK
   :noindex:

   HL7 v2 NCK segment.

NCK
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``nck_1``
     - NCK.1
     - str
     - required
     - 
     - SYSTEM DATE/TIME: Item #742

.. _hl7-v2_1-NK1:

.. py:class:: hl7types.hl7.v2_1.segments.NK1.NK1
   :noindex:

   HL7 v2 NK1 segment.

NK1
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``nk1_1``
     - NK1.1
     - str
     - required
     - 
     - SET ID - NEXT OF KIN: Item #712
   * - ``nk1_2``
     - NK1.2
     - Optional[str]
     - optional
     - 
     - NEXT OF KIN NAME: Item #48
   * - ``nk1_3``
     - NK1.3
     - Optional[str]
     - optional
     - 
     - NEXT OF KIN RELATIONSHIP: Item #47 | Table HL70063
   * - ``nk1_4``
     - NK1.4
     - Optional[str]
     - optional
     - 
     - NEXT OF KIN - ADDRESS: Item #225
   * - ``nk1_5``
     - NK1.5
     - Optional[List[str]]
     - optional
     - 
     - NEXT OF KIN - PHONE NUMBER: Item #230

.. _hl7-v2_1-NPU:

.. py:class:: hl7types.hl7.v2_1.segments.NPU.NPU
   :noindex:

   HL7 v2 NPU segment.

NPU
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``npu_1``
     - NPU.1
     - str
     - required
     - 
     - BED LOCATION: Item #785 | Table HL70079
   * - ``npu_2``
     - NPU.2
     - Optional[str]
     - optional
     - 
     - BED STATUS: Item #671 | Table HL70116

.. _hl7-v2_1-NSC:

.. py:class:: hl7types.hl7.v2_1.segments.NSC.NSC
   :noindex:

   HL7 v2 NSC segment.

NSC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``nsc_1``
     - NSC.1
     - str
     - required
     - 
     - NETWORK CHANGE TYPE: Item #758
   * - ``nsc_2``
     - NSC.2
     - Optional[str]
     - optional
     - 
     - CURRENT CPU: Item #759
   * - ``nsc_3``
     - NSC.3
     - Optional[str]
     - optional
     - 
     - CURRENT FILESERVER: Item #760
   * - ``nsc_4``
     - NSC.4
     - Optional[str]
     - optional
     - 
     - CURRENT APPLICATION: Item #761
   * - ``nsc_5``
     - NSC.5
     - Optional[str]
     - optional
     - 
     - CURRENT FACILITY: Item #762
   * - ``nsc_6``
     - NSC.6
     - Optional[str]
     - optional
     - 
     - NEW CPU: Item #763
   * - ``nsc_7``
     - NSC.7
     - Optional[str]
     - optional
     - 
     - NEW FILESERVER: Item #764
   * - ``nsc_8``
     - NSC.8
     - Optional[str]
     - optional
     - 
     - NEW APPLICATION: Item #765
   * - ``nsc_9``
     - NSC.9
     - Optional[str]
     - optional
     - 
     - NEW FACILITY: Item #766

.. _hl7-v2_1-NST:

.. py:class:: hl7types.hl7.v2_1.segments.NST.NST
   :noindex:

   HL7 v2 NST segment.

NST
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``nst_1``
     - NST.1
     - str
     - required
     - 
     - STATISTICS AVAILABLE: Item #743
   * - ``nst_2``
     - NST.2
     - Optional[str]
     - optional
     - 
     - SOURCE IDENTIFIER: Item #744
   * - ``nst_3``
     - NST.3
     - Optional[str]
     - optional
     - 
     - SOURCE TYPE: Item #745
   * - ``nst_4``
     - NST.4
     - Optional[str]
     - optional
     - 
     - STATISTICS START: Item #746
   * - ``nst_5``
     - NST.5
     - Optional[str]
     - optional
     - 
     - STATISTICS END: Item #747
   * - ``nst_6``
     - NST.6
     - Optional[str]
     - optional
     - 
     - RECEIVE CHARACTER COUNT: Item #748
   * - ``nst_7``
     - NST.7
     - Optional[str]
     - optional
     - 
     - SEND CHARACTER COUNT: Item #749
   * - ``nst_8``
     - NST.8
     - Optional[str]
     - optional
     - 
     - MESSAGES RECEIVED: Item #750
   * - ``nst_9``
     - NST.9
     - Optional[str]
     - optional
     - 
     - MESSAGES SENT: Item #751
   * - ``nst_10``
     - NST.10
     - Optional[str]
     - optional
     - 
     - CHECKSUM ERRORS RECEIVED: Item #752
   * - ``nst_11``
     - NST.11
     - Optional[str]
     - optional
     - 
     - LENGTH ERRORS RECEIVED: Item #753
   * - ``nst_12``
     - NST.12
     - Optional[str]
     - optional
     - 
     - OTHER ERRORS RECEIVED: Item #754
   * - ``nst_13``
     - NST.13
     - Optional[str]
     - optional
     - 
     - CONNECT TIMEOUTS: Item #755
   * - ``nst_14``
     - NST.14
     - Optional[str]
     - optional
     - 
     - RECEIVE TIMEOUTS: Item #756
   * - ``nst_15``
     - NST.15
     - Optional[str]
     - optional
     - 
     - NETWORK ERRORS: Item #757

.. _hl7-v2_1-NTE:

.. py:class:: hl7types.hl7.v2_1.segments.NTE.NTE
   :noindex:

   HL7 v2 NTE segment.

NTE
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``nte_1``
     - NTE.1
     - Optional[str]
     - optional
     - 
     - SET ID - NOTES AND COMMENTS: Item #573
   * - ``nte_2``
     - NTE.2
     - Optional[str]
     - optional
     - 
     - SOURCE OF COMMENT: Item #574 | Table HL70105
   * - ``nte_3``
     - NTE.3
     - List[str]
     - required
     - 
     - COMMENT: Item #575

.. _hl7-v2_1-OBR:

.. py:class:: hl7types.hl7.v2_1.segments.OBR.OBR
   :noindex:

   HL7 v2 OBR segment.

OBR
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``obr_1``
     - OBR.1
     - Optional[str]
     - optional
     - 
     - SET ID - OBSERVATION REQUEST: Item #520
   * - ``obr_2``
     - OBR.2
     - Optional[str]
     - optional
     - 
     - PLACER ORDER #: Item #732
   * - ``obr_3``
     - OBR.3
     - Optional[str]
     - optional
     - 
     - FILLER ORDER #: Item #733
   * - ``obr_4``
     - OBR.4
     - :ref:`CE <hl7-v2_1-CE>`
     - required
     - 
     - UNIVERSAL SERVICE IDENT.: Item #523
   * - ``obr_5``
     - OBR.5
     - Optional[str]
     - optional
     - 
     - PRIORITY: Item #524
   * - ``obr_6``
     - OBR.6
     - Optional[str]
     - optional
     - 
     - REQUESTED DATE-TIME: Item #529
   * - ``obr_7``
     - OBR.7
     - str
     - required
     - 
     - OBSERVATION DATE/TIME: Item #530
   * - ``obr_8``
     - OBR.8
     - str
     - required
     - 
     - OBSERVATION END DATE/TIME: Item #531
   * - ``obr_9``
     - OBR.9
     - str
     - required
     - 
     - COLLECTION VOLUME: Item #532 | Table HL70036
   * - ``obr_10``
     - OBR.10
     - Optional[List[str]]
     - optional
     - 
     - COLLECTOR IDENTIFIER: Item #533
   * - ``obr_11``
     - OBR.11
     - Optional[str]
     - optional
     - 
     - SPECIMEN ACTION CODE: Item #534 | Table HL70065
   * - ``obr_12``
     - OBR.12
     - Optional[str]
     - optional
     - 
     - DANGER CODE: Item #535 | Table HL70047
   * - ``obr_13``
     - OBR.13
     - Optional[str]
     - optional
     - 
     - RELEVANT CLINICAL INFO.: Item #536
   * - ``obr_14``
     - OBR.14
     - str
     - required
     - 
     - SPECIMEN RECEIVED DATE/TIME: Item #537
   * - ``obr_15``
     - OBR.15
     - Optional[str]
     - optional
     - 
     - SPECIMEN SOURCE: Item #538 | Table HL70070
   * - ``obr_16``
     - OBR.16
     - Optional[List[str]]
     - optional
     - 
     - ORDERING PROVIDER: Item #539 | Table HL70010
   * - ``obr_17``
     - OBR.17
     - Optional[List[str]]
     - optional
     - 
     - ORDER CALL-BACK PHONE NUM: Item #540
   * - ``obr_18``
     - OBR.18
     - Optional[str]
     - optional
     - 
     - PLACERS FIELD #1: Item #541
   * - ``obr_19``
     - OBR.19
     - Optional[str]
     - optional
     - 
     - PLACERS FIELD #2: Item #542
   * - ``obr_20``
     - OBR.20
     - Optional[str]
     - optional
     - 
     - FILLERS FIELD #1: Item #543
   * - ``obr_21``
     - OBR.21
     - Optional[str]
     - optional
     - 
     - FILLERS FIELD #2: Item #544
   * - ``obr_22``
     - OBR.22
     - str
     - required
     - 
     - RESULTS RPT/STATUS CHNG - DATE/T: Item #546
   * - ``obr_23``
     - OBR.23
     - Optional[str]
     - optional
     - 
     - CHARGE TO PRACTICE: Item #547
   * - ``obr_24``
     - OBR.24
     - Optional[str]
     - optional
     - 
     - DIAGNOSTIC SERV SECT ID: Item #548 | Table HL70074
   * - ``obr_25``
     - OBR.25
     - Optional[str]
     - optional
     - 
     - RESULT STATUS: Item #734 | Table HL70123
   * - ``obr_26``
     - OBR.26
     - Optional[:ref:`CE <hl7-v2_1-CE>`]
     - optional
     - 
     - LINKED RESULTS: Item #550
   * - ``obr_27``
     - OBR.27
     - Optional[List[str]]
     - optional
     - 
     - QUANTITY/TIMING: Item #735
   * - ``obr_28``
     - OBR.28
     - Optional[List[str]]
     - optional
     - 
     - RESULT COPIES TO: Item #551
   * - ``obr_29``
     - OBR.29
     - Optional[str]
     - optional
     - 
     - PARENT ACCESSION #: Item #737
   * - ``obr_30``
     - OBR.30
     - Optional[str]
     - optional
     - 
     - TRANSPORTATION MODE: Item #625 | Table HL70124
   * - ``obr_31``
     - OBR.31
     - Optional[List[:ref:`CE <hl7-v2_1-CE>`]]
     - optional
     - 
     - REASON FOR STUDY: Item #626
   * - ``obr_32``
     - OBR.32
     - Optional[str]
     - optional
     - 
     - PRINCIPAL RESULT INTERPRETER: Item #627
   * - ``obr_33``
     - OBR.33
     - Optional[str]
     - optional
     - 
     - ASSISTANT RESULT INTERPRETER: Item #628
   * - ``obr_34``
     - OBR.34
     - Optional[str]
     - optional
     - 
     - TECHNICIAN: Item #630
   * - ``obr_35``
     - OBR.35
     - Optional[str]
     - optional
     - 
     - TRANSCRIPTIONIST: Item #629
   * - ``obr_36``
     - OBR.36
     - Optional[str]
     - optional
     - 
     - SCHEDULED - DATE/TIME: Item #736

.. _hl7-v2_1-OBX:

.. py:class:: hl7types.hl7.v2_1.segments.OBX.OBX
   :noindex:

   HL7 v2 OBX segment.

OBX
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``obx_1``
     - OBX.1
     - Optional[str]
     - optional
     - 
     - SET ID - OBSERVATION SIMPLE: Item #559
   * - ``obx_2``
     - OBX.2
     - Optional[str]
     - optional
     - 
     - VALUE TYPE: Item #676 | Table HL70125
   * - ``obx_3``
     - OBX.3
     - :ref:`CE <hl7-v2_1-CE>`
     - required
     - 
     - OBSERVATION IDENTIFIER: Item #560
   * - ``obx_4``
     - OBX.4
     - Optional[str]
     - optional
     - 
     - OBSERVATION SUB-ID: Item #769
   * - ``obx_5``
     - OBX.5
     - str
     - required
     - 
     - OBSERVATION RESULTS: Item #561
   * - ``obx_6``
     - OBX.6
     - Optional[str]
     - optional
     - 
     - UNITS: Item #562
   * - ``obx_7``
     - OBX.7
     - Optional[str]
     - optional
     - 
     - REFERENCES RANGE: Item #563
   * - ``obx_8``
     - OBX.8
     - Optional[List[str]]
     - optional
     - 
     - ABNORMAL FLAGS: Item #564 | Table HL70078
   * - ``obx_9``
     - OBX.9
     - Optional[str]
     - optional
     - 
     - PROBABILITY: Item #639
   * - ``obx_10``
     - OBX.10
     - Optional[str]
     - optional
     - 
     - NATURE OF ABNORMAL TEST: Item #565 | Table HL70080
   * - ``obx_11``
     - OBX.11
     - Optional[str]
     - optional
     - 
     - OBSERV RESULT STATUS: Item #566 | Table HL70085
   * - ``obx_12``
     - OBX.12
     - Optional[str]
     - optional
     - 
     - DATE LAST OBS NORMAL VALUES: Item #567

.. _hl7-v2_1-ORC:

.. py:class:: hl7types.hl7.v2_1.segments.ORC.ORC
   :noindex:

   HL7 v2 ORC segment.

ORC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``orc_1``
     - ORC.1
     - str
     - required
     - 
     - ORDER CONTROL: Item #714 | Table HL70119
   * - ``orc_2``
     - ORC.2
     - Optional[str]
     - optional
     - 
     - PLACER ORDER #: Item #715
   * - ``orc_3``
     - ORC.3
     - Optional[str]
     - optional
     - 
     - FILLER ORDER #: Item #716
   * - ``orc_4``
     - ORC.4
     - Optional[str]
     - optional
     - 
     - PLACER GROUP #: Item #717
   * - ``orc_5``
     - ORC.5
     - Optional[str]
     - optional
     - 
     - ORDER STATUS: Item #718 | Table HL70038
   * - ``orc_6``
     - ORC.6
     - Optional[str]
     - optional
     - 
     - RESPONSE FLAG: Item #719 | Table HL70121
   * - ``orc_7``
     - ORC.7
     - Optional[str]
     - optional
     - 
     - TIMING/QUANTITY: Item #720
   * - ``orc_8``
     - ORC.8
     - Optional[str]
     - optional
     - 
     - PARENT: Item #721
   * - ``orc_9``
     - ORC.9
     - Optional[str]
     - optional
     - 
     - DATE/TIME OF TRANSACTION: Item #722
   * - ``orc_10``
     - ORC.10
     - Optional[str]
     - optional
     - 
     - ENTERED BY: Item #723
   * - ``orc_11``
     - ORC.11
     - Optional[str]
     - optional
     - 
     - VERIFIED BY: Item #724
   * - ``orc_12``
     - ORC.12
     - Optional[str]
     - optional
     - 
     - ORDERING PROVIDER: Item #725
   * - ``orc_13``
     - ORC.13
     - Optional[str]
     - optional
     - 
     - ENTERER'S LOCATION: Item #726
   * - ``orc_14``
     - ORC.14
     - Optional[List[str]]
     - optional
     - 
     - CALL BACK PHONE NUMBER: Item #727

.. _hl7-v2_1-ORO:

.. py:class:: hl7types.hl7.v2_1.segments.ORO.ORO
   :noindex:

   HL7 v2 ORO segment.

ORO
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``oro_1``
     - ORO.1
     - Optional[:ref:`CE <hl7-v2_1-CE>`]
     - optional
     - 
     - ORDER ITEM ID: Item #731
   * - ``oro_2``
     - ORO.2
     - Optional[str]
     - optional
     - 
     - SUBSTITUTE ALLOWED: Item #120
   * - ``oro_3``
     - ORO.3
     - Optional[List[str]]
     - optional
     - 
     - RESULTS COPIES TO: Item #586
   * - ``oro_4``
     - ORO.4
     - Optional[str]
     - optional
     - 
     - STOCK LOCATION: Item #68 | Table HL70012

.. _hl7-v2_1-PID:

.. py:class:: hl7types.hl7.v2_1.segments.PID.PID
   :noindex:

   HL7 v2 PID segment.

PID
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``pid_1``
     - PID.1
     - Optional[str]
     - optional
     - 
     - SET ID - PATIENT ID: Item #572
   * - ``pid_2``
     - PID.2
     - Optional[str]
     - optional
     - 
     - PATIENT ID EXTERNAL (EXTERNAL ID): Item #581 | Table HL70061
   * - ``pid_3``
     - PID.3
     - str
     - required
     - 
     - PATIENT ID INTERNAL (INTERNAL ID): Item #34 | Table HL70061
   * - ``pid_4``
     - PID.4
     - Optional[str]
     - optional
     - 
     - ALTERNATE PATIENT ID: Item #38
   * - ``pid_5``
     - PID.5
     - str
     - required
     - 
     - PATIENT NAME: Item #41
   * - ``pid_6``
     - PID.6
     - Optional[str]
     - optional
     - 
     - MOTHER'S MAIDEN NAME: Item #582
   * - ``pid_7``
     - PID.7
     - Optional[str]
     - optional
     - 
     - DATE OF BIRTH: Item #43
   * - ``pid_8``
     - PID.8
     - Optional[str]
     - optional
     - 
     - SEX: Item #42 | Table HL70001
   * - ``pid_9``
     - PID.9
     - Optional[List[str]]
     - optional
     - 
     - PATIENT ALIAS: Item #597
   * - ``pid_10``
     - PID.10
     - Optional[str]
     - optional
     - 
     - ETHNIC GROUP: Item #44 | Table HL70005
   * - ``pid_11``
     - PID.11
     - Optional[str]
     - optional
     - 
     - PATIENT ADDRESS: Item #20
   * - ``pid_12``
     - PID.12
     - Optional[str]
     - optional
     - 
     - COUNTY CODE: Item #26
   * - ``pid_13``
     - PID.13
     - Optional[List[str]]
     - optional
     - 
     - PHONE NUMBER - HOME: Item #49
   * - ``pid_14``
     - PID.14
     - Optional[List[str]]
     - optional
     - 
     - PHONE NUMBER - BUSINESS: Item #50
   * - ``pid_15``
     - PID.15
     - Optional[str]
     - optional
     - 
     - LANGUAGE - PATIENT: Item #464
   * - ``pid_16``
     - PID.16
     - Optional[str]
     - optional
     - 
     - MARITAL STATUS: Item #46 | Table HL70002
   * - ``pid_17``
     - PID.17
     - Optional[str]
     - optional
     - 
     - RELIGION: Item #45 | Table HL70006
   * - ``pid_18``
     - PID.18
     - Optional[str]
     - optional
     - 
     - PATIENT ACCOUNT NUMBER: Item #35 | Table HL70061
   * - ``pid_19``
     - PID.19
     - Optional[str]
     - optional
     - 
     - SSN NUMBER - PATIENT: Item #457
   * - ``pid_20``
     - PID.20
     - Optional[str]
     - optional
     - 
     - DRIVER'S LIC NUM - PATIENT: Item #453

.. _hl7-v2_1-PR1:

.. py:class:: hl7types.hl7.v2_1.segments.PR1.PR1
   :noindex:

   HL7 v2 PR1 segment.

PR1
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``pr1_1``
     - PR1.1
     - List[str]
     - required
     - 
     - SET ID - PROCEDURE: Item #304
   * - ``pr1_2``
     - PR1.2
     - str
     - required
     - 
     - PROCEDURE CODING METHOD.: Item #393 | Table HL70089
   * - ``pr1_3``
     - PR1.3
     - str
     - required
     - 
     - PROCEDURE CODE: Item #305 | Table HL70088
   * - ``pr1_4``
     - PR1.4
     - Optional[str]
     - optional
     - 
     - PROCEDURE DESCRIPTION: Item #306
   * - ``pr1_5``
     - PR1.5
     - str
     - required
     - 
     - PROCEDURE DATE/TIME: Item #307
   * - ``pr1_6``
     - PR1.6
     - str
     - required
     - 
     - PROCEDURE TYPE: Item #309 | Table HL70090
   * - ``pr1_7``
     - PR1.7
     - Optional[str]
     - optional
     - 
     - PROCEDURE MINUTES: Item #310
   * - ``pr1_8``
     - PR1.8
     - Optional[str]
     - optional
     - 
     - ANESTHESIOLOGIST: Item #311 | Table HL70010
   * - ``pr1_9``
     - PR1.9
     - Optional[str]
     - optional
     - 
     - ANESTHESIA CODE: Item #313 | Table HL70019
   * - ``pr1_10``
     - PR1.10
     - Optional[str]
     - optional
     - 
     - ANESTHESIA MINUTES: Item #314
   * - ``pr1_11``
     - PR1.11
     - Optional[str]
     - optional
     - 
     - SURGEON: Item #315 | Table HL70010
   * - ``pr1_12``
     - PR1.12
     - Optional[str]
     - optional
     - 
     - RESIDENT CODE: Item #318 | Table HL70010
   * - ``pr1_13``
     - PR1.13
     - Optional[str]
     - optional
     - 
     - CONSENT CODE: Item #317 | Table HL70059

.. _hl7-v2_1-PV1:

.. py:class:: hl7types.hl7.v2_1.segments.PV1.PV1
   :noindex:

   HL7 v2 PV1 segment.

PV1
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``pv1_1``
     - PV1.1
     - Optional[str]
     - optional
     - 
     - SET ID - PATIENT VISIT: Item #458
   * - ``pv1_2``
     - PV1.2
     - str
     - required
     - 
     - PATIENT CLASS: Item #52 | Table HL70004
   * - ``pv1_3``
     - PV1.3
     - str
     - required
     - 
     - ASSIGNED PATIENT LOCATION: Item #53 | Table HL70079
   * - ``pv1_4``
     - PV1.4
     - Optional[str]
     - optional
     - 
     - ADMISSION TYPE: Item #218 | Table HL70007
   * - ``pv1_5``
     - PV1.5
     - Optional[str]
     - optional
     - 
     - PRE-ADMIT NUMBER: Item #219
   * - ``pv1_6``
     - PV1.6
     - Optional[str]
     - optional
     - 
     - PRIOR PATIENT LOCATION: Item #56 | Table HL70079
   * - ``pv1_7``
     - PV1.7
     - Optional[str]
     - optional
     - 
     - ATTENDING DOCTOR: Item #57 | Table HL70010
   * - ``pv1_8``
     - PV1.8
     - Optional[str]
     - optional
     - 
     - REFERRING DOCTOR: Item #579 | Table HL70010
   * - ``pv1_9``
     - PV1.9
     - Optional[List[str]]
     - optional
     - 
     - CONSULTING DOCTOR: Item #580 | Table HL70010
   * - ``pv1_10``
     - PV1.10
     - Optional[str]
     - optional
     - 
     - HOSPITAL SERVICE: Item #59 | Table HL70069
   * - ``pv1_11``
     - PV1.11
     - Optional[str]
     - optional
     - 
     - TEMPORARY LOCATION: Item #60 | Table HL70079
   * - ``pv1_12``
     - PV1.12
     - Optional[str]
     - optional
     - 
     - PRE-ADMIT TEST INDICATOR: Item #220 | Table HL70087
   * - ``pv1_13``
     - PV1.13
     - Optional[str]
     - optional
     - 
     - RE-ADMISSION INDICATOR: Item #221 | Table HL70092
   * - ``pv1_14``
     - PV1.14
     - Optional[str]
     - optional
     - 
     - ADMIT SOURCE: Item #63 | Table HL70023
   * - ``pv1_15``
     - PV1.15
     - Optional[str]
     - optional
     - 
     - AMBULATORY STATUS: Item #64 | Table HL70009
   * - ``pv1_16``
     - PV1.16
     - Optional[str]
     - optional
     - 
     - VIP INDICATOR: Item #193 | Table HL70099
   * - ``pv1_17``
     - PV1.17
     - Optional[str]
     - optional
     - 
     - ADMITTING DOCTOR: Item #189 | Table HL70010
   * - ``pv1_18``
     - PV1.18
     - Optional[str]
     - optional
     - 
     - PATIENT TYPE: Item #191 | Table HL70018
   * - ``pv1_19``
     - PV1.19
     - Optional[str]
     - optional
     - 
     - VISIT NUMBER: Item #194
   * - ``pv1_20``
     - PV1.20
     - Optional[List[str]]
     - optional
     - 
     - FINANCIAL CLASS: Item #195 | Table HL70064
   * - ``pv1_21``
     - PV1.21
     - Optional[str]
     - optional
     - 
     - CHARGE PRICE INDICATOR: Item #199 | Table HL70032
   * - ``pv1_22``
     - PV1.22
     - Optional[str]
     - optional
     - 
     - COURTESY CODE: Item #386 | Table HL70045
   * - ``pv1_23``
     - PV1.23
     - Optional[str]
     - optional
     - 
     - CREDIT RATING: Item #200 | Table HL70046
   * - ``pv1_24``
     - PV1.24
     - Optional[List[str]]
     - optional
     - 
     - CONTRACT CODE: Item #201 | Table HL70044
   * - ``pv1_25``
     - PV1.25
     - Optional[List[str]]
     - optional
     - 
     - CONTRACT EFFECTIVE DATE: Item #202
   * - ``pv1_26``
     - PV1.26
     - Optional[List[str]]
     - optional
     - 
     - CONTRACT AMOUNT: Item #203
   * - ``pv1_27``
     - PV1.27
     - Optional[List[str]]
     - optional
     - 
     - CONTRACT PERIOD: Item #204
   * - ``pv1_28``
     - PV1.28
     - Optional[str]
     - optional
     - 
     - INTEREST CODE: Item #387 | Table HL70073
   * - ``pv1_29``
     - PV1.29
     - Optional[str]
     - optional
     - 
     - TRANSFER TO BAD DEBT CODE: Item #205 | Table HL70110
   * - ``pv1_30``
     - PV1.30
     - Optional[str]
     - optional
     - 
     - TRANSFER TO BAD DEBT DATE: Item #388
   * - ``pv1_31``
     - PV1.31
     - Optional[str]
     - optional
     - 
     - BAD DEBT AGENCY CODE: Item #206 | Table HL70021
   * - ``pv1_32``
     - PV1.32
     - Optional[str]
     - optional
     - 
     - BAD DEBT TRANSFER AMOUNT: Item #389
   * - ``pv1_33``
     - PV1.33
     - Optional[str]
     - optional
     - 
     - BAD DEBT RECOVERY AMOUNT: Item #390
   * - ``pv1_34``
     - PV1.34
     - Optional[str]
     - optional
     - 
     - DELETE ACCOUNT INDICATOR: Item #207 | Table HL70111
   * - ``pv1_35``
     - PV1.35
     - Optional[str]
     - optional
     - 
     - DELETE ACCOUNT DATE: Item #208
   * - ``pv1_36``
     - PV1.36
     - Optional[str]
     - optional
     - 
     - DISCHARGE DISPOSITION: Item #613 | Table HL70112
   * - ``pv1_37``
     - PV1.37
     - Optional[str]
     - optional
     - 
     - DISCHARGED TO LOCATION: Item #614 | Table HL70113
   * - ``pv1_38``
     - PV1.38
     - Optional[str]
     - optional
     - 
     - DIET TYPE: Item #615 | Table HL70114
   * - ``pv1_39``
     - PV1.39
     - Optional[str]
     - optional
     - 
     - SERVICING FACILITY: Item #616 | Table HL70115
   * - ``pv1_40``
     - PV1.40
     - Optional[str]
     - optional
     - 
     - BED STATUS: Item #617 | Table HL70116
   * - ``pv1_41``
     - PV1.41
     - Optional[str]
     - optional
     - 
     - ACCOUNT STATUS: Item #703 | Table HL70117
   * - ``pv1_42``
     - PV1.42
     - Optional[str]
     - optional
     - 
     - PENDING LOCATION: Item #704 | Table HL70079
   * - ``pv1_43``
     - PV1.43
     - Optional[str]
     - optional
     - 
     - PRIOR TEMPORARY LOCATION: Item #705 | Table HL70079
   * - ``pv1_44``
     - PV1.44
     - Optional[str]
     - optional
     - 
     - ADMIT DATE/TIME: Item #775
   * - ``pv1_45``
     - PV1.45
     - Optional[str]
     - optional
     - 
     - DISCHARGE DATE/TIME: Item #776
   * - ``pv1_46``
     - PV1.46
     - Optional[str]
     - optional
     - 
     - CURRENT PATIENT BALANCE: Item #777
   * - ``pv1_47``
     - PV1.47
     - Optional[str]
     - optional
     - 
     - TOTAL CHARGES: Item #778
   * - ``pv1_48``
     - PV1.48
     - Optional[str]
     - optional
     - 
     - TOTAL ADJUSTMENTS: Item #779
   * - ``pv1_49``
     - PV1.49
     - Optional[str]
     - optional
     - 
     - TOTAL PAYMENTS: Item #780

.. _hl7-v2_1-QRD:

.. py:class:: hl7types.hl7.v2_1.segments.QRD.QRD
   :noindex:

   HL7 v2 QRD segment.

QRD
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``qrd_1``
     - QRD.1
     - str
     - required
     - 
     - QUERY DATE/TIME: Item #156
   * - ``qrd_2``
     - QRD.2
     - str
     - required
     - 
     - QUERY FORMAT CODE: Item #158 | Table HL70106
   * - ``qrd_3``
     - QRD.3
     - str
     - required
     - 
     - QUERY PRIORITY: Item #159 | Table HL70091
   * - ``qrd_4``
     - QRD.4
     - str
     - required
     - 
     - QUERY ID: Item #160
   * - ``qrd_5``
     - QRD.5
     - Optional[str]
     - optional
     - 
     - DEFERRED RESPONSE TYPE: Item #161 | Table HL70107
   * - ``qrd_6``
     - QRD.6
     - Optional[str]
     - optional
     - 
     - DEFERRED RESPONSE DATE/TIME: Item #162
   * - ``qrd_7``
     - QRD.7
     - str
     - required
     - 
     - QUANTITY LIMITED REQUEST: Item #164 | Table HL70126
   * - ``qrd_8``
     - QRD.8
     - List[str]
     - required
     - 
     - WHO SUBJECT FILTER: Item #168
   * - ``qrd_9``
     - QRD.9
     - List[str]
     - required
     - 
     - WHAT SUBJECT FILTER: Item #169 | Table HL70048
   * - ``qrd_10``
     - QRD.10
     - List[str]
     - required
     - 
     - WHAT DEPARTMENT DATA CODE: Item #170
   * - ``qrd_11``
     - QRD.11
     - Optional[List[str]]
     - optional
     - 
     - WHAT DATA CODE VALUE QUAL.: Item #171
   * - ``qrd_12``
     - QRD.12
     - Optional[str]
     - optional
     - 
     - QUERY RESULTS LEVEL: Item #701 | Table HL70108

.. _hl7-v2_1-QRF:

.. py:class:: hl7types.hl7.v2_1.segments.QRF.QRF
   :noindex:

   HL7 v2 QRF segment.

QRF
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``qrf_1``
     - QRF.1
     - List[str]
     - required
     - 
     - WHERE SUBJECT FILTER: Item #173
   * - ``qrf_2``
     - QRF.2
     - Optional[str]
     - optional
     - 
     - WHEN DATA START DATE/TIME: Item #174
   * - ``qrf_3``
     - QRF.3
     - Optional[str]
     - optional
     - 
     - WHEN DATA END DATE/TIME: Item #176
   * - ``qrf_4``
     - QRF.4
     - Optional[List[str]]
     - optional
     - 
     - WHAT USER QUALIFIER: Item #178
   * - ``qrf_5``
     - QRF.5
     - Optional[List[str]]
     - optional
     - 
     - OTHER QRY SUBJECT FILTER: Item #179

.. _hl7-v2_1-RX1:

.. py:class:: hl7types.hl7.v2_1.segments.RX1.RX1
   :noindex:

   HL7 v2 RX1 segment.

RX1
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``rx1_1``
     - RX1.1
     - Optional[str]
     - optional
     - 
     - UNUSED: Item #770
   * - ``rx1_2``
     - RX1.2
     - Optional[str]
     - optional
     - 
     - UNUSED: Item #771
   * - ``rx1_3``
     - RX1.3
     - Optional[str]
     - optional
     - 
     - ROUTE: Item #129 | Table HL70033
   * - ``rx1_4``
     - RX1.4
     - Optional[str]
     - optional
     - 
     - SITE ADMINISTERED: Item #130 | Table HL70034
   * - ``rx1_5``
     - RX1.5
     - Optional[str]
     - optional
     - 
     - IV SOLUTION RATE: Item #131
   * - ``rx1_6``
     - RX1.6
     - Optional[str]
     - optional
     - 
     - DRUG STRENGTH: Item #133
   * - ``rx1_7``
     - RX1.7
     - Optional[str]
     - optional
     - 
     - FINAL CONCENTRATION: Item #137
   * - ``rx1_8``
     - RX1.8
     - Optional[str]
     - optional
     - 
     - FINAL VOLUME IN ML.: Item #138
   * - ``rx1_9``
     - RX1.9
     - Optional[str]
     - optional
     - 
     - DRUG DOSE: Item #135
   * - ``rx1_10``
     - RX1.10
     - Optional[str]
     - optional
     - 
     - DRUG ROLE: Item #139
   * - ``rx1_11``
     - RX1.11
     - Optional[str]
     - optional
     - 
     - PRESCRIPTION SEQUENCE #: Item #469
   * - ``rx1_12``
     - RX1.12
     - Optional[str]
     - optional
     - 
     - QUANTITY DISPENSED: Item #470
   * - ``rx1_13``
     - RX1.13
     - Optional[str]
     - optional
     - 
     - UNUSED: Item #772
   * - ``rx1_14``
     - RX1.14
     - Optional[:ref:`CE <hl7-v2_1-CE>`]
     - optional
     - 
     - DRUG ID: Item #473 | Table HL70057
   * - ``rx1_15``
     - RX1.15
     - Optional[List[str]]
     - optional
     - 
     - COMPONENT DRUG IDS: Item #474
   * - ``rx1_16``
     - RX1.16
     - Optional[str]
     - optional
     - 
     - PRESCRIPTION TYPE: Item #479
   * - ``rx1_17``
     - RX1.17
     - Optional[str]
     - optional
     - 
     - SUBSTITUTION STATUS: Item #480
   * - ``rx1_18``
     - RX1.18
     - Optional[str]
     - optional
     - 
     - RX ORDER STATUS: Item #588 | Table HL70038
   * - ``rx1_19``
     - RX1.19
     - Optional[str]
     - optional
     - 
     - NUMBER OF REFILLS: Item #481
   * - ``rx1_20``
     - RX1.20
     - Optional[str]
     - optional
     - 
     - UNUSED: Item #773
   * - ``rx1_21``
     - RX1.21
     - Optional[str]
     - optional
     - 
     - REFILLS REMAINING: Item #482
   * - ``rx1_22``
     - RX1.22
     - Optional[str]
     - optional
     - 
     - DEA CLASS: Item #619
   * - ``rx1_23``
     - RX1.23
     - Optional[str]
     - optional
     - 
     - ORDERING MD'S DEA NUMBER: Item #620
   * - ``rx1_24``
     - RX1.24
     - Optional[str]
     - optional
     - 
     - UNUSED: Item #774
   * - ``rx1_25``
     - RX1.25
     - Optional[str]
     - optional
     - 
     - LAST REFILL DATE/TIME: Item #483
   * - ``rx1_26``
     - RX1.26
     - Optional[str]
     - optional
     - 
     - RX NUMBER: Item #596
   * - ``rx1_27``
     - RX1.27
     - Optional[str]
     - optional
     - 
     - PRN STATUS: Item #621
   * - ``rx1_28``
     - RX1.28
     - Optional[List[str]]
     - optional
     - 
     - PHARMACY INSTRUCTIONS: Item #484
   * - ``rx1_29``
     - RX1.29
     - Optional[List[str]]
     - optional
     - 
     - PATIENT INSTRUCTIONS: Item #489
   * - ``rx1_30``
     - RX1.30
     - Optional[List[str]]
     - optional
     - 
     - INSTRUCTIONS (SIG): Item #618

.. _hl7-v2_1-UB1:

.. py:class:: hl7types.hl7.v2_1.segments.UB1.UB1
   :noindex:

   HL7 v2 UB1 segment.

UB1
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ub1_1``
     - UB1.1
     - Optional[str]
     - optional
     - 
     - SET ID - UB82: Item #459
   * - ``ub1_2``
     - UB1.2
     - Optional[str]
     - optional
     - 
     - BLOOD DEDUCTIBLE: Item #279
   * - ``ub1_3``
     - UB1.3
     - Optional[str]
     - optional
     - 
     - BLOOD FURN.-PINTS OF (40): Item #396
   * - ``ub1_4``
     - UB1.4
     - Optional[str]
     - optional
     - 
     - BLOOD REPLACED-PINTS (41): Item #397
   * - ``ub1_5``
     - UB1.5
     - Optional[str]
     - optional
     - 
     - BLOOD NOT RPLCD-PINTS(42): Item #398
   * - ``ub1_6``
     - UB1.6
     - Optional[str]
     - optional
     - 
     - CO-INSURANCE DAYS (25): Item #399
   * - ``ub1_7``
     - UB1.7
     - Optional[List[str]]
     - optional
     - 
     - CONDITION CODE: Item #400 | Table HL70043
   * - ``ub1_8``
     - UB1.8
     - Optional[str]
     - optional
     - 
     - COVERED DAYS - (23): Item #405
   * - ``ub1_9``
     - UB1.9
     - Optional[str]
     - optional
     - 
     - NON COVERED DAYS - (24): Item #406
   * - ``ub1_10``
     - UB1.10
     - Optional[List[str]]
     - optional
     - 
     - VALUE AMOUNT & CODE: Item #407
   * - ``ub1_11``
     - UB1.11
     - Optional[str]
     - optional
     - 
     - NUMBER OF GRACE DAYS (90): Item #424
   * - ``ub1_12``
     - UB1.12
     - Optional[str]
     - optional
     - 
     - SPEC. PROG. INDICATOR(44): Item #425
   * - ``ub1_13``
     - UB1.13
     - Optional[str]
     - optional
     - 
     - PSRO/UR APPROVAL IND. (87): Item #426
   * - ``ub1_14``
     - UB1.14
     - Optional[str]
     - optional
     - 
     - PSRO/UR APRVD STAY-FM(88): Item #427
   * - ``ub1_15``
     - UB1.15
     - Optional[str]
     - optional
     - 
     - PSRO/UR APRVD STAY-TO(89): Item #428
   * - ``ub1_16``
     - UB1.16
     - Optional[List[str]]
     - optional
     - 
     - OCCURRENCE (28-32): Item #429
   * - ``ub1_17``
     - UB1.17
     - Optional[str]
     - optional
     - 
     - OCCURRENCE SPAN (33): Item #435
   * - ``ub1_18``
     - UB1.18
     - Optional[str]
     - optional
     - 
     - OCCURRENCE SPAN START DATE(33): Item #446
   * - ``ub1_19``
     - UB1.19
     - Optional[str]
     - optional
     - 
     - OCCUR. SPAN END DATE (33): Item #447
   * - ``ub1_20``
     - UB1.20
     - Optional[str]
     - optional
     - 
     - UB-82 LOCATOR 2: Item #448
   * - ``ub1_21``
     - UB1.21
     - Optional[str]
     - optional
     - 
     - UB-82 LOCATOR 9: Item #449
   * - ``ub1_22``
     - UB1.22
     - Optional[str]
     - optional
     - 
     - UB-82 LOCATOR 27: Item #450
   * - ``ub1_23``
     - UB1.23
     - Optional[str]
     - optional
     - 
     - UB-82 LOCATOR 45: Item #451

.. _hl7-v2_1-URD:

.. py:class:: hl7types.hl7.v2_1.segments.URD.URD
   :noindex:

   HL7 v2 URD segment.

URD
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``urd_1``
     - URD.1
     - Optional[str]
     - optional
     - 
     - R/U DATE/TIME: Item #600
   * - ``urd_2``
     - URD.2
     - Optional[str]
     - optional
     - 
     - REPORT PRIORITY: Item #601 | Table HL70109
   * - ``urd_3``
     - URD.3
     - List[str]
     - required
     - 
     - R/U WHO SUBJECT DEFINITION: Item #602
   * - ``urd_4``
     - URD.4
     - Optional[List[str]]
     - optional
     - 
     - R/U WHAT SUBJECT DEFINITION: Item #603 | Table HL70048
   * - ``urd_5``
     - URD.5
     - Optional[List[str]]
     - optional
     - 
     - R/U WHAT DEPARTMENT CODE: Item #605
   * - ``urd_6``
     - URD.6
     - Optional[List[str]]
     - optional
     - 
     - R/U DISPLAY/PRINT LOCATIONS: Item #607
   * - ``urd_7``
     - URD.7
     - Optional[str]
     - optional
     - 
     - R/U RESULTS LEVEL: Item #702 | Table HL70108

.. _hl7-v2_1-URS:

.. py:class:: hl7types.hl7.v2_1.segments.URS.URS
   :noindex:

   HL7 v2 URS segment.

URS
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``urs_1``
     - URS.1
     - List[str]
     - required
     - 
     - R/U WHERE SUBJECT DEFINITION: Item #608
   * - ``urs_2``
     - URS.2
     - Optional[str]
     - optional
     - 
     - R/U WHEN DATA START DATE/TIME: Item #609
   * - ``urs_3``
     - URS.3
     - Optional[str]
     - optional
     - 
     - R/U WHEN DATA END DATE/TIME: Item #610
   * - ``urs_4``
     - URS.4
     - Optional[List[str]]
     - optional
     - 
     - R/U WHAT USER QUALIFIER: Item #611
   * - ``urs_5``
     - URS.5
     - Optional[List[str]]
     - optional
     - 
     - R/U OTHER RESULTS SUBJECT DEFINI: Item #612
