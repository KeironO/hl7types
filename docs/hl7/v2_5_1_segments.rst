v2.5.1 Segments
===============

.. _hl7-v2_5_1-ABS:

ABS: Abstract
~~~~~~~~~~~~~

Section 6.5.12

.. py:class:: hl7types.hl7.v2_5_1.segments.ABS.ABS
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
     - ``abs_1``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     - 0010
     - 01514
     - Discharge Care Provider
   * - 2
     - ``abs_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0069
     - 01515
     - Transfer Medical Service Code
   * - 3
     - ``abs_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0421
     - 01516
     - Severity of Illness Code
   * - 4
     - ``abs_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01517
     - Date/Time of Attestation
   * - 5
     - ``abs_5``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 01518
     - Attested By
   * - 6
     - ``abs_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0422
     - 01519
     - Triage Code
   * - 7
     - ``abs_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01520
     - Abstract Completion Date/Time
   * - 8
     - ``abs_8``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 01521
     - Abstracted By
   * - 9
     - ``abs_9``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0423
     - 01522
     - Case Category Code
   * - 10
     - ``abs_10``
     - 1
     - str
     - O
     - 0136
     - 01523
     - Caesarian Section Indicator
   * - 11
     - ``abs_11``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0424
     - 01524
     - Gestation Category Code
   * - 12
     - ``abs_12``
     - 3
     - str
     - O
     -
     - 01525
     - Gestation Period - Weeks
   * - 13
     - ``abs_13``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0425
     - 01526
     - Newborn Code
   * - 14
     - ``abs_14``
     - 1
     - str
     - O
     - 0136
     - 01527
     - Stillborn Indicator

.. _hl7-v2_5_1-ACC:

ACC: Accident
~~~~~~~~~~~~~

Section 6.5.9

.. py:class:: hl7types.hl7.v2_5_1.segments.ACC.ACC
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
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00527
     - Accident Date/Time
   * - 2
     - ``acc_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0050
     - 00528
     - Accident Code
   * - 3
     - ``acc_3``
     - 25
     - str
     - O
     -
     - 00529
     - Accident Location
   * - 4
     - ``acc_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0347
     - 00812
     - Auto Accident State
   * - 5
     - ``acc_5``
     - 1
     - str
     - O
     - 0136
     - 00813
     - Accident Job Related Indicator
   * - 6
     - ``acc_6``
     - 12
     - str
     - O
     - 0136
     - 00814
     - Accident Death Indicator
   * - 7
     - ``acc_7``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 00224
     - Entered By
   * - 8
     - ``acc_8``
     - 25
     - str
     - O
     -
     - 01503
     - Accident Description
   * - 9
     - ``acc_9``
     - 80
     - str
     - O
     -
     - 01504
     - Brought In By
   * - 10
     - ``acc_10``
     - 1
     - str
     - O
     - 0136
     - 01505
     - Police Notified Indicator
   * - 11
     - ``acc_11``
     -
     - :ref:`XAD <hl7-v2_5_1-XAD>`
     - O
     -
     - 01853
     - Accident Address

.. _hl7-v2_5_1-ADD:

ADD: Addendum
~~~~~~~~~~~~~

Section 2.15.1

.. py:class:: hl7types.hl7.v2_5_1.segments.ADD.ADD
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

.. _hl7-v2_5_1-AFF:

AFF: Professional Affiliation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.4.1

.. py:class:: hl7types.hl7.v2_5_1.segments.AFF.AFF
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
     - ``aff_1``
     - 60
     - str
     - R
     -
     - 01427
     - Set ID - AFF
   * - 2
     - ``aff_2``
     -
     - :ref:`XON <hl7-v2_5_1-XON>`
     - R
     -
     - 01444
     - Professional Organization
   * - 3
     - ``aff_3``
     -
     - :ref:`XAD <hl7-v2_5_1-XAD>`
     - O
     -
     - 01445
     - Professional Organization Address
   * - 4
     - ``aff_4``
     -
     - list[:ref:`DR <hl7-v2_5_1-DR>`]
     - O
     -
     - 01446
     - Professional Organization Affiliation Date Range
   * - 5
     - ``aff_5``
     - 60
     - str
     - O
     -
     - 01447
     - Professional Affiliation Additional Information

.. _hl7-v2_5_1-AIG:

AIG: Appointment Information - General Resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.6.5

.. py:class:: hl7types.hl7.v2_5_1.segments.AIG.AIG
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
     - ``aig_1``
     - 4
     - str
     - R
     -
     - 00896
     - Set ID - AIG
   * - 2
     - ``aig_2``
     - 3
     - str
     - C
     - 0206
     - 00763
     - Segment Action Code
   * - 3
     - ``aig_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00897
     - Resource ID
   * - 4
     - ``aig_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00898
     - Resource Type
   * - 5
     - ``aig_5``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00899
     - Resource Group
   * - 6
     - ``aig_6``
     - 5
     - str
     - O
     -
     - 00900
     - Resource Quantity
   * - 7
     - ``aig_7``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00901
     - Resource Quantity Units
   * - 8
     - ``aig_8``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 01202
     - Start Date/Time
   * - 9
     - ``aig_9``
     - 20
     - str
     - C
     -
     - 00891
     - Start Date/Time Offset
   * - 10
     - ``aig_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00892
     - Start Date/Time Offset Units
   * - 11
     - ``aig_11``
     - 20
     - str
     - O
     -
     - 00893
     - Duration
   * - 12
     - ``aig_12``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00894
     - Duration Units
   * - 13
     - ``aig_13``
     - 10
     - str
     - C
     - 0279
     - 00895
     - Allow Substitution Code
   * - 14
     - ``aig_14``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0278
     - 00889
     - Filler Status Code

.. _hl7-v2_5_1-AIL:

AIL: Appointment Information - Location Resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.6.6

.. py:class:: hl7types.hl7.v2_5_1.segments.AIL.AIL
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
     - ``ail_1``
     - 4
     - str
     - R
     -
     - 00902
     - Set ID - AIL
   * - 2
     - ``ail_2``
     - 3
     - str
     - C
     - 0206
     - 00763
     - Segment Action Code
   * - 3
     - ``ail_3``
     -
     - list[:ref:`PL <hl7-v2_5_1-PL>`]
     - C
     -
     - 00903
     - Location Resource ID
   * - 4
     - ``ail_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0305
     - 00904
     - Location Type-AIL
   * - 5
     - ``ail_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00905
     - Location Group
   * - 6
     - ``ail_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 01202
     - Start Date/Time
   * - 7
     - ``ail_7``
     - 20
     - str
     - C
     -
     - 00891
     - Start Date/Time Offset
   * - 8
     - ``ail_8``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00892
     - Start Date/Time Offset Units
   * - 9
     - ``ail_9``
     - 20
     - str
     - O
     -
     - 00893
     - Duration
   * - 10
     - ``ail_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00894
     - Duration Units
   * - 11
     - ``ail_11``
     - 10
     - str
     - C
     - 0279
     - 00895
     - Allow Substitution Code
   * - 12
     - ``ail_12``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0278
     - 00889
     - Filler Status Code

.. _hl7-v2_5_1-AIP:

AIP: Appointment Information - Personnel Resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.6.7

.. py:class:: hl7types.hl7.v2_5_1.segments.AIP.AIP
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
     - ``aip_1``
     - 4
     - str
     - R
     -
     - 00906
     - Set ID - AIP
   * - 2
     - ``aip_2``
     - 3
     - str
     - C
     - 0206
     - 00763
     - Segment Action Code
   * - 3
     - ``aip_3``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - C
     -
     - 00913
     - Personnel Resource ID
   * - 4
     - ``aip_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0182
     - 00907
     - Resource Type
   * - 5
     - ``aip_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00899
     - Resource Group
   * - 6
     - ``aip_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 01202
     - Start Date/Time
   * - 7
     - ``aip_7``
     - 20
     - str
     - C
     -
     - 00891
     - Start Date/Time Offset
   * - 8
     - ``aip_8``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00892
     - Start Date/Time Offset Units
   * - 9
     - ``aip_9``
     - 20
     - str
     - O
     -
     - 00893
     - Duration
   * - 10
     - ``aip_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00894
     - Duration Units
   * - 11
     - ``aip_11``
     - 10
     - str
     - C
     - 0279
     - 00895
     - Allow Substitution Code
   * - 12
     - ``aip_12``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0278
     - 00889
     - Filler Status Code

.. _hl7-v2_5_1-AIS:

AIS: Appointment Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.6.4

.. py:class:: hl7types.hl7.v2_5_1.segments.AIS.AIS
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
     - ``ais_1``
     - 4
     - str
     - R
     -
     - 00890
     - Set ID - AIS
   * - 2
     - ``ais_2``
     - 3
     - str
     - C
     - 0206
     - 00763
     - Segment Action Code
   * - 3
     - ``ais_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00238
     - Universal Service Identifier
   * - 4
     - ``ais_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 01202
     - Start Date/Time
   * - 5
     - ``ais_5``
     - 20
     - str
     - C
     -
     - 00891
     - Start Date/Time Offset
   * - 6
     - ``ais_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00892
     - Start Date/Time Offset Units
   * - 7
     - ``ais_7``
     - 20
     - str
     - O
     -
     - 00893
     - Duration
   * - 8
     - ``ais_8``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00894
     - Duration Units
   * - 9
     - ``ais_9``
     - 10
     - str
     - C
     - 0279
     - 00895
     - Allow Substitution Code
   * - 10
     - ``ais_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0278
     - 00889
     - Filler Status Code
   * - 11
     - ``ais_11``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0411
     - 01474
     - Placer Supplemental Service Information
   * - 12
     - ``ais_12``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0411
     - 01475
     - Filler Supplemental Service Information

.. _hl7-v2_5_1-AL1:

AL1: Patient Allergy Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.4.6

.. py:class:: hl7types.hl7.v2_5_1.segments.AL1.AL1
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
     - Set ID - AL1
   * - 2
     - ``al1_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0127
     - 00204
     - Allergen Type Code
   * - 3
     - ``al1_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00205
     - Allergen Code/Mnemonic/Description
   * - 4
     - ``al1_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0128
     - 00206
     - Allergy Severity Code
   * - 5
     - ``al1_5``
     - 15
     - list[str]
     - O
     -
     - 00207
     - Allergy Reaction Code
   * - 6
     - ``al1_6``
     - 8
     - str
     - O
     -
     - 00208
     - Identification Date

.. _hl7-v2_5_1-APR:

APR: Appointment Preferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.6.8

.. py:class:: hl7types.hl7.v2_5_1.segments.APR.APR
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
     - ``apr_1``
     -
     - list[:ref:`SCV <hl7-v2_5_1-SCV>`]
     - O
     - 0294
     - 00908
     - Time Selection Criteria
   * - 2
     - ``apr_2``
     -
     - list[:ref:`SCV <hl7-v2_5_1-SCV>`]
     - O
     - 0294
     - 00909
     - Resource Selection Criteria
   * - 3
     - ``apr_3``
     -
     - list[:ref:`SCV <hl7-v2_5_1-SCV>`]
     - O
     - 0294
     - 00910
     - Location Selection Criteria
   * - 4
     - ``apr_4``
     - 5
     - str
     - O
     -
     - 00911
     - Slot Spacing Criteria
   * - 5
     - ``apr_5``
     -
     - list[:ref:`SCV <hl7-v2_5_1-SCV>`]
     - O
     -
     - 00912
     - Filler Override Criteria

.. _hl7-v2_5_1-ARQ:

ARQ: Appointment Request
~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.6.1

.. py:class:: hl7types.hl7.v2_5_1.segments.ARQ.ARQ
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
     - ``arq_1``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 00860
     - Placer Appointment ID
   * - 2
     - ``arq_2``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 00861
     - Filler Appointment ID
   * - 3
     - ``arq_3``
     - 5
     - str
     - C
     -
     - 00862
     - Occurrence Number
   * - 4
     - ``arq_4``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 00218
     - Placer Group Number
   * - 5
     - ``arq_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00864
     - Schedule ID
   * - 6
     - ``arq_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00865
     - Request Event Reason
   * - 7
     - ``arq_7``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0276
     - 00866
     - Appointment Reason
   * - 8
     - ``arq_8``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0277
     - 00867
     - Appointment Type
   * - 9
     - ``arq_9``
     - 20
     - str
     - O
     -
     - 00868
     - Appointment Duration
   * - 10
     - ``arq_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00869
     - Appointment Duration Units
   * - 11
     - ``arq_11``
     -
     - list[:ref:`DR <hl7-v2_5_1-DR>`]
     - O
     -
     - 00870
     - Requested Start Date/Time Range
   * - 12
     - ``arq_12``
     - 5
     - str
     - O
     -
     - 00871
     - Priority-ARQ
   * - 13
     - ``arq_13``
     -
     - :ref:`RI <hl7-v2_5_1-RI>`
     - O
     -
     - 00872
     - Repeating Interval
   * - 14
     - ``arq_14``
     - 5
     - str
     - O
     -
     - 00873
     - Repeating Interval Duration
   * - 15
     - ``arq_15``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - R
     -
     - 00874
     - Placer Contact Person
   * - 16
     - ``arq_16``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00875
     - Placer Contact Phone Number
   * - 17
     - ``arq_17``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00876
     - Placer Contact Address
   * - 18
     - ``arq_18``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 00877
     - Placer Contact Location
   * - 19
     - ``arq_19``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - R
     -
     - 00878
     - Entered By Person
   * - 20
     - ``arq_20``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00879
     - Entered By Phone Number
   * - 21
     - ``arq_21``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 00880
     - Entered By Location
   * - 22
     - ``arq_22``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 00881
     - Parent Placer Appointment ID
   * - 23
     - ``arq_23``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 00882
     - Parent Filler Appointment ID
   * - 24
     - ``arq_24``
     -
     - list[:ref:`EI <hl7-v2_5_1-EI>`]
     - C
     -
     - 00216
     - Placer Order Number
   * - 25
     - ``arq_25``
     -
     - list[:ref:`EI <hl7-v2_5_1-EI>`]
     - C
     -
     - 00217
     - Filler Order Number

.. _hl7-v2_5_1-AUT:

AUT: Authorization Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.6.2

.. py:class:: hl7types.hl7.v2_5_1.segments.AUT.AUT
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
     - ``aut_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0072
     - 01146
     - Authorizing Payor, Plan ID
   * - 2
     - ``aut_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0285
     - 01147
     - Authorizing Payor, Company ID
   * - 3
     - ``aut_3``
     - 45
     - str
     - O
     -
     - 01148
     - Authorizing Payor, Company Name
   * - 4
     - ``aut_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01149
     - Authorization Effective Date
   * - 5
     - ``aut_5``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01150
     - Authorization Expiration Date
   * - 6
     - ``aut_6``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 01151
     - Authorization Identifier
   * - 7
     - ``aut_7``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 01152
     - Reimbursement Limit
   * - 8
     - ``aut_8``
     - 2
     - str
     - O
     -
     - 01153
     - Requested Number of Treatments
   * - 9
     - ``aut_9``
     - 2
     - str
     - O
     -
     - 01154
     - Authorized Number of Treatments
   * - 10
     - ``aut_10``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01145
     - Process Date

.. _hl7-v2_5_1-BHS:

BHS: Batch Header
~~~~~~~~~~~~~~~~~

Section 2.15.2

.. py:class:: hl7types.hl7.v2_5_1.segments.BHS.BHS
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
     - 3
     - str
     - R
     -
     - 00082
     - Batch Encoding Characters
   * - 3
     - ``bhs_3``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 00083
     - Batch Sending Application
   * - 4
     - ``bhs_4``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 00084
     - Batch Sending Facility
   * - 5
     - ``bhs_5``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 00085
     - Batch Receiving Application
   * - 6
     - ``bhs_6``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 00086
     - Batch Receiving Facility
   * - 7
     - ``bhs_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00087
     - Batch Creation Date/Time
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
     - Batch Name/ID/Type
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

.. _hl7-v2_5_1-BLC:

BLC: Blood Code
~~~~~~~~~~~~~~~

Section 6.5.13

.. py:class:: hl7types.hl7.v2_5_1.segments.BLC.BLC
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
     - ``blc_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0426
     - 01528
     - Blood Product Code
   * - 2
     - ``blc_2``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01529
     - Blood Amount

.. _hl7-v2_5_1-BLG:

BLG: Billing
~~~~~~~~~~~~

Section 4.5.2

.. py:class:: hl7types.hl7.v2_5_1.segments.BLG.BLG
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
     - :ref:`CCD <hl7-v2_5_1-CCD>`
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
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 00236
     - Account ID
   * - 4
     - ``blg_4``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0475
     - 01645
     - Charge Type Reason

.. _hl7-v2_5_1-BPO:

BPO: Blood product order
~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.21.1

.. py:class:: hl7types.hl7.v2_5_1.segments.BPO.BPO
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
     - ``bpo_1``
     - 4
     - str
     - R
     -
     - 01700
     - Set ID - BPO
   * - 2
     - ``bpo_2``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - R
     -
     - 01701
     - BP Universal Service ID
   * - 3
     - ``bpo_3``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0508
     - 01702
     - BP  Processing Requirements
   * - 4
     - ``bpo_4``
     - 5
     - str
     - R
     -
     - 01703
     - BP Quantity
   * - 5
     - ``bpo_5``
     - 5
     - str
     - O
     -
     - 01704
     - BP Amount
   * - 6
     - ``bpo_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01705
     - BP Units
   * - 7
     - ``bpo_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01706
     - BP Intended Use Date/Time
   * - 8
     - ``bpo_8``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 01707
     - BP Intended Dispense From Location
   * - 9
     - ``bpo_9``
     -
     - :ref:`XAD <hl7-v2_5_1-XAD>`
     - O
     -
     - 01708
     - BP Intended Dispense From Address
   * - 10
     - ``bpo_10``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01709
     - BP Requested Dispense Date/Time
   * - 11
     - ``bpo_11``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 01710
     - BP Requested Dispense To Location
   * - 12
     - ``bpo_12``
     -
     - :ref:`XAD <hl7-v2_5_1-XAD>`
     - O
     -
     - 01711
     - BP Requested Dispense To Address
   * - 13
     - ``bpo_13``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0509
     - 01712
     - BP Indication for Use
   * - 14
     - ``bpo_14``
     - 1
     - str
     - O
     - 0136
     - 01713
     - BP Informed Consent Indicator

.. _hl7-v2_5_1-BPX:

BPX: Blood product dispense status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.21.2

.. py:class:: hl7types.hl7.v2_5_1.segments.BPX.BPX
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
     - ``bpx_1``
     - 4
     - str
     - R
     -
     - 01714
     - Set ID - BPX
   * - 2
     - ``bpx_2``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - R
     - 0510
     - 01715
     - BP Dispense Status
   * - 3
     - ``bpx_3``
     - 1
     - str
     - R
     - 0511
     - 01716
     - BP Status
   * - 4
     - ``bpx_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01717
     - BP Date/Time of Status
   * - 5
     - ``bpx_5``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 01718
     - BC Donation ID
   * - 6
     - ``bpx_6``
     -
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - C
     -
     - 01719
     - BC Component
   * - 7
     - ``bpx_7``
     -
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - O
     -
     - 01720
     - BC Donation Type / Intended Use
   * - 8
     - ``bpx_8``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - C
     - 0512
     - 01721
     - CP Commercial Product
   * - 9
     - ``bpx_9``
     -
     - :ref:`XON <hl7-v2_5_1-XON>`
     - C
     -
     - 01722
     - CP Manufacturer
   * - 10
     - ``bpx_10``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 01723
     - CP Lot Number
   * - 11
     - ``bpx_11``
     -
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - O
     -
     - 01724
     - BP Blood Group
   * - 12
     - ``bpx_12``
     -
     - list[:ref:`CNE <hl7-v2_5_1-CNE>`]
     - O
     -
     - 01725
     - BC Special Testing
   * - 13
     - ``bpx_13``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01726
     - BP Expiration Date/Time
   * - 14
     - ``bpx_14``
     - 5
     - str
     - R
     -
     - 01727
     - BP Quantity
   * - 15
     - ``bpx_15``
     - 5
     - str
     - O
     -
     - 01728
     - BP Amount
   * - 16
     - ``bpx_16``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01729
     - BP Units
   * - 17
     - ``bpx_17``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 01730
     - BP Unique ID
   * - 18
     - ``bpx_18``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 01731
     - BP Actual Dispensed To Location
   * - 19
     - ``bpx_19``
     -
     - :ref:`XAD <hl7-v2_5_1-XAD>`
     - O
     -
     - 01732
     - BP Actual Dispensed To Address
   * - 20
     - ``bpx_20``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 01733
     - BP Dispensed to Receiver
   * - 21
     - ``bpx_21``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 01734
     - BP Dispensing Individual

.. _hl7-v2_5_1-BTS:

BTS: Batch Trailer
~~~~~~~~~~~~~~~~~~

Section 2.15.3

.. py:class:: hl7types.hl7.v2_5_1.segments.BTS.BTS
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
     - 00090
     - Batch Comment
   * - 3
     - ``bts_3``
     - 100
     - list[str]
     - O
     -
     - 00095
     - Batch Totals

.. _hl7-v2_5_1-BTX:

BTX: Blood Product Transfusion/Disposition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.21.3

.. py:class:: hl7types.hl7.v2_5_1.segments.BTX.BTX
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
     - ``btx_1``
     - 4
     - str
     - R
     -
     - 01735
     - Set ID - BTX
   * - 2
     - ``btx_2``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 01736
     - BC Donation ID
   * - 3
     - ``btx_3``
     -
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - C
     -
     - 01737
     - BC Component
   * - 4
     - ``btx_4``
     -
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - C
     -
     - 01738
     - BC Blood Group
   * - 5
     - ``btx_5``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - C
     - 0512
     - 01739
     - CP Commercial Product
   * - 6
     - ``btx_6``
     -
     - :ref:`XON <hl7-v2_5_1-XON>`
     - C
     -
     - 01740
     - CP Manufacturer
   * - 7
     - ``btx_7``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 01741
     - CP Lot Number
   * - 8
     - ``btx_8``
     - 5
     - str
     - R
     -
     - 01742
     - BP Quantity
   * - 9
     - ``btx_9``
     - 5
     - str
     - O
     -
     - 01743
     - BP Amount
   * - 10
     - ``btx_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01744
     - BP Units
   * - 11
     - ``btx_11``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - R
     - 0513
     - 01745
     - BP Transfusion/Disposition Status
   * - 12
     - ``btx_12``
     - 1
     - str
     - R
     - 0511
     - 01746
     - BP Message Status
   * - 13
     - ``btx_13``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01747
     - BP Date/Time of Status
   * - 14
     - ``btx_14``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 01748
     - BP Administrator
   * - 15
     - ``btx_15``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 01749
     - BP Verifier
   * - 16
     - ``btx_16``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01750
     - BP Transfusion Start Date/Time of Status
   * - 17
     - ``btx_17``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01751
     - BP Transfusion End Date/Time of Status
   * - 18
     - ``btx_18``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0514
     - 01752
     - BP Adverse Reaction Type
   * - 19
     - ``btx_19``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0515
     - 01753
     - BP Transfusion Interrupted Reason

.. _hl7-v2_5_1-CDM:

CDM: Charge Description Master
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.2

.. py:class:: hl7types.hl7.v2_5_1.segments.CDM.CDM
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
     - ``cdm_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0132
     - 01306
     - Primary Key Value - CDM
   * - 2
     - ``cdm_2``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00983
     - Charge Code Alias
   * - 3
     - ``cdm_3``
     - 20
     - str
     - R
     -
     - 00984
     - Charge Description Short
   * - 4
     - ``cdm_4``
     - 250
     - str
     - O
     -
     - 00985
     - Charge Description Long
   * - 5
     - ``cdm_5``
     - 1
     - str
     - O
     - 0268
     - 00986
     - Description Override Indicator
   * - 6
     - ``cdm_6``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00987
     - Exploding Charges
   * - 7
     - ``cdm_7``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0088
     - 00393
     - Procedure Code
   * - 8
     - ``cdm_8``
     - 1
     - str
     - O
     - 0183
     - 00675
     - Active/Inactive Flag
   * - 9
     - ``cdm_9``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0463
     - 00990
     - Inventory Number
   * - 10
     - ``cdm_10``
     - 12
     - str
     - O
     -
     - 00991
     - Resource Load
   * - 11
     - ``cdm_11``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00992
     - Contract Number
   * - 12
     - ``cdm_12``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 00993
     - Contract Organization
   * - 13
     - ``cdm_13``
     - 1
     - str
     - O
     - 0136
     - 00994
     - Room Fee Indicator

.. _hl7-v2_5_1-CER:

CER: Certificate Detail
~~~~~~~~~~~~~~~~~~~~~~~

Section 15.4.2

.. py:class:: hl7types.hl7.v2_5_1.segments.CER.CER
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
     - ``cer_1``
     - 4
     - str
     - R
     -
     - 01856
     - Set ID - CER
   * - 2
     - ``cer_2``
     - 80
     - str
     - O
     -
     - 01857
     - Serial Number
   * - 3
     - ``cer_3``
     - 80
     - str
     - O
     -
     - 01858
     - Version
   * - 4
     - ``cer_4``
     -
     - :ref:`XON <hl7-v2_5_1-XON>`
     - O
     -
     - 01859
     - Granting Authority
   * - 5
     - ``cer_5``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 01860
     - Issuing Authority
   * - 6
     - ``cer_6``
     -
     - :ref:`ED <hl7-v2_5_1-ED>`
     - O
     -
     - 01861
     - Signature of Issuing Authority
   * - 7
     - ``cer_7``
     - 3
     - str
     - O
     - 0399
     - 01862
     - Granting Country
   * - 8
     - ``cer_8``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0347
     - 01863
     - Granting State/Province
   * - 9
     - ``cer_9``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0289
     - 01864
     - Granting County/Parish
   * - 10
     - ``cer_10``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01865
     - Certificate Type
   * - 11
     - ``cer_11``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01866
     - Certificate Domain
   * - 12
     - ``cer_12``
     - 250
     - str
     - C
     -
     - 01867
     - Subject ID
   * - 13
     - ``cer_13``
     - 250
     - str
     - R
     -
     - 01907
     - Subject Name
   * - 14
     - ``cer_14``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     -
     - 01868
     - Subject Directory Attribute Extension (Health Professional Data)
   * - 15
     - ``cer_15``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01869
     - Subject Public Key Info
   * - 16
     - ``cer_16``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01870
     - Authority Key Identifier
   * - 17
     - ``cer_17``
     - 250
     - str
     - O
     - 0136
     - 01871
     - Basic Constraint
   * - 18
     - ``cer_18``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     -
     - 01872
     - CRL Distribution Point
   * - 19
     - ``cer_19``
     - 3
     - str
     - O
     - 0399
     - 01875
     - Jurisdiction Country
   * - 20
     - ``cer_20``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0347
     - 01873
     - Jurisdiction State/Province
   * - 21
     - ``cer_21``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0289
     - 01874
     - Jurisdiction County/Parish
   * - 22
     - ``cer_22``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0547
     - 01895
     - Jurisdiction Breadth
   * - 23
     - ``cer_23``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01876
     - Granting Date
   * - 24
     - ``cer_24``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01877
     - Issuing Date
   * - 25
     - ``cer_25``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01878
     - Activation Date
   * - 26
     - ``cer_26``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01879
     - Inactivation Date
   * - 27
     - ``cer_27``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01880
     - Expiration Date
   * - 28
     - ``cer_28``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01881
     - Renewal Date
   * - 29
     - ``cer_29``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01882
     - Revocation Date
   * - 30
     - ``cer_30``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01883
     - Revocation Reason Code
   * - 31
     - ``cer_31``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0536
     - 01884
     - Certificate Status

.. _hl7-v2_5_1-CM0:

CM0: Clinical Study Master
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.11.2

.. py:class:: hl7types.hl7.v2_5_1.segments.CM0.CM0
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
     - ``cm0_1``
     - 4
     - str
     - O
     -
     - 01010
     - Set ID - CM0
   * - 2
     - ``cm0_2``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01011
     - Sponsor Study ID
   * - 3
     - ``cm0_3``
     -
     - list[:ref:`EI <hl7-v2_5_1-EI>`]
     - O
     -
     - 01036
     - Alternate Study ID
   * - 4
     - ``cm0_4``
     - 300
     - str
     - R
     -
     - 01013
     - Title of Study
   * - 5
     - ``cm0_5``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 01014
     - Chairman of Study
   * - 6
     - ``cm0_6``
     - 8
     - str
     - O
     -
     - 01015
     - Last IRB Approval Date
   * - 7
     - ``cm0_7``
     - 8
     - str
     - O
     -
     - 01016
     - Total Accrual to Date
   * - 8
     - ``cm0_8``
     - 8
     - str
     - O
     -
     - 01017
     - Last Accrual Date
   * - 9
     - ``cm0_9``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 01018
     - Contact for Study
   * - 10
     - ``cm0_10``
     -
     - :ref:`XTN <hl7-v2_5_1-XTN>`
     - O
     -
     - 01019
     - Contact's Telephone Number
   * - 11
     - ``cm0_11``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 01020
     - Contact's Address

.. _hl7-v2_5_1-CM1:

CM1: Clinical Study Phase Master
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.11.3

.. py:class:: hl7types.hl7.v2_5_1.segments.CM1.CM1
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
     - ``cm1_1``
     - 4
     - str
     - R
     -
     - 01021
     - Set ID - CM1
   * - 2
     - ``cm1_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 01022
     - Study Phase Identifier
   * - 3
     - ``cm1_3``
     - 300
     - str
     - R
     -
     - 01023
     - Description of Study Phase

.. _hl7-v2_5_1-CM2:

CM2: Clinical Study Schedule Master
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.11.4

.. py:class:: hl7types.hl7.v2_5_1.segments.CM2.CM2
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
     - ``cm2_1``
     - 4
     - str
     - O
     -
     - 01024
     - Set ID - CM2
   * - 2
     - ``cm2_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 01025
     - Scheduled Time Point
   * - 3
     - ``cm2_3``
     - 300
     - str
     - O
     -
     - 01026
     - Description of Time Point
   * - 4
     - ``cm2_4``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - R
     -
     - 01027
     - Events Scheduled This Time Point

.. _hl7-v2_5_1-CNS:

CNS: Clear Notification
~~~~~~~~~~~~~~~~~~~~~~~

Section 13.4.8

.. py:class:: hl7types.hl7.v2_5_1.segments.CNS.CNS
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
     - ``cns_1``
     - 20
     - str
     - O
     -
     - 01402
     - Starting Notification Reference Number
   * - 2
     - ``cns_2``
     - 20
     - str
     - O
     -
     - 01403
     - Ending Notification Reference Number
   * - 3
     - ``cns_3``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01404
     - Starting Notification Date/Time
   * - 4
     - ``cns_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01405
     - Ending Notification Date/Time
   * - 5
     - ``cns_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01406
     - Starting Notification Code
   * - 6
     - ``cns_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01407
     - Ending Notification Code

.. _hl7-v2_5_1-CON:

CON: Consent Segment
~~~~~~~~~~~~~~~~~~~~

Section 9.9.4

.. py:class:: hl7types.hl7.v2_5_1.segments.CON.CON
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
     - ``con_1``
     - 4
     - str
     - R
     -
     - 01776
     - Set ID - CON
   * - 2
     - ``con_2``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0496
     - 01777
     - Consent Type
   * - 3
     - ``con_3``
     - 40
     - str
     - O
     -
     - 01778
     - Consent Form ID
   * - 4
     - ``con_4``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 01779
     - Consent Form Number
   * - 5
     - ``con_5``
     -
     - list[str]
     - O
     -
     - 01780
     - Consent Text
   * - 6
     - ``con_6``
     -
     - list[str]
     - O
     -
     - 01781
     - Subject-specific Consent Text
   * - 7
     - ``con_7``
     -
     - list[str]
     - O
     -
     - 01782
     - Consent Background
   * - 8
     - ``con_8``
     -
     - list[str]
     - O
     -
     - 01783
     - Subject-specific Consent Background
   * - 9
     - ``con_9``
     -
     - list[str]
     - O
     -
     - 01784
     - Consenter-imposed limitations
   * - 10
     - ``con_10``
     -
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - O
     - 0497
     - 01785
     - Consent Mode
   * - 11
     - ``con_11``
     -
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - R
     - 0498
     - 01786
     - Consent Status
   * - 12
     - ``con_12``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01787
     - Consent Discussion Date/Time
   * - 13
     - ``con_13``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01788
     - Consent Decision Date/Time
   * - 14
     - ``con_14``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01789
     - Consent Effective Date/Time
   * - 15
     - ``con_15``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01790
     - Consent End Date/Time
   * - 16
     - ``con_16``
     - 1
     - str
     - O
     - 0136
     - 01791
     - Subject Competence Indicator
   * - 17
     - ``con_17``
     - 1
     - str
     - O
     - 0136
     - 01792
     - Translator Assistance Indicator
   * - 18
     - ``con_18``
     - 1
     - str
     - O
     - 0296
     - 01793
     - Language Translated To
   * - 19
     - ``con_19``
     - 1
     - str
     - O
     - 0136
     - 01794
     - Informational Material Supplied Indicator
   * - 20
     - ``con_20``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0499
     - 01795
     - Consent Bypass Reason
   * - 21
     - ``con_21``
     - 1
     - str
     - O
     - 0500
     - 01796
     - Consent Disclosure Level
   * - 22
     - ``con_22``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0501
     - 01797
     - Consent Non-disclosure Reason
   * - 23
     - ``con_23``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0502
     - 01798
     - Non-subject Consenter Reason
   * - 24
     - ``con_24``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - R
     -
     - 01909
     - Consenter ID
   * - 25
     - ``con_25``
     - 100
     - list[str]
     - R
     - 0548
     - 01898
     - Relationship to Subject Table

.. _hl7-v2_5_1-CSP:

CSP: Clinical Study Phase
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.8.2

.. py:class:: hl7types.hl7.v2_5_1.segments.CSP.CSP
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
     - ``csp_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 01022
     - Study Phase Identifier
   * - 2
     - ``csp_2``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01052
     - Date/time Study Phase Began
   * - 3
     - ``csp_3``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01053
     - Date/time Study Phase Ended
   * - 4
     - ``csp_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 01054
     - Study Phase Evaluability

.. _hl7-v2_5_1-CSR:

CSR: Clinical Study Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.8.1

.. py:class:: hl7types.hl7.v2_5_1.segments.CSR.CSR
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
     - ``csr_1``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01011
     - Sponsor Study ID
   * - 2
     - ``csr_2``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 01036
     - Alternate Study ID
   * - 3
     - ``csr_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01037
     - Institution Registering the Patient
   * - 4
     - ``csr_4``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - R
     -
     - 01038
     - Sponsor Patient ID
   * - 5
     - ``csr_5``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 01039
     - Alternate Patient ID - CSR
   * - 6
     - ``csr_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01040
     - Date/Time Of Patient Study Registration
   * - 7
     - ``csr_7``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 01041
     - Person Performing Study Registration
   * - 8
     - ``csr_8``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - R
     -
     - 01042
     - Study Authorizing Provider
   * - 9
     - ``csr_9``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 01043
     - Date/time Patient Study Consent Signed
   * - 10
     - ``csr_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 01044
     - Patient Study Eligibility Status
   * - 11
     - ``csr_11``
     -
     - list[:ref:`TS <hl7-v2_5_1-TS>`]
     - O
     -
     - 01045
     - Study Randomization Date/time
   * - 12
     - ``csr_12``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01046
     - Randomized Study Arm
   * - 13
     - ``csr_13``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01047
     - Stratum for Study Randomization
   * - 14
     - ``csr_14``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 01048
     - Patient Evaluability Status
   * - 15
     - ``csr_15``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 01049
     - Date/time Ended Study
   * - 16
     - ``csr_16``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 01050
     - Reason Ended Study

.. _hl7-v2_5_1-CSS:

CSS: Clinical Study Data Schedule Segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.8.3

.. py:class:: hl7types.hl7.v2_5_1.segments.CSS.CSS
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
     - ``css_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 01055
     - Study Scheduled Time Point
   * - 2
     - ``css_2``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01056
     - Study Scheduled Patient Time Point
   * - 3
     - ``css_3``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01057
     - Study Quality Control Codes

.. _hl7-v2_5_1-CTD:

CTD: Contact Data
~~~~~~~~~~~~~~~~~

Section 11.6.4

.. py:class:: hl7types.hl7.v2_5_1.segments.CTD.CTD
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
     - ``ctd_1``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - R
     - 0131
     - 00196
     - Contact Role
   * - 2
     - ``ctd_2``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 01165
     - Contact Name
   * - 3
     - ``ctd_3``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 01166
     - Contact Address
   * - 4
     - ``ctd_4``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 01167
     - Contact Location
   * - 5
     - ``ctd_5``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 01168
     - Contact Communication Information
   * - 6
     - ``ctd_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0185
     - 00684
     - Preferred Method of Contact
   * - 7
     - ``ctd_7``
     -
     - list[:ref:`PLN <hl7-v2_5_1-PLN>`]
     - O
     -
     - 01171
     - Contact Identifiers

.. _hl7-v2_5_1-CTI:

CTI: Clinical Trial Identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.8.4

.. py:class:: hl7types.hl7.v2_5_1.segments.CTI.CTI
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
     - ``cti_1``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01011
     - Sponsor Study ID
   * - 2
     - ``cti_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 01022
     - Study Phase Identifier
   * - 3
     - ``cti_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01055
     - Study Scheduled Time Point

.. _hl7-v2_5_1-DB1:

DB1: Disability
~~~~~~~~~~~~~~~

Section 3.4.11

.. py:class:: hl7types.hl7.v2_5_1.segments.DB1.DB1
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
     - ``db1_1``
     - 4
     - str
     - R
     -
     - 01283
     - Set ID - DB1
   * - 2
     - ``db1_2``
     - 2
     - str
     - O
     - 0334
     - 01284
     - Disabled Person Code
   * - 3
     - ``db1_3``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 01285
     - Disabled Person Identifier
   * - 4
     - ``db1_4``
     - 1
     - str
     - O
     - 0136
     - 01286
     - Disabled Indicator
   * - 5
     - ``db1_5``
     - 8
     - str
     - O
     -
     - 01287
     - Disability Start Date
   * - 6
     - ``db1_6``
     - 8
     - str
     - O
     -
     - 01288
     - Disability End Date
   * - 7
     - ``db1_7``
     - 8
     - str
     - O
     -
     - 01289
     - Disability Return to Work Date
   * - 8
     - ``db1_8``
     - 8
     - str
     - O
     -
     - 01290
     - Disability Unable to Work Date

.. _hl7-v2_5_1-DG1:

DG1: Diagnosis
~~~~~~~~~~~~~~

Section 6.5.2

.. py:class:: hl7types.hl7.v2_5_1.segments.DG1.DG1
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
     - Set ID - DG1
   * - 2
     - ``dg1_2``
     - 2
     - str
     - R
     - 0053
     - 00376
     - Diagnosis Coding Method
   * - 3
     - ``dg1_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0051
     - 00377
     - Diagnosis Code - DG1
   * - 4
     - ``dg1_4``
     - 40
     - str
     - O
     -
     - 00378
     - Diagnosis Description
   * - 5
     - ``dg1_5``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00379
     - Diagnosis Date/Time
   * - 6
     - ``dg1_6``
     - 2
     - str
     - R
     - 0052
     - 00380
     - Diagnosis Type
   * - 7
     - ``dg1_7``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0118
     - 00381
     - Major Diagnostic Category
   * - 8
     - ``dg1_8``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0055
     - 00382
     - Diagnostic Related Group
   * - 9
     - ``dg1_9``
     - 1
     - str
     - O
     - 0136
     - 00383
     - DRG Approval Indicator
   * - 10
     - ``dg1_10``
     - 2
     - str
     - O
     - 0056
     - 00384
     - DRG Grouper Review Code
   * - 11
     - ``dg1_11``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0083
     - 00385
     - Outlier Type
   * - 12
     - ``dg1_12``
     - 3
     - str
     - O
     -
     - 00386
     - Outlier Days
   * - 13
     - ``dg1_13``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00387
     - Outlier Cost
   * - 14
     - ``dg1_14``
     - 4
     - str
     - O
     -
     - 00388
     - Grouper Version And Type
   * - 15
     - ``dg1_15``
     - 2
     - str
     - O
     - 0359
     - 00389
     - Diagnosis Priority
   * - 16
     - ``dg1_16``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00390
     - Diagnosing Clinician
   * - 17
     - ``dg1_17``
     - 3
     - str
     - O
     - 0228
     - 00766
     - Diagnosis Classification
   * - 18
     - ``dg1_18``
     - 1
     - str
     - O
     - 0136
     - 00767
     - Confidential Indicator
   * - 19
     - ``dg1_19``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00768
     - Attestation Date/Time
   * - 20
     - ``dg1_20``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 01850
     - Diagnosis Identifier
   * - 21
     - ``dg1_21``
     - 1
     - str
     - C
     - 0206
     - 01894
     - Diagnosis Action Code

.. _hl7-v2_5_1-DRG:

DRG: Diagnosis Related Group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.5.3

.. py:class:: hl7types.hl7.v2_5_1.segments.DRG.DRG
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
     - ``drg_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0055
     - 00382
     - Diagnostic Related Group
   * - 2
     - ``drg_2``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00769
     - DRG Assigned Date/Time
   * - 3
     - ``drg_3``
     - 1
     - str
     - O
     - 0136
     - 00383
     - DRG Approval Indicator
   * - 4
     - ``drg_4``
     - 2
     - str
     - O
     - 0056
     - 00384
     - DRG Grouper Review Code
   * - 5
     - ``drg_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0083
     - 00385
     - Outlier Type
   * - 6
     - ``drg_6``
     - 3
     - str
     - O
     -
     - 00386
     - Outlier Days
   * - 7
     - ``drg_7``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00387
     - Outlier Cost
   * - 8
     - ``drg_8``
     - 1
     - str
     - O
     - 0229
     - 00770
     - DRG Payor
   * - 9
     - ``drg_9``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00771
     - Outlier Reimbursement
   * - 10
     - ``drg_10``
     - 1
     - str
     - O
     - 0136
     - 00767
     - Confidential Indicator
   * - 11
     - ``drg_11``
     - 21
     - str
     - O
     - 0415
     - 01500
     - DRG Transfer Type

.. _hl7-v2_5_1-DSC:

DSC: Continuation Pointer
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.15.4

.. py:class:: hl7types.hl7.v2_5_1.segments.DSC.DSC
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
     - 00014
     - Continuation Pointer
   * - 2
     - ``dsc_2``
     - 1
     - str
     - O
     - 0398
     - 01354
     - Continuation Style

.. _hl7-v2_5_1-DSP:

DSP: Display Data
~~~~~~~~~~~~~~~~~

Section 5.5.1

.. py:class:: hl7types.hl7.v2_5_1.segments.DSP.DSP
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
     - Set ID - DSP
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

.. _hl7-v2_5_1-ECD:

ECD: Equipment Command
~~~~~~~~~~~~~~~~~~~~~~

Section 13.4.5

.. py:class:: hl7types.hl7.v2_5_1.segments.ECD.ECD
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
     - ``ecd_1``
     - 20
     - str
     - R
     -
     - 01390
     - Reference Command Number
   * - 2
     - ``ecd_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0368
     - 01391
     - Remote Control Command
   * - 3
     - ``ecd_3``
     - 80
     - str
     - O
     - 0136
     - 01392
     - Response Required
   * - 4
     - ``ecd_4``
     -
     - :ref:`TQ <hl7-v2_5_1-TQ>`
     - O
     -
     - 01393
     - Requested Completion Time
   * - 5
     - ``ecd_5``
     -
     - list[str]
     - O
     -
     - 01394
     - Parameters

.. _hl7-v2_5_1-ECR:

ECR: Equipment Command Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.4.6

.. py:class:: hl7types.hl7.v2_5_1.segments.ECR.ECR
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
     - ``ecr_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0387
     - 01395
     - Command Response
   * - 2
     - ``ecr_2``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01396
     - Date/Time Completed
   * - 3
     - ``ecr_3``
     -
     - list[str]
     - O
     -
     - 01397
     - Command Response Parameters

.. _hl7-v2_5_1-EDU:

EDU: Educational Detail
~~~~~~~~~~~~~~~~~~~~~~~

Section 15.4.3

.. py:class:: hl7types.hl7.v2_5_1.segments.EDU.EDU
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
     - ``edu_1``
     - 60
     - str
     - R
     -
     - 01448
     - Set ID - EDU
   * - 2
     - ``edu_2``
     - 10
     - str
     - O
     - 0360
     - 01449
     - Academic Degree
   * - 3
     - ``edu_3``
     -
     - :ref:`DR <hl7-v2_5_1-DR>`
     - O
     -
     - 01597
     - Academic Degree Program Date Range
   * - 4
     - ``edu_4``
     -
     - :ref:`DR <hl7-v2_5_1-DR>`
     - O
     -
     - 01450
     - Academic Degree Program Participation Date Range
   * - 5
     - ``edu_5``
     - 8
     - str
     - O
     -
     - 01451
     - Academic Degree Granted Date
   * - 6
     - ``edu_6``
     -
     - :ref:`XON <hl7-v2_5_1-XON>`
     - O
     -
     - 01452
     - School
   * - 7
     - ``edu_7``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0402
     - 01453
     - School Type Code
   * - 8
     - ``edu_8``
     -
     - :ref:`XAD <hl7-v2_5_1-XAD>`
     - O
     -
     - 01454
     - School Address
   * - 9
     - ``edu_9``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     -
     - 01885
     - Major Field of Study

.. _hl7-v2_5_1-EQL:

EQL: Embedded Query Language
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.10.5.1

.. py:class:: hl7types.hl7.v2_5_1.segments.EQL.EQL
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
     - ``eql_1``
     - 32
     - str
     - O
     -
     - 00696
     - Query Tag
   * - 2
     - ``eql_2``
     - 1
     - str
     - R
     - 0106
     - 00697
     - Query/Response Format Code
   * - 3
     - ``eql_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00709
     - EQL Query Name
   * - 4
     - ``eql_4``
     - 4096
     - str
     - R
     -
     - 00710
     - EQL Query Statement

.. _hl7-v2_5_1-EQP:

EQP: Equipment/log Service
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.4.12

.. py:class:: hl7types.hl7.v2_5_1.segments.EQP.EQP
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
     - ``eqp_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0450
     - 01430
     - Event type
   * - 2
     - ``eqp_2``
     - 20
     - str
     - O
     -
     - 01431
     - File Name
   * - 3
     - ``eqp_3``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01202
     - Start Date/Time
   * - 4
     - ``eqp_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01432
     - End Date/Time
   * - 5
     - ``eqp_5``
     -
     - str
     - R
     -
     - 01433
     - Transaction Data

.. _hl7-v2_5_1-EQU:

EQU: Equipment Detail
~~~~~~~~~~~~~~~~~~~~~

Section 13.4.1

.. py:class:: hl7types.hl7.v2_5_1.segments.EQU.EQU
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
     - ``equ_1``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01479
     - Equipment Instance Identifier
   * - 2
     - ``equ_2``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01322
     - Event Date/Time
   * - 3
     - ``equ_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0365
     - 01323
     - Equipment State
   * - 4
     - ``equ_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0366
     - 01324
     - Local/Remote Control State
   * - 5
     - ``equ_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0367
     - 01325
     - Alert Level

.. _hl7-v2_5_1-ERQ:

ERQ: Event replay query
~~~~~~~~~~~~~~~~~~~~~~~

Section 5.10.5.2

.. py:class:: hl7types.hl7.v2_5_1.segments.ERQ.ERQ
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
     - ``erq_1``
     - 32
     - str
     - O
     -
     - 00696
     - Query Tag
   * - 2
     - ``erq_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00706
     - Event Identifier
   * - 3
     - ``erq_3``
     -
     - list[:ref:`QIP <hl7-v2_5_1-QIP>`]
     - O
     -
     - 00705
     - Input Parameter List

.. _hl7-v2_5_1-ERR:

ERR: Error
~~~~~~~~~~

Section 2.15.5

.. py:class:: hl7types.hl7.v2_5_1.segments.ERR.ERR
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
     - list[:ref:`ELD <hl7-v2_5_1-ELD>`]
     - O
     -
     - 00024
     - Error Code and Location
   * - 2
     - ``err_2``
     -
     - list[:ref:`ERL <hl7-v2_5_1-ERL>`]
     - O
     -
     - 01812
     - Error Location
   * - 3
     - ``err_3``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - R
     - 0357
     - 01813
     - HL7 Error Code
   * - 4
     - ``err_4``
     - 2
     - str
     - R
     - 0516
     - 01814
     - Severity
   * - 5
     - ``err_5``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0533
     - 01815
     - Application Error Code
   * - 6
     - ``err_6``
     - 80
     - list[str]
     - O
     -
     - 01816
     - Application Error Parameter
   * - 7
     - ``err_7``
     -
     - str
     - O
     -
     - 01817
     - Diagnostic Information
   * - 8
     - ``err_8``
     -
     - str
     - O
     -
     - 01818
     - User Message
   * - 9
     - ``err_9``
     - 20
     - list[str]
     - O
     - 0517
     - 01819
     - Inform Person Indicator
   * - 10
     - ``err_10``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0518
     - 01820
     - Override Type
   * - 11
     - ``err_11``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0519
     - 01821
     - Override Reason Code
   * - 12
     - ``err_12``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 01822
     - Help Desk Contact Point

.. _hl7-v2_5_1-EVN:

EVN: Event Type
~~~~~~~~~~~~~~~

Section 3.4.1

.. py:class:: hl7types.hl7.v2_5_1.segments.EVN.EVN
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
     - O
     - 0003
     - 00099
     - Event Type Code
   * - 2
     - ``evn_2``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 00100
     - Recorded Date/Time
   * - 3
     - ``evn_3``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00101
     - Date/Time Planned Event
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
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     - 0188
     - 00103
     - Operator ID
   * - 6
     - ``evn_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01278
     - Event Occurred
   * - 7
     - ``evn_7``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 01534
     - Event Facility

.. _hl7-v2_5_1-FAC:

FAC: Facility
~~~~~~~~~~~~~

Section 7.12.6

.. py:class:: hl7types.hl7.v2_5_1.segments.FAC.FAC
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
     - ``fac_1``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01262
     - Facility ID-FAC
   * - 2
     - ``fac_2``
     - 1
     - str
     - O
     - 0331
     - 01263
     - Facility Type
   * - 3
     - ``fac_3``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - R
     -
     - 01264
     - Facility Address
   * - 4
     - ``fac_4``
     -
     - :ref:`XTN <hl7-v2_5_1-XTN>`
     - R
     -
     - 01265
     - Facility Telecommunication
   * - 5
     - ``fac_5``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 01266
     - Contact Person
   * - 6
     - ``fac_6``
     - 60
     - list[str]
     - O
     -
     - 01267
     - Contact Title
   * - 7
     - ``fac_7``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 01166
     - Contact Address
   * - 8
     - ``fac_8``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 01269
     - Contact Telecommunication
   * - 9
     - ``fac_9``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - R
     -
     - 01270
     - Signature Authority
   * - 10
     - ``fac_10``
     - 60
     - str
     - O
     -
     - 01271
     - Signature Authority Title
   * - 11
     - ``fac_11``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 01272
     - Signature Authority Address
   * - 12
     - ``fac_12``
     -
     - :ref:`XTN <hl7-v2_5_1-XTN>`
     - O
     -
     - 01273
     - Signature Authority Telecommunication

.. _hl7-v2_5_1-FHS:

FHS: File Header
~~~~~~~~~~~~~~~~

Section 2.15.6

.. py:class:: hl7types.hl7.v2_5_1.segments.FHS.FHS
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
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 00069
     - File Sending Application
   * - 4
     - ``fhs_4``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 00070
     - File Sending Facility
   * - 5
     - ``fhs_5``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 00071
     - File Receiving Application
   * - 6
     - ``fhs_6``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 00072
     - File Receiving Facility
   * - 7
     - ``fhs_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00073
     - File Creation Date/Time
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
     - File Name/ID
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

.. _hl7-v2_5_1-FT1:

FT1: Financial Transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.5.1

.. py:class:: hl7types.hl7.v2_5_1.segments.FT1.FT1
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
     - Set ID - FT1
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
     - Transaction Batch ID
   * - 4
     - ``ft1_4``
     -
     - :ref:`DR <hl7-v2_5_1-DR>`
     - R
     -
     - 00358
     - Transaction Date
   * - 5
     - ``ft1_5``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00359
     - Transaction Posting Date
   * - 6
     - ``ft1_6``
     - 8
     - str
     - R
     - 0017
     - 00360
     - Transaction Type
   * - 7
     - ``ft1_7``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0132
     - 00361
     - Transaction Code
   * - 8
     - ``ft1_8``
     - 40
     - str
     - O
     -
     - 00362
     - Transaction Description
   * - 9
     - ``ft1_9``
     - 40
     - str
     - O
     -
     - 00363
     - Transaction Description - Alt
   * - 10
     - ``ft1_10``
     - 6
     - str
     - O
     -
     - 00364
     - Transaction Quantity
   * - 11
     - ``ft1_11``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00365
     - Transaction Amount - Extended
   * - 12
     - ``ft1_12``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00366
     - Transaction Amount - Unit
   * - 13
     - ``ft1_13``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0049
     - 00367
     - Department Code
   * - 14
     - ``ft1_14``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0072
     - 00368
     - Insurance Plan ID
   * - 15
     - ``ft1_15``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00369
     - Insurance Amount
   * - 16
     - ``ft1_16``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 00133
     - Assigned Patient Location
   * - 17
     - ``ft1_17``
     - 1
     - str
     - O
     - 0024
     - 00370
     - Fee Schedule
   * - 18
     - ``ft1_18``
     - 2
     - str
     - O
     - 0018
     - 00148
     - Patient Type
   * - 19
     - ``ft1_19``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0051
     - 00371
     - Diagnosis Code - FT1
   * - 20
     - ``ft1_20``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     - 0084
     - 00372
     - Performed By Code
   * - 21
     - ``ft1_21``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00373
     - Ordered By Code
   * - 22
     - ``ft1_22``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00374
     - Unit Cost
   * - 23
     - ``ft1_23``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 00217
     - Filler Order Number
   * - 24
     - ``ft1_24``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00765
     - Entered By Code
   * - 25
     - ``ft1_25``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0088
     - 00393
     - Procedure Code
   * - 26
     - ``ft1_26``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0340
     - 01316
     - Procedure Code Modifier
   * - 27
     - ``ft1_27``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0339
     - 01310
     - Advanced Beneficiary Notice Code
   * - 28
     - ``ft1_28``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0476
     - 01646
     - Medically Necessary Duplicate Procedure Reason.
   * - 29
     - ``ft1_29``
     -
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - O
     - 0549
     - 01845
     - NDC Code
   * - 30
     - ``ft1_30``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 01846
     - Payment Reference ID
   * - 31
     - ``ft1_31``
     - 4
     - list[str]
     - O
     -
     - 01847
     - Transaction Reference Key

.. _hl7-v2_5_1-FTS:

FTS: File Trailer
~~~~~~~~~~~~~~~~~

Section 2.15.7

.. py:class:: hl7types.hl7.v2_5_1.segments.FTS.FTS
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

.. _hl7-v2_5_1-GOL:

GOL: Goal Detail
~~~~~~~~~~~~~~~~

Section 12.4.1

.. py:class:: hl7types.hl7.v2_5_1.segments.GOL.GOL
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
     - ``gol_1``
     - 2
     - str
     - R
     - 0287
     - 00816
     - Action Code
   * - 2
     - ``gol_2``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 00817
     - Action Date/Time
   * - 3
     - ``gol_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00818
     - Goal ID
   * - 4
     - ``gol_4``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 00819
     - Goal Instance ID
   * - 5
     - ``gol_5``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 00820
     - Episode of Care ID
   * - 6
     - ``gol_6``
     - 60
     - str
     - O
     -
     - 00821
     - Goal List Priority
   * - 7
     - ``gol_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00822
     - Goal Established Date/Time
   * - 8
     - ``gol_8``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00824
     - Expected Goal Achieve Date/Time
   * - 9
     - ``gol_9``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00825
     - Goal Classification
   * - 10
     - ``gol_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00826
     - Goal Management Discipline
   * - 11
     - ``gol_11``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00827
     - Current Goal Review Status
   * - 12
     - ``gol_12``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00828
     - Current Goal Review Date/Time
   * - 13
     - ``gol_13``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00829
     - Next Goal Review Date/Time
   * - 14
     - ``gol_14``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00830
     - Previous Goal Review Date/Time
   * - 15
     - ``gol_15``
     -
     - :ref:`TQ <hl7-v2_5_1-TQ>`
     - O
     -
     - 00831
     - Goal Review Interval
   * - 16
     - ``gol_16``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00832
     - Goal Evaluation
   * - 17
     - ``gol_17``
     - 300
     - list[str]
     - O
     -
     - 00833
     - Goal Evaluation Comment
   * - 18
     - ``gol_18``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00834
     - Goal Life Cycle Status
   * - 19
     - ``gol_19``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00835
     - Goal Life Cycle Status Date/Time
   * - 20
     - ``gol_20``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00836
     - Goal Target Type
   * - 21
     - ``gol_21``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00837
     - Goal Target Name

.. _hl7-v2_5_1-GP1:

GP1: Grouping/Reimbursement - Visit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.5.15

.. py:class:: hl7types.hl7.v2_5_1.segments.GP1.GP1
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
     - ``gp1_1``
     - 3
     - str
     - R
     - 0455
     - 01599
     - Type of Bill Code
   * - 2
     - ``gp1_2``
     - 3
     - list[str]
     - O
     - 0456
     - 01600
     - Revenue Code
   * - 3
     - ``gp1_3``
     - 1
     - str
     - O
     - 0457
     - 01601
     - Overall Claim Disposition Code
   * - 4
     - ``gp1_4``
     - 2
     - list[str]
     - O
     - 0458
     - 01602
     - OCE Edits per Visit Code
   * - 5
     - ``gp1_5``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00387
     - Outlier Cost

.. _hl7-v2_5_1-GP2:

GP2: Grouping/Reimbursement - Procedure Line Item
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.5.16

.. py:class:: hl7types.hl7.v2_5_1.segments.GP2.GP2
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
     - ``gp2_1``
     - 3
     - str
     - O
     - 0456
     - 01600
     - Revenue Code
   * - 2
     - ``gp2_2``
     - 7
     - str
     - O
     -
     - 01604
     - Number of Service Units
   * - 3
     - ``gp2_3``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 01605
     - Charge
   * - 4
     - ``gp2_4``
     - 1
     - str
     - O
     - 0459
     - 01606
     - Reimbursement Action Code
   * - 5
     - ``gp2_5``
     - 1
     - str
     - O
     - 0460
     - 01607
     - Denial or Rejection Code
   * - 6
     - ``gp2_6``
     - 3
     - list[str]
     - O
     - 0458
     - 01608
     - OCE Edit Code
   * - 7
     - ``gp2_7``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0466
     - 01609
     - Ambulatory Payment Classification Code
   * - 8
     - ``gp2_8``
     - 1
     - list[str]
     - O
     - 0467
     - 01610
     - Modifier Edit Code
   * - 9
     - ``gp2_9``
     - 1
     - str
     - O
     - 0468
     - 01611
     - Payment Adjustment Code
   * - 10
     - ``gp2_10``
     - 1
     - str
     - O
     - 0469
     - 01617
     - Packaging Status Code
   * - 11
     - ``gp2_11``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 01618
     - Expected CMS Payment Amount
   * - 12
     - ``gp2_12``
     - 2
     - str
     - O
     - 0470
     - 01619
     - Reimbursement Type Code
   * - 13
     - ``gp2_13``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 01620
     - Co-Pay Amount
   * - 14
     - ``gp2_14``
     - 4
     - str
     - O
     -
     - 01621
     - Pay Rate per Service Unit

.. _hl7-v2_5_1-GT1:

GT1: Guarantor
~~~~~~~~~~~~~~

Section 6.5.5

.. py:class:: hl7types.hl7.v2_5_1.segments.GT1.GT1
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
     - Set ID - GT1
   * - 2
     - ``gt1_2``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00406
     - Guarantor Number
   * - 3
     - ``gt1_3``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - R
     -
     - 00407
     - Guarantor Name
   * - 4
     - ``gt1_4``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00408
     - Guarantor Spouse Name
   * - 5
     - ``gt1_5``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00409
     - Guarantor Address
   * - 6
     - ``gt1_6``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00410
     - Guarantor Ph Num - Home
   * - 7
     - ``gt1_7``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00411
     - Guarantor Ph Num - Business
   * - 8
     - ``gt1_8``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00412
     - Guarantor Date/Time Of Birth
   * - 9
     - ``gt1_9``
     - 1
     - str
     - O
     - 0001
     - 00413
     - Guarantor Administrative Sex
   * - 10
     - ``gt1_10``
     - 2
     - str
     - O
     - 0068
     - 00414
     - Guarantor Type
   * - 11
     - ``gt1_11``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0063
     - 00415
     - Guarantor Relationship
   * - 12
     - ``gt1_12``
     - 11
     - str
     - O
     -
     - 00416
     - Guarantor SSN
   * - 13
     - ``gt1_13``
     - 8
     - str
     - O
     -
     - 00417
     - Guarantor Date - Begin
   * - 14
     - ``gt1_14``
     - 8
     - str
     - O
     -
     - 00418
     - Guarantor Date - End
   * - 15
     - ``gt1_15``
     - 2
     - str
     - O
     -
     - 00419
     - Guarantor Priority
   * - 16
     - ``gt1_16``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00420
     - Guarantor Employer Name
   * - 17
     - ``gt1_17``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00421
     - Guarantor Employer Address
   * - 18
     - ``gt1_18``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00422
     - Guarantor Employer Phone Number
   * - 19
     - ``gt1_19``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00423
     - Guarantor Employee ID Number
   * - 20
     - ``gt1_20``
     - 2
     - str
     - O
     - 0066
     - 00424
     - Guarantor Employment Status
   * - 21
     - ``gt1_21``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 00425
     - Guarantor Organization Name
   * - 22
     - ``gt1_22``
     - 1
     - str
     - O
     - 0136
     - 00773
     - Guarantor Billing Hold Flag
   * - 23
     - ``gt1_23``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0341
     - 00774
     - Guarantor Credit Rating Code
   * - 24
     - ``gt1_24``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00775
     - Guarantor Death Date And Time
   * - 25
     - ``gt1_25``
     - 1
     - str
     - O
     - 0136
     - 00776
     - Guarantor Death Flag
   * - 26
     - ``gt1_26``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0218
     - 00777
     - Guarantor Charge Adjustment Code
   * - 27
     - ``gt1_27``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00778
     - Guarantor Household Annual Income
   * - 28
     - ``gt1_28``
     - 3
     - str
     - O
     -
     - 00779
     - Guarantor Household Size
   * - 29
     - ``gt1_29``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00780
     - Guarantor Employer ID Number
   * - 30
     - ``gt1_30``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0002
     - 00781
     - Guarantor Marital Status Code
   * - 31
     - ``gt1_31``
     - 8
     - str
     - O
     -
     - 00782
     - Guarantor Hire Effective Date
   * - 32
     - ``gt1_32``
     - 8
     - str
     - O
     -
     - 00783
     - Employment Stop Date
   * - 33
     - ``gt1_33``
     - 2
     - str
     - O
     - 0223
     - 00755
     - Living Dependency
   * - 34
     - ``gt1_34``
     - 2
     - list[str]
     - O
     - 0009
     - 00145
     - Ambulatory Status
   * - 35
     - ``gt1_35``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0171
     - 00129
     - Citizenship
   * - 36
     - ``gt1_36``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0296
     - 00118
     - Primary Language
   * - 37
     - ``gt1_37``
     - 2
     - str
     - O
     - 0220
     - 00742
     - Living Arrangement
   * - 38
     - ``gt1_38``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0215
     - 00743
     - Publicity Code
   * - 39
     - ``gt1_39``
     - 1
     - str
     - O
     - 0136
     - 00744
     - Protection Indicator
   * - 40
     - ``gt1_40``
     - 2
     - str
     - O
     - 0231
     - 00745
     - Student Indicator
   * - 41
     - ``gt1_41``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0006
     - 00120
     - Religion
   * - 42
     - ``gt1_42``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00109
     - Mother's Maiden Name
   * - 43
     - ``gt1_43``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0212
     - 00739
     - Nationality
   * - 44
     - ``gt1_44``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0189
     - 00125
     - Ethnic Group
   * - 45
     - ``gt1_45``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00748
     - Contact Person's Name
   * - 46
     - ``gt1_46``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00749
     - Contact Person's Telephone Number
   * - 47
     - ``gt1_47``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0222
     - 00747
     - Contact Reason
   * - 48
     - ``gt1_48``
     - 3
     - str
     - O
     - 0063
     - 00784
     - Contact Relationship
   * - 49
     - ``gt1_49``
     - 20
     - str
     - O
     -
     - 00785
     - Job Title
   * - 50
     - ``gt1_50``
     -
     - :ref:`JCC <hl7-v2_5_1-JCC>`
     - O
     -
     - 00786
     - Job Code/Class
   * - 51
     - ``gt1_51``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 01299
     - Guarantor Employer's Organization Name
   * - 52
     - ``gt1_52``
     - 2
     - str
     - O
     - 0295
     - 00753
     - Handicap
   * - 53
     - ``gt1_53``
     - 2
     - str
     - O
     - 0311
     - 00752
     - Job Status
   * - 54
     - ``gt1_54``
     -
     - :ref:`FC <hl7-v2_5_1-FC>`
     - O
     -
     - 01231
     - Guarantor Financial Class
   * - 55
     - ``gt1_55``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0005
     - 01291
     - Guarantor Race
   * - 56
     - ``gt1_56``
     - 250
     - str
     - O
     -
     - 01851
     - Guarantor Birth Place
   * - 57
     - ``gt1_57``
     - 2
     - str
     - O
     - 0099
     - 00146
     - VIP Indicator

.. _hl7-v2_5_1-IAM:

IAM: Patient Adverse Reaction Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.4.7

.. py:class:: hl7types.hl7.v2_5_1.segments.IAM.IAM
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
     - ``iam_1``
     - 4
     - str
     - R
     -
     - 01612
     - Set ID - IAM
   * - 2
     - ``iam_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0127
     - 00204
     - Allergen Type Code
   * - 3
     - ``iam_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00205
     - Allergen Code/Mnemonic/Description
   * - 4
     - ``iam_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0128
     - 00206
     - Allergy Severity Code
   * - 5
     - ``iam_5``
     - 15
     - list[str]
     - O
     -
     - 00207
     - Allergy Reaction Code
   * - 6
     - ``iam_6``
     -
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - R
     - 0323
     - 01551
     - Allergy Action Code
   * - 7
     - ``iam_7``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 01552
     - Allergy Unique Identifier
   * - 8
     - ``iam_8``
     - 60
     - str
     - O
     -
     - 01553
     - Action Reason
   * - 9
     - ``iam_9``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0436
     - 01554
     - Sensitivity to Causative Agent Code
   * - 10
     - ``iam_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01555
     - Allergen Group Code/Mnemonic/Description
   * - 11
     - ``iam_11``
     - 8
     - str
     - O
     -
     - 01556
     - Onset Date
   * - 12
     - ``iam_12``
     - 60
     - str
     - O
     -
     - 01557
     - Onset Date Text
   * - 13
     - ``iam_13``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01558
     - Reported Date/Time
   * - 14
     - ``iam_14``
     -
     - :ref:`XPN <hl7-v2_5_1-XPN>`
     - O
     -
     - 01559
     - Reported By
   * - 15
     - ``iam_15``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0063
     - 01560
     - Relationship to Patient Code
   * - 16
     - ``iam_16``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0437
     - 01561
     - Alert Device Code
   * - 17
     - ``iam_17``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0438
     - 01562
     - Allergy Clinical Status Code
   * - 18
     - ``iam_18``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 01563
     - Statused by Person
   * - 19
     - ``iam_19``
     -
     - :ref:`XON <hl7-v2_5_1-XON>`
     - O
     -
     - 01564
     - Statused by Organization
   * - 20
     - ``iam_20``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01565
     - Statused at Date/Time

.. _hl7-v2_5_1-IIM:

IIM: Inventory Item Master
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.12.2

.. py:class:: hl7types.hl7.v2_5_1.segments.IIM.IIM
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
     - ``iim_1``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - R
     -
     - 01897
     - Primary Key Value - IIM
   * - 2
     - ``iim_2``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - R
     -
     - 01799
     - Service Item Code
   * - 3
     - ``iim_3``
     - 250
     - str
     - O
     -
     - 01800
     - Inventory Lot Number
   * - 4
     - ``iim_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01801
     - Inventory Expiration Date
   * - 5
     - ``iim_5``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01802
     - Inventory Manufacturer Name
   * - 6
     - ``iim_6``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01803
     - Inventory Location
   * - 7
     - ``iim_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01804
     - Inventory Received Date
   * - 8
     - ``iim_8``
     - 12
     - str
     - O
     -
     - 01805
     - Inventory Received Quantity
   * - 9
     - ``iim_9``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01806
     - Inventory Received Quantity Unit
   * - 10
     - ``iim_10``
     -
     - :ref:`MO <hl7-v2_5_1-MO>`
     - O
     -
     - 01807
     - Inventory Received Item Cost
   * - 11
     - ``iim_11``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01808
     - Inventory On Hand Date
   * - 12
     - ``iim_12``
     - 12
     - str
     - O
     -
     - 01809
     - Inventory On Hand Quantity
   * - 13
     - ``iim_13``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01810
     - Inventory On Hand Quantity Unit
   * - 14
     - ``iim_14``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0088
     - 00393
     - Procedure Code
   * - 15
     - ``iim_15``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0340
     - 01316
     - Procedure Code Modifier

.. _hl7-v2_5_1-IN1:

IN1: Insurance
~~~~~~~~~~~~~~

Section 6.5.6

.. py:class:: hl7types.hl7.v2_5_1.segments.IN1.IN1
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
     - Set ID - IN1
   * - 2
     - ``in1_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0072
     - 00368
     - Insurance Plan ID
   * - 3
     - ``in1_3``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - R
     -
     - 00428
     - Insurance Company ID
   * - 4
     - ``in1_4``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 00429
     - Insurance Company Name
   * - 5
     - ``in1_5``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00430
     - Insurance Company Address
   * - 6
     - ``in1_6``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00431
     - Insurance Co Contact Person
   * - 7
     - ``in1_7``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00432
     - Insurance Co Phone Number
   * - 8
     - ``in1_8``
     - 12
     - str
     - O
     -
     - 00433
     - Group Number
   * - 9
     - ``in1_9``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 00434
     - Group Name
   * - 10
     - ``in1_10``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00435
     - Insured's Group Emp ID
   * - 11
     - ``in1_11``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 00436
     - Insured's Group Emp Name
   * - 12
     - ``in1_12``
     - 8
     - str
     - O
     -
     - 00437
     - Plan Effective Date
   * - 13
     - ``in1_13``
     - 8
     - str
     - O
     -
     - 00438
     - Plan Expiration Date
   * - 14
     - ``in1_14``
     -
     - :ref:`AUI <hl7-v2_5_1-AUI>`
     - O
     -
     - 00439
     - Authorization Information
   * - 15
     - ``in1_15``
     - 3
     - str
     - O
     - 0086
     - 00440
     - Plan Type
   * - 16
     - ``in1_16``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00441
     - Name Of Insured
   * - 17
     - ``in1_17``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0063
     - 00442
     - Insured's Relationship To Patient
   * - 18
     - ``in1_18``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00443
     - Insured's Date Of Birth
   * - 19
     - ``in1_19``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00444
     - Insured's Address
   * - 20
     - ``in1_20``
     - 2
     - str
     - O
     - 0135
     - 00445
     - Assignment Of Benefits
   * - 21
     - ``in1_21``
     - 2
     - str
     - O
     - 0173
     - 00446
     - Coordination Of Benefits
   * - 22
     - ``in1_22``
     - 2
     - str
     - O
     -
     - 00447
     - Coord Of Ben. Priority
   * - 23
     - ``in1_23``
     - 1
     - str
     - O
     - 0136
     - 00448
     - Notice Of Admission Flag
   * - 24
     - ``in1_24``
     - 8
     - str
     - O
     -
     - 00449
     - Notice Of Admission Date
   * - 25
     - ``in1_25``
     - 1
     - str
     - O
     - 0136
     - 00450
     - Report Of Eligibility Flag
   * - 26
     - ``in1_26``
     - 8
     - str
     - O
     -
     - 00451
     - Report Of Eligibility Date
   * - 27
     - ``in1_27``
     - 2
     - str
     - O
     - 0093
     - 00452
     - Release Information Code
   * - 28
     - ``in1_28``
     - 15
     - str
     - O
     -
     - 00453
     - Pre-Admit Cert (PAC)
   * - 29
     - ``in1_29``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00454
     - Verification Date/Time
   * - 30
     - ``in1_30``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00455
     - Verification By
   * - 31
     - ``in1_31``
     - 2
     - str
     - O
     - 0098
     - 00456
     - Type Of Agreement Code
   * - 32
     - ``in1_32``
     - 2
     - str
     - O
     - 0022
     - 00457
     - Billing Status
   * - 33
     - ``in1_33``
     - 4
     - str
     - O
     -
     - 00458
     - Lifetime Reserve Days
   * - 34
     - ``in1_34``
     - 4
     - str
     - O
     -
     - 00459
     - Delay Before L.R. Day
   * - 35
     - ``in1_35``
     - 8
     - str
     - O
     - 0042
     - 00460
     - Company Plan Code
   * - 36
     - ``in1_36``
     - 15
     - str
     - O
     -
     - 00461
     - Policy Number
   * - 37
     - ``in1_37``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00462
     - Policy Deductible
   * - 38
     - ``in1_38``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00463
     - Policy Limit - Amount
   * - 39
     - ``in1_39``
     - 4
     - str
     - O
     -
     - 00464
     - Policy Limit - Days
   * - 40
     - ``in1_40``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00465
     - Room Rate - Semi-Private
   * - 41
     - ``in1_41``
     -
     - :ref:`CP <hl7-v2_5_1-CP>`
     - O
     -
     - 00466
     - Room Rate - Private
   * - 42
     - ``in1_42``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0066
     - 00467
     - Insured's Employment Status
   * - 43
     - ``in1_43``
     - 1
     - str
     - O
     - 0001
     - 00468
     - Insured's Administrative Sex
   * - 44
     - ``in1_44``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00469
     - Insured's Employer's Address
   * - 45
     - ``in1_45``
     - 2
     - str
     - O
     -
     - 00470
     - Verification Status
   * - 46
     - ``in1_46``
     - 8
     - str
     - O
     - 0072
     - 00471
     - Prior Insurance Plan ID
   * - 47
     - ``in1_47``
     - 3
     - str
     - O
     - 0309
     - 01227
     - Coverage Type
   * - 48
     - ``in1_48``
     - 2
     - str
     - O
     - 0295
     - 00753
     - Handicap
   * - 49
     - ``in1_49``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 01230
     - Insured's ID Number
   * - 50
     - ``in1_50``
     - 1
     - str
     - O
     - 0535
     - 01854
     - Signature Code
   * - 51
     - ``in1_51``
     - 8
     - str
     - O
     -
     - 01855
     - Signature Code Date
   * - 52
     - ``in1_52``
     - 250
     - str
     - O
     -
     - 01899
     - Insured's Birth Place
   * - 53
     - ``in1_53``
     - 2
     - str
     - O
     - 0099
     - 01852
     - VIP Indicator

.. _hl7-v2_5_1-IN2:

IN2: Insurance Additional Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.5.7

.. py:class:: hl7types.hl7.v2_5_1.segments.IN2.IN2
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
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00472
     - Insured's Employee ID
   * - 2
     - ``in2_2``
     - 11
     - str
     - O
     -
     - 00473
     - Insured's Social Security Number
   * - 3
     - ``in2_3``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00474
     - Insured's Employer's Name and ID
   * - 4
     - ``in2_4``
     - 1
     - str
     - O
     - 0139
     - 00475
     - Employer Information Data
   * - 5
     - ``in2_5``
     - 1
     - list[str]
     - O
     - 0137
     - 00476
     - Mail Claim Party
   * - 6
     - ``in2_6``
     - 15
     - str
     - O
     -
     - 00477
     - Medicare Health Ins Card Number
   * - 7
     - ``in2_7``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00478
     - Medicaid Case Name
   * - 8
     - ``in2_8``
     - 15
     - str
     - O
     -
     - 00479
     - Medicaid Case Number
   * - 9
     - ``in2_9``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00480
     - Military Sponsor Name
   * - 10
     - ``in2_10``
     - 20
     - str
     - O
     -
     - 00481
     - Military ID Number
   * - 11
     - ``in2_11``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0342
     - 00482
     - Dependent Of Military Recipient
   * - 12
     - ``in2_12``
     - 25
     - str
     - O
     -
     - 00483
     - Military Organization
   * - 13
     - ``in2_13``
     - 25
     - str
     - O
     -
     - 00484
     - Military Station
   * - 14
     - ``in2_14``
     - 14
     - str
     - O
     - 0140
     - 00485
     - Military Service
   * - 15
     - ``in2_15``
     - 2
     - str
     - O
     - 0141
     - 00486
     - Military Rank/Grade
   * - 16
     - ``in2_16``
     - 3
     - str
     - O
     - 0142
     - 00487
     - Military Status
   * - 17
     - ``in2_17``
     - 8
     - str
     - O
     -
     - 00488
     - Military Retire Date
   * - 18
     - ``in2_18``
     - 1
     - str
     - O
     - 0136
     - 00489
     - Military Non-Avail Cert On File
   * - 19
     - ``in2_19``
     - 1
     - str
     - O
     - 0136
     - 00490
     - Baby Coverage
   * - 20
     - ``in2_20``
     - 1
     - str
     - O
     - 0136
     - 00491
     - Combine Baby Bill
   * - 21
     - ``in2_21``
     - 1
     - str
     - O
     -
     - 00492
     - Blood Deductible
   * - 22
     - ``in2_22``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00493
     - Special Coverage Approval Name
   * - 23
     - ``in2_23``
     - 30
     - str
     - O
     -
     - 00494
     - Special Coverage Approval Title
   * - 24
     - ``in2_24``
     - 8
     - list[str]
     - O
     - 0143
     - 00495
     - Non-Covered Insurance Code
   * - 25
     - ``in2_25``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00496
     - Payor ID
   * - 26
     - ``in2_26``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00497
     - Payor Subscriber ID
   * - 27
     - ``in2_27``
     - 1
     - str
     - O
     - 0144
     - 00498
     - Eligibility Source
   * - 28
     - ``in2_28``
     -
     - list[:ref:`RMC <hl7-v2_5_1-RMC>`]
     - O
     -
     - 00499
     - Room Coverage Type/Amount
   * - 29
     - ``in2_29``
     -
     - list[:ref:`PTA <hl7-v2_5_1-PTA>`]
     - O
     -
     - 00500
     - Policy Type/Amount
   * - 30
     - ``in2_30``
     -
     - :ref:`DDI <hl7-v2_5_1-DDI>`
     - O
     -
     - 00501
     - Daily Deductible
   * - 31
     - ``in2_31``
     - 2
     - str
     - O
     - 0223
     - 00755
     - Living Dependency
   * - 32
     - ``in2_32``
     - 2
     - list[str]
     - O
     - 0009
     - 00145
     - Ambulatory Status
   * - 33
     - ``in2_33``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0171
     - 00129
     - Citizenship
   * - 34
     - ``in2_34``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0296
     - 00118
     - Primary Language
   * - 35
     - ``in2_35``
     - 2
     - str
     - O
     - 0220
     - 00742
     - Living Arrangement
   * - 36
     - ``in2_36``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0215
     - 00743
     - Publicity Code
   * - 37
     - ``in2_37``
     - 1
     - str
     - O
     - 0136
     - 00744
     - Protection Indicator
   * - 38
     - ``in2_38``
     - 2
     - str
     - O
     - 0231
     - 00745
     - Student Indicator
   * - 39
     - ``in2_39``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0006
     - 00120
     - Religion
   * - 40
     - ``in2_40``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00109
     - Mother's Maiden Name
   * - 41
     - ``in2_41``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0212
     - 00739
     - Nationality
   * - 42
     - ``in2_42``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0189
     - 00125
     - Ethnic Group
   * - 43
     - ``in2_43``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0002
     - 00119
     - Marital Status
   * - 44
     - ``in2_44``
     - 8
     - str
     - O
     -
     - 00787
     - Insured's Employment Start Date
   * - 45
     - ``in2_45``
     - 8
     - str
     - O
     -
     - 00783
     - Employment Stop Date
   * - 46
     - ``in2_46``
     - 20
     - str
     - O
     -
     - 00785
     - Job Title
   * - 47
     - ``in2_47``
     -
     - :ref:`JCC <hl7-v2_5_1-JCC>`
     - O
     -
     - 00786
     - Job Code/Class
   * - 48
     - ``in2_48``
     - 2
     - str
     - O
     - 0311
     - 00752
     - Job Status
   * - 49
     - ``in2_49``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00789
     - Employer Contact Person Name
   * - 50
     - ``in2_50``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00790
     - Employer Contact Person Phone Number
   * - 51
     - ``in2_51``
     - 2
     - str
     - O
     - 0222
     - 00791
     - Employer Contact Reason
   * - 52
     - ``in2_52``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00792
     - Insured's Contact Person's Name
   * - 53
     - ``in2_53``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00793
     - Insured's Contact Person Phone Number
   * - 54
     - ``in2_54``
     - 2
     - list[str]
     - O
     - 0222
     - 00794
     - Insured's Contact Person Reason
   * - 55
     - ``in2_55``
     - 8
     - str
     - O
     -
     - 00795
     - Relationship to the Patient Start Date
   * - 56
     - ``in2_56``
     - 8
     - list[str]
     - O
     -
     - 00796
     - Relationship to the Patient Stop Date
   * - 57
     - ``in2_57``
     - 2
     - str
     - O
     - 0232
     - 00797
     - Insurance Co. Contact Reason
   * - 58
     - ``in2_58``
     -
     - :ref:`XTN <hl7-v2_5_1-XTN>`
     - O
     -
     - 00798
     - Insurance Co Contact Phone Number
   * - 59
     - ``in2_59``
     - 2
     - str
     - O
     - 0312
     - 00799
     - Policy Scope
   * - 60
     - ``in2_60``
     - 2
     - str
     - O
     - 0313
     - 00800
     - Policy Source
   * - 61
     - ``in2_61``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 00801
     - Patient Member Number
   * - 62
     - ``in2_62``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0063
     - 00802
     - Guarantor's Relationship to Insured
   * - 63
     - ``in2_63``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00803
     - Insured's Phone Number - Home
   * - 64
     - ``in2_64``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00804
     - Insured's Employer Phone Number
   * - 65
     - ``in2_65``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0343
     - 00805
     - Military Handicapped Program
   * - 66
     - ``in2_66``
     - 1
     - str
     - O
     - 0136
     - 00806
     - Suspend Flag
   * - 67
     - ``in2_67``
     - 1
     - str
     - O
     - 0136
     - 00807
     - Copay Limit Flag
   * - 68
     - ``in2_68``
     - 1
     - str
     - O
     - 0136
     - 00808
     - Stoploss Limit Flag
   * - 69
     - ``in2_69``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 00809
     - Insured Organization Name and ID
   * - 70
     - ``in2_70``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 00810
     - Insured Employer Organization Name and ID
   * - 71
     - ``in2_71``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0005
     - 00113
     - Race
   * - 72
     - ``in2_72``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0344
     - 00811
     - CMS Patient's Relationship to Insured

.. _hl7-v2_5_1-IN3:

IN3: Insurance Additional Information, Certification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.5.8

.. py:class:: hl7types.hl7.v2_5_1.segments.IN3.IN3
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
     - Set ID - IN3
   * - 2
     - ``in3_2``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 00503
     - Certification Number
   * - 3
     - ``in3_3``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00504
     - Certified By
   * - 4
     - ``in3_4``
     - 1
     - str
     - O
     - 0136
     - 00505
     - Certification Required
   * - 5
     - ``in3_5``
     -
     - :ref:`MOP <hl7-v2_5_1-MOP>`
     - O
     -
     - 00506
     - Penalty
   * - 6
     - ``in3_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00507
     - Certification Date/Time
   * - 7
     - ``in3_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00508
     - Certification Modify Date/Time
   * - 8
     - ``in3_8``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
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
     - Certification Begin Date
   * - 10
     - ``in3_10``
     - 8
     - str
     - O
     -
     - 00511
     - Certification End Date
   * - 11
     - ``in3_11``
     -
     - :ref:`DTN <hl7-v2_5_1-DTN>`
     - O
     -
     - 00512
     - Days
   * - 12
     - ``in3_12``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0233
     - 00513
     - Non-Concur Code/Description
   * - 13
     - ``in3_13``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00514
     - Non-Concur Effective Date/Time
   * - 14
     - ``in3_14``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     - 0010
     - 00515
     - Physician Reviewer
   * - 15
     - ``in3_15``
     - 48
     - str
     - O
     -
     - 00516
     - Certification Contact
   * - 16
     - ``in3_16``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00517
     - Certification Contact Phone Number
   * - 17
     - ``in3_17``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0345
     - 00518
     - Appeal Reason
   * - 18
     - ``in3_18``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0346
     - 00519
     - Certification Agency
   * - 19
     - ``in3_19``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00520
     - Certification Agency Phone Number
   * - 20
     - ``in3_20``
     -
     - list[:ref:`ICD <hl7-v2_5_1-ICD>`]
     - O
     -
     - 00521
     - Pre-Certification Requirement
   * - 21
     - ``in3_21``
     - 48
     - str
     - O
     -
     - 00522
     - Case Manager
   * - 22
     - ``in3_22``
     - 8
     - str
     - O
     -
     - 00523
     - Second Opinion Date
   * - 23
     - ``in3_23``
     - 1
     - str
     - O
     - 0151
     - 00524
     - Second Opinion Status
   * - 24
     - ``in3_24``
     - 1
     - list[str]
     - O
     - 0152
     - 00525
     - Second Opinion Documentation Received
   * - 25
     - ``in3_25``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     - 0010
     - 00526
     - Second Opinion Physician

.. _hl7-v2_5_1-INV:

INV: Inventory Detail
~~~~~~~~~~~~~~~~~~~~~

Section 13.4.4

.. py:class:: hl7types.hl7.v2_5_1.segments.INV.INV
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
     - ``inv_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0451
     - 01372
     - Substance Identifier
   * - 2
     - ``inv_2``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - R
     - 0383
     - 01373
     - Substance Status
   * - 3
     - ``inv_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0384
     - 01374
     - Substance Type
   * - 4
     - ``inv_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01532
     - Inventory Container Identifier
   * - 5
     - ``inv_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01376
     - Container Carrier Identifier
   * - 6
     - ``inv_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01377
     - Position on Carrier
   * - 7
     - ``inv_7``
     - 20
     - str
     - O
     -
     - 01378
     - Initial Quantity
   * - 8
     - ``inv_8``
     - 20
     - str
     - O
     -
     - 01379
     - Current Quantity
   * - 9
     - ``inv_9``
     - 20
     - str
     - O
     -
     - 01380
     - Available Quantity
   * - 10
     - ``inv_10``
     - 20
     - str
     - O
     -
     - 01381
     - Consumption Quantity
   * - 11
     - ``inv_11``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01382
     - Quantity Units
   * - 12
     - ``inv_12``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01383
     - Expiration Date/Time
   * - 13
     - ``inv_13``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01384
     - First Used Date/Time
   * - 14
     - ``inv_14``
     -
     - :ref:`TQ <hl7-v2_5_1-TQ>`
     - O
     -
     - 01385
     - On Board Stability Duration
   * - 15
     - ``inv_15``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01386
     - Test/Fluid Identifier(s)
   * - 16
     - ``inv_16``
     - 200
     - str
     - O
     -
     - 01387
     - Manufacturer Lot Number
   * - 17
     - ``inv_17``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0385
     - 00286
     - Manufacturer Identifier
   * - 18
     - ``inv_18``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0386
     - 01389
     - Supplier Identifier
   * - 19
     - ``inv_19``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01626
     - On Board Stability Time
   * - 20
     - ``inv_20``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01896
     - Target Value

.. _hl7-v2_5_1-IPC:

IPC: Imaging Procedure Control Segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.5.6

.. py:class:: hl7types.hl7.v2_5_1.segments.IPC.IPC
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
     - ``ipc_1``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01330
     - Accession Identifier
   * - 2
     - ``ipc_2``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01658
     - Requested Procedure ID
   * - 3
     - ``ipc_3``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01659
     - Study Instance UID
   * - 4
     - ``ipc_4``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01660
     - Scheduled Procedure Step ID
   * - 5
     - ``ipc_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01661
     - Modality
   * - 6
     - ``ipc_6``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01662
     - Protocol Code
   * - 7
     - ``ipc_7``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 01663
     - Scheduled Station Name
   * - 8
     - ``ipc_8``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01664
     - Scheduled Procedure Step Location
   * - 9
     - ``ipc_9``
     - 16
     - str
     - O
     -
     - 01665
     - Scheduled AE Title

.. _hl7-v2_5_1-ISD:

ISD: Interaction Status Detail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.4.2

.. py:class:: hl7types.hl7.v2_5_1.segments.ISD.ISD
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
     - ``isd_1``
     - 20
     - str
     - R
     -
     - 01326
     - Reference Interaction Number (unique identifier)
   * - 2
     - ``isd_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0368
     - 01327
     - Interaction Type Identifier
   * - 3
     - ``isd_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0387
     - 01328
     - Interaction Active State

.. _hl7-v2_5_1-LAN:

LAN: Language Detail
~~~~~~~~~~~~~~~~~~~~

Section 15.4.4

.. py:class:: hl7types.hl7.v2_5_1.segments.LAN.LAN
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
     - ``lan_1``
     - 60
     - str
     - R
     -
     - 01455
     - Set ID - LAN
   * - 2
     - ``lan_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0296
     - 01456
     - Language Code
   * - 3
     - ``lan_3``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0403
     - 01457
     - Language Ability Code
   * - 4
     - ``lan_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0404
     - 01458
     - Language Proficiency Code

.. _hl7-v2_5_1-LCC:

LCC: Location Charge Code
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.9.6

.. py:class:: hl7types.hl7.v2_5_1.segments.LCC.LCC
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
     - ``lcc_1``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - R
     -
     - 00979
     - Primary Key Value - LCC
   * - 2
     - ``lcc_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0264
     - 00964
     - Location Department
   * - 3
     - ``lcc_3``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0129
     - 00980
     - Accommodation Type
   * - 4
     - ``lcc_4``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - R
     - 0132
     - 00981
     - Charge Code

.. _hl7-v2_5_1-LCH:

LCH: Location Characteristic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.9.3

.. py:class:: hl7types.hl7.v2_5_1.segments.LCH.LCH
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
     - ``lch_1``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - R
     -
     - 01305
     - Primary Key Value - LCH
   * - 2
     - ``lch_2``
     - 3
     - str
     - O
     - 0206
     - 00763
     - Segment Action Code
   * - 3
     - ``lch_3``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 00764
     - Segment Unique Key
   * - 4
     - ``lch_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0324
     - 01295
     - Location Characteristic ID
   * - 5
     - ``lch_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0136
     - 01294
     - Location Characteristic Value-LCH

.. _hl7-v2_5_1-LDP:

LDP: Location Department
~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.9.5

.. py:class:: hl7types.hl7.v2_5_1.segments.LDP.LDP
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
     - ``ldp_1``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - R
     -
     - 00963
     - Primary Key Value - LDP
   * - 2
     - ``ldp_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0264
     - 00964
     - Location Department
   * - 3
     - ``ldp_3``
     - 3
     - list[str]
     - O
     - 0069
     - 00965
     - Location Service
   * - 4
     - ``ldp_4``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0265
     - 00966
     - Specialty Type
   * - 5
     - ``ldp_5``
     - 1
     - list[str]
     - O
     - 0004
     - 00967
     - Valid Patient Classes
   * - 6
     - ``ldp_6``
     - 1
     - str
     - O
     - 0183
     - 00675
     - Active/Inactive Flag
   * - 7
     - ``ldp_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00969
     - Activation Date  LDP
   * - 8
     - ``ldp_8``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00970
     - Inactivation Date - LDP
   * - 9
     - ``ldp_9``
     - 80
     - str
     - O
     -
     - 00971
     - Inactivated Reason
   * - 10
     - ``ldp_10``
     -
     - list[:ref:`VH <hl7-v2_5_1-VH>`]
     - O
     - 0267
     - 00976
     - Visiting Hours
   * - 11
     - ``ldp_11``
     -
     - :ref:`XTN <hl7-v2_5_1-XTN>`
     - O
     -
     - 00978
     - Contact Phone
   * - 12
     - ``ldp_12``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0462
     - 01584
     - Location Cost Center

.. _hl7-v2_5_1-LOC:

LOC: Location Identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.9.2

.. py:class:: hl7types.hl7.v2_5_1.segments.LOC.LOC
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
     - ``loc_1``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - R
     -
     - 01307
     - Primary Key Value - LOC
   * - 2
     - ``loc_2``
     - 48
     - str
     - O
     -
     - 00944
     - Location Description
   * - 3
     - ``loc_3``
     - 2
     - list[str]
     - R
     - 0260
     - 00945
     - Location Type - LOC
   * - 4
     - ``loc_4``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 00947
     - Organization Name - LOC
   * - 5
     - ``loc_5``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00948
     - Location Address
   * - 6
     - ``loc_6``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00949
     - Location Phone
   * - 7
     - ``loc_7``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0461
     - 00951
     - License Number
   * - 8
     - ``loc_8``
     - 3
     - list[str]
     - O
     - 0261
     - 00953
     - Location Equipment
   * - 9
     - ``loc_9``
     - 1
     - str
     - O
     - 0442
     - 01583
     - Location Service Code

.. _hl7-v2_5_1-LRL:

LRL: Location Relationship
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.9.4

.. py:class:: hl7types.hl7.v2_5_1.segments.LRL.LRL
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
     - ``lrl_1``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - R
     -
     - 00943
     - Primary Key Value - LRL
   * - 2
     - ``lrl_2``
     - 3
     - str
     - O
     - 0206
     - 00763
     - Segment Action Code
   * - 3
     - ``lrl_3``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 00764
     - Segment Unique Key
   * - 4
     - ``lrl_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0325
     - 01277
     - Location Relationship ID
   * - 5
     - ``lrl_5``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - C
     -
     - 01301
     - Organizational Location Relationship Value
   * - 6
     - ``lrl_6``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - C
     -
     - 01292
     - Patient Location Relationship Value

.. _hl7-v2_5_1-MFA:

MFA: Master File Acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.5.3

.. py:class:: hl7types.hl7.v2_5_1.segments.MFA.MFA
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
     - Record-Level Event Code
   * - 2
     - ``mfa_2``
     - 20
     - str
     - C
     -
     - 00665
     - MFN Control ID
   * - 3
     - ``mfa_3``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00668
     - Event Completion Date/Time
   * - 4
     - ``mfa_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0181
     - 00669
     - MFN Record Level Error Return
   * - 5
     - ``mfa_5``
     -
     - list[str]
     - R
     - 9999
     - 01308
     - Primary Key Value - MFA
   * - 6
     - ``mfa_6``
     - 3
     - list[str]
     - R
     - 0355
     - 01320
     - Primary Key Value Type - MFA

.. _hl7-v2_5_1-MFE:

MFE: Master File Entry
~~~~~~~~~~~~~~~~~~~~~~

Section 8.5.2

.. py:class:: hl7types.hl7.v2_5_1.segments.MFE.MFE
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
     - Record-Level Event Code
   * - 2
     - ``mfe_2``
     - 20
     - str
     - C
     -
     - 00665
     - MFN Control ID
   * - 3
     - ``mfe_3``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00662
     - Effective Date/Time
   * - 4
     - ``mfe_4``
     -
     - list[str]
     - R
     - 9999
     - 00667
     - Primary Key Value - MFE
   * - 5
     - ``mfe_5``
     - 3
     - list[str]
     - R
     - 0355
     - 01319
     - Primary Key Value Type

.. _hl7-v2_5_1-MFI:

MFI: Master File Identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.5.1

.. py:class:: hl7types.hl7.v2_5_1.segments.MFI.MFI
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0175
     - 00658
     - Master File Identifier
   * - 2
     - ``mfi_2``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - 0361
     - 00659
     - Master File Application Identifier
   * - 3
     - ``mfi_3``
     - 3
     - str
     - R
     - 0178
     - 00660
     - File-Level Event Code
   * - 4
     - ``mfi_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00661
     - Entered Date/Time
   * - 5
     - ``mfi_5``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00662
     - Effective Date/Time
   * - 6
     - ``mfi_6``
     - 2
     - str
     - R
     - 0179
     - 00663
     - Response Level Code

.. _hl7-v2_5_1-MRG:

MRG: Merge Patient Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.4.9

.. py:class:: hl7types.hl7.v2_5_1.segments.MRG.MRG
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
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - R
     -
     - 00211
     - Prior Patient Identifier List
   * - 2
     - ``mrg_2``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00212
     - Prior Alternate Patient ID
   * - 3
     - ``mrg_3``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 00213
     - Prior Patient Account Number
   * - 4
     - ``mrg_4``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 00214
     - Prior Patient ID
   * - 5
     - ``mrg_5``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 01279
     - Prior Visit Number
   * - 6
     - ``mrg_6``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 01280
     - Prior Alternate Visit ID
   * - 7
     - ``mrg_7``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 01281
     - Prior Patient Name

.. _hl7-v2_5_1-MSA:

MSA: Message Acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.15.8

.. py:class:: hl7types.hl7.v2_5_1.segments.MSA.MSA
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
     - Acknowledgment Code
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
     -
     - str
     - X
     -
     - 00022
     - Delayed Acknowledgment Type
   * - 6
     - ``msa_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0357
     - 00023
     - Error Condition

.. _hl7-v2_5_1-MSH:

MSH: Message Header
~~~~~~~~~~~~~~~~~~~

Section 2.15.9

.. py:class:: hl7types.hl7.v2_5_1.segments.MSH.MSH
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
     - Field Separator
   * - 2
     - ``msh_2``
     - 4
     - str
     - R
     -
     - 00002
     - Encoding Characters
   * - 3
     - ``msh_3``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - 0361
     - 00003
     - Sending Application
   * - 4
     - ``msh_4``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - 0362
     - 00004
     - Sending Facility
   * - 5
     - ``msh_5``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - 0361
     - 00005
     - Receiving Application
   * - 6
     - ``msh_6``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - 0362
     - 00006
     - Receiving Facility
   * - 7
     - ``msh_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 00007
     - Date/Time Of Message
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
     - :ref:`MSG <hl7-v2_5_1-MSG>`
     - R
     -
     - 00009
     - Message Type
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
     -
     - :ref:`PT <hl7-v2_5_1-PT>`
     - R
     -
     - 00011
     - Processing ID
   * - 12
     - ``msh_12``
     -
     - :ref:`VID <hl7-v2_5_1-VID>`
     - R
     -
     - 00012
     - Version ID
   * - 13
     - ``msh_13``
     - 15
     - str
     - O
     -
     - 00013
     - Sequence Number
   * - 14
     - ``msh_14``
     - 180
     - str
     - O
     -
     - 00014
     - Continuation Pointer
   * - 15
     - ``msh_15``
     - 2
     - str
     - O
     - 0155
     - 00015
     - Accept Acknowledgment Type
   * - 16
     - ``msh_16``
     - 2
     - str
     - O
     - 0155
     - 00016
     - Application Acknowledgment Type
   * - 17
     - ``msh_17``
     - 3
     - str
     - O
     - 0399
     - 00017
     - Country Code
   * - 18
     - ``msh_18``
     - 16
     - list[str]
     - O
     - 0211
     - 00692
     - Character Set
   * - 19
     - ``msh_19``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00693
     - Principal Language Of Message
   * - 20
     - ``msh_20``
     - 20
     - str
     - O
     - 0356
     - 01317
     - Alternate Character Set Handling Scheme
   * - 21
     - ``msh_21``
     -
     - list[:ref:`EI <hl7-v2_5_1-EI>`]
     - O
     -
     - 01598
     - Message Profile Identifier

.. _hl7-v2_5_1-NCK:

NCK: System Clock
~~~~~~~~~~~~~~~~~

Section 14.4.1

.. py:class:: hl7types.hl7.v2_5_1.segments.NCK.NCK
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
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01172
     - System Date/Time

.. _hl7-v2_5_1-NDS:

NDS: Notification Detail
~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.4.7

.. py:class:: hl7types.hl7.v2_5_1.segments.NDS.NDS
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
     - ``nds_1``
     - 20
     - str
     - R
     -
     - 01398
     - Notification Reference Number
   * - 2
     - ``nds_2``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01399
     - Notification Date/Time
   * - 3
     - ``nds_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0367
     - 01400
     - Notification Alert Severity
   * - 4
     - ``nds_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 01401
     - Notification Code

.. _hl7-v2_5_1-NK1:

NK1: Next of Kin / Associated Parties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.4.5

.. py:class:: hl7types.hl7.v2_5_1.segments.NK1.NK1
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
     - Set ID - NK1
   * - 2
     - ``nk1_2``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00191
     - Name
   * - 3
     - ``nk1_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0063
     - 00192
     - Relationship
   * - 4
     - ``nk1_4``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00193
     - Address
   * - 5
     - ``nk1_5``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00194
     - Phone Number
   * - 6
     - ``nk1_6``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00195
     - Business Phone Number
   * - 7
     - ``nk1_7``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
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
     - Next of Kin / Associated Parties Job Title
   * - 11
     - ``nk1_11``
     -
     - :ref:`JCC <hl7-v2_5_1-JCC>`
     - O
     - 0327
     - 00200
     - Next of Kin / Associated Parties Job Code/Class
   * - 12
     - ``nk1_12``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 00201
     - Next of Kin / Associated Parties Employee Number
   * - 13
     - ``nk1_13``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 00202
     - Organization Name - NK1
   * - 14
     - ``nk1_14``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0002
     - 00119
     - Marital Status
   * - 15
     - ``nk1_15``
     - 1
     - str
     - O
     - 0001
     - 00111
     - Administrative Sex
   * - 16
     - ``nk1_16``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00110
     - Date/Time of Birth
   * - 17
     - ``nk1_17``
     - 2
     - list[str]
     - O
     - 0223
     - 00755
     - Living Dependency
   * - 18
     - ``nk1_18``
     - 2
     - list[str]
     - O
     - 0009
     - 00145
     - Ambulatory Status
   * - 19
     - ``nk1_19``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0171
     - 00129
     - Citizenship
   * - 20
     - ``nk1_20``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0296
     - 00118
     - Primary Language
   * - 21
     - ``nk1_21``
     - 2
     - str
     - O
     - 0220
     - 00742
     - Living Arrangement
   * - 22
     - ``nk1_22``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0215
     - 00743
     - Publicity Code
   * - 23
     - ``nk1_23``
     - 1
     - str
     - O
     - 0136
     - 00744
     - Protection Indicator
   * - 24
     - ``nk1_24``
     - 2
     - str
     - O
     - 0231
     - 00745
     - Student Indicator
   * - 25
     - ``nk1_25``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0006
     - 00120
     - Religion
   * - 26
     - ``nk1_26``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00109
     - Mother's Maiden Name
   * - 27
     - ``nk1_27``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0212
     - 00739
     - Nationality
   * - 28
     - ``nk1_28``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0189
     - 00125
     - Ethnic Group
   * - 29
     - ``nk1_29``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0222
     - 00747
     - Contact Reason
   * - 30
     - ``nk1_30``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00748
     - Contact Person's Name
   * - 31
     - ``nk1_31``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00749
     - Contact Person's Telephone Number
   * - 32
     - ``nk1_32``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00750
     - Contact Person's Address
   * - 33
     - ``nk1_33``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00751
     - Next of Kin/Associated Party's Identifiers
   * - 34
     - ``nk1_34``
     - 2
     - str
     - O
     - 0311
     - 00752
     - Job Status
   * - 35
     - ``nk1_35``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0005
     - 00113
     - Race
   * - 36
     - ``nk1_36``
     - 2
     - str
     - O
     - 0295
     - 00753
     - Handicap
   * - 37
     - ``nk1_37``
     - 16
     - str
     - O
     -
     - 00754
     - Contact Person Social Security Number
   * - 38
     - ``nk1_38``
     - 250
     - str
     - O
     -
     - 01905
     - Next of Kin Birth Place
   * - 39
     - ``nk1_39``
     - 2
     - str
     - O
     - 0099
     - 00146
     - VIP Indicator

.. _hl7-v2_5_1-NPU:

NPU: Bed Status Update
~~~~~~~~~~~~~~~~~~~~~~

Section 3.4.8

.. py:class:: hl7types.hl7.v2_5_1.segments.NPU.NPU
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
     - :ref:`PL <hl7-v2_5_1-PL>`
     - R
     -
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

.. _hl7-v2_5_1-NSC:

NSC: Application Status Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 14.4.2

.. py:class:: hl7types.hl7.v2_5_1.segments.NSC.NSC
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
     - 0409
     - 01188
     - Application Change Type
   * - 2
     - ``nsc_2``
     - 30
     - str
     - O
     -
     - 01189
     - Current CPU
   * - 3
     - ``nsc_3``
     - 30
     - str
     - O
     -
     - 01190
     - Current Fileserver
   * - 4
     - ``nsc_4``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 01191
     - Current Application
   * - 5
     - ``nsc_5``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 01192
     - Current Facility
   * - 6
     - ``nsc_6``
     - 30
     - str
     - O
     -
     - 01193
     - New CPU
   * - 7
     - ``nsc_7``
     - 30
     - str
     - O
     -
     - 01194
     - New Fileserver
   * - 8
     - ``nsc_8``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 01195
     - New Application
   * - 9
     - ``nsc_9``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 01196
     - New Facility

.. _hl7-v2_5_1-NST:

NST: Application control level statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 14.4.3

.. py:class:: hl7types.hl7.v2_5_1.segments.NST.NST
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
     - 01173
     - Statistics Available
   * - 2
     - ``nst_2``
     - 30
     - str
     - O
     -
     - 01174
     - Source Identifier
   * - 3
     - ``nst_3``
     - 3
     - str
     - O
     - 0332
     - 01175
     - Source Type
   * - 4
     - ``nst_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01176
     - Statistics Start
   * - 5
     - ``nst_5``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01177
     - Statistics End
   * - 6
     - ``nst_6``
     - 10
     - str
     - O
     -
     - 01178
     - Receive Character Count
   * - 7
     - ``nst_7``
     - 10
     - str
     - O
     -
     - 01179
     - Send Character Count
   * - 8
     - ``nst_8``
     - 10
     - str
     - O
     -
     - 01180
     - Messages Received
   * - 9
     - ``nst_9``
     - 10
     - str
     - O
     -
     - 01181
     - Messages Sent
   * - 10
     - ``nst_10``
     - 10
     - str
     - O
     -
     - 01182
     - Checksum Errors Received
   * - 11
     - ``nst_11``
     - 10
     - str
     - O
     -
     - 01183
     - Length Errors Received
   * - 12
     - ``nst_12``
     - 10
     - str
     - O
     -
     - 01184
     - Other Errors Received
   * - 13
     - ``nst_13``
     - 10
     - str
     - O
     -
     - 01185
     - Connect Timeouts
   * - 14
     - ``nst_14``
     - 10
     - str
     - O
     -
     - 01186
     - Receive Timeouts
   * - 15
     - ``nst_15``
     - 10
     - str
     - O
     -
     - 01187
     - Application control-level Errors

.. _hl7-v2_5_1-NTE:

NTE: Notes and Comments
~~~~~~~~~~~~~~~~~~~~~~~

Section 2.15.10

.. py:class:: hl7types.hl7.v2_5_1.segments.NTE.NTE
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
     - Set ID - NTE
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
   * - 4
     - ``nte_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0364
     - 01318
     - Comment Type

.. _hl7-v2_5_1-OBR:

OBR: Observation Request
~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.5.3

.. py:class:: hl7types.hl7.v2_5_1.segments.OBR.OBR
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
     - Set ID - OBR
   * - 2
     - ``obr_2``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 00216
     - Placer Order Number
   * - 3
     - ``obr_3``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 00217
     - Filler Order Number
   * - 4
     - ``obr_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00238
     - Universal Service Identifier
   * - 5
     - ``obr_5``
     - 2
     - str
     - O
     -
     - 00239
     - Priority - OBR
   * - 6
     - ``obr_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00240
     - Requested Date/Time
   * - 7
     - ``obr_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 00241
     - Observation Date/Time
   * - 8
     - ``obr_8``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00242
     - Observation End Date/Time
   * - 9
     - ``obr_9``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 00243
     - Collection Volume
   * - 10
     - ``obr_10``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
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
     - Specimen Action Code
   * - 12
     - ``obr_12``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
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
     - Relevant Clinical Information
   * - 14
     - ``obr_14``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00248
     - Specimen Received Date/Time
   * - 15
     - ``obr_15``
     -
     - :ref:`SPS <hl7-v2_5_1-SPS>`
     - O
     -
     - 00249
     - Specimen Source
   * - 16
     - ``obr_16``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00226
     - Ordering Provider
   * - 17
     - ``obr_17``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
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
     - Placer Field 1
   * - 19
     - ``obr_19``
     - 60
     - str
     - O
     -
     - 00252
     - Placer Field 2
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
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 00255
     - Results Rpt/Status Chng - Date/Time
   * - 23
     - ``obr_23``
     -
     - :ref:`MOC <hl7-v2_5_1-MOC>`
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
     - Diagnostic Serv Sect ID
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
     - :ref:`PRL <hl7-v2_5_1-PRL>`
     - O
     -
     - 00259
     - Parent Result
   * - 27
     - ``obr_27``
     -
     - list[:ref:`TQ <hl7-v2_5_1-TQ>`]
     - O
     -
     - 00221
     - Quantity/Timing
   * - 28
     - ``obr_28``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00260
     - Result Copies To
   * - 29
     - ``obr_29``
     -
     - :ref:`EIP <hl7-v2_5_1-EIP>`
     - O
     -
     - 00261
     - Parent
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
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00263
     - Reason for Study
   * - 32
     - ``obr_32``
     -
     - :ref:`NDL <hl7-v2_5_1-NDL>`
     - O
     -
     - 00264
     - Principal Result Interpreter
   * - 33
     - ``obr_33``
     -
     - list[:ref:`NDL <hl7-v2_5_1-NDL>`]
     - O
     -
     - 00265
     - Assistant Result Interpreter
   * - 34
     - ``obr_34``
     -
     - list[:ref:`NDL <hl7-v2_5_1-NDL>`]
     - O
     -
     - 00266
     - Technician
   * - 35
     - ``obr_35``
     -
     - list[:ref:`NDL <hl7-v2_5_1-NDL>`]
     - O
     -
     - 00267
     - Transcriptionist
   * - 36
     - ``obr_36``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00268
     - Scheduled Date/Time
   * - 37
     - ``obr_37``
     - 4
     - str
     - O
     -
     - 01028
     - Number of Sample Containers *
   * - 38
     - ``obr_38``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01029
     - Transport Logistics of Collected Sample
   * - 39
     - ``obr_39``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01030
     - Collector's Comment *
   * - 40
     - ``obr_40``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01031
     - Transport Arrangement Responsibility
   * - 41
     - ``obr_41``
     - 30
     - str
     - O
     - 0224
     - 01032
     - Transport Arranged
   * - 42
     - ``obr_42``
     - 1
     - str
     - O
     - 0225
     - 01033
     - Escort Required
   * - 43
     - ``obr_43``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01034
     - Planned Patient Transport Comment
   * - 44
     - ``obr_44``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0088
     - 00393
     - Procedure Code
   * - 45
     - ``obr_45``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0340
     - 01316
     - Procedure Code Modifier
   * - 46
     - ``obr_46``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0411
     - 01474
     - Placer Supplemental Service Information
   * - 47
     - ``obr_47``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0411
     - 01475
     - Filler Supplemental Service Information
   * - 48
     - ``obr_48``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - C
     - 0476
     - 01646
     - Medically Necessary Duplicate Procedure Reason.
   * - 49
     - ``obr_49``
     - 2
     - str
     - O
     - 0507
     - 01647
     - Result Handling
   * - 50
     - ``obr_50``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 02286
     - Parent Universal Service Identifier

.. _hl7-v2_5_1-OBX:

OBX: Observation/Result
~~~~~~~~~~~~~~~~~~~~~~~

Section 7.4.2

.. py:class:: hl7types.hl7.v2_5_1.segments.OBX.OBX
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
     - Set ID - OBX
   * - 2
     - ``obx_2``
     - 2
     - str
     - C
     - 0125
     - 00570
     - Value Type
   * - 3
     - ``obx_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
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
     - list[str]
     - C
     -
     - 00573
     - Observation Value
   * - 6
     - ``obx_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
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
     - 5
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
     - 2
     - list[str]
     - O
     - 0080
     - 00578
     - Nature of Abnormal Test
   * - 11
     - ``obx_11``
     - 1
     - str
     - R
     - 0085
     - 00579
     - Observation Result Status
   * - 12
     - ``obx_12``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00580
     - Effective Date of Reference Range Values
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
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00582
     - Date/Time of the Observation
   * - 15
     - ``obx_15``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00583
     - Producer's Reference
   * - 16
     - ``obx_16``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00584
     - Responsible Observer
   * - 17
     - ``obx_17``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00936
     - Observation Method
   * - 18
     - ``obx_18``
     -
     - list[:ref:`EI <hl7-v2_5_1-EI>`]
     - O
     -
     - 01479
     - Equipment Instance Identifier
   * - 19
     - ``obx_19``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01480
     - Date/Time of the Analysis
   * - 20
     - ``obx_20``
     -
     - :ref:`XON <hl7-v2_5_1-XON>`
     - O
     -
     - 09999
     - Performing Organization Name
   * - 21
     - ``obx_21``
     -
     - :ref:`XAD <hl7-v2_5_1-XAD>`
     - O
     -
     - 09999
     - Performing Organization Address
   * - 22
     - ``obx_22``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 09999
     - Performing Organization Medical Director

.. _hl7-v2_5_1-ODS:

ODS: Dietary Orders, Supplements, and Preferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.1

.. py:class:: hl7types.hl7.v2_5_1.segments.ODS.ODS
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
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00270
     - Service Period
   * - 3
     - ``ods_3``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
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

.. _hl7-v2_5_1-ODT:

ODT: Diet Tray Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.2

.. py:class:: hl7types.hl7.v2_5_1.segments.ODT.ODT
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0160
     - 00273
     - Tray Type
   * - 2
     - ``odt_2``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00270
     - Service Period
   * - 3
     - ``odt_3``
     - 80
     - str
     - O
     -
     - 00272
     - Text Instruction

.. _hl7-v2_5_1-OM1:

OM1: General Segment
~~~~~~~~~~~~~~~~~~~~

Section 8.8.8

.. py:class:: hl7types.hl7.v2_5_1.segments.OM1.OM1
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
     - 4
     - str
     - R
     -
     - 00586
     - Sequence Number - Test/Observation Master File
   * - 2
     - ``om1_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 9999
     - 00587
     - Producer's Service/Test/Observation ID
   * - 3
     - ``om1_3``
     - 12
     - list[str]
     - O
     - 0125
     - 00588
     - Permitted Data Types
   * - 4
     - ``om1_4``
     - 1
     - str
     - R
     - 0136
     - 00589
     - Specimen Required
   * - 5
     - ``om1_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 9999
     - 00590
     - Producer ID
   * - 6
     - ``om1_6``
     -
     - str
     - O
     -
     - 00591
     - Observation Description
   * - 7
     - ``om1_7``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00592
     - Other Service/Test/Observation IDs for the Observation
   * - 8
     - ``om1_8``
     - 200
     - list[str]
     - R
     -
     - 00593
     - Other Names
   * - 9
     - ``om1_9``
     - 30
     - str
     - O
     -
     - 00594
     - Preferred Report Name for the Observation
   * - 10
     - ``om1_10``
     - 8
     - str
     - O
     -
     - 00595
     - Preferred Short Name or Mnemonic for Observation
   * - 11
     - ``om1_11``
     - 200
     - str
     - O
     -
     - 00596
     - Preferred Long Name for the Observation
   * - 12
     - ``om1_12``
     - 1
     - str
     - O
     - 0136
     - 00597
     - Orderability
   * - 13
     - ``om1_13``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 9999
     - 00598
     - Identity of Instrument Used to Perform this Study
   * - 14
     - ``om1_14``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 9999
     - 00599
     - Coded Representation of Method
   * - 15
     - ``om1_15``
     - 1
     - str
     - O
     - 0136
     - 00600
     - Portable Device Indicator
   * - 16
     - ``om1_16``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 9999
     - 00601
     - Observation Producing Department/Section
   * - 17
     - ``om1_17``
     -
     - :ref:`XTN <hl7-v2_5_1-XTN>`
     - O
     -
     - 00602
     - Telephone Number of Section
   * - 18
     - ``om1_18``
     - 1
     - str
     - R
     - 0174
     - 00603
     - Nature of Service/Test/Observation
   * - 19
     - ``om1_19``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00604
     - Report Subheader
   * - 20
     - ``om1_20``
     - 20
     - str
     - O
     -
     - 00605
     - Report Display Order
   * - 21
     - ``om1_21``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00606
     - Date/Time Stamp for any change in Definition for the Observation
   * - 22
     - ``om1_22``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00607
     - Effective Date/Time of Change
   * - 23
     - ``om1_23``
     - 20
     - str
     - O
     -
     - 00608
     - Typical Turn-Around Time
   * - 24
     - ``om1_24``
     - 20
     - str
     - O
     -
     - 00609
     - Processing Time
   * - 25
     - ``om1_25``
     - 40
     - list[str]
     - O
     - 0168
     - 00610
     - Processing Priority
   * - 26
     - ``om1_26``
     - 5
     - str
     - O
     - 0169
     - 00611
     - Reporting Priority
   * - 27
     - ``om1_27``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 9999
     - 00612
     - Outside Site(s) Where Observation may be Performed
   * - 28
     - ``om1_28``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00613
     - Address of Outside Site(s)
   * - 29
     - ``om1_29``
     -
     - :ref:`XTN <hl7-v2_5_1-XTN>`
     - O
     -
     - 00614
     - Phone Number of Outside Site
   * - 30
     - ``om1_30``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0177
     - 00615
     - Confidentiality Code
   * - 31
     - ``om1_31``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00616
     - Observations Required to Interpret the Observation
   * - 32
     - ``om1_32``
     -
     - str
     - O
     -
     - 00617
     - Interpretation of Observations
   * - 33
     - ``om1_33``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00618
     - Contraindications to Observations
   * - 34
     - ``om1_34``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 9999
     - 00619
     - Reflex Tests/Observations
   * - 35
     - ``om1_35``
     -
     - str
     - O
     -
     - 00620
     - Rules that Trigger Reflex Testing
   * - 36
     - ``om1_36``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00621
     - Fixed Canned Message
   * - 37
     - ``om1_37``
     -
     - str
     - O
     -
     - 00622
     - Patient Preparation
   * - 38
     - ``om1_38``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00623
     - Procedure Medication
   * - 39
     - ``om1_39``
     -
     - str
     - O
     -
     - 00624
     - Factors that may Affect the Observation
   * - 40
     - ``om1_40``
     - 60
     - list[str]
     - O
     -
     - 00625
     - Service/Test/Observation Performance Schedule
   * - 41
     - ``om1_41``
     -
     - str
     - O
     -
     - 00626
     - Description of Test Methods
   * - 42
     - ``om1_42``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0254
     - 00937
     - Kind of Quantity Observed
   * - 43
     - ``om1_43``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0255
     - 00938
     - Point Versus Interval
   * - 44
     - ``om1_44``
     -
     - str
     - O
     - 0256
     - 00939
     - Challenge Information
   * - 45
     - ``om1_45``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0258
     - 00940
     - Relationship Modifier
   * - 46
     - ``om1_46``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00941
     - Target Anatomic Site Of Test
   * - 47
     - ``om1_47``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0259
     - 00942
     - Modality Of Imaging Measurement

.. _hl7-v2_5_1-OM2:

OM2: Numeric Observation
~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.8.9

.. py:class:: hl7types.hl7.v2_5_1.segments.OM2.OM2
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
     - 4
     - str
     - O
     -
     - 00586
     - Sequence Number - Test/Observation Master File
   * - 2
     - ``om2_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00627
     - Units of Measure
   * - 3
     - ``om2_3``
     - 10
     - list[str]
     - O
     -
     - 00628
     - Range of Decimal Precision
   * - 4
     - ``om2_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00629
     - Corresponding SI Units of Measure
   * - 5
     - ``om2_5``
     -
     - str
     - O
     -
     - 00630
     - SI Conversion Factor
   * - 6
     - ``om2_6``
     -
     - list[:ref:`RFR <hl7-v2_5_1-RFR>`]
     - O
     -
     - 00631
     - Reference (Normal) Range - Ordinal and Continuous Observations
   * - 7
     - ``om2_7``
     -
     - list[:ref:`RFR <hl7-v2_5_1-RFR>`]
     - O
     -
     - 00632
     - Critical Range for Ordinal and Continuous Observations
   * - 8
     - ``om2_8``
     -
     - :ref:`RFR <hl7-v2_5_1-RFR>`
     - O
     -
     - 00633
     - Absolute Range for Ordinal and Continuous Observations
   * - 9
     - ``om2_9``
     -
     - list[:ref:`DLT <hl7-v2_5_1-DLT>`]
     - O
     -
     - 00634
     - Delta Check Criteria
   * - 10
     - ``om2_10``
     - 20
     - str
     - O
     -
     - 00635
     - Minimum Meaningful Increments

.. _hl7-v2_5_1-OM3:

OM3: Categorical Service/Test/Observation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.8.10

.. py:class:: hl7types.hl7.v2_5_1.segments.OM3.OM3
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
     - 4
     - str
     - O
     -
     - 00586
     - Sequence Number - Test/Observation Master File
   * - 2
     - ``om3_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00636
     - Preferred Coding System
   * - 3
     - ``om3_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00637
     - Valid Coded "Answers"
   * - 4
     - ``om3_4``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 9999
     - 00638
     - Normal Text/Codes for Categorical Observations
   * - 5
     - ``om3_5``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 9999
     - 00639
     - Abnormal Text/Codes for Categorical Observations
   * - 6
     - ``om3_6``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 9999
     - 00640
     - Critical Text/Codes for Categorical Observations
   * - 7
     - ``om3_7``
     - 2
     - str
     - O
     - 0125
     - 00570
     - Value Type

.. _hl7-v2_5_1-OM4:

OM4: Observations that Require Specimens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.8.11

.. py:class:: hl7types.hl7.v2_5_1.segments.OM4.OM4
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
     - 4
     - str
     - O
     -
     - 00586
     - Sequence Number - Test/Observation Master File
   * - 2
     - ``om4_2``
     - 1
     - str
     - O
     - 0170
     - 00642
     - Derived Specimen
   * - 3
     - ``om4_3``
     -
     - str
     - O
     -
     - 00643
     - Container Description
   * - 4
     - ``om4_4``
     - 20
     - str
     - O
     -
     - 00644
     - Container Volume
   * - 5
     - ``om4_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00645
     - Container Units
   * - 6
     - ``om4_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 00646
     - Specimen
   * - 7
     - ``om4_7``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0371
     - 00647
     - Additive
   * - 8
     - ``om4_8``
     -
     - str
     - O
     -
     - 00648
     - Preparation
   * - 9
     - ``om4_9``
     -
     - str
     - O
     -
     - 00649
     - Special Handling Requirements
   * - 10
     - ``om4_10``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 00650
     - Normal Collection Volume
   * - 11
     - ``om4_11``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 00651
     - Minimum Collection Volume
   * - 12
     - ``om4_12``
     -
     - str
     - O
     -
     - 00652
     - Specimen Requirements
   * - 13
     - ``om4_13``
     - 1
     - list[str]
     - O
     - 0027
     - 00653
     - Specimen Priorities
   * - 14
     - ``om4_14``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 00654
     - Specimen Retention Time

.. _hl7-v2_5_1-OM5:

OM5: Observation Batteries (Sets)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.8.12

.. py:class:: hl7types.hl7.v2_5_1.segments.OM5.OM5
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
     - 4
     - str
     - O
     -
     - 00586
     - Sequence Number - Test/Observation Master File
   * - 2
     - ``om5_2``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 9999
     - 00655
     - Test/Observations Included within an Ordered Test Battery
   * - 3
     - ``om5_3``
     - 250
     - str
     - O
     -
     - 00656
     - Observation ID Suffixes

.. _hl7-v2_5_1-OM6:

OM6: Observations that are Calculated from Other Observations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.8.13

.. py:class:: hl7types.hl7.v2_5_1.segments.OM6.OM6
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
     - 4
     - str
     - O
     -
     - 00586
     - Sequence Number - Test/Observation Master File
   * - 2
     - ``om6_2``
     -
     - str
     - O
     -
     - 00657
     - Derivation Rule

.. _hl7-v2_5_1-OM7:

OM7: Additional Basic Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.8.14

.. py:class:: hl7types.hl7.v2_5_1.segments.OM7.OM7
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
     - ``om7_1``
     - 4
     - str
     - R
     -
     - 00586
     - Sequence Number - Test/Observation Master File
   * - 2
     - ``om7_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00238
     - Universal Service Identifier
   * - 3
     - ``om7_3``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0412
     - 01481
     - Category Identifier
   * - 4
     - ``om7_4``
     -
     - str
     - O
     -
     - 01482
     - Category Description
   * - 5
     - ``om7_5``
     - 200
     - list[str]
     - O
     -
     - 01483
     - Category Synonym
   * - 6
     - ``om7_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01484
     - Effective Test/Service Start Date/Time
   * - 7
     - ``om7_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01485
     - Effective Test/Service End Date/Time
   * - 8
     - ``om7_8``
     - 5
     - str
     - O
     -
     - 01486
     - Test/Service Default Duration Quantity
   * - 9
     - ``om7_9``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 9999
     - 01487
     - Test/Service Default Duration Units
   * - 10
     - ``om7_10``
     - 60
     - str
     - O
     - 0335
     - 01488
     - Test/Service Default Frequency
   * - 11
     - ``om7_11``
     - 1
     - str
     - O
     - 0136
     - 01489
     - Consent Indicator
   * - 12
     - ``om7_12``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0413
     - 01490
     - Consent Identifier
   * - 13
     - ``om7_13``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01491
     - Consent Effective Start Date/Time
   * - 14
     - ``om7_14``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01492
     - Consent Effective End Date/Time
   * - 15
     - ``om7_15``
     - 5
     - str
     - O
     -
     - 01493
     - Consent Interval Quantity
   * - 16
     - ``om7_16``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0414
     - 01494
     - Consent Interval Units
   * - 17
     - ``om7_17``
     - 5
     - str
     - O
     -
     - 01495
     - Consent Waiting Period Quantity
   * - 18
     - ``om7_18``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0414
     - 01496
     - Consent Waiting Period Units
   * - 19
     - ``om7_19``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00607
     - Effective Date/Time of Change
   * - 20
     - ``om7_20``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 00224
     - Entered By
   * - 21
     - ``om7_21``
     -
     - list[:ref:`PL <hl7-v2_5_1-PL>`]
     - O
     -
     - 01497
     - Orderable-at Location
   * - 22
     - ``om7_22``
     - 1
     - str
     - O
     - 0473
     - 01498
     - Formulary Status
   * - 23
     - ``om7_23``
     - 1
     - str
     - O
     - 0136
     - 01499
     - Special Order Indicator
   * - 24
     - ``om7_24``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0132
     - 01306
     - Primary Key Value - CDM

.. _hl7-v2_5_1-ORC:

ORC: Common Order
~~~~~~~~~~~~~~~~~

Section 4.5.1

.. py:class:: hl7types.hl7.v2_5_1.segments.ORC.ORC
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
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 00216
     - Placer Order Number
   * - 3
     - ``orc_3``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 00217
     - Filler Order Number
   * - 4
     - ``orc_4``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
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
     - list[:ref:`TQ <hl7-v2_5_1-TQ>`]
     - O
     -
     - 00221
     - Quantity/Timing
   * - 8
     - ``orc_8``
     -
     - :ref:`EIP <hl7-v2_5_1-EIP>`
     - O
     -
     - 00222
     - Parent
   * - 9
     - ``orc_9``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00223
     - Date/Time of Transaction
   * - 10
     - ``orc_10``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00224
     - Entered By
   * - 11
     - ``orc_11``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00225
     - Verified By
   * - 12
     - ``orc_12``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00226
     - Ordering Provider
   * - 13
     - ``orc_13``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 00227
     - Enterer's Location
   * - 14
     - ``orc_14``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00228
     - Call Back Phone Number
   * - 15
     - ``orc_15``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00229
     - Order Effective Date/Time
   * - 16
     - ``orc_16``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00230
     - Order Control Code Reason
   * - 17
     - ``orc_17``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00231
     - Entering Organization
   * - 18
     - ``orc_18``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00232
     - Entering Device
   * - 19
     - ``orc_19``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00233
     - Action By
   * - 20
     - ``orc_20``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0339
     - 01310
     - Advanced Beneficiary Notice Code
   * - 21
     - ``orc_21``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 01311
     - Ordering Facility Name
   * - 22
     - ``orc_22``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 01312
     - Ordering Facility Address
   * - 23
     - ``orc_23``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 01313
     - Ordering Facility Phone Number
   * - 24
     - ``orc_24``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 01314
     - Ordering Provider Address
   * - 25
     - ``orc_25``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01473
     - Order Status Modifier
   * - 26
     - ``orc_26``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - C
     - 0552
     - 01641
     - Advanced Beneficiary Notice Override Reason
   * - 27
     - ``orc_27``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01642
     - Filler's Expected Availability Date/Time
   * - 28
     - ``orc_28``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0177
     - 00615
     - Confidentiality Code
   * - 29
     - ``orc_29``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0482
     - 01643
     - Order Type
   * - 30
     - ``orc_30``
     -
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - O
     - 0483
     - 01644
     - Enterer Authorization Mode
   * - 31
     - ``orc_31``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 02286
     - Parent Universal Service Identifier

.. _hl7-v2_5_1-ORG:

ORG: Practitioner Organization Unit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.4.5

.. py:class:: hl7types.hl7.v2_5_1.segments.ORG.ORG
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
     - ``org_1``
     - 60
     - str
     - R
     -
     - 01459
     - Set ID - ORG
   * - 2
     - ``org_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0405
     - 01460
     - Organization Unit Code
   * - 3
     - ``org_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0474
     - 01625
     - Organization Unit Type Code
   * - 4
     - ``org_4``
     - 1
     - str
     - O
     - 0136
     - 01462
     - Primary Org Unit Indicator
   * - 5
     - ``org_5``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 01463
     - Practitioner Org Unit Identifier
   * - 6
     - ``org_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0452
     - 01464
     - Health Care Provider Type Code
   * - 7
     - ``org_7``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0453
     - 01614
     - Health Care Provider Classification Code
   * - 8
     - ``org_8``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0454
     - 01615
     - Health Care Provider Area of Specialization Code
   * - 9
     - ``org_9``
     -
     - :ref:`DR <hl7-v2_5_1-DR>`
     - O
     -
     - 01465
     - Effective Date Range
   * - 10
     - ``org_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0066
     - 01276
     - Employment Status Code
   * - 11
     - ``org_11``
     - 1
     - str
     - O
     - 0136
     - 01467
     - Board Approval Indicator
   * - 12
     - ``org_12``
     - 1
     - str
     - O
     - 0136
     - 01468
     - Primary Care Physician Indicator

.. _hl7-v2_5_1-OVR:

OVR: Override Segment
~~~~~~~~~~~~~~~~~~~~~

Section 2.15.11

.. py:class:: hl7types.hl7.v2_5_1.segments.OVR.OVR
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
     - ``ovr_1``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0518
     - 01829
     - Business Rule Override Type
   * - 2
     - ``ovr_2``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0521
     - 01830
     - Business Rule Override Code
   * - 3
     - ``ovr_3``
     -
     - str
     - O
     -
     - 01831
     - Override Comments
   * - 4
     - ``ovr_4``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 01832
     - Override Entered By
   * - 5
     - ``ovr_5``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 01833
     - Override Authorized By

.. _hl7-v2_5_1-PCR:

PCR: Possible Causal Relationship
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.12.3

.. py:class:: hl7types.hl7.v2_5_1.segments.PCR.PCR
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
     - ``pcr_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 01098
     - Implicated Product
   * - 2
     - ``pcr_2``
     - 1
     - str
     - O
     - 0249
     - 01099
     - Generic Product
   * - 3
     - ``pcr_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01100
     - Product Class
   * - 4
     - ``pcr_4``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01101
     - Total Duration Of Therapy
   * - 5
     - ``pcr_5``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01102
     - Product Manufacture Date
   * - 6
     - ``pcr_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01103
     - Product Expiration Date
   * - 7
     - ``pcr_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01104
     - Product Implantation Date
   * - 8
     - ``pcr_8``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01105
     - Product Explantation Date
   * - 9
     - ``pcr_9``
     - 8
     - str
     - O
     - 0244
     - 01106
     - Single Use Device
   * - 10
     - ``pcr_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01107
     - Indication For Product Use
   * - 11
     - ``pcr_11``
     - 8
     - str
     - O
     - 0245
     - 01108
     - Product Problem
   * - 12
     - ``pcr_12``
     - 30
     - list[str]
     - O
     -
     - 01109
     - Product Serial/Lot Number
   * - 13
     - ``pcr_13``
     - 1
     - str
     - O
     - 0246
     - 01110
     - Product Available For Inspection
   * - 14
     - ``pcr_14``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01111
     - Product Evaluation Performed
   * - 15
     - ``pcr_15``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0247
     - 01112
     - Product Evaluation Status
   * - 16
     - ``pcr_16``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01113
     - Product Evaluation Results
   * - 17
     - ``pcr_17``
     - 8
     - str
     - O
     - 0248
     - 01114
     - Evaluated Product Source
   * - 18
     - ``pcr_18``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01115
     - Date Product Returned To Manufacturer
   * - 19
     - ``pcr_19``
     - 1
     - str
     - O
     - 0242
     - 01116
     - Device Operator Qualifications
   * - 20
     - ``pcr_20``
     - 1
     - str
     - O
     - 0250
     - 01117
     - Relatedness Assessment
   * - 21
     - ``pcr_21``
     - 2
     - list[str]
     - O
     - 0251
     - 01118
     - Action Taken In Response To The Event
   * - 22
     - ``pcr_22``
     - 2
     - list[str]
     - O
     - 0252
     - 01119
     - Event Causality Observations
   * - 23
     - ``pcr_23``
     - 1
     - list[str]
     - O
     - 0253
     - 01120
     - Indirect Exposure Mechanism

.. _hl7-v2_5_1-PD1:

PD1: Patient Additional Demographic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.4.10

.. py:class:: hl7types.hl7.v2_5_1.segments.PD1.PD1
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
     - ``pd1_1``
     - 2
     - list[str]
     - O
     - 0223
     - 00755
     - Living Dependency
   * - 2
     - ``pd1_2``
     - 2
     - str
     - O
     - 0220
     - 00742
     - Living Arrangement
   * - 3
     - ``pd1_3``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 00756
     - Patient Primary Facility
   * - 4
     - ``pd1_4``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00757
     - Patient Primary Care Provider Name & ID No.
   * - 5
     - ``pd1_5``
     - 2
     - str
     - O
     - 0231
     - 00745
     - Student Indicator
   * - 6
     - ``pd1_6``
     - 2
     - str
     - O
     - 0295
     - 00753
     - Handicap
   * - 7
     - ``pd1_7``
     - 2
     - str
     - O
     - 0315
     - 00759
     - Living Will Code
   * - 8
     - ``pd1_8``
     - 2
     - str
     - O
     - 0316
     - 00760
     - Organ Donor Code
   * - 9
     - ``pd1_9``
     - 1
     - str
     - O
     - 0136
     - 00761
     - Separate Bill
   * - 10
     - ``pd1_10``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00762
     - Duplicate Patient
   * - 11
     - ``pd1_11``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0215
     - 00743
     - Publicity Code
   * - 12
     - ``pd1_12``
     - 1
     - str
     - O
     - 0136
     - 00744
     - Protection Indicator
   * - 13
     - ``pd1_13``
     - 8
     - str
     - O
     -
     - 01566
     - Protection Indicator Effective Date
   * - 14
     - ``pd1_14``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 01567
     - Place of Worship
   * - 15
     - ``pd1_15``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0435
     - 01568
     - Advance Directive Code
   * - 16
     - ``pd1_16``
     - 1
     - str
     - O
     - 0441
     - 01569
     - Immunization Registry Status
   * - 17
     - ``pd1_17``
     - 8
     - str
     - O
     -
     - 01570
     - Immunization Registry Status Effective Date
   * - 18
     - ``pd1_18``
     - 8
     - str
     - O
     -
     - 01571
     - Publicity Code Effective Date
   * - 19
     - ``pd1_19``
     - 5
     - str
     - O
     - 0140
     - 01572
     - Military Branch
   * - 20
     - ``pd1_20``
     - 2
     - str
     - O
     - 0141
     - 00486
     - Military Rank/Grade
   * - 21
     - ``pd1_21``
     - 3
     - str
     - O
     - 0142
     - 01573
     - Military Status

.. _hl7-v2_5_1-PDA:

PDA: Patient Death and Autopsy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.4.12

.. py:class:: hl7types.hl7.v2_5_1.segments.PDA.PDA
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
     - ``pda_1``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01574
     - Death Cause Code
   * - 2
     - ``pda_2``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 01575
     - Death Location
   * - 3
     - ``pda_3``
     - 1
     - str
     - O
     - 0136
     - 01576
     - Death Certified Indicator
   * - 4
     - ``pda_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01577
     - Death Certificate Signed Date/Time
   * - 5
     - ``pda_5``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 01578
     - Death Certified By
   * - 6
     - ``pda_6``
     - 1
     - str
     - O
     - 0136
     - 01579
     - Autopsy Indicator
   * - 7
     - ``pda_7``
     -
     - :ref:`DR <hl7-v2_5_1-DR>`
     - O
     -
     - 01580
     - Autopsy Start and End Date/Time
   * - 8
     - ``pda_8``
     -
     - :ref:`XCN <hl7-v2_5_1-XCN>`
     - O
     -
     - 01581
     - Autopsy Performed By
   * - 9
     - ``pda_9``
     - 1
     - str
     - O
     - 0136
     - 01582
     - Coroner Indicator

.. _hl7-v2_5_1-PDC:

PDC: Product Detail Country
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.12.5

.. py:class:: hl7types.hl7.v2_5_1.segments.PDC.PDC
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
     - ``pdc_1``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - R
     -
     - 01247
     - Manufacturer/Distributor
   * - 2
     - ``pdc_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 01248
     - Country
   * - 3
     - ``pdc_3``
     - 60
     - str
     - R
     -
     - 01249
     - Brand Name
   * - 4
     - ``pdc_4``
     - 60
     - str
     - O
     -
     - 01250
     - Device Family Name
   * - 5
     - ``pdc_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01251
     - Generic Name
   * - 6
     - ``pdc_6``
     - 60
     - list[str]
     - O
     -
     - 01252
     - Model Identifier
   * - 7
     - ``pdc_7``
     - 60
     - str
     - O
     -
     - 01253
     - Catalogue Identifier
   * - 8
     - ``pdc_8``
     - 60
     - list[str]
     - O
     -
     - 01254
     - Other Identifier
   * - 9
     - ``pdc_9``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01255
     - Product Code
   * - 10
     - ``pdc_10``
     - 4
     - str
     - O
     - 0330
     - 01256
     - Marketing Basis
   * - 11
     - ``pdc_11``
     - 60
     - str
     - O
     -
     - 01257
     - Marketing Approval ID
   * - 12
     - ``pdc_12``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01258
     - Labeled Shelf Life
   * - 13
     - ``pdc_13``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01259
     - Expected Shelf Life
   * - 14
     - ``pdc_14``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01260
     - Date First Marketed
   * - 15
     - ``pdc_15``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01261
     - Date Last Marketed

.. _hl7-v2_5_1-PEO:

PEO: Product Experience Observation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.12.2

.. py:class:: hl7types.hl7.v2_5_1.segments.PEO.PEO
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
     - ``peo_1``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01073
     - Event Identifiers Used
   * - 2
     - ``peo_2``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01074
     - Event Symptom/Diagnosis Code
   * - 3
     - ``peo_3``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01075
     - Event Onset Date/Time
   * - 4
     - ``peo_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01076
     - Event Exacerbation Date/Time
   * - 5
     - ``peo_5``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01077
     - Event Improved Date/Time
   * - 6
     - ``peo_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01078
     - Event Ended Data/Time
   * - 7
     - ``peo_7``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 01079
     - Event Location Occurred Address
   * - 8
     - ``peo_8``
     - 1
     - list[str]
     - O
     - 0237
     - 01080
     - Event Qualification
   * - 9
     - ``peo_9``
     - 1
     - str
     - O
     - 0238
     - 01081
     - Event Serious
   * - 10
     - ``peo_10``
     - 1
     - str
     - O
     - 0239
     - 01082
     - Event Expected
   * - 11
     - ``peo_11``
     - 1
     - list[str]
     - O
     - 0240
     - 01083
     - Event Outcome
   * - 12
     - ``peo_12``
     - 1
     - str
     - O
     - 0241
     - 01084
     - Patient Outcome
   * - 13
     - ``peo_13``
     -
     - list[str]
     - O
     -
     - 01085
     - Event Description From Others
   * - 14
     - ``peo_14``
     -
     - list[str]
     - O
     -
     - 01086
     - Event From Original Reporter
   * - 15
     - ``peo_15``
     -
     - list[str]
     - O
     -
     - 01087
     - Event Description From Patient
   * - 16
     - ``peo_16``
     -
     - list[str]
     - O
     -
     - 01088
     - Event Description From Practitioner
   * - 17
     - ``peo_17``
     -
     - list[str]
     - O
     -
     - 01089
     - Event Description From Autopsy
   * - 18
     - ``peo_18``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01090
     - Cause Of Death
   * - 19
     - ``peo_19``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 01091
     - Primary Observer Name
   * - 20
     - ``peo_20``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 01092
     - Primary Observer Address
   * - 21
     - ``peo_21``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 01093
     - Primary Observer Telephone
   * - 22
     - ``peo_22``
     - 1
     - str
     - O
     - 0242
     - 01094
     - Primary Observer's Qualification
   * - 23
     - ``peo_23``
     - 1
     - str
     - O
     - 0242
     - 01095
     - Confirmation Provided By
   * - 24
     - ``peo_24``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01096
     - Primary Observer Aware Date/Time
   * - 25
     - ``peo_25``
     - 1
     - str
     - O
     - 0243
     - 01097
     - Primary Observer's identity May Be Divulged

.. _hl7-v2_5_1-PES:

PES: Product Experience Sender
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.12.1

.. py:class:: hl7types.hl7.v2_5_1.segments.PES.PES
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
     - ``pes_1``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 01059
     - Sender Organization Name
   * - 2
     - ``pes_2``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 01060
     - Sender Individual Name
   * - 3
     - ``pes_3``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 01062
     - Sender Address
   * - 4
     - ``pes_4``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 01063
     - Sender Telephone
   * - 5
     - ``pes_5``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 01064
     - Sender Event Identifier
   * - 6
     - ``pes_6``
     - 2
     - str
     - O
     -
     - 01065
     - Sender Sequence Number
   * - 7
     - ``pes_7``
     -
     - list[str]
     - O
     -
     - 01066
     - Sender Event Description
   * - 8
     - ``pes_8``
     -
     - str
     - O
     -
     - 01067
     - Sender Comment
   * - 9
     - ``pes_9``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01068
     - Sender Aware Date/Time
   * - 10
     - ``pes_10``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01069
     - Event Report Date
   * - 11
     - ``pes_11``
     - 3
     - list[str]
     - O
     - 0234
     - 01070
     - Event Report Timing/Type
   * - 12
     - ``pes_12``
     - 1
     - str
     - O
     - 0235
     - 01071
     - Event Report Source
   * - 13
     - ``pes_13``
     - 1
     - list[str]
     - O
     - 0236
     - 01072
     - Event Reported To

.. _hl7-v2_5_1-PID:

PID: Patient Identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.4.2

.. py:class:: hl7types.hl7.v2_5_1.segments.PID.PID
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
     - Set ID - PID
   * - 2
     - ``pid_2``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 00105
     - Patient ID
   * - 3
     - ``pid_3``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - R
     -
     - 00106
     - Patient Identifier List
   * - 4
     - ``pid_4``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00107
     - Alternate Patient ID - PID
   * - 5
     - ``pid_5``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - R
     -
     - 00108
     - Patient Name
   * - 6
     - ``pid_6``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00109
     - Mother's Maiden Name
   * - 7
     - ``pid_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00110
     - Date/Time of Birth
   * - 8
     - ``pid_8``
     - 1
     - str
     - O
     - 0001
     - 00111
     - Administrative Sex
   * - 9
     - ``pid_9``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 00112
     - Patient Alias
   * - 10
     - ``pid_10``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0005
     - 00113
     - Race
   * - 11
     - ``pid_11``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00114
     - Patient Address
   * - 12
     - ``pid_12``
     - 4
     - str
     - O
     - 0289
     - 00115
     - County Code
   * - 13
     - ``pid_13``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00116
     - Phone Number - Home
   * - 14
     - ``pid_14``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00117
     - Phone Number - Business
   * - 15
     - ``pid_15``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0296
     - 00118
     - Primary Language
   * - 16
     - ``pid_16``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0002
     - 00119
     - Marital Status
   * - 17
     - ``pid_17``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0006
     - 00120
     - Religion
   * - 18
     - ``pid_18``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
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
     - SSN Number - Patient
   * - 20
     - ``pid_20``
     -
     - :ref:`DLN <hl7-v2_5_1-DLN>`
     - O
     -
     - 00123
     - Driver's License Number - Patient
   * - 21
     - ``pid_21``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00124
     - Mother's Identifier
   * - 22
     - ``pid_22``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0189
     - 00125
     - Ethnic Group
   * - 23
     - ``pid_23``
     - 250
     - str
     - O
     -
     - 00126
     - Birth Place
   * - 24
     - ``pid_24``
     - 1
     - str
     - O
     - 0136
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
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0171
     - 00129
     - Citizenship
   * - 27
     - ``pid_27``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0172
     - 00130
     - Veterans Military Status
   * - 28
     - ``pid_28``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0212
     - 00739
     - Nationality
   * - 29
     - ``pid_29``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00740
     - Patient Death Date and Time
   * - 30
     - ``pid_30``
     - 1
     - str
     - O
     - 0136
     - 00741
     - Patient Death Indicator
   * - 31
     - ``pid_31``
     - 1
     - str
     - O
     - 0136
     - 01535
     - Identity Unknown Indicator
   * - 32
     - ``pid_32``
     - 20
     - list[str]
     - O
     - 0445
     - 01536
     - Identity Reliability Code
   * - 33
     - ``pid_33``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01537
     - Last Update Date/Time
   * - 34
     - ``pid_34``
     -
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     -
     - 01538
     - Last Update Facility
   * - 35
     - ``pid_35``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0446
     - 01539
     - Species Code
   * - 36
     - ``pid_36``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0447
     - 01540
     - Breed Code
   * - 37
     - ``pid_37``
     - 80
     - str
     - O
     -
     - 01541
     - Strain
   * - 38
     - ``pid_38``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0429
     - 01542
     - Production Class Code
   * - 39
     - ``pid_39``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0171
     - 01840
     - Tribal Citizenship

.. _hl7-v2_5_1-PR1:

PR1: Procedures
~~~~~~~~~~~~~~~

Section 6.5.4

.. py:class:: hl7types.hl7.v2_5_1.segments.PR1.PR1
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
     - Set ID - PR1
   * - 2
     - ``pr1_2``
     - 3
     - str
     - R
     - 0089
     - 00392
     - Procedure Coding Method
   * - 3
     - ``pr1_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0088
     - 00393
     - Procedure Code
   * - 4
     - ``pr1_4``
     - 40
     - str
     - O
     -
     - 00394
     - Procedure Description
   * - 5
     - ``pr1_5``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 00395
     - Procedure Date/Time
   * - 6
     - ``pr1_6``
     - 2
     - str
     - O
     - 0230
     - 00396
     - Procedure Functional Type
   * - 7
     - ``pr1_7``
     - 4
     - str
     - O
     -
     - 00397
     - Procedure Minutes
   * - 8
     - ``pr1_8``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
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
     - Anesthesia Code
   * - 10
     - ``pr1_10``
     - 4
     - str
     - O
     -
     - 00400
     - Anesthesia Minutes
   * - 11
     - ``pr1_11``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     - 0010
     - 00401
     - Surgeon
   * - 12
     - ``pr1_12``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     - 0010
     - 00402
     - Procedure Practitioner
   * - 13
     - ``pr1_13``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0059
     - 00403
     - Consent Code
   * - 14
     - ``pr1_14``
     - 2
     - str
     - O
     - 0418
     - 00404
     - Procedure Priority
   * - 15
     - ``pr1_15``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0051
     - 00772
     - Associated Diagnosis Code
   * - 16
     - ``pr1_16``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0340
     - 01316
     - Procedure Code Modifier
   * - 17
     - ``pr1_17``
     - 20
     - str
     - O
     - 0416
     - 01501
     - Procedure DRG Type
   * - 18
     - ``pr1_18``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0417
     - 01502
     - Tissue Type Code
   * - 19
     - ``pr1_19``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 01848
     - Procedure Identifier
   * - 20
     - ``pr1_20``
     - 1
     - str
     - C
     - 0206
     - 01849
     - Procedure Action Code

.. _hl7-v2_5_1-PRA:

PRA: Practitioner Detail
~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.4.6

.. py:class:: hl7types.hl7.v2_5_1.segments.PRA.PRA
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
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 9999
     - 00685
     - Primary Key Value - PRA
   * - 2
     - ``pra_2``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0358
     - 00686
     - Practitioner Group
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
     - list[:ref:`SPD <hl7-v2_5_1-SPD>`]
     - O
     - 0337
     - 00689
     - Specialty
   * - 6
     - ``pra_6``
     -
     - list[:ref:`PLN <hl7-v2_5_1-PLN>`]
     - O
     - 0338
     - 00690
     - Practitioner ID Numbers
   * - 7
     - ``pra_7``
     -
     - list[:ref:`PIP <hl7-v2_5_1-PIP>`]
     - O
     -
     - 00691
     - Privileges
   * - 8
     - ``pra_8``
     - 8
     - str
     - O
     -
     - 01296
     - Date Entered Practice
   * - 9
     - ``pra_9``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0537
     - 01613
     - Institution
   * - 10
     - ``pra_10``
     - 8
     - str
     - O
     -
     - 01348
     - Date Left Practice
   * - 11
     - ``pra_11``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0401
     - 01388
     - Government Reimbursement Billing Eligibility
   * - 12
     - ``pra_12``
     - 60
     - str
     - C
     -
     - 01616
     - Set ID - PRA

.. _hl7-v2_5_1-PRB:

PRB: Problem Details
~~~~~~~~~~~~~~~~~~~~

Section 12.4.2

.. py:class:: hl7types.hl7.v2_5_1.segments.PRB.PRB
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
     - ``prb_1``
     - 2
     - str
     - R
     - 0287
     - 00816
     - Action Code
   * - 2
     - ``prb_2``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 00817
     - Action Date/Time
   * - 3
     - ``prb_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00838
     - Problem ID
   * - 4
     - ``prb_4``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 00839
     - Problem Instance ID
   * - 5
     - ``prb_5``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 00820
     - Episode of Care ID
   * - 6
     - ``prb_6``
     - 60
     - str
     - O
     -
     - 00841
     - Problem List Priority
   * - 7
     - ``prb_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00842
     - Problem Established Date/Time
   * - 8
     - ``prb_8``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00843
     - Anticipated Problem Resolution Date/Time
   * - 9
     - ``prb_9``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00844
     - Actual Problem Resolution Date/Time
   * - 10
     - ``prb_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00845
     - Problem Classification
   * - 11
     - ``prb_11``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00846
     - Problem Management Discipline
   * - 12
     - ``prb_12``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00847
     - Problem Persistence
   * - 13
     - ``prb_13``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00848
     - Problem Confirmation Status
   * - 14
     - ``prb_14``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00849
     - Problem Life Cycle Status
   * - 15
     - ``prb_15``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00850
     - Problem Life Cycle Status Date/Time
   * - 16
     - ``prb_16``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00851
     - Problem Date of Onset
   * - 17
     - ``prb_17``
     - 80
     - str
     - O
     -
     - 00852
     - Problem Onset Text
   * - 18
     - ``prb_18``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00853
     - Problem Ranking
   * - 19
     - ``prb_19``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00854
     - Certainty of Problem
   * - 20
     - ``prb_20``
     - 5
     - str
     - O
     -
     - 00855
     - Probability of Problem (0-1)
   * - 21
     - ``prb_21``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00856
     - Individual Awareness of Problem
   * - 22
     - ``prb_22``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00857
     - Problem Prognosis
   * - 23
     - ``prb_23``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00858
     - Individual Awareness of Prognosis
   * - 24
     - ``prb_24``
     - 200
     - str
     - O
     -
     - 00859
     - Family/Significant Other Awareness of Problem/Prognosis
   * - 25
     - ``prb_25``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00823
     - Security/Sensitivity

.. _hl7-v2_5_1-PRC:

PRC: Pricing
~~~~~~~~~~~~

Section 8.10.3

.. py:class:: hl7types.hl7.v2_5_1.segments.PRC.PRC
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
     - ``prc_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0132
     - 00982
     - Primary Key Value - PRC
   * - 2
     - ``prc_2``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0464
     - 00995
     - Facility ID - PRC
   * - 3
     - ``prc_3``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0184
     - 00676
     - Department
   * - 4
     - ``prc_4``
     - 1
     - list[str]
     - O
     - 0004
     - 00967
     - Valid Patient Classes
   * - 5
     - ``prc_5``
     -
     - list[:ref:`CP <hl7-v2_5_1-CP>`]
     - C
     -
     - 00998
     - Price
   * - 6
     - ``prc_6``
     - 200
     - list[str]
     - O
     -
     - 00999
     - Formula
   * - 7
     - ``prc_7``
     - 4
     - str
     - O
     -
     - 01000
     - Minimum Quantity
   * - 8
     - ``prc_8``
     - 4
     - str
     - O
     -
     - 01001
     - Maximum Quantity
   * - 9
     - ``prc_9``
     -
     - :ref:`MO <hl7-v2_5_1-MO>`
     - O
     -
     - 01002
     - Minimum Price
   * - 10
     - ``prc_10``
     -
     - :ref:`MO <hl7-v2_5_1-MO>`
     - O
     -
     - 01003
     - Maximum Price
   * - 11
     - ``prc_11``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01004
     - Effective Start Date
   * - 12
     - ``prc_12``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01005
     - Effective End Date
   * - 13
     - ``prc_13``
     - 1
     - str
     - O
     - 0268
     - 01006
     - Price Override Flag
   * - 14
     - ``prc_14``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0293
     - 01007
     - Billing Category
   * - 15
     - ``prc_15``
     - 1
     - str
     - O
     - 0136
     - 01008
     - Chargeable Flag
   * - 16
     - ``prc_16``
     - 1
     - str
     - O
     - 0183
     - 00675
     - Active/Inactive Flag
   * - 17
     - ``prc_17``
     -
     - :ref:`MO <hl7-v2_5_1-MO>`
     - O
     -
     - 00989
     - Cost
   * - 18
     - ``prc_18``
     - 1
     - str
     - O
     - 0269
     - 01009
     - Charge On Indicator

.. _hl7-v2_5_1-PRD:

PRD: Provider Data
~~~~~~~~~~~~~~~~~~

Section 11.6.3

.. py:class:: hl7types.hl7.v2_5_1.segments.PRD.PRD
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
     - ``prd_1``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - R
     - 0286
     - 01155
     - Provider Role
   * - 2
     - ``prd_2``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
     - O
     -
     - 01156
     - Provider Name
   * - 3
     - ``prd_3``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 01157
     - Provider Address
   * - 4
     - ``prd_4``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 01158
     - Provider Location
   * - 5
     - ``prd_5``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 01159
     - Provider Communication Information
   * - 6
     - ``prd_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0185
     - 00684
     - Preferred Method of Contact
   * - 7
     - ``prd_7``
     -
     - list[:ref:`PLN <hl7-v2_5_1-PLN>`]
     - O
     -
     - 01162
     - Provider Identifiers
   * - 8
     - ``prd_8``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01163
     - Effective Start Date of Provider Role
   * - 9
     - ``prd_9``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01164
     - Effective End Date of Provider Role

.. _hl7-v2_5_1-PSH:

PSH: Product Summary Header
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.12.4

.. py:class:: hl7types.hl7.v2_5_1.segments.PSH.PSH
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
     - ``psh_1``
     - 60
     - str
     - R
     -
     - 01233
     - Report Type
   * - 2
     - ``psh_2``
     - 60
     - str
     - O
     -
     - 01297
     - Report Form Identifier
   * - 3
     - ``psh_3``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01235
     - Report Date
   * - 4
     - ``psh_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01236
     - Report Interval Start Date
   * - 5
     - ``psh_5``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01237
     - Report Interval End Date
   * - 6
     - ``psh_6``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01238
     - Quantity Manufactured
   * - 7
     - ``psh_7``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01239
     - Quantity Distributed
   * - 8
     - ``psh_8``
     - 1
     - str
     - O
     - 0329
     - 01240
     - Quantity Distributed Method
   * - 9
     - ``psh_9``
     -
     - str
     - O
     -
     - 01241
     - Quantity Distributed Comment
   * - 10
     - ``psh_10``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01242
     - Quantity in Use
   * - 11
     - ``psh_11``
     - 1
     - str
     - O
     - 0329
     - 01243
     - Quantity in Use Method
   * - 12
     - ``psh_12``
     -
     - str
     - O
     -
     - 01244
     - Quantity in Use Comment
   * - 13
     - ``psh_13``
     - 2
     - list[str]
     - O
     -
     - 01245
     - Number of Product Experience Reports Filed by Facility
   * - 14
     - ``psh_14``
     - 2
     - list[str]
     - O
     -
     - 01246
     - Number of Product Experience Reports Filed by Distributor

.. _hl7-v2_5_1-PTH:

PTH: Pathway
~~~~~~~~~~~~

Section 12.4.4

.. py:class:: hl7types.hl7.v2_5_1.segments.PTH.PTH
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
     - ``pth_1``
     - 2
     - str
     - R
     - 0287
     - 00816
     - Action Code
   * - 2
     - ``pth_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 01207
     - Pathway ID
   * - 3
     - ``pth_3``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01208
     - Pathway Instance ID
   * - 4
     - ``pth_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01209
     - Pathway Established Date/Time
   * - 5
     - ``pth_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01210
     - Pathway Life Cycle Status
   * - 6
     - ``pth_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 01211
     - Change Pathway Life Cycle Status Date/Time

.. _hl7-v2_5_1-PV1:

PV1: Patient Visit
~~~~~~~~~~~~~~~~~~

Section 3.4.3

.. py:class:: hl7types.hl7.v2_5_1.segments.PV1.PV1
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
     - Set ID - PV1
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
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
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
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 00135
     - Preadmit Number
   * - 6
     - ``pv1_6``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 00136
     - Prior Patient Location
   * - 7
     - ``pv1_7``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     - 0010
     - 00137
     - Attending Doctor
   * - 8
     - ``pv1_8``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     - 0010
     - 00138
     - Referring Doctor
   * - 9
     - ``pv1_9``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
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
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
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
     - Re-admission Indicator
   * - 14
     - ``pv1_14``
     - 6
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
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
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
     - Patient Type
   * - 19
     - ``pv1_19``
     -
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     -
     - 00149
     - Visit Number
   * - 20
     - ``pv1_20``
     -
     - list[:ref:`FC <hl7-v2_5_1-FC>`]
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
     - 4
     - str
     - O
     - 0110
     - 00159
     - Transfer to Bad Debt Code
   * - 30
     - ``pv1_30``
     - 8
     - str
     - O
     -
     - 00160
     - Transfer to Bad Debt Date
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
     - :ref:`DLD <hl7-v2_5_1-DLD>`
     - O
     - 0113
     - 00167
     - Discharged to Location
   * - 38
     - ``pv1_38``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0114
     - 00168
     - Diet Type
   * - 39
     - ``pv1_39``
     - 2
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
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 00172
     - Pending Location
   * - 43
     - ``pv1_43``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 00173
     - Prior Temporary Location
   * - 44
     - ``pv1_44``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00174
     - Admit Date/Time
   * - 45
     - ``pv1_45``
     -
     - list[:ref:`TS <hl7-v2_5_1-TS>`]
     - O
     -
     - 00175
     - Discharge Date/Time
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
     - :ref:`CX <hl7-v2_5_1-CX>`
     - O
     - 0203
     - 00180
     - Alternate Visit ID
   * - 51
     - ``pv1_51``
     - 1
     - str
     - O
     - 0326
     - 01226
     - Visit Indicator
   * - 52
     - ``pv1_52``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     - 0010
     - 01274
     - Other Healthcare Provider

.. _hl7-v2_5_1-PV2:

PV2: Patient Visit - Additional Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.4.4

.. py:class:: hl7types.hl7.v2_5_1.segments.PV2.PV2
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
     - :ref:`PL <hl7-v2_5_1-PL>`
     - C
     -
     - 00181
     - Prior Pending Location
   * - 2
     - ``pv2_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0129
     - 00182
     - Accommodation Code
   * - 3
     - ``pv2_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00183
     - Admit Reason
   * - 4
     - ``pv2_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
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
     - list[str]
     - O
     - 0130
     - 00187
     - Visit User Code
   * - 8
     - ``pv2_8``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00188
     - Expected Admit Date/Time
   * - 9
     - ``pv2_9``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00189
     - Expected Discharge Date/Time
   * - 10
     - ``pv2_10``
     - 3
     - str
     - O
     -
     - 00711
     - Estimated Length of Inpatient Stay
   * - 11
     - ``pv2_11``
     - 3
     - str
     - O
     -
     - 00712
     - Actual Length of Inpatient Stay
   * - 12
     - ``pv2_12``
     - 50
     - str
     - O
     -
     - 00713
     - Visit Description
   * - 13
     - ``pv2_13``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00714
     - Referral Source Code
   * - 14
     - ``pv2_14``
     - 8
     - str
     - O
     -
     - 00715
     - Previous Service Date
   * - 15
     - ``pv2_15``
     - 1
     - str
     - O
     - 0136
     - 00716
     - Employment Illness Related Indicator
   * - 16
     - ``pv2_16``
     - 1
     - str
     - O
     - 0213
     - 00717
     - Purge Status Code
   * - 17
     - ``pv2_17``
     - 8
     - str
     - O
     -
     - 00718
     - Purge Status Date
   * - 18
     - ``pv2_18``
     - 2
     - str
     - O
     - 0214
     - 00719
     - Special Program Code
   * - 19
     - ``pv2_19``
     - 1
     - str
     - O
     - 0136
     - 00720
     - Retention Indicator
   * - 20
     - ``pv2_20``
     - 1
     - str
     - O
     -
     - 00721
     - Expected Number of Insurance Plans
   * - 21
     - ``pv2_21``
     - 1
     - str
     - O
     - 0215
     - 00722
     - Visit Publicity Code
   * - 22
     - ``pv2_22``
     - 1
     - str
     - O
     - 0136
     - 00723
     - Visit Protection Indicator
   * - 23
     - ``pv2_23``
     -
     - list[:ref:`XON <hl7-v2_5_1-XON>`]
     - O
     -
     - 00724
     - Clinic Organization Name
   * - 24
     - ``pv2_24``
     - 2
     - str
     - O
     - 0216
     - 00725
     - Patient Status Code
   * - 25
     - ``pv2_25``
     - 1
     - str
     - O
     - 0217
     - 00726
     - Visit Priority Code
   * - 26
     - ``pv2_26``
     - 8
     - str
     - O
     -
     - 00727
     - Previous Treatment Date
   * - 27
     - ``pv2_27``
     - 2
     - str
     - O
     - 0112
     - 00728
     - Expected Discharge Disposition
   * - 28
     - ``pv2_28``
     - 8
     - str
     - O
     -
     - 00729
     - Signature on File Date
   * - 29
     - ``pv2_29``
     - 8
     - str
     - O
     -
     - 00730
     - First Similar Illness Date
   * - 30
     - ``pv2_30``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0218
     - 00731
     - Patient Charge Adjustment Code
   * - 31
     - ``pv2_31``
     - 2
     - str
     - O
     - 0219
     - 00732
     - Recurring Service Code
   * - 32
     - ``pv2_32``
     - 1
     - str
     - O
     - 0136
     - 00733
     - Billing Media Code
   * - 33
     - ``pv2_33``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00734
     - Expected Surgery Date and Time
   * - 34
     - ``pv2_34``
     - 1
     - str
     - O
     - 0136
     - 00735
     - Military Partnership Code
   * - 35
     - ``pv2_35``
     - 1
     - str
     - O
     - 0136
     - 00736
     - Military Non-Availability Code
   * - 36
     - ``pv2_36``
     - 1
     - str
     - O
     - 0136
     - 00737
     - Newborn Baby Indicator
   * - 37
     - ``pv2_37``
     - 1
     - str
     - O
     - 0136
     - 00738
     - Baby Detained Indicator
   * - 38
     - ``pv2_38``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0430
     - 01543
     - Mode of Arrival Code
   * - 39
     - ``pv2_39``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0431
     - 01544
     - Recreational Drug Use Code
   * - 40
     - ``pv2_40``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0432
     - 01545
     - Admission Level of Care Code
   * - 41
     - ``pv2_41``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0433
     - 01546
     - Precaution Code
   * - 42
     - ``pv2_42``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0434
     - 01547
     - Patient Condition Code
   * - 43
     - ``pv2_43``
     - 2
     - str
     - O
     - 0315
     - 00759
     - Living Will Code
   * - 44
     - ``pv2_44``
     - 2
     - str
     - O
     - 0316
     - 00760
     - Organ Donor Code
   * - 45
     - ``pv2_45``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0435
     - 01548
     - Advance Directive Code
   * - 46
     - ``pv2_46``
     - 8
     - str
     - O
     -
     - 01549
     - Patient Status Effective Date
   * - 47
     - ``pv2_47``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 01550
     - Expected LOA Return Date/Time
   * - 48
     - ``pv2_48``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01841
     - Expected Pre-admission Testing Date/Time
   * - 49
     - ``pv2_49``
     - 20
     - list[str]
     - O
     - 0534
     - 01842
     - Notify Clergy Code

.. _hl7-v2_5_1-QAK:

QAK: Query Acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.5.2

.. py:class:: hl7types.hl7.v2_5_1.segments.QAK.QAK
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
     - ``qak_1``
     - 32
     - str
     - C
     -
     - 00696
     - Query Tag
   * - 2
     - ``qak_2``
     - 2
     - str
     - O
     - 0208
     - 00708
     - Query Response Status
   * - 3
     - ``qak_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0471
     - 01375
     - Message Query Name
   * - 4
     - ``qak_4``
     - 10
     - str
     - O
     -
     - 01434
     - Hit Count
   * - 5
     - ``qak_5``
     - 10
     - str
     - O
     -
     - 01622
     - This payload
   * - 6
     - ``qak_6``
     - 10
     - str
     - O
     -
     - 01623
     - Hits remaining

.. _hl7-v2_5_1-QID:

QID: Query Identification
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.5.3

.. py:class:: hl7types.hl7.v2_5_1.segments.QID.QID
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
     - ``qid_1``
     - 32
     - str
     - R
     -
     - 00696
     - Query Tag
   * - 2
     - ``qid_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0471
     - 01375
     - Message Query Name

.. _hl7-v2_5_1-QPD:

QPD: Query Parameter Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.5.4

.. py:class:: hl7types.hl7.v2_5_1.segments.QPD.QPD
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
     - ``qpd_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0471
     - 01375
     - Message Query Name
   * - 2
     - ``qpd_2``
     - 32
     - str
     - C
     -
     - 00696
     - Query Tag
   * - 3
     - ``qpd_3``
     -
     - str
     - O
     -
     - 01435
     - User Parameters (in successive fields)

.. _hl7-v2_5_1-QRD:

QRD: Original-Style Query Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.10.5.3

.. py:class:: hl7types.hl7.v2_5_1.segments.QRD.QRD
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
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 00025
     - Query Date/Time
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
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00030
     - Deferred Response Date/Time
   * - 7
     - ``qrd_7``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - R
     - 0126
     - 00031
     - Quantity Limited Request
   * - 8
     - ``qrd_8``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - R
     -
     - 00032
     - Who Subject Filter
   * - 9
     - ``qrd_9``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - R
     - 0048
     - 00033
     - What Subject Filter
   * - 10
     - ``qrd_10``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - R
     -
     - 00034
     - What Department Data Code
   * - 11
     - ``qrd_11``
     -
     - list[:ref:`VR <hl7-v2_5_1-VR>`]
     - O
     -
     - 00035
     - What Data Code Value Qual.
   * - 12
     - ``qrd_12``
     - 1
     - str
     - O
     - 0108
     - 00036
     - Query Results Level

.. _hl7-v2_5_1-QRF:

QRF: Original style query filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.10.5.4

.. py:class:: hl7types.hl7.v2_5_1.segments.QRF.QRF
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
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00038
     - When Data Start Date/Time
   * - 3
     - ``qrf_3``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00039
     - When Data End Date/Time
   * - 4
     - ``qrf_4``
     - 60
     - list[str]
     - O
     -
     - 00040
     - What User Qualifier
   * - 5
     - ``qrf_5``
     - 60
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
     - Which Date/Time Qualifier
   * - 7
     - ``qrf_7``
     - 12
     - list[str]
     - O
     - 0157
     - 00043
     - Which Date/Time Status Qualifier
   * - 8
     - ``qrf_8``
     - 12
     - list[str]
     - O
     - 0158
     - 00044
     - Date/Time Selection Qualifier
   * - 9
     - ``qrf_9``
     -
     - :ref:`TQ <hl7-v2_5_1-TQ>`
     - O
     -
     - 00694
     - When Quantity/Timing Qualifier
   * - 10
     - ``qrf_10``
     - 10
     - str
     - O
     -
     - 01442
     - Search Confidence Threshold

.. _hl7-v2_5_1-QRI:

QRI: Query Response Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.5.5

.. py:class:: hl7types.hl7.v2_5_1.segments.QRI.QRI
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
     - ``qri_1``
     - 10
     - str
     - O
     -
     - 01436
     - Candidate Confidence
   * - 2
     - ``qri_2``
     - 2
     - list[str]
     - O
     - 0392
     - 01437
     - Match Reason Code
   * - 3
     - ``qri_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0393
     - 01438
     - Algorithm Descriptor

.. _hl7-v2_5_1-RCP:

RCP: Response Control Parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.5.6

.. py:class:: hl7types.hl7.v2_5_1.segments.RCP.RCP
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
     - ``rcp_1``
     - 1
     - str
     - O
     - 0091
     - 00027
     - Query Priority
   * - 2
     - ``rcp_2``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     - 0126
     - 00031
     - Quantity Limited Request
   * - 3
     - ``rcp_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0394
     - 01440
     - Response Modality
   * - 4
     - ``rcp_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 01441
     - Execution and Delivery Time
   * - 5
     - ``rcp_5``
     - 1
     - str
     - O
     - 0395
     - 01443
     - Modify Indicator
   * - 6
     - ``rcp_6``
     -
     - list[:ref:`SRT <hl7-v2_5_1-SRT>`]
     - O
     -
     - 01624
     - Sort-by Field
   * - 7
     - ``rcp_7``
     - 256
     - list[str]
     - O
     -
     - 01594
     - Segment group inclusion

.. _hl7-v2_5_1-RDF:

RDF: Table Row Definition
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.5.7

.. py:class:: hl7types.hl7.v2_5_1.segments.RDF.RDF
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
     - ``rdf_1``
     - 3
     - str
     - R
     -
     - 00701
     - Number of Columns per Row
   * - 2
     - ``rdf_2``
     -
     - list[:ref:`RCD <hl7-v2_5_1-RCD>`]
     - R
     - 0440
     - 00702
     - Column Description

.. _hl7-v2_5_1-RDT:

RDT: Table Row Data
~~~~~~~~~~~~~~~~~~~

Section 5.5.8

.. py:class:: hl7types.hl7.v2_5_1.segments.RDT.RDT
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
     - ``rdt_1``
     -
     - str
     - R
     -
     - 00703
     - Column Value

.. _hl7-v2_5_1-RF1:

RF1: Referral Information
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.6.1

.. py:class:: hl7types.hl7.v2_5_1.segments.RF1.RF1
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
     - ``rf1_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0283
     - 01137
     - Referral Status
   * - 2
     - ``rf1_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0280
     - 01138
     - Referral Priority
   * - 3
     - ``rf1_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0281
     - 01139
     - Referral Type
   * - 4
     - ``rf1_4``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0282
     - 01140
     - Referral Disposition
   * - 5
     - ``rf1_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0284
     - 01141
     - Referral Category
   * - 6
     - ``rf1_6``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01142
     - Originating Referral Identifier
   * - 7
     - ``rf1_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01143
     - Effective Date
   * - 8
     - ``rf1_8``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01144
     - Expiration Date
   * - 9
     - ``rf1_9``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01145
     - Process Date
   * - 10
     - ``rf1_10``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0336
     - 01228
     - Referral Reason
   * - 11
     - ``rf1_11``
     -
     - list[:ref:`EI <hl7-v2_5_1-EI>`]
     - O
     -
     - 01300
     - External Referral Identifier

.. _hl7-v2_5_1-RGS:

RGS: Resource Group
~~~~~~~~~~~~~~~~~~~

Section 10.6.3

.. py:class:: hl7types.hl7.v2_5_1.segments.RGS.RGS
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
     - ``rgs_1``
     - 4
     - str
     - R
     -
     - 01203
     - Set ID - RGS
   * - 2
     - ``rgs_2``
     - 3
     - str
     - C
     - 0206
     - 00763
     - Segment Action Code
   * - 3
     - ``rgs_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01204
     - Resource Group ID

.. _hl7-v2_5_1-RMI:

RMI: Risk Management Incident
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.5.14

.. py:class:: hl7types.hl7.v2_5_1.segments.RMI.RMI
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
     - ``rmi_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0427
     - 01530
     - Risk Management Incident Code
   * - 2
     - ``rmi_2``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01531
     - Date/Time Incident
   * - 3
     - ``rmi_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0428
     - 01533
     - Incident Type Code

.. _hl7-v2_5_1-ROL:

ROL: Role
~~~~~~~~~

Section 15.4.7

.. py:class:: hl7types.hl7.v2_5_1.segments.ROL.ROL
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
     - ``rol_1``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 01206
     - Role Instance ID
   * - 2
     - ``rol_2``
     - 2
     - str
     - R
     - 0287
     - 00816
     - Action Code
   * - 3
     - ``rol_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0443
     - 01197
     - Role-ROL
   * - 4
     - ``rol_4``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - R
     -
     - 01198
     - Role Person
   * - 5
     - ``rol_5``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01199
     - Role Begin Date/Time
   * - 6
     - ``rol_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01200
     - Role End Date/Time
   * - 7
     - ``rol_7``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01201
     - Role Duration
   * - 8
     - ``rol_8``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01205
     - Role Action Reason
   * - 9
     - ``rol_9``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01510
     - Provider Type
   * - 10
     - ``rol_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0406
     - 01461
     - Organization Unit Type
   * - 11
     - ``rol_11``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00679
     - Office/Home Address/Birthplace
   * - 12
     - ``rol_12``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00678
     - Phone

.. _hl7-v2_5_1-RQ1:

RQ1: Requisition Detail-1
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.11.2

.. py:class:: hl7types.hl7.v2_5_1.segments.RQ1.RQ1
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0385
     - 00286
     - Manufacturer Identifier
   * - 3
     - ``rq1_3``
     - 16
     - str
     - C
     -
     - 00287
     - Manufacturer's Catalog
   * - 4
     - ``rq1_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00288
     - Vendor ID
   * - 5
     - ``rq1_5``
     - 16
     - str
     - C
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

.. _hl7-v2_5_1-RQD:

RQD: Requisition Detail
~~~~~~~~~~~~~~~~~~~~~~~

Section 4.11.1

.. py:class:: hl7types.hl7.v2_5_1.segments.RQD.RQD
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00276
     - Item Code - Internal
   * - 3
     - ``rqd_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00277
     - Item Code - External
   * - 4
     - ``rqd_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00280
     - Requisition Unit of Measure
   * - 7
     - ``rqd_7``
     - 30
     - str
     - O
     - 0319
     - 00281
     - Dept. Cost Center
   * - 8
     - ``rqd_8``
     - 30
     - str
     - O
     - 0320
     - 00282
     - Item Natural Account Code
   * - 9
     - ``rqd_9``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00283
     - Deliver To ID
   * - 10
     - ``rqd_10``
     - 8
     - str
     - O
     -
     - 00284
     - Date Needed

.. _hl7-v2_5_1-RXA:

RXA: Pharmacy/Treatment Administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.14.7

.. py:class:: hl7types.hl7.v2_5_1.segments.RXA.RXA
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
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 00345
     - Date/Time Start of Administration
   * - 4
     - ``rxa_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 00346
     - Date/Time End of Administration
   * - 5
     - ``rxa_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0292
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00349
     - Administered Units
   * - 8
     - ``rxa_8``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00350
     - Administered Dosage Form
   * - 9
     - ``rxa_9``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00351
     - Administration Notes
   * - 10
     - ``rxa_10``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00352
     - Administering Provider
   * - 11
     - ``rxa_11``
     -
     - :ref:`LA2 <hl7-v2_5_1-LA2>`
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
   * - 13
     - ``rxa_13``
     - 20
     - str
     - O
     -
     - 01134
     - Administered Strength
   * - 14
     - ``rxa_14``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01135
     - Administered Strength Units
   * - 15
     - ``rxa_15``
     - 20
     - list[str]
     - O
     -
     - 01129
     - Substance Lot Number
   * - 16
     - ``rxa_16``
     -
     - list[:ref:`TS <hl7-v2_5_1-TS>`]
     - O
     -
     - 01130
     - Substance Expiration Date
   * - 17
     - ``rxa_17``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0227
     - 01131
     - Substance Manufacturer Name
   * - 18
     - ``rxa_18``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01136
     - Substance/Treatment Refusal Reason
   * - 19
     - ``rxa_19``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01123
     - Indication
   * - 20
     - ``rxa_20``
     - 2
     - str
     - O
     - 0322
     - 01223
     - Completion Status
   * - 21
     - ``rxa_21``
     - 2
     - str
     - O
     - 0323
     - 01224
     - Action Code - RXA
   * - 22
     - ``rxa_22``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01225
     - System Entry Date/Time
   * - 23
     - ``rxa_23``
     - 5
     - str
     - O
     -
     - 01696
     - Administered Drug Strength Volume
   * - 24
     - ``rxa_24``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01697
     - Administered Drug Strength Volume Units
   * - 25
     - ``rxa_25``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01698
     - Administered Barcode Identifier
   * - 26
     - ``rxa_26``
     - 1
     - str
     - O
     - 0480
     - 01699
     - Pharmacy Order Type

.. _hl7-v2_5_1-RXC:

RXC: Pharmacy/Treatment Component Order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.14.3

.. py:class:: hl7types.hl7.v2_5_1.segments.RXC.RXC
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
     - :ref:`CE <hl7-v2_5_1-CE>`
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00316
     - Component Units
   * - 5
     - ``rxc_5``
     - 20
     - str
     - O
     -
     - 01124
     - Component Strength
   * - 6
     - ``rxc_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01125
     - Component Strength Units
   * - 7
     - ``rxc_7``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01476
     - Supplementary Code
   * - 8
     - ``rxc_8``
     - 5
     - str
     - O
     -
     - 01671
     - Component Drug Strength Volume
   * - 9
     - ``rxc_9``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01672
     - Component Drug Strength Volume Units

.. _hl7-v2_5_1-RXD:

RXD: Pharmacy/Treatment Dispense
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.14.5

.. py:class:: hl7types.hl7.v2_5_1.segments.RXD.RXD
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
     - R
     -
     - 00334
     - Dispense Sub-ID Counter
   * - 2
     - ``rxd_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0292
     - 00335
     - Dispense/Give Code
   * - 3
     - ``rxd_3``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 00336
     - Date/Time Dispensed
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00338
     - Actual Dispense Units
   * - 6
     - ``rxd_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
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
     - O
     -
     - 00340
     - Dispense Notes
   * - 10
     - ``rxd_10``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
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
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 00329
     - Total Daily Dose
   * - 13
     - ``rxd_13``
     -
     - :ref:`LA2 <hl7-v2_5_1-LA2>`
     - C
     -
     - 01303
     - Dispense-to Location
   * - 14
     - ``rxd_14``
     - 1
     - str
     - O
     - 0136
     - 00307
     - Needs Human Review
   * - 15
     - ``rxd_15``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00330
     - Pharmacy/Treatment Supplier's Special Dispensing Instructions
   * - 16
     - ``rxd_16``
     - 20
     - str
     - O
     -
     - 01132
     - Actual Strength
   * - 17
     - ``rxd_17``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01133
     - Actual Strength Unit
   * - 18
     - ``rxd_18``
     - 20
     - list[str]
     - O
     -
     - 01129
     - Substance Lot Number
   * - 19
     - ``rxd_19``
     -
     - list[:ref:`TS <hl7-v2_5_1-TS>`]
     - O
     -
     - 01130
     - Substance Expiration Date
   * - 20
     - ``rxd_20``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0227
     - 01131
     - Substance Manufacturer Name
   * - 21
     - ``rxd_21``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01123
     - Indication
   * - 22
     - ``rxd_22``
     - 20
     - str
     - O
     -
     - 01220
     - Dispense Package Size
   * - 23
     - ``rxd_23``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01221
     - Dispense Package Size Unit
   * - 24
     - ``rxd_24``
     - 2
     - str
     - O
     - 0321
     - 01222
     - Dispense Package Method
   * - 25
     - ``rxd_25``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01476
     - Supplementary Code
   * - 26
     - ``rxd_26``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01477
     - Initiating Location
   * - 27
     - ``rxd_27``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01478
     - Packaging/Assembly Location
   * - 28
     - ``rxd_28``
     - 5
     - str
     - O
     -
     - 01686
     - Actual Drug Strength Volume
   * - 29
     - ``rxd_29``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01687
     - Actual Drug Strength Volume Units
   * - 30
     - ``rxd_30``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01688
     - Dispense to Pharmacy
   * - 31
     - ``rxd_31``
     -
     - :ref:`XAD <hl7-v2_5_1-XAD>`
     - O
     -
     - 01689
     - Dispense to Pharmacy Address
   * - 32
     - ``rxd_32``
     - 1
     - str
     - O
     - 0480
     - 01690
     - Pharmacy Order Type
   * - 33
     - ``rxd_33``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0484
     - 01691
     - Dispense Type

.. _hl7-v2_5_1-RXE:

RXE: Pharmacy/Treatment Encoded Order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.14.4

.. py:class:: hl7types.hl7.v2_5_1.segments.RXE.RXE
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
     - :ref:`TQ <hl7-v2_5_1-TQ>`
     - O
     -
     - 00221
     - Quantity/Timing
   * - 2
     - ``rxe_2``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0292
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00320
     - Give Units
   * - 6
     - ``rxe_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00321
     - Give Dosage Form
   * - 7
     - ``rxe_7``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00298
     - Provider's Administration Instructions
   * - 8
     - ``rxe_8``
     -
     - :ref:`LA1 <hl7-v2_5_1-LA1>`
     - O
     -
     - 00299
     - Deliver-To Location
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
     - :ref:`CE <hl7-v2_5_1-CE>`
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
     - Number Of Refills
   * - 13
     - ``rxe_13``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - C
     -
     - 00305
     - Ordering Provider's DEA Number
   * - 14
     - ``rxe_14``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00306
     - Pharmacist/Treatment Supplier's Verifier ID
   * - 15
     - ``rxe_15``
     - 20
     - str
     - C
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
     - Number of Refills/Doses Dispensed
   * - 18
     - ``rxe_18``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 00328
     - D/T of Most Recent Refill or Dose Dispensed
   * - 19
     - ``rxe_19``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - C
     -
     - 00329
     - Total Daily Dose
   * - 20
     - ``rxe_20``
     - 1
     - str
     - O
     - 0136
     - 00307
     - Needs Human Review
   * - 21
     - ``rxe_21``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00330
     - Pharmacy/Treatment Supplier's Special Dispensing Instructions
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
     - 6
     - str
     - O
     -
     - 00332
     - Give Rate Amount
   * - 24
     - ``rxe_24``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00333
     - Give Rate Units
   * - 25
     - ``rxe_25``
     - 20
     - str
     - O
     -
     - 01126
     - Give Strength
   * - 26
     - ``rxe_26``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01127
     - Give Strength Units
   * - 27
     - ``rxe_27``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01128
     - Give Indication
   * - 28
     - ``rxe_28``
     - 20
     - str
     - O
     -
     - 01220
     - Dispense Package Size
   * - 29
     - ``rxe_29``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01221
     - Dispense Package Size Unit
   * - 30
     - ``rxe_30``
     - 2
     - str
     - O
     - 0321
     - 01222
     - Dispense Package Method
   * - 31
     - ``rxe_31``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01476
     - Supplementary Code
   * - 32
     - ``rxe_32``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01673
     - Original Order Date/Time
   * - 33
     - ``rxe_33``
     - 5
     - str
     - O
     -
     - 01674
     - Give Drug Strength Volume
   * - 34
     - ``rxe_34``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01675
     - Give Drug Strength Volume Units
   * - 35
     - ``rxe_35``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0477
     - 01676
     - Controlled Substance Schedule
   * - 36
     - ``rxe_36``
     - 1
     - str
     - O
     - 0478
     - 01677
     - Formulary Status
   * - 37
     - ``rxe_37``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     -
     - 01678
     - Pharmaceutical Substance Alternative
   * - 38
     - ``rxe_38``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01679
     - Pharmacy of Most Recent Fill
   * - 39
     - ``rxe_39``
     - 250
     - str
     - O
     -
     - 01680
     - Initial Dispense Amount
   * - 40
     - ``rxe_40``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01681
     - Dispensing Pharmacy
   * - 41
     - ``rxe_41``
     -
     - :ref:`XAD <hl7-v2_5_1-XAD>`
     - O
     -
     - 01682
     - Dispensing Pharmacy Address
   * - 42
     - ``rxe_42``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 01683
     - Deliver-to Patient Location
   * - 43
     - ``rxe_43``
     -
     - :ref:`XAD <hl7-v2_5_1-XAD>`
     - O
     -
     - 01684
     - Deliver-to Address
   * - 44
     - ``rxe_44``
     - 1
     - str
     - O
     - 0480
     - 01685
     - Pharmacy Order Type

.. _hl7-v2_5_1-RXG:

RXG: Pharmacy/Treatment Give
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.14.6

.. py:class:: hl7types.hl7.v2_5_1.segments.RXG.RXG
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
     - :ref:`TQ <hl7-v2_5_1-TQ>`
     - O
     -
     - 00221
     - Quantity/Timing
   * - 4
     - ``rxg_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0292
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00320
     - Give Units
   * - 8
     - ``rxg_8``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00321
     - Give Dosage Form
   * - 9
     - ``rxg_9``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
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
     - :ref:`LA2 <hl7-v2_5_1-LA2>`
     - O
     -
     - 01303
     - Dispense-to Location
   * - 12
     - ``rxg_12``
     - 1
     - str
     - O
     - 0136
     - 00307
     - Needs Human Review
   * - 13
     - ``rxg_13``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00343
     - Pharmacy/Treatment Supplier's Special Administration Instructions
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
     - 6
     - str
     - O
     -
     - 00332
     - Give Rate Amount
   * - 16
     - ``rxg_16``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00333
     - Give Rate Units
   * - 17
     - ``rxg_17``
     - 20
     - str
     - O
     -
     - 01126
     - Give Strength
   * - 18
     - ``rxg_18``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01127
     - Give Strength Units
   * - 19
     - ``rxg_19``
     - 20
     - list[str]
     - O
     -
     - 01129
     - Substance Lot Number
   * - 20
     - ``rxg_20``
     -
     - list[:ref:`TS <hl7-v2_5_1-TS>`]
     - O
     -
     - 01130
     - Substance Expiration Date
   * - 21
     - ``rxg_21``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0227
     - 01131
     - Substance Manufacturer Name
   * - 22
     - ``rxg_22``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01123
     - Indication
   * - 23
     - ``rxg_23``
     - 5
     - str
     - O
     -
     - 01692
     - Give Drug Strength Volume
   * - 24
     - ``rxg_24``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01693
     - Give Drug Strength Volume Units
   * - 25
     - ``rxg_25``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01694
     - Give Barcode Identifier
   * - 26
     - ``rxg_26``
     - 1
     - str
     - O
     - 0480
     - 01695
     - Pharmacy Order Type

.. _hl7-v2_5_1-RXO:

RXO: Pharmacy/Treatment Order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.14.1

.. py:class:: hl7types.hl7.v2_5_1.segments.RXO.RXO
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00292
     - Requested Give Code
   * - 2
     - ``rxo_2``
     - 20
     - str
     - C
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00295
     - Requested Give Units
   * - 5
     - ``rxo_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 00296
     - Requested Dosage Form
   * - 6
     - ``rxo_6``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00297
     - Provider's Pharmacy/Treatment Instructions
   * - 7
     - ``rxo_7``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 00298
     - Provider's Administration Instructions
   * - 8
     - ``rxo_8``
     -
     - :ref:`LA1 <hl7-v2_5_1-LA1>`
     - O
     -
     - 00299
     - Deliver-To Location
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00301
     - Requested Dispense Code
   * - 11
     - ``rxo_11``
     - 20
     - str
     - O
     -
     - 00302
     - Requested Dispense Amount
   * - 12
     - ``rxo_12``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
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
     - Number Of Refills
   * - 14
     - ``rxo_14``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - C
     -
     - 00305
     - Ordering Provider's DEA Number
   * - 15
     - ``rxo_15``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - C
     -
     - 00306
     - Pharmacist/Treatment Supplier's Verifier ID
   * - 16
     - ``rxo_16``
     - 1
     - str
     - O
     - 0136
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
   * - 18
     - ``rxo_18``
     - 20
     - str
     - O
     -
     - 01121
     - Requested Give Strength
   * - 19
     - ``rxo_19``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01122
     - Requested Give Strength Units
   * - 20
     - ``rxo_20``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01123
     - Indication
   * - 21
     - ``rxo_21``
     - 6
     - str
     - O
     -
     - 01218
     - Requested Give Rate Amount
   * - 22
     - ``rxo_22``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01219
     - Requested Give Rate Units
   * - 23
     - ``rxo_23``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 00329
     - Total Daily Dose
   * - 24
     - ``rxo_24``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01476
     - Supplementary Code
   * - 25
     - ``rxo_25``
     - 5
     - str
     - O
     -
     - 01666
     - Requested Drug Strength Volume
   * - 26
     - ``rxo_26``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01667
     - Requested Drug Strength Volume Units
   * - 27
     - ``rxo_27``
     - 1
     - str
     - O
     - 0480
     - 01668
     - Pharmacy Order Type
   * - 28
     - ``rxo_28``
     - 20
     - str
     - O
     -
     - 01669
     - Dispensing Interval

.. _hl7-v2_5_1-RXR:

RXR: Pharmacy/Treatment Route
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.14.2

.. py:class:: hl7types.hl7.v2_5_1.segments.RXR.RXR
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     - 0162
     - 00309
     - Route
   * - 2
     - ``rxr_2``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0163
     - 00310
     - Administration Site
   * - 3
     - ``rxr_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0164
     - 00311
     - Administration Device
   * - 4
     - ``rxr_4``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0165
     - 00312
     - Administration Method
   * - 5
     - ``rxr_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01315
     - Routing Instruction
   * - 6
     - ``rxr_6``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0495
     - 01670
     - Administration Site Modifier

.. _hl7-v2_5_1-SAC:

SAC: Specimen Container detail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.4.3

.. py:class:: hl7types.hl7.v2_5_1.segments.SAC.SAC
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
     - ``sac_1``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 01329
     - External Accession Identifier
   * - 2
     - ``sac_2``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 01330
     - Accession Identifier
   * - 3
     - ``sac_3``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 01331
     - Container Identifier
   * - 4
     - ``sac_4``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 01332
     - Primary (parent) Container Identifier
   * - 5
     - ``sac_5``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 01333
     - Equipment Container Identifier
   * - 6
     - ``sac_6``
     -
     - :ref:`SPS <hl7-v2_5_1-SPS>`
     - C
     -
     - 00249
     - Specimen Source
   * - 7
     - ``sac_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01334
     - Registration Date/Time
   * - 8
     - ``sac_8``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0370
     - 01335
     - Container Status
   * - 9
     - ``sac_9``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0378
     - 01336
     - Carrier Type
   * - 10
     - ``sac_10``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 01337
     - Carrier Identifier
   * - 11
     - ``sac_11``
     -
     - :ref:`NA <hl7-v2_5_1-NA>`
     - O
     -
     - 01338
     - Position in Carrier
   * - 12
     - ``sac_12``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0379
     - 01339
     - Tray Type - SAC
   * - 13
     - ``sac_13``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 01340
     - Tray Identifier
   * - 14
     - ``sac_14``
     -
     - :ref:`NA <hl7-v2_5_1-NA>`
     - O
     -
     - 01341
     - Position in Tray
   * - 15
     - ``sac_15``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     -
     - 01342
     - Location
   * - 16
     - ``sac_16``
     - 20
     - str
     - O
     -
     - 01343
     - Container Height
   * - 17
     - ``sac_17``
     - 20
     - str
     - O
     -
     - 01344
     - Container Diameter
   * - 18
     - ``sac_18``
     - 20
     - str
     - O
     -
     - 01345
     - Barrier Delta
   * - 19
     - ``sac_19``
     - 20
     - str
     - O
     -
     - 01346
     - Bottom Delta
   * - 20
     - ``sac_20``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01347
     - Container Height/Diameter/Delta Units
   * - 21
     - ``sac_21``
     - 20
     - str
     - O
     -
     - 00644
     - Container Volume
   * - 22
     - ``sac_22``
     - 20
     - str
     - O
     -
     - 01349
     - Available Specimen Volume
   * - 23
     - ``sac_23``
     - 20
     - str
     - O
     -
     - 01350
     - Initial Specimen Volume
   * - 24
     - ``sac_24``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01351
     - Volume Units
   * - 25
     - ``sac_25``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0380
     - 01352
     - Separator Type
   * - 26
     - ``sac_26``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0381
     - 01353
     - Cap Type
   * - 27
     - ``sac_27``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0371
     - 00647
     - Additive
   * - 28
     - ``sac_28``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01355
     - Specimen Component
   * - 29
     - ``sac_29``
     -
     - :ref:`SN <hl7-v2_5_1-SN>`
     - O
     -
     - 01356
     - Dilution Factor
   * - 30
     - ``sac_30``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0373
     - 01357
     - Treatment
   * - 31
     - ``sac_31``
     -
     - :ref:`SN <hl7-v2_5_1-SN>`
     - O
     -
     - 01358
     - Temperature
   * - 32
     - ``sac_32``
     - 20
     - str
     - O
     -
     - 01359
     - Hemolysis Index
   * - 33
     - ``sac_33``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01360
     - Hemolysis Index Units
   * - 34
     - ``sac_34``
     - 20
     - str
     - O
     -
     - 01361
     - Lipemia Index
   * - 35
     - ``sac_35``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01362
     - Lipemia Index Units
   * - 36
     - ``sac_36``
     - 20
     - str
     - O
     -
     - 01363
     - Icterus Index
   * - 37
     - ``sac_37``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01364
     - Icterus Index Units
   * - 38
     - ``sac_38``
     - 20
     - str
     - O
     -
     - 01365
     - Fibrin Index
   * - 39
     - ``sac_39``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01366
     - Fibrin Index Units
   * - 40
     - ``sac_40``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0374
     - 01367
     - System Induced Contaminants
   * - 41
     - ``sac_41``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0382
     - 01368
     - Drug Interference
   * - 42
     - ``sac_42``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0375
     - 01369
     - Artificial Blood
   * - 43
     - ``sac_43``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0376
     - 01370
     - Special Handling Code
   * - 44
     - ``sac_44``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0377
     - 01371
     - Other Environmental Factors

.. _hl7-v2_5_1-SCH:

SCH: Scheduling Activity Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.6.2

.. py:class:: hl7types.hl7.v2_5_1.segments.SCH.SCH
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
     - ``sch_1``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 00860
     - Placer Appointment ID
   * - 2
     - ``sch_2``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 00861
     - Filler Appointment ID
   * - 3
     - ``sch_3``
     - 5
     - str
     - C
     -
     - 00862
     - Occurrence Number
   * - 4
     - ``sch_4``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 00218
     - Placer Group Number
   * - 5
     - ``sch_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00864
     - Schedule ID
   * - 6
     - ``sch_6``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00883
     - Event Reason
   * - 7
     - ``sch_7``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0276
     - 00866
     - Appointment Reason
   * - 8
     - ``sch_8``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0277
     - 00867
     - Appointment Type
   * - 9
     - ``sch_9``
     - 20
     - str
     - O
     -
     - 00868
     - Appointment Duration
   * - 10
     - ``sch_10``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00869
     - Appointment Duration Units
   * - 11
     - ``sch_11``
     -
     - list[:ref:`TQ <hl7-v2_5_1-TQ>`]
     - O
     -
     - 00884
     - Appointment Timing Quantity
   * - 12
     - ``sch_12``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00874
     - Placer Contact Person
   * - 13
     - ``sch_13``
     -
     - :ref:`XTN <hl7-v2_5_1-XTN>`
     - O
     -
     - 00875
     - Placer Contact Phone Number
   * - 14
     - ``sch_14``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00876
     - Placer Contact Address
   * - 15
     - ``sch_15``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 00877
     - Placer Contact Location
   * - 16
     - ``sch_16``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - R
     -
     - 00885
     - Filler Contact Person
   * - 17
     - ``sch_17``
     -
     - :ref:`XTN <hl7-v2_5_1-XTN>`
     - O
     -
     - 00886
     - Filler Contact Phone Number
   * - 18
     - ``sch_18``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00887
     - Filler Contact Address
   * - 19
     - ``sch_19``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 00888
     - Filler Contact Location
   * - 20
     - ``sch_20``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - R
     -
     - 00878
     - Entered By Person
   * - 21
     - ``sch_21``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00879
     - Entered By Phone Number
   * - 22
     - ``sch_22``
     -
     - :ref:`PL <hl7-v2_5_1-PL>`
     - O
     -
     - 00880
     - Entered By Location
   * - 23
     - ``sch_23``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 00881
     - Parent Placer Appointment ID
   * - 24
     - ``sch_24``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 00882
     - Parent Filler Appointment ID
   * - 25
     - ``sch_25``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0278
     - 00889
     - Filler Status Code
   * - 26
     - ``sch_26``
     -
     - list[:ref:`EI <hl7-v2_5_1-EI>`]
     - C
     -
     - 00216
     - Placer Order Number
   * - 27
     - ``sch_27``
     -
     - list[:ref:`EI <hl7-v2_5_1-EI>`]
     - C
     -
     - 00217
     - Filler Order Number

.. _hl7-v2_5_1-SFT:

SFT: Software Segment
~~~~~~~~~~~~~~~~~~~~~

Section 2.15.12

.. py:class:: hl7types.hl7.v2_5_1.segments.SFT.SFT
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
     - ``sft_1``
     -
     - :ref:`XON <hl7-v2_5_1-XON>`
     - R
     -
     - 01834
     - Software Vendor Organization
   * - 2
     - ``sft_2``
     - 15
     - str
     - R
     -
     - 01835
     - Software Certified Version or Release Number
   * - 3
     - ``sft_3``
     - 20
     - str
     - R
     -
     - 01836
     - Software Product Name
   * - 4
     - ``sft_4``
     - 20
     - str
     - R
     -
     - 01837
     - Software Binary ID
   * - 5
     - ``sft_5``
     -
     - str
     - O
     -
     - 01838
     - Software Product Information
   * - 6
     - ``sft_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01839
     - Software Install Date

.. _hl7-v2_5_1-SID:

SID: Substance Identifier
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.4.11

.. py:class:: hl7types.hl7.v2_5_1.segments.SID.SID
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
     - ``sid_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     -
     - 01426
     - Application / Method Identifier
   * - 2
     - ``sid_2``
     - 20
     - str
     - C
     -
     - 01129
     - Substance Lot Number
   * - 3
     - ``sid_3``
     - 200
     - str
     - C
     -
     - 01428
     - Substance Container Identifier
   * - 4
     - ``sid_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 0385
     - 01429
     - Substance Manufacturer Identifier

.. _hl7-v2_5_1-SPM:

SPM: Specimen
~~~~~~~~~~~~~

Section 7.4.3

.. py:class:: hl7types.hl7.v2_5_1.segments.SPM.SPM
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
     - ``spm_1``
     - 4
     - str
     - O
     -
     - 01754
     - Set ID - SPM
   * - 2
     - ``spm_2``
     -
     - :ref:`EIP <hl7-v2_5_1-EIP>`
     - O
     -
     - 01755
     - Specimen ID
   * - 3
     - ``spm_3``
     -
     - list[:ref:`EIP <hl7-v2_5_1-EIP>`]
     - O
     -
     - 01756
     - Specimen Parent IDs
   * - 4
     - ``spm_4``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - R
     - 0487
     - 01900
     - Specimen Type
   * - 5
     - ``spm_5``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0541
     - 01757
     - Specimen Type Modifier
   * - 6
     - ``spm_6``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0371
     - 01758
     - Specimen Additives
   * - 7
     - ``spm_7``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0488
     - 01759
     - Specimen Collection Method
   * - 8
     - ``spm_8``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01901
     - Specimen Source Site
   * - 9
     - ``spm_9``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0542
     - 01760
     - Specimen Source Site Modifier
   * - 10
     - ``spm_10``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0543
     - 01761
     - Specimen Collection Site
   * - 11
     - ``spm_11``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0369
     - 01762
     - Specimen Role
   * - 12
     - ``spm_12``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01902
     - Specimen Collection Amount
   * - 13
     - ``spm_13``
     - 6
     - str
     - C
     -
     - 01763
     - Grouped Specimen Count
   * - 14
     - ``spm_14``
     - 250
     - list[str]
     - O
     -
     - 01764
     - Specimen Description
   * - 15
     - ``spm_15``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0376
     - 01908
     - Specimen Handling Code
   * - 16
     - ``spm_16``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0489
     - 01903
     - Specimen Risk Code
   * - 17
     - ``spm_17``
     -
     - :ref:`DR <hl7-v2_5_1-DR>`
     - O
     -
     - 01765
     - Specimen Collection Date/Time
   * - 18
     - ``spm_18``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00248
     - Specimen Received Date/Time
   * - 19
     - ``spm_19``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01904
     - Specimen Expiration Date/Time
   * - 20
     - ``spm_20``
     - 1
     - str
     - O
     - 0136
     - 01766
     - Specimen Availability
   * - 21
     - ``spm_21``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0490
     - 01767
     - Specimen Reject Reason
   * - 22
     - ``spm_22``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0491
     - 01768
     - Specimen Quality
   * - 23
     - ``spm_23``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0492
     - 01769
     - Specimen Appropriateness
   * - 24
     - ``spm_24``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0493
     - 01770
     - Specimen Condition
   * - 25
     - ``spm_25``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01771
     - Specimen Current Quantity
   * - 26
     - ``spm_26``
     - 4
     - str
     - O
     -
     - 01772
     - Number of Specimen Containers
   * - 27
     - ``spm_27``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     -
     - 01773
     - Container Type
   * - 28
     - ``spm_28``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0544
     - 01774
     - Container Condition
   * - 29
     - ``spm_29``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0494
     - 01775
     - Specimen Child Role

.. _hl7-v2_5_1-SPR:

SPR: Stored Procedure Request Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.10.5.5

.. py:class:: hl7types.hl7.v2_5_1.segments.SPR.SPR
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
     - ``spr_1``
     - 32
     - str
     - O
     -
     - 00696
     - Query Tag
   * - 2
     - ``spr_2``
     - 1
     - str
     - R
     - 0106
     - 00697
     - Query/Response Format Code
   * - 3
     - ``spr_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00704
     - Stored Procedure Name
   * - 4
     - ``spr_4``
     -
     - list[:ref:`QIP <hl7-v2_5_1-QIP>`]
     - O
     -
     - 00705
     - Input Parameter List

.. _hl7-v2_5_1-STF:

STF: Staff Identification
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.4.8

.. py:class:: hl7types.hl7.v2_5_1.segments.STF.STF
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - C
     - 9999
     - 00671
     - Primary Key Value - STF
   * - 2
     - ``stf_2``
     -
     - list[:ref:`CX <hl7-v2_5_1-CX>`]
     - O
     -
     - 00672
     - Staff Identifier List
   * - 3
     - ``stf_3``
     -
     - list[:ref:`XPN <hl7-v2_5_1-XPN>`]
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
     - Administrative Sex
   * - 6
     - ``stf_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00110
     - Date/Time of Birth
   * - 7
     - ``stf_7``
     - 1
     - str
     - O
     - 0183
     - 00675
     - Active/Inactive Flag
   * - 8
     - ``stf_8``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0184
     - 00676
     - Department
   * - 9
     - ``stf_9``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0069
     - 00677
     - Hospital Service - STF
   * - 10
     - ``stf_10``
     -
     - list[:ref:`XTN <hl7-v2_5_1-XTN>`]
     - O
     -
     - 00678
     - Phone
   * - 11
     - ``stf_11``
     -
     - list[:ref:`XAD <hl7-v2_5_1-XAD>`]
     - O
     -
     - 00679
     - Office/Home Address/Birthplace
   * - 12
     - ``stf_12``
     -
     - list[:ref:`DIN <hl7-v2_5_1-DIN>`]
     - O
     - 0537
     - 00680
     - Institution Activation Date
   * - 13
     - ``stf_13``
     -
     - list[:ref:`DIN <hl7-v2_5_1-DIN>`]
     - O
     - 0537
     - 00681
     - Institution Inactivation Date
   * - 14
     - ``stf_14``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
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
     - E-Mail Address
   * - 16
     - ``stf_16``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0185
     - 00684
     - Preferred Method of Contact
   * - 17
     - ``stf_17``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0002
     - 00119
     - Marital Status
   * - 18
     - ``stf_18``
     - 20
     - str
     - O
     -
     - 00785
     - Job Title
   * - 19
     - ``stf_19``
     -
     - :ref:`JCC <hl7-v2_5_1-JCC>`
     - O
     -
     - 00786
     - Job Code/Class
   * - 20
     - ``stf_20``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0066
     - 01276
     - Employment Status Code
   * - 21
     - ``stf_21``
     - 1
     - str
     - O
     - 0136
     - 01275
     - Additional Insured on Auto
   * - 22
     - ``stf_22``
     -
     - :ref:`DLN <hl7-v2_5_1-DLN>`
     - O
     -
     - 01302
     - Driver's License Number - Staff
   * - 23
     - ``stf_23``
     - 1
     - str
     - O
     - 0136
     - 01229
     - Copy Auto Ins
   * - 24
     - ``stf_24``
     - 8
     - str
     - O
     -
     - 01232
     - Auto Ins. Expires
   * - 25
     - ``stf_25``
     - 8
     - str
     - O
     -
     - 01298
     - Date Last DMV Review
   * - 26
     - ``stf_26``
     - 8
     - str
     - O
     -
     - 01234
     - Date Next DMV Review
   * - 27
     - ``stf_27``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0005
     - 00113
     - Race
   * - 28
     - ``stf_28``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0189
     - 00125
     - Ethnic Group
   * - 29
     - ``stf_29``
     - 1
     - str
     - O
     - 0136
     - 01596
     - Re-activation Approval Indicator
   * - 30
     - ``stf_30``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0171
     - 00129
     - Citizenship
   * - 31
     - ``stf_31``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01886
     - Death Date and Time
   * - 32
     - ``stf_32``
     - 1
     - str
     - O
     - 0136
     - 01887
     - Death Indicator
   * - 33
     - ``stf_33``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0538
     - 01888
     - Institution Relationship Type Code
   * - 34
     - ``stf_34``
     -
     - :ref:`DR <hl7-v2_5_1-DR>`
     - O
     -
     - 01889
     - Institution Relationship Period
   * - 35
     - ``stf_35``
     - 8
     - str
     - O
     -
     - 01890
     - Expected Return Date
   * - 36
     - ``stf_36``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0539
     - 01891
     - Cost Center Code
   * - 37
     - ``stf_37``
     - 1
     - str
     - O
     - 0136
     - 01892
     - Generic Classification Indicator
   * - 38
     - ``stf_38``
     -
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - 0540
     - 01893
     - Inactive Reason Code

.. _hl7-v2_5_1-TCC:

TCC: Test Code Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.4.9

.. py:class:: hl7types.hl7.v2_5_1.segments.TCC.TCC
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
     - ``tcc_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00238
     - Universal Service Identifier
   * - 2
     - ``tcc_2``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01408
     - Test Application Identifier
   * - 3
     - ``tcc_3``
     -
     - :ref:`SPS <hl7-v2_5_1-SPS>`
     - O
     -
     - 00249
     - Specimen Source
   * - 4
     - ``tcc_4``
     -
     - :ref:`SN <hl7-v2_5_1-SN>`
     - O
     -
     - 01410
     - Auto-Dilution Factor Default
   * - 5
     - ``tcc_5``
     -
     - :ref:`SN <hl7-v2_5_1-SN>`
     - O
     -
     - 01411
     - Rerun Dilution Factor Default
   * - 6
     - ``tcc_6``
     -
     - :ref:`SN <hl7-v2_5_1-SN>`
     - O
     -
     - 01412
     - Pre-Dilution Factor Default
   * - 7
     - ``tcc_7``
     -
     - :ref:`SN <hl7-v2_5_1-SN>`
     - O
     -
     - 01413
     - Endogenous Content of Pre-Dilution Diluent
   * - 8
     - ``tcc_8``
     - 10
     - str
     - O
     -
     - 01414
     - Inventory Limits Warning Level
   * - 9
     - ``tcc_9``
     - 1
     - str
     - O
     - 0136
     - 01415
     - Automatic Rerun Allowed
   * - 10
     - ``tcc_10``
     - 1
     - str
     - O
     - 0136
     - 01416
     - Automatic Repeat Allowed
   * - 11
     - ``tcc_11``
     - 1
     - str
     - O
     - 0136
     - 01417
     - Automatic Reflex Allowed
   * - 12
     - ``tcc_12``
     -
     - :ref:`SN <hl7-v2_5_1-SN>`
     - O
     -
     - 01418
     - Equipment Dynamic Range
   * - 13
     - ``tcc_13``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 00574
     - Units
   * - 14
     - ``tcc_14``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0388
     - 01419
     - Processing Type

.. _hl7-v2_5_1-TCD:

TCD: Test Code Detail
~~~~~~~~~~~~~~~~~~~~~

Section 13.4.10

.. py:class:: hl7types.hl7.v2_5_1.segments.TCD.TCD
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
     - ``tcd_1``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00238
     - Universal Service Identifier
   * - 2
     - ``tcd_2``
     -
     - :ref:`SN <hl7-v2_5_1-SN>`
     - O
     -
     - 01420
     - Auto-Dilution Factor
   * - 3
     - ``tcd_3``
     -
     - :ref:`SN <hl7-v2_5_1-SN>`
     - O
     -
     - 01421
     - Rerun Dilution Factor
   * - 4
     - ``tcd_4``
     -
     - :ref:`SN <hl7-v2_5_1-SN>`
     - O
     -
     - 01422
     - Pre-Dilution Factor
   * - 5
     - ``tcd_5``
     -
     - :ref:`SN <hl7-v2_5_1-SN>`
     - O
     -
     - 01413
     - Endogenous Content of Pre-Dilution Diluent
   * - 6
     - ``tcd_6``
     - 1
     - str
     - O
     - 0136
     - 01416
     - Automatic Repeat Allowed
   * - 7
     - ``tcd_7``
     - 1
     - str
     - O
     - 0136
     - 01424
     - Reflex Allowed
   * - 8
     - ``tcd_8``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0389
     - 01425
     - Analyte Repeat Status

.. _hl7-v2_5_1-TQ1:

TQ1: Timing/Quantity
~~~~~~~~~~~~~~~~~~~~

Section 4.5.4

.. py:class:: hl7types.hl7.v2_5_1.segments.TQ1.TQ1
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
     - ``tq1_1``
     - 4
     - str
     - O
     -
     - 01627
     - Set ID - TQ1
   * - 2
     - ``tq1_2``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01628
     - Quantity
   * - 3
     - ``tq1_3``
     -
     - list[:ref:`RPT <hl7-v2_5_1-RPT>`]
     - O
     - 0335
     - 01629
     - Repeat Pattern
   * - 4
     - ``tq1_4``
     - 20
     - list[str]
     - O
     -
     - 01630
     - Explicit Time
   * - 5
     - ``tq1_5``
     -
     - list[:ref:`CQ <hl7-v2_5_1-CQ>`]
     - O
     -
     - 01631
     - Relative Time and Units
   * - 6
     - ``tq1_6``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01632
     - Service Duration
   * - 7
     - ``tq1_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01633
     - Start date/time
   * - 8
     - ``tq1_8``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01634
     - End date/time
   * - 9
     - ``tq1_9``
     -
     - list[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - O
     - 0485
     - 01635
     - Priority
   * - 10
     - ``tq1_10``
     -
     - str
     - O
     -
     - 01636
     - Condition text
   * - 11
     - ``tq1_11``
     -
     - str
     - O
     -
     - 01637
     - Text instruction
   * - 12
     - ``tq1_12``
     - 10
     - str
     - C
     - 0427
     - 01638
     - Conjunction
   * - 13
     - ``tq1_13``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01639
     - Occurrence duration
   * - 14
     - ``tq1_14``
     - 10
     - str
     - O
     -
     - 01640
     - Total occurrence's

.. _hl7-v2_5_1-TQ2:

TQ2: Timing/Quantity Relationship
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.5.5

.. py:class:: hl7types.hl7.v2_5_1.segments.TQ2.TQ2
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
     - ``tq2_1``
     - 4
     - str
     - O
     -
     - 01648
     - Set ID - TQ2
   * - 2
     - ``tq2_2``
     - 1
     - str
     - O
     - 0503
     - 01649
     - Sequence/Results Flag
   * - 3
     - ``tq2_3``
     -
     - list[:ref:`EI <hl7-v2_5_1-EI>`]
     - C
     -
     - 01650
     - Related Placer Number
   * - 4
     - ``tq2_4``
     -
     - list[:ref:`EI <hl7-v2_5_1-EI>`]
     - C
     -
     - 01651
     - Related Filler Number
   * - 5
     - ``tq2_5``
     -
     - list[:ref:`EI <hl7-v2_5_1-EI>`]
     - C
     -
     - 01652
     - Related Placer Group Number
   * - 6
     - ``tq2_6``
     - 2
     - str
     - C
     - 0504
     - 01653
     - Sequence Condition Code
   * - 7
     - ``tq2_7``
     - 1
     - str
     - C
     - 0505
     - 01654
     - Cyclic Entry/Exit Indicator
   * - 8
     - ``tq2_8``
     -
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     -
     - 01655
     - Sequence Condition Time Interval
   * - 9
     - ``tq2_9``
     - 10
     - str
     - O
     -
     - 01656
     - Cyclic Group Maximum Number of Repeats
   * - 10
     - ``tq2_10``
     - 1
     - str
     - C
     - 0506
     - 01657
     - Special Service Request Relationship

.. _hl7-v2_5_1-TXA:

TXA: Transcription Document Header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.6.1

.. py:class:: hl7types.hl7.v2_5_1.segments.TXA.TXA
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
     - ``txa_1``
     - 4
     - str
     - R
     -
     - 00914
     - Set ID - TXA
   * - 2
     - ``txa_2``
     - 30
     - str
     - R
     - 0270
     - 00915
     - Document Type
   * - 3
     - ``txa_3``
     - 2
     - str
     - C
     - 0191
     - 00916
     - Document Content Presentation
   * - 4
     - ``txa_4``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00917
     - Activity Date/Time
   * - 5
     - ``txa_5``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - C
     -
     - 00918
     - Primary Activity Provider Code/Name
   * - 6
     - ``txa_6``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00919
     - Origination Date/Time
   * - 7
     - ``txa_7``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - C
     -
     - 00920
     - Transcription Date/Time
   * - 8
     - ``txa_8``
     -
     - list[:ref:`TS <hl7-v2_5_1-TS>`]
     - O
     -
     - 00921
     - Edit Date/Time
   * - 9
     - ``txa_9``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00922
     - Originator Code/Name
   * - 10
     - ``txa_10``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00923
     - Assigned Document Authenticator
   * - 11
     - ``txa_11``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - C
     -
     - 00924
     - Transcriptionist Code/Name
   * - 12
     - ``txa_12``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 00925
     - Unique Document Number
   * - 13
     - ``txa_13``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - C
     -
     - 00926
     - Parent Document Number
   * - 14
     - ``txa_14``
     -
     - list[:ref:`EI <hl7-v2_5_1-EI>`]
     - O
     -
     - 00216
     - Placer Order Number
   * - 15
     - ``txa_15``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     -
     - 00217
     - Filler Order Number
   * - 16
     - ``txa_16``
     - 30
     - str
     - O
     -
     - 00927
     - Unique Document File Name
   * - 17
     - ``txa_17``
     - 2
     - str
     - R
     - 0271
     - 00928
     - Document Completion Status
   * - 18
     - ``txa_18``
     - 2
     - str
     - O
     - 0272
     - 00929
     - Document Confidentiality Status
   * - 19
     - ``txa_19``
     - 2
     - str
     - O
     - 0273
     - 00930
     - Document Availability Status
   * - 20
     - ``txa_20``
     - 2
     - str
     - O
     - 0275
     - 00932
     - Document Storage Status
   * - 21
     - ``txa_21``
     - 30
     - str
     - C
     -
     - 00933
     - Document Change Reason
   * - 22
     - ``txa_22``
     -
     - list[:ref:`PPN <hl7-v2_5_1-PPN>`]
     - C
     -
     - 00934
     - Authentication Person, Time Stamp
   * - 23
     - ``txa_23``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 00935
     - Distributed Copies (Code and Name of Recipients)

.. _hl7-v2_5_1-UB1:

UB1: UB82
~~~~~~~~~

Section 6.5.10

.. py:class:: hl7types.hl7.v2_5_1.segments.UB1.UB1
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
     - Set ID - UB1
   * - 2
     - ``ub1_2``
     - 1
     - str
     - O
     -
     - 00531
     - Blood Deductible  (43)
   * - 3
     - ``ub1_3``
     - 2
     - str
     - O
     -
     - 00532
     - Blood Furnished-Pints Of (40)
   * - 4
     - ``ub1_4``
     - 2
     - str
     - O
     -
     - 00533
     - Blood Replaced-Pints (41)
   * - 5
     - ``ub1_5``
     - 2
     - str
     - O
     -
     - 00534
     - Blood Not Replaced-Pints(42)
   * - 6
     - ``ub1_6``
     - 2
     - str
     - O
     -
     - 00535
     - Co-Insurance Days (25)
   * - 7
     - ``ub1_7``
     - 14
     - list[str]
     - O
     - 0043
     - 00536
     - Condition Code (35-39)
   * - 8
     - ``ub1_8``
     - 3
     - str
     - O
     -
     - 00537
     - Covered Days - (23)
   * - 9
     - ``ub1_9``
     - 3
     - str
     - O
     -
     - 00538
     - Non Covered Days - (24)
   * - 10
     - ``ub1_10``
     -
     - list[:ref:`UVC <hl7-v2_5_1-UVC>`]
     - O
     -
     - 00539
     - Value Amount & Code (46-49)
   * - 11
     - ``ub1_11``
     - 2
     - str
     - O
     -
     - 00540
     - Number Of Grace Days (90)
   * - 12
     - ``ub1_12``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0348
     - 00541
     - Special Program Indicator (44)
   * - 13
     - ``ub1_13``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0349
     - 00542
     - PSRO/UR Approval Indicator (87)
   * - 14
     - ``ub1_14``
     - 8
     - str
     - O
     -
     - 00543
     - PSRO/UR Approved Stay-Fm (88)
   * - 15
     - ``ub1_15``
     - 8
     - str
     - O
     -
     - 00544
     - PSRO/UR Approved Stay-To (89)
   * - 16
     - ``ub1_16``
     -
     - list[:ref:`OCD <hl7-v2_5_1-OCD>`]
     - O
     -
     - 00545
     - Occurrence (28-32)
   * - 17
     - ``ub1_17``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - 0351
     - 00546
     - Occurrence Span (33)
   * - 18
     - ``ub1_18``
     - 8
     - str
     - O
     -
     - 00547
     - Occur Span Start Date(33)
   * - 19
     - ``ub1_19``
     - 8
     - str
     - O
     -
     - 00548
     - Occur Span End Date (33)
   * - 20
     - ``ub1_20``
     - 30
     - str
     - O
     -
     - 00549
     - UB-82 Locator 2
   * - 21
     - ``ub1_21``
     - 7
     - str
     - O
     -
     - 00550
     - UB-82 Locator 9
   * - 22
     - ``ub1_22``
     - 8
     - str
     - O
     -
     - 00551
     - UB-82 Locator 27
   * - 23
     - ``ub1_23``
     - 17
     - str
     - O
     -
     - 00552
     - UB-82 Locator 45

.. _hl7-v2_5_1-UB2:

UB2: UB92 Data
~~~~~~~~~~~~~~

Section 6.5.11

.. py:class:: hl7types.hl7.v2_5_1.segments.UB2.UB2
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
     - Set ID - UB2
   * - 2
     - ``ub2_2``
     - 3
     - str
     - O
     -
     - 00554
     - Co-Insurance Days (9)
   * - 3
     - ``ub2_3``
     - 2
     - list[str]
     - O
     - 0043
     - 00555
     - Condition Code (24-30)
   * - 4
     - ``ub2_4``
     - 3
     - str
     - O
     -
     - 00556
     - Covered Days (7)
   * - 5
     - ``ub2_5``
     - 4
     - str
     - O
     -
     - 00557
     - Non-Covered Days (8)
   * - 6
     - ``ub2_6``
     -
     - list[:ref:`UVC <hl7-v2_5_1-UVC>`]
     - O
     -
     - 00558
     - Value Amount & Code
   * - 7
     - ``ub2_7``
     -
     - list[:ref:`OCD <hl7-v2_5_1-OCD>`]
     - O
     -
     - 00559
     - Occurrence Code & Date (32-35)
   * - 8
     - ``ub2_8``
     -
     - list[:ref:`OSP <hl7-v2_5_1-OSP>`]
     - O
     -
     - 00560
     - Occurrence Span Code/Dates (36)
   * - 9
     - ``ub2_9``
     - 29
     - list[str]
     - O
     -
     - 00561
     - UB92 Locator 2 (State)
   * - 10
     - ``ub2_10``
     - 12
     - list[str]
     - O
     -
     - 00562
     - UB92 Locator 11 (State)
   * - 11
     - ``ub2_11``
     - 5
     - str
     - O
     -
     - 00563
     - UB92 Locator 31 (National)
   * - 12
     - ``ub2_12``
     - 23
     - list[str]
     - O
     -
     - 00564
     - Document Control Number
   * - 13
     - ``ub2_13``
     - 4
     - list[str]
     - O
     -
     - 00565
     - UB92 Locator 49 (National)
   * - 14
     - ``ub2_14``
     - 14
     - list[str]
     - O
     -
     - 00566
     - UB92 Locator 56 (State)
   * - 15
     - ``ub2_15``
     - 27
     - str
     - O
     -
     - 00567
     - UB92 Locator 57 (National)
   * - 16
     - ``ub2_16``
     - 2
     - list[str]
     - O
     -
     - 00568
     - UB92 Locator 78 (State)
   * - 17
     - ``ub2_17``
     - 3
     - str
     - O
     -
     - 00815
     - Special Visit Count

.. _hl7-v2_5_1-URD:

URD: Results/update Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.10.5.6

.. py:class:: hl7types.hl7.v2_5_1.segments.URD.URD
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
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00045
     - R/U Date/Time
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
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - R
     -
     - 00047
     - R/U Who Subject Definition
   * - 4
     - ``urd_4``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
     - O
     - 0048
     - 00048
     - R/U What Subject Definition
   * - 5
     - ``urd_5``
     -
     - list[:ref:`CE <hl7-v2_5_1-CE>`]
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
     - R/U Display/Print Locations
   * - 7
     - ``urd_7``
     - 1
     - str
     - O
     - 0108
     - 00051
     - R/U Results Level

.. _hl7-v2_5_1-URS:

URS: Unsolicited Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.10.5.7

.. py:class:: hl7types.hl7.v2_5_1.segments.URS.URS
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
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00053
     - R/U When Data Start Date/Time
   * - 3
     - ``urs_3``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 00054
     - R/U When Data End Date/Time
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
     - R/U Which Date/Time Qualifier
   * - 7
     - ``urs_7``
     - 12
     - list[str]
     - O
     - 0157
     - 00058
     - R/U Which Date/Time Status Qualifier
   * - 8
     - ``urs_8``
     - 12
     - list[str]
     - O
     - 0158
     - 00059
     - R/U Date/Time Selection Qualifier
   * - 9
     - ``urs_9``
     -
     - :ref:`TQ <hl7-v2_5_1-TQ>`
     - O
     -
     - 00695
     - R/U Quantity/Timing Qualifier

.. _hl7-v2_5_1-VAR:

VAR: Variance
~~~~~~~~~~~~~

Section 12.4.5

.. py:class:: hl7types.hl7.v2_5_1.segments.VAR.VAR
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
     - ``var_1``
     -
     - :ref:`EI <hl7-v2_5_1-EI>`
     - R
     -
     - 01212
     - Variance Instance ID
   * - 2
     - ``var_2``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - R
     -
     - 01213
     - Documented Date/Time
   * - 3
     - ``var_3``
     -
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     -
     - 01214
     - Stated Variance Date/Time
   * - 4
     - ``var_4``
     -
     - list[:ref:`XCN <hl7-v2_5_1-XCN>`]
     - O
     -
     - 01215
     - Variance Originator
   * - 5
     - ``var_5``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     -
     - 01216
     - Variance Classification
   * - 6
     - ``var_6``
     - 512
     - list[str]
     - O
     -
     - 01217
     - Variance Description

.. _hl7-v2_5_1-VTQ:

VTQ: Virtual Table Query Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.10.5.8

.. py:class:: hl7types.hl7.v2_5_1.segments.VTQ.VTQ
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
     - ``vtq_1``
     - 32
     - str
     - O
     -
     - 00696
     - Query Tag
   * - 2
     - ``vtq_2``
     - 1
     - str
     - R
     - 0106
     - 00697
     - Query/Response Format Code
   * - 3
     - ``vtq_3``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00698
     - VT Query Name
   * - 4
     - ``vtq_4``
     -
     - :ref:`CE <hl7-v2_5_1-CE>`
     - R
     -
     - 00699
     - Virtual Table Name
   * - 5
     - ``vtq_5``
     -
     - list[:ref:`QSC <hl7-v2_5_1-QSC>`]
     - O
     -
     - 00700
     - Selection Criteria
