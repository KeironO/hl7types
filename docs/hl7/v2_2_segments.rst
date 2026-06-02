v2.2 Segments
=============

.. _hl7-v2_2-ACC:

.. py:class:: hl7types.hl7.v2_2.segments.ACC.ACC
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
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Accident date / time: Item #527
   * - ``acc_2``
     - ACC.2
     - Optional[str]
     - optional
     -
     - Accident code: Item #528 | Table HL70050
   * - ``acc_3``
     - ACC.3
     - Optional[str]
     - optional
     -
     - Accident location: Item #529

.. _hl7-v2_2-ADD:

.. py:class:: hl7types.hl7.v2_2.segments.ADD.ADD
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
     - Addendum Continuation Pointer: Item #66

.. _hl7-v2_2-AL1:

.. py:class:: hl7types.hl7.v2_2.segments.AL1.AL1
   :noindex:

   HL7 v2 AL1 segment.

AL1
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
   * - ``al1_1``
     - AL1.1
     - str
     - required
     -
     - Set ID - Allergy: Item #203
   * - ``al1_2``
     - AL1.2
     - Optional[str]
     - optional
     -
     - Allergy Type: Item #204 | Table HL70127
   * - ``al1_3``
     - AL1.3
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Allergy code / mnemonic / description: Item #205
   * - ``al1_4``
     - AL1.4
     - Optional[str]
     - optional
     -
     - Allergy Severity: Item #206 | Table HL70128
   * - ``al1_5``
     - AL1.5
     - Optional[str]
     - optional
     -
     - Allergy Reaction: Item #207
   * - ``al1_6``
     - AL1.6
     - Optional[str]
     - optional
     -
     - Identification Date: Item #208

.. _hl7-v2_2-BHS:

.. py:class:: hl7types.hl7.v2_2.segments.BHS.BHS
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
     - Batch Field Separator: Item #81
   * - ``bhs_2``
     - BHS.2
     - str
     - optional
     -
     - Batch Encoding Characters: Item #82
   * - ``bhs_3``
     - BHS.3
     - Optional[str]
     - optional
     -
     - Batch Sending Application: Item #83
   * - ``bhs_4``
     - BHS.4
     - Optional[str]
     - optional
     -
     - Batch Sending Facility: Item #84
   * - ``bhs_5``
     - BHS.5
     - Optional[str]
     - optional
     -
     - Batch Receiving Application: Item #85
   * - ``bhs_6``
     - BHS.6
     - Optional[str]
     - optional
     -
     - Batch Receiving Facility: Item #86
   * - ``bhs_7``
     - BHS.7
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Batch creation date / time: Item #87
   * - ``bhs_8``
     - BHS.8
     - Optional[str]
     - optional
     -
     - Batch Security: Item #88
   * - ``bhs_9``
     - BHS.9
     - Optional[str]
     - optional
     -
     - Batch name / ID / type: Item #89
   * - ``bhs_10``
     - BHS.10
     - Optional[str]
     - optional
     -
     - Batch Comment: Item #90
   * - ``bhs_11``
     - BHS.11
     - Optional[str]
     - optional
     -
     - Batch Control ID: Item #91
   * - ``bhs_12``
     - BHS.12
     - Optional[str]
     - optional
     -
     - Reference Batch Control ID: Item #92

.. _hl7-v2_2-BLG:

.. py:class:: hl7types.hl7.v2_2.segments.BLG.BLG
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
     - When to Charge: Item #234 | Table HL70100
   * - ``blg_2``
     - BLG.2
     - Optional[str]
     - optional
     -
     - Charge Type: Item #235 | Table HL70122
   * - ``blg_3``
     - BLG.3
     - Optional[str]
     - optional
     -
     - Account ID: Item #236

.. _hl7-v2_2-BTS:

.. py:class:: hl7types.hl7.v2_2.segments.BTS.BTS
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
     - Batch Message Count: Item #93
   * - ``bts_2``
     - BTS.2
     - Optional[str]
     - optional
     -
     - Batch Comment: Item #94
   * - ``bts_3``
     - BTS.3
     - Optional[List[str]]
     - optional
     -
     - Batch Totals: Item #95

.. _hl7-v2_2-DG1:

.. py:class:: hl7types.hl7.v2_2.segments.DG1.DG1
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
     - Set ID - diagnosis: Item #375
   * - ``dg1_2``
     - DG1.2
     - str
     - required
     -
     - Diagnosis coding method: Item #376 | Table HL70053
   * - ``dg1_3``
     - DG1.3
     - Optional[str]
     - optional
     -
     - Diagnosis code: Item #377 | Table HL70051
   * - ``dg1_4``
     - DG1.4
     - Optional[str]
     - optional
     -
     - Diagnosis description: Item #378
   * - ``dg1_5``
     - DG1.5
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Diagnosis date / time: Item #379
   * - ``dg1_6``
     - DG1.6
     - str
     - required
     -
     - Diagnosis / DRG type: Item #380 | Table HL70052
   * - ``dg1_7``
     - DG1.7
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Major diagnostic category: Item #381 | Table HL70118
   * - ``dg1_8``
     - DG1.8
     - Optional[str]
     - optional
     -
     - Diagnostic related group: Item #382 | Table HL70055
   * - ``dg1_9``
     - DG1.9
     - Optional[str]
     - optional
     -
     - DRG approval indicator: Item #383
   * - ``dg1_10``
     - DG1.10
     - Optional[str]
     - optional
     -
     - DRG grouper review code: Item #384 | Table HL70056
   * - ``dg1_11``
     - DG1.11
     - Optional[str]
     - optional
     -
     - Outlier type: Item #385 | Table HL70083
   * - ``dg1_12``
     - DG1.12
     - Optional[str]
     - optional
     -
     - Outlier days: Item #386
   * - ``dg1_13``
     - DG1.13
     - Optional[str]
     - optional
     -
     - Outlier cost: Item #387
   * - ``dg1_14``
     - DG1.14
     - Optional[str]
     - optional
     -
     - Grouper version and type: Item #388
   * - ``dg1_15``
     - DG1.15
     - Optional[str]
     - optional
     -
     - Diagnosis / DRG priority: Item #389
   * - ``dg1_16``
     - DG1.16
     - Optional[str]
     - optional
     -
     - Diagnosing clinician: Item #390

.. _hl7-v2_2-DSC:

.. py:class:: hl7types.hl7.v2_2.segments.DSC.DSC
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
     - Continuation Pointer: Item #60

.. _hl7-v2_2-DSP:

.. py:class:: hl7types.hl7.v2_2.segments.DSP.DSP
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
     - Set ID - Display Data: Item #61
   * - ``dsp_2``
     - DSP.2
     - Optional[str]
     - optional
     -
     - Display Level: Item #62
   * - ``dsp_3``
     - DSP.3
     - :ref:`TX <hl7-v2_2-TX>`
     - required
     -
     - Data Line: Item #63
   * - ``dsp_4``
     - DSP.4
     - Optional[str]
     - optional
     -
     - Logical Break Point: Item #64
   * - ``dsp_5``
     - DSP.5
     - Optional[:ref:`TX <hl7-v2_2-TX>`]
     - optional
     -
     - Result ID: Item #65

.. _hl7-v2_2-ERR:

.. py:class:: hl7types.hl7.v2_2.segments.ERR.ERR
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
     - Error Code and Location: Item #24 | Table HL70060

.. _hl7-v2_2-EVN:

.. py:class:: hl7types.hl7.v2_2.segments.EVN.EVN
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
     - Event Type Code: Item #99 | Table HL70003
   * - ``evn_2``
     - EVN.2
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     -
     - Date / time of event: Item #100
   * - ``evn_3``
     - EVN.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Date / time planned event: Item #101
   * - ``evn_4``
     - EVN.4
     - Optional[str]
     - optional
     -
     - Event Reason Code: Item #102 | Table HL70062
   * - ``evn_5``
     - EVN.5
     - Optional[str]
     - optional
     -
     - Operator ID: Item #103 | Table HL70188

.. _hl7-v2_2-FHS:

.. py:class:: hl7types.hl7.v2_2.segments.FHS.FHS
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
     - File Field Separator: Item #67
   * - ``fhs_2``
     - FHS.2
     - str
     - optional
     -
     - File Encoding Characters: Item #68
   * - ``fhs_3``
     - FHS.3
     - Optional[str]
     - optional
     -
     - File Sending Application: Item #69
   * - ``fhs_4``
     - FHS.4
     - Optional[str]
     - optional
     -
     - File Sending Facility: Item #70
   * - ``fhs_5``
     - FHS.5
     - Optional[str]
     - optional
     -
     - File Receiving Application: Item #71
   * - ``fhs_6``
     - FHS.6
     - Optional[str]
     - optional
     -
     - File Receiving Facility: Item #72
   * - ``fhs_7``
     - FHS.7
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - File creation date / time: Item #73
   * - ``fhs_8``
     - FHS.8
     - Optional[str]
     - optional
     -
     - File Security: Item #74
   * - ``fhs_9``
     - FHS.9
     - Optional[str]
     - optional
     -
     - File name / ID: Item #75
   * - ``fhs_10``
     - FHS.10
     - Optional[str]
     - optional
     -
     - File Header Comment: Item #76
   * - ``fhs_11``
     - FHS.11
     - Optional[str]
     - optional
     -
     - File Control ID: Item #77
   * - ``fhs_12``
     - FHS.12
     - Optional[str]
     - optional
     -
     - Reference File Control ID: Item #78

.. _hl7-v2_2-FT1:

.. py:class:: hl7types.hl7.v2_2.segments.FT1.FT1
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
     - Set ID - financial transaction: Item #355
   * - ``ft1_2``
     - FT1.2
     - Optional[str]
     - optional
     -
     - Transaction ID: Item #356
   * - ``ft1_3``
     - FT1.3
     - Optional[str]
     - optional
     -
     - Transaction batch ID: Item #357
   * - ``ft1_4``
     - FT1.4
     - str
     - required
     -
     - Transaction date: Item #358
   * - ``ft1_5``
     - FT1.5
     - Optional[str]
     - optional
     -
     - Transaction posting date: Item #359
   * - ``ft1_6``
     - FT1.6
     - str
     - required
     -
     - Transaction type: Item #360 | Table HL70017
   * - ``ft1_7``
     - FT1.7
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Transaction code: Item #361 | Table HL70132
   * - ``ft1_8``
     - FT1.8
     - Optional[str]
     - optional
     -
     - Transaction description: Item #362
   * - ``ft1_9``
     - FT1.9
     - Optional[str]
     - optional
     -
     - Transaction description - alternate: Item #363
   * - ``ft1_10``
     - FT1.10
     - Optional[str]
     - optional
     -
     - Transaction quantity: Item #364
   * - ``ft1_11``
     - FT1.11
     - Optional[str]
     - optional
     -
     - Transaction amount - extended: Item #365
   * - ``ft1_12``
     - FT1.12
     - Optional[str]
     - optional
     -
     - Transaction amount - unit: Item #366
   * - ``ft1_13``
     - FT1.13
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Department code: Item #367 | Table HL70049
   * - ``ft1_14``
     - FT1.14
     - str
     - required
     -
     - Insurance plan ID: Item #368 | Table HL70072
   * - ``ft1_15``
     - FT1.15
     - Optional[str]
     - optional
     -
     - Insurance amount: Item #369
   * - ``ft1_16``
     - FT1.16
     - Optional[str]
     - optional
     -
     - Assigned Patient Location: Item #133 | Table HL70079
   * - ``ft1_17``
     - FT1.17
     - Optional[str]
     - optional
     -
     - Fee schedule: Item #370 | Table HL70024
   * - ``ft1_18``
     - FT1.18
     - Optional[str]
     - optional
     -
     - Patient type: Item #148 | Table HL70018
   * - ``ft1_19``
     - FT1.19
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Diagnosis code: Item #371 | Table HL70051
   * - ``ft1_20``
     - FT1.20
     - Optional[str]
     - optional
     -
     - Performed by code: Item #372 | Table HL70084
   * - ``ft1_21``
     - FT1.21
     - Optional[str]
     - optional
     -
     - Ordered by code: Item #373
   * - ``ft1_22``
     - FT1.22
     - Optional[str]
     - optional
     -
     - Unit cost: Item #374
   * - ``ft1_23``
     - FT1.23
     - Optional[str]
     - optional
     -
     - Filler Order Number: Item #217

.. _hl7-v2_2-FTS:

.. py:class:: hl7types.hl7.v2_2.segments.FTS.FTS
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
     - File Batch Count: Item #79
   * - ``fts_2``
     - FTS.2
     - Optional[str]
     - optional
     -
     - File Trailer Comment: Item #80

.. _hl7-v2_2-GT1:

.. py:class:: hl7types.hl7.v2_2.segments.GT1.GT1
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
     - Set ID - guarantor: Item #405
   * - ``gt1_2``
     - GT1.2
     - Optional[str]
     - optional
     -
     - Guarantor number: Item #406
   * - ``gt1_3``
     - GT1.3
     - :ref:`PN <hl7-v2_2-PN>`
     - required
     -
     - Guarantor name: Item #407
   * - ``gt1_4``
     - GT1.4
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     -
     - Guarantor spouse name: Item #408
   * - ``gt1_5``
     - GT1.5
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     -
     - Guarantor address: Item #409
   * - ``gt1_6``
     - GT1.6
     - Optional[List[str]]
     - optional
     -
     - Guarantor phone number - home: Item #410
   * - ``gt1_7``
     - GT1.7
     - Optional[List[str]]
     - optional
     -
     - Guarantor phone number - business: Item #411
   * - ``gt1_8``
     - GT1.8
     - Optional[str]
     - optional
     -
     - Guarantor date of birth: Item #412
   * - ``gt1_9``
     - GT1.9
     - Optional[str]
     - optional
     -
     - Guarantor sex: Item #413 | Table HL70001
   * - ``gt1_10``
     - GT1.10
     - Optional[str]
     - optional
     -
     - Guarantor type: Item #414 | Table HL70068
   * - ``gt1_11``
     - GT1.11
     - Optional[str]
     - optional
     -
     - Guarantor relationship: Item #415 | Table HL70063
   * - ``gt1_12``
     - GT1.12
     - Optional[str]
     - optional
     -
     - Guarantor social security number: Item #416
   * - ``gt1_13``
     - GT1.13
     - Optional[str]
     - optional
     -
     - Guarantor date - begin: Item #417
   * - ``gt1_14``
     - GT1.14
     - Optional[str]
     - optional
     -
     - Guarantor date - end: Item #418
   * - ``gt1_15``
     - GT1.15
     - Optional[str]
     - optional
     -
     - Guarantor priority: Item #419
   * - ``gt1_16``
     - GT1.16
     - Optional[str]
     - optional
     -
     - Guarantor employer name: Item #420
   * - ``gt1_17``
     - GT1.17
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     -
     - Guarantor employer address: Item #421
   * - ``gt1_18``
     - GT1.18
     - Optional[List[str]]
     - optional
     -
     - Guarantor employ phone number: Item #422
   * - ``gt1_19``
     - GT1.19
     - Optional[str]
     - optional
     -
     - Guarantor employee ID number: Item #423
   * - ``gt1_20``
     - GT1.20
     - Optional[str]
     - optional
     -
     - Guarantor employment status: Item #424 | Table HL70066
   * - ``gt1_21``
     - GT1.21
     - Optional[str]
     - optional
     -
     - Guarantor organization: Item #425

.. _hl7-v2_2-IN1:

.. py:class:: hl7types.hl7.v2_2.segments.IN1.IN1
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
     - Set ID - insurance: Item #426
   * - ``in1_2``
     - IN1.2
     - str
     - required
     -
     - Insurance plan ID: Item #368 | Table HL70072
   * - ``in1_3``
     - IN1.3
     - str
     - required
     -
     - Insurance company ID: Item #428
   * - ``in1_4``
     - IN1.4
     - Optional[str]
     - optional
     -
     - Insurance company name: Item #429
   * - ``in1_5``
     - IN1.5
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     -
     - Insurance company address: Item #430
   * - ``in1_6``
     - IN1.6
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     -
     - Insurance company contact pers: Item #431
   * - ``in1_7``
     - IN1.7
     - Optional[List[str]]
     - optional
     -
     - Insurance company phone number: Item #432
   * - ``in1_8``
     - IN1.8
     - Optional[str]
     - optional
     -
     - Group number: Item #433
   * - ``in1_9``
     - IN1.9
     - Optional[str]
     - optional
     -
     - Group name: Item #434
   * - ``in1_10``
     - IN1.10
     - Optional[str]
     - optional
     -
     - Insured's group employer ID: Item #435
   * - ``in1_11``
     - IN1.11
     - Optional[str]
     - optional
     -
     - Insured's group employer name: Item #436
   * - ``in1_12``
     - IN1.12
     - Optional[str]
     - optional
     -
     - Plan effective date: Item #437
   * - ``in1_13``
     - IN1.13
     - Optional[str]
     - optional
     -
     - Plan expiration date: Item #438
   * - ``in1_14``
     - IN1.14
     - Optional[str]
     - optional
     -
     - Authorization information: Item #439
   * - ``in1_15``
     - IN1.15
     - Optional[str]
     - optional
     -
     - Plan type: Item #440 | Table HL70086
   * - ``in1_16``
     - IN1.16
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     -
     - Name of insured: Item #441
   * - ``in1_17``
     - IN1.17
     - Optional[str]
     - optional
     -
     - Insured's relationship to patient: Item #442 | Table HL70063
   * - ``in1_18``
     - IN1.18
     - Optional[str]
     - optional
     -
     - Insured's date of birth: Item #443
   * - ``in1_19``
     - IN1.19
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     -
     - Insured's address: Item #444
   * - ``in1_20``
     - IN1.20
     - Optional[str]
     - optional
     -
     - Assignment of benefits: Item #445 | Table HL70135
   * - ``in1_21``
     - IN1.21
     - Optional[str]
     - optional
     -
     - Coordination of benefits: Item #446 | Table HL70173
   * - ``in1_22``
     - IN1.22
     - Optional[str]
     - optional
     -
     - Coordination of benefits - priority: Item #447
   * - ``in1_23``
     - IN1.23
     - Optional[str]
     - optional
     -
     - Notice of admission code: Item #448 | Table HL70136
   * - ``in1_24``
     - IN1.24
     - Optional[str]
     - optional
     -
     - Notice of admission date: Item #449
   * - ``in1_25``
     - IN1.25
     - Optional[str]
     - optional
     -
     - Report of eligibility code: Item #450
   * - ``in1_26``
     - IN1.26
     - Optional[str]
     - optional
     -
     - Report of eligibility date: Item #451
   * - ``in1_27``
     - IN1.27
     - Optional[str]
     - optional
     -
     - Release information code: Item #452 | Table HL70093
   * - ``in1_28``
     - IN1.28
     - Optional[str]
     - optional
     -
     - Pre-admit certification (PAC): Item #453
   * - ``in1_29``
     - IN1.29
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Verification date / time: Item #454
   * - ``in1_30``
     - IN1.30
     - Optional[str]
     - optional
     -
     - Verification by: Item #455
   * - ``in1_31``
     - IN1.31
     - Optional[str]
     - optional
     -
     - Type of agreement code: Item #456 | Table HL70098
   * - ``in1_32``
     - IN1.32
     - Optional[str]
     - optional
     -
     - Billing status: Item #457 | Table HL70022
   * - ``in1_33``
     - IN1.33
     - Optional[str]
     - optional
     -
     - Lifetime reserve days: Item #458
   * - ``in1_34``
     - IN1.34
     - Optional[str]
     - optional
     -
     - Delay before lifetime reserve days: Item #459
   * - ``in1_35``
     - IN1.35
     - Optional[str]
     - optional
     -
     - Company plan code: Item #460 | Table HL70042
   * - ``in1_36``
     - IN1.36
     - Optional[str]
     - optional
     -
     - Policy number: Item #461
   * - ``in1_37``
     - IN1.37
     - Optional[str]
     - optional
     -
     - Policy deductible: Item #462
   * - ``in1_38``
     - IN1.38
     - Optional[str]
     - optional
     -
     - Policy limit - amount: Item #463
   * - ``in1_39``
     - IN1.39
     - Optional[str]
     - optional
     -
     - Policy limit - days: Item #464
   * - ``in1_40``
     - IN1.40
     - Optional[str]
     - optional
     -
     - Room rate - semi-private: Item #465
   * - ``in1_41``
     - IN1.41
     - Optional[str]
     - optional
     -
     - Room rate - private: Item #466
   * - ``in1_42``
     - IN1.42
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Insured's employment status: Item #467 | Table HL70066
   * - ``in1_43``
     - IN1.43
     - Optional[str]
     - optional
     -
     - Insured's sex: Item #468 | Table HL70001
   * - ``in1_44``
     - IN1.44
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     -
     - Insured's employer address: Item #469
   * - ``in1_45``
     - IN1.45
     - Optional[str]
     - optional
     -
     - Verification status: Item #470
   * - ``in1_46``
     - IN1.46
     - Optional[str]
     - optional
     -
     - Prior insurance plan ID: Item #471 | Table HL70072

.. _hl7-v2_2-IN2:

.. py:class:: hl7types.hl7.v2_2.segments.IN2.IN2
   :noindex:

   HL7 v2 IN2 segment.

IN2
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
   * - ``in2_1``
     - IN2.1
     - Optional[str]
     - optional
     -
     - Insured's employee ID: Item #472
   * - ``in2_2``
     - IN2.2
     - Optional[str]
     - optional
     -
     - Insured's social security number: Item #473
   * - ``in2_3``
     - IN2.3
     - Optional[str]
     - optional
     -
     - Insured's employer name: Item #474
   * - ``in2_4``
     - IN2.4
     - Optional[str]
     - optional
     -
     - Employer information data: Item #475 | Table HL70139
   * - ``in2_5``
     - IN2.5
     - Optional[str]
     - optional
     -
     - Mail claim party: Item #476 | Table HL70137
   * - ``in2_6``
     - IN2.6
     - Optional[str]
     - optional
     -
     - Medicare health insurance card number: Item #477
   * - ``in2_7``
     - IN2.7
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     -
     - Medicaid case name: Item #478
   * - ``in2_8``
     - IN2.8
     - Optional[str]
     - optional
     -
     - Medicaid case number: Item #479
   * - ``in2_9``
     - IN2.9
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     -
     - Champus sponsor name: Item #480
   * - ``in2_10``
     - IN2.10
     - Optional[str]
     - optional
     -
     - Champus ID number: Item #481
   * - ``in2_11``
     - IN2.11
     - Optional[str]
     - optional
     -
     - Dependent of champus recipient: Item #482
   * - ``in2_12``
     - IN2.12
     - Optional[str]
     - optional
     -
     - Champus organization: Item #483
   * - ``in2_13``
     - IN2.13
     - Optional[str]
     - optional
     -
     - Champus station: Item #484
   * - ``in2_14``
     - IN2.14
     - Optional[str]
     - optional
     -
     - Champus service: Item #485 | Table HL70140
   * - ``in2_15``
     - IN2.15
     - Optional[str]
     - optional
     -
     - Champus rank / grade: Item #486 | Table HL70141
   * - ``in2_16``
     - IN2.16
     - Optional[str]
     - optional
     -
     - Champus status: Item #487 | Table HL70142
   * - ``in2_17``
     - IN2.17
     - Optional[str]
     - optional
     -
     - Champus retire date: Item #488
   * - ``in2_18``
     - IN2.18
     - Optional[str]
     - optional
     -
     - Champus non-availability certification on file: Item #489 | Table HL70136
   * - ``in2_19``
     - IN2.19
     - Optional[str]
     - optional
     -
     - Baby coverage: Item #490 | Table HL70136
   * - ``in2_20``
     - IN2.20
     - Optional[str]
     - optional
     -
     - Combine baby bill: Item #491 | Table HL70136
   * - ``in2_21``
     - IN2.21
     - Optional[str]
     - optional
     -
     - Blood deductible: Item #531
   * - ``in2_22``
     - IN2.22
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     -
     - Special coverage approval name: Item #493
   * - ``in2_23``
     - IN2.23
     - Optional[str]
     - optional
     -
     - Special coverage approval title: Item #494
   * - ``in2_24``
     - IN2.24
     - Optional[List[str]]
     - optional
     -
     - Non-covered insurance code: Item #495 | Table HL70143
   * - ``in2_25``
     - IN2.25
     - Optional[str]
     - optional
     -
     - Payor ID: Item #496
   * - ``in2_26``
     - IN2.26
     - Optional[str]
     - optional
     -
     - Payor subscriber ID: Item #497
   * - ``in2_27``
     - IN2.27
     - Optional[str]
     - optional
     -
     - Eligibility source: Item #498 | Table HL70144
   * - ``in2_28``
     - IN2.28
     - Optional[List[str]]
     - optional
     -
     - Room coverage type / amount: Item #499 | Table HL70145
   * - ``in2_29``
     - IN2.29
     - Optional[List[str]]
     - optional
     -
     - Policy type / amount: Item #500 | Table HL70147
   * - ``in2_30``
     - IN2.30
     - Optional[str]
     - optional
     -
     - Daily deductible: Item #501

.. _hl7-v2_2-IN3:

.. py:class:: hl7types.hl7.v2_2.segments.IN3.IN3
   :noindex:

   HL7 v2 IN3 segment.

IN3
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
   * - ``in3_1``
     - IN3.1
     - str
     - required
     -
     - Set ID - insurance certification: Item #502
   * - ``in3_2``
     - IN3.2
     - Optional[str]
     - optional
     -
     - Certification number: Item #503
   * - ``in3_3``
     - IN3.3
     - Optional[str]
     - optional
     -
     - Certified by: Item #504
   * - ``in3_4``
     - IN3.4
     - Optional[str]
     - optional
     -
     - Certification required: Item #505 | Table HL70136
   * - ``in3_5``
     - IN3.5
     - Optional[str]
     - optional
     -
     - Penalty: Item #506 | Table HL70148
   * - ``in3_6``
     - IN3.6
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Certification date / time: Item #507
   * - ``in3_7``
     - IN3.7
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Certification modify date / time: Item #508
   * - ``in3_8``
     - IN3.8
     - Optional[str]
     - optional
     -
     - Operator: Item #509
   * - ``in3_9``
     - IN3.9
     - Optional[str]
     - optional
     -
     - Certification begin date: Item #510
   * - ``in3_10``
     - IN3.10
     - Optional[str]
     - optional
     -
     - Certification end date: Item #511
   * - ``in3_11``
     - IN3.11
     - Optional[str]
     - optional
     -
     - Days: Item #512 | Table HL70149
   * - ``in3_12``
     - IN3.12
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Non-concur code / description: Item #513
   * - ``in3_13``
     - IN3.13
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Non-concur effective date / time: Item #514
   * - ``in3_14``
     - IN3.14
     - Optional[str]
     - optional
     -
     - Physician reviewer: Item #515
   * - ``in3_15``
     - IN3.15
     - Optional[str]
     - optional
     -
     - Certification contact: Item #516
   * - ``in3_16``
     - IN3.16
     - Optional[List[str]]
     - optional
     -
     - Certification contact phone number: Item #517
   * - ``in3_17``
     - IN3.17
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Appeal reason: Item #518
   * - ``in3_18``
     - IN3.18
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Certification agency: Item #519
   * - ``in3_19``
     - IN3.19
     - Optional[List[str]]
     - optional
     -
     - Certification agency phone number: Item #520
   * - ``in3_20``
     - IN3.20
     - Optional[List[str]]
     - optional
     -
     - Pre-certification required / window: Item #521 | Table HL70150
   * - ``in3_21``
     - IN3.21
     - Optional[str]
     - optional
     -
     - Case manager: Item #522
   * - ``in3_22``
     - IN3.22
     - Optional[str]
     - optional
     -
     - Second opinion date: Item #523
   * - ``in3_23``
     - IN3.23
     - Optional[str]
     - optional
     -
     - Second opinion status: Item #524 | Table HL70151
   * - ``in3_24``
     - IN3.24
     - Optional[str]
     - optional
     -
     - Second opinion documentation received: Item #525 | Table HL70152
   * - ``in3_25``
     - IN3.25
     - Optional[str]
     - optional
     -
     - Second opinion practitioner: Item #526

.. _hl7-v2_2-MFA:

.. py:class:: hl7types.hl7.v2_2.segments.MFA.MFA
   :noindex:

   HL7 v2 MFA segment.

MFA
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
   * - ``mfa_1``
     - MFA.1
     - str
     - required
     -
     - Record-level event code: Item #664 | Table HL70180
   * - ``mfa_2``
     - MFA.2
     - Optional[str]
     - optional
     -
     - MFN control ID: Item #665
   * - ``mfa_3``
     - MFA.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Event completion date / time: Item #668
   * - ``mfa_4``
     - MFA.4
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Error return code and/or text: Item #669 | Table HL70181
   * - ``mfa_5``
     - MFA.5
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Primary key value: Item #667

.. _hl7-v2_2-MFE:

.. py:class:: hl7types.hl7.v2_2.segments.MFE.MFE
   :noindex:

   HL7 v2 MFE segment.

MFE
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
   * - ``mfe_1``
     - MFE.1
     - str
     - required
     -
     - Record-level event code: Item #664 | Table HL70180
   * - ``mfe_2``
     - MFE.2
     - Optional[str]
     - optional
     -
     - MFN control ID: Item #665
   * - ``mfe_3``
     - MFE.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Effective date / time: Item #662
   * - ``mfe_4``
     - MFE.4
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Primary key value: Item #667

.. _hl7-v2_2-MFI:

.. py:class:: hl7types.hl7.v2_2.segments.MFI.MFI
   :noindex:

   HL7 v2 MFI segment.

MFI
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
   * - ``mfi_1``
     - MFI.1
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Master file identifier: Item #658 | Table HL70175
   * - ``mfi_2``
     - MFI.2
     - Optional[str]
     - optional
     -
     - Master file application identifier: Item #659 | Table HL70176
   * - ``mfi_3``
     - MFI.3
     - str
     - required
     -
     - File-level event code: Item #660 | Table HL70178
   * - ``mfi_4``
     - MFI.4
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Entered date / time: Item #661
   * - ``mfi_5``
     - MFI.5
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Effective date / time: Item #662
   * - ``mfi_6``
     - MFI.6
     - str
     - required
     -
     - Response level code: Item #663 | Table HL70179

.. _hl7-v2_2-MRG:

.. py:class:: hl7types.hl7.v2_2.segments.MRG.MRG
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
     - Prior Patient ID - Internal: Item #211
   * - ``mrg_2``
     - MRG.2
     - Optional[str]
     - optional
     -
     - Prior Alternate Patient ID: Item #212
   * - ``mrg_3``
     - MRG.3
     - Optional[str]
     - optional
     -
     - Prior Patient Account Number: Item #213
   * - ``mrg_4``
     - MRG.4
     - Optional[str]
     - optional
     -
     - Prior Patient ID - External: Item #214

.. _hl7-v2_2-MSA:

.. py:class:: hl7types.hl7.v2_2.segments.MSA.MSA
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
     - Acknowledgement code: Item #18 | Table HL70008
   * - ``msa_2``
     - MSA.2
     - str
     - required
     -
     - Message Control ID: Item #10
   * - ``msa_3``
     - MSA.3
     - Optional[str]
     - optional
     -
     - Text Message: Item #20
   * - ``msa_4``
     - MSA.4
     - Optional[str]
     - optional
     -
     - Expected Sequence Number: Item #21
   * - ``msa_5``
     - MSA.5
     - Optional[str]
     - optional
     -
     - Delayed Acknowledgement type: Item #22 | Table HL70102
   * - ``msa_6``
     - MSA.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Error Condition: Item #23

.. _hl7-v2_2-MSH:

.. py:class:: hl7types.hl7.v2_2.segments.MSH.MSH
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
     - Field separator: Item #1
   * - ``msh_2``
     - MSH.2
     - str
     - optional
     -
     - Encoding characters: Item #2
   * - ``msh_3``
     - MSH.3
     - Optional[str]
     - optional
     -
     - Sending application: Item #3
   * - ``msh_4``
     - MSH.4
     - Optional[str]
     - optional
     -
     - Sending facility: Item #4
   * - ``msh_5``
     - MSH.5
     - Optional[str]
     - optional
     -
     - Receiving application: Item #5
   * - ``msh_6``
     - MSH.6
     - Optional[str]
     - optional
     -
     - Receiving facility: Item #6
   * - ``msh_7``
     - MSH.7
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Date / Time of message: Item #7
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
     - Message type: Item #9 | Table HL70076
   * - ``msh_10``
     - MSH.10
     - str
     - required
     -
     - Message Control ID: Item #10
   * - ``msh_11``
     - MSH.11
     - str
     - required
     -
     - Processing ID: Item #11 | Table HL70103
   * - ``msh_12``
     - MSH.12
     - str
     - required
     -
     - Version ID: Item #12 | Table HL70104
   * - ``msh_13``
     - MSH.13
     - Optional[str]
     - optional
     -
     - Sequence number: Item #13
   * - ``msh_14``
     - MSH.14
     - Optional[str]
     - optional
     -
     - Continuation pointer: Item #14
   * - ``msh_15``
     - MSH.15
     - Optional[str]
     - optional
     -
     - Accept acknowledgement type: Item #15 | Table HL70155
   * - ``msh_16``
     - MSH.16
     - Optional[str]
     - optional
     -
     - Application acknowledgement type: Item #16 | Table HL70155
   * - ``msh_17``
     - MSH.17
     - Optional[str]
     - optional
     -
     - Country code: Item #17

.. _hl7-v2_2-NCK:

.. py:class:: hl7types.hl7.v2_2.segments.NCK.NCK
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
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     -
     - System Date/Time: Item #742

.. _hl7-v2_2-NK1:

.. py:class:: hl7types.hl7.v2_2.segments.NK1.NK1
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
     - Set ID - Next of Kin: Item #190
   * - ``nk1_2``
     - NK1.2
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     -
     - Name: Item #191
   * - ``nk1_3``
     - NK1.3
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Relationship: Item #192 | Table HL70063
   * - ``nk1_4``
     - NK1.4
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     -
     - Address: Item #193
   * - ``nk1_5``
     - NK1.5
     - Optional[List[str]]
     - optional
     -
     - Phone Number: Item #194
   * - ``nk1_6``
     - NK1.6
     - Optional[str]
     - optional
     -
     - Business Phone Number: Item #195
   * - ``nk1_7``
     - NK1.7
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Contact Role: Item #196 | Table HL70131
   * - ``nk1_8``
     - NK1.8
     - Optional[str]
     - optional
     -
     - Start Date: Item #197
   * - ``nk1_9``
     - NK1.9
     - Optional[str]
     - optional
     -
     - End Date: Item #198
   * - ``nk1_10``
     - NK1.10
     - Optional[str]
     - optional
     -
     - Next of Kin: Item #199
   * - ``nk1_11``
     - NK1.11
     - Optional[str]
     - optional
     -
     - Next of kin job code / class: Item #200
   * - ``nk1_12``
     - NK1.12
     - Optional[str]
     - optional
     -
     - Next of Kin Employee Number: Item #201
   * - ``nk1_13``
     - NK1.13
     - Optional[str]
     - optional
     -
     - Organization Name: Item #202

.. _hl7-v2_2-NPU:

.. py:class:: hl7types.hl7.v2_2.segments.NPU.NPU
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
     - Bed Location: Item #209 | Table HL70079
   * - ``npu_2``
     - NPU.2
     - Optional[str]
     - optional
     -
     - Bed Status: Item #170 | Table HL70116

.. _hl7-v2_2-NSC:

.. py:class:: hl7types.hl7.v2_2.segments.NSC.NSC
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
     - Network Change Type: Item #758
   * - ``nsc_2``
     - NSC.2
     - Optional[str]
     - optional
     -
     - Current CPU: Item #759
   * - ``nsc_3``
     - NSC.3
     - Optional[str]
     - optional
     -
     - Current Fileserver: Item #760
   * - ``nsc_4``
     - NSC.4
     - Optional[str]
     - optional
     -
     - Current Application: Item #761
   * - ``nsc_5``
     - NSC.5
     - Optional[str]
     - optional
     -
     - Current Facility: Item #762
   * - ``nsc_6``
     - NSC.6
     - Optional[str]
     - optional
     -
     - New CPU: Item #763
   * - ``nsc_7``
     - NSC.7
     - Optional[str]
     - optional
     -
     - New Fileserver: Item #764
   * - ``nsc_8``
     - NSC.8
     - Optional[str]
     - optional
     -
     - New Application: Item #765
   * - ``nsc_9``
     - NSC.9
     - Optional[str]
     - optional
     -
     - New Facility: Item #766

.. _hl7-v2_2-NST:

.. py:class:: hl7types.hl7.v2_2.segments.NST.NST
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
     - Statistics Available: Item #743 | Table HL70136
   * - ``nst_2``
     - NST.2
     - Optional[str]
     - optional
     -
     - Source Identifier: Item #744
   * - ``nst_3``
     - NST.3
     - Optional[str]
     - optional
     -
     - Source Type: Item #745
   * - ``nst_4``
     - NST.4
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Statistics Start: Item #746
   * - ``nst_5``
     - NST.5
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Statistics End: Item #747
   * - ``nst_6``
     - NST.6
     - Optional[str]
     - optional
     -
     - Receive Character Count: Item #748
   * - ``nst_7``
     - NST.7
     - Optional[str]
     - optional
     -
     - Send Character Count: Item #749
   * - ``nst_8``
     - NST.8
     - Optional[str]
     - optional
     -
     - Message Received: Item #750
   * - ``nst_9``
     - NST.9
     - Optional[str]
     - optional
     -
     - Message Sent: Item #751
   * - ``nst_10``
     - NST.10
     - Optional[str]
     - optional
     -
     - Checksum Errors Received: Item #752
   * - ``nst_11``
     - NST.11
     - Optional[str]
     - optional
     -
     - Length Errors Received: Item #753
   * - ``nst_12``
     - NST.12
     - Optional[str]
     - optional
     -
     - Other Errors Received: Item #754
   * - ``nst_13``
     - NST.13
     - Optional[str]
     - optional
     -
     - Connect Timeouts: Item #755
   * - ``nst_14``
     - NST.14
     - Optional[str]
     - optional
     -
     - Receive Timeouts: Item #756
   * - ``nst_15``
     - NST.15
     - Optional[str]
     - optional
     -
     - Network Errors: Item #757

.. _hl7-v2_2-NTE:

.. py:class:: hl7types.hl7.v2_2.segments.NTE.NTE
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
     - Set ID - Notes and Comments: Item #96
   * - ``nte_2``
     - NTE.2
     - Optional[str]
     - optional
     -
     - Source of Comment: Item #97 | Table HL70105
   * - ``nte_3``
     - NTE.3
     - Optional[List[:ref:`FT <hl7-v2_2-FT>`]]
     - optional
     -
     - Comment: Item #98

.. _hl7-v2_2-OBR:

.. py:class:: hl7types.hl7.v2_2.segments.OBR.OBR
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
     - Set ID - Observation Request: Item #237
   * - ``obr_2``
     - OBR.2
     - Optional[str]
     - optional
     -
     - Placer Order Number: Item #216
   * - ``obr_3``
     - OBR.3
     - Optional[str]
     - optional
     -
     - Filler Order Number: Item #217
   * - ``obr_4``
     - OBR.4
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Universal Service ID: Item #238
   * - ``obr_5``
     - OBR.5
     - Optional[str]
     - optional
     -
     - Priority (not used): Item #239
   * - ``obr_6``
     - OBR.6
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Requested date / time (not used): Item #240
   * - ``obr_7``
     - OBR.7
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Observation date / time: Item #241
   * - ``obr_8``
     - OBR.8
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Observation end date / time: Item #242
   * - ``obr_9``
     - OBR.9
     - Optional[str]
     - optional
     -
     - Collection Volume: Item #243
   * - ``obr_10``
     - OBR.10
     - Optional[List[str]]
     - optional
     -
     - Collector Identifier: Item #244
   * - ``obr_11``
     - OBR.11
     - Optional[str]
     - optional
     -
     - Specimen action code: Item #245 | Table HL70065
   * - ``obr_12``
     - OBR.12
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Danger Code: Item #246
   * - ``obr_13``
     - OBR.13
     - Optional[str]
     - optional
     -
     - Relevant clinical information: Item #247
   * - ``obr_14``
     - OBR.14
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Specimen received date / time: Item #248
   * - ``obr_15``
     - OBR.15
     - Optional[str]
     - optional
     -
     - Specimen source: Item #249 | Table HL70070
   * - ``obr_16``
     - OBR.16
     - Optional[str]
     - optional
     -
     - Ordering Provider: Item #226
   * - ``obr_17``
     - OBR.17
     - Optional[List[str]]
     - optional
     -
     - Order Callback Phone Number: Item #250
   * - ``obr_18``
     - OBR.18
     - Optional[str]
     - optional
     -
     - Placer field 1: Item #251
   * - ``obr_19``
     - OBR.19
     - Optional[str]
     - optional
     -
     - Placer field 2: Item #252
   * - ``obr_20``
     - OBR.20
     - Optional[str]
     - optional
     -
     - Filler Field 1: Item #253
   * - ``obr_21``
     - OBR.21
     - Optional[str]
     - optional
     -
     - Filler Field 2: Item #254
   * - ``obr_22``
     - OBR.22
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Results report / status change - date / time: Item #255
   * - ``obr_23``
     - OBR.23
     - Optional[str]
     - optional
     -
     - Charge to Practice: Item #256
   * - ``obr_24``
     - OBR.24
     - Optional[str]
     - optional
     -
     - Diagnostic service section ID: Item #257 | Table HL70074
   * - ``obr_25``
     - OBR.25
     - Optional[str]
     - optional
     -
     - Result Status: Item #258 | Table HL70123
   * - ``obr_26``
     - OBR.26
     - Optional[str]
     - optional
     -
     - Parent Result: Item #259
   * - ``obr_27``
     - OBR.27
     - Optional[List[:ref:`TQ <hl7-v2_2-TQ>`]]
     - optional
     -
     - Quantity / timing: Item #221
   * - ``obr_28``
     - OBR.28
     - Optional[List[str]]
     - optional
     -
     - Result Copies To: Item #260
   * - ``obr_29``
     - OBR.29
     - Optional[str]
     - optional
     -
     - Parent Number: Item #261
   * - ``obr_30``
     - OBR.30
     - Optional[str]
     - optional
     -
     - Transportation Mode: Item #262 | Table HL70124
   * - ``obr_31``
     - OBR.31
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Reason for Study: Item #263
   * - ``obr_32``
     - OBR.32
     - Optional[str]
     - optional
     -
     - Principal Result Interpreter: Item #264
   * - ``obr_33``
     - OBR.33
     - Optional[List[str]]
     - optional
     -
     - Assistant Result Interpreter: Item #265
   * - ``obr_34``
     - OBR.34
     - Optional[List[str]]
     - optional
     -
     - Technician: Item #266
   * - ``obr_35``
     - OBR.35
     - Optional[List[str]]
     - optional
     -
     - Transcriptionist: Item #267
   * - ``obr_36``
     - OBR.36
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Scheduled date / time: Item #268

.. _hl7-v2_2-OBX:

.. py:class:: hl7types.hl7.v2_2.segments.OBX.OBX
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
     - Set ID - Observational Simple: Item #569
   * - ``obx_2``
     - OBX.2
     - str
     - required
     -
     - Value Type: Item #570 | Table HL70125
   * - ``obx_3``
     - OBX.3
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Observation Identifier: Item #571
   * - ``obx_4``
     - OBX.4
     - Optional[str]
     - optional
     -
     - Observation Sub-ID: Item #572
   * - ``obx_5``
     - OBX.5
     - Optional[str]
     - optional
     -
     - Observation Value: Item #573
   * - ``obx_6``
     - OBX.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Units: Item #574
   * - ``obx_7``
     - OBX.7
     - Optional[str]
     - optional
     -
     - References Range: Item #575
   * - ``obx_8``
     - OBX.8
     - Optional[List[str]]
     - optional
     -
     - Abnormal Flags: Item #576 | Table HL70078
   * - ``obx_9``
     - OBX.9
     - Optional[str]
     - optional
     -
     - Probability: Item #577
   * - ``obx_10``
     - OBX.10
     - Optional[str]
     - optional
     -
     - Nature of Abnormal Test: Item #578 | Table HL70080
   * - ``obx_11``
     - OBX.11
     - str
     - required
     -
     - Observation result status: Item #579 | Table HL70085
   * - ``obx_12``
     - OBX.12
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Effective date last observation normal values: Item #580
   * - ``obx_13``
     - OBX.13
     - Optional[str]
     - optional
     -
     - User Defined Access Checks: Item #581
   * - ``obx_14``
     - OBX.14
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Date / time of the observation: Item #582
   * - ``obx_15``
     - OBX.15
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Producer's ID: Item #583
   * - ``obx_16``
     - OBX.16
     - Optional[str]
     - optional
     -
     - Responsible Observer: Item #584

.. _hl7-v2_2-ODS:

.. py:class:: hl7types.hl7.v2_2.segments.ODS.ODS
   :noindex:

   HL7 v2 ODS segment.

ODS
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
   * - ``ods_1``
     - ODS.1
     - str
     - required
     -
     - Type: Item #269 | Table HL70159
   * - ``ods_2``
     - ODS.2
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Service Period: Item #270
   * - ``ods_3``
     - ODS.3
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Diet, Supplement, or Preference Code: Item #271
   * - ``ods_4``
     - ODS.4
     - Optional[List[str]]
     - optional
     -
     - Text Instruction: Item #272

.. _hl7-v2_2-ODT:

.. py:class:: hl7types.hl7.v2_2.segments.ODT.ODT
   :noindex:

   HL7 v2 ODT segment.

ODT
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
   * - ``odt_1``
     - ODT.1
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Tray Type: Item #273 | Table HL70160
   * - ``odt_2``
     - ODT.2
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Service Period: Item #270
   * - ``odt_3``
     - ODT.3
     - Optional[List[str]]
     - optional
     -
     - Text Instruction: Item #272

.. _hl7-v2_2-OM1:

.. py:class:: hl7types.hl7.v2_2.segments.OM1.OM1
   :noindex:

   HL7 v2 OM1 segment.

OM1
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
   * - ``om1_1``
     - OM1.1
     - Optional[str]
     - optional
     -
     - Segment Type ID: Item #585
   * - ``om1_2``
     - OM1.2
     - Optional[str]
     - optional
     -
     - Sequence Number - Test/ Observation Master File: Item #586
   * - ``om1_3``
     - OM1.3
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Producer's test / observation ID: Item #587
   * - ``om1_4``
     - OM1.4
     - Optional[List[str]]
     - optional
     -
     - Permitted Data Types: Item #588 | Table HL70125
   * - ``om1_5``
     - OM1.5
     - str
     - required
     -
     - Specimen Required: Item #589 | Table HL70136
   * - ``om1_6``
     - OM1.6
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Producer ID: Item #590
   * - ``om1_7``
     - OM1.7
     - Optional[:ref:`TX <hl7-v2_2-TX>`]
     - optional
     -
     - Observation Description: Item #591
   * - ``om1_8``
     - OM1.8
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Other test / observation IDs for the observation: Item #592
   * - ``om1_9``
     - OM1.9
     - List[str]
     - required
     -
     - Other Names: Item #593
   * - ``om1_10``
     - OM1.10
     - Optional[str]
     - optional
     -
     - Preferred Report Name for the Observation: Item #594
   * - ``om1_11``
     - OM1.11
     - Optional[str]
     - optional
     -
     - Preferred Short Name or Mnemonic for Observation: Item #595
   * - ``om1_12``
     - OM1.12
     - Optional[str]
     - optional
     -
     - Preferred Long Name for the Observation: Item #596
   * - ``om1_13``
     - OM1.13
     - Optional[str]
     - optional
     -
     - Orderability: Item #597 | Table HL70136
   * - ``om1_14``
     - OM1.14
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Identity of instrument used to perform this study: Item #598
   * - ``om1_15``
     - OM1.15
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Coded Representation of Method: Item #599
   * - ``om1_16``
     - OM1.16
     - Optional[str]
     - optional
     -
     - Portable: Item #600 | Table HL70136
   * - ``om1_17``
     - OM1.17
     - Optional[List[str]]
     - optional
     -
     - Observation producing department / section: Item #601
   * - ``om1_18``
     - OM1.18
     - Optional[str]
     - optional
     -
     - Telephone Number of Section: Item #602
   * - ``om1_19``
     - OM1.19
     - str
     - required
     -
     - Nature of test / observation: Item #603 | Table HL70174
   * - ``om1_20``
     - OM1.20
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Report Subheader: Item #604
   * - ``om1_21``
     - OM1.21
     - Optional[str]
     - optional
     -
     - Report Display Order: Item #605
   * - ``om1_22``
     - OM1.22
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     -
     - Date / time stamp for any change in definition for obs: Item #606
   * - ``om1_23``
     - OM1.23
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Effective date / time of change: Item #607
   * - ``om1_24``
     - OM1.24
     - Optional[str]
     - optional
     -
     - Typical Turn-around Time: Item #608
   * - ``om1_25``
     - OM1.25
     - Optional[str]
     - optional
     -
     - Processing Time: Item #609
   * - ``om1_26``
     - OM1.26
     - Optional[List[str]]
     - optional
     -
     - Processing Priority: Item #610 | Table HL70168
   * - ``om1_27``
     - OM1.27
     - Optional[str]
     - optional
     -
     - Reporting Priority: Item #611 | Table HL70169
   * - ``om1_28``
     - OM1.28
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Outside Site(s) Where Observation may be Performed: Item #612
   * - ``om1_29``
     - OM1.29
     - Optional[List[:ref:`AD <hl7-v2_2-AD>`]]
     - optional
     -
     - Address of Outside Site(s): Item #613
   * - ``om1_30``
     - OM1.30
     - Optional[List[str]]
     - optional
     -
     - Phone Number of Outside Site: Item #614
   * - ``om1_31``
     - OM1.31
     - Optional[str]
     - optional
     -
     - Confidentiality Code: Item #615 | Table HL70177
   * - ``om1_32``
     - OM1.32
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Observations required to interpret the observation: Item #616
   * - ``om1_33``
     - OM1.33
     - Optional[:ref:`TX <hl7-v2_2-TX>`]
     - optional
     -
     - Interpretation of Observations: Item #617
   * - ``om1_34``
     - OM1.34
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Contraindications to Observations: Item #618
   * - ``om1_35``
     - OM1.35
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Reflex tests / observations: Item #619
   * - ``om1_36``
     - OM1.36
     - Optional[str]
     - optional
     -
     - Rules that Trigger Reflex Testing: Item #620
   * - ``om1_37``
     - OM1.37
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Fixed Canned Message: Item #621
   * - ``om1_38``
     - OM1.38
     - Optional[:ref:`TX <hl7-v2_2-TX>`]
     - optional
     -
     - Patient Preparation: Item #622
   * - ``om1_39``
     - OM1.39
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Procedure Medication: Item #623
   * - ``om1_40``
     - OM1.40
     - Optional[:ref:`TX <hl7-v2_2-TX>`]
     - optional
     -
     - Factors that may affect the observation: Item #624
   * - ``om1_41``
     - OM1.41
     - Optional[List[str]]
     - optional
     -
     - Test / observation performance schedule: Item #625
   * - ``om1_42``
     - OM1.42
     - Optional[:ref:`TX <hl7-v2_2-TX>`]
     - optional
     -
     - Description of Test Methods: Item #626

.. _hl7-v2_2-OM2:

.. py:class:: hl7types.hl7.v2_2.segments.OM2.OM2
   :noindex:

   HL7 v2 OM2 segment.

OM2
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
   * - ``om2_1``
     - OM2.1
     - Optional[str]
     - optional
     -
     - Segment Type ID: Item #585
   * - ``om2_2``
     - OM2.2
     - Optional[str]
     - optional
     -
     - Sequence Number - Test/ Observation Master File: Item #586
   * - ``om2_3``
     - OM2.3
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Units of Measure: Item #627
   * - ``om2_4``
     - OM2.4
     - Optional[str]
     - optional
     -
     - Range of Decimal Precision: Item #628
   * - ``om2_5``
     - OM2.5
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Corresponding SI Units of Measure: Item #629
   * - ``om2_6``
     - OM2.6
     - Optional[List[:ref:`TX <hl7-v2_2-TX>`]]
     - optional
     -
     - SI Conversion Factor: Item #630
   * - ``om2_7``
     - OM2.7
     - Optional[List[str]]
     - optional
     -
     - Reference (normal) range - ordinal & continuous observations: Item #631
   * - ``om2_8``
     - OM2.8
     - Optional[str]
     - optional
     -
     - Critical range for ordinal and continuous observations: Item #632
   * - ``om2_9``
     - OM2.9
     - Optional[str]
     - optional
     -
     - Absolute range for ordinal and continuous observations: Item #633
   * - ``om2_10``
     - OM2.10
     - Optional[List[str]]
     - optional
     -
     - Delta Check Criteria: Item #634
   * - ``om2_11``
     - OM2.11
     - Optional[str]
     - optional
     -
     - Minimum Meaningful Increments: Item #635

.. _hl7-v2_2-OM3:

.. py:class:: hl7types.hl7.v2_2.segments.OM3.OM3
   :noindex:

   HL7 v2 OM3 segment.

OM3
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
   * - ``om3_1``
     - OM3.1
     - Optional[str]
     - optional
     -
     - Segment Type ID: Item #585
   * - ``om3_2``
     - OM3.2
     - Optional[str]
     - optional
     -
     - Sequence Number - Test/ Observation Master File: Item #586
   * - ``om3_3``
     - OM3.3
     - Optional[str]
     - optional
     -
     - Preferred Coding System: Item #636
   * - ``om3_4``
     - OM3.4
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Valid coded answers: Item #637
   * - ``om3_5``
     - OM3.5
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Normal test codes for categorical observations: Item #638
   * - ``om3_6``
     - OM3.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Abnormal test codes for categorical observations: Item #639
   * - ``om3_7``
     - OM3.7
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Critical test codes for categorical observations: Item #640
   * - ``om3_8``
     - OM3.8
     - Optional[str]
     - optional
     -
     - Data Type: Item #641

.. _hl7-v2_2-OM4:

.. py:class:: hl7types.hl7.v2_2.segments.OM4.OM4
   :noindex:

   HL7 v2 OM4 segment.

OM4
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
   * - ``om4_1``
     - OM4.1
     - Optional[str]
     - optional
     -
     - Segment Type ID: Item #585
   * - ``om4_2``
     - OM4.2
     - Optional[str]
     - optional
     -
     - Sequence Number - Test/ Observation Master File: Item #586
   * - ``om4_3``
     - OM4.3
     - Optional[str]
     - optional
     -
     - Derived Specimen: Item #642 | Table HL70170
   * - ``om4_4``
     - OM4.4
     - Optional[:ref:`TX <hl7-v2_2-TX>`]
     - optional
     -
     - Container Description: Item #643
   * - ``om4_5``
     - OM4.5
     - Optional[str]
     - optional
     -
     - Container Volume: Item #644
   * - ``om4_6``
     - OM4.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Container Units: Item #645
   * - ``om4_7``
     - OM4.7
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Specimen: Item #646
   * - ``om4_8``
     - OM4.8
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Additive: Item #647
   * - ``om4_9``
     - OM4.9
     - Optional[:ref:`TX <hl7-v2_2-TX>`]
     - optional
     -
     - Preparation: Item #648
   * - ``om4_10``
     - OM4.10
     - Optional[:ref:`TX <hl7-v2_2-TX>`]
     - optional
     -
     - Special Handling Requirements: Item #649
   * - ``om4_11``
     - OM4.11
     - Optional[str]
     - optional
     -
     - Normal Collection Volume: Item #650
   * - ``om4_12``
     - OM4.12
     - Optional[str]
     - optional
     -
     - Minimum Collection Volume: Item #651
   * - ``om4_13``
     - OM4.13
     - Optional[:ref:`TX <hl7-v2_2-TX>`]
     - optional
     -
     - Specimen Requirements: Item #652
   * - ``om4_14``
     - OM4.14
     - Optional[List[str]]
     - optional
     -
     - Specimen Priorities: Item #653 | Table HL70027
   * - ``om4_15``
     - OM4.15
     - Optional[str]
     - optional
     -
     - Specimen Retention Time: Item #654

.. _hl7-v2_2-OM5:

.. py:class:: hl7types.hl7.v2_2.segments.OM5.OM5
   :noindex:

   HL7 v2 OM5 segment.

OM5
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
   * - ``om5_1``
     - OM5.1
     - Optional[str]
     - optional
     -
     - Segment Type ID: Item #585
   * - ``om5_2``
     - OM5.2
     - Optional[str]
     - optional
     -
     - Sequence Number - Test/ Observation Master File: Item #586
   * - ``om5_3``
     - OM5.3
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Tests / observations included within an ordered test battery: Item #655
   * - ``om5_4``
     - OM5.4
     - Optional[str]
     - optional
     -
     - Observation ID Suffixes: Item #656

.. _hl7-v2_2-OM6:

.. py:class:: hl7types.hl7.v2_2.segments.OM6.OM6
   :noindex:

   HL7 v2 OM6 segment.

OM6
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
   * - ``om6_1``
     - OM6.1
     - Optional[str]
     - optional
     -
     - Segment Type ID: Item #585
   * - ``om6_2``
     - OM6.2
     - Optional[str]
     - optional
     -
     - Sequence Number - Test/ Observation Master File: Item #586
   * - ``om6_3``
     - OM6.3
     - Optional[:ref:`TX <hl7-v2_2-TX>`]
     - optional
     -
     - Derivation Rule: Item #657

.. _hl7-v2_2-ORC:

.. py:class:: hl7types.hl7.v2_2.segments.ORC.ORC
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
     - Order Control: Item #215 | Table HL70119
   * - ``orc_2``
     - ORC.2
     - Optional[str]
     - optional
     -
     - Placer Order Number: Item #216
   * - ``orc_3``
     - ORC.3
     - Optional[str]
     - optional
     -
     - Filler Order Number: Item #217
   * - ``orc_4``
     - ORC.4
     - Optional[str]
     - optional
     -
     - Placer Group Number: Item #218
   * - ``orc_5``
     - ORC.5
     - Optional[str]
     - optional
     -
     - Order Status: Item #219 | Table HL70038
   * - ``orc_6``
     - ORC.6
     - Optional[str]
     - optional
     -
     - Response Flag: Item #220 | Table HL70121
   * - ``orc_7``
     - ORC.7
     - Optional[List[:ref:`TQ <hl7-v2_2-TQ>`]]
     - optional
     -
     - Quantity / timing: Item #221
   * - ``orc_8``
     - ORC.8
     - Optional[str]
     - optional
     -
     - Parent: Item #222
   * - ``orc_9``
     - ORC.9
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Date / time of transaction: Item #223
   * - ``orc_10``
     - ORC.10
     - Optional[str]
     - optional
     -
     - Entered By: Item #224
   * - ``orc_11``
     - ORC.11
     - Optional[str]
     - optional
     -
     - Verified By: Item #225
   * - ``orc_12``
     - ORC.12
     - Optional[str]
     - optional
     -
     - Ordering Provider: Item #226
   * - ``orc_13``
     - ORC.13
     - Optional[str]
     - optional
     -
     - Enterer's Location: Item #227
   * - ``orc_14``
     - ORC.14
     - Optional[List[str]]
     - optional
     -
     - Call Back Phone Number: Item #228
   * - ``orc_15``
     - ORC.15
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Order effective date / time: Item #229
   * - ``orc_16``
     - ORC.16
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Order Control Code Reason: Item #230
   * - ``orc_17``
     - ORC.17
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Entering Organization: Item #231
   * - ``orc_18``
     - ORC.18
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Entering Device: Item #232
   * - ``orc_19``
     - ORC.19
     - Optional[str]
     - optional
     -
     - Action by: Item #233

.. _hl7-v2_2-PID:

.. py:class:: hl7types.hl7.v2_2.segments.PID.PID
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
     - Set ID - Patient ID: Item #104
   * - ``pid_2``
     - PID.2
     - Optional[str]
     - optional
     -
     - Patient ID (External ID): Item #105
   * - ``pid_3``
     - PID.3
     - List[str]
     - required
     -
     - Patient ID (Internal ID): Item #106
   * - ``pid_4``
     - PID.4
     - Optional[str]
     - optional
     -
     - Alternate Patient ID: Item #107
   * - ``pid_5``
     - PID.5
     - :ref:`PN <hl7-v2_2-PN>`
     - required
     -
     - Patient Name: Item #108
   * - ``pid_6``
     - PID.6
     - Optional[str]
     - optional
     -
     - Mother's Maiden Name: Item #109
   * - ``pid_7``
     - PID.7
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Date of Birth: Item #110
   * - ``pid_8``
     - PID.8
     - Optional[str]
     - optional
     -
     - Sex: Item #111 | Table HL70001
   * - ``pid_9``
     - PID.9
     - Optional[List[:ref:`PN <hl7-v2_2-PN>`]]
     - optional
     -
     - Patient Alias: Item #112
   * - ``pid_10``
     - PID.10
     - Optional[str]
     - optional
     -
     - Race: Item #113 | Table HL70005
   * - ``pid_11``
     - PID.11
     - Optional[List[:ref:`AD <hl7-v2_2-AD>`]]
     - optional
     -
     - Patient Address: Item #114
   * - ``pid_12``
     - PID.12
     - Optional[str]
     - optional
     -
     - County code: Item #115
   * - ``pid_13``
     - PID.13
     - Optional[List[str]]
     - optional
     -
     - Phone Number - Home: Item #116
   * - ``pid_14``
     - PID.14
     - Optional[List[str]]
     - optional
     -
     - Phone Number - Business: Item #117
   * - ``pid_15``
     - PID.15
     - Optional[str]
     - optional
     -
     - Language - Patient: Item #118
   * - ``pid_16``
     - PID.16
     - Optional[str]
     - optional
     -
     - Marital Status: Item #119 | Table HL70002
   * - ``pid_17``
     - PID.17
     - Optional[str]
     - optional
     -
     - Religion: Item #120 | Table HL70006
   * - ``pid_18``
     - PID.18
     - Optional[str]
     - optional
     -
     - Patient Account Number: Item #121
   * - ``pid_19``
     - PID.19
     - Optional[str]
     - optional
     -
     - Social security number - patient: Item #122
   * - ``pid_20``
     - PID.20
     - Optional[str]
     - optional
     -
     - Driver's license number - patient: Item #123
   * - ``pid_21``
     - PID.21
     - Optional[str]
     - optional
     -
     - Mother's Identifier: Item #124
   * - ``pid_22``
     - PID.22
     - Optional[str]
     - optional
     -
     - Ethnic Group: Item #125 | Table HL70189
   * - ``pid_23``
     - PID.23
     - Optional[str]
     - optional
     -
     - Birth Place: Item #126
   * - ``pid_24``
     - PID.24
     - Optional[str]
     - optional
     -
     - Multiple Birth Indicator: Item #127
   * - ``pid_25``
     - PID.25
     - Optional[str]
     - optional
     -
     - Birth Order: Item #128
   * - ``pid_26``
     - PID.26
     - Optional[List[str]]
     - optional
     -
     - Citizenship: Item #129 | Table HL70171
   * - ``pid_27``
     - PID.27
     - Optional[str]
     - optional
     -
     - Veterans Military Status: Item #130

.. _hl7-v2_2-PR1:

.. py:class:: hl7types.hl7.v2_2.segments.PR1.PR1
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
     - str
     - required
     -
     - Set ID - procedure: Item #391
   * - ``pr1_2``
     - PR1.2
     - List[str]
     - required
     -
     - Procedure coding method: Item #392 | Table HL70089
   * - ``pr1_3``
     - PR1.3
     - List[str]
     - required
     -
     - Procedure code: Item #393 | Table HL70088
   * - ``pr1_4``
     - PR1.4
     - Optional[List[str]]
     - optional
     -
     - Procedure description: Item #394
   * - ``pr1_5``
     - PR1.5
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     -
     - Procedure date / time: Item #395
   * - ``pr1_6``
     - PR1.6
     - str
     - required
     -
     - Procedure type: Item #396 | Table HL70090
   * - ``pr1_7``
     - PR1.7
     - Optional[str]
     - optional
     -
     - Procedure minutes: Item #397
   * - ``pr1_8``
     - PR1.8
     - Optional[str]
     - optional
     -
     - Anesthesiologist: Item #398 | Table HL70010
   * - ``pr1_9``
     - PR1.9
     - Optional[str]
     - optional
     -
     - Anesthesia code: Item #399 | Table HL70019
   * - ``pr1_10``
     - PR1.10
     - Optional[str]
     - optional
     -
     - Anesthesia minutes: Item #400
   * - ``pr1_11``
     - PR1.11
     - Optional[str]
     - optional
     -
     - Surgeon: Item #401 | Table HL70010
   * - ``pr1_12``
     - PR1.12
     - Optional[List[str]]
     - optional
     -
     - Procedure Practitioner: Item #402 | Table HL70010
   * - ``pr1_13``
     - PR1.13
     - Optional[str]
     - optional
     -
     - Consent code: Item #403 | Table HL70059
   * - ``pr1_14``
     - PR1.14
     - Optional[str]
     - optional
     -
     - Procedure priority: Item #404

.. _hl7-v2_2-PRA:

.. py:class:: hl7types.hl7.v2_2.segments.PRA.PRA
   :noindex:

   HL7 v2 PRA segment.

PRA
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
   * - ``pra_1``
     - PRA.1
     - str
     - required
     -
     - PRA - primary key value: Item #685
   * - ``pra_2``
     - PRA.2
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Practitioner group: Item #686
   * - ``pra_3``
     - PRA.3
     - Optional[List[str]]
     - optional
     -
     - Practitioner Category: Item #687 | Table HL70186
   * - ``pra_4``
     - PRA.4
     - Optional[str]
     - optional
     -
     - Provider Billing: Item #688 | Table HL70187
   * - ``pra_5``
     - PRA.5
     - Optional[List[str]]
     - optional
     -
     - Specialty: Item #689
   * - ``pra_6``
     - PRA.6
     - Optional[List[str]]
     - optional
     -
     - Practitioner ID Numbers: Item #690
   * - ``pra_7``
     - PRA.7
     - Optional[List[str]]
     - optional
     -
     - Privileges: Item #691

.. _hl7-v2_2-PV1:

.. py:class:: hl7types.hl7.v2_2.segments.PV1.PV1
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
     - Set ID - Patient Visit: Item #131
   * - ``pv1_2``
     - PV1.2
     - str
     - required
     -
     - Patient Class: Item #132 | Table HL70004
   * - ``pv1_3``
     - PV1.3
     - Optional[str]
     - optional
     -
     - Assigned Patient Location: Item #133 | Table HL70079
   * - ``pv1_4``
     - PV1.4
     - Optional[str]
     - optional
     -
     - Admission Type: Item #134 | Table HL70007
   * - ``pv1_5``
     - PV1.5
     - Optional[str]
     - optional
     -
     - Preadmit Number: Item #135
   * - ``pv1_6``
     - PV1.6
     - Optional[str]
     - optional
     -
     - Prior Patient Location: Item #136
   * - ``pv1_7``
     - PV1.7
     - Optional[str]
     - optional
     -
     - Attending Doctor: Item #137 | Table HL70010
   * - ``pv1_8``
     - PV1.8
     - Optional[str]
     - optional
     -
     - Referring Doctor: Item #138 | Table HL70010
   * - ``pv1_9``
     - PV1.9
     - Optional[List[str]]
     - optional
     -
     - Consulting Doctor: Item #139 | Table HL70010
   * - ``pv1_10``
     - PV1.10
     - Optional[str]
     - optional
     -
     - Hospital Service: Item #140 | Table HL70069
   * - ``pv1_11``
     - PV1.11
     - Optional[str]
     - optional
     -
     - Temporary Location: Item #141 | Table HL70079
   * - ``pv1_12``
     - PV1.12
     - Optional[str]
     - optional
     -
     - Preadmit Test Indicator: Item #142 | Table HL70087
   * - ``pv1_13``
     - PV1.13
     - Optional[str]
     - optional
     -
     - Readmission indicator: Item #143 | Table HL70092
   * - ``pv1_14``
     - PV1.14
     - Optional[str]
     - optional
     -
     - Admit Source: Item #144 | Table HL70023
   * - ``pv1_15``
     - PV1.15
     - Optional[List[str]]
     - optional
     -
     - Ambulatory Status: Item #145 | Table HL70009
   * - ``pv1_16``
     - PV1.16
     - Optional[str]
     - optional
     -
     - VIP Indicator: Item #146 | Table HL70099
   * - ``pv1_17``
     - PV1.17
     - Optional[str]
     - optional
     -
     - Admitting Doctor: Item #147 | Table HL70010
   * - ``pv1_18``
     - PV1.18
     - Optional[str]
     - optional
     -
     - Patient type: Item #148 | Table HL70018
   * - ``pv1_19``
     - PV1.19
     - Optional[str]
     - optional
     -
     - Visit Number: Item #149
   * - ``pv1_20``
     - PV1.20
     - Optional[List[str]]
     - optional
     -
     - Financial Class: Item #150 | Table HL70064
   * - ``pv1_21``
     - PV1.21
     - Optional[str]
     - optional
     -
     - Charge Price Indicator: Item #151 | Table HL70032
   * - ``pv1_22``
     - PV1.22
     - Optional[str]
     - optional
     -
     - Courtesy Code: Item #152 | Table HL70045
   * - ``pv1_23``
     - PV1.23
     - Optional[str]
     - optional
     -
     - Credit Rating: Item #153 | Table HL70046
   * - ``pv1_24``
     - PV1.24
     - Optional[List[str]]
     - optional
     -
     - Contract Code: Item #154 | Table HL70044
   * - ``pv1_25``
     - PV1.25
     - Optional[List[str]]
     - optional
     -
     - Contract Effective Date: Item #155
   * - ``pv1_26``
     - PV1.26
     - Optional[List[str]]
     - optional
     -
     - Contract Amount: Item #156
   * - ``pv1_27``
     - PV1.27
     - Optional[List[str]]
     - optional
     -
     - Contract Period: Item #157
   * - ``pv1_28``
     - PV1.28
     - Optional[str]
     - optional
     -
     - Interest Code: Item #158 | Table HL70073
   * - ``pv1_29``
     - PV1.29
     - Optional[str]
     - optional
     -
     - Transfer to bad debt - code: Item #159 | Table HL70110
   * - ``pv1_30``
     - PV1.30
     - Optional[str]
     - optional
     -
     - Transfer to bad debt - date: Item #160
   * - ``pv1_31``
     - PV1.31
     - Optional[str]
     - optional
     -
     - Bad Debt Agency Code: Item #161 | Table HL70021
   * - ``pv1_32``
     - PV1.32
     - Optional[str]
     - optional
     -
     - Bad Debt Transfer Amount: Item #162
   * - ``pv1_33``
     - PV1.33
     - Optional[str]
     - optional
     -
     - Bad Debt Recovery Amount: Item #163
   * - ``pv1_34``
     - PV1.34
     - Optional[str]
     - optional
     -
     - Delete Account Indicator: Item #164 | Table HL70111
   * - ``pv1_35``
     - PV1.35
     - Optional[str]
     - optional
     -
     - Delete Account Date: Item #165
   * - ``pv1_36``
     - PV1.36
     - Optional[str]
     - optional
     -
     - Discharge Disposition: Item #166 | Table HL70112
   * - ``pv1_37``
     - PV1.37
     - Optional[str]
     - optional
     -
     - Discharged to Location: Item #167 | Table HL70113
   * - ``pv1_38``
     - PV1.38
     - Optional[str]
     - optional
     -
     - Diet Type: Item #168 | Table HL70114
   * - ``pv1_39``
     - PV1.39
     - Optional[str]
     - optional
     -
     - Servicing Facility: Item #169 | Table HL70115
   * - ``pv1_40``
     - PV1.40
     - Optional[str]
     - optional
     -
     - Bed Status: Item #170 | Table HL70116
   * - ``pv1_41``
     - PV1.41
     - Optional[str]
     - optional
     -
     - Account Status: Item #171 | Table HL70117
   * - ``pv1_42``
     - PV1.42
     - Optional[str]
     - optional
     -
     - Pending Location: Item #172
   * - ``pv1_43``
     - PV1.43
     - Optional[str]
     - optional
     -
     - Prior Temporary Location: Item #173
   * - ``pv1_44``
     - PV1.44
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Admit date / time: Item #174
   * - ``pv1_45``
     - PV1.45
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Discharge date / time: Item #175
   * - ``pv1_46``
     - PV1.46
     - Optional[str]
     - optional
     -
     - Current Patient Balance: Item #176
   * - ``pv1_47``
     - PV1.47
     - Optional[str]
     - optional
     -
     - Total Charges: Item #177
   * - ``pv1_48``
     - PV1.48
     - Optional[str]
     - optional
     -
     - Total Adjustments: Item #178
   * - ``pv1_49``
     - PV1.49
     - Optional[str]
     - optional
     -
     - Total Payments: Item #179
   * - ``pv1_50``
     - PV1.50
     - Optional[str]
     - optional
     -
     - Alternate Visit ID: Item #180

.. _hl7-v2_2-PV2:

.. py:class:: hl7types.hl7.v2_2.segments.PV2.PV2
   :noindex:

   HL7 v2 PV2 segment.

PV2
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
   * - ``pv2_1``
     - PV2.1
     - Optional[str]
     - optional
     -
     - Prior Pending Location: Item #181
   * - ``pv2_2``
     - PV2.2
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Accommodation Code: Item #182 | Table HL70129
   * - ``pv2_3``
     - PV2.3
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Admit Reason: Item #183
   * - ``pv2_4``
     - PV2.4
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Transfer Reason: Item #184
   * - ``pv2_5``
     - PV2.5
     - Optional[List[str]]
     - optional
     -
     - Patient Valuables: Item #185
   * - ``pv2_6``
     - PV2.6
     - Optional[str]
     - optional
     -
     - Patient Valuables Location: Item #186
   * - ``pv2_7``
     - PV2.7
     - Optional[str]
     - optional
     -
     - Visit User Code: Item #187 | Table HL70130
   * - ``pv2_8``
     - PV2.8
     - Optional[str]
     - optional
     -
     - Expected Admit Date: Item #188
   * - ``pv2_9``
     - PV2.9
     - Optional[str]
     - optional
     -
     - Expected Discharge Date: Item #189

.. _hl7-v2_2-QRD:

.. py:class:: hl7types.hl7.v2_2.segments.QRD.QRD
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
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     -
     - Query date / time: Item #25
   * - ``qrd_2``
     - QRD.2
     - str
     - required
     -
     - Query Format Code: Item #26 | Table HL70106
   * - ``qrd_3``
     - QRD.3
     - str
     - required
     -
     - Query Priority: Item #27 | Table HL70091
   * - ``qrd_4``
     - QRD.4
     - str
     - required
     -
     - Query ID: Item #28
   * - ``qrd_5``
     - QRD.5
     - Optional[str]
     - optional
     -
     - Deferred Response Type: Item #29 | Table HL70107
   * - ``qrd_6``
     - QRD.6
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Deferred response date / time: Item #30
   * - ``qrd_7``
     - QRD.7
     - str
     - required
     -
     - Quantity Limited Request: Item #31 | Table HL70126
   * - ``qrd_8``
     - QRD.8
     - List[str]
     - required
     -
     - Who Subject Filter: Item #32
   * - ``qrd_9``
     - QRD.9
     - List[str]
     - required
     -
     - What Subject Filter: Item #33 | Table HL70048
   * - ``qrd_10``
     - QRD.10
     - List[str]
     - required
     -
     - What Department Data Code: Item #34
   * - ``qrd_11``
     - QRD.11
     - Optional[List[str]]
     - optional
     -
     - What data code value qualifier: Item #35
   * - ``qrd_12``
     - QRD.12
     - Optional[str]
     - optional
     -
     - Query Results Level: Item #36 | Table HL70108

.. _hl7-v2_2-QRF:

.. py:class:: hl7types.hl7.v2_2.segments.QRF.QRF
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
     - Where Subject Filter: Item #37
   * - ``qrf_2``
     - QRF.2
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - When data start date / time: Item #38
   * - ``qrf_3``
     - QRF.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - When data end date / time: Item #39
   * - ``qrf_4``
     - QRF.4
     - Optional[List[str]]
     - optional
     -
     - What User Qualifier: Item #40
   * - ``qrf_5``
     - QRF.5
     - Optional[List[str]]
     - optional
     -
     - Other QRY Subject Filter: Item #41
   * - ``qrf_6``
     - QRF.6
     - Optional[List[str]]
     - optional
     -
     - Which date / time qualifier: Item #42 | Table HL70156
   * - ``qrf_7``
     - QRF.7
     - Optional[List[str]]
     - optional
     -
     - Which date / time status qualifier: Item #43 | Table HL70157
   * - ``qrf_8``
     - QRF.8
     - Optional[List[str]]
     - optional
     -
     - Date / time selection qualifier: Item #44 | Table HL70158

.. _hl7-v2_2-RQ1:

.. py:class:: hl7types.hl7.v2_2.segments.RQ1.RQ1
   :noindex:

   HL7 v2 RQ1 segment.

RQ1
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
   * - ``rq1_1``
     - RQ1.1
     - Optional[str]
     - optional
     -
     - Anticipated Price: Item #285
   * - ``rq1_2``
     - RQ1.2
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Manufacturer ID: Item #286
   * - ``rq1_3``
     - RQ1.3
     - Optional[str]
     - optional
     -
     - Manufacturer's Catalog: Item #287
   * - ``rq1_4``
     - RQ1.4
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Vendor ID: Item #288
   * - ``rq1_5``
     - RQ1.5
     - Optional[str]
     - optional
     -
     - Vendor Catalog: Item #289
   * - ``rq1_6``
     - RQ1.6
     - Optional[str]
     - optional
     -
     - Taxable: Item #290 | Table HL70136
   * - ``rq1_7``
     - RQ1.7
     - Optional[str]
     - optional
     -
     - Substitute Allowed: Item #291 | Table HL70136

.. _hl7-v2_2-RQD:

.. py:class:: hl7types.hl7.v2_2.segments.RQD.RQD
   :noindex:

   HL7 v2 RQD segment.

RQD
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
   * - ``rqd_1``
     - RQD.1
     - Optional[str]
     - optional
     -
     - Requisition Line Number: Item #275
   * - ``rqd_2``
     - RQD.2
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Item Code - Internal: Item #276
   * - ``rqd_3``
     - RQD.3
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Item Code - External: Item #277
   * - ``rqd_4``
     - RQD.4
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Hospital Item Code: Item #278
   * - ``rqd_5``
     - RQD.5
     - Optional[str]
     - optional
     -
     - Requisition Quantity: Item #279
   * - ``rqd_6``
     - RQD.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Requisition Unit of measure: Item #280
   * - ``rqd_7``
     - RQD.7
     - Optional[str]
     - optional
     -
     - Department cost center: Item #281
   * - ``rqd_8``
     - RQD.8
     - Optional[str]
     - optional
     -
     - Item Natural Account Code: Item #282
   * - ``rqd_9``
     - RQD.9
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Deliver-to ID: Item #283
   * - ``rqd_10``
     - RQD.10
     - Optional[str]
     - optional
     -
     - Date Needed: Item #284

.. _hl7-v2_2-RXA:

.. py:class:: hl7types.hl7.v2_2.segments.RXA.RXA
   :noindex:

   HL7 v2 RXA segment.

RXA
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
   * - ``rxa_1``
     - RXA.1
     - str
     - required
     -
     - Give Sub-ID Counter: Item #342
   * - ``rxa_2``
     - RXA.2
     - str
     - required
     -
     - Administration Sub-ID Counter: Item #344
   * - ``rxa_3``
     - RXA.3
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     -
     - Date / time start of administration: Item #345
   * - ``rxa_4``
     - RXA.4
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     -
     - Date / time end of administration: Item #346
   * - ``rxa_5``
     - RXA.5
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Administered Code: Item #347
   * - ``rxa_6``
     - RXA.6
     - str
     - required
     -
     - Administered Amount: Item #348
   * - ``rxa_7``
     - RXA.7
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Administered Units: Item #349
   * - ``rxa_8``
     - RXA.8
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Administered Dosage Form: Item #350
   * - ``rxa_9``
     - RXA.9
     - Optional[str]
     - optional
     -
     - Administration Notes: Item #351
   * - ``rxa_10``
     - RXA.10
     - Optional[str]
     - optional
     -
     - Administering Provider: Item #352
   * - ``rxa_11``
     - RXA.11
     - Optional[str]
     - optional
     -
     - Administered-at Location: Item #353
   * - ``rxa_12``
     - RXA.12
     - Optional[str]
     - optional
     -
     - Administered Per (Time Unit): Item #354

.. _hl7-v2_2-RXC:

.. py:class:: hl7types.hl7.v2_2.segments.RXC.RXC
   :noindex:

   HL7 v2 RXC segment.

RXC
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
   * - ``rxc_1``
     - RXC.1
     - str
     - required
     -
     - RX Component Type: Item #313 | Table HL70166
   * - ``rxc_2``
     - RXC.2
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Component Code: Item #314
   * - ``rxc_3``
     - RXC.3
     - str
     - required
     -
     - Component Amount: Item #315
   * - ``rxc_4``
     - RXC.4
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Component Units: Item #316

.. _hl7-v2_2-RXD:

.. py:class:: hl7types.hl7.v2_2.segments.RXD.RXD
   :noindex:

   HL7 v2 RXD segment.

RXD
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
   * - ``rxd_1``
     - RXD.1
     - Optional[str]
     - optional
     -
     - Dispense Sub-ID Counter: Item #334
   * - ``rxd_2``
     - RXD.2
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Dispense / give code: Item #335
   * - ``rxd_3``
     - RXD.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Date / time dispensed: Item #336
   * - ``rxd_4``
     - RXD.4
     - str
     - required
     -
     - Actual Dispense Amount: Item #337
   * - ``rxd_5``
     - RXD.5
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Actual Dispense Units: Item #338
   * - ``rxd_6``
     - RXD.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Actual Dosage Form: Item #339
   * - ``rxd_7``
     - RXD.7
     - str
     - required
     -
     - Prescription Number: Item #325
   * - ``rxd_8``
     - RXD.8
     - Optional[str]
     - optional
     -
     - Number of Refills Remaining: Item #326
   * - ``rxd_9``
     - RXD.9
     - Optional[List[str]]
     - optional
     -
     - Dispense Notes: Item #340
   * - ``rxd_10``
     - RXD.10
     - Optional[str]
     - optional
     -
     - Dispensing Provider: Item #341
   * - ``rxd_11``
     - RXD.11
     - Optional[str]
     - optional
     -
     - Substitution Status: Item #322 | Table HL70167
   * - ``rxd_12``
     - RXD.12
     - Optional[str]
     - optional
     -
     - Total Daily Dose: Item #329
   * - ``rxd_13``
     - RXD.13
     - Optional[str]
     - optional
     -
     - Deliver-to location: Item #299
   * - ``rxd_14``
     - RXD.14
     - Optional[str]
     - optional
     -
     - Needs Human Review: Item #307
   * - ``rxd_15``
     - RXD.15
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Pharmacy Special Dispensing Instructions: Item #330

.. _hl7-v2_2-RXE:

.. py:class:: hl7types.hl7.v2_2.segments.RXE.RXE
   :noindex:

   HL7 v2 RXE segment.

RXE
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
   * - ``rxe_1``
     - RXE.1
     - Optional[List[:ref:`TQ <hl7-v2_2-TQ>`]]
     - optional
     -
     - Quantity / timing: Item #221
   * - ``rxe_2``
     - RXE.2
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Give Code: Item #317
   * - ``rxe_3``
     - RXE.3
     - str
     - required
     -
     - Give Amount - Minimum: Item #318
   * - ``rxe_4``
     - RXE.4
     - Optional[str]
     - optional
     -
     - Give Amount - Maximum: Item #319
   * - ``rxe_5``
     - RXE.5
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Give Units: Item #320
   * - ``rxe_6``
     - RXE.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Give Dosage Form: Item #321
   * - ``rxe_7``
     - RXE.7
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Provider's Administration Instructions: Item #298
   * - ``rxe_8``
     - RXE.8
     - Optional[str]
     - optional
     -
     - Deliver-to location: Item #299
   * - ``rxe_9``
     - RXE.9
     - Optional[str]
     - optional
     -
     - Substitution Status: Item #322 | Table HL70167
   * - ``rxe_10``
     - RXE.10
     - Optional[str]
     - optional
     -
     - Dispense Amount: Item #323
   * - ``rxe_11``
     - RXE.11
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Dispense Units: Item #324
   * - ``rxe_12``
     - RXE.12
     - Optional[str]
     - optional
     -
     - Number of Refills: Item #304
   * - ``rxe_13``
     - RXE.13
     - Optional[str]
     - optional
     -
     - Ordering Provider's DEA Number: Item #305
   * - ``rxe_14``
     - RXE.14
     - Optional[str]
     - optional
     -
     - Pharmacist Verifier ID: Item #306
   * - ``rxe_15``
     - RXE.15
     - str
     - required
     -
     - Prescription Number: Item #325
   * - ``rxe_16``
     - RXE.16
     - Optional[str]
     - optional
     -
     - Number of Refills Remaining: Item #326
   * - ``rxe_17``
     - RXE.17
     - Optional[str]
     - optional
     -
     - Number of refills / doses dispensed: Item #327
   * - ``rxe_18``
     - RXE.18
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Date / time of most recent refill or dose dispensed: Item #328
   * - ``rxe_19``
     - RXE.19
     - Optional[str]
     - optional
     -
     - Total Daily Dose: Item #329
   * - ``rxe_20``
     - RXE.20
     - Optional[str]
     - optional
     -
     - Needs Human Review: Item #307
   * - ``rxe_21``
     - RXE.21
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Pharmacy Special Dispensing Instructions: Item #330
   * - ``rxe_22``
     - RXE.22
     - Optional[str]
     - optional
     -
     - Give Per (Time Unit): Item #331
   * - ``rxe_23``
     - RXE.23
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Give Rate Amount: Item #332
   * - ``rxe_24``
     - RXE.24
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Give Rate Units: Item #333

.. _hl7-v2_2-RXG:

.. py:class:: hl7types.hl7.v2_2.segments.RXG.RXG
   :noindex:

   HL7 v2 RXG segment.

RXG
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
   * - ``rxg_1``
     - RXG.1
     - str
     - required
     -
     - Give Sub-ID Counter: Item #342
   * - ``rxg_2``
     - RXG.2
     - Optional[str]
     - optional
     -
     - Dispense Sub-ID Counter: Item #334
   * - ``rxg_3``
     - RXG.3
     - Optional[List[:ref:`TQ <hl7-v2_2-TQ>`]]
     - optional
     -
     - Quantity / timing: Item #221
   * - ``rxg_4``
     - RXG.4
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Give Code: Item #317
   * - ``rxg_5``
     - RXG.5
     - str
     - required
     -
     - Give Amount - Minimum: Item #318
   * - ``rxg_6``
     - RXG.6
     - Optional[str]
     - optional
     -
     - Give Amount - Maximum: Item #319
   * - ``rxg_7``
     - RXG.7
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Give Units: Item #320
   * - ``rxg_8``
     - RXG.8
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Give Dosage Form: Item #321
   * - ``rxg_9``
     - RXG.9
     - Optional[str]
     - optional
     -
     - Administration Notes: Item #351
   * - ``rxg_10``
     - RXG.10
     - Optional[str]
     - optional
     -
     - Substitution Status: Item #322 | Table HL70167
   * - ``rxg_11``
     - RXG.11
     - Optional[str]
     - optional
     -
     - Deliver-to location: Item #299
   * - ``rxg_12``
     - RXG.12
     - Optional[str]
     - optional
     -
     - Needs Human Review: Item #307
   * - ``rxg_13``
     - RXG.13
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Pharmacy Special Administration Instructions: Item #343
   * - ``rxg_14``
     - RXG.14
     - Optional[str]
     - optional
     -
     - Give Per (Time Unit): Item #331
   * - ``rxg_15``
     - RXG.15
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Give Rate Amount: Item #332
   * - ``rxg_16``
     - RXG.16
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Give Rate Units: Item #333

.. _hl7-v2_2-RXO:

.. py:class:: hl7types.hl7.v2_2.segments.RXO.RXO
   :noindex:

   HL7 v2 RXO segment.

RXO
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
   * - ``rxo_1``
     - RXO.1
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Requested Give Code: Item #292
   * - ``rxo_2``
     - RXO.2
     - str
     - required
     -
     - Requested Give Amount - Minimum: Item #293
   * - ``rxo_3``
     - RXO.3
     - Optional[str]
     - optional
     -
     - Requested Give Amount - Maximum: Item #294
   * - ``rxo_4``
     - RXO.4
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Requested Give Units: Item #295
   * - ``rxo_5``
     - RXO.5
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Requested Dosage Form: Item #296
   * - ``rxo_6``
     - RXO.6
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Provider's Pharmacy Instructions: Item #297
   * - ``rxo_7``
     - RXO.7
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Provider's Administration Instructions: Item #298
   * - ``rxo_8``
     - RXO.8
     - Optional[str]
     - optional
     -
     - Deliver-to location: Item #299
   * - ``rxo_9``
     - RXO.9
     - Optional[str]
     - optional
     -
     - Allow Substitutions: Item #300 | Table HL70161
   * - ``rxo_10``
     - RXO.10
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Requested Dispense Code: Item #301
   * - ``rxo_11``
     - RXO.11
     - Optional[str]
     - optional
     -
     - Requested Dispense Amount: Item #302
   * - ``rxo_12``
     - RXO.12
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Requested Dispense Units: Item #303
   * - ``rxo_13``
     - RXO.13
     - Optional[str]
     - optional
     -
     - Number of Refills: Item #304
   * - ``rxo_14``
     - RXO.14
     - Optional[str]
     - optional
     -
     - Ordering Provider's DEA Number: Item #305
   * - ``rxo_15``
     - RXO.15
     - Optional[str]
     - optional
     -
     - Pharmacist Verifier ID: Item #306
   * - ``rxo_16``
     - RXO.16
     - Optional[str]
     - optional
     -
     - Needs Human Review: Item #307
   * - ``rxo_17``
     - RXO.17
     - Optional[str]
     - optional
     -
     - Requested Give Per (Time Unit): Item #308

.. _hl7-v2_2-RXR:

.. py:class:: hl7types.hl7.v2_2.segments.RXR.RXR
   :noindex:

   HL7 v2 RXR segment.

RXR
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
   * - ``rxr_1``
     - RXR.1
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - Route: Item #309 | Table HL70162
   * - ``rxr_2``
     - RXR.2
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Site: Item #310 | Table HL70163
   * - ``rxr_3``
     - RXR.3
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Administration Device: Item #311 | Table HL70164
   * - ``rxr_4``
     - RXR.4
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     -
     - Administration Method: Item #312 | Table HL70165

.. _hl7-v2_2-STF:

.. py:class:: hl7types.hl7.v2_2.segments.STF.STF
   :noindex:

   HL7 v2 STF segment.

STF
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
   * - ``stf_1``
     - STF.1
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     -
     - STF - primary key value: Item #671
   * - ``stf_2``
     - STF.2
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Staff ID Code: Item #672
   * - ``stf_3``
     - STF.3
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     -
     - Staff Name: Item #673
   * - ``stf_4``
     - STF.4
     - Optional[List[str]]
     - optional
     -
     - Staff Type: Item #674 | Table HL70182
   * - ``stf_5``
     - STF.5
     - Optional[str]
     - optional
     -
     - Sex: Item #111 | Table HL70001
   * - ``stf_6``
     - STF.6
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - Date of Birth: Item #110
   * - ``stf_7``
     - STF.7
     - Optional[str]
     - optional
     -
     - Active / inactive: Item #675 | Table HL70183
   * - ``stf_8``
     - STF.8
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Department: Item #676 | Table HL70184
   * - ``stf_9``
     - STF.9
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Service: Item #677
   * - ``stf_10``
     - STF.10
     - Optional[List[str]]
     - optional
     -
     - Phone: Item #678
   * - ``stf_11``
     - STF.11
     - Optional[List[:ref:`AD <hl7-v2_2-AD>`]]
     - optional
     -
     - Office / home address: Item #679
   * - ``stf_12``
     - STF.12
     - Optional[List[str]]
     - optional
     -
     - Activation Date: Item #680
   * - ``stf_13``
     - STF.13
     - Optional[List[str]]
     - optional
     -
     - Inactivation Date: Item #681
   * - ``stf_14``
     - STF.14
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     -
     - Backup Person ID: Item #682
   * - ``stf_15``
     - STF.15
     - Optional[List[str]]
     - optional
     -
     - E-mail Address: Item #683
   * - ``stf_16``
     - STF.16
     - Optional[str]
     - optional
     -
     - Preferred method of Contact: Item #684 | Table HL70185

.. _hl7-v2_2-UB1:

.. py:class:: hl7types.hl7.v2_2.segments.UB1.UB1
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
     - Set ID - UB82: Item #530
   * - ``ub1_2``
     - UB1.2
     - Optional[str]
     - optional
     -
     - Blood deductible (43): Item #492 | Table HL70136
   * - ``ub1_3``
     - UB1.3
     - Optional[str]
     - optional
     -
     - Blood furnished pints of (40): Item #532
   * - ``ub1_4``
     - UB1.4
     - Optional[str]
     - optional
     -
     - Blood replaced pints (41): Item #533
   * - ``ub1_5``
     - UB1.5
     - Optional[str]
     - optional
     -
     - Blood not replaced pints (42): Item #534
   * - ``ub1_6``
     - UB1.6
     - Optional[str]
     - optional
     -
     - Co-insurance days (25): Item #535
   * - ``ub1_7``
     - UB1.7
     - Optional[List[str]]
     - optional
     -
     - Condition code (35-39): Item #536 | Table HL70043
   * - ``ub1_8``
     - UB1.8
     - Optional[str]
     - optional
     -
     - Covered days (23): Item #537
   * - ``ub1_9``
     - UB1.9
     - Optional[str]
     - optional
     -
     - Non-covered days (24): Item #538
   * - ``ub1_10``
     - UB1.10
     - Optional[List[str]]
     - optional
     -
     - Value amount and code (46-49): Item #539 | Table HL70153
   * - ``ub1_11``
     - UB1.11
     - Optional[str]
     - optional
     -
     - Number of grace days (90): Item #540
   * - ``ub1_12``
     - UB1.12
     - Optional[str]
     - optional
     -
     - Special program indicator (44): Item #541
   * - ``ub1_13``
     - UB1.13
     - Optional[str]
     - optional
     -
     - PSRO / UR approval indicator (87): Item #542
   * - ``ub1_14``
     - UB1.14
     - Optional[str]
     - optional
     -
     - PSRO / UR approved stay - from (88): Item #543
   * - ``ub1_15``
     - UB1.15
     - Optional[str]
     - optional
     -
     - PSRO / UR approved stay - to (89): Item #544
   * - ``ub1_16``
     - UB1.16
     - Optional[List[str]]
     - optional
     -
     - Occurrence (28-32): Item #545
   * - ``ub1_17``
     - UB1.17
     - Optional[str]
     - optional
     -
     - Occurrence span (33): Item #546
   * - ``ub1_18``
     - UB1.18
     - Optional[str]
     - optional
     -
     - Occurrence span start date (33): Item #547
   * - ``ub1_19``
     - UB1.19
     - Optional[str]
     - optional
     -
     - Occurrence span end date (33): Item #548
   * - ``ub1_20``
     - UB1.20
     - Optional[str]
     - optional
     -
     - UB-82 locator 2: Item #549
   * - ``ub1_21``
     - UB1.21
     - Optional[str]
     - optional
     -
     - UB-82 locator 9: Item #550
   * - ``ub1_22``
     - UB1.22
     - Optional[str]
     - optional
     -
     - UB-82 locator 27: Item #551
   * - ``ub1_23``
     - UB1.23
     - Optional[str]
     - optional
     -
     - UB-82 locator 45: Item #552

.. _hl7-v2_2-UB2:

.. py:class:: hl7types.hl7.v2_2.segments.UB2.UB2
   :noindex:

   HL7 v2 UB2 segment.

UB2
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
   * - ``ub2_1``
     - UB2.1
     - Optional[str]
     - optional
     -
     - Set ID - UB92: Item #553
   * - ``ub2_2``
     - UB2.2
     - Optional[str]
     - optional
     -
     - Co-insurance days (9): Item #554
   * - ``ub2_3``
     - UB2.3
     - Optional[List[str]]
     - optional
     -
     - Condition code (24-30): Item #555 | Table HL70043
   * - ``ub2_4``
     - UB2.4
     - Optional[str]
     - optional
     -
     - Covered days (7): Item #556
   * - ``ub2_5``
     - UB2.5
     - Optional[str]
     - optional
     -
     - Non-covered days (8): Item #557
   * - ``ub2_6``
     - UB2.6
     - Optional[List[str]]
     - optional
     -
     - Value amount and code (39-41): Item #558
   * - ``ub2_7``
     - UB2.7
     - Optional[List[str]]
     - optional
     -
     - Occurrence code and date (32-35): Item #559
   * - ``ub2_8``
     - UB2.8
     - Optional[List[str]]
     - optional
     -
     - Occurrence span code / dates (36): Item #560
   * - ``ub2_9``
     - UB2.9
     - Optional[List[str]]
     - optional
     -
     - UB92 locator 2 (state): Item #561
   * - ``ub2_10``
     - UB2.10
     - Optional[List[str]]
     - optional
     -
     - UB92 locator 11 (state): Item #562
   * - ``ub2_11``
     - UB2.11
     - Optional[str]
     - optional
     -
     - UB92 locator 31 (national): Item #563
   * - ``ub2_12``
     - UB2.12
     - Optional[List[str]]
     - optional
     -
     - Document control number (37): Item #564
   * - ``ub2_13``
     - UB2.13
     - Optional[List[str]]
     - optional
     -
     - UB92 locator 49 (national): Item #565
   * - ``ub2_14``
     - UB2.14
     - Optional[List[str]]
     - optional
     -
     - UB92 locator 56 (state): Item #566
   * - ``ub2_15``
     - UB2.15
     - Optional[str]
     - optional
     -
     - UB92 locator 57 (national): Item #567
   * - ``ub2_16``
     - UB2.16
     - Optional[List[str]]
     - optional
     -
     - UB92 Locator 78 (state): Item #568

.. _hl7-v2_2-URD:

.. py:class:: hl7types.hl7.v2_2.segments.URD.URD
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
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - R/U date / time: Item #45
   * - ``urd_2``
     - URD.2
     - Optional[str]
     - optional
     -
     - Report Priority: Item #46 | Table HL70109
   * - ``urd_3``
     - URD.3
     - List[str]
     - required
     -
     - R/U Who Subject Definition: Item #47
   * - ``urd_4``
     - URD.4
     - Optional[List[str]]
     - optional
     -
     - R/U What Subject Definition: Item #48 | Table HL70048
   * - ``urd_5``
     - URD.5
     - Optional[List[str]]
     - optional
     -
     - R/U What Department Code: Item #49
   * - ``urd_6``
     - URD.6
     - Optional[List[str]]
     - optional
     -
     - R/U display / print locations: Item #50
   * - ``urd_7``
     - URD.7
     - Optional[str]
     - optional
     -
     - R/U Results Level: Item #51 | Table HL70108

.. _hl7-v2_2-URS:

.. py:class:: hl7types.hl7.v2_2.segments.URS.URS
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
     - R/U Where Subject Definition: Item #52
   * - ``urs_2``
     - URS.2
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - R/U when data start date / time: Item #53
   * - ``urs_3``
     - URS.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     -
     - R/U when data end date / time: Item #54
   * - ``urs_4``
     - URS.4
     - Optional[List[str]]
     - optional
     -
     - R/U What User Qualifier: Item #55
   * - ``urs_5``
     - URS.5
     - Optional[List[str]]
     - optional
     -
     - R/U Other Results Subject Definition: Item #56
   * - ``urs_6``
     - URS.6
     - Optional[List[str]]
     - optional
     -
     - R/U which date / time qualifier: Item #57 | Table HL70156
   * - ``urs_7``
     - URS.7
     - Optional[List[str]]
     - optional
     -
     - R/U which date / time status qualifier: Item #58 | Table HL70157
   * - ``urs_8``
     - URS.8
     - Optional[List[str]]
     - optional
     -
     - R/U date / time selection qualifier: Item #59 | Table HL70158
