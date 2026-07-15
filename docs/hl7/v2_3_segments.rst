v2.3 Segments
=============

.. _hl7-v2_3-ACC:

ACC: Accident
~~~~~~~~~~~~~

Section 6.4.9

.. py:class:: hl7types.hl7.v2_3.segments.ACC.ACC
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00527
     - Accident Date/Time
   * - 2
     - ``acc_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00812
     - Auto Accident State
   * - 5
     - ``acc_5``
     - 2
     - str
     - O
     - 0136
     - 00813
     - Accident Job Related Indicator
   * - 6
     - ``acc_6``
     - 2
     - str
     - O
     - 0136
     - 00814
     - Accident Death Indicator

.. _hl7-v2_3-ADD:

ADD: Addendum segment
~~~~~~~~~~~~~~~~~~~~~

Section 2.24.10

.. py:class:: hl7types.hl7.v2_3.segments.ADD.ADD
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

.. _hl7-v2_3-AIG:

AIG: Appointment Information - General Resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.5.5

.. py:class:: hl7types.hl7.v2_3.segments.AIG.AIG
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
     - O
     - 0206
     - 00763
     - Segment Action Code
   * - 3
     - ``aig_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     -
     - 00897
     - Resource ID
   * - 4
     - ``aig_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00898
     - Resource Type
   * - 5
     - ``aig_5``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00901
     - Resource Quantity Units
   * - 8
     - ``aig_8``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     - 0278
     - 00889
     - Filler Status Code

.. _hl7-v2_3-AIL:

AIL: Appointment Information - Location Resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.5.6

.. py:class:: hl7types.hl7.v2_3.segments.AIL.AIL
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
     - O
     - 0206
     - 00763
     - Segment Action Code
   * - 3
     - ``ail_3``
     -
     - :ref:`PL <hl7-v2_3-PL>`
     - R
     -
     - 00903
     - Location Resource ID
   * - 4
     - ``ail_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     -
     - 00904
     - Location Type
   * - 5
     - ``ail_5``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     -
     - 00905
     - Location Group
   * - 6
     - ``ail_6``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     - 0278
     - 00889
     - Filler Status Code

.. _hl7-v2_3-AIP:

AIP: Appointment Information - Personnel Resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.5.7

.. py:class:: hl7types.hl7.v2_3.segments.AIP.AIP
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
     - O
     - 0206
     - 00763
     - Segment Action Code
   * - 3
     - ``aip_3``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - C
     -
     - 00913
     - Personnel Resource ID
   * - 4
     - ``aip_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00907
     - Resource Role
   * - 5
     - ``aip_5``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00899
     - Resource Group
   * - 6
     - ``aip_6``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     - 0278
     - 00889
     - Filler Status Code

.. _hl7-v2_3-AIS:

AIS: Appointment Information - Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.5.4

.. py:class:: hl7types.hl7.v2_3.segments.AIS.AIS
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
     - O
     - 0206
     - 00763
     - Segment Action Code
   * - 3
     - ``ais_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00238
     - Universal Service Identifier
   * - 4
     - ``ais_4``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     - 0278
     - 00889
     - Filler Status Code

.. _hl7-v2_3-AL1:

AL1: Patient allergy information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.6

.. py:class:: hl7types.hl7.v2_3.segments.AL1.AL1
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
     - 2
     - str
     - O
     - 0127
     - 00204
     - Allergy Type
   * - 3
     - ``al1_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00205
     - Allergy Code/Mnemonic/ Description
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

.. _hl7-v2_3-APR:

APR: Appointment Preferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.5.8

.. py:class:: hl7types.hl7.v2_3.segments.APR.APR
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
     - list[:ref:`SCV <hl7-v2_3-SCV>`]
     - O
     -
     - 00908
     - Time Selection Criteria
   * - 2
     - ``apr_2``
     -
     - list[:ref:`SCV <hl7-v2_3-SCV>`]
     - O
     -
     - 00909
     - Resource Selection Criteria
   * - 3
     - ``apr_3``
     -
     - list[:ref:`SCV <hl7-v2_3-SCV>`]
     - O
     -
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
     - list[:ref:`SCV <hl7-v2_3-SCV>`]
     - O
     -
     - 00912
     - Filler Override Criteria

.. _hl7-v2_3-ARQ:

ARQ: Appointment Request
~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.5.1

.. py:class:: hl7types.hl7.v2_3.segments.ARQ.ARQ
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
     - :ref:`EI <hl7-v2_3-EI>`
     - R
     -
     - 00860
     - Placer Appointment ID
   * - 2
     - ``arq_2``
     -
     - :ref:`EI <hl7-v2_3-EI>`
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
     - :ref:`EI <hl7-v2_3-EI>`
     - O
     -
     - 00863
     - Placer Group Number
   * - 5
     - ``arq_5``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00864
     - Schedule ID
   * - 6
     - ``arq_6``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00865
     - Request Event Reason
   * - 7
     - ``arq_7``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0276
     - 00866
     - Appointment Reason
   * - 8
     - ``arq_8``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00869
     - Appointment Duration Units
   * - 11
     - ``arq_11``
     -
     - list[:ref:`DR <hl7-v2_3-DR>`]
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
     - Priority
   * - 13
     - ``arq_13``
     -
     - :ref:`RI <hl7-v2_3-RI>`
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
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 00874
     - Placer Contact Person
   * - 16
     - ``arq_16``
     -
     - :ref:`XTN <hl7-v2_3-XTN>`
     - O
     -
     - 00875
     - Placer Contact Phone Number
   * - 17
     - ``arq_17``
     -
     - :ref:`XAD <hl7-v2_3-XAD>`
     - O
     -
     - 00876
     - Placer Contact Address
   * - 18
     - ``arq_18``
     -
     - :ref:`PL <hl7-v2_3-PL>`
     - O
     -
     - 00877
     - Placer Contact Location
   * - 19
     - ``arq_19``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - R
     -
     - 00878
     - Entered By Person
   * - 20
     - ``arq_20``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00879
     - Entered By Phone Number
   * - 21
     - ``arq_21``
     -
     - :ref:`PL <hl7-v2_3-PL>`
     - O
     -
     - 00880
     - Entered By Location
   * - 22
     - ``arq_22``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - O
     -
     - 00881
     - Parent Placer Appointment ID
   * - 23
     - ``arq_23``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - O
     -
     - 00882
     - Parent Filler Appointment ID

.. _hl7-v2_3-AUT:

AUT: Authorization Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.5.2

.. py:class:: hl7types.hl7.v2_3.segments.AUT.AUT
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0072
     - 01146
     - Authorizing Payor, Plan Code
   * - 2
     - ``aut_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01149
     - Authorization Effective Date
   * - 5
     - ``aut_5``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01150
     - Authorization Expiration Date
   * - 6
     - ``aut_6``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - C
     -
     - 01151
     - Authorization Identifier
   * - 7
     - ``aut_7``
     -
     - :ref:`CP <hl7-v2_3-CP>`
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01145
     - Process Date

.. _hl7-v2_3-BHS:

BHS: Batch header
~~~~~~~~~~~~~~~~~

Section 2.24.13

.. py:class:: hl7types.hl7.v2_3.segments.BHS.BHS
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
     - 15
     - str
     - O
     -
     - 00085
     - Batch Receiving Application
   * - 6
     - ``bhs_6``
     - 20
     - str
     - O
     -
     - 00086
     - Batch Receiving Facility
   * - 7
     - ``bhs_7``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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

.. _hl7-v2_3-BLG:

BLG: Billing Segment
~~~~~~~~~~~~~~~~~~~~

Section 4.3.2

.. py:class:: hl7types.hl7.v2_3.segments.BLG.BLG
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
     -
     - :ref:`CK <hl7-v2_3-CK>`
     - O
     -
     - 00236
     - Account ID

.. _hl7-v2_3-BTS:

BTS: Batch trailer segment
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.14

.. py:class:: hl7types.hl7.v2_3.segments.BTS.BTS
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

.. _hl7-v2_3-CDM:

CDM: Charge Description Master
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.9.2

.. py:class:: hl7types.hl7.v2_3.segments.CDM.CDM
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     - 0132
     - 00982
     - Primary Key Value
   * - 2
     - ``cdm_2``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00987
     - Exploding Charges
   * - 7
     - ``cdm_7``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00988
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
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
     - list[:ref:`CK <hl7-v2_3-CK>`]
     - O
     -
     - 00992
     - Contract Number
   * - 12
     - ``cdm_12``
     -
     - :ref:`XON <hl7-v2_3-XON>`
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

.. _hl7-v2_3-CM0:

CM0: Clinical Study Master
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.2

.. py:class:: hl7types.hl7.v2_3.segments.CM0.CM0
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
     - CM0 - Set ID
   * - 2
     - ``cm0_2``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - R
     -
     - 01011
     - Sponsor Study ID
   * - 3
     - ``cm0_3``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 01012
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
     - :ref:`XCN <hl7-v2_3-XCN>`
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
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 01018
     - Contact for Study
   * - 10
     - ``cm0_10``
     -
     - :ref:`XTN <hl7-v2_3-XTN>`
     - O
     -
     - 01019
     - Contact's Tel. Number
   * - 11
     - ``cm0_11``
     -
     - :ref:`XAD <hl7-v2_3-XAD>`
     - O
     -
     - 01020
     - Contact's Address

.. _hl7-v2_3-CM1:

CM1: Clinical Study Phase Master
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.3

.. py:class:: hl7types.hl7.v2_3.segments.CM1.CM1
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
     - CM1 - Set ID
   * - 2
     - ``cm1_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     -
     - 01051
     - Study Phase Identifier
   * - 3
     - ``cm1_3``
     - 300
     - str
     - R
     -
     - 01023
     - Description of Study Phase

.. _hl7-v2_3-CM2:

CM2: Clinical Study Schedule Master
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.4

.. py:class:: hl7types.hl7.v2_3.segments.CM2.CM2
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
     - CM2 - Set ID
   * - 2
     - ``cm2_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - R
     -
     - 01027
     - Events Scheduled This Time Point

.. _hl7-v2_3-CSP:

CSP: Clinical Study Phase
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.2

.. py:class:: hl7types.hl7.v2_3.segments.CSP.CSP
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
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     -
     - 01051
     - Study Phase Identifier
   * - 2
     - ``csp_2``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - R
     -
     - 01052
     - Date/time Study Phase Began
   * - 3
     - ``csp_3``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01053
     - Date/time Study Phase Ended
   * - 4
     - ``csp_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01054
     - Study Phase Evaluability

.. _hl7-v2_3-CSR:

CSR: Clinical Study Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_3.segments.CSR.CSR
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
     - :ref:`EI <hl7-v2_3-EI>`
     - R
     -
     - 01011
     - Sponsor Study ID
   * - 2
     - ``csr_2``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - O
     -
     - 01036
     - Alternate Study ID
   * - 3
     - ``csr_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01037
     - Institution Registering the Patient
   * - 4
     - ``csr_4``
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - R
     -
     - 01038
     - Sponsor Patient ID
   * - 5
     - ``csr_5``
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 01039
     - Alternate Patient ID
   * - 6
     - ``csr_6``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01040
     - Date/Time of Patient Study Registration
   * - 7
     - ``csr_7``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 01041
     - Person Performing Study Registration
   * - 8
     - ``csr_8``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - R
     -
     - 01042
     - Study Authorizing Provider
   * - 9
     - ``csr_9``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - C
     -
     - 01043
     - Date/time Patient Study Consent Signed
   * - 10
     - ``csr_10``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     -
     - 01044
     - Patient Study Eligibility Status
   * - 11
     - ``csr_11``
     -
     - list[:ref:`TS <hl7-v2_3-TS>`]
     - O
     -
     - 01045
     - Study Randomization Date/time
   * - 12
     - ``csr_12``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 01046
     - Study Randomized Arm
   * - 13
     - ``csr_13``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 01047
     - Stratum for Study Randomization
   * - 14
     - ``csr_14``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     -
     - 01048
     - Patient Evaluability Status
   * - 15
     - ``csr_15``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - C
     -
     - 01049
     - Date/time Ended Study
   * - 16
     - ``csr_16``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     -
     - 01050
     - Reason Ended Study

.. _hl7-v2_3-CSS:

CSS: Clinical Study Data Schedule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.3

.. py:class:: hl7types.hl7.v2_3.segments.CSS.CSS
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01055
     - Study Scheduled Time Point
   * - 2
     - ``css_2``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01056
     - Study Scheduled Patient Time Point
   * - 3
     - ``css_3``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 01057
     - Study Quality Control Codes

.. _hl7-v2_3-CTD:

CTD: Contact Data
~~~~~~~~~~~~~~~~~

Section 11.5.4

.. py:class:: hl7types.hl7.v2_3.segments.CTD.CTD
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     - 0131
     - 00196
     - Contact Role
   * - 2
     - ``ctd_2``
     -
     - list[:ref:`XPN <hl7-v2_3-XPN>`]
     - O
     -
     - 01165
     - Contact Name
   * - 3
     - ``ctd_3``
     -
     - list[:ref:`XAD <hl7-v2_3-XAD>`]
     - O
     -
     - 01268
     - Contact Address
   * - 4
     - ``ctd_4``
     -
     - :ref:`PL <hl7-v2_3-PL>`
     - O
     -
     - 01167
     - Contact Location
   * - 5
     - ``ctd_5``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 01168
     - Contact Communication Information
   * - 6
     - ``ctd_6``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0185
     - 00684
     - Preferred Method of Contact
   * - 7
     - ``ctd_7``
     -
     - list[str]
     - O
     -
     - 01171
     - Contact Identifiers

.. _hl7-v2_3-CTI:

CTI: Clinical Trial Identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.4

.. py:class:: hl7types.hl7.v2_3.segments.CTI.CTI
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
     - :ref:`EI <hl7-v2_3-EI>`
     - R
     -
     - 01011
     - Sponsor Study ID
   * - 2
     - ``cti_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     -
     - 01051
     - Study Phase Identifier
   * - 3
     - ``cti_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01055
     - Study Scheduled Time Point

.. _hl7-v2_3-DB1:

DB1: Disability Segment
~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.10

.. py:class:: hl7types.hl7.v2_3.segments.DB1.DB1
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
     - Disabled person code
   * - 3
     - ``db1_3``
     -
     - list[:ref:`CX <hl7-v2_3-CX>`]
     - O
     -
     - 01285
     - Disabled person identifier
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
     - Disability start date
   * - 6
     - ``db1_6``
     - 8
     - str
     - O
     -
     - 01288
     - Disability end date
   * - 7
     - ``db1_7``
     - 8
     - str
     - O
     -
     - 01289
     - Disability return to work date
   * - 8
     - ``db1_8``
     - 8
     - str
     - O
     -
     - 01290
     - Disability unable to work date

.. _hl7-v2_3-DG1:

DG1: Diagnosis
~~~~~~~~~~~~~~

Section 6.4.2

.. py:class:: hl7types.hl7.v2_3.segments.DG1.DG1
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
     - Set ID - Diagnosis
   * - 2
     - ``dg1_2``
     - 2
     - str
     - O
     - 0053
     - 00376
     - Diagnosis Coding Method
   * - 3
     - ``dg1_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0051
     - 00377
     - Diagnosis Code
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
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0118
     - 00381
     - Major Diagnostic Category
   * - 8
     - ``dg1_8``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0055
     - 00382
     - Diagnostic Related Group
   * - 9
     - ``dg1_9``
     - 2
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CP <hl7-v2_3-CP>`
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
     - Grouper Version and Type
   * - 15
     - ``dg1_15``
     - 2
     - str
     - O
     -
     - 00389
     - Diagnosis Priority
   * - 16
     - ``dg1_16``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00768
     - Attestation Date/Time

.. _hl7-v2_3-DRG:

DRG: Diagnosis Related Group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.3

.. py:class:: hl7types.hl7.v2_3.segments.DRG.DRG
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0055
     - 00382
     - Diagnostic Related Group
   * - 2
     - ``drg_2``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00769
     - DRG Assigned Date/Time
   * - 3
     - ``drg_3``
     - 2
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CP <hl7-v2_3-CP>`
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
     - :ref:`CP <hl7-v2_3-CP>`
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

.. _hl7-v2_3-DSC:

DSC: Continuation pointer segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.8

.. py:class:: hl7types.hl7.v2_3.segments.DSC.DSC
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

.. _hl7-v2_3-DSP:

DSP: Display data segment
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.9

.. py:class:: hl7types.hl7.v2_3.segments.DSP.DSP
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

.. _hl7-v2_3-EQL:

EQL: Embedded Query Language
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.16

.. py:class:: hl7types.hl7.v2_3.segments.EQL.EQL
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
     - Query tag
   * - 2
     - ``eql_2``
     - 1
     - str
     - R
     - 0106
     - 00697
     - Query/ Response Format Code
   * - 3
     - ``eql_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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

.. _hl7-v2_3-ERQ:

ERQ: Event Replay Query Segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.21

.. py:class:: hl7types.hl7.v2_3.segments.ERQ.ERQ
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
     - Query tag
   * - 2
     - ``erq_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00706
     - Event identifier
   * - 3
     - ``erq_3``
     -
     - list[:ref:`QIP <hl7-v2_3-QIP>`]
     - O
     -
     - 00705
     - Input parameter list

.. _hl7-v2_3-ERR:

ERR: Error segment
~~~~~~~~~~~~~~~~~~

Section 2.24.3

.. py:class:: hl7types.hl7.v2_3.segments.ERR.ERR
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
     - HL70060
     - 00024
     - Error Code and Location

.. _hl7-v2_3-EVN:

EVN: Event type
~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_3.segments.EVN.EVN
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00100
     - Recorded Date/Time
   * - 3
     - ``evn_3``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`CN <hl7-v2_3-CN>`
     - O
     - 0188
     - 00103
     - Operator ID
   * - 6
     - ``evn_6``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01278
     - Event occured

.. _hl7-v2_3-FAC:

FAC: Facility
~~~~~~~~~~~~~

Section 7.11.6

.. py:class:: hl7types.hl7.v2_3.segments.FAC.FAC
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
     - list[:ref:`EI <hl7-v2_3-EI>`]
     - R
     -
     - 01262
     - Facility ID
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
     - :ref:`XAD <hl7-v2_3-XAD>`
     - R
     -
     - 01264
     - Facility Address
   * - 4
     - ``fac_4``
     -
     - :ref:`XTN <hl7-v2_3-XTN>`
     - R
     -
     - 01265
     - Facility Telecommunication
   * - 5
     - ``fac_5``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
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
     - list[:ref:`XAD <hl7-v2_3-XAD>`]
     - O
     -
     - 01268
     - Contact Address
   * - 8
     - ``fac_8``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 01269
     - Contact Telecommunication
   * - 9
     - ``fac_9``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
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
     - :ref:`XAD <hl7-v2_3-XAD>`
     - O
     -
     - 01272
     - Signature Authority Address
   * - 12
     - ``fac_12``
     -
     - :ref:`XTN <hl7-v2_3-XTN>`
     - O
     -
     - 01273
     - Signature Authority Telecommunication

.. _hl7-v2_3-FHS:

FHS: File header segment
~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.11

.. py:class:: hl7types.hl7.v2_3.segments.FHS.FHS
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
     - 15
     - str
     - O
     -
     - 00071
     - File Receiving Application
   * - 6
     - ``fhs_6``
     - 20
     - str
     - O
     -
     - 00072
     - File Receiving Facility
   * - 7
     - ``fhs_7``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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

.. _hl7-v2_3-FT1:

FT1: Financial transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.1

.. py:class:: hl7types.hl7.v2_3.segments.FT1.FT1
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
     - Set ID - Financial Transaction
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
     - :ref:`TS <hl7-v2_3-TS>`
     - R
     -
     - 00358
     - Transaction Date
   * - 5
     - ``ft1_5``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - Transaction Description - alternate
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
     - :ref:`CP <hl7-v2_3-CP>`
     - O
     -
     - 00365
     - Transaction Amount - Extended
   * - 12
     - ``ft1_12``
     -
     - :ref:`CP <hl7-v2_3-CP>`
     - O
     -
     - 00366
     - Transaction Amount - Unit
   * - 13
     - ``ft1_13``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0049
     - 00367
     - Department Code
   * - 14
     - ``ft1_14``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0072
     - 00368
     - Insurance Plan ID
   * - 15
     - ``ft1_15``
     -
     - :ref:`CP <hl7-v2_3-CP>`
     - O
     -
     - 00369
     - Insurance Amount
   * - 16
     - ``ft1_16``
     -
     - :ref:`PL <hl7-v2_3-PL>`
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     - 0051
     - 00371
     - Diagnosis Code
   * - 20
     - ``ft1_20``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     - 0084
     - 00372
     - Performed By Code
   * - 21
     - ``ft1_21``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 00373
     - Ordered By Code
   * - 22
     - ``ft1_22``
     - 12
     - str
     - O
     -
     - 00374
     - Unit Cost
   * - 23
     - ``ft1_23``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - C
     -
     - 00217
     - Filler Order Number
   * - 24
     - ``ft1_24``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 00765
     - Entered By Code
   * - 25
     - ``ft1_25``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0088
     - 00393
     - Procedure Code

.. _hl7-v2_3-FTS:

FTS: File trailer segment
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.12

.. py:class:: hl7types.hl7.v2_3.segments.FTS.FTS
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

.. _hl7-v2_3-GOL:

GOL: Goal Detail
~~~~~~~~~~~~~~~~

Section 12.3.1

.. py:class:: hl7types.hl7.v2_3.segments.GOL.GOL
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
     - :ref:`TS <hl7-v2_3-TS>`
     - R
     -
     - 00817
     - Action Date/Time
   * - 3
     - ``gol_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00818
     - Goal ID
   * - 4
     - ``gol_4``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - R
     -
     - 00819
     - Goal Instance ID
   * - 5
     - ``gol_5``
     -
     - :ref:`EI <hl7-v2_3-EI>`
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00822
     - Goal Established Date/Time
   * - 8
     - ``gol_8``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00824
     - Expected Goal Achievement Date/Time
   * - 9
     - ``gol_9``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00825
     - Goal Classification
   * - 10
     - ``gol_10``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00826
     - Goal Management Discipline
   * - 11
     - ``gol_11``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00827
     - Current Goal Review Status
   * - 12
     - ``gol_12``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00828
     - Current Goal Review Date/Time
   * - 13
     - ``gol_13``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00829
     - Next Goal Review Date/Time
   * - 14
     - ``gol_14``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00830
     - Previous Goal Review Date/Time
   * - 15
     - ``gol_15``
     -
     - :ref:`TQ <hl7-v2_3-TQ>`
     - O
     -
     - 00831
     - Goal Review Interval
   * - 16
     - ``gol_16``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00834
     - Goal Life Cycle Status
   * - 19
     - ``gol_19``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00835
     - Goal Life Cycle Status Date/Time
   * - 20
     - ``gol_20``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00836
     - Goal Target Type
   * - 21
     - ``gol_21``
     -
     - list[:ref:`XPN <hl7-v2_3-XPN>`]
     - O
     -
     - 00837
     - Goal Target Name

.. _hl7-v2_3-GT1:

GT1: Guarantor
~~~~~~~~~~~~~~

Section 6.4.5

.. py:class:: hl7types.hl7.v2_3.segments.GT1.GT1
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
     - Set ID - Guarantor
   * - 2
     - ``gt1_2``
     -
     - list[:ref:`CX <hl7-v2_3-CX>`]
     - O
     -
     - 00406
     - Guarantor Number
   * - 3
     - ``gt1_3``
     -
     - list[:ref:`XPN <hl7-v2_3-XPN>`]
     - R
     -
     - 00407
     - Guarantor Name
   * - 4
     - ``gt1_4``
     -
     - list[:ref:`XPN <hl7-v2_3-XPN>`]
     - O
     -
     - 00408
     - Guarantor Spouse Name
   * - 5
     - ``gt1_5``
     -
     - list[:ref:`XAD <hl7-v2_3-XAD>`]
     - O
     -
     - 00409
     - Guarantor Address
   * - 6
     - ``gt1_6``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00410
     - Guarantor Ph Num- Home
   * - 7
     - ``gt1_7``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00411
     - Guarantor Ph Num-Business
   * - 8
     - ``gt1_8``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00412
     - Guarantor Date/Time of Birth
   * - 9
     - ``gt1_9``
     - 1
     - str
     - O
     - 0001
     - 00413
     - Guarantor Sex
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
     - 2
     - str
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
     - list[:ref:`XPN <hl7-v2_3-XPN>`]
     - O
     -
     - 00420
     - Guarantor Employer Name
   * - 17
     - ``gt1_17``
     -
     - list[:ref:`XAD <hl7-v2_3-XAD>`]
     - O
     -
     - 00421
     - Guarantor Employer Address
   * - 18
     - ``gt1_18``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00422
     - Guarantor Employ Phone Number
   * - 19
     - ``gt1_19``
     -
     - list[:ref:`CX <hl7-v2_3-CX>`]
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
     - list[:ref:`XON <hl7-v2_3-XON>`]
     - O
     -
     - 00425
     - Guarantor Organization
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00774
     - Guarantor Credit Rating Code
   * - 24
     - ``gt1_24``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0218
     - 00777
     - Guarantor Charge Adjustment Code
   * - 27
     - ``gt1_27``
     -
     - :ref:`CP <hl7-v2_3-CP>`
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
     - list[:ref:`CX <hl7-v2_3-CX>`]
     - O
     -
     - 00780
     - Guarantor Employer ID Number
   * - 30
     - ``gt1_30``
     - 1
     - str
     - O
     -
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
     - str
     - O
     - 0009
     - 00145
     - Ambulatory Status
   * - 35
     - ``gt1_35``
     - 4
     - str
     - O
     - 0171
     - 00129
     - Citizenship
   * - 36
     - ``gt1_36``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0215
     - 00743
     - Publicity Indicator
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
     - 3
     - str
     - O
     - 0006
     - 00120
     - Religion
   * - 42
     - ``gt1_42``
     -
     - :ref:`XPN <hl7-v2_3-XPN>`
     - O
     -
     - 00746
     - Mother’s Maiden Name
   * - 43
     - ``gt1_43``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0212
     - 00739
     - Nationality Code
   * - 44
     - ``gt1_44``
     - 1
     - str
     - O
     - 0189
     - 00125
     - Ethnic Group
   * - 45
     - ``gt1_45``
     -
     - list[:ref:`XPN <hl7-v2_3-XPN>`]
     - O
     -
     - 00748
     - Contact Person's Name
   * - 46
     - ``gt1_46``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00749
     - Contact Person’s Telephone Number
   * - 47
     - ``gt1_47``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0222
     - 00747
     - Contact Reason
   * - 48
     - ``gt1_48``
     - 2
     - str
     - O
     - 0063
     - 00784
     - Contact Relationship Code
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
     - :ref:`JCC <hl7-v2_3-JCC>`
     - O
     -
     - 00786
     - Job Code/Class
   * - 51
     - ``gt1_51``
     -
     - list[:ref:`XON <hl7-v2_3-XON>`]
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
     - :ref:`FC <hl7-v2_3-FC>`
     - O
     - 0064
     - 01231
     - Guarantor Financial Class
   * - 55
     - ``gt1_55``
     - 1
     - str
     - O
     - 0005
     - 01291
     - Guarantor Race

.. _hl7-v2_3-IN1:

IN1: Insurance
~~~~~~~~~~~~~~

Section 6.4.6

.. py:class:: hl7types.hl7.v2_3.segments.IN1.IN1
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
     - Set ID - Insurance
   * - 2
     - ``in1_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0072
     - 00368
     - Insurance Plan ID
   * - 3
     - ``in1_3``
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - R
     -
     - 00428
     - Insurance Company ID
   * - 4
     - ``in1_4``
     -
     - :ref:`XON <hl7-v2_3-XON>`
     - O
     -
     - 00429
     - Insurance Company Name
   * - 5
     - ``in1_5``
     -
     - :ref:`XAD <hl7-v2_3-XAD>`
     - O
     -
     - 00430
     - Insurance Company Address
   * - 6
     - ``in1_6``
     -
     - :ref:`XPN <hl7-v2_3-XPN>`
     - O
     -
     - 00431
     - Insurance Co. Contact Ppers
   * - 7
     - ``in1_7``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
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
     - :ref:`XON <hl7-v2_3-XON>`
     - O
     -
     - 00434
     - Group Name
   * - 10
     - ``in1_10``
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 00435
     - Insured's group employer ID
   * - 11
     - ``in1_11``
     -
     - :ref:`XON <hl7-v2_3-XON>`
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
     - str
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
     - :ref:`XPN <hl7-v2_3-XPN>`
     - O
     -
     - 00441
     - Name of Insured
   * - 17
     - ``in1_17``
     - 2
     - str
     - O
     - 0063
     - 00442
     - Insured's Relationship to Patient
   * - 18
     - ``in1_18``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00443
     - Insured's Date of Birth
   * - 19
     - ``in1_19``
     -
     - :ref:`XAD <hl7-v2_3-XAD>`
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
     - Assignment of Benefits
   * - 21
     - ``in1_21``
     - 2
     - str
     - O
     - 0173
     - 00446
     - Coordination of Benefits
   * - 22
     - ``in1_22``
     - 2
     - str
     - O
     -
     - 00447
     - Coord of Ben. Priority
   * - 23
     - ``in1_23``
     - 2
     - str
     - O
     - 0136
     - 00448
     - Notice of Admission Code
   * - 24
     - ``in1_24``
     - 8
     - str
     - O
     -
     - 00449
     - Notice of Admission Date
   * - 25
     - ``in1_25``
     - 2
     - str
     - O
     - 0136
     - 00450
     - Rpt of Eigibility Code
   * - 26
     - ``in1_26``
     - 8
     - str
     - O
     -
     - 00451
     - Rpt of Eligibility Date
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00454
     - Verification Date/Time
   * - 30
     - ``in1_30``
     -
     - :ref:`XPN <hl7-v2_3-XPN>`
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
     - Type of Agreement Code
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
     - Delay before lifetime reserve days
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
     - :ref:`CP <hl7-v2_3-CP>`
     - O
     -
     - 00462
     - Policy Deductible
   * - 38
     - ``in1_38``
     -
     - :ref:`CP <hl7-v2_3-CP>`
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
     - :ref:`CP <hl7-v2_3-CP>`
     - O
     -
     - 00465
     - Room Rate - Semi-Private
   * - 41
     - ``in1_41``
     -
     - :ref:`CP <hl7-v2_3-CP>`
     - O
     -
     - 00466
     - Room Rate - Private
   * - 42
     - ``in1_42``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - Insured's Sex
   * - 44
     - ``in1_44``
     -
     - :ref:`XAD <hl7-v2_3-XAD>`
     - O
     -
     - 00469
     - Insured's Employer Address
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
     - 01277
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
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 01230
     - Insured's ID Number

.. _hl7-v2_3-IN2:

IN2: Insurance additional info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.7

.. py:class:: hl7types.hl7.v2_3.segments.IN2.IN2
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
     - :ref:`CX <hl7-v2_3-CX>`
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
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 00474
     - Insured's Employer Name
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
     - str
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
     - :ref:`XPN <hl7-v2_3-XPN>`
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
     - :ref:`XPN <hl7-v2_3-XPN>`
     - O
     -
     - 00480
     - Champus Sponsor Name
   * - 10
     - ``in2_10``
     - 20
     - str
     - O
     -
     - 00481
     - Champus ID Number
   * - 11
     - ``in2_11``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00482
     - Dependent of Champus Recipient
   * - 12
     - ``in2_12``
     - 25
     - str
     - O
     -
     - 00483
     - Champus Organization
   * - 13
     - ``in2_13``
     - 25
     - str
     - O
     -
     - 00484
     - Champus Station
   * - 14
     - ``in2_14``
     - 14
     - str
     - O
     - 0140
     - 00485
     - Champus Service
   * - 15
     - ``in2_15``
     - 2
     - str
     - O
     - 0141
     - 00486
     - Champus Rank/Grade
   * - 16
     - ``in2_16``
     - 3
     - str
     - O
     - 0142
     - 00487
     - Champus Status
   * - 17
     - ``in2_17``
     - 8
     - str
     - O
     -
     - 00488
     - Champus Retire Date
   * - 18
     - ``in2_18``
     - 1
     - str
     - O
     - 0136
     - 00489
     - Champus Non-Avail Cert on File
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
     - :ref:`XPN <hl7-v2_3-XPN>`
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
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 00496
     - Payor ID
   * - 26
     - ``in2_26``
     -
     - :ref:`CX <hl7-v2_3-CX>`
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
     - list[str]
     - O
     -
     - 00499
     - Room Coverage Type/Amount
   * - 29
     - ``in2_29``
     -
     - list[str]
     - O
     -
     - 00500
     - Policy Type/Amount
   * - 30
     - ``in2_30``
     -
     - str
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
     - str
     - O
     - 0009
     - 00145
     - Ambulatory Status
   * - 33
     - ``in2_33``
     - 4
     - str
     - O
     - 0171
     - 00129
     - Citizenship
   * - 34
     - ``in2_34``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0215
     - 00743
     - Publicity Indicator
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
     - 3
     - str
     - O
     - 0006
     - 00120
     - Religion
   * - 40
     - ``in2_40``
     -
     - :ref:`XPN <hl7-v2_3-XPN>`
     - O
     -
     - 00746
     - Mother’s Maiden Name
   * - 41
     - ``in2_41``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0212
     - 00739
     - Nationality Code
   * - 42
     - ``in2_42``
     - 1
     - str
     - O
     - 0189
     - 00125
     - Ethnic Group
   * - 43
     - ``in2_43``
     - 1
     - list[str]
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
     - Employment Start Date
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
     - :ref:`JCC <hl7-v2_3-JCC>`
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
     - list[:ref:`XPN <hl7-v2_3-XPN>`]
     - O
     -
     - 00789
     - Employer Contact Person Name
   * - 50
     - ``in2_50``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
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
     - list[:ref:`XPN <hl7-v2_3-XPN>`]
     - O
     -
     - 00792
     - Insured’s Contact Person’s Name
   * - 53
     - ``in2_53``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00793
     - Insured’s Contact Person Telephone Number
   * - 54
     - ``in2_54``
     - 2
     - list[str]
     - O
     - 0222
     - 00794
     - Insured’s Contact Person Reason
   * - 55
     - ``in2_55``
     - 8
     - str
     - O
     -
     - 00795
     - Relationship To The Patient Start Date
   * - 56
     - ``in2_56``
     - 8
     - list[str]
     - O
     -
     - 00796
     - Relationship To The Patient Stop Date
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
     - :ref:`XTN <hl7-v2_3-XTN>`
     - O
     -
     - 00798
     - Insurance Co. Contact Phone Number
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
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 00801
     - Patient Member Number
   * - 62
     - ``in2_62``
     - 2
     - str
     - O
     - 0063
     - 00802
     - Guarantor’s Relationship To Insured
   * - 63
     - ``in2_63``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00803
     - Insured’s Telephone Number - Home
   * - 64
     - ``in2_64``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00804
     - Insured’s Employer Telephone Number
   * - 65
     - ``in2_65``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00805
     - Military Handicapped Program
   * - 66
     - ``in2_66``
     - 2
     - str
     - O
     - 0136
     - 00806
     - Suspend Flag
   * - 67
     - ``in2_67``
     - 2
     - str
     - O
     - 0136
     - 00807
     - Co-pay Limit Flag
   * - 68
     - ``in2_68``
     - 2
     - str
     - O
     - 0136
     - 00808
     - Stoploss Limit Flag
   * - 69
     - ``in2_69``
     -
     - list[:ref:`XON <hl7-v2_3-XON>`]
     - O
     -
     - 00809
     - Insured Organization Name And ID
   * - 70
     - ``in2_70``
     -
     - list[:ref:`XON <hl7-v2_3-XON>`]
     - O
     -
     - 00810
     - Insured Employer Organization Name And ID
   * - 71
     - ``in2_71``
     - 1
     - str
     - O
     - 0005
     - 00113
     - Race
   * - 72
     - ``in2_72``
     - 1
     - str
     - O
     -
     - 00811
     - Patient Relationship to Insured

.. _hl7-v2_3-IN3:

IN3: Insurance additional info - certification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.8

.. py:class:: hl7types.hl7.v2_3.segments.IN3.IN3
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
     - Set ID - Insurance Certification
   * - 2
     - ``in3_2``
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 00503
     - Certification Number
   * - 3
     - ``in3_3``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
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
     - str
     - O
     - 0148
     - 00506
     - Penalty
   * - 6
     - ``in3_6``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00507
     - Certification Date/Time
   * - 7
     - ``in3_7``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00508
     - Certification Modify Date/Time
   * - 8
     - ``in3_8``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
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
     - str
     - O
     - 0149
     - 00512
     - Days
   * - 12
     - ``in3_12``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0233
     - 00513
     - Non-Concur Code/Description
   * - 13
     - ``in3_13``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00514
     - Non-Concur Effective Date/Time
   * - 14
     - ``in3_14``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
     - O
     -
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
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00517
     - Certification Contact Phone Number
   * - 17
     - ``in3_17``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00518
     - Appeal Reason
   * - 18
     - ``in3_18``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00519
     - Certification Agency
   * - 19
     - ``in3_19``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00520
     - Certification Agency Phone Number
   * - 20
     - ``in3_20``
     -
     - list[str]
     - O
     -
     - 00521
     - Pre-Certification required/Window
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
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
     - O
     -
     - 00526
     - Second Opinion Physician

.. _hl7-v2_3-LCC:

LCC: Location Charge Code
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.8.6

.. py:class:: hl7types.hl7.v2_3.segments.LCC.LCC
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
     - :ref:`PL <hl7-v2_3-PL>`
     - R
     -
     - 00979
     - Primary Key Value
   * - 2
     - ``lcc_2``
     - 10
     - str
     - R
     - 0264
     - 00964
     - Location Department
   * - 3
     - ``lcc_3``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00980
     - Accommodation Type
   * - 4
     - ``lcc_4``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - R
     -
     - 00981
     - Charge Code

.. _hl7-v2_3-LCH:

LCH: Location Characteristic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.8.3

.. py:class:: hl7types.hl7.v2_3.segments.LCH.LCH
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
     - :ref:`PL <hl7-v2_3-PL>`
     - R
     -
     - 00943
     - Primary Key Value
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
     - :ref:`EI <hl7-v2_3-EI>`
     - O
     -
     - 00764
     - Segment Unique Key
   * - 4
     - ``lch_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     - 0324
     - 01295
     - Location Characteristic ID
   * - 5
     - ``lch_5``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 01294
     - Location Characteristic Value

.. _hl7-v2_3-LDP:

LDP: Location Department
~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.8.5

.. py:class:: hl7types.hl7.v2_3.segments.LDP.LDP
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
     - :ref:`PL <hl7-v2_3-PL>`
     - R
     -
     - 00963
     - LDP Primary Key Value
   * - 2
     - ``ldp_2``
     - 10
     - str
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     - 0265
     - 00966
     - Speciality Type
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00969
     - Activation Date
   * - 8
     - ``ldp_8``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - list[:ref:`VH <hl7-v2_3-VH>`]
     - O
     - 0267
     - 00976
     - Visiting Hours
   * - 11
     - ``ldp_11``
     -
     - :ref:`XTN <hl7-v2_3-XTN>`
     - O
     -
     - 00978
     - Contact Phone

.. _hl7-v2_3-LOC:

LOC: Location Identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.8.2

.. py:class:: hl7types.hl7.v2_3.segments.LOC.LOC
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
     - :ref:`PL <hl7-v2_3-PL>`
     - R
     -
     - 00943
     - Primary Key Value
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
     - Location Type
   * - 4
     - ``loc_4``
     -
     - :ref:`XON <hl7-v2_3-XON>`
     - O
     -
     - 00947
     - Organization Name
   * - 5
     - ``loc_5``
     -
     - :ref:`XAD <hl7-v2_3-XAD>`
     - O
     -
     - 00948
     - Location Address
   * - 6
     - ``loc_6``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00949
     - Location Phone
   * - 7
     - ``loc_7``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
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

.. _hl7-v2_3-LRL:

LRL: Location Relationship
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.8.4

.. py:class:: hl7types.hl7.v2_3.segments.LRL.LRL
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
     - :ref:`PL <hl7-v2_3-PL>`
     - R
     -
     - 00943
     - Primary Key Value
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
     - :ref:`EI <hl7-v2_3-EI>`
     - O
     -
     - 00764
     - Segment Unique Key
   * - 4
     - ``lrl_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0325
     - 01227
     - Location Relationship ID
   * - 5
     - ``lrl_5``
     -
     - :ref:`XON <hl7-v2_3-XON>`
     - C
     -
     - 01301
     - Organizational Location Relationship Value
   * - 6
     - ``lrl_6``
     -
     - :ref:`PL <hl7-v2_3-PL>`
     - O
     -
     - 01292
     - Patient Location Relationship Value

.. _hl7-v2_3-MFA:

MFA: Master file acknowledgement segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.4.3

.. py:class:: hl7types.hl7.v2_3.segments.MFA.MFA
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00668
     - Event Completion Date/Time
   * - 4
     - ``mfa_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     - 0181
     - 00669
     - Error Return Code and/or Text
   * - 5
     - ``mfa_5``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - R
     -
     - 00667
     - Primary Key Value

.. _hl7-v2_3-MFE:

MFE: Master file entry segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.4.2

.. py:class:: hl7types.hl7.v2_3.segments.MFE.MFE
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00662
     - Effective Date/Time
   * - 4
     - ``mfe_4``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - R
     -
     - 00667
     - Primary Key Value

.. _hl7-v2_3-MFI:

MFI: Master file identification segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.4.1

.. py:class:: hl7types.hl7.v2_3.segments.MFI.MFI
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     - 0175
     - 00658
     - Master File Identifier
   * - 2
     - ``mfi_2``
     -
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - 0176
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00661
     - Entered Date/Time
   * - 5
     - ``mfi_5``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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

.. _hl7-v2_3-MRG:

MRG: Merge patient information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.8

.. py:class:: hl7types.hl7.v2_3.segments.MRG.MRG
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
     - list[:ref:`CX <hl7-v2_3-CX>`]
     - R
     -
     - 00211
     - Prior Patient ID - Internal
   * - 2
     - ``mrg_2``
     -
     - list[:ref:`CX <hl7-v2_3-CX>`]
     - O
     -
     - 00212
     - Prior Alternate Patient ID
   * - 3
     - ``mrg_3``
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 00213
     - Prior Patient Account Number
   * - 4
     - ``mrg_4``
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 00214
     - Prior Patient ID - External
   * - 5
     - ``mrg_5``
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 01279
     - Prior Visit Number
   * - 6
     - ``mrg_6``
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 01280
     - Prior Alternate Visit ID
   * - 7
     - ``mrg_7``
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 01281
     - Prior Patient Name

.. _hl7-v2_3-MSA:

MSA: Message acknowledgement segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.2

.. py:class:: hl7types.hl7.v2_3.segments.MSA.MSA
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
     - Delayed Acknowledgement Type
   * - 6
     - ``msa_6``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00023
     - Error Condition

.. _hl7-v2_3-MSH:

MSH: Message header segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.1

.. py:class:: hl7types.hl7.v2_3.segments.MSH.MSH
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
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     -
     - 00003
     - Sending Application
   * - 4
     - ``msh_4``
     -
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     -
     - 00004
     - Sending Facility
   * - 5
     - ``msh_5``
     -
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     -
     - 00005
     - Receiving Application
   * - 6
     - ``msh_6``
     -
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     -
     - 00006
     - Receiving Facility
   * - 7
     - ``msh_7``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00007
     - Date / Time of Message
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
     - :ref:`PT <hl7-v2_3-PT>`
     - R
     -
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
     - Accept Acknowledgement Type
   * - 16
     - ``msh_16``
     - 2
     - str
     - O
     - 0155
     - 00016
     - Application Acknowledgement Type
   * - 17
     - ``msh_17``
     - 2
     - str
     - O
     -
     - 00017
     - Country Code
   * - 18
     - ``msh_18``
     - 6
     - str
     - O
     - 0211
     - 00692
     - Character Set
   * - 19
     - ``msh_19``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00693
     - Principal Language of Message

.. _hl7-v2_3-NCK:

NCK: System Clock
~~~~~~~~~~~~~~~~~

Section C.2.1

.. py:class:: hl7types.hl7.v2_3.segments.NCK.NCK
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01172
     - System Date/Time

.. _hl7-v2_3-NK1:

NK1: Next of kin
~~~~~~~~~~~~~~~~

Section 3.3.5

.. py:class:: hl7types.hl7.v2_3.segments.NK1.NK1
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
     - list[:ref:`XPN <hl7-v2_3-XPN>`]
     - O
     -
     - 00191
     - Name
   * - 3
     - ``nk1_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0063
     - 00192
     - Relationship
   * - 4
     - ``nk1_4``
     -
     - list[:ref:`XAD <hl7-v2_3-XAD>`]
     - O
     -
     - 00193
     - Address
   * - 5
     - ``nk1_5``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00194
     - Phone Number
   * - 6
     - ``nk1_6``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00195
     - Business Phone Number
   * - 7
     - ``nk1_7``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
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
     - Next of Kin/Associated Parties Job Title
   * - 11
     - ``nk1_11``
     -
     - :ref:`JCC <hl7-v2_3-JCC>`
     - O
     -
     - 00200
     - Next of Kin Job/Associated Parties Code/Class
   * - 12
     - ``nk1_12``
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 00201
     - Next of Kin/Associated Parties Employee Number
   * - 13
     - ``nk1_13``
     -
     - list[:ref:`XON <hl7-v2_3-XON>`]
     - O
     -
     - 00202
     - Organization Name
   * - 14
     - ``nk1_14``
     - 1
     - list[str]
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
     - Sex
   * - 16
     - ``nk1_16``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00110
     - Date of Birth
   * - 17
     - ``nk1_17``
     - 2
     - str
     - O
     - 0223
     - 00755
     - Living Dependency
   * - 18
     - ``nk1_18``
     - 2
     - str
     - O
     - 0009
     - 00145
     - Ambulatory Status
   * - 19
     - ``nk1_19``
     - 4
     - str
     - O
     - 0171
     - 00129
     - Citizenship
   * - 20
     - ``nk1_20``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0215
     - 00743
     - Publicity Indicator
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
     - 3
     - str
     - O
     - 0006
     - 00120
     - Religion
   * - 26
     - ``nk1_26``
     -
     - :ref:`XPN <hl7-v2_3-XPN>`
     - O
     -
     - 00746
     - Mother’s Maiden Name
   * - 27
     - ``nk1_27``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0212
     - 00739
     - Nationality Code
   * - 28
     - ``nk1_28``
     - 1
     - str
     - O
     - 0189
     - 00125
     - Ethnic Group
   * - 29
     - ``nk1_29``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0222
     - 00747
     - Contact Reason
   * - 30
     - ``nk1_30``
     -
     - list[:ref:`XPN <hl7-v2_3-XPN>`]
     - O
     -
     - 00748
     - Contact Person's Name
   * - 31
     - ``nk1_31``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00749
     - Contact Person’s Telephone Number
   * - 32
     - ``nk1_32``
     -
     - list[:ref:`XAD <hl7-v2_3-XAD>`]
     - O
     -
     - 00750
     - Contact Person’s Address
   * - 33
     - ``nk1_33``
     -
     - list[:ref:`CX <hl7-v2_3-CX>`]
     - O
     -
     - 00751
     - Associated Party’s Identifiers
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
     - 1
     - str
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

.. _hl7-v2_3-NPU:

NPU: Bed status update
~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.7

.. py:class:: hl7types.hl7.v2_3.segments.NPU.NPU
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
     - :ref:`PL <hl7-v2_3-PL>`
     - R
     - HL70079
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

.. _hl7-v2_3-NSC:

NSC: STATUS CHANGE
~~~~~~~~~~~~~~~~~~

Section C.2.3

.. py:class:: hl7types.hl7.v2_3.segments.NSC.NSC
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
     - O
     -
     - 01188
     - Network Change Type
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
     - 30
     - str
     - O
     -
     - 01191
     - Current Application
   * - 5
     - ``nsc_5``
     - 30
     - str
     - O
     -
     - 01192
     - Current Facility
   * - 6
     - ``nsc_6``
     - 30
     - str
     - C
     - 0206
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
     - 30
     - str
     - O
     -
     - 01195
     - New Application

.. _hl7-v2_3-NST:

NST: Statistics
~~~~~~~~~~~~~~~

Section C.2.2

.. py:class:: hl7types.hl7.v2_3.segments.NST.NST
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
     - O
     - 0125
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
     -
     - 01175
     - Source Type
   * - 4
     - ``nst_4``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01176
     - Statistics Start
   * - 5
     - ``nst_5``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - Network Errors

.. _hl7-v2_3-NTE:

NTE: Notes and comments segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.15

.. py:class:: hl7types.hl7.v2_3.segments.NTE.NTE
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

.. _hl7-v2_3-OBR:

OBR: Observation request segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.5.1

.. py:class:: hl7types.hl7.v2_3.segments.OBR.OBR
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
     - C
     -
     - 00237
     - Set ID - Observation Request
   * - 2
     - ``obr_2``
     -
     - list[:ref:`EI <hl7-v2_3-EI>`]
     - C
     -
     - 00216
     - Placer Order Number
   * - 3
     - ``obr_3``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - C
     -
     - 00217
     - Filler Order Number
   * - 4
     - ``obr_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - Priority
   * - 6
     - ``obr_6``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00240
     - Requested Date/Time
   * - 7
     - ``obr_7``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - C
     -
     - 00241
     - Observation Date/Time
   * - 8
     - ``obr_8``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00242
     - Observation End Date/Time
   * - 9
     - ``obr_9``
     -
     - :ref:`CQ <hl7-v2_3-CQ>`
     - O
     -
     - 00243
     - Collection Volume
   * - 10
     - ``obr_10``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00246
     - Danger Code
   * - 13
     - ``obr_13``
     - 300
     - str
     - C
     -
     - 00247
     - Relevant Clinical Information
   * - 14
     - ``obr_14``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00248
     - Specimen Received Date/Time
   * - 15
     - ``obr_15``
     -
     - str
     - O
     - 0070
     - 00249
     - Specimen Source
   * - 16
     - ``obr_16``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
     - O
     -
     - 00226
     - Ordering Provider
   * - 17
     - ``obr_17``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
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
     - :ref:`TS <hl7-v2_3-TS>`
     - C
     -
     - 00255
     - Results Rpt/Status Chng - Date/Time
   * - 23
     - ``obr_23``
     -
     - str
     - O
     -
     - 00256
     - Charge To Practice
   * - 24
     - ``obr_24``
     - 10
     - str
     - C
     - 0074
     - 00257
     - Diagnostic Service Section ID
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
     - :ref:`TQ <hl7-v2_3-TQ>`
     - O
     -
     - 00221
     - Quantity/Timing
   * - 28
     - ``obr_28``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00263
     - Reason For Study
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
     - :ref:`TS <hl7-v2_3-TS>`
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
     - Number Of Sample Containers
   * - 38
     - ``obr_38``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 01029
     - Transport Logistics Of Collected Sample
   * - 39
     - ``obr_39``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 01030
     - Collector’s Comment
   * - 40
     - ``obr_40``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 01034
     - Planned Patient Transport Comment

.. _hl7-v2_3-OBX:

OBX: Observation segment
~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.2

.. py:class:: hl7types.hl7.v2_3.segments.OBX.OBX
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
     - R
     - 0125
     - 00570
     - Value Type
   * - 3
     - ``obx_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00574
     - Units
   * - 7
     - ``obx_7``
     - 10
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
     - str
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
     - Observ Result Status
   * - 12
     - ``obx_12``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - C
     -
     - 00580
     - Date Last Obs Normal Values
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00582
     - Date/Time of the Observation
   * - 15
     - ``obx_15``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     -
     - 00583
     - Producer's ID
   * - 16
     - ``obx_16``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 00584
     - Responsible Observer
   * - 17
     - ``obx_17``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00936
     - Observation Method

.. _hl7-v2_3-ODS:

ODS: Dietary orders, supplements, and preferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.6.1

.. py:class:: hl7types.hl7.v2_3.segments.ODS.ODS
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00270
     - Service Period
   * - 3
     - ``ods_3``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - R
     -
     - 00271
     - Diet, Supplement, or Preference Code
   * - 4
     - ``ods_4``
     - 80
     - str
     - O
     -
     - 00272
     - Text Instruction

.. _hl7-v2_3-ODT:

ODT: Diet tray instructions segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.6.2

.. py:class:: hl7types.hl7.v2_3.segments.ODT.ODT
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     - 0160
     - 00273
     - Tray Type
   * - 2
     - ``odt_2``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
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

.. _hl7-v2_3-OM1:

OM1: General - fields that apply to most observations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.7.3

.. py:class:: hl7types.hl7.v2_3.segments.OM1.OM1
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
     - O
     -
     - 00586
     - Sequence Number - Test/ Observation Master File
   * - 2
     - ``om1_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00587
     - Producer's Test/Observation ID
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00590
     - Producer ID
   * - 6
     - ``om1_6``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00591
     - Observation Description
   * - 7
     - ``om1_7``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00592
     - Other Test/Observation IDs for the Observation
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00598
     - Identity of Instrument Used to Perfrom this Study
   * - 14
     - ``om1_14``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00599
     - Coded Representation of Method
   * - 15
     - ``om1_15``
     - 1
     - str
     - O
     - 0136
     - 00600
     - Portable
   * - 16
     - ``om1_16``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00601
     - Observation Producing Department/Section
   * - 17
     - ``om1_17``
     - 40
     - str
     - O
     -
     - 00602
     - Telephone Number of Section
   * - 18
     - ``om1_18``
     - 1
     - str
     - O
     - 0174
     - 00603
     - Nature of Test/Observation
   * - 19
     - ``om1_19``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00606
     - Date/Time Stamp for any change in Def Attri for Obs
   * - 22
     - ``om1_22``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00607
     - Effective Date/Time of Change in Test Proc. that make Results Non-Comparable
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00612
     - Outside Site(s) Where Observation may be Performed
   * - 28
     - ``om1_28``
     -
     - :ref:`AD <hl7-v2_3-AD>`
     - O
     -
     - 00613
     - Address of Outside Site(s)
   * - 29
     - ``om1_29``
     - 400
     - str
     - O
     -
     - 00614
     - Phone Number of Outside Site
   * - 30
     - ``om1_30``
     - 1
     - str
     - O
     - 0177
     - 00615
     - Confidentiality Code
   * - 31
     - ``om1_31``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00618
     - Contraindications to Observations
   * - 34
     - ``om1_34``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00619
     - Reflex Tests/Observations
   * - 35
     - ``om1_35``
     - 80
     - str
     - O
     -
     - 00620
     - Rules that Trigger Reflex Testing
   * - 36
     - ``om1_36``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00623
     - Procedure Medication
   * - 39
     - ``om1_39``
     -
     - str
     - O
     -
     - 00624
     - Factors that may Effect the Observation
   * - 40
     - ``om1_40``
     - 60
     - list[str]
     - O
     -
     - 00625
     - Test/Observation Performance Schedule
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00937
     - Kind of Quantity Observed
   * - 43
     - ``om1_43``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00938
     - Point versus Interval
   * - 44
     - ``om1_44``
     -
     - str
     - O
     -
     - 00939
     - Challenge information
   * - 45
     - ``om1_45``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00940
     - Relationship modifier
   * - 46
     - ``om1_46``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00941
     - Target anatomic site of test
   * - 47
     - ``om1_47``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00942
     - Modality of imaging measurement

.. _hl7-v2_3-OM2:

OM2: Numeric observation
~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.7.4

.. py:class:: hl7types.hl7.v2_3.segments.OM2.OM2
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
     - Sequence Number - Test/ Observation Master File
   * - 2
     - ``om2_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
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
     - str
     - O
     -
     - 00631
     - Reference (Normal) Range - Ordinal & Continuous Obs
   * - 7
     - ``om2_7``
     -
     - str
     - O
     -
     - 00632
     - Critical Range for Ordinal & Continuous Obs
   * - 8
     - ``om2_8``
     -
     - str
     - O
     -
     - 00633
     - Absolute Range for Ordinal & Continuous Obs
   * - 9
     - ``om2_9``
     -
     - list[str]
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

.. _hl7-v2_3-OM3:

OM3: Categorical test/observation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.7.5

.. py:class:: hl7types.hl7.v2_3.segments.OM3.OM3
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
     - Sequence Number - Test/ Observation Master File
   * - 2
     - ``om3_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00636
     - Preferred Coding System
   * - 3
     - ``om3_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00637
     - Valid Coded "Answers"
   * - 4
     - ``om3_4``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00638
     - Normal Text/Codes for Categorical Observations
   * - 5
     - ``om3_5``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00639
     - Abnormal Text/Codes for Categorical Observations
   * - 6
     - ``om3_6``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00640
     - Critical Text Codes for Categorical Observations
   * - 7
     - ``om3_7``
     - 2
     - str
     - R
     - 0125
     - 00570
     - Value Type

.. _hl7-v2_3-OM4:

OM4: Observations that require specimens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.7.6

.. py:class:: hl7types.hl7.v2_3.segments.OM4.OM4
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
     - Sequence Number - Test/ Observation Master File
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00645
     - Container Units
   * - 6
     - ``om4_6``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00646
     - Specimen
   * - 7
     - ``om4_7``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
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
     - :ref:`CQ <hl7-v2_3-CQ>`
     - O
     -
     - 00650
     - Normal Collection Volume
   * - 11
     - ``om4_11``
     -
     - :ref:`CQ <hl7-v2_3-CQ>`
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
     - str
     - O
     - 0027
     - 00653
     - Specimen Priorities
   * - 14
     - ``om4_14``
     -
     - :ref:`CQ <hl7-v2_3-CQ>`
     - O
     -
     - 00654
     - Specimen Retention Time

.. _hl7-v2_3-OM5:

OM5: Observation batteries
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.7.7

.. py:class:: hl7types.hl7.v2_3.segments.OM5.OM5
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
     - Sequence Number - Test/ Observation Master File
   * - 2
     - ``om5_2``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00655
     - Test/Observations Included w/an Ordered Test Battery
   * - 3
     - ``om5_3``
     - 200
     - str
     - O
     -
     - 00656
     - Observation ID Suffixes

.. _hl7-v2_3-OM6:

OM6: Observations that are calculated from other observations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.7.8

.. py:class:: hl7types.hl7.v2_3.segments.OM6.OM6
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
     - Sequence Number - Test/ Observation Master File
   * - 2
     - ``om6_2``
     -
     - str
     - O
     -
     - 00657
     - Derivation Rule

.. _hl7-v2_3-ORC:

ORC: Common order segment
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.3.1

.. py:class:: hl7types.hl7.v2_3.segments.ORC.ORC
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
     - list[:ref:`EI <hl7-v2_3-EI>`]
     - O
     -
     - 00216
     - Placer Order Number
   * - 3
     - ``orc_3``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - C
     -
     - 00217
     - Filler Order Number
   * - 4
     - ``orc_4``
     -
     - :ref:`EI <hl7-v2_3-EI>`
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
     - :ref:`TQ <hl7-v2_3-TQ>`
     - R
     -
     - 00221
     - Quantity/Timing
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00223
     - Date/Time of Transaction
   * - 10
     - ``orc_10``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 00224
     - Entered By
   * - 11
     - ``orc_11``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 00225
     - Verified By
   * - 12
     - ``orc_12``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
     - O
     -
     - 00226
     - Ordering Provider
   * - 13
     - ``orc_13``
     -
     - :ref:`PL <hl7-v2_3-PL>`
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00229
     - Order Effective Date/Time
   * - 16
     - ``orc_16``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00230
     - Order Control Code Reason
   * - 17
     - ``orc_17``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00231
     - Entering Organization
   * - 18
     - ``orc_18``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00232
     - Entering Device
   * - 19
     - ``orc_19``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 00233
     - Action By

.. _hl7-v2_3-PCR:

PCR: Possible Causal Relationship
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.11.3

.. py:class:: hl7types.hl7.v2_3.segments.PCR.PCR
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01100
     - Product Class
   * - 4
     - ``pcr_4``
     -
     - :ref:`CQ <hl7-v2_3-CQ>`
     - O
     -
     - 01101
     - Total Duration Of Therapy
   * - 5
     - ``pcr_5``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01102
     - Product Manufacture Date
   * - 6
     - ``pcr_6``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01103
     - Product Expiration Date
   * - 7
     - ``pcr_7``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01104
     - Product Implantation Date
   * - 8
     - ``pcr_8``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01111
     - Product Evaluation Performed
   * - 15
     - ``pcr_15``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0247
     - 01112
     - Product Evaluation Status
   * - 16
     - ``pcr_16``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`TS <hl7-v2_3-TS>`
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
     - 8
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
     - 0232
     - 01119
     - Event Causality Observations
   * - 23
     - ``pcr_23``
     - 2
     - list[str]
     - O
     - 0253
     - 01120
     - Indirect Exposure Mechanism

.. _hl7-v2_3-PD1:

PD1: Patient Demographic
~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.9

.. py:class:: hl7types.hl7.v2_3.segments.PD1.PD1
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
     - str
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
     - list[:ref:`XON <hl7-v2_3-XON>`]
     - O
     -
     - 00756
     - Patient Primary Facility
   * - 4
     - ``pd1_4``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
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
     - Living Will
   * - 8
     - ``pd1_8``
     - 2
     - str
     - O
     - 0316
     - 00760
     - Organ Donor
   * - 9
     - ``pd1_9``
     - 2
     - str
     - O
     - 0136
     - 00761
     - Separate Bill
   * - 10
     - ``pd1_10``
     -
     - list[:ref:`CX <hl7-v2_3-CX>`]
     - O
     -
     - 00762
     - Duplicate Patient
   * - 11
     - ``pd1_11``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0215
     - 00743
     - Publicity Indicator
   * - 12
     - ``pd1_12``
     - 1
     - str
     - O
     - 0136
     - 00744
     - Protection Indicator

.. _hl7-v2_3-PDC:

PDC: Product Detail Country
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.11.5

.. py:class:: hl7types.hl7.v2_3.segments.PDC.PDC
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
     - :ref:`XON <hl7-v2_3-XON>`
     - R
     -
     - 01247
     - Manufacturer/Distributor
   * - 2
     - ``pdc_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - Marketing Approval Identifier
   * - 12
     - ``pdc_12``
     -
     - :ref:`CQ <hl7-v2_3-CQ>`
     - O
     -
     - 01258
     - Labeled Shelf Life
   * - 13
     - ``pdc_13``
     -
     - :ref:`CQ <hl7-v2_3-CQ>`
     - O
     -
     - 01259
     - Expected Shelf Life
   * - 14
     - ``pdc_14``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01260
     - Date First Marked
   * - 15
     - ``pdc_15``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01261
     - Date Last Marked

.. _hl7-v2_3-PEO:

PEO: Product Experience Observation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.11.2

.. py:class:: hl7types.hl7.v2_3.segments.PEO.PEO
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 01073
     - Event Identifiers Used
   * - 2
     - ``peo_2``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 01074
     - Event Symptom/Diagnosis Code
   * - 3
     - ``peo_3``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - R
     -
     - 01075
     - Event Onset Date/Time
   * - 4
     - ``peo_4``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01076
     - Event Exacerbation Date/Time
   * - 5
     - ``peo_5``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01077
     - Event Improved Date/Time
   * - 6
     - ``peo_6``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01078
     - Event Ended Data/Time
   * - 7
     - ``peo_7``
     -
     - :ref:`XAD <hl7-v2_3-XAD>`
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 01090
     - Cause Of Death
   * - 19
     - ``peo_19``
     -
     - :ref:`XPN <hl7-v2_3-XPN>`
     - O
     -
     - 01091
     - Primary Observer Name
   * - 20
     - ``peo_20``
     -
     - list[:ref:`XAD <hl7-v2_3-XAD>`]
     - O
     -
     - 01092
     - Primary Observer Address
   * - 21
     - ``peo_21``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
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
     - Primary Observer’s Qualification
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
     - :ref:`TS <hl7-v2_3-TS>`
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
     - Primary Observer’s Identity May Be Divulged

.. _hl7-v2_3-PES:

PES: Product Experience Sender
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.11.1

.. py:class:: hl7types.hl7.v2_3.segments.PES.PES
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
     - :ref:`XON <hl7-v2_3-XON>`
     - O
     -
     - 01059
     - Sender Organization Name
   * - 2
     - ``pes_2``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
     - O
     -
     - 01060
     - Sender Individual Name
   * - 3
     - ``pes_3``
     -
     - list[:ref:`XAD <hl7-v2_3-XAD>`]
     - O
     -
     - 01062
     - Sender Address
   * - 4
     - ``pes_4``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 01063
     - Sender Telephone
   * - 5
     - ``pes_5``
     -
     - :ref:`EI <hl7-v2_3-EI>`
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01068
     - Sender Aware Date/Time
   * - 10
     - ``pes_10``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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

.. _hl7-v2_3-PID:

PID: Patient Identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.2

.. py:class:: hl7types.hl7.v2_3.segments.PID.PID
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
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 00105
     - Patient ID (External ID)
   * - 3
     - ``pid_3``
     -
     - list[:ref:`CX <hl7-v2_3-CX>`]
     - R
     -
     - 00106
     - Patient ID (Internal ID)
   * - 4
     - ``pid_4``
     -
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 00107
     - Alternate Patient ID
   * - 5
     - ``pid_5``
     -
     - :ref:`XPN <hl7-v2_3-XPN>`
     - R
     -
     - 00108
     - Patient Name
   * - 6
     - ``pid_6``
     -
     - :ref:`XPN <hl7-v2_3-XPN>`
     - O
     -
     - 00109
     - Mother's Maiden Name
   * - 7
     - ``pid_7``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - list[:ref:`XPN <hl7-v2_3-XPN>`]
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
     - list[:ref:`XAD <hl7-v2_3-XAD>`]
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
     - County Code
   * - 13
     - ``pid_13``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00116
     - Phone Number - Home
   * - 14
     - ``pid_14``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00117
     - Phone Number - Business
   * - 15
     - ``pid_15``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0296
     - 00118
     - Primary Language
   * - 16
     - ``pid_16``
     - 1
     - list[str]
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
     -
     - :ref:`CX <hl7-v2_3-CX>`
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
     - :ref:`DLN <hl7-v2_3-DLN>`
     - O
     -
     - 00123
     - Driver's License Number
   * - 21
     - ``pid_21``
     -
     - :ref:`CX <hl7-v2_3-CX>`
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
     - 60
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
     - 4
     - str
     - O
     - 0171
     - 00129
     - Citizenship
   * - 27
     - ``pid_27``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0172
     - 00130
     - Veterans Military Status
   * - 28
     - ``pid_28``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0212
     - 00739
     - Nationality Code
   * - 29
     - ``pid_29``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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

.. _hl7-v2_3-PR1:

PR1: Procedures
~~~~~~~~~~~~~~~

Section 6.4.4

.. py:class:: hl7types.hl7.v2_3.segments.PR1.PR1
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
     - Set ID - Procedure
   * - 2
     - ``pr1_2``
     - 2
     - str
     - R
     - 0089
     - 00392
     - Procedure Coding Method
   * - 3
     - ``pr1_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00395
     - Procedure Date/Time
   * - 6
     - ``pr1_6``
     - 2
     - str
     - R
     - 0230
     - 00396
     - Procedure Type
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
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
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
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
     - O
     - 0010
     - 00401
     - Surgeon
   * - 12
     - ``pr1_12``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
     - O
     - 0010
     - 00402
     - Procedure Practitioner
   * - 13
     - ``pr1_13``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0059
     - 00403
     - Consent Code
   * - 14
     - ``pr1_14``
     - 2
     - str
     - O
     -
     - 00404
     - Procedure Priority
   * - 15
     - ``pr1_15``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00772
     - Associated Diagnosis Code

.. _hl7-v2_3-PRA:

PRA: Practitioner detail segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.6.3

.. py:class:: hl7types.hl7.v2_3.segments.PRA.PRA
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
     - PRA - Primary Key Value
   * - 2
     - ``pra_2``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00686
     - Practioner Group
   * - 3
     - ``pra_3``
     - 3
     - list[str]
     - O
     -
     - 00687
     - Practioner Category
   * - 4
     - ``pra_4``
     - 1
     - str
     - O
     - 0186
     - 00688
     - Provider Billing
   * - 5
     - ``pra_5``
     -
     - list[str]
     - O
     - 0187
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

.. _hl7-v2_3-PRB:

PRB: Problem Detail
~~~~~~~~~~~~~~~~~~~

Section 12.3.2

.. py:class:: hl7types.hl7.v2_3.segments.PRB.PRB
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
     - :ref:`TS <hl7-v2_3-TS>`
     - R
     -
     - 00817
     - Action Date/Time
   * - 3
     - ``prb_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00838
     - Problem ID
   * - 4
     - ``prb_4``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - R
     -
     - 00839
     - Problem Instance ID
   * - 5
     - ``prb_5``
     -
     - :ref:`EI <hl7-v2_3-EI>`
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00842
     - Problem Established Date/Time
   * - 8
     - ``prb_8``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00843
     - Anticipated Problem Resolution Date/Time
   * - 9
     - ``prb_9``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00844
     - Actual Problem Resolution Date/Time
   * - 10
     - ``prb_10``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00845
     - Problem Classification
   * - 11
     - ``prb_11``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00846
     - Problem Management Discipline
   * - 12
     - ``prb_12``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00847
     - Problem Persistence
   * - 13
     - ``prb_13``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00848
     - Problem Confirmation Status
   * - 14
     - ``prb_14``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00849
     - Problem Life Cycle Status
   * - 15
     - ``prb_15``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00850
     - Problem Life Cycle Status Date/Time
   * - 16
     - ``prb_16``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00853
     - Problem Ranking
   * - 19
     - ``prb_19``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00856
     - Individual Awareness of Problem
   * - 22
     - ``prb_22``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00857
     - Problem Prognosis
   * - 23
     - ``prb_23``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00823
     - Security/Sensitivity

.. _hl7-v2_3-PRC:

PRC: Pricing
~~~~~~~~~~~~

Section 8.9.3

.. py:class:: hl7types.hl7.v2_3.segments.PRC.PRC
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     - 0132
     - 00982
     - Primary Key Value
   * - 2
     - ``prc_2``
     -
     - list[:ref:`EI <hl7-v2_3-EI>`]
     - R
     -
     - 01262
     - Facility ID
   * - 3
     - ``prc_3``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00996
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
     - list[:ref:`CP <hl7-v2_3-CP>`]
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
     - :ref:`MO <hl7-v2_3-MO>`
     - O
     -
     - 01002
     - Minimum Price
   * - 10
     - ``prc_10``
     -
     - :ref:`MO <hl7-v2_3-MO>`
     - O
     -
     - 01003
     - Maximum Price
   * - 11
     - ``prc_11``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01004
     - Effective Start Date
   * - 12
     - ``prc_12``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
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
     - :ref:`MO <hl7-v2_3-MO>`
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

.. _hl7-v2_3-PRD:

PRD: Provider Data
~~~~~~~~~~~~~~~~~~

Section 11.5.3

.. py:class:: hl7types.hl7.v2_3.segments.PRD.PRD
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - R
     - 0286
     - 01155
     - Role
   * - 2
     - ``prd_2``
     -
     - list[:ref:`XPN <hl7-v2_3-XPN>`]
     - O
     -
     - 01156
     - Provider Name
   * - 3
     - ``prd_3``
     -
     - :ref:`XAD <hl7-v2_3-XAD>`
     - O
     -
     - 01157
     - Provider Address
   * - 4
     - ``prd_4``
     -
     - :ref:`PL <hl7-v2_3-PL>`
     - O
     -
     - 01158
     - Provider Location
   * - 5
     - ``prd_5``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 01159
     - Provider Communication Information
   * - 6
     - ``prd_6``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0185
     - 00684
     - Preferred Method of Contact
   * - 7
     - ``prd_7``
     -
     - list[str]
     - O
     -
     - 01162
     - Provider Identifiers
   * - 8
     - ``prd_8``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01163
     - Effective Start Date of Role
   * - 9
     - ``prd_9``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01164
     - Effective End Date of Role

.. _hl7-v2_3-PSH:

PSH: Product Summary Header
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.11.4

.. py:class:: hl7types.hl7.v2_3.segments.PSH.PSH
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
     - 01234
     - Report Form Identifier
   * - 3
     - ``psh_3``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - R
     -
     - 01235
     - Report Date
   * - 4
     - ``psh_4``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01236
     - Report Interval Start Date
   * - 5
     - ``psh_5``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01237
     - Report Interval End Date
   * - 6
     - ``psh_6``
     -
     - :ref:`CQ <hl7-v2_3-CQ>`
     - O
     -
     - 01238
     - Quantity Manufactured
   * - 7
     - ``psh_7``
     -
     - :ref:`CQ <hl7-v2_3-CQ>`
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
     - :ref:`CQ <hl7-v2_3-CQ>`
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

.. _hl7-v2_3-PTH:

PTH: Pathway
~~~~~~~~~~~~

Section 12.3.4

.. py:class:: hl7types.hl7.v2_3.segments.PTH.PTH
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 01207
     - Pathway ID
   * - 3
     - ``pth_3``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - R
     -
     - 01208
     - Pathway Instance ID
   * - 4
     - ``pth_4``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - R
     -
     - 01209
     - Pathway Established Date/Time
   * - 5
     - ``pth_5``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01210
     - Pathway Lifecycle Status
   * - 6
     - ``pth_6``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - C
     -
     - 01211
     - Change Pathway Lifecycle Status Date/Time

.. _hl7-v2_3-PV1:

PV1: Patient visit
~~~~~~~~~~~~~~~~~~

Section 3.3.3

.. py:class:: hl7types.hl7.v2_3.segments.PV1.PV1
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
     - :ref:`PL <hl7-v2_3-PL>`
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
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 00135
     - Preadmit Number
   * - 6
     - ``pv1_6``
     -
     - :ref:`PL <hl7-v2_3-PL>`
     - O
     -
     - 00136
     - Prior Patient Location
   * - 7
     - ``pv1_7``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     - 0010
     - 00137
     - Attending Doctor
   * - 8
     - ``pv1_8``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     - 0010
     - 00138
     - Referring Doctor
   * - 9
     - ``pv1_9``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
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
     - :ref:`PL <hl7-v2_3-PL>`
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
     - Readmission Indicator
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
     - str
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
     - :ref:`XCN <hl7-v2_3-XCN>`
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
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     -
     - 00149
     - Visit Number
   * - 20
     - ``pv1_20``
     -
     - list[:ref:`FC <hl7-v2_3-FC>`]
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
     - :ref:`PL <hl7-v2_3-PL>`
     - O
     -
     - 00172
     - Pending Location
   * - 43
     - ``pv1_43``
     -
     - :ref:`PL <hl7-v2_3-PL>`
     - O
     -
     - 00173
     - Prior Temporary Location
   * - 44
     - ``pv1_44``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00174
     - Admit Date/Time
   * - 45
     - ``pv1_45``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`CX <hl7-v2_3-CX>`
     - O
     - 0192
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
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
     - O
     - 0010
     - 01274
     - Other Healthcare Provider

.. _hl7-v2_3-PV2:

PV2: Patient visit - additional information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.4

.. py:class:: hl7types.hl7.v2_3.segments.PV2.PV2
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
     - :ref:`PL <hl7-v2_3-PL>`
     - O
     -
     - 00181
     - Prior Pending Location
   * - 2
     - ``pv2_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0129
     - 00182
     - Accommodation Code
   * - 3
     - ``pv2_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00183
     - Admit Reason
   * - 4
     - ``pv2_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00188
     - Expected Admit Date
   * - 9
     - ``pv2_9``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00189
     - Expected Discharge Date
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
     - :ref:`XCN <hl7-v2_3-XCN>`
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
     - list[:ref:`XON <hl7-v2_3-XON>`]
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
     - 3
     - str
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00734
     - Expected Surgery Date & Time
   * - 34
     - ``pv2_34``
     - 2
     - str
     - O
     - 0136
     - 00735
     - Military Partnership Code
   * - 35
     - ``pv2_35``
     - 2
     - str
     - O
     - 0136
     - 00736
     - Military Non-Availabiltiy Code
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

.. _hl7-v2_3-QAK:

QAK: Query Acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.22

.. py:class:: hl7types.hl7.v2_3.segments.QAK.QAK
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
     - O
     -
     - 00696
     - Query tag
   * - 2
     - ``qak_2``
     - 2
     - str
     - O
     - 0208
     - 00708
     - Query response status

.. _hl7-v2_3-QRD:

QRD: Query definition segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.4

.. py:class:: hl7types.hl7.v2_3.segments.QRD.QRD
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00030
     - Deferred Response Date/Time
   * - 7
     - ``qrd_7``
     -
     - :ref:`CQ <hl7-v2_3-CQ>`
     - R
     - 0126
     - 00031
     - Quantity Limited Request
   * - 8
     - ``qrd_8``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
     - R
     -
     - 00032
     - Who Subject Filter
   * - 9
     - ``qrd_9``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - R
     - 0048
     - 00033
     - What Subject Filter
   * - 10
     - ``qrd_10``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
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
     - What Data Code Value Qualifier
   * - 12
     - ``qrd_12``
     - 1
     - str
     - O
     - 0108
     - 00036
     - Query Results Level

.. _hl7-v2_3-QRF:

QRF: Query filter segment
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.5

.. py:class:: hl7types.hl7.v2_3.segments.QRF.QRF
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00038
     - When Data Start Date/Time
   * - 3
     - ``qrf_3``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`TQ <hl7-v2_3-TQ>`
     - O
     -
     - 00694
     - When Quantity/Timing Qualifier

.. _hl7-v2_3-RDF:

RDF: Table Row Definition
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.18

.. py:class:: hl7types.hl7.v2_3.segments.RDF.RDF
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
     - list[:ref:`RCD <hl7-v2_3-RCD>`]
     - R
     -
     - 00702
     - Column Description

.. _hl7-v2_3-RDT:

RDT: Table Row Data
~~~~~~~~~~~~~~~~~~~

Section 2.24.19

.. py:class:: hl7types.hl7.v2_3.segments.RDT.RDT
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
     - Column value

.. _hl7-v2_3-RF1:

RF1: Referral Information Segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.5.1

.. py:class:: hl7types.hl7.v2_3.segments.RF1.RF1
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0283
     - 01137
     - Referral Status
   * - 2
     - ``rf1_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0280
     - 01138
     - Referral Priority
   * - 3
     - ``rf1_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0281
     - 01139
     - Referral Type
   * - 4
     - ``rf1_4``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     - 0282
     - 01140
     - Referral Disposition
   * - 5
     - ``rf1_5``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0284
     - 01141
     - Referral Category
   * - 6
     - ``rf1_6``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - R
     -
     - 01142
     - Originating Referral Identifier
   * - 7
     - ``rf1_7``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01143
     - Effective Date
   * - 8
     - ``rf1_8``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01144
     - Expiration Date
   * - 9
     - ``rf1_9``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01145
     - Process Date
   * - 10
     - ``rf1_10``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     - 0336
     - 01228
     - Referral Reason
   * - 11
     - ``rf1_11``
     -
     - list[:ref:`EI <hl7-v2_3-EI>`]
     - O
     -
     - 01300
     - External Referral Identifier

.. _hl7-v2_3-RGS:

RGS: Resource Group
~~~~~~~~~~~~~~~~~~~

Section 10.5.3

.. py:class:: hl7types.hl7.v2_3.segments.RGS.RGS
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
     - O
     - 0206
     - 00763
     - Segment Action Code
   * - 3
     - ``rgs_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01204
     - Resource Group ID

.. _hl7-v2_3-ROL:

ROL: Role
~~~~~~~~~

Section 12.3.3

.. py:class:: hl7types.hl7.v2_3.segments.ROL.ROL
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
     - :ref:`EI <hl7-v2_3-EI>`
     - R
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01197
     - Role
   * - 4
     - ``rol_4``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - R
     -
     - 01198
     - Role Person
   * - 5
     - ``rol_5``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01199
     - Role Begin Date/Time
   * - 6
     - ``rol_6``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01200
     - Role End Date/Time
   * - 7
     - ``rol_7``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01201
     - Role Duration
   * - 8
     - ``rol_8``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01205
     - Role Action (Assumption) Reason

.. _hl7-v2_3-RQ1:

RQ1: Requisition detail-1 segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.7.2

.. py:class:: hl7types.hl7.v2_3.segments.RQ1.RQ1
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00286
     - Manufactured ID
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
     - :ref:`CE <hl7-v2_3-CE>`
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

.. _hl7-v2_3-RQD:

RQD: Requisition detail
~~~~~~~~~~~~~~~~~~~~~~~

Section 4.7.1

.. py:class:: hl7types.hl7.v2_3.segments.RQD.RQD
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00276
     - Item Code - Internal
   * - 3
     - ``rqd_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00277
     - Item Code - External
   * - 4
     - ``rqd_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00280
     - Requisition Unit of Measure
   * - 7
     - ``rqd_7``
     - 30
     - str
     - O
     -
     - 00281
     - Department Cost Center
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
     - :ref:`CE <hl7-v2_3-CE>`
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

.. _hl7-v2_3-RXA:

RXA: Pharmacy administration segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.14

.. py:class:: hl7types.hl7.v2_3.segments.RXA.RXA
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
     - :ref:`TS <hl7-v2_3-TS>`
     - R
     -
     - 00345
     - Date/Time Start of Administration
   * - 4
     - ``rxa_4``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - R
     -
     - 00346
     - Date/Time End of Administration
   * - 5
     - ``rxa_5``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     -
     - 00349
     - Administered Units
   * - 8
     - ``rxa_8``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00350
     - Administered Dosage Form
   * - 9
     - ``rxa_9``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - C
     -
     - 00351
     - Administration Notes
   * - 10
     - ``rxa_10``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - list[:ref:`TS <hl7-v2_3-TS>`]
     - O
     -
     - 01130
     - Substance Expiration Date
   * - 17
     - ``rxa_17``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     - 0227
     - 01131
     - Substance Manufacturer Name
   * - 18
     - ``rxa_18``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 01136
     - Substance Refusal Reason
   * - 19
     - ``rxa_19``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
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
     - Action Code-RXA
   * - 22
     - ``rxa_22``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01225
     - System Entry Date/Time

.. _hl7-v2_3-RXC:

RXC: Pharmacy component order segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.4

.. py:class:: hl7types.hl7.v2_3.segments.RXC.RXC
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01125
     - Component Strength Units

.. _hl7-v2_3-RXD:

RXD: Pharmacy dispense segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.10

.. py:class:: hl7types.hl7.v2_3.segments.RXD.RXD
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     - 0292
     - 00335
     - Dispense/Give Code
   * - 3
     - ``rxd_3``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     -
     - 00338
     - Actual Dispense Units
   * - 6
     - ``rxd_6``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - C
     -
     - 00340
     - Dispense Notes
   * - 10
     - ``rxd_10``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
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
     - :ref:`CQ <hl7-v2_3-CQ>`
     - C
     -
     - 00329
     - Total Daily Dose
   * - 13
     - ``rxd_13``
     -
     - str
     - O
     -
     - 01303
     - Dispense-To Location
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - list[:ref:`TS <hl7-v2_3-TS>`]
     - O
     -
     - 01130
     - Substance Expiration Date
   * - 20
     - ``rxd_20``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     - 0227
     - 01131
     - Substance Manufacturer Name
   * - 21
     - ``rxd_21``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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

.. _hl7-v2_3-RXE:

RXE: Pharmacy encoded order segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.7

.. py:class:: hl7types.hl7.v2_3.segments.RXE.RXE
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
     - :ref:`TQ <hl7-v2_3-TQ>`
     - R
     -
     - 00221
     - Quantity/Timing
   * - 2
     - ``rxe_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00320
     - Give Units
   * - 6
     - ``rxe_6``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00321
     - Give Dosage Form
   * - 7
     - ``rxe_7``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00298
     - Provider's Administration Instructions
   * - 8
     - ``rxe_8``
     -
     - str
     - O
     -
     - 00299
     - Deliver To Location
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CN <hl7-v2_3-CN>`
     - C
     -
     - 00305
     - Ordering Provider's DEA Number
   * - 14
     - ``rxe_14``
     -
     - :ref:`CN <hl7-v2_3-CN>`
     - C
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00328
     - Date / time of most recent refill or dose dispensed
   * - 19
     - ``rxe_19``
     -
     - :ref:`CQ <hl7-v2_3-CQ>`
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01127
     - Give Strength Units
   * - 27
     - ``rxe_27``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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

.. _hl7-v2_3-RXG:

RXG: Pharmacy give segment
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.12

.. py:class:: hl7types.hl7.v2_3.segments.RXG.RXG
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
     - O
     -
     - 00342
     - Give Sub-ID Counter
   * - 2
     - ``rxg_2``
     - 4
     - str
     - R
     -
     - 00334
     - Dispense Sub-ID Counter
   * - 3
     - ``rxg_3``
     -
     - :ref:`TQ <hl7-v2_3-TQ>`
     - R
     -
     - 00221
     - Quantity/Timing
   * - 4
     - ``rxg_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00320
     - Give Units
   * - 8
     - ``rxg_8``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00321
     - Give Dosage Form
   * - 9
     - ``rxg_9``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
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
     - O
     -
     - 01303
     - Dispense-To Location
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - 6
     - str
     - O
     -
     - 00332
     - Give Rate Amount
   * - 16
     - ``rxg_16``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - list[:ref:`TS <hl7-v2_3-TS>`]
     - O
     -
     - 01130
     - Substance Expiration Date
   * - 21
     - ``rxg_21``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     - 0227
     - 01131
     - Substance Manufacturer Name
   * - 22
     - ``rxg_22``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01123
     - Indication

.. _hl7-v2_3-RXO:

RXO: Pharmacy prescription order segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.2

.. py:class:: hl7types.hl7.v2_3.segments.RXO.RXO
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00295
     - Requested Give Units
   * - 5
     - ``rxo_5``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00296
     - Requested Dosage Form
   * - 6
     - ``rxo_6``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00297
     - Provider's Pharmacy Instructions
   * - 7
     - ``rxo_7``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00298
     - Provider's Administration Instructions
   * - 8
     - ``rxo_8``
     -
     - str
     - O
     -
     - 00299
     - Deliver To Location
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CN <hl7-v2_3-CN>`
     - C
     -
     - 00305
     - Ordering Provider's DEA Number
   * - 15
     - ``rxo_15``
     -
     - :ref:`CN <hl7-v2_3-CN>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01122
     - Requested Give Strength Units
   * - 20
     - ``rxo_20``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 01219
     - Requested Give Rate Units

.. _hl7-v2_3-RXR:

RXR: Pharmacy route segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.8.3

.. py:class:: hl7types.hl7.v2_3.segments.RXR.RXR
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     - 0162
     - 00309
     - Route
   * - 2
     - ``rxr_2``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0163
     - 00310
     - Site
   * - 3
     - ``rxr_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0164
     - 00311
     - Administration Device
   * - 4
     - ``rxr_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0165
     - 00312
     - Administration Method

.. _hl7-v2_3-SCH:

SCH: Schedule Activity Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.5.2

.. py:class:: hl7types.hl7.v2_3.segments.SCH.SCH
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
     - :ref:`EI <hl7-v2_3-EI>`
     - R
     -
     - 00860
     - Placer Appointment ID
   * - 2
     - ``sch_2``
     -
     - :ref:`EI <hl7-v2_3-EI>`
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
     - :ref:`EI <hl7-v2_3-EI>`
     - O
     -
     - 00863
     - Placer Group Number
   * - 5
     - ``sch_5``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00864
     - Schedule ID
   * - 6
     - ``sch_6``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00883
     - Event Reason
   * - 7
     - ``sch_7``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0276
     - 00866
     - Appointment Reason
   * - 8
     - ``sch_8``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00869
     - Appointment Duration Units
   * - 11
     - ``sch_11``
     -
     - list[:ref:`TQ <hl7-v2_3-TQ>`]
     - R
     -
     - 00884
     - Appointment Timing Quantity
   * - 12
     - ``sch_12``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 00874
     - Placer Contact Person
   * - 13
     - ``sch_13``
     -
     - :ref:`XTN <hl7-v2_3-XTN>`
     - O
     -
     - 00875
     - Placer Contact Phone Number
   * - 14
     - ``sch_14``
     -
     - :ref:`XAD <hl7-v2_3-XAD>`
     - O
     -
     - 00876
     - Placer Contact Address
   * - 15
     - ``sch_15``
     -
     - :ref:`PL <hl7-v2_3-PL>`
     - O
     -
     - 00877
     - Placer Contact Location
   * - 16
     - ``sch_16``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - R
     -
     - 00885
     - Filler Contact Person
   * - 17
     - ``sch_17``
     -
     - :ref:`XTN <hl7-v2_3-XTN>`
     - O
     -
     - 00886
     - Filler Contact Phone Number
   * - 18
     - ``sch_18``
     -
     - :ref:`XAD <hl7-v2_3-XAD>`
     - O
     -
     - 00887
     - Filler Contact Address
   * - 19
     - ``sch_19``
     -
     - :ref:`PL <hl7-v2_3-PL>`
     - O
     -
     - 00888
     - Filler Contact Location
   * - 20
     - ``sch_20``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - R
     -
     - 00878
     - Entered By Person
   * - 21
     - ``sch_21``
     -
     - list[:ref:`XTN <hl7-v2_3-XTN>`]
     - O
     -
     - 00879
     - Entered By Phone Number
   * - 22
     - ``sch_22``
     -
     - :ref:`PL <hl7-v2_3-PL>`
     - O
     -
     - 00880
     - Entered By Location
   * - 23
     - ``sch_23``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - O
     -
     - 00881
     - Parent Placer Appointment ID
   * - 24
     - ``sch_24``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - O
     -
     - 00882
     - Parent Filler Appointment ID
   * - 25
     - ``sch_25``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - C
     - 0278
     - 00889
     - Filler Status Code

.. _hl7-v2_3-SPR:

SPR: Stored Procedure Request Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.20

.. py:class:: hl7types.hl7.v2_3.segments.SPR.SPR
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
     - Query tag
   * - 2
     - ``spr_2``
     - 1
     - str
     - R
     - 0106
     - 00697
     - Query/ Response Format Code
   * - 3
     - ``spr_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00704
     - Stored procedure name
   * - 4
     - ``spr_4``
     -
     - list[:ref:`QIP <hl7-v2_3-QIP>`]
     - O
     -
     - 00705
     - Input parameter list

.. _hl7-v2_3-STF:

STF: Staff identification segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.6.2

.. py:class:: hl7types.hl7.v2_3.segments.STF.STF
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
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00671
     - STF - Primary Key Value
   * - 2
     - ``stf_2``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     -
     - 00672
     - Staff ID Code
   * - 3
     - ``stf_3``
     -
     - :ref:`XPN <hl7-v2_3-XPN>`
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
     - :ref:`TS <hl7-v2_3-TS>`
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
     - Active/Inactive Flag
   * - 8
     - ``stf_8``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     - 0184
     - 00676
     - Department
   * - 9
     - ``stf_9``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
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
     - list[:ref:`AD <hl7-v2_3-AD>`]
     - O
     -
     - 00679
     - Office/Home Address
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
     - list[:ref:`CE <hl7-v2_3-CE>`]
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
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - 0185
     - 00684
     - Preferred Method of Contact
   * - 17
     - ``stf_17``
     - 1
     - list[str]
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
     - :ref:`JCC <hl7-v2_3-JCC>`
     - O
     -
     - 00786
     - Job Code/Class
   * - 20
     - ``stf_20``
     - 2
     - str
     - O
     - 0066
     - 01276
     - Employment Status
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
     - :ref:`DLN <hl7-v2_3-DLN>`
     - O
     -
     - 00123
     - Driver's License Number
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
     - 01297
     - Date Next DMV Review

.. _hl7-v2_3-TXA:

TXA: Document notification segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.5.1

.. py:class:: hl7types.hl7.v2_3.segments.TXA.TXA
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
     - Set ID- TXA
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00917
     - Activity Date/Time
   * - 5
     - ``txa_5``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - C
     -
     - 00918
     - Primary Activity Provider Code/Name
   * - 6
     - ``txa_6``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00919
     - Origination Date/Time
   * - 7
     - ``txa_7``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - C
     -
     - 00920
     - Transcription Date/Time
   * - 8
     - ``txa_8``
     -
     - list[:ref:`TS <hl7-v2_3-TS>`]
     - O
     -
     - 00921
     - Edit Date/Time
   * - 9
     - ``txa_9``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 00922
     - Originator Code/Name
   * - 10
     - ``txa_10``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
     - O
     -
     - 00923
     - Assigned Document Authenticator
   * - 11
     - ``txa_11``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - C
     -
     - 00924
     - Transcriptionist Code/Name
   * - 12
     - ``txa_12``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - R
     -
     - 00925
     - Unique Document Number
   * - 13
     - ``txa_13``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - C
     -
     - 00926
     - Parent Document Number
   * - 14
     - ``txa_14``
     -
     - list[:ref:`EI <hl7-v2_3-EI>`]
     - O
     -
     - 00216
     - Placer Order Number
   * - 15
     - ``txa_15``
     -
     - :ref:`EI <hl7-v2_3-EI>`
     - C
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
     - list[str]
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
     - list[:ref:`PPN <hl7-v2_3-PPN>`]
     - O
     -
     - 00934
     - Authentication Person, Time Stamp
   * - 23
     - ``txa_23``
     -
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
     - O
     -
     - 00935
     - Distributed Copies (Code and Name of Recipients)

.. _hl7-v2_3-UB1:

UB1: UB82  data
~~~~~~~~~~~~~~~

Section 6.4.10

.. py:class:: hl7types.hl7.v2_3.segments.UB1.UB1
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
     - Blood Furnished Pints Of (40)
   * - 4
     - ``ub1_4``
     - 2
     - str
     - O
     -
     - 00533
     - Blood Replaced Pints (41)
   * - 5
     - ``ub1_5``
     - 2
     - str
     - O
     -
     - 00534
     - Blood Not Replaced Pints(42)
   * - 6
     - ``ub1_6``
     - 2
     - str
     - O
     -
     - 00535
     - Co Insurance Days (25)
   * - 7
     - ``ub1_7``
     - 2
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
     - Covered Days   (23)
   * - 9
     - ``ub1_9``
     - 3
     - str
     - O
     -
     - 00538
     - Non Covered Days   (24)
   * - 10
     - ``ub1_10``
     -
     - list[str]
     - O
     - 0153
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
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     -
     - 00541
     - Spec Program Indicator (44)
   * - 13
     - ``ub1_13``
     - 60
     - str
     - O
     -
     - 00542
     - PSRO/UR Approval Indicator (87)
   * - 14
     - ``ub1_14``
     - 8
     - str
     - O
     -
     - 00543
     - PSRO/UR Approved Stay Fm (88)
   * - 15
     - ``ub1_15``
     - 8
     - str
     - O
     -
     - 00544
     - PSRO/UR Approved Stay To (89)
   * - 16
     - ``ub1_16``
     -
     - list[str]
     - O
     -
     - 00545
     - Occurrence (28 32)
   * - 17
     - ``ub1_17``
     - 2
     - str
     - O
     -
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
     - UB 82 Locator 2
   * - 21
     - ``ub1_21``
     - 7
     - str
     - O
     -
     - 00550
     - UB 82 Locator 9
   * - 22
     - ``ub1_22``
     - 8
     - str
     - O
     -
     - 00551
     - UB 82 Locator 27
   * - 23
     - ``ub1_23``
     - 17
     - str
     - O
     -
     - 00552
     - UB 82 Locator 45

.. _hl7-v2_3-UB2:

UB2: UB92 data
~~~~~~~~~~~~~~

Section 6.4.11

.. py:class:: hl7types.hl7.v2_3.segments.UB2.UB2
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
     - list[str]
     - O
     -
     - 00558
     - Value Amount & Code
   * - 7
     - ``ub2_7``
     -
     - list[str]
     - O
     -
     - 00559
     - Occurrence Code & Date (32-35)
   * - 8
     - ``ub2_8``
     -
     - list[str]
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

.. _hl7-v2_3-URD:

URD: Results/update definition segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.6

.. py:class:: hl7types.hl7.v2_3.segments.URD.URD
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
     - :ref:`TS <hl7-v2_3-TS>`
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
     - list[:ref:`XCN <hl7-v2_3-XCN>`]
     - R
     -
     - 00047
     - R/U Who Subject Definition
   * - 4
     - ``urd_4``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
     - O
     - 0048
     - 00048
     - R/U What Subject Definition
   * - 5
     - ``urd_5``
     -
     - list[:ref:`CE <hl7-v2_3-CE>`]
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

.. _hl7-v2_3-URS:

URS: Unsolicited selection segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.7

.. py:class:: hl7types.hl7.v2_3.segments.URS.URS
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
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 00053
     - R/U When Data Start Date/Time
   * - 3
     - ``urs_3``
     -
     - :ref:`TS <hl7-v2_3-TS>`
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
     - :ref:`TQ <hl7-v2_3-TQ>`
     - O
     -
     - 00695
     - R/U Quantity/Timing Qualifier

.. _hl7-v2_3-VAR:

VAR: Variance
~~~~~~~~~~~~~

Section 12.3.5

.. py:class:: hl7types.hl7.v2_3.segments.VAR.VAR
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
     - :ref:`EI <hl7-v2_3-EI>`
     - R
     -
     - 01212
     - Variance Instance ID
   * - 2
     - ``var_2``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - R
     -
     - 01213
     - Documented Date/Time
   * - 3
     - ``var_3``
     -
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     -
     - 01214
     - Stated Variance Date/Time
   * - 4
     - ``var_4``
     -
     - :ref:`XCN <hl7-v2_3-XCN>`
     - O
     -
     - 01215
     - Variance Originator
   * - 5
     - ``var_5``
     -
     - :ref:`CE <hl7-v2_3-CE>`
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

.. _hl7-v2_3-VTQ:

VTQ: Virtual Table Query Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.24.17

.. py:class:: hl7types.hl7.v2_3.segments.VTQ.VTQ
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
     - Query tag
   * - 2
     - ``vtq_2``
     - 1
     - str
     - R
     - 0106
     - 00697
     - Query/ Response Format Code
   * - 3
     - ``vtq_3``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00698
     - VT Query Name
   * - 4
     - ``vtq_4``
     -
     - :ref:`CE <hl7-v2_3-CE>`
     - R
     -
     - 00699
     - Virtual Table Name
   * - 5
     - ``vtq_5``
     -
     - list[:ref:`QSC <hl7-v2_3-QSC>`]
     - O
     -
     - 00700
     - Selection Criteria
