v2.2 Segments
=============

.. _hl7-v2_2-ACC:

ACC ACCIDENT (S6.4.8).
~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.ACC.ACC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``acc_1``
     - ACC.1
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #527
   * - ``acc_2``
     - ACC.2
     - Optional[str]
     - optional
     - Item #528 | Table HL70050
   * - ``acc_3``
     - ACC.3
     - Optional[str]
     - optional
     - Item #529

.. _hl7-v2_2-ADD:

ADD ADDENDUM (S2.10.10).
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.ADD.ADD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``add_1``
     - ADD.1
     - Optional[str]
     - optional
     - Item #66

.. _hl7-v2_2-AL1:

AL1 PATIENT ALLERGY INFORMATION (S3.3.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.AL1.AL1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``al1_1``
     - AL1.1
     - str
     - required
     - Item #203
   * - ``al1_2``
     - AL1.2
     - Optional[str]
     - optional
     - Item #204 | Table HL70127
   * - ``al1_3``
     - AL1.3
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #205
   * - ``al1_4``
     - AL1.4
     - Optional[str]
     - optional
     - Item #206 | Table HL70128
   * - ``al1_5``
     - AL1.5
     - Optional[str]
     - optional
     - Item #207
   * - ``al1_6``
     - AL1.6
     - Optional[str]
     - optional
     - Item #208

.. _hl7-v2_2-BHS:

BHS BATCH HEADER (S2.10.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.BHS.BHS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``bhs_1``
     - BHS.1
     - str
     - optional
     - Item #81
   * - ``bhs_2``
     - BHS.2
     - str
     - optional
     - Item #82
   * - ``bhs_3``
     - BHS.3
     - Optional[str]
     - optional
     - Item #83
   * - ``bhs_4``
     - BHS.4
     - Optional[str]
     - optional
     - Item #84
   * - ``bhs_5``
     - BHS.5
     - Optional[str]
     - optional
     - Item #85
   * - ``bhs_6``
     - BHS.6
     - Optional[str]
     - optional
     - Item #86
   * - ``bhs_7``
     - BHS.7
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #87
   * - ``bhs_8``
     - BHS.8
     - Optional[str]
     - optional
     - Item #88
   * - ``bhs_9``
     - BHS.9
     - Optional[str]
     - optional
     - Item #89
   * - ``bhs_10``
     - BHS.10
     - Optional[str]
     - optional
     - Item #90
   * - ``bhs_11``
     - BHS.11
     - Optional[str]
     - optional
     - Item #91
   * - ``bhs_12``
     - BHS.12
     - Optional[str]
     - optional
     - Item #92

.. _hl7-v2_2-BLG:

BLG BILLING (S4.3.2).
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.BLG.BLG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``blg_1``
     - BLG.1
     - Optional[str]
     - optional
     - Item #234 | Table HL70100
   * - ``blg_2``
     - BLG.2
     - Optional[str]
     - optional
     - Item #235 | Table HL70122
   * - ``blg_3``
     - BLG.3
     - Optional[str]
     - optional
     - Item #236

.. _hl7-v2_2-BTS:

BTS BATCH TRAILER (S2.10.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.BTS.BTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``bts_1``
     - BTS.1
     - Optional[str]
     - optional
     - Item #93
   * - ``bts_2``
     - BTS.2
     - Optional[str]
     - optional
     - Item #94
   * - ``bts_3``
     - BTS.3
     - Optional[List[str]]
     - optional
     - Item #95

.. _hl7-v2_2-DG1:

DG1 DIAGNOSIS (S6.4.2).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.DG1.DG1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``dg1_1``
     - DG1.1
     - str
     - required
     - Item #375
   * - ``dg1_2``
     - DG1.2
     - str
     - required
     - Item #376 | Table HL70053
   * - ``dg1_3``
     - DG1.3
     - Optional[str]
     - optional
     - Item #377 | Table HL70051
   * - ``dg1_4``
     - DG1.4
     - Optional[str]
     - optional
     - Item #378
   * - ``dg1_5``
     - DG1.5
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #379
   * - ``dg1_6``
     - DG1.6
     - str
     - required
     - Item #380 | Table HL70052
   * - ``dg1_7``
     - DG1.7
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #381 | Table HL70118
   * - ``dg1_8``
     - DG1.8
     - Optional[str]
     - optional
     - Item #382 | Table HL70055
   * - ``dg1_9``
     - DG1.9
     - Optional[str]
     - optional
     - Item #383
   * - ``dg1_10``
     - DG1.10
     - Optional[str]
     - optional
     - Item #384 | Table HL70056
   * - ``dg1_11``
     - DG1.11
     - Optional[str]
     - optional
     - Item #385 | Table HL70083
   * - ``dg1_12``
     - DG1.12
     - Optional[str]
     - optional
     - Item #386
   * - ``dg1_13``
     - DG1.13
     - Optional[str]
     - optional
     - Item #387
   * - ``dg1_14``
     - DG1.14
     - Optional[str]
     - optional
     - Item #388
   * - ``dg1_15``
     - DG1.15
     - Optional[str]
     - optional
     - Item #389
   * - ``dg1_16``
     - DG1.16
     - Optional[str]
     - optional
     - Item #390

.. _hl7-v2_2-DSC:

DSC CONTINUATION POINTER (S2.10.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.DSC.DSC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``dsc_1``
     - DSC.1
     - Optional[str]
     - optional
     - Item #60

.. _hl7-v2_2-DSP:

DSP DISPLAY DATA (S2.10.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.DSP.DSP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``dsp_1``
     - DSP.1
     - Optional[str]
     - optional
     - Item #61
   * - ``dsp_2``
     - DSP.2
     - Optional[str]
     - optional
     - Item #62
   * - ``dsp_3``
     - DSP.3
     - str
     - required
     - Item #63
   * - ``dsp_4``
     - DSP.4
     - Optional[str]
     - optional
     - Item #64
   * - ``dsp_5``
     - DSP.5
     - Optional[str]
     - optional
     - Item #65

.. _hl7-v2_2-ERR:

ERR ERROR (S2.10.3).
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.ERR.ERR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``err_1``
     - ERR.1
     - List[str]
     - required
     - Item #24 | Table HL70060

.. _hl7-v2_2-EVN:

EVN EVENT TYPE (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.EVN.EVN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``evn_1``
     - EVN.1
     - str
     - required
     - Item #99 | Table HL70003
   * - ``evn_2``
     - EVN.2
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     - Item #100
   * - ``evn_3``
     - EVN.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #101
   * - ``evn_4``
     - EVN.4
     - Optional[str]
     - optional
     - Item #102 | Table HL70062
   * - ``evn_5``
     - EVN.5
     - Optional[str]
     - optional
     - Item #103 | Table HL70188

.. _hl7-v2_2-FHS:

FHS FILE HEADER (S2.10.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.FHS.FHS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``fhs_1``
     - FHS.1
     - str
     - optional
     - Item #67
   * - ``fhs_2``
     - FHS.2
     - str
     - optional
     - Item #68
   * - ``fhs_3``
     - FHS.3
     - Optional[str]
     - optional
     - Item #69
   * - ``fhs_4``
     - FHS.4
     - Optional[str]
     - optional
     - Item #70
   * - ``fhs_5``
     - FHS.5
     - Optional[str]
     - optional
     - Item #71
   * - ``fhs_6``
     - FHS.6
     - Optional[str]
     - optional
     - Item #72
   * - ``fhs_7``
     - FHS.7
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #73
   * - ``fhs_8``
     - FHS.8
     - Optional[str]
     - optional
     - Item #74
   * - ``fhs_9``
     - FHS.9
     - Optional[str]
     - optional
     - Item #75
   * - ``fhs_10``
     - FHS.10
     - Optional[str]
     - optional
     - Item #76
   * - ``fhs_11``
     - FHS.11
     - Optional[str]
     - optional
     - Item #77
   * - ``fhs_12``
     - FHS.12
     - Optional[str]
     - optional
     - Item #78

.. _hl7-v2_2-FT1:

FT1 FINANCIAL TRANSACTION (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.FT1.FT1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ft1_1``
     - FT1.1
     - Optional[str]
     - optional
     - Item #355
   * - ``ft1_2``
     - FT1.2
     - Optional[str]
     - optional
     - Item #356
   * - ``ft1_3``
     - FT1.3
     - Optional[str]
     - optional
     - Item #357
   * - ``ft1_4``
     - FT1.4
     - str
     - required
     - Item #358
   * - ``ft1_5``
     - FT1.5
     - Optional[str]
     - optional
     - Item #359
   * - ``ft1_6``
     - FT1.6
     - str
     - required
     - Item #360 | Table HL70017
   * - ``ft1_7``
     - FT1.7
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #361 | Table HL70132
   * - ``ft1_8``
     - FT1.8
     - Optional[str]
     - optional
     - Item #362
   * - ``ft1_9``
     - FT1.9
     - Optional[str]
     - optional
     - Item #363
   * - ``ft1_10``
     - FT1.10
     - Optional[str]
     - optional
     - Item #364
   * - ``ft1_11``
     - FT1.11
     - Optional[str]
     - optional
     - Item #365
   * - ``ft1_12``
     - FT1.12
     - Optional[str]
     - optional
     - Item #366
   * - ``ft1_13``
     - FT1.13
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #367 | Table HL70049
   * - ``ft1_14``
     - FT1.14
     - str
     - required
     - Item #368 | Table HL70072
   * - ``ft1_15``
     - FT1.15
     - Optional[str]
     - optional
     - Item #369
   * - ``ft1_16``
     - FT1.16
     - Optional[str]
     - optional
     - Item #133 | Table HL70079
   * - ``ft1_17``
     - FT1.17
     - Optional[str]
     - optional
     - Item #370 | Table HL70024
   * - ``ft1_18``
     - FT1.18
     - Optional[str]
     - optional
     - Item #148 | Table HL70018
   * - ``ft1_19``
     - FT1.19
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #371 | Table HL70051
   * - ``ft1_20``
     - FT1.20
     - Optional[str]
     - optional
     - Item #372 | Table HL70084
   * - ``ft1_21``
     - FT1.21
     - Optional[str]
     - optional
     - Item #373
   * - ``ft1_22``
     - FT1.22
     - Optional[str]
     - optional
     - Item #374
   * - ``ft1_23``
     - FT1.23
     - Optional[str]
     - optional
     - Item #217

.. _hl7-v2_2-FTS:

FTS FILE TRAILER (S2.10.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.FTS.FTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``fts_1``
     - FTS.1
     - Optional[str]
     - optional
     - Item #79
   * - ``fts_2``
     - FTS.2
     - Optional[str]
     - optional
     - Item #80

.. _hl7-v2_2-GT1:

GT1 GUARANTOR (S6.4.4).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.GT1.GT1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``gt1_1``
     - GT1.1
     - str
     - required
     - Item #405
   * - ``gt1_2``
     - GT1.2
     - Optional[str]
     - optional
     - Item #406
   * - ``gt1_3``
     - GT1.3
     - :ref:`PN <hl7-v2_2-PN>`
     - required
     - Item #407
   * - ``gt1_4``
     - GT1.4
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     - Item #408
   * - ``gt1_5``
     - GT1.5
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     - Item #409
   * - ``gt1_6``
     - GT1.6
     - Optional[List[str]]
     - optional
     - Item #410
   * - ``gt1_7``
     - GT1.7
     - Optional[List[str]]
     - optional
     - Item #411
   * - ``gt1_8``
     - GT1.8
     - Optional[str]
     - optional
     - Item #412
   * - ``gt1_9``
     - GT1.9
     - Optional[str]
     - optional
     - Item #413 | Table HL70001
   * - ``gt1_10``
     - GT1.10
     - Optional[str]
     - optional
     - Item #414 | Table HL70068
   * - ``gt1_11``
     - GT1.11
     - Optional[str]
     - optional
     - Item #415 | Table HL70063
   * - ``gt1_12``
     - GT1.12
     - Optional[str]
     - optional
     - Item #416
   * - ``gt1_13``
     - GT1.13
     - Optional[str]
     - optional
     - Item #417
   * - ``gt1_14``
     - GT1.14
     - Optional[str]
     - optional
     - Item #418
   * - ``gt1_15``
     - GT1.15
     - Optional[str]
     - optional
     - Item #419
   * - ``gt1_16``
     - GT1.16
     - Optional[str]
     - optional
     - Item #420
   * - ``gt1_17``
     - GT1.17
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     - Item #421
   * - ``gt1_18``
     - GT1.18
     - Optional[List[str]]
     - optional
     - Item #422
   * - ``gt1_19``
     - GT1.19
     - Optional[str]
     - optional
     - Item #423
   * - ``gt1_20``
     - GT1.20
     - Optional[str]
     - optional
     - Item #424 | Table HL70066
   * - ``gt1_21``
     - GT1.21
     - Optional[str]
     - optional
     - Item #425

.. _hl7-v2_2-IN1:

IN1 INSURANCE (S6.4.5).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.IN1.IN1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``in1_1``
     - IN1.1
     - str
     - required
     - Item #426
   * - ``in1_2``
     - IN1.2
     - str
     - required
     - Item #368 | Table HL70072
   * - ``in1_3``
     - IN1.3
     - str
     - required
     - Item #428
   * - ``in1_4``
     - IN1.4
     - Optional[str]
     - optional
     - Item #429
   * - ``in1_5``
     - IN1.5
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     - Item #430
   * - ``in1_6``
     - IN1.6
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     - Item #431
   * - ``in1_7``
     - IN1.7
     - Optional[List[str]]
     - optional
     - Item #432
   * - ``in1_8``
     - IN1.8
     - Optional[str]
     - optional
     - Item #433
   * - ``in1_9``
     - IN1.9
     - Optional[str]
     - optional
     - Item #434
   * - ``in1_10``
     - IN1.10
     - Optional[str]
     - optional
     - Item #435
   * - ``in1_11``
     - IN1.11
     - Optional[str]
     - optional
     - Item #436
   * - ``in1_12``
     - IN1.12
     - Optional[str]
     - optional
     - Item #437
   * - ``in1_13``
     - IN1.13
     - Optional[str]
     - optional
     - Item #438
   * - ``in1_14``
     - IN1.14
     - Optional[str]
     - optional
     - Item #439
   * - ``in1_15``
     - IN1.15
     - Optional[str]
     - optional
     - Item #440 | Table HL70086
   * - ``in1_16``
     - IN1.16
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     - Item #441
   * - ``in1_17``
     - IN1.17
     - Optional[str]
     - optional
     - Item #442 | Table HL70063
   * - ``in1_18``
     - IN1.18
     - Optional[str]
     - optional
     - Item #443
   * - ``in1_19``
     - IN1.19
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     - Item #444
   * - ``in1_20``
     - IN1.20
     - Optional[str]
     - optional
     - Item #445 | Table HL70135
   * - ``in1_21``
     - IN1.21
     - Optional[str]
     - optional
     - Item #446 | Table HL70173
   * - ``in1_22``
     - IN1.22
     - Optional[str]
     - optional
     - Item #447
   * - ``in1_23``
     - IN1.23
     - Optional[str]
     - optional
     - Item #448 | Table HL70136
   * - ``in1_24``
     - IN1.24
     - Optional[str]
     - optional
     - Item #449
   * - ``in1_25``
     - IN1.25
     - Optional[str]
     - optional
     - Item #450
   * - ``in1_26``
     - IN1.26
     - Optional[str]
     - optional
     - Item #451
   * - ``in1_27``
     - IN1.27
     - Optional[str]
     - optional
     - Item #452 | Table HL70093
   * - ``in1_28``
     - IN1.28
     - Optional[str]
     - optional
     - Item #453
   * - ``in1_29``
     - IN1.29
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #454
   * - ``in1_30``
     - IN1.30
     - Optional[str]
     - optional
     - Item #455
   * - ``in1_31``
     - IN1.31
     - Optional[str]
     - optional
     - Item #456 | Table HL70098
   * - ``in1_32``
     - IN1.32
     - Optional[str]
     - optional
     - Item #457 | Table HL70022
   * - ``in1_33``
     - IN1.33
     - Optional[str]
     - optional
     - Item #458
   * - ``in1_34``
     - IN1.34
     - Optional[str]
     - optional
     - Item #459
   * - ``in1_35``
     - IN1.35
     - Optional[str]
     - optional
     - Item #460 | Table HL70042
   * - ``in1_36``
     - IN1.36
     - Optional[str]
     - optional
     - Item #461
   * - ``in1_37``
     - IN1.37
     - Optional[str]
     - optional
     - Item #462
   * - ``in1_38``
     - IN1.38
     - Optional[str]
     - optional
     - Item #463
   * - ``in1_39``
     - IN1.39
     - Optional[str]
     - optional
     - Item #464
   * - ``in1_40``
     - IN1.40
     - Optional[str]
     - optional
     - Item #465
   * - ``in1_41``
     - IN1.41
     - Optional[str]
     - optional
     - Item #466
   * - ``in1_42``
     - IN1.42
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #467 | Table HL70066
   * - ``in1_43``
     - IN1.43
     - Optional[str]
     - optional
     - Item #468 | Table HL70001
   * - ``in1_44``
     - IN1.44
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     - Item #469
   * - ``in1_45``
     - IN1.45
     - Optional[str]
     - optional
     - Item #470
   * - ``in1_46``
     - IN1.46
     - Optional[str]
     - optional
     - Item #471 | Table HL70072

.. _hl7-v2_2-IN2:

IN2 INSURANCE ADDITIONAL INFO (S6.4.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.IN2.IN2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``in2_1``
     - IN2.1
     - Optional[str]
     - optional
     - Item #472
   * - ``in2_2``
     - IN2.2
     - Optional[str]
     - optional
     - Item #473
   * - ``in2_3``
     - IN2.3
     - Optional[str]
     - optional
     - Item #474
   * - ``in2_4``
     - IN2.4
     - Optional[str]
     - optional
     - Item #475 | Table HL70139
   * - ``in2_5``
     - IN2.5
     - Optional[str]
     - optional
     - Item #476 | Table HL70137
   * - ``in2_6``
     - IN2.6
     - Optional[str]
     - optional
     - Item #477
   * - ``in2_7``
     - IN2.7
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     - Item #478
   * - ``in2_8``
     - IN2.8
     - Optional[str]
     - optional
     - Item #479
   * - ``in2_9``
     - IN2.9
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     - Item #480
   * - ``in2_10``
     - IN2.10
     - Optional[str]
     - optional
     - Item #481
   * - ``in2_11``
     - IN2.11
     - Optional[str]
     - optional
     - Item #482
   * - ``in2_12``
     - IN2.12
     - Optional[str]
     - optional
     - Item #483
   * - ``in2_13``
     - IN2.13
     - Optional[str]
     - optional
     - Item #484
   * - ``in2_14``
     - IN2.14
     - Optional[str]
     - optional
     - Item #485 | Table HL70140
   * - ``in2_15``
     - IN2.15
     - Optional[str]
     - optional
     - Item #486 | Table HL70141
   * - ``in2_16``
     - IN2.16
     - Optional[str]
     - optional
     - Item #487 | Table HL70142
   * - ``in2_17``
     - IN2.17
     - Optional[str]
     - optional
     - Item #488
   * - ``in2_18``
     - IN2.18
     - Optional[str]
     - optional
     - Item #489 | Table HL70136
   * - ``in2_19``
     - IN2.19
     - Optional[str]
     - optional
     - Item #490 | Table HL70136
   * - ``in2_20``
     - IN2.20
     - Optional[str]
     - optional
     - Item #491 | Table HL70136
   * - ``in2_21``
     - IN2.21
     - Optional[str]
     - optional
     - Item #531
   * - ``in2_22``
     - IN2.22
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     - Item #493
   * - ``in2_23``
     - IN2.23
     - Optional[str]
     - optional
     - Item #494
   * - ``in2_24``
     - IN2.24
     - Optional[List[str]]
     - optional
     - Item #495 | Table HL70143
   * - ``in2_25``
     - IN2.25
     - Optional[str]
     - optional
     - Item #496
   * - ``in2_26``
     - IN2.26
     - Optional[str]
     - optional
     - Item #497
   * - ``in2_27``
     - IN2.27
     - Optional[str]
     - optional
     - Item #498 | Table HL70144
   * - ``in2_28``
     - IN2.28
     - Optional[List[str]]
     - optional
     - Item #499 | Table HL70145
   * - ``in2_29``
     - IN2.29
     - Optional[List[str]]
     - optional
     - Item #500 | Table HL70147
   * - ``in2_30``
     - IN2.30
     - Optional[str]
     - optional
     - Item #501

.. _hl7-v2_2-IN3:

IN3 INSURANCE ADDITIONAL INFO-CERTIFICATION (S6.4.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.IN3.IN3
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``in3_1``
     - IN3.1
     - str
     - required
     - Item #502
   * - ``in3_2``
     - IN3.2
     - Optional[str]
     - optional
     - Item #503
   * - ``in3_3``
     - IN3.3
     - Optional[str]
     - optional
     - Item #504
   * - ``in3_4``
     - IN3.4
     - Optional[str]
     - optional
     - Item #505 | Table HL70136
   * - ``in3_5``
     - IN3.5
     - Optional[str]
     - optional
     - Item #506 | Table HL70148
   * - ``in3_6``
     - IN3.6
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #507
   * - ``in3_7``
     - IN3.7
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #508
   * - ``in3_8``
     - IN3.8
     - Optional[str]
     - optional
     - Item #509
   * - ``in3_9``
     - IN3.9
     - Optional[str]
     - optional
     - Item #510
   * - ``in3_10``
     - IN3.10
     - Optional[str]
     - optional
     - Item #511
   * - ``in3_11``
     - IN3.11
     - Optional[str]
     - optional
     - Item #512 | Table HL70149
   * - ``in3_12``
     - IN3.12
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #513
   * - ``in3_13``
     - IN3.13
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #514
   * - ``in3_14``
     - IN3.14
     - Optional[str]
     - optional
     - Item #515
   * - ``in3_15``
     - IN3.15
     - Optional[str]
     - optional
     - Item #516
   * - ``in3_16``
     - IN3.16
     - Optional[List[str]]
     - optional
     - Item #517
   * - ``in3_17``
     - IN3.17
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #518
   * - ``in3_18``
     - IN3.18
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #519
   * - ``in3_19``
     - IN3.19
     - Optional[List[str]]
     - optional
     - Item #520
   * - ``in3_20``
     - IN3.20
     - Optional[List[str]]
     - optional
     - Item #521 | Table HL70150
   * - ``in3_21``
     - IN3.21
     - Optional[str]
     - optional
     - Item #522
   * - ``in3_22``
     - IN3.22
     - Optional[str]
     - optional
     - Item #523
   * - ``in3_23``
     - IN3.23
     - Optional[str]
     - optional
     - Item #524 | Table HL70151
   * - ``in3_24``
     - IN3.24
     - Optional[str]
     - optional
     - Item #525 | Table HL70152
   * - ``in3_25``
     - IN3.25
     - Optional[str]
     - optional
     - Item #526

.. _hl7-v2_2-MFA:

MFA MASTER FILE ACKNOWLEDGEMENT (S8.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.MFA.MFA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``mfa_1``
     - MFA.1
     - str
     - required
     - Item #664 | Table HL70180
   * - ``mfa_2``
     - MFA.2
     - Optional[str]
     - optional
     - Item #665
   * - ``mfa_3``
     - MFA.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #668
   * - ``mfa_4``
     - MFA.4
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #669 | Table HL70181
   * - ``mfa_5``
     - MFA.5
     - List[:ref:`CE <hl7-v2_2-CE>`]
     - required
     - Item #667

.. _hl7-v2_2-MFE:

MFE MASTER FILE ENTRY (S8.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.MFE.MFE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``mfe_1``
     - MFE.1
     - str
     - required
     - Item #664 | Table HL70180
   * - ``mfe_2``
     - MFE.2
     - Optional[str]
     - optional
     - Item #665
   * - ``mfe_3``
     - MFE.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #662
   * - ``mfe_4``
     - MFE.4
     - List[:ref:`CE <hl7-v2_2-CE>`]
     - required
     - Item #667

.. _hl7-v2_2-MFI:

MFI MASTER FILE IDENTIFICATION (S8.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.MFI.MFI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``mfi_1``
     - MFI.1
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #658 | Table HL70175
   * - ``mfi_2``
     - MFI.2
     - Optional[str]
     - optional
     - Item #659 | Table HL70176
   * - ``mfi_3``
     - MFI.3
     - str
     - required
     - Item #660 | Table HL70178
   * - ``mfi_4``
     - MFI.4
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #661
   * - ``mfi_5``
     - MFI.5
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #662
   * - ``mfi_6``
     - MFI.6
     - str
     - required
     - Item #663 | Table HL70179

.. _hl7-v2_2-MRG:

MRG MERGE PATIENT INFORMATION (S3.3.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.MRG.MRG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``mrg_1``
     - MRG.1
     - str
     - required
     - Item #211
   * - ``mrg_2``
     - MRG.2
     - Optional[str]
     - optional
     - Item #212
   * - ``mrg_3``
     - MRG.3
     - Optional[str]
     - optional
     - Item #213
   * - ``mrg_4``
     - MRG.4
     - Optional[str]
     - optional
     - Item #214

.. _hl7-v2_2-MSA:

MSA MESSAGE ACKNOWLEDGMENT (S2.10.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.MSA.MSA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``msa_1``
     - MSA.1
     - str
     - required
     - Item #18 | Table HL70008
   * - ``msa_2``
     - MSA.2
     - str
     - required
     - Item #10
   * - ``msa_3``
     - MSA.3
     - Optional[str]
     - optional
     - Item #20
   * - ``msa_4``
     - MSA.4
     - Optional[str]
     - optional
     - Item #21
   * - ``msa_5``
     - MSA.5
     - Optional[str]
     - optional
     - Item #22 | Table HL70102
   * - ``msa_6``
     - MSA.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #23

.. _hl7-v2_2-MSH:

MSH MESSAGE HEADER (S2.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.MSH.MSH
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``msh_1``
     - MSH.1
     - str
     - optional
     - Item #1
   * - ``msh_2``
     - MSH.2
     - str
     - optional
     - Item #2
   * - ``msh_3``
     - MSH.3
     - Optional[str]
     - optional
     - Item #3
   * - ``msh_4``
     - MSH.4
     - Optional[str]
     - optional
     - Item #4
   * - ``msh_5``
     - MSH.5
     - Optional[str]
     - optional
     - Item #5
   * - ``msh_6``
     - MSH.6
     - Optional[str]
     - optional
     - Item #6
   * - ``msh_7``
     - MSH.7
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #7
   * - ``msh_8``
     - MSH.8
     - Optional[str]
     - optional
     - Item #8
   * - ``msh_9``
     - MSH.9
     - str
     - required
     - Item #9 | Table HL70076
   * - ``msh_10``
     - MSH.10
     - str
     - required
     - Item #10
   * - ``msh_11``
     - MSH.11
     - str
     - required
     - Item #11 | Table HL70103
   * - ``msh_12``
     - MSH.12
     - str
     - required
     - Item #12 | Table HL70104
   * - ``msh_13``
     - MSH.13
     - Optional[str]
     - optional
     - Item #13
   * - ``msh_14``
     - MSH.14
     - Optional[str]
     - optional
     - Item #14
   * - ``msh_15``
     - MSH.15
     - Optional[str]
     - optional
     - Item #15 | Table HL70155
   * - ``msh_16``
     - MSH.16
     - Optional[str]
     - optional
     - Item #16 | Table HL70155
   * - ``msh_17``
     - MSH.17
     - Optional[str]
     - optional
     - Item #17

.. _hl7-v2_2-NCK:

NCK System Clock.
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.NCK.NCK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``nck_1``
     - NCK.1
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     - Item #742

.. _hl7-v2_2-NK1:

NK1 NEXT OF KIN (S3.3.5).
~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.NK1.NK1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``nk1_1``
     - NK1.1
     - str
     - required
     - Item #190
   * - ``nk1_2``
     - NK1.2
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     - Item #191
   * - ``nk1_3``
     - NK1.3
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #192 | Table HL70063
   * - ``nk1_4``
     - NK1.4
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     - Item #193
   * - ``nk1_5``
     - NK1.5
     - Optional[List[str]]
     - optional
     - Item #194
   * - ``nk1_6``
     - NK1.6
     - Optional[str]
     - optional
     - Item #195
   * - ``nk1_7``
     - NK1.7
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #196 | Table HL70131
   * - ``nk1_8``
     - NK1.8
     - Optional[str]
     - optional
     - Item #197
   * - ``nk1_9``
     - NK1.9
     - Optional[str]
     - optional
     - Item #198
   * - ``nk1_10``
     - NK1.10
     - Optional[str]
     - optional
     - Item #199
   * - ``nk1_11``
     - NK1.11
     - Optional[str]
     - optional
     - Item #200
   * - ``nk1_12``
     - NK1.12
     - Optional[str]
     - optional
     - Item #201
   * - ``nk1_13``
     - NK1.13
     - Optional[str]
     - optional
     - Item #202

.. _hl7-v2_2-NPU:

NPU BED STATUS UPDATE (S3.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.NPU.NPU
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``npu_1``
     - NPU.1
     - str
     - required
     - Item #209 | Table HL70079
   * - ``npu_2``
     - NPU.2
     - Optional[str]
     - optional
     - Item #170 | Table HL70116

.. _hl7-v2_2-NSC:

NSC STATUS CHANGE.
~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.NSC.NSC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``nsc_1``
     - NSC.1
     - str
     - required
     - Item #758
   * - ``nsc_2``
     - NSC.2
     - Optional[str]
     - optional
     - Item #759
   * - ``nsc_3``
     - NSC.3
     - Optional[str]
     - optional
     - Item #760
   * - ``nsc_4``
     - NSC.4
     - Optional[str]
     - optional
     - Item #761
   * - ``nsc_5``
     - NSC.5
     - Optional[str]
     - optional
     - Item #762
   * - ``nsc_6``
     - NSC.6
     - Optional[str]
     - optional
     - Item #763
   * - ``nsc_7``
     - NSC.7
     - Optional[str]
     - optional
     - Item #764
   * - ``nsc_8``
     - NSC.8
     - Optional[str]
     - optional
     - Item #765
   * - ``nsc_9``
     - NSC.9
     - Optional[str]
     - optional
     - Item #766

.. _hl7-v2_2-NST:

NST Statistics.
~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.NST.NST
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``nst_1``
     - NST.1
     - str
     - required
     - Item #743 | Table HL70136
   * - ``nst_2``
     - NST.2
     - Optional[str]
     - optional
     - Item #744
   * - ``nst_3``
     - NST.3
     - Optional[str]
     - optional
     - Item #745
   * - ``nst_4``
     - NST.4
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #746
   * - ``nst_5``
     - NST.5
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #747
   * - ``nst_6``
     - NST.6
     - Optional[str]
     - optional
     - Item #748
   * - ``nst_7``
     - NST.7
     - Optional[str]
     - optional
     - Item #749
   * - ``nst_8``
     - NST.8
     - Optional[str]
     - optional
     - Item #750
   * - ``nst_9``
     - NST.9
     - Optional[str]
     - optional
     - Item #751
   * - ``nst_10``
     - NST.10
     - Optional[str]
     - optional
     - Item #752
   * - ``nst_11``
     - NST.11
     - Optional[str]
     - optional
     - Item #753
   * - ``nst_12``
     - NST.12
     - Optional[str]
     - optional
     - Item #754
   * - ``nst_13``
     - NST.13
     - Optional[str]
     - optional
     - Item #755
   * - ``nst_14``
     - NST.14
     - Optional[str]
     - optional
     - Item #756
   * - ``nst_15``
     - NST.15
     - Optional[str]
     - optional
     - Item #757

.. _hl7-v2_2-NTE:

NTE NOTES AND COMMENTS (S2.10.15).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.NTE.NTE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``nte_1``
     - NTE.1
     - Optional[str]
     - optional
     - Item #96
   * - ``nte_2``
     - NTE.2
     - Optional[str]
     - optional
     - Item #97 | Table HL70105
   * - ``nte_3``
     - NTE.3
     - Optional[List[str]]
     - optional
     - Item #98

.. _hl7-v2_2-OBR:

OBR OBSERVATION REQUEST (S7.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.OBR.OBR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``obr_1``
     - OBR.1
     - Optional[str]
     - optional
     - Item #237
   * - ``obr_2``
     - OBR.2
     - Optional[str]
     - optional
     - Item #216
   * - ``obr_3``
     - OBR.3
     - Optional[str]
     - optional
     - Item #217
   * - ``obr_4``
     - OBR.4
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #238
   * - ``obr_5``
     - OBR.5
     - Optional[str]
     - optional
     - Item #239
   * - ``obr_6``
     - OBR.6
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #240
   * - ``obr_7``
     - OBR.7
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #241
   * - ``obr_8``
     - OBR.8
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #242
   * - ``obr_9``
     - OBR.9
     - Optional[str]
     - optional
     - Item #243
   * - ``obr_10``
     - OBR.10
     - Optional[List[str]]
     - optional
     - Item #244
   * - ``obr_11``
     - OBR.11
     - Optional[str]
     - optional
     - Item #245 | Table HL70065
   * - ``obr_12``
     - OBR.12
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #246
   * - ``obr_13``
     - OBR.13
     - Optional[str]
     - optional
     - Item #247
   * - ``obr_14``
     - OBR.14
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #248
   * - ``obr_15``
     - OBR.15
     - Optional[str]
     - optional
     - Item #249 | Table HL70070
   * - ``obr_16``
     - OBR.16
     - Optional[str]
     - optional
     - Item #226
   * - ``obr_17``
     - OBR.17
     - Optional[List[str]]
     - optional
     - Item #250
   * - ``obr_18``
     - OBR.18
     - Optional[str]
     - optional
     - Item #251
   * - ``obr_19``
     - OBR.19
     - Optional[str]
     - optional
     - Item #252
   * - ``obr_20``
     - OBR.20
     - Optional[str]
     - optional
     - Item #253
   * - ``obr_21``
     - OBR.21
     - Optional[str]
     - optional
     - Item #254
   * - ``obr_22``
     - OBR.22
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #255
   * - ``obr_23``
     - OBR.23
     - Optional[str]
     - optional
     - Item #256
   * - ``obr_24``
     - OBR.24
     - Optional[str]
     - optional
     - Item #257 | Table HL70074
   * - ``obr_25``
     - OBR.25
     - Optional[str]
     - optional
     - Item #258 | Table HL70123
   * - ``obr_26``
     - OBR.26
     - Optional[str]
     - optional
     - Item #259
   * - ``obr_27``
     - OBR.27
     - Optional[List[:ref:`TQ <hl7-v2_2-TQ>`]]
     - optional
     - Item #221
   * - ``obr_28``
     - OBR.28
     - Optional[List[str]]
     - optional
     - Item #260
   * - ``obr_29``
     - OBR.29
     - Optional[str]
     - optional
     - Item #261
   * - ``obr_30``
     - OBR.30
     - Optional[str]
     - optional
     - Item #262 | Table HL70124
   * - ``obr_31``
     - OBR.31
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #263
   * - ``obr_32``
     - OBR.32
     - Optional[str]
     - optional
     - Item #264
   * - ``obr_33``
     - OBR.33
     - Optional[List[str]]
     - optional
     - Item #265
   * - ``obr_34``
     - OBR.34
     - Optional[List[str]]
     - optional
     - Item #266
   * - ``obr_35``
     - OBR.35
     - Optional[List[str]]
     - optional
     - Item #267
   * - ``obr_36``
     - OBR.36
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #268

.. _hl7-v2_2-OBX:

OBX OBSERVATION RESULT (S7.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.OBX.OBX
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``obx_1``
     - OBX.1
     - Optional[str]
     - optional
     - Item #569
   * - ``obx_2``
     - OBX.2
     - str
     - required
     - Item #570 | Table HL70125
   * - ``obx_3``
     - OBX.3
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #571
   * - ``obx_4``
     - OBX.4
     - Optional[str]
     - optional
     - Item #572
   * - ``obx_5``
     - OBX.5
     - Optional[str]
     - optional
     - Item #573
   * - ``obx_6``
     - OBX.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #574
   * - ``obx_7``
     - OBX.7
     - Optional[str]
     - optional
     - Item #575
   * - ``obx_8``
     - OBX.8
     - Optional[List[str]]
     - optional
     - Item #576 | Table HL70078
   * - ``obx_9``
     - OBX.9
     - Optional[str]
     - optional
     - Item #577
   * - ``obx_10``
     - OBX.10
     - Optional[str]
     - optional
     - Item #578 | Table HL70080
   * - ``obx_11``
     - OBX.11
     - str
     - required
     - Item #579 | Table HL70085
   * - ``obx_12``
     - OBX.12
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #580
   * - ``obx_13``
     - OBX.13
     - Optional[str]
     - optional
     - Item #581
   * - ``obx_14``
     - OBX.14
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #582
   * - ``obx_15``
     - OBX.15
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #583
   * - ``obx_16``
     - OBX.16
     - Optional[str]
     - optional
     - Item #584

.. _hl7-v2_2-ODS:

ODS DIETARY ORDERS, SUPPLEMENTS, and PREFERENCES (S4.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.ODS.ODS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ods_1``
     - ODS.1
     - str
     - required
     - Item #269 | Table HL70159
   * - ``ods_2``
     - ODS.2
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #270
   * - ``ods_3``
     - ODS.3
     - List[:ref:`CE <hl7-v2_2-CE>`]
     - required
     - Item #271
   * - ``ods_4``
     - ODS.4
     - Optional[List[str]]
     - optional
     - Item #272

.. _hl7-v2_2-ODT:

ODT DIET TRAY INSTRUCTION (S4.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.ODT.ODT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``odt_1``
     - ODT.1
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #273 | Table HL70160
   * - ``odt_2``
     - ODT.2
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #270
   * - ``odt_3``
     - ODT.3
     - Optional[List[str]]
     - optional
     - Item #272

.. _hl7-v2_2-OM1:

OM1 GENERAL - fields that apply to most observations (S7.6.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.OM1.OM1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``om1_1``
     - OM1.1
     - Optional[str]
     - optional
     - Item #585
   * - ``om1_2``
     - OM1.2
     - Optional[str]
     - optional
     - Item #586
   * - ``om1_3``
     - OM1.3
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #587
   * - ``om1_4``
     - OM1.4
     - Optional[List[str]]
     - optional
     - Item #588 | Table HL70125
   * - ``om1_5``
     - OM1.5
     - str
     - required
     - Item #589 | Table HL70136
   * - ``om1_6``
     - OM1.6
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #590
   * - ``om1_7``
     - OM1.7
     - Optional[str]
     - optional
     - Item #591
   * - ``om1_8``
     - OM1.8
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #592
   * - ``om1_9``
     - OM1.9
     - List[str]
     - required
     - Item #593
   * - ``om1_10``
     - OM1.10
     - Optional[str]
     - optional
     - Item #594
   * - ``om1_11``
     - OM1.11
     - Optional[str]
     - optional
     - Item #595
   * - ``om1_12``
     - OM1.12
     - Optional[str]
     - optional
     - Item #596
   * - ``om1_13``
     - OM1.13
     - Optional[str]
     - optional
     - Item #597 | Table HL70136
   * - ``om1_14``
     - OM1.14
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #598
   * - ``om1_15``
     - OM1.15
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #599
   * - ``om1_16``
     - OM1.16
     - Optional[str]
     - optional
     - Item #600 | Table HL70136
   * - ``om1_17``
     - OM1.17
     - Optional[List[str]]
     - optional
     - Item #601
   * - ``om1_18``
     - OM1.18
     - Optional[str]
     - optional
     - Item #602
   * - ``om1_19``
     - OM1.19
     - str
     - required
     - Item #603 | Table HL70174
   * - ``om1_20``
     - OM1.20
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #604
   * - ``om1_21``
     - OM1.21
     - Optional[str]
     - optional
     - Item #605
   * - ``om1_22``
     - OM1.22
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     - Item #606
   * - ``om1_23``
     - OM1.23
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #607
   * - ``om1_24``
     - OM1.24
     - Optional[str]
     - optional
     - Item #608
   * - ``om1_25``
     - OM1.25
     - Optional[str]
     - optional
     - Item #609
   * - ``om1_26``
     - OM1.26
     - Optional[List[str]]
     - optional
     - Item #610 | Table HL70168
   * - ``om1_27``
     - OM1.27
     - Optional[str]
     - optional
     - Item #611 | Table HL70169
   * - ``om1_28``
     - OM1.28
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #612
   * - ``om1_29``
     - OM1.29
     - Optional[List[:ref:`AD <hl7-v2_2-AD>`]]
     - optional
     - Item #613
   * - ``om1_30``
     - OM1.30
     - Optional[List[str]]
     - optional
     - Item #614
   * - ``om1_31``
     - OM1.31
     - Optional[str]
     - optional
     - Item #615 | Table HL70177
   * - ``om1_32``
     - OM1.32
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #616
   * - ``om1_33``
     - OM1.33
     - Optional[str]
     - optional
     - Item #617
   * - ``om1_34``
     - OM1.34
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #618
   * - ``om1_35``
     - OM1.35
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #619
   * - ``om1_36``
     - OM1.36
     - Optional[str]
     - optional
     - Item #620
   * - ``om1_37``
     - OM1.37
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #621
   * - ``om1_38``
     - OM1.38
     - Optional[str]
     - optional
     - Item #622
   * - ``om1_39``
     - OM1.39
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #623
   * - ``om1_40``
     - OM1.40
     - Optional[str]
     - optional
     - Item #624
   * - ``om1_41``
     - OM1.41
     - Optional[List[str]]
     - optional
     - Item #625
   * - ``om1_42``
     - OM1.42
     - Optional[str]
     - optional
     - Item #626

.. _hl7-v2_2-OM2:

OM2 NUMERIC OBSERVATION (S7.6.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.OM2.OM2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``om2_1``
     - OM2.1
     - Optional[str]
     - optional
     - Item #585
   * - ``om2_2``
     - OM2.2
     - Optional[str]
     - optional
     - Item #586
   * - ``om2_3``
     - OM2.3
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #627
   * - ``om2_4``
     - OM2.4
     - Optional[str]
     - optional
     - Item #628
   * - ``om2_5``
     - OM2.5
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #629
   * - ``om2_6``
     - OM2.6
     - List[str]
     - required
     - Item #630
   * - ``om2_7``
     - OM2.7
     - Optional[List[str]]
     - optional
     - Item #631
   * - ``om2_8``
     - OM2.8
     - Optional[str]
     - optional
     - Item #632
   * - ``om2_9``
     - OM2.9
     - Optional[str]
     - optional
     - Item #633
   * - ``om2_10``
     - OM2.10
     - Optional[List[str]]
     - optional
     - Item #634
   * - ``om2_11``
     - OM2.11
     - Optional[str]
     - optional
     - Item #635

.. _hl7-v2_2-OM3:

OM3 CATEGORICAL TEST/OBSERVATION (S7.6.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.OM3.OM3
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``om3_1``
     - OM3.1
     - Optional[str]
     - optional
     - Item #585
   * - ``om3_2``
     - OM3.2
     - Optional[str]
     - optional
     - Item #586
   * - ``om3_3``
     - OM3.3
     - Optional[str]
     - optional
     - Item #636
   * - ``om3_4``
     - OM3.4
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #637
   * - ``om3_5``
     - OM3.5
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #638
   * - ``om3_6``
     - OM3.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #639
   * - ``om3_7``
     - OM3.7
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #640
   * - ``om3_8``
     - OM3.8
     - Optional[str]
     - optional
     - Item #641

.. _hl7-v2_2-OM4:

OM4 OBSERVATION that require specimens (S7.6.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.OM4.OM4
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``om4_1``
     - OM4.1
     - Optional[str]
     - optional
     - Item #585
   * - ``om4_2``
     - OM4.2
     - Optional[str]
     - optional
     - Item #586
   * - ``om4_3``
     - OM4.3
     - Optional[str]
     - optional
     - Item #642 | Table HL70170
   * - ``om4_4``
     - OM4.4
     - Optional[str]
     - optional
     - Item #643
   * - ``om4_5``
     - OM4.5
     - Optional[str]
     - optional
     - Item #644
   * - ``om4_6``
     - OM4.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #645
   * - ``om4_7``
     - OM4.7
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #646
   * - ``om4_8``
     - OM4.8
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #647
   * - ``om4_9``
     - OM4.9
     - Optional[str]
     - optional
     - Item #648
   * - ``om4_10``
     - OM4.10
     - Optional[str]
     - optional
     - Item #649
   * - ``om4_11``
     - OM4.11
     - Optional[str]
     - optional
     - Item #650
   * - ``om4_12``
     - OM4.12
     - Optional[str]
     - optional
     - Item #651
   * - ``om4_13``
     - OM4.13
     - Optional[str]
     - optional
     - Item #652
   * - ``om4_14``
     - OM4.14
     - Optional[List[str]]
     - optional
     - Item #653 | Table HL70027
   * - ``om4_15``
     - OM4.15
     - Optional[str]
     - optional
     - Item #654

.. _hl7-v2_2-OM5:

OM5 OBSERVATION BATTERIES (S7.6.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.OM5.OM5
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``om5_1``
     - OM5.1
     - Optional[str]
     - optional
     - Item #585
   * - ``om5_2``
     - OM5.2
     - Optional[str]
     - optional
     - Item #586
   * - ``om5_3``
     - OM5.3
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #655
   * - ``om5_4``
     - OM5.4
     - Optional[str]
     - optional
     - Item #656

.. _hl7-v2_2-OM6:

OM6 OBSERVATIONS that are calculated from other obersvations (S7.6.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.OM6.OM6
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``om6_1``
     - OM6.1
     - Optional[str]
     - optional
     - Item #585
   * - ``om6_2``
     - OM6.2
     - Optional[str]
     - optional
     - Item #586
   * - ``om6_3``
     - OM6.3
     - Optional[str]
     - optional
     - Item #657

.. _hl7-v2_2-ORC:

ORC COMMOM ORDER (S4.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.ORC.ORC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``orc_1``
     - ORC.1
     - str
     - required
     - Item #215 | Table HL70119
   * - ``orc_2``
     - ORC.2
     - Optional[str]
     - optional
     - Item #216
   * - ``orc_3``
     - ORC.3
     - Optional[str]
     - optional
     - Item #217
   * - ``orc_4``
     - ORC.4
     - Optional[str]
     - optional
     - Item #218
   * - ``orc_5``
     - ORC.5
     - Optional[str]
     - optional
     - Item #219 | Table HL70038
   * - ``orc_6``
     - ORC.6
     - Optional[str]
     - optional
     - Item #220 | Table HL70121
   * - ``orc_7``
     - ORC.7
     - Optional[List[:ref:`TQ <hl7-v2_2-TQ>`]]
     - optional
     - Item #221
   * - ``orc_8``
     - ORC.8
     - Optional[str]
     - optional
     - Item #222
   * - ``orc_9``
     - ORC.9
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #223
   * - ``orc_10``
     - ORC.10
     - Optional[str]
     - optional
     - Item #224
   * - ``orc_11``
     - ORC.11
     - Optional[str]
     - optional
     - Item #225
   * - ``orc_12``
     - ORC.12
     - Optional[str]
     - optional
     - Item #226
   * - ``orc_13``
     - ORC.13
     - Optional[str]
     - optional
     - Item #227
   * - ``orc_14``
     - ORC.14
     - Optional[List[str]]
     - optional
     - Item #228
   * - ``orc_15``
     - ORC.15
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #229
   * - ``orc_16``
     - ORC.16
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #230
   * - ``orc_17``
     - ORC.17
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #231
   * - ``orc_18``
     - ORC.18
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #232
   * - ``orc_19``
     - ORC.19
     - Optional[str]
     - optional
     - Item #233

.. _hl7-v2_2-PID:

PID PATIENT IDENTIFICATION (S3.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.PID.PID
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pid_1``
     - PID.1
     - Optional[str]
     - optional
     - Item #104
   * - ``pid_2``
     - PID.2
     - Optional[str]
     - optional
     - Item #105
   * - ``pid_3``
     - PID.3
     - List[str]
     - required
     - Item #106
   * - ``pid_4``
     - PID.4
     - Optional[str]
     - optional
     - Item #107
   * - ``pid_5``
     - PID.5
     - :ref:`PN <hl7-v2_2-PN>`
     - required
     - Item #108
   * - ``pid_6``
     - PID.6
     - Optional[str]
     - optional
     - Item #109
   * - ``pid_7``
     - PID.7
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #110
   * - ``pid_8``
     - PID.8
     - Optional[str]
     - optional
     - Item #111 | Table HL70001
   * - ``pid_9``
     - PID.9
     - Optional[List[:ref:`PN <hl7-v2_2-PN>`]]
     - optional
     - Item #112
   * - ``pid_10``
     - PID.10
     - Optional[str]
     - optional
     - Item #113 | Table HL70005
   * - ``pid_11``
     - PID.11
     - Optional[List[:ref:`AD <hl7-v2_2-AD>`]]
     - optional
     - Item #114
   * - ``pid_12``
     - PID.12
     - Optional[str]
     - optional
     - Item #115
   * - ``pid_13``
     - PID.13
     - Optional[List[str]]
     - optional
     - Item #116
   * - ``pid_14``
     - PID.14
     - Optional[List[str]]
     - optional
     - Item #117
   * - ``pid_15``
     - PID.15
     - Optional[str]
     - optional
     - Item #118
   * - ``pid_16``
     - PID.16
     - Optional[str]
     - optional
     - Item #119 | Table HL70002
   * - ``pid_17``
     - PID.17
     - Optional[str]
     - optional
     - Item #120 | Table HL70006
   * - ``pid_18``
     - PID.18
     - Optional[str]
     - optional
     - Item #121
   * - ``pid_19``
     - PID.19
     - Optional[str]
     - optional
     - Item #122
   * - ``pid_20``
     - PID.20
     - Optional[str]
     - optional
     - Item #123
   * - ``pid_21``
     - PID.21
     - Optional[str]
     - optional
     - Item #124
   * - ``pid_22``
     - PID.22
     - Optional[str]
     - optional
     - Item #125 | Table HL70189
   * - ``pid_23``
     - PID.23
     - Optional[str]
     - optional
     - Item #126
   * - ``pid_24``
     - PID.24
     - Optional[str]
     - optional
     - Item #127
   * - ``pid_25``
     - PID.25
     - Optional[str]
     - optional
     - Item #128
   * - ``pid_26``
     - PID.26
     - Optional[List[str]]
     - optional
     - Item #129 | Table HL70171
   * - ``pid_27``
     - PID.27
     - Optional[str]
     - optional
     - Item #130

.. _hl7-v2_2-PR1:

PR1 PROCEDURES (S6.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.PR1.PR1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pr1_1``
     - PR1.1
     - str
     - required
     - Item #391
   * - ``pr1_2``
     - PR1.2
     - List[str]
     - required
     - Item #392 | Table HL70089
   * - ``pr1_3``
     - PR1.3
     - List[str]
     - required
     - Item #393 | Table HL70088
   * - ``pr1_4``
     - PR1.4
     - Optional[List[str]]
     - optional
     - Item #394
   * - ``pr1_5``
     - PR1.5
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     - Item #395
   * - ``pr1_6``
     - PR1.6
     - str
     - required
     - Item #396 | Table HL70090
   * - ``pr1_7``
     - PR1.7
     - Optional[str]
     - optional
     - Item #397
   * - ``pr1_8``
     - PR1.8
     - Optional[str]
     - optional
     - Item #398 | Table HL70010
   * - ``pr1_9``
     - PR1.9
     - Optional[str]
     - optional
     - Item #399 | Table HL70019
   * - ``pr1_10``
     - PR1.10
     - Optional[str]
     - optional
     - Item #400
   * - ``pr1_11``
     - PR1.11
     - Optional[str]
     - optional
     - Item #401 | Table HL70010
   * - ``pr1_12``
     - PR1.12
     - Optional[List[str]]
     - optional
     - Item #402 | Table HL70010
   * - ``pr1_13``
     - PR1.13
     - Optional[str]
     - optional
     - Item #403 | Table HL70059
   * - ``pr1_14``
     - PR1.14
     - Optional[str]
     - optional
     - Item #404

.. _hl7-v2_2-PRA:

PRA practitioner detail (S9.1.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.PRA.PRA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pra_1``
     - PRA.1
     - str
     - required
     - Item #685
   * - ``pra_2``
     - PRA.2
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #686
   * - ``pra_3``
     - PRA.3
     - Optional[List[str]]
     - optional
     - Item #687 | Table HL70186
   * - ``pra_4``
     - PRA.4
     - Optional[str]
     - optional
     - Item #688 | Table HL70187
   * - ``pra_5``
     - PRA.5
     - Optional[List[str]]
     - optional
     - Item #689
   * - ``pra_6``
     - PRA.6
     - Optional[List[str]]
     - optional
     - Item #690
   * - ``pra_7``
     - PRA.7
     - Optional[List[str]]
     - optional
     - Item #691

.. _hl7-v2_2-PV1:

PV1 PATIENT VISIT (S3.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.PV1.PV1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pv1_1``
     - PV1.1
     - Optional[str]
     - optional
     - Item #131
   * - ``pv1_2``
     - PV1.2
     - str
     - required
     - Item #132 | Table HL70004
   * - ``pv1_3``
     - PV1.3
     - Optional[str]
     - optional
     - Item #133 | Table HL70079
   * - ``pv1_4``
     - PV1.4
     - Optional[str]
     - optional
     - Item #134 | Table HL70007
   * - ``pv1_5``
     - PV1.5
     - Optional[str]
     - optional
     - Item #135
   * - ``pv1_6``
     - PV1.6
     - Optional[str]
     - optional
     - Item #136
   * - ``pv1_7``
     - PV1.7
     - Optional[str]
     - optional
     - Item #137 | Table HL70010
   * - ``pv1_8``
     - PV1.8
     - Optional[str]
     - optional
     - Item #138 | Table HL70010
   * - ``pv1_9``
     - PV1.9
     - Optional[List[str]]
     - optional
     - Item #139 | Table HL70010
   * - ``pv1_10``
     - PV1.10
     - Optional[str]
     - optional
     - Item #140 | Table HL70069
   * - ``pv1_11``
     - PV1.11
     - Optional[str]
     - optional
     - Item #141 | Table HL70079
   * - ``pv1_12``
     - PV1.12
     - Optional[str]
     - optional
     - Item #142 | Table HL70087
   * - ``pv1_13``
     - PV1.13
     - Optional[str]
     - optional
     - Item #143 | Table HL70092
   * - ``pv1_14``
     - PV1.14
     - Optional[str]
     - optional
     - Item #144 | Table HL70023
   * - ``pv1_15``
     - PV1.15
     - Optional[List[str]]
     - optional
     - Item #145 | Table HL70009
   * - ``pv1_16``
     - PV1.16
     - Optional[str]
     - optional
     - Item #146 | Table HL70099
   * - ``pv1_17``
     - PV1.17
     - Optional[str]
     - optional
     - Item #147 | Table HL70010
   * - ``pv1_18``
     - PV1.18
     - Optional[str]
     - optional
     - Item #148 | Table HL70018
   * - ``pv1_19``
     - PV1.19
     - Optional[str]
     - optional
     - Item #149
   * - ``pv1_20``
     - PV1.20
     - Optional[List[str]]
     - optional
     - Item #150 | Table HL70064
   * - ``pv1_21``
     - PV1.21
     - Optional[str]
     - optional
     - Item #151 | Table HL70032
   * - ``pv1_22``
     - PV1.22
     - Optional[str]
     - optional
     - Item #152 | Table HL70045
   * - ``pv1_23``
     - PV1.23
     - Optional[str]
     - optional
     - Item #153 | Table HL70046
   * - ``pv1_24``
     - PV1.24
     - Optional[List[str]]
     - optional
     - Item #154 | Table HL70044
   * - ``pv1_25``
     - PV1.25
     - Optional[List[str]]
     - optional
     - Item #155
   * - ``pv1_26``
     - PV1.26
     - Optional[List[str]]
     - optional
     - Item #156
   * - ``pv1_27``
     - PV1.27
     - Optional[List[str]]
     - optional
     - Item #157
   * - ``pv1_28``
     - PV1.28
     - Optional[str]
     - optional
     - Item #158 | Table HL70073
   * - ``pv1_29``
     - PV1.29
     - Optional[str]
     - optional
     - Item #159 | Table HL70110
   * - ``pv1_30``
     - PV1.30
     - Optional[str]
     - optional
     - Item #160
   * - ``pv1_31``
     - PV1.31
     - Optional[str]
     - optional
     - Item #161 | Table HL70021
   * - ``pv1_32``
     - PV1.32
     - Optional[str]
     - optional
     - Item #162
   * - ``pv1_33``
     - PV1.33
     - Optional[str]
     - optional
     - Item #163
   * - ``pv1_34``
     - PV1.34
     - Optional[str]
     - optional
     - Item #164 | Table HL70111
   * - ``pv1_35``
     - PV1.35
     - Optional[str]
     - optional
     - Item #165
   * - ``pv1_36``
     - PV1.36
     - Optional[str]
     - optional
     - Item #166 | Table HL70112
   * - ``pv1_37``
     - PV1.37
     - Optional[str]
     - optional
     - Item #167 | Table HL70113
   * - ``pv1_38``
     - PV1.38
     - Optional[str]
     - optional
     - Item #168 | Table HL70114
   * - ``pv1_39``
     - PV1.39
     - Optional[str]
     - optional
     - Item #169 | Table HL70115
   * - ``pv1_40``
     - PV1.40
     - Optional[str]
     - optional
     - Item #170 | Table HL70116
   * - ``pv1_41``
     - PV1.41
     - Optional[str]
     - optional
     - Item #171 | Table HL70117
   * - ``pv1_42``
     - PV1.42
     - Optional[str]
     - optional
     - Item #172
   * - ``pv1_43``
     - PV1.43
     - Optional[str]
     - optional
     - Item #173
   * - ``pv1_44``
     - PV1.44
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #174
   * - ``pv1_45``
     - PV1.45
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #175
   * - ``pv1_46``
     - PV1.46
     - Optional[str]
     - optional
     - Item #176
   * - ``pv1_47``
     - PV1.47
     - Optional[str]
     - optional
     - Item #177
   * - ``pv1_48``
     - PV1.48
     - Optional[str]
     - optional
     - Item #178
   * - ``pv1_49``
     - PV1.49
     - Optional[str]
     - optional
     - Item #179
   * - ``pv1_50``
     - PV1.50
     - Optional[str]
     - optional
     - Item #180

.. _hl7-v2_2-PV2:

PV2 PATIENT VISIT - additional information (S3.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.PV2.PV2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pv2_1``
     - PV2.1
     - Optional[str]
     - optional
     - Item #181
   * - ``pv2_2``
     - PV2.2
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #182 | Table HL70129
   * - ``pv2_3``
     - PV2.3
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #183
   * - ``pv2_4``
     - PV2.4
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #184
   * - ``pv2_5``
     - PV2.5
     - Optional[List[str]]
     - optional
     - Item #185
   * - ``pv2_6``
     - PV2.6
     - Optional[str]
     - optional
     - Item #186
   * - ``pv2_7``
     - PV2.7
     - Optional[str]
     - optional
     - Item #187 | Table HL70130
   * - ``pv2_8``
     - PV2.8
     - Optional[str]
     - optional
     - Item #188
   * - ``pv2_9``
     - PV2.9
     - Optional[str]
     - optional
     - Item #189

.. _hl7-v2_2-QRD:

QRD QUERY DEFINITION (S2.10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.QRD.QRD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``qrd_1``
     - QRD.1
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     - Item #25
   * - ``qrd_2``
     - QRD.2
     - str
     - required
     - Item #26 | Table HL70106
   * - ``qrd_3``
     - QRD.3
     - str
     - required
     - Item #27 | Table HL70091
   * - ``qrd_4``
     - QRD.4
     - str
     - required
     - Item #28
   * - ``qrd_5``
     - QRD.5
     - Optional[str]
     - optional
     - Item #29 | Table HL70107
   * - ``qrd_6``
     - QRD.6
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #30
   * - ``qrd_7``
     - QRD.7
     - str
     - required
     - Item #31 | Table HL70126
   * - ``qrd_8``
     - QRD.8
     - List[str]
     - required
     - Item #32
   * - ``qrd_9``
     - QRD.9
     - List[str]
     - required
     - Item #33 | Table HL70048
   * - ``qrd_10``
     - QRD.10
     - List[str]
     - required
     - Item #34
   * - ``qrd_11``
     - QRD.11
     - Optional[List[str]]
     - optional
     - Item #35
   * - ``qrd_12``
     - QRD.12
     - Optional[str]
     - optional
     - Item #36 | Table HL70108

.. _hl7-v2_2-QRF:

QRF QUERY FILTER (S2.10.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.QRF.QRF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``qrf_1``
     - QRF.1
     - List[str]
     - required
     - Item #37
   * - ``qrf_2``
     - QRF.2
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #38
   * - ``qrf_3``
     - QRF.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #39
   * - ``qrf_4``
     - QRF.4
     - Optional[List[str]]
     - optional
     - Item #40
   * - ``qrf_5``
     - QRF.5
     - Optional[List[str]]
     - optional
     - Item #41
   * - ``qrf_6``
     - QRF.6
     - Optional[List[str]]
     - optional
     - Item #42 | Table HL70156
   * - ``qrf_7``
     - QRF.7
     - Optional[List[str]]
     - optional
     - Item #43 | Table HL70157
   * - ``qrf_8``
     - QRF.8
     - Optional[List[str]]
     - optional
     - Item #44 | Table HL70158

.. _hl7-v2_2-RQ1:

RQ1 REQUISITION DETAIL-! (S4.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.RQ1.RQ1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rq1_1``
     - RQ1.1
     - Optional[str]
     - optional
     - Item #285
   * - ``rq1_2``
     - RQ1.2
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #286
   * - ``rq1_3``
     - RQ1.3
     - Optional[str]
     - optional
     - Item #287
   * - ``rq1_4``
     - RQ1.4
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #288
   * - ``rq1_5``
     - RQ1.5
     - Optional[str]
     - optional
     - Item #289
   * - ``rq1_6``
     - RQ1.6
     - Optional[str]
     - optional
     - Item #290 | Table HL70136
   * - ``rq1_7``
     - RQ1.7
     - Optional[str]
     - optional
     - Item #291 | Table HL70136

.. _hl7-v2_2-RQD:

RQD REQUISITION DETAIL (S4.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.RQD.RQD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rqd_1``
     - RQD.1
     - Optional[str]
     - optional
     - Item #275
   * - ``rqd_2``
     - RQD.2
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #276
   * - ``rqd_3``
     - RQD.3
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #277
   * - ``rqd_4``
     - RQD.4
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #278
   * - ``rqd_5``
     - RQD.5
     - Optional[str]
     - optional
     - Item #279
   * - ``rqd_6``
     - RQD.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #280
   * - ``rqd_7``
     - RQD.7
     - Optional[str]
     - optional
     - Item #281
   * - ``rqd_8``
     - RQD.8
     - Optional[str]
     - optional
     - Item #282
   * - ``rqd_9``
     - RQD.9
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #283
   * - ``rqd_10``
     - RQD.10
     - Optional[str]
     - optional
     - Item #284

.. _hl7-v2_2-RXA:

RXA PHARMACY AADMINISTRATION (S4.8.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.RXA.RXA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rxa_1``
     - RXA.1
     - str
     - required
     - Item #342
   * - ``rxa_2``
     - RXA.2
     - str
     - required
     - Item #344
   * - ``rxa_3``
     - RXA.3
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     - Item #345
   * - ``rxa_4``
     - RXA.4
     - :ref:`TS <hl7-v2_2-TS>`
     - required
     - Item #346
   * - ``rxa_5``
     - RXA.5
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #347
   * - ``rxa_6``
     - RXA.6
     - str
     - required
     - Item #348
   * - ``rxa_7``
     - RXA.7
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #349
   * - ``rxa_8``
     - RXA.8
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #350
   * - ``rxa_9``
     - RXA.9
     - Optional[str]
     - optional
     - Item #351
   * - ``rxa_10``
     - RXA.10
     - Optional[str]
     - optional
     - Item #352
   * - ``rxa_11``
     - RXA.11
     - Optional[str]
     - optional
     - Item #353
   * - ``rxa_12``
     - RXA.12
     - Optional[str]
     - optional
     - Item #354

.. _hl7-v2_2-RXC:

RXC PHARMACY COMPONENT ORDER (S4.8.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.RXC.RXC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rxc_1``
     - RXC.1
     - str
     - required
     - Item #313 | Table HL70166
   * - ``rxc_2``
     - RXC.2
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #314
   * - ``rxc_3``
     - RXC.3
     - str
     - required
     - Item #315
   * - ``rxc_4``
     - RXC.4
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #316

.. _hl7-v2_2-RXD:

RXD PHARMACY DISPENSE (S4.8.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.RXD.RXD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rxd_1``
     - RXD.1
     - Optional[str]
     - optional
     - Item #334
   * - ``rxd_2``
     - RXD.2
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #335
   * - ``rxd_3``
     - RXD.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #336
   * - ``rxd_4``
     - RXD.4
     - str
     - required
     - Item #337
   * - ``rxd_5``
     - RXD.5
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #338
   * - ``rxd_6``
     - RXD.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #339
   * - ``rxd_7``
     - RXD.7
     - str
     - required
     - Item #325
   * - ``rxd_8``
     - RXD.8
     - Optional[str]
     - optional
     - Item #326
   * - ``rxd_9``
     - RXD.9
     - Optional[List[str]]
     - optional
     - Item #340
   * - ``rxd_10``
     - RXD.10
     - Optional[str]
     - optional
     - Item #341
   * - ``rxd_11``
     - RXD.11
     - Optional[str]
     - optional
     - Item #322 | Table HL70167
   * - ``rxd_12``
     - RXD.12
     - Optional[str]
     - optional
     - Item #329
   * - ``rxd_13``
     - RXD.13
     - Optional[str]
     - optional
     - Item #299
   * - ``rxd_14``
     - RXD.14
     - Optional[str]
     - optional
     - Item #307
   * - ``rxd_15``
     - RXD.15
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #330

.. _hl7-v2_2-RXE:

RXE PHARMACY ENCODED ORDER (S4.8.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.RXE.RXE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rxe_1``
     - RXE.1
     - Optional[List[:ref:`TQ <hl7-v2_2-TQ>`]]
     - optional
     - Item #221
   * - ``rxe_2``
     - RXE.2
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #317
   * - ``rxe_3``
     - RXE.3
     - str
     - required
     - Item #318
   * - ``rxe_4``
     - RXE.4
     - Optional[str]
     - optional
     - Item #319
   * - ``rxe_5``
     - RXE.5
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #320
   * - ``rxe_6``
     - RXE.6
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #321
   * - ``rxe_7``
     - RXE.7
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #298
   * - ``rxe_8``
     - RXE.8
     - Optional[str]
     - optional
     - Item #299
   * - ``rxe_9``
     - RXE.9
     - Optional[str]
     - optional
     - Item #322 | Table HL70167
   * - ``rxe_10``
     - RXE.10
     - Optional[str]
     - optional
     - Item #323
   * - ``rxe_11``
     - RXE.11
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #324
   * - ``rxe_12``
     - RXE.12
     - Optional[str]
     - optional
     - Item #304
   * - ``rxe_13``
     - RXE.13
     - Optional[str]
     - optional
     - Item #305
   * - ``rxe_14``
     - RXE.14
     - Optional[str]
     - optional
     - Item #306
   * - ``rxe_15``
     - RXE.15
     - str
     - required
     - Item #325
   * - ``rxe_16``
     - RXE.16
     - Optional[str]
     - optional
     - Item #326
   * - ``rxe_17``
     - RXE.17
     - Optional[str]
     - optional
     - Item #327
   * - ``rxe_18``
     - RXE.18
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #328
   * - ``rxe_19``
     - RXE.19
     - Optional[str]
     - optional
     - Item #329
   * - ``rxe_20``
     - RXE.20
     - Optional[str]
     - optional
     - Item #307
   * - ``rxe_21``
     - RXE.21
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #330
   * - ``rxe_22``
     - RXE.22
     - Optional[str]
     - optional
     - Item #331
   * - ``rxe_23``
     - RXE.23
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #332
   * - ``rxe_24``
     - RXE.24
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #333

.. _hl7-v2_2-RXG:

RXG PHARMACY GIVE (S4.8.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.RXG.RXG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rxg_1``
     - RXG.1
     - str
     - required
     - Item #342
   * - ``rxg_2``
     - RXG.2
     - Optional[str]
     - optional
     - Item #334
   * - ``rxg_3``
     - RXG.3
     - Optional[List[:ref:`TQ <hl7-v2_2-TQ>`]]
     - optional
     - Item #221
   * - ``rxg_4``
     - RXG.4
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #317
   * - ``rxg_5``
     - RXG.5
     - str
     - required
     - Item #318
   * - ``rxg_6``
     - RXG.6
     - Optional[str]
     - optional
     - Item #319
   * - ``rxg_7``
     - RXG.7
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #320
   * - ``rxg_8``
     - RXG.8
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #321
   * - ``rxg_9``
     - RXG.9
     - Optional[str]
     - optional
     - Item #351
   * - ``rxg_10``
     - RXG.10
     - Optional[str]
     - optional
     - Item #322 | Table HL70167
   * - ``rxg_11``
     - RXG.11
     - Optional[str]
     - optional
     - Item #299
   * - ``rxg_12``
     - RXG.12
     - Optional[str]
     - optional
     - Item #307
   * - ``rxg_13``
     - RXG.13
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #343
   * - ``rxg_14``
     - RXG.14
     - Optional[str]
     - optional
     - Item #331
   * - ``rxg_15``
     - RXG.15
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #332
   * - ``rxg_16``
     - RXG.16
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #333

.. _hl7-v2_2-RXO:

RXO PHARMACY PRESCRIPTION ORDER (S4.8.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.RXO.RXO
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rxo_1``
     - RXO.1
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #292
   * - ``rxo_2``
     - RXO.2
     - str
     - required
     - Item #293
   * - ``rxo_3``
     - RXO.3
     - Optional[str]
     - optional
     - Item #294
   * - ``rxo_4``
     - RXO.4
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #295
   * - ``rxo_5``
     - RXO.5
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #296
   * - ``rxo_6``
     - RXO.6
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #297
   * - ``rxo_7``
     - RXO.7
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #298
   * - ``rxo_8``
     - RXO.8
     - Optional[str]
     - optional
     - Item #299
   * - ``rxo_9``
     - RXO.9
     - Optional[str]
     - optional
     - Item #300 | Table HL70161
   * - ``rxo_10``
     - RXO.10
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #301
   * - ``rxo_11``
     - RXO.11
     - Optional[str]
     - optional
     - Item #302
   * - ``rxo_12``
     - RXO.12
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #303
   * - ``rxo_13``
     - RXO.13
     - Optional[str]
     - optional
     - Item #304
   * - ``rxo_14``
     - RXO.14
     - Optional[str]
     - optional
     - Item #305
   * - ``rxo_15``
     - RXO.15
     - Optional[str]
     - optional
     - Item #306
   * - ``rxo_16``
     - RXO.16
     - Optional[str]
     - optional
     - Item #307
   * - ``rxo_17``
     - RXO.17
     - Optional[str]
     - optional
     - Item #308

.. _hl7-v2_2-RXR:

RXR PHARMACY ROUTE (S4.8.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.RXR.RXR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rxr_1``
     - RXR.1
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #309 | Table HL70162
   * - ``rxr_2``
     - RXR.2
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #310 | Table HL70163
   * - ``rxr_3``
     - RXR.3
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #311 | Table HL70164
   * - ``rxr_4``
     - RXR.4
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Item #312 | Table HL70165

.. _hl7-v2_2-STF:

STF staff identification segment (S9.1.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.STF.STF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``stf_1``
     - STF.1
     - :ref:`CE <hl7-v2_2-CE>`
     - required
     - Item #671
   * - ``stf_2``
     - STF.2
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #672
   * - ``stf_3``
     - STF.3
     - Optional[:ref:`PN <hl7-v2_2-PN>`]
     - optional
     - Item #673
   * - ``stf_4``
     - STF.4
     - Optional[List[str]]
     - optional
     - Item #674 | Table HL70182
   * - ``stf_5``
     - STF.5
     - Optional[str]
     - optional
     - Item #111 | Table HL70001
   * - ``stf_6``
     - STF.6
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #110
   * - ``stf_7``
     - STF.7
     - Optional[str]
     - optional
     - Item #675 | Table HL70183
   * - ``stf_8``
     - STF.8
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #676 | Table HL70184
   * - ``stf_9``
     - STF.9
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #677
   * - ``stf_10``
     - STF.10
     - Optional[List[str]]
     - optional
     - Item #678
   * - ``stf_11``
     - STF.11
     - Optional[List[:ref:`AD <hl7-v2_2-AD>`]]
     - optional
     - Item #679
   * - ``stf_12``
     - STF.12
     - Optional[List[str]]
     - optional
     - Item #680
   * - ``stf_13``
     - STF.13
     - Optional[List[str]]
     - optional
     - Item #681
   * - ``stf_14``
     - STF.14
     - Optional[List[:ref:`CE <hl7-v2_2-CE>`]]
     - optional
     - Item #682
   * - ``stf_15``
     - STF.15
     - Optional[List[str]]
     - optional
     - Item #683
   * - ``stf_16``
     - STF.16
     - Optional[str]
     - optional
     - Item #684 | Table HL70185

.. _hl7-v2_2-UB1:

UB1 UB82 DATA (S6.4.9).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.UB1.UB1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ub1_1``
     - UB1.1
     - Optional[str]
     - optional
     - Item #530
   * - ``ub1_2``
     - UB1.2
     - Optional[str]
     - optional
     - Item #492 | Table HL70136
   * - ``ub1_3``
     - UB1.3
     - Optional[str]
     - optional
     - Item #532
   * - ``ub1_4``
     - UB1.4
     - Optional[str]
     - optional
     - Item #533
   * - ``ub1_5``
     - UB1.5
     - Optional[str]
     - optional
     - Item #534
   * - ``ub1_6``
     - UB1.6
     - Optional[str]
     - optional
     - Item #535
   * - ``ub1_7``
     - UB1.7
     - Optional[List[str]]
     - optional
     - Item #536 | Table HL70043
   * - ``ub1_8``
     - UB1.8
     - Optional[str]
     - optional
     - Item #537
   * - ``ub1_9``
     - UB1.9
     - Optional[str]
     - optional
     - Item #538
   * - ``ub1_10``
     - UB1.10
     - Optional[List[str]]
     - optional
     - Item #539 | Table HL70153
   * - ``ub1_11``
     - UB1.11
     - Optional[str]
     - optional
     - Item #540
   * - ``ub1_12``
     - UB1.12
     - Optional[str]
     - optional
     - Item #541
   * - ``ub1_13``
     - UB1.13
     - Optional[str]
     - optional
     - Item #542
   * - ``ub1_14``
     - UB1.14
     - Optional[str]
     - optional
     - Item #543
   * - ``ub1_15``
     - UB1.15
     - Optional[str]
     - optional
     - Item #544
   * - ``ub1_16``
     - UB1.16
     - Optional[List[str]]
     - optional
     - Item #545
   * - ``ub1_17``
     - UB1.17
     - Optional[str]
     - optional
     - Item #546
   * - ``ub1_18``
     - UB1.18
     - Optional[str]
     - optional
     - Item #547
   * - ``ub1_19``
     - UB1.19
     - Optional[str]
     - optional
     - Item #548
   * - ``ub1_20``
     - UB1.20
     - Optional[str]
     - optional
     - Item #549
   * - ``ub1_21``
     - UB1.21
     - Optional[str]
     - optional
     - Item #550
   * - ``ub1_22``
     - UB1.22
     - Optional[str]
     - optional
     - Item #551
   * - ``ub1_23``
     - UB1.23
     - Optional[str]
     - optional
     - Item #552

.. _hl7-v2_2-UB2:

UB2 UB92 DATA (S6.4.10).
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.UB2.UB2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ub2_1``
     - UB2.1
     - Optional[str]
     - optional
     - Item #553
   * - ``ub2_2``
     - UB2.2
     - Optional[str]
     - optional
     - Item #554
   * - ``ub2_3``
     - UB2.3
     - Optional[List[str]]
     - optional
     - Item #555 | Table HL70043
   * - ``ub2_4``
     - UB2.4
     - Optional[str]
     - optional
     - Item #556
   * - ``ub2_5``
     - UB2.5
     - Optional[str]
     - optional
     - Item #557
   * - ``ub2_6``
     - UB2.6
     - Optional[List[str]]
     - optional
     - Item #558
   * - ``ub2_7``
     - UB2.7
     - Optional[List[str]]
     - optional
     - Item #559
   * - ``ub2_8``
     - UB2.8
     - Optional[List[str]]
     - optional
     - Item #560
   * - ``ub2_9``
     - UB2.9
     - Optional[List[str]]
     - optional
     - Item #561
   * - ``ub2_10``
     - UB2.10
     - Optional[List[str]]
     - optional
     - Item #562
   * - ``ub2_11``
     - UB2.11
     - Optional[str]
     - optional
     - Item #563
   * - ``ub2_12``
     - UB2.12
     - Optional[List[str]]
     - optional
     - Item #564
   * - ``ub2_13``
     - UB2.13
     - Optional[List[str]]
     - optional
     - Item #565
   * - ``ub2_14``
     - UB2.14
     - Optional[List[str]]
     - optional
     - Item #566
   * - ``ub2_15``
     - UB2.15
     - Optional[str]
     - optional
     - Item #567
   * - ``ub2_16``
     - UB2.16
     - Optional[List[str]]
     - optional
     - Item #568

.. _hl7-v2_2-URD:

URD RESULTS/UPDATE DEFINITION (S2.10.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.URD.URD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``urd_1``
     - URD.1
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #45
   * - ``urd_2``
     - URD.2
     - Optional[str]
     - optional
     - Item #46 | Table HL70109
   * - ``urd_3``
     - URD.3
     - List[str]
     - required
     - Item #47
   * - ``urd_4``
     - URD.4
     - Optional[List[str]]
     - optional
     - Item #48 | Table HL70048
   * - ``urd_5``
     - URD.5
     - Optional[List[str]]
     - optional
     - Item #49
   * - ``urd_6``
     - URD.6
     - Optional[List[str]]
     - optional
     - Item #50
   * - ``urd_7``
     - URD.7
     - Optional[str]
     - optional
     - Item #51 | Table HL70108

.. _hl7-v2_2-URS:

URS UNSOLICITED SELECTION (S2.10.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.segments.URS.URS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``urs_1``
     - URS.1
     - List[str]
     - required
     - Item #52
   * - ``urs_2``
     - URS.2
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #53
   * - ``urs_3``
     - URS.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Item #54
   * - ``urs_4``
     - URS.4
     - Optional[List[str]]
     - optional
     - Item #55
   * - ``urs_5``
     - URS.5
     - Optional[List[str]]
     - optional
     - Item #56
   * - ``urs_6``
     - URS.6
     - Optional[List[str]]
     - optional
     - Item #57 | Table HL70156
   * - ``urs_7``
     - URS.7
     - Optional[List[str]]
     - optional
     - Item #58 | Table HL70157
   * - ``urs_8``
     - URS.8
     - Optional[List[str]]
     - optional
     - Item #59 | Table HL70158
