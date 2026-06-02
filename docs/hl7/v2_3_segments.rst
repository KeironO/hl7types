v2.3 Segments
=============

.. _hl7-v2_3-ACC:

.. py:class:: hl7types.hl7.v2_3.segments.ACC.ACC
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Accident Date/Time: Item #527
   * - ``acc_2``
     - ACC.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Accident Code: Item #528 | Table HL70050
   * - ``acc_3``
     - ACC.3
     - Optional[str]
     - optional
     -
     - Accident Location: Item #529
   * - ``acc_4``
     - ACC.4
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Auto Accident State: Item #812
   * - ``acc_5``
     - ACC.5
     - Optional[str]
     - optional
     -
     - Accident Job Related Indicator: Item #813 | Table HL70136
   * - ``acc_6``
     - ACC.6
     - Optional[str]
     - optional
     -
     - Accident Death Indicator: Item #814 | Table HL70136

.. _hl7-v2_3-ADD:

.. py:class:: hl7types.hl7.v2_3.segments.ADD.ADD
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

.. _hl7-v2_3-AIG:

.. py:class:: hl7types.hl7.v2_3.segments.AIG.AIG
   :noindex:

   HL7 v2 AIG segment.

AIG
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
   * - ``aig_1``
     - AIG.1
     - str
     - required
     -
     - Set ID - AIG: Item #896
   * - ``aig_2``
     - AIG.2
     - Optional[str]
     - optional
     -
     - Segment Action Code: Item #763 | Table HL70206
   * - ``aig_3``
     - AIG.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Resource ID: Item #897
   * - ``aig_4``
     - AIG.4
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Resource Type: Item #898
   * - ``aig_5``
     - AIG.5
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Resource Group: Item #899
   * - ``aig_6``
     - AIG.6
     - Optional[str]
     - optional
     -
     - Resource Quantity: Item #900
   * - ``aig_7``
     - AIG.7
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Resource Quantity Units: Item #901
   * - ``aig_8``
     - AIG.8
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Start Date/Time: Item #1202
   * - ``aig_9``
     - AIG.9
     - Optional[str]
     - optional
     -
     - Start Date/Time Offset: Item #891
   * - ``aig_10``
     - AIG.10
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Start Date/Time Offset Units: Item #892
   * - ``aig_11``
     - AIG.11
     - Optional[str]
     - optional
     -
     - Duration: Item #893
   * - ``aig_12``
     - AIG.12
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Duration Units: Item #894
   * - ``aig_13``
     - AIG.13
     - Optional[str]
     - optional
     -
     - Allow Substitution Code: Item #895 | Table HL70279
   * - ``aig_14``
     - AIG.14
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Filler Status Code: Item #889 | Table HL70278

.. _hl7-v2_3-AIL:

.. py:class:: hl7types.hl7.v2_3.segments.AIL.AIL
   :noindex:

   HL7 v2 AIL segment.

AIL
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
   * - ``ail_1``
     - AIL.1
     - str
     - required
     -
     - Set ID - AIL: Item #902
   * - ``ail_2``
     - AIL.2
     - Optional[str]
     - optional
     -
     - Segment Action Code: Item #763 | Table HL70206
   * - ``ail_3``
     - AIL.3
     - :ref:`PL <hl7-v2_3-PL>`
     - required
     -
     - Location Resource ID: Item #903
   * - ``ail_4``
     - AIL.4
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Location Type: Item #904
   * - ``ail_5``
     - AIL.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Location Group: Item #905
   * - ``ail_6``
     - AIL.6
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Start Date/Time: Item #1202
   * - ``ail_7``
     - AIL.7
     - Optional[str]
     - optional
     -
     - Start Date/Time Offset: Item #891
   * - ``ail_8``
     - AIL.8
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Start Date/Time Offset Units: Item #892
   * - ``ail_9``
     - AIL.9
     - Optional[str]
     - optional
     -
     - Duration: Item #893
   * - ``ail_10``
     - AIL.10
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Duration Units: Item #894
   * - ``ail_11``
     - AIL.11
     - Optional[str]
     - optional
     -
     - Allow Substitution Code: Item #895 | Table HL70279
   * - ``ail_12``
     - AIL.12
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Filler Status Code: Item #889 | Table HL70278

.. _hl7-v2_3-AIP:

.. py:class:: hl7types.hl7.v2_3.segments.AIP.AIP
   :noindex:

   HL7 v2 AIP segment.

AIP
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
   * - ``aip_1``
     - AIP.1
     - str
     - required
     -
     - Set ID - AIP: Item #906
   * - ``aip_2``
     - AIP.2
     - Optional[str]
     - optional
     -
     - Segment Action Code: Item #763 | Table HL70206
   * - ``aip_3``
     - AIP.3
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Personnel Resource ID: Item #913
   * - ``aip_4``
     - AIP.4
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Resource Role: Item #907
   * - ``aip_5``
     - AIP.5
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Resource Group: Item #899
   * - ``aip_6``
     - AIP.6
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Start Date/Time: Item #1202
   * - ``aip_7``
     - AIP.7
     - Optional[str]
     - optional
     -
     - Start Date/Time Offset: Item #891
   * - ``aip_8``
     - AIP.8
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Start Date/Time Offset Units: Item #892
   * - ``aip_9``
     - AIP.9
     - Optional[str]
     - optional
     -
     - Duration: Item #893
   * - ``aip_10``
     - AIP.10
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Duration Units: Item #894
   * - ``aip_11``
     - AIP.11
     - Optional[str]
     - optional
     -
     - Allow Substitution Code: Item #895 | Table HL70279
   * - ``aip_12``
     - AIP.12
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Filler Status Code: Item #889 | Table HL70278

.. _hl7-v2_3-AIS:

.. py:class:: hl7types.hl7.v2_3.segments.AIS.AIS
   :noindex:

   HL7 v2 AIS segment.

AIS
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
   * - ``ais_1``
     - AIS.1
     - str
     - required
     -
     - Set ID - AIS: Item #890
   * - ``ais_2``
     - AIS.2
     - Optional[str]
     - optional
     -
     - Segment Action Code: Item #763 | Table HL70206
   * - ``ais_3``
     - AIS.3
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Universal Service Identifier: Item #238
   * - ``ais_4``
     - AIS.4
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Start Date/Time: Item #1202
   * - ``ais_5``
     - AIS.5
     - Optional[str]
     - optional
     -
     - Start Date/Time Offset: Item #891
   * - ``ais_6``
     - AIS.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Start Date/Time Offset Units: Item #892
   * - ``ais_7``
     - AIS.7
     - Optional[str]
     - optional
     -
     - Duration: Item #893
   * - ``ais_8``
     - AIS.8
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Duration Units: Item #894
   * - ``ais_9``
     - AIS.9
     - Optional[str]
     - optional
     -
     - Allow Substitution Code: Item #895 | Table HL70279
   * - ``ais_10``
     - AIS.10
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Filler Status Code: Item #889 | Table HL70278

.. _hl7-v2_3-AL1:

.. py:class:: hl7types.hl7.v2_3.segments.AL1.AL1
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
     - Set ID - AL1: Item #203
   * - ``al1_2``
     - AL1.2
     - Optional[str]
     - optional
     -
     - Allergy Type: Item #204 | Table HL70127
   * - ``al1_3``
     - AL1.3
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Allergy Code/Mnemonic/ Description: Item #205
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

.. _hl7-v2_3-APR:

.. py:class:: hl7types.hl7.v2_3.segments.APR.APR
   :noindex:

   HL7 v2 APR segment.

APR
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
   * - ``apr_1``
     - APR.1
     - Optional[List[:ref:`SCV <hl7-v2_3-SCV>`]]
     - optional
     -
     - Time Selection Criteria: Item #908
   * - ``apr_2``
     - APR.2
     - Optional[List[:ref:`SCV <hl7-v2_3-SCV>`]]
     - optional
     -
     - Resource Selection Criteria: Item #909
   * - ``apr_3``
     - APR.3
     - Optional[List[:ref:`SCV <hl7-v2_3-SCV>`]]
     - optional
     -
     - Location Selection Criteria: Item #910
   * - ``apr_4``
     - APR.4
     - Optional[str]
     - optional
     -
     - Slot Spacing Criteria: Item #911
   * - ``apr_5``
     - APR.5
     - Optional[List[:ref:`SCV <hl7-v2_3-SCV>`]]
     - optional
     -
     - Filler Override Criteria: Item #912

.. _hl7-v2_3-ARQ:

.. py:class:: hl7types.hl7.v2_3.segments.ARQ.ARQ
   :noindex:

   HL7 v2 ARQ segment.

ARQ
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
   * - ``arq_1``
     - ARQ.1
     - :ref:`EI <hl7-v2_3-EI>`
     - required
     -
     - Placer Appointment ID: Item #860
   * - ``arq_2``
     - ARQ.2
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Filler Appointment ID: Item #861
   * - ``arq_3``
     - ARQ.3
     - Optional[str]
     - optional
     -
     - Occurrence Number: Item #862
   * - ``arq_4``
     - ARQ.4
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Placer Group Number: Item #863
   * - ``arq_5``
     - ARQ.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Schedule ID: Item #864
   * - ``arq_6``
     - ARQ.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Request Event Reason: Item #865
   * - ``arq_7``
     - ARQ.7
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Appointment Reason: Item #866 | Table HL70276
   * - ``arq_8``
     - ARQ.8
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Appointment Type: Item #867 | Table HL70277
   * - ``arq_9``
     - ARQ.9
     - Optional[str]
     - optional
     -
     - Appointment Duration: Item #868
   * - ``arq_10``
     - ARQ.10
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Appointment Duration Units: Item #869
   * - ``arq_11``
     - ARQ.11
     - Optional[List[:ref:`DR <hl7-v2_3-DR>`]]
     - optional
     -
     - Requested Start Date/Time Range: Item #870
   * - ``arq_12``
     - ARQ.12
     - Optional[str]
     - optional
     -
     - Priority: Item #871
   * - ``arq_13``
     - ARQ.13
     - Optional[:ref:`RI <hl7-v2_3-RI>`]
     - optional
     -
     - Repeating Interval: Item #872
   * - ``arq_14``
     - ARQ.14
     - Optional[str]
     - optional
     -
     - Repeating Interval Duration: Item #873
   * - ``arq_15``
     - ARQ.15
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Placer Contact Person: Item #874
   * - ``arq_16``
     - ARQ.16
     - Optional[:ref:`XTN <hl7-v2_3-XTN>`]
     - optional
     -
     - Placer Contact Phone Number: Item #875
   * - ``arq_17``
     - ARQ.17
     - Optional[:ref:`XAD <hl7-v2_3-XAD>`]
     - optional
     -
     - Placer Contact Address: Item #876
   * - ``arq_18``
     - ARQ.18
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Placer Contact Location: Item #877
   * - ``arq_19``
     - ARQ.19
     - :ref:`XCN <hl7-v2_3-XCN>`
     - required
     -
     - Entered By Person: Item #878
   * - ``arq_20``
     - ARQ.20
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Entered By Phone Number: Item #879
   * - ``arq_21``
     - ARQ.21
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Entered By Location: Item #880
   * - ``arq_22``
     - ARQ.22
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Parent Placer Appointment ID: Item #881
   * - ``arq_23``
     - ARQ.23
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Parent Filler Appointment ID: Item #882

.. _hl7-v2_3-AUT:

.. py:class:: hl7types.hl7.v2_3.segments.AUT.AUT
   :noindex:

   HL7 v2 AUT segment.

AUT
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
   * - ``aut_1``
     - AUT.1
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Authorizing Payor, Plan Code: Item #1146 | Table HL70072
   * - ``aut_2``
     - AUT.2
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Authorizing Payor, Company ID: Item #1147 | Table HL70285
   * - ``aut_3``
     - AUT.3
     - Optional[str]
     - optional
     -
     - Authorizing Payor, Company Name: Item #1148
   * - ``aut_4``
     - AUT.4
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Authorization Effective Date: Item #1149
   * - ``aut_5``
     - AUT.5
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Authorization Expiration Date: Item #1150
   * - ``aut_6``
     - AUT.6
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Authorization Identifier: Item #1151
   * - ``aut_7``
     - AUT.7
     - Optional[:ref:`CP <hl7-v2_3-CP>`]
     - optional
     -
     - Reimbursement Limit: Item #1152
   * - ``aut_8``
     - AUT.8
     - Optional[str]
     - optional
     -
     - Requested Number of Treatments: Item #1153
   * - ``aut_9``
     - AUT.9
     - Optional[str]
     - optional
     -
     - Authorized Number of Treatments: Item #1154
   * - ``aut_10``
     - AUT.10
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Process Date: Item #1145

.. _hl7-v2_3-BHS:

.. py:class:: hl7types.hl7.v2_3.segments.BHS.BHS
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Batch Creation Date/Time: Item #87
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
     - Batch Name/ID/Type: Item #89
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

.. _hl7-v2_3-BLG:

.. py:class:: hl7types.hl7.v2_3.segments.BLG.BLG
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
     - Optional[:ref:`CK <hl7-v2_3-CK>`]
     - optional
     -
     - Account ID: Item #236

.. _hl7-v2_3-BTS:

.. py:class:: hl7types.hl7.v2_3.segments.BTS.BTS
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
     - Batch Comment: Item #90
   * - ``bts_3``
     - BTS.3
     - Optional[List[str]]
     - optional
     -
     - Batch Totals: Item #95

.. _hl7-v2_3-CDM:

.. py:class:: hl7types.hl7.v2_3.segments.CDM.CDM
   :noindex:

   HL7 v2 CDM segment.

CDM
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
   * - ``cdm_1``
     - CDM.1
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Primary Key Value: Item #982 | Table HL70132
   * - ``cdm_2``
     - CDM.2
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Charge Code Alias: Item #983
   * - ``cdm_3``
     - CDM.3
     - str
     - required
     -
     - Charge Description Short: Item #984
   * - ``cdm_4``
     - CDM.4
     - Optional[str]
     - optional
     -
     - Charge Description Long: Item #985
   * - ``cdm_5``
     - CDM.5
     - Optional[str]
     - optional
     -
     - Description Override Indicator: Item #986 | Table HL70268
   * - ``cdm_6``
     - CDM.6
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Exploding Charges: Item #987
   * - ``cdm_7``
     - CDM.7
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Procedure Code: Item #988
   * - ``cdm_8``
     - CDM.8
     - Optional[str]
     - optional
     -
     - Active/Inactive Flag: Item #675 | Table HL70183
   * - ``cdm_9``
     - CDM.9
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Inventory Number: Item #990
   * - ``cdm_10``
     - CDM.10
     - Optional[str]
     - optional
     -
     - Resource Load: Item #991
   * - ``cdm_11``
     - CDM.11
     - Optional[List[:ref:`CK <hl7-v2_3-CK>`]]
     - optional
     -
     - Contract Number: Item #992
   * - ``cdm_12``
     - CDM.12
     - Optional[:ref:`XON <hl7-v2_3-XON>`]
     - optional
     -
     - Contract Organization: Item #993
   * - ``cdm_13``
     - CDM.13
     - Optional[str]
     - optional
     -
     - Room Fee Indicator: Item #994 | Table HL70136

.. _hl7-v2_3-CM0:

.. py:class:: hl7types.hl7.v2_3.segments.CM0.CM0
   :noindex:

   HL7 v2 CM0 segment.

CM0
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
   * - ``cm0_1``
     - CM0.1
     - Optional[str]
     - optional
     -
     - CM0 - Set ID: Item #1010
   * - ``cm0_2``
     - CM0.2
     - :ref:`EI <hl7-v2_3-EI>`
     - required
     -
     - Sponsor Study ID: Item #1011
   * - ``cm0_3``
     - CM0.3
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Alternate Study ID: Item #1012
   * - ``cm0_4``
     - CM0.4
     - str
     - required
     -
     - Title of Study: Item #1013
   * - ``cm0_5``
     - CM0.5
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Chairman of Study: Item #1014
   * - ``cm0_6``
     - CM0.6
     - Optional[str]
     - optional
     -
     - Last IRB Approval Date: Item #1015
   * - ``cm0_7``
     - CM0.7
     - Optional[str]
     - optional
     -
     - Total Accrual to Date: Item #1016
   * - ``cm0_8``
     - CM0.8
     - Optional[str]
     - optional
     -
     - Last Accrual Date: Item #1017
   * - ``cm0_9``
     - CM0.9
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Contact for Study: Item #1018
   * - ``cm0_10``
     - CM0.10
     - Optional[:ref:`XTN <hl7-v2_3-XTN>`]
     - optional
     -
     - Contact's Tel. Number: Item #1019
   * - ``cm0_11``
     - CM0.11
     - Optional[:ref:`XAD <hl7-v2_3-XAD>`]
     - optional
     -
     - Contact's Address: Item #1020

.. _hl7-v2_3-CM1:

.. py:class:: hl7types.hl7.v2_3.segments.CM1.CM1
   :noindex:

   HL7 v2 CM1 segment.

CM1
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
   * - ``cm1_1``
     - CM1.1
     - str
     - required
     -
     - CM1 - Set ID: Item #1021
   * - ``cm1_2``
     - CM1.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Study Phase Identifier: Item #1051
   * - ``cm1_3``
     - CM1.3
     - str
     - required
     -
     - Description of Study Phase: Item #1023

.. _hl7-v2_3-CM2:

.. py:class:: hl7types.hl7.v2_3.segments.CM2.CM2
   :noindex:

   HL7 v2 CM2 segment.

CM2
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
   * - ``cm2_1``
     - CM2.1
     - Optional[str]
     - optional
     -
     - CM2 - Set ID: Item #1024
   * - ``cm2_2``
     - CM2.2
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Scheduled Time Point: Item #1025
   * - ``cm2_3``
     - CM2.3
     - Optional[str]
     - optional
     -
     - Description of Time Point: Item #1026
   * - ``cm2_4``
     - CM2.4
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Events Scheduled This Time Point: Item #1027

.. _hl7-v2_3-CSP:

.. py:class:: hl7types.hl7.v2_3.segments.CSP.CSP
   :noindex:

   HL7 v2 CSP segment.

CSP
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
   * - ``csp_1``
     - CSP.1
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Study Phase Identifier: Item #1051
   * - ``csp_2``
     - CSP.2
     - :ref:`TS <hl7-v2_3-TS>`
     - required
     -
     - Date/time Study Phase Began: Item #1052
   * - ``csp_3``
     - CSP.3
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date/time Study Phase Ended: Item #1053
   * - ``csp_4``
     - CSP.4
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Study Phase Evaluability: Item #1054

.. _hl7-v2_3-CSR:

.. py:class:: hl7types.hl7.v2_3.segments.CSR.CSR
   :noindex:

   HL7 v2 CSR segment.

CSR
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
   * - ``csr_1``
     - CSR.1
     - :ref:`EI <hl7-v2_3-EI>`
     - required
     -
     - Sponsor Study ID: Item #1011
   * - ``csr_2``
     - CSR.2
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Alternate Study ID: Item #1036
   * - ``csr_3``
     - CSR.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Institution Registering the Patient: Item #1037
   * - ``csr_4``
     - CSR.4
     - :ref:`CX <hl7-v2_3-CX>`
     - required
     -
     - Sponsor Patient ID: Item #1038
   * - ``csr_5``
     - CSR.5
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Alternate Patient ID: Item #1039
   * - ``csr_6``
     - CSR.6
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date/Time of Patient Study Registration: Item #1040
   * - ``csr_7``
     - CSR.7
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Person Performing Study Registration: Item #1041
   * - ``csr_8``
     - CSR.8
     - :ref:`XCN <hl7-v2_3-XCN>`
     - required
     -
     - Study Authorizing Provider: Item #1042
   * - ``csr_9``
     - CSR.9
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date/time Patient Study Consent Signed: Item #1043
   * - ``csr_10``
     - CSR.10
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Patient Study Eligibility Status: Item #1044
   * - ``csr_11``
     - CSR.11
     - Optional[List[:ref:`TS <hl7-v2_3-TS>`]]
     - optional
     -
     - Study Randomization Date/time: Item #1045
   * - ``csr_12``
     - CSR.12
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Study Randomized Arm: Item #1046
   * - ``csr_13``
     - CSR.13
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Stratum for Study Randomization: Item #1047
   * - ``csr_14``
     - CSR.14
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Patient Evaluability Status: Item #1048
   * - ``csr_15``
     - CSR.15
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date/time Ended Study: Item #1049
   * - ``csr_16``
     - CSR.16
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Reason Ended Study: Item #1050

.. _hl7-v2_3-CSS:

.. py:class:: hl7types.hl7.v2_3.segments.CSS.CSS
   :noindex:

   HL7 v2 CSS segment.

CSS
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
   * - ``css_1``
     - CSS.1
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Study Scheduled Time Point: Item #1055
   * - ``css_2``
     - CSS.2
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Study Scheduled Patient Time Point: Item #1056
   * - ``css_3``
     - CSS.3
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Study Quality Control Codes: Item #1057

.. _hl7-v2_3-CTD:

.. py:class:: hl7types.hl7.v2_3.segments.CTD.CTD
   :noindex:

   HL7 v2 CTD segment.

CTD
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
   * - ``ctd_1``
     - CTD.1
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Contact Role: Item #196 | Table HL70131
   * - ``ctd_2``
     - CTD.2
     - Optional[List[:ref:`XPN <hl7-v2_3-XPN>`]]
     - optional
     -
     - Contact Name: Item #1165
   * - ``ctd_3``
     - CTD.3
     - Optional[List[:ref:`XAD <hl7-v2_3-XAD>`]]
     - optional
     -
     - Contact Address: Item #1268
   * - ``ctd_4``
     - CTD.4
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Contact Location: Item #1167
   * - ``ctd_5``
     - CTD.5
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Contact Communication Information: Item #1168
   * - ``ctd_6``
     - CTD.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Preferred Method of Contact: Item #684 | Table HL70185
   * - ``ctd_7``
     - CTD.7
     - Optional[List[str]]
     - optional
     -
     - Contact Identifiers: Item #1171

.. _hl7-v2_3-CTI:

.. py:class:: hl7types.hl7.v2_3.segments.CTI.CTI
   :noindex:

   HL7 v2 CTI segment.

CTI
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
   * - ``cti_1``
     - CTI.1
     - :ref:`EI <hl7-v2_3-EI>`
     - required
     -
     - Sponsor Study ID: Item #1011
   * - ``cti_2``
     - CTI.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Study Phase Identifier: Item #1051
   * - ``cti_3``
     - CTI.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Study Scheduled Time Point: Item #1055

.. _hl7-v2_3-DB1:

.. py:class:: hl7types.hl7.v2_3.segments.DB1.DB1
   :noindex:

   HL7 v2 DB1 segment.

DB1
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
   * - ``db1_1``
     - DB1.1
     - str
     - required
     -
     - Set ID - DB1: Item #1283
   * - ``db1_2``
     - DB1.2
     - Optional[str]
     - optional
     -
     - Disabled person code: Item #1284 | Table HL70033
   * - ``db1_3``
     - DB1.3
     - Optional[List[:ref:`CX <hl7-v2_3-CX>`]]
     - optional
     -
     - Disabled person identifier: Item #1285
   * - ``db1_4``
     - DB1.4
     - Optional[str]
     - optional
     -
     - Disabled Indicator: Item #1286 | Table HL70136
   * - ``db1_5``
     - DB1.5
     - Optional[str]
     - optional
     -
     - Disability start date: Item #1287
   * - ``db1_6``
     - DB1.6
     - Optional[str]
     - optional
     -
     - Disability end date: Item #1288
   * - ``db1_7``
     - DB1.7
     - Optional[str]
     - optional
     -
     - Disability return to work date: Item #1289
   * - ``db1_8``
     - DB1.8
     - Optional[str]
     - optional
     -
     - Disability unable to work date: Item #1290

.. _hl7-v2_3-DG1:

.. py:class:: hl7types.hl7.v2_3.segments.DG1.DG1
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
     - Set ID - Diagnosis: Item #375
   * - ``dg1_2``
     - DG1.2
     - Optional[str]
     - optional
     -
     - Diagnosis Coding Method: Item #376 | Table HL70053
   * - ``dg1_3``
     - DG1.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Diagnosis Code: Item #377 | Table HL70051
   * - ``dg1_4``
     - DG1.4
     - Optional[str]
     - optional
     -
     - Diagnosis Description: Item #378
   * - ``dg1_5``
     - DG1.5
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Diagnosis Date/Time: Item #379
   * - ``dg1_6``
     - DG1.6
     - str
     - required
     -
     - Diagnosis Type: Item #380 | Table HL70052
   * - ``dg1_7``
     - DG1.7
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Major Diagnostic Category: Item #381 | Table HL70118
   * - ``dg1_8``
     - DG1.8
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Diagnostic Related Group: Item #382 | Table HL70055
   * - ``dg1_9``
     - DG1.9
     - Optional[str]
     - optional
     -
     - DRG Approval Indicator: Item #383 | Table HL70136
   * - ``dg1_10``
     - DG1.10
     - Optional[str]
     - optional
     -
     - DRG Grouper Review Code: Item #384 | Table HL70056
   * - ``dg1_11``
     - DG1.11
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Outlier Type: Item #385 | Table HL70083
   * - ``dg1_12``
     - DG1.12
     - Optional[str]
     - optional
     -
     - Outlier Days: Item #386
   * - ``dg1_13``
     - DG1.13
     - Optional[:ref:`CP <hl7-v2_3-CP>`]
     - optional
     -
     - Outlier Cost: Item #387
   * - ``dg1_14``
     - DG1.14
     - Optional[str]
     - optional
     -
     - Grouper Version and Type: Item #388
   * - ``dg1_15``
     - DG1.15
     - Optional[str]
     - optional
     -
     - Diagnosis Priority: Item #389
   * - ``dg1_16``
     - DG1.16
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Diagnosing Clinician: Item #390
   * - ``dg1_17``
     - DG1.17
     - Optional[str]
     - optional
     -
     - Diagnosis Classification: Item #766 | Table HL70228
   * - ``dg1_18``
     - DG1.18
     - Optional[str]
     - optional
     -
     - Confidential Indicator: Item #767 | Table HL70136
   * - ``dg1_19``
     - DG1.19
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Attestation Date/Time: Item #768

.. _hl7-v2_3-DRG:

.. py:class:: hl7types.hl7.v2_3.segments.DRG.DRG
   :noindex:

   HL7 v2 DRG segment.

DRG
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
   * - ``drg_1``
     - DRG.1
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Diagnostic Related Group: Item #382 | Table HL70055
   * - ``drg_2``
     - DRG.2
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - DRG Assigned Date/Time: Item #769
   * - ``drg_3``
     - DRG.3
     - Optional[str]
     - optional
     -
     - DRG Approval Indicator: Item #383 | Table HL70136
   * - ``drg_4``
     - DRG.4
     - Optional[str]
     - optional
     -
     - DRG Grouper Review Code: Item #384 | Table HL70056
   * - ``drg_5``
     - DRG.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Outlier Type: Item #385 | Table HL70083
   * - ``drg_6``
     - DRG.6
     - Optional[str]
     - optional
     -
     - Outlier Days: Item #386
   * - ``drg_7``
     - DRG.7
     - Optional[:ref:`CP <hl7-v2_3-CP>`]
     - optional
     -
     - Outlier Cost: Item #387
   * - ``drg_8``
     - DRG.8
     - Optional[str]
     - optional
     -
     - DRG Payor: Item #770 | Table HL70229
   * - ``drg_9``
     - DRG.9
     - Optional[:ref:`CP <hl7-v2_3-CP>`]
     - optional
     -
     - Outlier Reimbursement: Item #771
   * - ``drg_10``
     - DRG.10
     - Optional[str]
     - optional
     -
     - Confidential Indicator: Item #767 | Table HL70136

.. _hl7-v2_3-DSC:

.. py:class:: hl7types.hl7.v2_3.segments.DSC.DSC
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
     - Continuation Pointer: Item #14

.. _hl7-v2_3-DSP:

.. py:class:: hl7types.hl7.v2_3.segments.DSP.DSP
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
     - :ref:`TX <hl7-v2_3-TX>`
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
     - Optional[:ref:`TX <hl7-v2_3-TX>`]
     - optional
     -
     - Result ID: Item #65

.. _hl7-v2_3-EQL:

.. py:class:: hl7types.hl7.v2_3.segments.EQL.EQL
   :noindex:

   HL7 v2 EQL segment.

EQL
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
   * - ``eql_1``
     - EQL.1
     - Optional[str]
     - optional
     -
     - Query tag: Item #696
   * - ``eql_2``
     - EQL.2
     - str
     - required
     -
     - Query/ Response Format Code: Item #697 | Table HL70106
   * - ``eql_3``
     - EQL.3
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - EQL Query Name: Item #709
   * - ``eql_4``
     - EQL.4
     - str
     - required
     -
     - EQL Query Statement: Item #710

.. _hl7-v2_3-ERQ:

.. py:class:: hl7types.hl7.v2_3.segments.ERQ.ERQ
   :noindex:

   HL7 v2 ERQ segment.

ERQ
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
   * - ``erq_1``
     - ERQ.1
     - Optional[str]
     - optional
     -
     - Query tag: Item #696
   * - ``erq_2``
     - ERQ.2
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Event identifier: Item #706
   * - ``erq_3``
     - ERQ.3
     - Optional[List[:ref:`QIP <hl7-v2_3-QIP>`]]
     - optional
     -
     - Input parameter list: Item #705

.. _hl7-v2_3-ERR:

.. py:class:: hl7types.hl7.v2_3.segments.ERR.ERR
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

.. _hl7-v2_3-EVN:

.. py:class:: hl7types.hl7.v2_3.segments.EVN.EVN
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Recorded Date/Time: Item #100
   * - ``evn_3``
     - EVN.3
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date/Time Planned Event: Item #101
   * - ``evn_4``
     - EVN.4
     - Optional[str]
     - optional
     -
     - Event Reason Code: Item #102 | Table HL70062
   * - ``evn_5``
     - EVN.5
     - Optional[:ref:`CN <hl7-v2_3-CN>`]
     - optional
     -
     - Operator ID: Item #103 | Table HL70188
   * - ``evn_6``
     - EVN.6
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Event occured: Item #1278

.. _hl7-v2_3-FAC:

.. py:class:: hl7types.hl7.v2_3.segments.FAC.FAC
   :noindex:

   HL7 v2 FAC segment.

FAC
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
   * - ``fac_1``
     - FAC.1
     - Optional[List[:ref:`EI <hl7-v2_3-EI>`]]
     - optional
     -
     - Facility ID: Item #1262
   * - ``fac_2``
     - FAC.2
     - Optional[str]
     - optional
     -
     - Facility Type: Item #1263 | Table HL70331
   * - ``fac_3``
     - FAC.3
     - :ref:`XAD <hl7-v2_3-XAD>`
     - required
     -
     - Facility Address: Item #1264
   * - ``fac_4``
     - FAC.4
     - :ref:`XTN <hl7-v2_3-XTN>`
     - required
     -
     - Facility Telecommunication: Item #1265
   * - ``fac_5``
     - FAC.5
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Contact Person: Item #1266
   * - ``fac_6``
     - FAC.6
     - Optional[List[str]]
     - optional
     -
     - Contact Title: Item #1267
   * - ``fac_7``
     - FAC.7
     - Optional[List[:ref:`XAD <hl7-v2_3-XAD>`]]
     - optional
     -
     - Contact Address: Item #1268
   * - ``fac_8``
     - FAC.8
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Contact Telecommunication: Item #1269
   * - ``fac_9``
     - FAC.9
     - :ref:`XCN <hl7-v2_3-XCN>`
     - required
     -
     - Signature Authority: Item #1270
   * - ``fac_10``
     - FAC.10
     - Optional[str]
     - optional
     -
     - Signature Authority Title: Item #1271
   * - ``fac_11``
     - FAC.11
     - Optional[:ref:`XAD <hl7-v2_3-XAD>`]
     - optional
     -
     - Signature Authority Address: Item #1272
   * - ``fac_12``
     - FAC.12
     - Optional[:ref:`XTN <hl7-v2_3-XTN>`]
     - optional
     -
     - Signature Authority Telecommunication: Item #1273

.. _hl7-v2_3-FHS:

.. py:class:: hl7types.hl7.v2_3.segments.FHS.FHS
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - File Creation Date/Time: Item #73
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
     - File Name/ID: Item #75
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

.. _hl7-v2_3-FT1:

.. py:class:: hl7types.hl7.v2_3.segments.FT1.FT1
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
     - Set ID - Financial Transaction: Item #355
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
     - Transaction Batch ID: Item #357
   * - ``ft1_4``
     - FT1.4
     - :ref:`TS <hl7-v2_3-TS>`
     - required
     -
     - Transaction Date: Item #358
   * - ``ft1_5``
     - FT1.5
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Transaction Posting Date: Item #359
   * - ``ft1_6``
     - FT1.6
     - str
     - required
     -
     - Transaction Type: Item #360 | Table HL70017
   * - ``ft1_7``
     - FT1.7
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Transaction Code: Item #361 | Table HL70132
   * - ``ft1_8``
     - FT1.8
     - Optional[str]
     - optional
     -
     - Transaction Description: Item #362
   * - ``ft1_9``
     - FT1.9
     - Optional[str]
     - optional
     -
     - Transaction Description - alternate: Item #363
   * - ``ft1_10``
     - FT1.10
     - Optional[str]
     - optional
     -
     - Transaction Quantity: Item #364
   * - ``ft1_11``
     - FT1.11
     - Optional[:ref:`CP <hl7-v2_3-CP>`]
     - optional
     -
     - Transaction Amount - Extended: Item #365
   * - ``ft1_12``
     - FT1.12
     - Optional[:ref:`CP <hl7-v2_3-CP>`]
     - optional
     -
     - Transaction Amount - Unit: Item #366
   * - ``ft1_13``
     - FT1.13
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Department Code: Item #367 | Table HL70049
   * - ``ft1_14``
     - FT1.14
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Insurance Plan ID: Item #368 | Table HL70072
   * - ``ft1_15``
     - FT1.15
     - Optional[:ref:`CP <hl7-v2_3-CP>`]
     - optional
     -
     - Insurance Amount: Item #369
   * - ``ft1_16``
     - FT1.16
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Assigned Patient Location: Item #133
   * - ``ft1_17``
     - FT1.17
     - Optional[str]
     - optional
     -
     - Fee Schedule: Item #370 | Table HL70024
   * - ``ft1_18``
     - FT1.18
     - Optional[str]
     - optional
     -
     - Patient Type: Item #148 | Table HL70018
   * - ``ft1_19``
     - FT1.19
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Diagnosis Code: Item #371 | Table HL70051
   * - ``ft1_20``
     - FT1.20
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Performed By Code: Item #372 | Table HL70084
   * - ``ft1_21``
     - FT1.21
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Ordered By Code: Item #373
   * - ``ft1_22``
     - FT1.22
     - Optional[str]
     - optional
     -
     - Unit Cost: Item #374
   * - ``ft1_23``
     - FT1.23
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Filler Order Number: Item #217
   * - ``ft1_24``
     - FT1.24
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Entered By Code: Item #765
   * - ``ft1_25``
     - FT1.25
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Procedure Code: Item #393 | Table HL70088

.. _hl7-v2_3-FTS:

.. py:class:: hl7types.hl7.v2_3.segments.FTS.FTS
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

.. _hl7-v2_3-GOL:

.. py:class:: hl7types.hl7.v2_3.segments.GOL.GOL
   :noindex:

   HL7 v2 GOL segment.

GOL
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
   * - ``gol_1``
     - GOL.1
     - str
     - required
     -
     - Action Code: Item #816 | Table HL70287
   * - ``gol_2``
     - GOL.2
     - :ref:`TS <hl7-v2_3-TS>`
     - required
     -
     - Action Date/Time: Item #817
   * - ``gol_3``
     - GOL.3
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Goal ID: Item #818
   * - ``gol_4``
     - GOL.4
     - :ref:`EI <hl7-v2_3-EI>`
     - required
     -
     - Goal Instance ID: Item #819
   * - ``gol_5``
     - GOL.5
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Episode of Care ID: Item #820
   * - ``gol_6``
     - GOL.6
     - Optional[str]
     - optional
     -
     - Goal List Priority: Item #821
   * - ``gol_7``
     - GOL.7
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Goal Established Date/Time: Item #822
   * - ``gol_8``
     - GOL.8
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Expected Goal Achievement Date/Time: Item #824
   * - ``gol_9``
     - GOL.9
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Goal Classification: Item #825
   * - ``gol_10``
     - GOL.10
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Goal Management Discipline: Item #826
   * - ``gol_11``
     - GOL.11
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Current Goal Review Status: Item #827
   * - ``gol_12``
     - GOL.12
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Current Goal Review Date/Time: Item #828
   * - ``gol_13``
     - GOL.13
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Next Goal Review Date/Time: Item #829
   * - ``gol_14``
     - GOL.14
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Previous Goal Review Date/Time: Item #830
   * - ``gol_15``
     - GOL.15
     - Optional[:ref:`TQ <hl7-v2_3-TQ>`]
     - optional
     -
     - Goal Review Interval: Item #831
   * - ``gol_16``
     - GOL.16
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Goal Evaluation: Item #832
   * - ``gol_17``
     - GOL.17
     - Optional[List[str]]
     - optional
     -
     - Goal Evaluation Comment: Item #833
   * - ``gol_18``
     - GOL.18
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Goal Life Cycle Status: Item #834
   * - ``gol_19``
     - GOL.19
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Goal Life Cycle Status Date/Time: Item #835
   * - ``gol_20``
     - GOL.20
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Goal Target Type: Item #836
   * - ``gol_21``
     - GOL.21
     - Optional[List[:ref:`XPN <hl7-v2_3-XPN>`]]
     - optional
     -
     - Goal Target Name: Item #837

.. _hl7-v2_3-GT1:

.. py:class:: hl7types.hl7.v2_3.segments.GT1.GT1
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
     - Set ID - Guarantor: Item #405
   * - ``gt1_2``
     - GT1.2
     - Optional[List[:ref:`CX <hl7-v2_3-CX>`]]
     - optional
     -
     - Guarantor Number: Item #406
   * - ``gt1_3``
     - GT1.3
     - Optional[List[:ref:`XPN <hl7-v2_3-XPN>`]]
     - optional
     -
     - Guarantor Name: Item #407
   * - ``gt1_4``
     - GT1.4
     - Optional[List[:ref:`XPN <hl7-v2_3-XPN>`]]
     - optional
     -
     - Guarantor Spouse Name: Item #408
   * - ``gt1_5``
     - GT1.5
     - Optional[List[:ref:`XAD <hl7-v2_3-XAD>`]]
     - optional
     -
     - Guarantor Address: Item #409
   * - ``gt1_6``
     - GT1.6
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Guarantor Ph Num- Home: Item #410
   * - ``gt1_7``
     - GT1.7
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Guarantor Ph Num-Business: Item #411
   * - ``gt1_8``
     - GT1.8
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Guarantor Date/Time of Birth: Item #412
   * - ``gt1_9``
     - GT1.9
     - Optional[str]
     - optional
     -
     - Guarantor Sex: Item #413 | Table HL70001
   * - ``gt1_10``
     - GT1.10
     - Optional[str]
     - optional
     -
     - Guarantor Type: Item #414 | Table HL70068
   * - ``gt1_11``
     - GT1.11
     - Optional[str]
     - optional
     -
     - Guarantor Relationship: Item #415 | Table HL70063
   * - ``gt1_12``
     - GT1.12
     - Optional[str]
     - optional
     -
     - Guarantor SSN: Item #416
   * - ``gt1_13``
     - GT1.13
     - Optional[str]
     - optional
     -
     - Guarantor Date - Begin: Item #417
   * - ``gt1_14``
     - GT1.14
     - Optional[str]
     - optional
     -
     - Guarantor Date - End: Item #418
   * - ``gt1_15``
     - GT1.15
     - Optional[str]
     - optional
     -
     - Guarantor Priority: Item #419
   * - ``gt1_16``
     - GT1.16
     - Optional[List[:ref:`XPN <hl7-v2_3-XPN>`]]
     - optional
     -
     - Guarantor Employer Name: Item #420
   * - ``gt1_17``
     - GT1.17
     - Optional[List[:ref:`XAD <hl7-v2_3-XAD>`]]
     - optional
     -
     - Guarantor Employer Address: Item #421
   * - ``gt1_18``
     - GT1.18
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Guarantor Employ Phone Number: Item #422
   * - ``gt1_19``
     - GT1.19
     - Optional[List[:ref:`CX <hl7-v2_3-CX>`]]
     - optional
     -
     - Guarantor Employee ID Number: Item #423
   * - ``gt1_20``
     - GT1.20
     - Optional[str]
     - optional
     -
     - Guarantor Employment Status: Item #424 | Table HL70066
   * - ``gt1_21``
     - GT1.21
     - Optional[List[:ref:`XON <hl7-v2_3-XON>`]]
     - optional
     -
     - Guarantor Organization: Item #425
   * - ``gt1_22``
     - GT1.22
     - Optional[str]
     - optional
     -
     - Guarantor Billing Hold Flag: Item #773 | Table HL70136
   * - ``gt1_23``
     - GT1.23
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Guarantor Credit Rating Code: Item #774
   * - ``gt1_24``
     - GT1.24
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Guarantor Death Date And Time: Item #775
   * - ``gt1_25``
     - GT1.25
     - Optional[str]
     - optional
     -
     - Guarantor Death Flag: Item #776 | Table HL70136
   * - ``gt1_26``
     - GT1.26
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Guarantor Charge Adjustment Code: Item #777 | Table HL70218
   * - ``gt1_27``
     - GT1.27
     - Optional[:ref:`CP <hl7-v2_3-CP>`]
     - optional
     -
     - Guarantor Household Annual Income: Item #778
   * - ``gt1_28``
     - GT1.28
     - Optional[str]
     - optional
     -
     - Guarantor Household Size: Item #779
   * - ``gt1_29``
     - GT1.29
     - Optional[List[:ref:`CX <hl7-v2_3-CX>`]]
     - optional
     -
     - Guarantor Employer ID Number: Item #780
   * - ``gt1_30``
     - GT1.30
     - Optional[str]
     - optional
     -
     - Guarantor Marital Status Code: Item #781
   * - ``gt1_31``
     - GT1.31
     - Optional[str]
     - optional
     -
     - Guarantor Hire Effective Date: Item #782
   * - ``gt1_32``
     - GT1.32
     - Optional[str]
     - optional
     -
     - Employment Stop Date: Item #783
   * - ``gt1_33``
     - GT1.33
     - Optional[str]
     - optional
     -
     - Living Dependency: Item #755 | Table HL70223
   * - ``gt1_34``
     - GT1.34
     - Optional[str]
     - optional
     -
     - Ambulatory Status: Item #145 | Table HL70009
   * - ``gt1_35``
     - GT1.35
     - Optional[str]
     - optional
     -
     - Citizenship: Item #129 | Table HL70171
   * - ``gt1_36``
     - GT1.36
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Primary Language: Item #118 | Table HL70296
   * - ``gt1_37``
     - GT1.37
     - Optional[str]
     - optional
     -
     - Living Arrangement: Item #742 | Table HL70220
   * - ``gt1_38``
     - GT1.38
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Publicity Indicator: Item #743 | Table HL70215
   * - ``gt1_39``
     - GT1.39
     - Optional[str]
     - optional
     -
     - Protection Indicator: Item #744 | Table HL70136
   * - ``gt1_40``
     - GT1.40
     - Optional[str]
     - optional
     -
     - Student Indicator: Item #745 | Table HL70231
   * - ``gt1_41``
     - GT1.41
     - Optional[str]
     - optional
     -
     - Religion: Item #120 | Table HL70006
   * - ``gt1_42``
     - GT1.42
     - Optional[:ref:`XPN <hl7-v2_3-XPN>`]
     - optional
     -
     - Mother’s Maiden Name: Item #746
   * - ``gt1_43``
     - GT1.43
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Nationality Code: Item #739 | Table HL70212
   * - ``gt1_44``
     - GT1.44
     - Optional[str]
     - optional
     -
     - Ethnic Group: Item #125 | Table HL70189
   * - ``gt1_45``
     - GT1.45
     - Optional[List[:ref:`XPN <hl7-v2_3-XPN>`]]
     - optional
     -
     - Contact Person's Name: Item #748
   * - ``gt1_46``
     - GT1.46
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Contact Person’s Telephone Number: Item #749
   * - ``gt1_47``
     - GT1.47
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Contact Reason: Item #747 | Table HL70222
   * - ``gt1_48``
     - GT1.48
     - Optional[str]
     - optional
     -
     - Contact Relationship Code: Item #784 | Table HL70063
   * - ``gt1_49``
     - GT1.49
     - Optional[str]
     - optional
     -
     - Job Title: Item #785
   * - ``gt1_50``
     - GT1.50
     - Optional[:ref:`JCC <hl7-v2_3-JCC>`]
     - optional
     -
     - Job Code/Class: Item #786
   * - ``gt1_51``
     - GT1.51
     - Optional[List[:ref:`XON <hl7-v2_3-XON>`]]
     - optional
     -
     - Guarantor Employer's Organization Name: Item #1299
   * - ``gt1_52``
     - GT1.52
     - Optional[str]
     - optional
     -
     - Handicap: Item #753 | Table HL70310
   * - ``gt1_53``
     - GT1.53
     - Optional[str]
     - optional
     -
     - Job Status: Item #752 | Table HL70311
   * - ``gt1_54``
     - GT1.54
     - Optional[:ref:`FC <hl7-v2_3-FC>`]
     - optional
     -
     - Guarantor Financial Class: Item #1231 | Table HL70064
   * - ``gt1_55``
     - GT1.55
     - Optional[str]
     - optional
     -
     - Guarantor Race: Item #1291 | Table HL70005

.. _hl7-v2_3-IN1:

.. py:class:: hl7types.hl7.v2_3.segments.IN1.IN1
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
     - Set ID - Insurance: Item #426
   * - ``in1_2``
     - IN1.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Insurance Plan ID: Item #368 | Table HL70072
   * - ``in1_3``
     - IN1.3
     - :ref:`CX <hl7-v2_3-CX>`
     - required
     -
     - Insurance Company ID: Item #428
   * - ``in1_4``
     - IN1.4
     - Optional[:ref:`XON <hl7-v2_3-XON>`]
     - optional
     -
     - Insurance Company Name: Item #429
   * - ``in1_5``
     - IN1.5
     - Optional[:ref:`XAD <hl7-v2_3-XAD>`]
     - optional
     -
     - Insurance Company Address: Item #430
   * - ``in1_6``
     - IN1.6
     - Optional[:ref:`XPN <hl7-v2_3-XPN>`]
     - optional
     -
     - Insurance Co. Contact Ppers: Item #431
   * - ``in1_7``
     - IN1.7
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Insurance Co Phone Number: Item #432
   * - ``in1_8``
     - IN1.8
     - Optional[str]
     - optional
     -
     - Group Number: Item #433
   * - ``in1_9``
     - IN1.9
     - Optional[:ref:`XON <hl7-v2_3-XON>`]
     - optional
     -
     - Group Name: Item #434
   * - ``in1_10``
     - IN1.10
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Insured's group employer ID: Item #435
   * - ``in1_11``
     - IN1.11
     - Optional[:ref:`XON <hl7-v2_3-XON>`]
     - optional
     -
     - Insured's Group Emp Name: Item #436
   * - ``in1_12``
     - IN1.12
     - Optional[str]
     - optional
     -
     - Plan Effective Date: Item #437
   * - ``in1_13``
     - IN1.13
     - Optional[str]
     - optional
     -
     - Plan Expiration Date: Item #438
   * - ``in1_14``
     - IN1.14
     - Optional[str]
     - optional
     -
     - Authorization Information: Item #439
   * - ``in1_15``
     - IN1.15
     - Optional[str]
     - optional
     -
     - Plan Type: Item #440 | Table HL70086
   * - ``in1_16``
     - IN1.16
     - Optional[:ref:`XPN <hl7-v2_3-XPN>`]
     - optional
     -
     - Name of Insured: Item #441
   * - ``in1_17``
     - IN1.17
     - Optional[str]
     - optional
     -
     - Insured's Relationship to Patient: Item #442 | Table HL70063
   * - ``in1_18``
     - IN1.18
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Insured's Date of Birth: Item #443
   * - ``in1_19``
     - IN1.19
     - Optional[:ref:`XAD <hl7-v2_3-XAD>`]
     - optional
     -
     - Insured's Address: Item #444
   * - ``in1_20``
     - IN1.20
     - Optional[str]
     - optional
     -
     - Assignment of Benefits: Item #445 | Table HL70135
   * - ``in1_21``
     - IN1.21
     - Optional[str]
     - optional
     -
     - Coordination of Benefits: Item #446 | Table HL70173
   * - ``in1_22``
     - IN1.22
     - Optional[str]
     - optional
     -
     - Coord of Ben. Priority: Item #447
   * - ``in1_23``
     - IN1.23
     - Optional[str]
     - optional
     -
     - Notice of Admission Code: Item #448 | Table HL70136
   * - ``in1_24``
     - IN1.24
     - Optional[str]
     - optional
     -
     - Notice of Admission Date: Item #449
   * - ``in1_25``
     - IN1.25
     - Optional[str]
     - optional
     -
     - Rpt of Eigibility Code: Item #450 | Table HL70136
   * - ``in1_26``
     - IN1.26
     - Optional[str]
     - optional
     -
     - Rpt of Eligibility Date: Item #451
   * - ``in1_27``
     - IN1.27
     - Optional[str]
     - optional
     -
     - Release Information Code: Item #452 | Table HL70093
   * - ``in1_28``
     - IN1.28
     - Optional[str]
     - optional
     -
     - Pre-Admit Cert (PAC): Item #453
   * - ``in1_29``
     - IN1.29
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Verification Date/Time: Item #454
   * - ``in1_30``
     - IN1.30
     - Optional[:ref:`XPN <hl7-v2_3-XPN>`]
     - optional
     -
     - Verification By: Item #455
   * - ``in1_31``
     - IN1.31
     - Optional[str]
     - optional
     -
     - Type of Agreement Code: Item #456 | Table HL70098
   * - ``in1_32``
     - IN1.32
     - Optional[str]
     - optional
     -
     - Billing Status: Item #457 | Table HL70022
   * - ``in1_33``
     - IN1.33
     - Optional[str]
     - optional
     -
     - Lifetime Reserve Days: Item #458
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
     - Company Plan Code: Item #460 | Table HL70042
   * - ``in1_36``
     - IN1.36
     - Optional[str]
     - optional
     -
     - Policy Number: Item #461
   * - ``in1_37``
     - IN1.37
     - Optional[:ref:`CP <hl7-v2_3-CP>`]
     - optional
     -
     - Policy Deductible: Item #462
   * - ``in1_38``
     - IN1.38
     - Optional[:ref:`CP <hl7-v2_3-CP>`]
     - optional
     -
     - Policy Limit - Amount: Item #463
   * - ``in1_39``
     - IN1.39
     - Optional[str]
     - optional
     -
     - Policy Limit - Days: Item #464
   * - ``in1_40``
     - IN1.40
     - Optional[:ref:`CP <hl7-v2_3-CP>`]
     - optional
     -
     - Room Rate - Semi-Private: Item #465
   * - ``in1_41``
     - IN1.41
     - Optional[:ref:`CP <hl7-v2_3-CP>`]
     - optional
     -
     - Room Rate - Private: Item #466
   * - ``in1_42``
     - IN1.42
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Insured's Employment Status: Item #467 | Table HL70066
   * - ``in1_43``
     - IN1.43
     - Optional[str]
     - optional
     -
     - Insured's Sex: Item #468 | Table HL70001
   * - ``in1_44``
     - IN1.44
     - Optional[:ref:`XAD <hl7-v2_3-XAD>`]
     - optional
     -
     - Insured's Employer Address: Item #469
   * - ``in1_45``
     - IN1.45
     - Optional[str]
     - optional
     -
     - Verification Status: Item #470
   * - ``in1_46``
     - IN1.46
     - Optional[str]
     - optional
     -
     - Prior Insurance Plan ID: Item #471 | Table HL70072
   * - ``in1_47``
     - IN1.47
     - Optional[str]
     - optional
     -
     - Coverage Type: Item #1277 | Table HL70309
   * - ``in1_48``
     - IN1.48
     - Optional[str]
     - optional
     -
     - Handicap: Item #753 | Table HL70310
   * - ``in1_49``
     - IN1.49
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Insured's ID Number: Item #1230

.. _hl7-v2_3-IN2:

.. py:class:: hl7types.hl7.v2_3.segments.IN2.IN2
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
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Insured's Employee ID: Item #472
   * - ``in2_2``
     - IN2.2
     - Optional[str]
     - optional
     -
     - Insured's Social Security Number: Item #473
   * - ``in2_3``
     - IN2.3
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Insured's Employer Name: Item #474
   * - ``in2_4``
     - IN2.4
     - Optional[str]
     - optional
     -
     - Employer Information Data: Item #475 | Table HL70139
   * - ``in2_5``
     - IN2.5
     - Optional[str]
     - optional
     -
     - Mail Claim Party: Item #476 | Table HL70137
   * - ``in2_6``
     - IN2.6
     - Optional[str]
     - optional
     -
     - Medicare Health Ins Card Number: Item #477
   * - ``in2_7``
     - IN2.7
     - Optional[:ref:`XPN <hl7-v2_3-XPN>`]
     - optional
     -
     - Medicaid Case Name: Item #478
   * - ``in2_8``
     - IN2.8
     - Optional[str]
     - optional
     -
     - Medicaid Case Number: Item #479
   * - ``in2_9``
     - IN2.9
     - Optional[:ref:`XPN <hl7-v2_3-XPN>`]
     - optional
     -
     - Champus Sponsor Name: Item #480
   * - ``in2_10``
     - IN2.10
     - Optional[str]
     - optional
     -
     - Champus ID Number: Item #481
   * - ``in2_11``
     - IN2.11
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Dependent of Champus Recipient: Item #482
   * - ``in2_12``
     - IN2.12
     - Optional[str]
     - optional
     -
     - Champus Organization: Item #483
   * - ``in2_13``
     - IN2.13
     - Optional[str]
     - optional
     -
     - Champus Station: Item #484
   * - ``in2_14``
     - IN2.14
     - Optional[str]
     - optional
     -
     - Champus Service: Item #485 | Table HL70140
   * - ``in2_15``
     - IN2.15
     - Optional[str]
     - optional
     -
     - Champus Rank/Grade: Item #486 | Table HL70141
   * - ``in2_16``
     - IN2.16
     - Optional[str]
     - optional
     -
     - Champus Status: Item #487 | Table HL70142
   * - ``in2_17``
     - IN2.17
     - Optional[str]
     - optional
     -
     - Champus Retire Date: Item #488
   * - ``in2_18``
     - IN2.18
     - Optional[str]
     - optional
     -
     - Champus Non-Avail Cert on File: Item #489 | Table HL70136
   * - ``in2_19``
     - IN2.19
     - Optional[str]
     - optional
     -
     - Baby Coverage: Item #490 | Table HL70136
   * - ``in2_20``
     - IN2.20
     - Optional[str]
     - optional
     -
     - Combine Baby Bill: Item #491 | Table HL70136
   * - ``in2_21``
     - IN2.21
     - Optional[str]
     - optional
     -
     - Blood Deductible: Item #492
   * - ``in2_22``
     - IN2.22
     - Optional[:ref:`XPN <hl7-v2_3-XPN>`]
     - optional
     -
     - Special Coverage Approval Name: Item #493
   * - ``in2_23``
     - IN2.23
     - Optional[str]
     - optional
     -
     - Special Coverage Approval Title: Item #494
   * - ``in2_24``
     - IN2.24
     - Optional[List[str]]
     - optional
     -
     - Non-Covered Insurance Code: Item #495 | Table HL70143
   * - ``in2_25``
     - IN2.25
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Payor ID: Item #496
   * - ``in2_26``
     - IN2.26
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Payor Subscriber ID: Item #497
   * - ``in2_27``
     - IN2.27
     - Optional[str]
     - optional
     -
     - Eligibility Source: Item #498 | Table HL70144
   * - ``in2_28``
     - IN2.28
     - Optional[List[str]]
     - optional
     -
     - Room Coverage Type/Amount: Item #499
   * - ``in2_29``
     - IN2.29
     - Optional[List[str]]
     - optional
     -
     - Policy Type/Amount: Item #500
   * - ``in2_30``
     - IN2.30
     - Optional[str]
     - optional
     -
     - Daily Deductible: Item #501
   * - ``in2_31``
     - IN2.31
     - Optional[str]
     - optional
     -
     - Living Dependency: Item #755 | Table HL70223
   * - ``in2_32``
     - IN2.32
     - Optional[str]
     - optional
     -
     - Ambulatory Status: Item #145 | Table HL70009
   * - ``in2_33``
     - IN2.33
     - Optional[str]
     - optional
     -
     - Citizenship: Item #129 | Table HL70171
   * - ``in2_34``
     - IN2.34
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Primary Language: Item #118 | Table HL70296
   * - ``in2_35``
     - IN2.35
     - Optional[str]
     - optional
     -
     - Living Arrangement: Item #742 | Table HL70220
   * - ``in2_36``
     - IN2.36
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Publicity Indicator: Item #743 | Table HL70215
   * - ``in2_37``
     - IN2.37
     - Optional[str]
     - optional
     -
     - Protection Indicator: Item #744 | Table HL70136
   * - ``in2_38``
     - IN2.38
     - Optional[str]
     - optional
     -
     - Student Indicator: Item #745 | Table HL70231
   * - ``in2_39``
     - IN2.39
     - Optional[str]
     - optional
     -
     - Religion: Item #120 | Table HL70006
   * - ``in2_40``
     - IN2.40
     - Optional[:ref:`XPN <hl7-v2_3-XPN>`]
     - optional
     -
     - Mother’s Maiden Name: Item #746
   * - ``in2_41``
     - IN2.41
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Nationality Code: Item #739 | Table HL70212
   * - ``in2_42``
     - IN2.42
     - Optional[str]
     - optional
     -
     - Ethnic Group: Item #125 | Table HL70189
   * - ``in2_43``
     - IN2.43
     - Optional[List[str]]
     - optional
     -
     - Marital Status: Item #119 | Table HL70002
   * - ``in2_44``
     - IN2.44
     - Optional[str]
     - optional
     -
     - Employment Start Date: Item #787
   * - ``in2_45``
     - IN2.45
     - Optional[str]
     - optional
     -
     - Employment Stop Date: Item #783
   * - ``in2_46``
     - IN2.46
     - Optional[str]
     - optional
     -
     - Job Title: Item #785
   * - ``in2_47``
     - IN2.47
     - Optional[:ref:`JCC <hl7-v2_3-JCC>`]
     - optional
     -
     - Job Code/Class: Item #786
   * - ``in2_48``
     - IN2.48
     - Optional[str]
     - optional
     -
     - Job Status: Item #752 | Table HL70311
   * - ``in2_49``
     - IN2.49
     - Optional[List[:ref:`XPN <hl7-v2_3-XPN>`]]
     - optional
     -
     - Employer Contact Person Name: Item #789
   * - ``in2_50``
     - IN2.50
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Employer Contact Person Phone Number: Item #790
   * - ``in2_51``
     - IN2.51
     - Optional[str]
     - optional
     -
     - Employer Contact Reason: Item #791 | Table HL70222
   * - ``in2_52``
     - IN2.52
     - Optional[List[:ref:`XPN <hl7-v2_3-XPN>`]]
     - optional
     -
     - Insured’s Contact Person’s Name: Item #792
   * - ``in2_53``
     - IN2.53
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Insured’s Contact Person Telephone Number: Item #793
   * - ``in2_54``
     - IN2.54
     - Optional[List[str]]
     - optional
     -
     - Insured’s Contact Person Reason: Item #794 | Table HL70222
   * - ``in2_55``
     - IN2.55
     - Optional[str]
     - optional
     -
     - Relationship To The Patient Start Date: Item #795
   * - ``in2_56``
     - IN2.56
     - Optional[List[str]]
     - optional
     -
     - Relationship To The Patient Stop Date: Item #796
   * - ``in2_57``
     - IN2.57
     - Optional[str]
     - optional
     -
     - Insurance Co. Contact Reason: Item #797 | Table HL70232
   * - ``in2_58``
     - IN2.58
     - Optional[:ref:`XTN <hl7-v2_3-XTN>`]
     - optional
     -
     - Insurance Co. Contact Phone Number: Item #798
   * - ``in2_59``
     - IN2.59
     - Optional[str]
     - optional
     -
     - Policy Scope: Item #799 | Table HL70312
   * - ``in2_60``
     - IN2.60
     - Optional[str]
     - optional
     -
     - Policy Source: Item #800 | Table HL70313
   * - ``in2_61``
     - IN2.61
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Patient Member Number: Item #801
   * - ``in2_62``
     - IN2.62
     - Optional[str]
     - optional
     -
     - Guarantor’s Relationship To Insured: Item #802 | Table HL70063
   * - ``in2_63``
     - IN2.63
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Insured’s Telephone Number - Home: Item #803
   * - ``in2_64``
     - IN2.64
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Insured’s Employer Telephone Number: Item #804
   * - ``in2_65``
     - IN2.65
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Military Handicapped Program: Item #805
   * - ``in2_66``
     - IN2.66
     - Optional[str]
     - optional
     -
     - Suspend Flag: Item #806 | Table HL70136
   * - ``in2_67``
     - IN2.67
     - Optional[str]
     - optional
     -
     - Co-pay Limit Flag: Item #807 | Table HL70136
   * - ``in2_68``
     - IN2.68
     - Optional[str]
     - optional
     -
     - Stoploss Limit Flag: Item #808 | Table HL70136
   * - ``in2_69``
     - IN2.69
     - Optional[List[:ref:`XON <hl7-v2_3-XON>`]]
     - optional
     -
     - Insured Organization Name And ID: Item #809
   * - ``in2_70``
     - IN2.70
     - Optional[List[:ref:`XON <hl7-v2_3-XON>`]]
     - optional
     -
     - Insured Employer Organization Name And ID: Item #810
   * - ``in2_71``
     - IN2.71
     - Optional[str]
     - optional
     -
     - Race: Item #113 | Table HL70005
   * - ``in2_72``
     - IN2.72
     - Optional[str]
     - optional
     -
     - Patient Relationship to Insured: Item #811

.. _hl7-v2_3-IN3:

.. py:class:: hl7types.hl7.v2_3.segments.IN3.IN3
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
     - Set ID - Insurance Certification: Item #502
   * - ``in3_2``
     - IN3.2
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Certification Number: Item #503
   * - ``in3_3``
     - IN3.3
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Certified By: Item #504
   * - ``in3_4``
     - IN3.4
     - Optional[str]
     - optional
     -
     - Certification Required: Item #505 | Table HL70136
   * - ``in3_5``
     - IN3.5
     - Optional[str]
     - optional
     -
     - Penalty: Item #506 | Table HL70148
   * - ``in3_6``
     - IN3.6
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Certification Date/Time: Item #507
   * - ``in3_7``
     - IN3.7
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Certification Modify Date/Time: Item #508
   * - ``in3_8``
     - IN3.8
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Operator: Item #509
   * - ``in3_9``
     - IN3.9
     - Optional[str]
     - optional
     -
     - Certification Begin Date: Item #510
   * - ``in3_10``
     - IN3.10
     - Optional[str]
     - optional
     -
     - Certification End Date: Item #511
   * - ``in3_11``
     - IN3.11
     - Optional[str]
     - optional
     -
     - Days: Item #512 | Table HL70149
   * - ``in3_12``
     - IN3.12
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Non-Concur Code/Description: Item #513 | Table HL70233
   * - ``in3_13``
     - IN3.13
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Non-Concur Effective Date/Time: Item #514
   * - ``in3_14``
     - IN3.14
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Physician Reviewer: Item #515
   * - ``in3_15``
     - IN3.15
     - Optional[str]
     - optional
     -
     - Certification Contact: Item #516
   * - ``in3_16``
     - IN3.16
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Certification Contact Phone Number: Item #517
   * - ``in3_17``
     - IN3.17
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Appeal Reason: Item #518
   * - ``in3_18``
     - IN3.18
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Certification Agency: Item #519
   * - ``in3_19``
     - IN3.19
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Certification Agency Phone Number: Item #520
   * - ``in3_20``
     - IN3.20
     - Optional[List[str]]
     - optional
     -
     - Pre-Certification required/Window: Item #521
   * - ``in3_21``
     - IN3.21
     - Optional[str]
     - optional
     -
     - Case Manager: Item #522
   * - ``in3_22``
     - IN3.22
     - Optional[str]
     - optional
     -
     - Second Opinion Date: Item #523
   * - ``in3_23``
     - IN3.23
     - Optional[str]
     - optional
     -
     - Second Opinion Status: Item #524 | Table HL70151
   * - ``in3_24``
     - IN3.24
     - Optional[List[str]]
     - optional
     -
     - Second Opinion Documentation Received: Item #525 | Table HL70152
   * - ``in3_25``
     - IN3.25
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Second Opinion Physician: Item #526

.. _hl7-v2_3-LCC:

.. py:class:: hl7types.hl7.v2_3.segments.LCC.LCC
   :noindex:

   HL7 v2 LCC segment.

LCC
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
   * - ``lcc_1``
     - LCC.1
     - :ref:`PL <hl7-v2_3-PL>`
     - required
     -
     - Primary Key Value: Item #979
   * - ``lcc_2``
     - LCC.2
     - str
     - required
     -
     - Location Department: Item #964 | Table HL70264
   * - ``lcc_3``
     - LCC.3
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Accommodation Type: Item #980
   * - ``lcc_4``
     - LCC.4
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Charge Code: Item #981

.. _hl7-v2_3-LCH:

.. py:class:: hl7types.hl7.v2_3.segments.LCH.LCH
   :noindex:

   HL7 v2 LCH segment.

LCH
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
   * - ``lch_1``
     - LCH.1
     - :ref:`PL <hl7-v2_3-PL>`
     - required
     -
     - Primary Key Value: Item #943
   * - ``lch_2``
     - LCH.2
     - Optional[str]
     - optional
     -
     - Segment Action Code: Item #763 | Table HL70206
   * - ``lch_3``
     - LCH.3
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Segment Unique Key: Item #764
   * - ``lch_4``
     - LCH.4
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Location Characteristic ID: Item #1295 | Table HL70324
   * - ``lch_5``
     - LCH.5
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Location Characteristic Value: Item #1294

.. _hl7-v2_3-LDP:

.. py:class:: hl7types.hl7.v2_3.segments.LDP.LDP
   :noindex:

   HL7 v2 LDP segment.

LDP
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
   * - ``ldp_1``
     - LDP.1
     - :ref:`PL <hl7-v2_3-PL>`
     - required
     -
     - LDP Primary Key Value: Item #963
   * - ``ldp_2``
     - LDP.2
     - str
     - required
     -
     - Location Department: Item #964 | Table HL70264
   * - ``ldp_3``
     - LDP.3
     - Optional[List[str]]
     - optional
     -
     - Location Service: Item #965 | Table HL70069
   * - ``ldp_4``
     - LDP.4
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Speciality Type: Item #966 | Table HL70265
   * - ``ldp_5``
     - LDP.5
     - Optional[List[str]]
     - optional
     -
     - Valid Patient Classes: Item #967 | Table HL70004
   * - ``ldp_6``
     - LDP.6
     - Optional[str]
     - optional
     -
     - Active/Inactive Flag: Item #675 | Table HL70183
   * - ``ldp_7``
     - LDP.7
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Activation Date: Item #969
   * - ``ldp_8``
     - LDP.8
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Inactivation Date - LDP: Item #970
   * - ``ldp_9``
     - LDP.9
     - Optional[str]
     - optional
     -
     - Inactivated Reason: Item #971
   * - ``ldp_10``
     - LDP.10
     - Optional[List[:ref:`VH <hl7-v2_3-VH>`]]
     - optional
     -
     - Visiting Hours: Item #976 | Table HL70267
   * - ``ldp_11``
     - LDP.11
     - Optional[:ref:`XTN <hl7-v2_3-XTN>`]
     - optional
     -
     - Contact Phone: Item #978

.. _hl7-v2_3-LOC:

.. py:class:: hl7types.hl7.v2_3.segments.LOC.LOC
   :noindex:

   HL7 v2 LOC segment.

LOC
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
   * - ``loc_1``
     - LOC.1
     - :ref:`PL <hl7-v2_3-PL>`
     - required
     -
     - Primary Key Value: Item #943
   * - ``loc_2``
     - LOC.2
     - Optional[str]
     - optional
     -
     - Location Description: Item #944
   * - ``loc_3``
     - LOC.3
     - List[str]
     - required
     -
     - Location Type: Item #945 | Table HL70260
   * - ``loc_4``
     - LOC.4
     - Optional[:ref:`XON <hl7-v2_3-XON>`]
     - optional
     -
     - Organization Name: Item #947
   * - ``loc_5``
     - LOC.5
     - Optional[:ref:`XAD <hl7-v2_3-XAD>`]
     - optional
     -
     - Location Address: Item #948
   * - ``loc_6``
     - LOC.6
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Location Phone: Item #949
   * - ``loc_7``
     - LOC.7
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - License Number: Item #951
   * - ``loc_8``
     - LOC.8
     - Optional[List[str]]
     - optional
     -
     - Location Equipment: Item #953 | Table HL70261

.. _hl7-v2_3-LRL:

.. py:class:: hl7types.hl7.v2_3.segments.LRL.LRL
   :noindex:

   HL7 v2 LRL segment.

LRL
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
   * - ``lrl_1``
     - LRL.1
     - :ref:`PL <hl7-v2_3-PL>`
     - required
     -
     - Primary Key Value: Item #943
   * - ``lrl_2``
     - LRL.2
     - Optional[str]
     - optional
     -
     - Segment Action Code: Item #763 | Table HL70206
   * - ``lrl_3``
     - LRL.3
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Segment Unique Key: Item #764
   * - ``lrl_4``
     - LRL.4
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Location Relationship ID: Item #1227 | Table HL70325
   * - ``lrl_5``
     - LRL.5
     - Optional[:ref:`XON <hl7-v2_3-XON>`]
     - optional
     -
     - Organizational Location Relationship Value: Item #1301
   * - ``lrl_6``
     - LRL.6
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Patient Location Relationship Value: Item #1292

.. _hl7-v2_3-MFA:

.. py:class:: hl7types.hl7.v2_3.segments.MFA.MFA
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
     - Record-Level Event Code: Item #664 | Table HL70180
   * - ``mfa_2``
     - MFA.2
     - Optional[str]
     - optional
     -
     - MFN Control ID: Item #665
   * - ``mfa_3``
     - MFA.3
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Event Completion Date/Time: Item #668
   * - ``mfa_4``
     - MFA.4
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Error Return Code and/or Text: Item #669 | Table HL70181
   * - ``mfa_5``
     - MFA.5
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Primary Key Value: Item #667

.. _hl7-v2_3-MFE:

.. py:class:: hl7types.hl7.v2_3.segments.MFE.MFE
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
     - Record-Level Event Code: Item #664 | Table HL70180
   * - ``mfe_2``
     - MFE.2
     - Optional[str]
     - optional
     -
     - MFN Control ID: Item #665
   * - ``mfe_3``
     - MFE.3
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Effective Date/Time: Item #662
   * - ``mfe_4``
     - MFE.4
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Primary Key Value: Item #667

.. _hl7-v2_3-MFI:

.. py:class:: hl7types.hl7.v2_3.segments.MFI.MFI
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
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Master File Identifier: Item #658 | Table HL70175
   * - ``mfi_2``
     - MFI.2
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     -
     - Master File Application Identifier: Item #659 | Table HL70176
   * - ``mfi_3``
     - MFI.3
     - str
     - required
     -
     - File-Level Event Code: Item #660 | Table HL70178
   * - ``mfi_4``
     - MFI.4
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Entered Date/Time: Item #661
   * - ``mfi_5``
     - MFI.5
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Effective Date/Time: Item #662
   * - ``mfi_6``
     - MFI.6
     - str
     - required
     -
     - Response Level Code: Item #663 | Table HL70179

.. _hl7-v2_3-MRG:

.. py:class:: hl7types.hl7.v2_3.segments.MRG.MRG
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
     - Optional[List[:ref:`CX <hl7-v2_3-CX>`]]
     - optional
     -
     - Prior Patient ID - Internal: Item #211
   * - ``mrg_2``
     - MRG.2
     - Optional[List[:ref:`CX <hl7-v2_3-CX>`]]
     - optional
     -
     - Prior Alternate Patient ID: Item #212
   * - ``mrg_3``
     - MRG.3
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Prior Patient Account Number: Item #213
   * - ``mrg_4``
     - MRG.4
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Prior Patient ID - External: Item #214
   * - ``mrg_5``
     - MRG.5
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Prior Visit Number: Item #1279
   * - ``mrg_6``
     - MRG.6
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Prior Alternate Visit ID: Item #1280
   * - ``mrg_7``
     - MRG.7
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Prior Patient Name: Item #1281

.. _hl7-v2_3-MSA:

.. py:class:: hl7types.hl7.v2_3.segments.MSA.MSA
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
     - Delayed Acknowledgement Type: Item #22 | Table HL70102
   * - ``msa_6``
     - MSA.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Error Condition: Item #23

.. _hl7-v2_3-MSH:

.. py:class:: hl7types.hl7.v2_3.segments.MSH.MSH
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
     - Field Separator: Item #1
   * - ``msh_2``
     - MSH.2
     - str
     - optional
     -
     - Encoding Characters: Item #2
   * - ``msh_3``
     - MSH.3
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     -
     - Sending Application: Item #3
   * - ``msh_4``
     - MSH.4
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     -
     - Sending Facility: Item #4
   * - ``msh_5``
     - MSH.5
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     -
     - Receiving Application: Item #5
   * - ``msh_6``
     - MSH.6
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     -
     - Receiving Facility: Item #6
   * - ``msh_7``
     - MSH.7
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date / Time of Message: Item #7
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
     - Message Type: Item #9
   * - ``msh_10``
     - MSH.10
     - str
     - required
     -
     - Message Control ID: Item #10
   * - ``msh_11``
     - MSH.11
     - :ref:`PT <hl7-v2_3-PT>`
     - required
     -
     - Processing ID: Item #11
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
     - Sequence Number: Item #13
   * - ``msh_14``
     - MSH.14
     - Optional[str]
     - optional
     -
     - Continuation Pointer: Item #14
   * - ``msh_15``
     - MSH.15
     - Optional[str]
     - optional
     -
     - Accept Acknowledgement Type: Item #15 | Table HL70155
   * - ``msh_16``
     - MSH.16
     - Optional[str]
     - optional
     -
     - Application Acknowledgement Type: Item #16 | Table HL70155
   * - ``msh_17``
     - MSH.17
     - Optional[str]
     - optional
     -
     - Country Code: Item #17
   * - ``msh_18``
     - MSH.18
     - Optional[str]
     - optional
     -
     - Character Set: Item #692 | Table HL70211
   * - ``msh_19``
     - MSH.19
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Principal Language of Message: Item #693

.. _hl7-v2_3-NCK:

.. py:class:: hl7types.hl7.v2_3.segments.NCK.NCK
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - System Date/Time: Item #1172

.. _hl7-v2_3-NK1:

.. py:class:: hl7types.hl7.v2_3.segments.NK1.NK1
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
     - Optional[List[:ref:`XPN <hl7-v2_3-XPN>`]]
     - optional
     -
     - Name: Item #191
   * - ``nk1_3``
     - NK1.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Relationship: Item #192 | Table HL70063
   * - ``nk1_4``
     - NK1.4
     - Optional[List[:ref:`XAD <hl7-v2_3-XAD>`]]
     - optional
     -
     - Address: Item #193
   * - ``nk1_5``
     - NK1.5
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Phone Number: Item #194
   * - ``nk1_6``
     - NK1.6
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Business Phone Number: Item #195
   * - ``nk1_7``
     - NK1.7
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
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
     - Next of Kin/Associated Parties Job Title: Item #199
   * - ``nk1_11``
     - NK1.11
     - Optional[:ref:`JCC <hl7-v2_3-JCC>`]
     - optional
     -
     - Next of Kin Job/Associated Parties Code/Class: Item #200
   * - ``nk1_12``
     - NK1.12
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Next of Kin/Associated Parties Employee Number: Item #201
   * - ``nk1_13``
     - NK1.13
     - Optional[List[:ref:`XON <hl7-v2_3-XON>`]]
     - optional
     -
     - Organization Name: Item #202
   * - ``nk1_14``
     - NK1.14
     - Optional[List[str]]
     - optional
     -
     - Marital Status: Item #119 | Table HL70002
   * - ``nk1_15``
     - NK1.15
     - Optional[str]
     - optional
     -
     - Sex: Item #111 | Table HL70001
   * - ``nk1_16``
     - NK1.16
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date of Birth: Item #110
   * - ``nk1_17``
     - NK1.17
     - Optional[str]
     - optional
     -
     - Living Dependency: Item #755 | Table HL70223
   * - ``nk1_18``
     - NK1.18
     - Optional[str]
     - optional
     -
     - Ambulatory Status: Item #145 | Table HL70009
   * - ``nk1_19``
     - NK1.19
     - Optional[str]
     - optional
     -
     - Citizenship: Item #129 | Table HL70171
   * - ``nk1_20``
     - NK1.20
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Primary Language: Item #118 | Table HL70296
   * - ``nk1_21``
     - NK1.21
     - Optional[str]
     - optional
     -
     - Living Arrangement: Item #742 | Table HL70220
   * - ``nk1_22``
     - NK1.22
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Publicity Indicator: Item #743 | Table HL70215
   * - ``nk1_23``
     - NK1.23
     - Optional[str]
     - optional
     -
     - Protection Indicator: Item #744 | Table HL70136
   * - ``nk1_24``
     - NK1.24
     - Optional[str]
     - optional
     -
     - Student Indicator: Item #745 | Table HL70231
   * - ``nk1_25``
     - NK1.25
     - Optional[str]
     - optional
     -
     - Religion: Item #120 | Table HL70006
   * - ``nk1_26``
     - NK1.26
     - Optional[:ref:`XPN <hl7-v2_3-XPN>`]
     - optional
     -
     - Mother’s Maiden Name: Item #746
   * - ``nk1_27``
     - NK1.27
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Nationality Code: Item #739 | Table HL70212
   * - ``nk1_28``
     - NK1.28
     - Optional[str]
     - optional
     -
     - Ethnic Group: Item #125 | Table HL70189
   * - ``nk1_29``
     - NK1.29
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Contact Reason: Item #747 | Table HL70222
   * - ``nk1_30``
     - NK1.30
     - Optional[List[:ref:`XPN <hl7-v2_3-XPN>`]]
     - optional
     -
     - Contact Person's Name: Item #748
   * - ``nk1_31``
     - NK1.31
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Contact Person’s Telephone Number: Item #749
   * - ``nk1_32``
     - NK1.32
     - Optional[List[:ref:`XAD <hl7-v2_3-XAD>`]]
     - optional
     -
     - Contact Person’s Address: Item #750
   * - ``nk1_33``
     - NK1.33
     - Optional[List[:ref:`CX <hl7-v2_3-CX>`]]
     - optional
     -
     - Associated Party’s Identifiers: Item #751
   * - ``nk1_34``
     - NK1.34
     - Optional[str]
     - optional
     -
     - Job Status: Item #752 | Table HL70311
   * - ``nk1_35``
     - NK1.35
     - Optional[str]
     - optional
     -
     - Race: Item #113 | Table HL70005
   * - ``nk1_36``
     - NK1.36
     - Optional[str]
     - optional
     -
     - Handicap: Item #753 | Table HL70310
   * - ``nk1_37``
     - NK1.37
     - Optional[str]
     - optional
     -
     - Contact Person Social Security Number: Item #754

.. _hl7-v2_3-NPU:

.. py:class:: hl7types.hl7.v2_3.segments.NPU.NPU
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
     - :ref:`PL <hl7-v2_3-PL>`
     - required
     -
     - Bed Location: Item #209 | Table HL70079
   * - ``npu_2``
     - NPU.2
     - Optional[str]
     - optional
     -
     - Bed Status: Item #170 | Table HL70116

.. _hl7-v2_3-NSC:

.. py:class:: hl7types.hl7.v2_3.segments.NSC.NSC
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
     - Optional[str]
     - optional
     -
     - Network Change Type: Item #1188
   * - ``nsc_2``
     - NSC.2
     - Optional[str]
     - optional
     -
     - Current CPU: Item #1189
   * - ``nsc_3``
     - NSC.3
     - Optional[str]
     - optional
     -
     - Current Fileserver: Item #1190
   * - ``nsc_4``
     - NSC.4
     - Optional[str]
     - optional
     -
     - Current Application: Item #1191
   * - ``nsc_5``
     - NSC.5
     - Optional[str]
     - optional
     -
     - Current Facility: Item #1192
   * - ``nsc_6``
     - NSC.6
     - Optional[str]
     - optional
     -
     - New CPU: Item #1193 | Table HL70206
   * - ``nsc_7``
     - NSC.7
     - Optional[str]
     - optional
     -
     - New Fileserver: Item #1194
   * - ``nsc_8``
     - NSC.8
     - Optional[str]
     - optional
     -
     - New Application: Item #1195

.. _hl7-v2_3-NST:

.. py:class:: hl7types.hl7.v2_3.segments.NST.NST
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
     - Optional[str]
     - optional
     -
     - Statistics Available: Item #1173 | Table HL70125
   * - ``nst_2``
     - NST.2
     - Optional[str]
     - optional
     -
     - Source Identifier: Item #1174
   * - ``nst_3``
     - NST.3
     - Optional[str]
     - optional
     -
     - Source Type: Item #1175
   * - ``nst_4``
     - NST.4
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Statistics Start: Item #1176
   * - ``nst_5``
     - NST.5
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Statistics End: Item #1177
   * - ``nst_6``
     - NST.6
     - Optional[str]
     - optional
     -
     - Receive Character Count: Item #1178
   * - ``nst_7``
     - NST.7
     - Optional[str]
     - optional
     -
     - Send Character Count: Item #1179
   * - ``nst_8``
     - NST.8
     - Optional[str]
     - optional
     -
     - Messages Received: Item #1180
   * - ``nst_9``
     - NST.9
     - Optional[str]
     - optional
     -
     - Messages Sent: Item #1181
   * - ``nst_10``
     - NST.10
     - Optional[str]
     - optional
     -
     - Checksum Errors Received: Item #1182
   * - ``nst_11``
     - NST.11
     - Optional[str]
     - optional
     -
     - Length Errors Received: Item #1183
   * - ``nst_12``
     - NST.12
     - Optional[str]
     - optional
     -
     - Other Errors Received: Item #1184
   * - ``nst_13``
     - NST.13
     - Optional[str]
     - optional
     -
     - Connect Timeouts: Item #1185
   * - ``nst_14``
     - NST.14
     - Optional[str]
     - optional
     -
     - Receive Timeouts: Item #1186
   * - ``nst_15``
     - NST.15
     - Optional[str]
     - optional
     -
     - Network Errors: Item #1187

.. _hl7-v2_3-NTE:

.. py:class:: hl7types.hl7.v2_3.segments.NTE.NTE
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
     - Optional[List[:ref:`FT <hl7-v2_3-FT>`]]
     - optional
     -
     - Comment: Item #98

.. _hl7-v2_3-OBR:

.. py:class:: hl7types.hl7.v2_3.segments.OBR.OBR
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
     - Optional[List[:ref:`EI <hl7-v2_3-EI>`]]
     - optional
     -
     - Placer Order Number: Item #216
   * - ``obr_3``
     - OBR.3
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Filler Order Number: Item #217
   * - ``obr_4``
     - OBR.4
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Universal Service Identifier: Item #238
   * - ``obr_5``
     - OBR.5
     - Optional[str]
     - optional
     -
     - Priority: Item #239
   * - ``obr_6``
     - OBR.6
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Requested Date/Time: Item #240
   * - ``obr_7``
     - OBR.7
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Observation Date/Time: Item #241
   * - ``obr_8``
     - OBR.8
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Observation End Date/Time: Item #242
   * - ``obr_9``
     - OBR.9
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     -
     - Collection Volume: Item #243
   * - ``obr_10``
     - OBR.10
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Collector Identifier: Item #244
   * - ``obr_11``
     - OBR.11
     - Optional[str]
     - optional
     -
     - Specimen Action Code: Item #245 | Table HL70065
   * - ``obr_12``
     - OBR.12
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Danger Code: Item #246
   * - ``obr_13``
     - OBR.13
     - Optional[str]
     - optional
     -
     - Relevant Clinical Information: Item #247
   * - ``obr_14``
     - OBR.14
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Specimen Received Date/Time: Item #248
   * - ``obr_15``
     - OBR.15
     - Optional[str]
     - optional
     -
     - Specimen Source: Item #249 | Table HL70070
   * - ``obr_16``
     - OBR.16
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Ordering Provider: Item #226
   * - ``obr_17``
     - OBR.17
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Order Callback Phone Number: Item #250
   * - ``obr_18``
     - OBR.18
     - Optional[str]
     - optional
     -
     - Placer Field 1: Item #251
   * - ``obr_19``
     - OBR.19
     - Optional[str]
     - optional
     -
     - Placer Field 2: Item #252
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Results Rpt/Status Chng - Date/Time: Item #255
   * - ``obr_23``
     - OBR.23
     - Optional[str]
     - optional
     -
     - Charge To Practice: Item #256
   * - ``obr_24``
     - OBR.24
     - Optional[str]
     - optional
     -
     - Diagnostic Service Section ID: Item #257 | Table HL70074
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
     - :ref:`TQ <hl7-v2_3-TQ>`
     - required
     -
     - Quantity/Timing: Item #221
   * - ``obr_28``
     - OBR.28
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
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
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Reason For Study: Item #263
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Scheduled Date/Time: Item #268
   * - ``obr_37``
     - OBR.37
     - Optional[str]
     - optional
     -
     - Number Of Sample Containers: Item #1028
   * - ``obr_38``
     - OBR.38
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Transport Logistics Of Collected Sample: Item #1029
   * - ``obr_39``
     - OBR.39
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Collector’s Comment: Item #1030
   * - ``obr_40``
     - OBR.40
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Transport Arrangement Responsibility: Item #1031
   * - ``obr_41``
     - OBR.41
     - Optional[str]
     - optional
     -
     - Transport Arranged: Item #1032 | Table HL70224
   * - ``obr_42``
     - OBR.42
     - Optional[str]
     - optional
     -
     - Escort Required: Item #1033 | Table HL70225
   * - ``obr_43``
     - OBR.43
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Planned Patient Transport Comment: Item #1034

.. _hl7-v2_3-OBX:

.. py:class:: hl7types.hl7.v2_3.segments.OBX.OBX
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
     - Set ID - OBX: Item #569
   * - ``obx_2``
     - OBX.2
     - str
     - required
     -
     - Value Type: Item #570 | Table HL70125
   * - ``obx_3``
     - OBX.3
     - :ref:`CE <hl7-v2_3-CE>`
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
     - Optional[List[str]]
     - optional
     -
     - Observation Value: Item #573
   * - ``obx_6``
     - OBX.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
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
     - Observ Result Status: Item #579 | Table HL70085
   * - ``obx_12``
     - OBX.12
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date Last Obs Normal Values: Item #580
   * - ``obx_13``
     - OBX.13
     - Optional[str]
     - optional
     -
     - User Defined Access Checks: Item #581
   * - ``obx_14``
     - OBX.14
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date/Time of the Observation: Item #582
   * - ``obx_15``
     - OBX.15
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Producer's ID: Item #583
   * - ``obx_16``
     - OBX.16
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Responsible Observer: Item #584
   * - ``obx_17``
     - OBX.17
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Observation Method: Item #936

.. _hl7-v2_3-ODS:

.. py:class:: hl7types.hl7.v2_3.segments.ODS.ODS
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
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Service Period: Item #270
   * - ``ods_3``
     - ODS.3
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Diet, Supplement, or Preference Code: Item #271
   * - ``ods_4``
     - ODS.4
     - Optional[str]
     - optional
     -
     - Text Instruction: Item #272

.. _hl7-v2_3-ODT:

.. py:class:: hl7types.hl7.v2_3.segments.ODT.ODT
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
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Tray Type: Item #273 | Table HL70160
   * - ``odt_2``
     - ODT.2
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Service Period: Item #270
   * - ``odt_3``
     - ODT.3
     - Optional[str]
     - optional
     -
     - Text Instruction: Item #272

.. _hl7-v2_3-OM1:

.. py:class:: hl7types.hl7.v2_3.segments.OM1.OM1
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
     - Sequence Number - Test/ Observation Master File: Item #586
   * - ``om1_2``
     - OM1.2
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Producer's Test/Observation ID: Item #587
   * - ``om1_3``
     - OM1.3
     - Optional[List[str]]
     - optional
     -
     - Permitted Data Types: Item #588 | Table HL70125
   * - ``om1_4``
     - OM1.4
     - str
     - required
     -
     - Specimen Required: Item #589 | Table HL70136
   * - ``om1_5``
     - OM1.5
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Producer ID: Item #590
   * - ``om1_6``
     - OM1.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Observation Description: Item #591
   * - ``om1_7``
     - OM1.7
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Other Test/Observation IDs for the Observation: Item #592
   * - ``om1_8``
     - OM1.8
     - List[str]
     - required
     -
     - Other Names: Item #593
   * - ``om1_9``
     - OM1.9
     - Optional[str]
     - optional
     -
     - Preferred Report Name for the Observation: Item #594
   * - ``om1_10``
     - OM1.10
     - Optional[str]
     - optional
     -
     - Preferred Short Name or Mnemonic for Observation: Item #595
   * - ``om1_11``
     - OM1.11
     - Optional[str]
     - optional
     -
     - Preferred Long Name for the Observation: Item #596
   * - ``om1_12``
     - OM1.12
     - Optional[str]
     - optional
     -
     - Orderability: Item #597 | Table HL70136
   * - ``om1_13``
     - OM1.13
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Identity of Instrument Used to Perfrom this Study: Item #598
   * - ``om1_14``
     - OM1.14
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Coded Representation of Method: Item #599
   * - ``om1_15``
     - OM1.15
     - Optional[str]
     - optional
     -
     - Portable: Item #600 | Table HL70136
   * - ``om1_16``
     - OM1.16
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Observation Producing Department/Section: Item #601
   * - ``om1_17``
     - OM1.17
     - Optional[str]
     - optional
     -
     - Telephone Number of Section: Item #602
   * - ``om1_18``
     - OM1.18
     - Optional[str]
     - optional
     -
     - Nature of Test/Observation: Item #603 | Table HL70174
   * - ``om1_19``
     - OM1.19
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Report Subheader: Item #604
   * - ``om1_20``
     - OM1.20
     - Optional[str]
     - optional
     -
     - Report Display Order: Item #605
   * - ``om1_21``
     - OM1.21
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date/Time Stamp for any change in Def Attri for Obs: Item #606
   * - ``om1_22``
     - OM1.22
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Effective Date/Time of Change in Test Proc. that make Results Non-Comparable: Item #607
   * - ``om1_23``
     - OM1.23
     - Optional[str]
     - optional
     -
     - Typical Turn-Around Time: Item #608
   * - ``om1_24``
     - OM1.24
     - Optional[str]
     - optional
     -
     - Processing Time: Item #609
   * - ``om1_25``
     - OM1.25
     - Optional[List[str]]
     - optional
     -
     - Processing Priority: Item #610 | Table HL70168
   * - ``om1_26``
     - OM1.26
     - Optional[str]
     - optional
     -
     - Reporting Priority: Item #611 | Table HL70169
   * - ``om1_27``
     - OM1.27
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Outside Site(s) Where Observation may be Performed: Item #612
   * - ``om1_28``
     - OM1.28
     - Optional[:ref:`AD <hl7-v2_3-AD>`]
     - optional
     -
     - Address of Outside Site(s): Item #613
   * - ``om1_29``
     - OM1.29
     - Optional[str]
     - optional
     -
     - Phone Number of Outside Site: Item #614
   * - ``om1_30``
     - OM1.30
     - Optional[str]
     - optional
     -
     - Confidentiality Code: Item #615 | Table HL70177
   * - ``om1_31``
     - OM1.31
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Observations Required to Interpret the Observation: Item #616
   * - ``om1_32``
     - OM1.32
     - Optional[:ref:`TX <hl7-v2_3-TX>`]
     - optional
     -
     - Interpretation of Observations: Item #617
   * - ``om1_33``
     - OM1.33
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Contraindications to Observations: Item #618
   * - ``om1_34``
     - OM1.34
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Reflex Tests/Observations: Item #619
   * - ``om1_35``
     - OM1.35
     - Optional[str]
     - optional
     -
     - Rules that Trigger Reflex Testing: Item #620
   * - ``om1_36``
     - OM1.36
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Fixed Canned Message: Item #621
   * - ``om1_37``
     - OM1.37
     - Optional[:ref:`TX <hl7-v2_3-TX>`]
     - optional
     -
     - Patient Preparation: Item #622
   * - ``om1_38``
     - OM1.38
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Procedure Medication: Item #623
   * - ``om1_39``
     - OM1.39
     - Optional[:ref:`TX <hl7-v2_3-TX>`]
     - optional
     -
     - Factors that may Effect the Observation: Item #624
   * - ``om1_40``
     - OM1.40
     - Optional[List[str]]
     - optional
     -
     - Test/Observation Performance Schedule: Item #625
   * - ``om1_41``
     - OM1.41
     - Optional[:ref:`TX <hl7-v2_3-TX>`]
     - optional
     -
     - Description of Test Methods: Item #626
   * - ``om1_42``
     - OM1.42
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Kind of Quantity Observed: Item #937
   * - ``om1_43``
     - OM1.43
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Point versus Interval: Item #938
   * - ``om1_44``
     - OM1.44
     - Optional[:ref:`TX <hl7-v2_3-TX>`]
     - optional
     -
     - Challenge information: Item #939
   * - ``om1_45``
     - OM1.45
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Relationship modifier: Item #940
   * - ``om1_46``
     - OM1.46
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Target anatomic site of test: Item #941
   * - ``om1_47``
     - OM1.47
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Modality of imaging measurement: Item #942

.. _hl7-v2_3-OM2:

.. py:class:: hl7types.hl7.v2_3.segments.OM2.OM2
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
     - Sequence Number - Test/ Observation Master File: Item #586
   * - ``om2_2``
     - OM2.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Units of Measure: Item #627
   * - ``om2_3``
     - OM2.3
     - Optional[List[str]]
     - optional
     -
     - Range of Decimal Precision: Item #628
   * - ``om2_4``
     - OM2.4
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Corresponding SI Units of Measure: Item #629
   * - ``om2_5``
     - OM2.5
     - Optional[:ref:`TX <hl7-v2_3-TX>`]
     - optional
     -
     - SI Conversion Factor: Item #630
   * - ``om2_6``
     - OM2.6
     - Optional[str]
     - optional
     -
     - Reference (Normal) Range - Ordinal & Continuous Obs: Item #631
   * - ``om2_7``
     - OM2.7
     - Optional[str]
     - optional
     -
     - Critical Range for Ordinal & Continuous Obs: Item #632
   * - ``om2_8``
     - OM2.8
     - Optional[str]
     - optional
     -
     - Absolute Range for Ordinal & Continuous Obs: Item #633
   * - ``om2_9``
     - OM2.9
     - Optional[List[str]]
     - optional
     -
     - Delta Check Criteria: Item #634
   * - ``om2_10``
     - OM2.10
     - Optional[str]
     - optional
     -
     - Minimum Meaningful Increments: Item #635

.. _hl7-v2_3-OM3:

.. py:class:: hl7types.hl7.v2_3.segments.OM3.OM3
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
     - Sequence Number - Test/ Observation Master File: Item #586
   * - ``om3_2``
     - OM3.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Preferred Coding System: Item #636
   * - ``om3_3``
     - OM3.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Valid Coded "Answers": Item #637
   * - ``om3_4``
     - OM3.4
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Normal Text/Codes for Categorical Observations: Item #638
   * - ``om3_5``
     - OM3.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Abnormal Text/Codes for Categorical Observations: Item #639
   * - ``om3_6``
     - OM3.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Critical Text Codes for Categorical Observations: Item #640
   * - ``om3_7``
     - OM3.7
     - str
     - required
     -
     - Value Type: Item #570 | Table HL70125

.. _hl7-v2_3-OM4:

.. py:class:: hl7types.hl7.v2_3.segments.OM4.OM4
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
     - Sequence Number - Test/ Observation Master File: Item #586
   * - ``om4_2``
     - OM4.2
     - Optional[str]
     - optional
     -
     - Derived Specimen: Item #642 | Table HL70170
   * - ``om4_3``
     - OM4.3
     - Optional[:ref:`TX <hl7-v2_3-TX>`]
     - optional
     -
     - Container Description: Item #643
   * - ``om4_4``
     - OM4.4
     - Optional[str]
     - optional
     -
     - Container Volume: Item #644
   * - ``om4_5``
     - OM4.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Container Units: Item #645
   * - ``om4_6``
     - OM4.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Specimen: Item #646
   * - ``om4_7``
     - OM4.7
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Additive: Item #647
   * - ``om4_8``
     - OM4.8
     - Optional[:ref:`TX <hl7-v2_3-TX>`]
     - optional
     -
     - Preparation: Item #648
   * - ``om4_9``
     - OM4.9
     - Optional[:ref:`TX <hl7-v2_3-TX>`]
     - optional
     -
     - Special Handling Requirements: Item #649
   * - ``om4_10``
     - OM4.10
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     -
     - Normal Collection Volume: Item #650
   * - ``om4_11``
     - OM4.11
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     -
     - Minimum Collection Volume: Item #651
   * - ``om4_12``
     - OM4.12
     - Optional[:ref:`TX <hl7-v2_3-TX>`]
     - optional
     -
     - Specimen Requirements: Item #652
   * - ``om4_13``
     - OM4.13
     - Optional[str]
     - optional
     -
     - Specimen Priorities: Item #653 | Table HL70027
   * - ``om4_14``
     - OM4.14
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     -
     - Specimen Retention Time: Item #654

.. _hl7-v2_3-OM5:

.. py:class:: hl7types.hl7.v2_3.segments.OM5.OM5
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
     - Sequence Number - Test/ Observation Master File: Item #586
   * - ``om5_2``
     - OM5.2
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Test/Observations Included w/an Ordered Test Battery: Item #655
   * - ``om5_3``
     - OM5.3
     - Optional[str]
     - optional
     -
     - Observation ID Suffixes: Item #656

.. _hl7-v2_3-OM6:

.. py:class:: hl7types.hl7.v2_3.segments.OM6.OM6
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
     - Sequence Number - Test/ Observation Master File: Item #586
   * - ``om6_2``
     - OM6.2
     - Optional[:ref:`TX <hl7-v2_3-TX>`]
     - optional
     -
     - Derivation Rule: Item #657

.. _hl7-v2_3-ORC:

.. py:class:: hl7types.hl7.v2_3.segments.ORC.ORC
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
     - Optional[List[:ref:`EI <hl7-v2_3-EI>`]]
     - optional
     -
     - Placer Order Number: Item #216
   * - ``orc_3``
     - ORC.3
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Filler Order Number: Item #217
   * - ``orc_4``
     - ORC.4
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
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
     - :ref:`TQ <hl7-v2_3-TQ>`
     - required
     -
     - Quantity/Timing: Item #221
   * - ``orc_8``
     - ORC.8
     - Optional[str]
     - optional
     -
     - Parent: Item #222
   * - ``orc_9``
     - ORC.9
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date/Time of Transaction: Item #223
   * - ``orc_10``
     - ORC.10
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Entered By: Item #224
   * - ``orc_11``
     - ORC.11
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Verified By: Item #225
   * - ``orc_12``
     - ORC.12
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Ordering Provider: Item #226
   * - ``orc_13``
     - ORC.13
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Order Effective Date/Time: Item #229
   * - ``orc_16``
     - ORC.16
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Order Control Code Reason: Item #230
   * - ``orc_17``
     - ORC.17
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Entering Organization: Item #231
   * - ``orc_18``
     - ORC.18
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Entering Device: Item #232
   * - ``orc_19``
     - ORC.19
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Action By: Item #233

.. _hl7-v2_3-PCR:

.. py:class:: hl7types.hl7.v2_3.segments.PCR.PCR
   :noindex:

   HL7 v2 PCR segment.

PCR
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
   * - ``pcr_1``
     - PCR.1
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Implicated Product: Item #1098
   * - ``pcr_2``
     - PCR.2
     - Optional[str]
     - optional
     -
     - Generic Product: Item #1099 | Table HL70249
   * - ``pcr_3``
     - PCR.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Product Class: Item #1100
   * - ``pcr_4``
     - PCR.4
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     -
     - Total Duration Of Therapy: Item #1101
   * - ``pcr_5``
     - PCR.5
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Product Manufacture Date: Item #1102
   * - ``pcr_6``
     - PCR.6
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Product Expiration Date: Item #1103
   * - ``pcr_7``
     - PCR.7
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Product Implantation Date: Item #1104
   * - ``pcr_8``
     - PCR.8
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Product Explantation Date: Item #1105
   * - ``pcr_9``
     - PCR.9
     - Optional[str]
     - optional
     -
     - Single Use Device: Item #1106 | Table HL70244
   * - ``pcr_10``
     - PCR.10
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Indication For Product Use: Item #1107
   * - ``pcr_11``
     - PCR.11
     - Optional[str]
     - optional
     -
     - Product Problem: Item #1108 | Table HL70245
   * - ``pcr_12``
     - PCR.12
     - Optional[List[str]]
     - optional
     -
     - Product Serial/Lot Number: Item #1109
   * - ``pcr_13``
     - PCR.13
     - Optional[str]
     - optional
     -
     - Product Available For Inspection: Item #1110 | Table HL70246
   * - ``pcr_14``
     - PCR.14
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Product Evaluation Performed: Item #1111
   * - ``pcr_15``
     - PCR.15
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Product Evaluation Status: Item #1112 | Table HL70247
   * - ``pcr_16``
     - PCR.16
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Product Evaluation Results: Item #1113
   * - ``pcr_17``
     - PCR.17
     - Optional[str]
     - optional
     -
     - Evaluated Product Source: Item #1114 | Table HL70248
   * - ``pcr_18``
     - PCR.18
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date Product Returned To Manufacturer: Item #1115
   * - ``pcr_19``
     - PCR.19
     - Optional[str]
     - optional
     -
     - Device Operator Qualifications: Item #1116 | Table HL70242
   * - ``pcr_20``
     - PCR.20
     - Optional[str]
     - optional
     -
     - Relatedness Assessment: Item #1117 | Table HL70250
   * - ``pcr_21``
     - PCR.21
     - Optional[List[str]]
     - optional
     -
     - Action Taken In Response To The Event: Item #1118 | Table HL70251
   * - ``pcr_22``
     - PCR.22
     - Optional[List[str]]
     - optional
     -
     - Event Causality Observations: Item #1119 | Table HL70232
   * - ``pcr_23``
     - PCR.23
     - Optional[List[str]]
     - optional
     -
     - Indirect Exposure Mechanism: Item #1120 | Table HL70253

.. _hl7-v2_3-PD1:

.. py:class:: hl7types.hl7.v2_3.segments.PD1.PD1
   :noindex:

   HL7 v2 PD1 segment.

PD1
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
   * - ``pd1_1``
     - PD1.1
     - Optional[str]
     - optional
     -
     - Living Dependency: Item #755 | Table HL70223
   * - ``pd1_2``
     - PD1.2
     - Optional[str]
     - optional
     -
     - Living Arrangement: Item #742 | Table HL70220
   * - ``pd1_3``
     - PD1.3
     - Optional[List[:ref:`XON <hl7-v2_3-XON>`]]
     - optional
     -
     - Patient Primary Facility: Item #756
   * - ``pd1_4``
     - PD1.4
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Patient Primary Care Provider Name & ID No.: Item #757
   * - ``pd1_5``
     - PD1.5
     - Optional[str]
     - optional
     -
     - Student Indicator: Item #745 | Table HL70231
   * - ``pd1_6``
     - PD1.6
     - Optional[str]
     - optional
     -
     - Handicap: Item #753 | Table HL70310
   * - ``pd1_7``
     - PD1.7
     - Optional[str]
     - optional
     -
     - Living Will: Item #759 | Table HL70315
   * - ``pd1_8``
     - PD1.8
     - Optional[str]
     - optional
     -
     - Organ Donor: Item #760 | Table HL70316
   * - ``pd1_9``
     - PD1.9
     - Optional[str]
     - optional
     -
     - Separate Bill: Item #761 | Table HL70136
   * - ``pd1_10``
     - PD1.10
     - Optional[List[:ref:`CX <hl7-v2_3-CX>`]]
     - optional
     -
     - Duplicate Patient: Item #762
   * - ``pd1_11``
     - PD1.11
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Publicity Indicator: Item #743 | Table HL70215
   * - ``pd1_12``
     - PD1.12
     - Optional[str]
     - optional
     -
     - Protection Indicator: Item #744 | Table HL70136

.. _hl7-v2_3-PDC:

.. py:class:: hl7types.hl7.v2_3.segments.PDC.PDC
   :noindex:

   HL7 v2 PDC segment.

PDC
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
   * - ``pdc_1``
     - PDC.1
     - :ref:`XON <hl7-v2_3-XON>`
     - required
     -
     - Manufacturer/Distributor: Item #1247
   * - ``pdc_2``
     - PDC.2
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Country: Item #1248
   * - ``pdc_3``
     - PDC.3
     - str
     - required
     -
     - Brand Name: Item #1249
   * - ``pdc_4``
     - PDC.4
     - Optional[str]
     - optional
     -
     - Device Family Name: Item #1250
   * - ``pdc_5``
     - PDC.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Generic Name: Item #1251
   * - ``pdc_6``
     - PDC.6
     - Optional[List[str]]
     - optional
     -
     - Model Identifier: Item #1252
   * - ``pdc_7``
     - PDC.7
     - Optional[str]
     - optional
     -
     - Catalogue Identifier: Item #1253
   * - ``pdc_8``
     - PDC.8
     - Optional[List[str]]
     - optional
     -
     - Other Identifier: Item #1254
   * - ``pdc_9``
     - PDC.9
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Product Code: Item #1255
   * - ``pdc_10``
     - PDC.10
     - Optional[str]
     - optional
     -
     - Marketing Basis: Item #1256 | Table HL70330
   * - ``pdc_11``
     - PDC.11
     - Optional[str]
     - optional
     -
     - Marketing Approval Identifier: Item #1257
   * - ``pdc_12``
     - PDC.12
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     -
     - Labeled Shelf Life: Item #1258
   * - ``pdc_13``
     - PDC.13
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     -
     - Expected Shelf Life: Item #1259
   * - ``pdc_14``
     - PDC.14
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date First Marked: Item #1260
   * - ``pdc_15``
     - PDC.15
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date Last Marked: Item #1261

.. _hl7-v2_3-PEO:

.. py:class:: hl7types.hl7.v2_3.segments.PEO.PEO
   :noindex:

   HL7 v2 PEO segment.

PEO
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
   * - ``peo_1``
     - PEO.1
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Event Identifiers Used: Item #1073
   * - ``peo_2``
     - PEO.2
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Event Symptom/Diagnosis Code: Item #1074
   * - ``peo_3``
     - PEO.3
     - :ref:`TS <hl7-v2_3-TS>`
     - required
     -
     - Event Onset Date/Time: Item #1075
   * - ``peo_4``
     - PEO.4
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Event Exacerbation Date/Time: Item #1076
   * - ``peo_5``
     - PEO.5
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Event Improved Date/Time: Item #1077
   * - ``peo_6``
     - PEO.6
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Event Ended Data/Time: Item #1078
   * - ``peo_7``
     - PEO.7
     - Optional[:ref:`XAD <hl7-v2_3-XAD>`]
     - optional
     -
     - Event Location Occurred Address: Item #1079
   * - ``peo_8``
     - PEO.8
     - Optional[List[str]]
     - optional
     -
     - Event Qualification: Item #1080 | Table HL70237
   * - ``peo_9``
     - PEO.9
     - Optional[str]
     - optional
     -
     - Event Serious: Item #1081 | Table HL70238
   * - ``peo_10``
     - PEO.10
     - Optional[str]
     - optional
     -
     - Event Expected: Item #1082 | Table HL70239
   * - ``peo_11``
     - PEO.11
     - Optional[List[str]]
     - optional
     -
     - Event Outcome: Item #1083 | Table HL70240
   * - ``peo_12``
     - PEO.12
     - Optional[str]
     - optional
     -
     - Patient Outcome: Item #1084 | Table HL70241
   * - ``peo_13``
     - PEO.13
     - Optional[List[:ref:`FT <hl7-v2_3-FT>`]]
     - optional
     -
     - Event Description From Others: Item #1085
   * - ``peo_14``
     - PEO.14
     - Optional[List[:ref:`FT <hl7-v2_3-FT>`]]
     - optional
     -
     - Event From Original Reporter: Item #1086
   * - ``peo_15``
     - PEO.15
     - Optional[List[:ref:`FT <hl7-v2_3-FT>`]]
     - optional
     -
     - Event Description From Patient: Item #1087
   * - ``peo_16``
     - PEO.16
     - Optional[List[:ref:`FT <hl7-v2_3-FT>`]]
     - optional
     -
     - Event Description From Practitioner: Item #1088
   * - ``peo_17``
     - PEO.17
     - Optional[List[:ref:`FT <hl7-v2_3-FT>`]]
     - optional
     -
     - Event Description From Autopsy: Item #1089
   * - ``peo_18``
     - PEO.18
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Cause Of Death: Item #1090
   * - ``peo_19``
     - PEO.19
     - Optional[:ref:`XPN <hl7-v2_3-XPN>`]
     - optional
     -
     - Primary Observer Name: Item #1091
   * - ``peo_20``
     - PEO.20
     - Optional[List[:ref:`XAD <hl7-v2_3-XAD>`]]
     - optional
     -
     - Primary Observer Address: Item #1092
   * - ``peo_21``
     - PEO.21
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Primary Observer Telephone: Item #1093
   * - ``peo_22``
     - PEO.22
     - Optional[str]
     - optional
     -
     - Primary Observer’s Qualification: Item #1094 | Table HL70242
   * - ``peo_23``
     - PEO.23
     - Optional[str]
     - optional
     -
     - Confirmation Provided By: Item #1095 | Table HL70242
   * - ``peo_24``
     - PEO.24
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Primary Observer Aware Date/Time: Item #1096
   * - ``peo_25``
     - PEO.25
     - Optional[str]
     - optional
     -
     - Primary Observer’s Identity May Be Divulged: Item #1097 | Table HL70243

.. _hl7-v2_3-PES:

.. py:class:: hl7types.hl7.v2_3.segments.PES.PES
   :noindex:

   HL7 v2 PES segment.

PES
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
   * - ``pes_1``
     - PES.1
     - Optional[:ref:`XON <hl7-v2_3-XON>`]
     - optional
     -
     - Sender Organization Name: Item #1059
   * - ``pes_2``
     - PES.2
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Sender Individual Name: Item #1060
   * - ``pes_3``
     - PES.3
     - Optional[List[:ref:`XAD <hl7-v2_3-XAD>`]]
     - optional
     -
     - Sender Address: Item #1062
   * - ``pes_4``
     - PES.4
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Sender Telephone: Item #1063
   * - ``pes_5``
     - PES.5
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Sender Event Identifier: Item #1064
   * - ``pes_6``
     - PES.6
     - Optional[str]
     - optional
     -
     - Sender Sequence Number: Item #1065
   * - ``pes_7``
     - PES.7
     - Optional[List[:ref:`FT <hl7-v2_3-FT>`]]
     - optional
     -
     - Sender Event Description: Item #1066
   * - ``pes_8``
     - PES.8
     - Optional[:ref:`FT <hl7-v2_3-FT>`]
     - optional
     -
     - Sender Comment: Item #1067
   * - ``pes_9``
     - PES.9
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Sender Aware Date/Time: Item #1068
   * - ``pes_10``
     - PES.10
     - :ref:`TS <hl7-v2_3-TS>`
     - required
     -
     - Event Report Date: Item #1069
   * - ``pes_11``
     - PES.11
     - Optional[List[str]]
     - optional
     -
     - Event Report Timing/Type: Item #1070 | Table HL70234
   * - ``pes_12``
     - PES.12
     - Optional[str]
     - optional
     -
     - Event Report Source: Item #1071 | Table HL70235
   * - ``pes_13``
     - PES.13
     - Optional[List[str]]
     - optional
     -
     - Event Reported To: Item #1072 | Table HL70236

.. _hl7-v2_3-PID:

.. py:class:: hl7types.hl7.v2_3.segments.PID.PID
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
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Patient ID (External ID): Item #105
   * - ``pid_3``
     - PID.3
     - Optional[List[:ref:`CX <hl7-v2_3-CX>`]]
     - optional
     -
     - Patient ID (Internal ID): Item #106
   * - ``pid_4``
     - PID.4
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Alternate Patient ID: Item #107
   * - ``pid_5``
     - PID.5
     - :ref:`XPN <hl7-v2_3-XPN>`
     - required
     -
     - Patient Name: Item #108
   * - ``pid_6``
     - PID.6
     - Optional[:ref:`XPN <hl7-v2_3-XPN>`]
     - optional
     -
     - Mother's Maiden Name: Item #109
   * - ``pid_7``
     - PID.7
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
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
     - Optional[List[:ref:`XPN <hl7-v2_3-XPN>`]]
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
     - Optional[List[:ref:`XAD <hl7-v2_3-XAD>`]]
     - optional
     -
     - Patient Address: Item #114
   * - ``pid_12``
     - PID.12
     - Optional[str]
     - optional
     -
     - County Code: Item #115
   * - ``pid_13``
     - PID.13
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Phone Number - Home: Item #116
   * - ``pid_14``
     - PID.14
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Phone Number - Business: Item #117
   * - ``pid_15``
     - PID.15
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Primary Language: Item #118 | Table HL70296
   * - ``pid_16``
     - PID.16
     - Optional[List[str]]
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
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Patient Account Number: Item #121
   * - ``pid_19``
     - PID.19
     - Optional[str]
     - optional
     -
     - SSN Number - Patient: Item #122
   * - ``pid_20``
     - PID.20
     - Optional[:ref:`DLN <hl7-v2_3-DLN>`]
     - optional
     -
     - Driver's License Number: Item #123
   * - ``pid_21``
     - PID.21
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
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
     - Multiple Birth Indicator: Item #127 | Table HL70136
   * - ``pid_25``
     - PID.25
     - Optional[str]
     - optional
     -
     - Birth Order: Item #128
   * - ``pid_26``
     - PID.26
     - Optional[str]
     - optional
     -
     - Citizenship: Item #129 | Table HL70171
   * - ``pid_27``
     - PID.27
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Veterans Military Status: Item #130 | Table HL70172
   * - ``pid_28``
     - PID.28
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Nationality Code: Item #739 | Table HL70212
   * - ``pid_29``
     - PID.29
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Patient Death Date and Time: Item #740
   * - ``pid_30``
     - PID.30
     - Optional[str]
     - optional
     -
     - Patient Death Indicator: Item #741 | Table HL70136

.. _hl7-v2_3-PR1:

.. py:class:: hl7types.hl7.v2_3.segments.PR1.PR1
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
     - Set ID - Procedure: Item #391
   * - ``pr1_2``
     - PR1.2
     - str
     - required
     -
     - Procedure Coding Method: Item #392 | Table HL70089
   * - ``pr1_3``
     - PR1.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Procedure Code: Item #393 | Table HL70088
   * - ``pr1_4``
     - PR1.4
     - Optional[str]
     - optional
     -
     - Procedure Description: Item #394
   * - ``pr1_5``
     - PR1.5
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Procedure Date/Time: Item #395
   * - ``pr1_6``
     - PR1.6
     - str
     - required
     -
     - Procedure Type: Item #396 | Table HL70230
   * - ``pr1_7``
     - PR1.7
     - Optional[str]
     - optional
     -
     - Procedure Minutes: Item #397
   * - ``pr1_8``
     - PR1.8
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Anesthesiologist: Item #398 | Table HL70010
   * - ``pr1_9``
     - PR1.9
     - Optional[str]
     - optional
     -
     - Anesthesia Code: Item #399 | Table HL70019
   * - ``pr1_10``
     - PR1.10
     - Optional[str]
     - optional
     -
     - Anesthesia Minutes: Item #400
   * - ``pr1_11``
     - PR1.11
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Surgeon: Item #401 | Table HL70010
   * - ``pr1_12``
     - PR1.12
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Procedure Practitioner: Item #402 | Table HL70010
   * - ``pr1_13``
     - PR1.13
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Consent Code: Item #403 | Table HL70059
   * - ``pr1_14``
     - PR1.14
     - Optional[str]
     - optional
     -
     - Procedure Priority: Item #404
   * - ``pr1_15``
     - PR1.15
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Associated Diagnosis Code: Item #772

.. _hl7-v2_3-PRA:

.. py:class:: hl7types.hl7.v2_3.segments.PRA.PRA
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
     - PRA - Primary Key Value: Item #685
   * - ``pra_2``
     - PRA.2
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Practioner Group: Item #686
   * - ``pra_3``
     - PRA.3
     - Optional[List[str]]
     - optional
     -
     - Practioner Category: Item #687
   * - ``pra_4``
     - PRA.4
     - Optional[str]
     - optional
     -
     - Provider Billing: Item #688 | Table HL70186
   * - ``pra_5``
     - PRA.5
     - Optional[List[str]]
     - optional
     -
     - Specialty: Item #689 | Table HL70187
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

.. _hl7-v2_3-PRB:

.. py:class:: hl7types.hl7.v2_3.segments.PRB.PRB
   :noindex:

   HL7 v2 PRB segment.

PRB
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
   * - ``prb_1``
     - PRB.1
     - str
     - required
     -
     - Action Code: Item #816 | Table HL70287
   * - ``prb_2``
     - PRB.2
     - :ref:`TS <hl7-v2_3-TS>`
     - required
     -
     - Action Date/Time: Item #817
   * - ``prb_3``
     - PRB.3
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Problem ID: Item #838
   * - ``prb_4``
     - PRB.4
     - :ref:`EI <hl7-v2_3-EI>`
     - required
     -
     - Problem Instance ID: Item #839
   * - ``prb_5``
     - PRB.5
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Episode of Care ID: Item #820
   * - ``prb_6``
     - PRB.6
     - Optional[str]
     - optional
     -
     - Problem List Priority: Item #841
   * - ``prb_7``
     - PRB.7
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Problem Established Date/Time: Item #842
   * - ``prb_8``
     - PRB.8
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Anticipated Problem Resolution Date/Time: Item #843
   * - ``prb_9``
     - PRB.9
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Actual Problem Resolution Date/Time: Item #844
   * - ``prb_10``
     - PRB.10
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Problem Classification: Item #845
   * - ``prb_11``
     - PRB.11
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Problem Management Discipline: Item #846
   * - ``prb_12``
     - PRB.12
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Problem Persistence: Item #847
   * - ``prb_13``
     - PRB.13
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Problem Confirmation Status: Item #848
   * - ``prb_14``
     - PRB.14
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Problem Life Cycle Status: Item #849
   * - ``prb_15``
     - PRB.15
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Problem Life Cycle Status Date/Time: Item #850
   * - ``prb_16``
     - PRB.16
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Problem Date of Onset: Item #851
   * - ``prb_17``
     - PRB.17
     - Optional[str]
     - optional
     -
     - Problem Onset Text: Item #852
   * - ``prb_18``
     - PRB.18
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Problem Ranking: Item #853
   * - ``prb_19``
     - PRB.19
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Certainty of Problem: Item #854
   * - ``prb_20``
     - PRB.20
     - Optional[str]
     - optional
     -
     - Probability of Problem (0-1): Item #855
   * - ``prb_21``
     - PRB.21
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Individual Awareness of Problem: Item #856
   * - ``prb_22``
     - PRB.22
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Problem Prognosis: Item #857
   * - ``prb_23``
     - PRB.23
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Individual Awareness of Prognosis: Item #858
   * - ``prb_24``
     - PRB.24
     - Optional[str]
     - optional
     -
     - Family/Significant Other Awareness of Problem/Prognosis: Item #859
   * - ``prb_25``
     - PRB.25
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Security/Sensitivity: Item #823

.. _hl7-v2_3-PRC:

.. py:class:: hl7types.hl7.v2_3.segments.PRC.PRC
   :noindex:

   HL7 v2 PRC segment.

PRC
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
   * - ``prc_1``
     - PRC.1
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Primary Key Value: Item #982 | Table HL70132
   * - ``prc_2``
     - PRC.2
     - Optional[List[:ref:`EI <hl7-v2_3-EI>`]]
     - optional
     -
     - Facility ID: Item #1262
   * - ``prc_3``
     - PRC.3
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Department: Item #996
   * - ``prc_4``
     - PRC.4
     - Optional[List[str]]
     - optional
     -
     - Valid Patient Classes: Item #967 | Table HL70004
   * - ``prc_5``
     - PRC.5
     - Optional[List[:ref:`CP <hl7-v2_3-CP>`]]
     - optional
     -
     - Price: Item #998
   * - ``prc_6``
     - PRC.6
     - Optional[List[str]]
     - optional
     -
     - Formula: Item #999
   * - ``prc_7``
     - PRC.7
     - Optional[str]
     - optional
     -
     - Minimum Quantity: Item #1000
   * - ``prc_8``
     - PRC.8
     - Optional[str]
     - optional
     -
     - Maximum Quantity: Item #1001
   * - ``prc_9``
     - PRC.9
     - Optional[:ref:`MO <hl7-v2_3-MO>`]
     - optional
     -
     - Minimum Price: Item #1002
   * - ``prc_10``
     - PRC.10
     - Optional[:ref:`MO <hl7-v2_3-MO>`]
     - optional
     -
     - Maximum Price: Item #1003
   * - ``prc_11``
     - PRC.11
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Effective Start Date: Item #1004
   * - ``prc_12``
     - PRC.12
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Effective End Date: Item #1005
   * - ``prc_13``
     - PRC.13
     - Optional[str]
     - optional
     -
     - Price Override Flag: Item #1006 | Table HL70268
   * - ``prc_14``
     - PRC.14
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Billing Category: Item #1007 | Table HL70293
   * - ``prc_15``
     - PRC.15
     - Optional[str]
     - optional
     -
     - Chargeable Flag: Item #1008 | Table HL70136
   * - ``prc_16``
     - PRC.16
     - Optional[str]
     - optional
     -
     - Active/Inactive Flag: Item #675 | Table HL70183
   * - ``prc_17``
     - PRC.17
     - Optional[:ref:`MO <hl7-v2_3-MO>`]
     - optional
     -
     - Cost: Item #989
   * - ``prc_18``
     - PRC.18
     - Optional[str]
     - optional
     -
     - Charge On Indicator: Item #1009 | Table HL70269

.. _hl7-v2_3-PRD:

.. py:class:: hl7types.hl7.v2_3.segments.PRD.PRD
   :noindex:

   HL7 v2 PRD segment.

PRD
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
   * - ``prd_1``
     - PRD.1
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Role: Item #1155 | Table HL70286
   * - ``prd_2``
     - PRD.2
     - Optional[List[:ref:`XPN <hl7-v2_3-XPN>`]]
     - optional
     -
     - Provider Name: Item #1156
   * - ``prd_3``
     - PRD.3
     - Optional[:ref:`XAD <hl7-v2_3-XAD>`]
     - optional
     -
     - Provider Address: Item #1157
   * - ``prd_4``
     - PRD.4
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Provider Location: Item #1158
   * - ``prd_5``
     - PRD.5
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Provider Communication Information: Item #1159
   * - ``prd_6``
     - PRD.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Preferred Method of Contact: Item #684 | Table HL70185
   * - ``prd_7``
     - PRD.7
     - Optional[List[str]]
     - optional
     -
     - Provider Identifiers: Item #1162
   * - ``prd_8``
     - PRD.8
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Effective Start Date of Role: Item #1163
   * - ``prd_9``
     - PRD.9
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Effective End Date of Role: Item #1164

.. _hl7-v2_3-PSH:

.. py:class:: hl7types.hl7.v2_3.segments.PSH.PSH
   :noindex:

   HL7 v2 PSH segment.

PSH
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
   * - ``psh_1``
     - PSH.1
     - str
     - required
     -
     - Report Type: Item #1233
   * - ``psh_2``
     - PSH.2
     - Optional[str]
     - optional
     -
     - Report Form Identifier: Item #1234
   * - ``psh_3``
     - PSH.3
     - :ref:`TS <hl7-v2_3-TS>`
     - required
     -
     - Report Date: Item #1235
   * - ``psh_4``
     - PSH.4
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Report Interval Start Date: Item #1236
   * - ``psh_5``
     - PSH.5
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Report Interval End Date: Item #1237
   * - ``psh_6``
     - PSH.6
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     -
     - Quantity Manufactured: Item #1238
   * - ``psh_7``
     - PSH.7
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     -
     - Quantity Distributed: Item #1239
   * - ``psh_8``
     - PSH.8
     - Optional[str]
     - optional
     -
     - Quantity Distributed Method: Item #1240 | Table HL70329
   * - ``psh_9``
     - PSH.9
     - Optional[:ref:`FT <hl7-v2_3-FT>`]
     - optional
     -
     - Quantity Distributed Comment: Item #1241
   * - ``psh_10``
     - PSH.10
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     -
     - Quantity in Use: Item #1242
   * - ``psh_11``
     - PSH.11
     - Optional[str]
     - optional
     -
     - Quantity in Use Method: Item #1243 | Table HL70329
   * - ``psh_12``
     - PSH.12
     - Optional[:ref:`FT <hl7-v2_3-FT>`]
     - optional
     -
     - Quantity in Use Comment: Item #1244
   * - ``psh_13``
     - PSH.13
     - Optional[List[str]]
     - optional
     -
     - Number of Product Experience Reports Filed by Facility: Item #1245
   * - ``psh_14``
     - PSH.14
     - Optional[List[str]]
     - optional
     -
     - Number of Product Experience Reports Filed by Distributor: Item #1246

.. _hl7-v2_3-PTH:

.. py:class:: hl7types.hl7.v2_3.segments.PTH.PTH
   :noindex:

   HL7 v2 PTH segment.

PTH
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
   * - ``pth_1``
     - PTH.1
     - str
     - required
     -
     - Action Code: Item #816 | Table HL70287
   * - ``pth_2``
     - PTH.2
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Pathway ID: Item #1207
   * - ``pth_3``
     - PTH.3
     - :ref:`EI <hl7-v2_3-EI>`
     - required
     -
     - Pathway Instance ID: Item #1208
   * - ``pth_4``
     - PTH.4
     - :ref:`TS <hl7-v2_3-TS>`
     - required
     -
     - Pathway Established Date/Time: Item #1209
   * - ``pth_5``
     - PTH.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Pathway Lifecycle Status: Item #1210
   * - ``pth_6``
     - PTH.6
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Change Pathway Lifecycle Status Date/Time: Item #1211

.. _hl7-v2_3-PV1:

.. py:class:: hl7types.hl7.v2_3.segments.PV1.PV1
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
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Assigned Patient Location: Item #133
   * - ``pv1_4``
     - PV1.4
     - Optional[str]
     - optional
     -
     - Admission Type: Item #134 | Table HL70007
   * - ``pv1_5``
     - PV1.5
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Preadmit Number: Item #135
   * - ``pv1_6``
     - PV1.6
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Prior Patient Location: Item #136
   * - ``pv1_7``
     - PV1.7
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Attending Doctor: Item #137 | Table HL70010
   * - ``pv1_8``
     - PV1.8
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Referring Doctor: Item #138 | Table HL70010
   * - ``pv1_9``
     - PV1.9
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
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
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Temporary Location: Item #141
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
     - Readmission Indicator: Item #143 | Table HL70092
   * - ``pv1_14``
     - PV1.14
     - Optional[str]
     - optional
     -
     - Admit Source: Item #144 | Table HL70023
   * - ``pv1_15``
     - PV1.15
     - Optional[str]
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
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Admitting Doctor: Item #147 | Table HL70010
   * - ``pv1_18``
     - PV1.18
     - Optional[str]
     - optional
     -
     - Patient Type: Item #148 | Table HL70018
   * - ``pv1_19``
     - PV1.19
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Visit Number: Item #149
   * - ``pv1_20``
     - PV1.20
     - Optional[List[:ref:`FC <hl7-v2_3-FC>`]]
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
     - Transfer to Bad Debt Code: Item #159 | Table HL70110
   * - ``pv1_30``
     - PV1.30
     - Optional[str]
     - optional
     -
     - Transfer to Bad Debt Date: Item #160
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
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Pending Location: Item #172
   * - ``pv1_43``
     - PV1.43
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Prior Temporary Location: Item #173
   * - ``pv1_44``
     - PV1.44
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Admit Date/Time: Item #174
   * - ``pv1_45``
     - PV1.45
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Discharge Date/Time: Item #175
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
     - Optional[:ref:`CX <hl7-v2_3-CX>`]
     - optional
     -
     - Alternate Visit ID: Item #180 | Table HL70192
   * - ``pv1_51``
     - PV1.51
     - Optional[str]
     - optional
     -
     - Visit Indicator: Item #1226 | Table HL70326
   * - ``pv1_52``
     - PV1.52
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Other Healthcare Provider: Item #1274 | Table HL70010

.. _hl7-v2_3-PV2:

.. py:class:: hl7types.hl7.v2_3.segments.PV2.PV2
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
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Prior Pending Location: Item #181
   * - ``pv2_2``
     - PV2.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Accommodation Code: Item #182 | Table HL70129
   * - ``pv2_3``
     - PV2.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Admit Reason: Item #183
   * - ``pv2_4``
     - PV2.4
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Expected Admit Date: Item #188
   * - ``pv2_9``
     - PV2.9
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Expected Discharge Date: Item #189
   * - ``pv2_10``
     - PV2.10
     - Optional[str]
     - optional
     -
     - Estimated Length of Inpatient Stay: Item #711
   * - ``pv2_11``
     - PV2.11
     - Optional[str]
     - optional
     -
     - Actual Length of Inpatient Stay: Item #712
   * - ``pv2_12``
     - PV2.12
     - Optional[str]
     - optional
     -
     - Visit Description: Item #713
   * - ``pv2_13``
     - PV2.13
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Referral Source Code: Item #714
   * - ``pv2_14``
     - PV2.14
     - Optional[str]
     - optional
     -
     - Previous Service Date: Item #715
   * - ``pv2_15``
     - PV2.15
     - Optional[str]
     - optional
     -
     - Employment Illness Related Indicator: Item #716 | Table HL70136
   * - ``pv2_16``
     - PV2.16
     - Optional[str]
     - optional
     -
     - Purge Status Code: Item #717 | Table HL70213
   * - ``pv2_17``
     - PV2.17
     - Optional[str]
     - optional
     -
     - Purge Status Date: Item #718
   * - ``pv2_18``
     - PV2.18
     - Optional[str]
     - optional
     -
     - Special Program Code: Item #719 | Table HL70214
   * - ``pv2_19``
     - PV2.19
     - Optional[str]
     - optional
     -
     - Retention Indicator: Item #720 | Table HL70136
   * - ``pv2_20``
     - PV2.20
     - Optional[str]
     - optional
     -
     - Expected Number of Insurance Plans: Item #721
   * - ``pv2_21``
     - PV2.21
     - Optional[str]
     - optional
     -
     - Visit Publicity Code: Item #722 | Table HL70215
   * - ``pv2_22``
     - PV2.22
     - Optional[str]
     - optional
     -
     - Visit Protection Indicator: Item #723 | Table HL70136
   * - ``pv2_23``
     - PV2.23
     - Optional[List[:ref:`XON <hl7-v2_3-XON>`]]
     - optional
     -
     - Clinic Organization Name: Item #724
   * - ``pv2_24``
     - PV2.24
     - Optional[str]
     - optional
     -
     - Patient Status Code: Item #725 | Table HL70216
   * - ``pv2_25``
     - PV2.25
     - Optional[str]
     - optional
     -
     - Visit Priority Code: Item #726 | Table HL70217
   * - ``pv2_26``
     - PV2.26
     - Optional[str]
     - optional
     -
     - Previous Treatment Date: Item #727
   * - ``pv2_27``
     - PV2.27
     - Optional[str]
     - optional
     -
     - Expected Discharge Disposition: Item #728 | Table HL70112
   * - ``pv2_28``
     - PV2.28
     - Optional[str]
     - optional
     -
     - Signature on File Date: Item #729
   * - ``pv2_29``
     - PV2.29
     - Optional[str]
     - optional
     -
     - First Similar Illness Date: Item #730
   * - ``pv2_30``
     - PV2.30
     - Optional[str]
     - optional
     -
     - Patient Charge Adjustment Code: Item #731 | Table HL70218
   * - ``pv2_31``
     - PV2.31
     - Optional[str]
     - optional
     -
     - Recurring Service Code: Item #732 | Table HL70219
   * - ``pv2_32``
     - PV2.32
     - Optional[str]
     - optional
     -
     - Billing Media Code: Item #733 | Table HL70136
   * - ``pv2_33``
     - PV2.33
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Expected Surgery Date & Time: Item #734
   * - ``pv2_34``
     - PV2.34
     - Optional[str]
     - optional
     -
     - Military Partnership Code: Item #735 | Table HL70136
   * - ``pv2_35``
     - PV2.35
     - Optional[str]
     - optional
     -
     - Military Non-Availabiltiy Code: Item #736 | Table HL70136
   * - ``pv2_36``
     - PV2.36
     - Optional[str]
     - optional
     -
     - Newborn Baby Indicator: Item #737 | Table HL70136
   * - ``pv2_37``
     - PV2.37
     - Optional[str]
     - optional
     -
     - Baby Detained Indicator: Item #738 | Table HL70136

.. _hl7-v2_3-QAK:

.. py:class:: hl7types.hl7.v2_3.segments.QAK.QAK
   :noindex:

   HL7 v2 QAK segment.

QAK
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
   * - ``qak_1``
     - QAK.1
     - Optional[str]
     - optional
     -
     - Query tag: Item #696
   * - ``qak_2``
     - QAK.2
     - Optional[str]
     - optional
     -
     - Query response status: Item #708 | Table HL70208

.. _hl7-v2_3-QRD:

.. py:class:: hl7types.hl7.v2_3.segments.QRD.QRD
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Query Date/Time: Item #25
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Deferred Response Date/Time: Item #30
   * - ``qrd_7``
     - QRD.7
     - :ref:`CQ <hl7-v2_3-CQ>`
     - required
     -
     - Quantity Limited Request: Item #31 | Table HL70126
   * - ``qrd_8``
     - QRD.8
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Who Subject Filter: Item #32
   * - ``qrd_9``
     - QRD.9
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - What Subject Filter: Item #33 | Table HL70048
   * - ``qrd_10``
     - QRD.10
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - What Department Data Code: Item #34
   * - ``qrd_11``
     - QRD.11
     - Optional[List[str]]
     - optional
     -
     - What Data Code Value Qualifier: Item #35
   * - ``qrd_12``
     - QRD.12
     - Optional[str]
     - optional
     -
     - Query Results Level: Item #36 | Table HL70108

.. _hl7-v2_3-QRF:

.. py:class:: hl7types.hl7.v2_3.segments.QRF.QRF
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - When Data Start Date/Time: Item #38
   * - ``qrf_3``
     - QRF.3
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - When Data End Date/Time: Item #39
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
     - Which Date/Time Qualifier: Item #42 | Table HL70156
   * - ``qrf_7``
     - QRF.7
     - Optional[List[str]]
     - optional
     -
     - Which Date/Time Status Qualifier: Item #43 | Table HL70157
   * - ``qrf_8``
     - QRF.8
     - Optional[List[str]]
     - optional
     -
     - Date/Time Selection Qualifier: Item #44 | Table HL70158
   * - ``qrf_9``
     - QRF.9
     - Optional[:ref:`TQ <hl7-v2_3-TQ>`]
     - optional
     -
     - When Quantity/Timing Qualifier: Item #694

.. _hl7-v2_3-RDF:

.. py:class:: hl7types.hl7.v2_3.segments.RDF.RDF
   :noindex:

   HL7 v2 RDF segment.

RDF
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
   * - ``rdf_1``
     - RDF.1
     - str
     - required
     -
     - Number of Columns per Row: Item #701
   * - ``rdf_2``
     - RDF.2
     - Optional[List[:ref:`RCD <hl7-v2_3-RCD>`]]
     - optional
     -
     - Column Description: Item #702

.. _hl7-v2_3-RDT:

.. py:class:: hl7types.hl7.v2_3.segments.RDT.RDT
   :noindex:

   HL7 v2 RDT segment.

RDT
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
   * - ``rdt_1``
     - RDT.1
     - str
     - required
     -
     - Column value: Item #703

.. _hl7-v2_3-RF1:

.. py:class:: hl7types.hl7.v2_3.segments.RF1.RF1
   :noindex:

   HL7 v2 RF1 segment.

RF1
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
   * - ``rf1_1``
     - RF1.1
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Referral Status: Item #1137 | Table HL70283
   * - ``rf1_2``
     - RF1.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Referral Priority: Item #1138 | Table HL70280
   * - ``rf1_3``
     - RF1.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Referral Type: Item #1139 | Table HL70281
   * - ``rf1_4``
     - RF1.4
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Referral Disposition: Item #1140 | Table HL70282
   * - ``rf1_5``
     - RF1.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Referral Category: Item #1141 | Table HL70284
   * - ``rf1_6``
     - RF1.6
     - :ref:`EI <hl7-v2_3-EI>`
     - required
     -
     - Originating Referral Identifier: Item #1142
   * - ``rf1_7``
     - RF1.7
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Effective Date: Item #1143
   * - ``rf1_8``
     - RF1.8
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Expiration Date: Item #1144
   * - ``rf1_9``
     - RF1.9
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Process Date: Item #1145
   * - ``rf1_10``
     - RF1.10
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Referral Reason: Item #1228 | Table HL70336
   * - ``rf1_11``
     - RF1.11
     - Optional[List[:ref:`EI <hl7-v2_3-EI>`]]
     - optional
     -
     - External Referral Identifier: Item #1300

.. _hl7-v2_3-RGS:

.. py:class:: hl7types.hl7.v2_3.segments.RGS.RGS
   :noindex:

   HL7 v2 RGS segment.

RGS
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
   * - ``rgs_1``
     - RGS.1
     - str
     - required
     -
     - Set ID - RGS: Item #1203
   * - ``rgs_2``
     - RGS.2
     - Optional[str]
     - optional
     -
     - Segment Action Code: Item #763 | Table HL70206
   * - ``rgs_3``
     - RGS.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Resource Group ID: Item #1204

.. _hl7-v2_3-ROL:

.. py:class:: hl7types.hl7.v2_3.segments.ROL.ROL
   :noindex:

   HL7 v2 ROL segment.

ROL
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
   * - ``rol_1``
     - ROL.1
     - :ref:`EI <hl7-v2_3-EI>`
     - required
     -
     - Role Instance ID: Item #1206
   * - ``rol_2``
     - ROL.2
     - str
     - required
     -
     - Action Code: Item #816 | Table HL70287
   * - ``rol_3``
     - ROL.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Role: Item #1197
   * - ``rol_4``
     - ROL.4
     - :ref:`XCN <hl7-v2_3-XCN>`
     - required
     -
     - Role Person: Item #1198
   * - ``rol_5``
     - ROL.5
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Role Begin Date/Time: Item #1199
   * - ``rol_6``
     - ROL.6
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Role End Date/Time: Item #1200
   * - ``rol_7``
     - ROL.7
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Role Duration: Item #1201
   * - ``rol_8``
     - ROL.8
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Role Action (Assumption) Reason: Item #1205

.. _hl7-v2_3-RQ1:

.. py:class:: hl7types.hl7.v2_3.segments.RQ1.RQ1
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
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Manufactured ID: Item #286
   * - ``rq1_3``
     - RQ1.3
     - Optional[str]
     - optional
     -
     - Manufacturer's Catalog: Item #287
   * - ``rq1_4``
     - RQ1.4
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
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

.. _hl7-v2_3-RQD:

.. py:class:: hl7types.hl7.v2_3.segments.RQD.RQD
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
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Item Code - Internal: Item #276
   * - ``rqd_3``
     - RQD.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Item Code - External: Item #277
   * - ``rqd_4``
     - RQD.4
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
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
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Requisition Unit of Measure: Item #280
   * - ``rqd_7``
     - RQD.7
     - Optional[str]
     - optional
     -
     - Department Cost Center: Item #281
   * - ``rqd_8``
     - RQD.8
     - Optional[str]
     - optional
     -
     - Item Natural Account Code: Item #282
   * - ``rqd_9``
     - RQD.9
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Deliver To ID: Item #283
   * - ``rqd_10``
     - RQD.10
     - Optional[str]
     - optional
     -
     - Date Needed: Item #284

.. _hl7-v2_3-RXA:

.. py:class:: hl7types.hl7.v2_3.segments.RXA.RXA
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
     - :ref:`TS <hl7-v2_3-TS>`
     - required
     -
     - Date/Time Start of Administration: Item #345
   * - ``rxa_4``
     - RXA.4
     - :ref:`TS <hl7-v2_3-TS>`
     - required
     -
     - Date/Time End of Administration: Item #346
   * - ``rxa_5``
     - RXA.5
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Administered Code: Item #347 | Table HL70292
   * - ``rxa_6``
     - RXA.6
     - str
     - required
     -
     - Administered Amount: Item #348
   * - ``rxa_7``
     - RXA.7
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Administered Units: Item #349
   * - ``rxa_8``
     - RXA.8
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Administered Dosage Form: Item #350
   * - ``rxa_9``
     - RXA.9
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Administration Notes: Item #351
   * - ``rxa_10``
     - RXA.10
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
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
   * - ``rxa_13``
     - RXA.13
     - Optional[str]
     - optional
     -
     - Administered Strength: Item #1134
   * - ``rxa_14``
     - RXA.14
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Administered Strength Units: Item #1135
   * - ``rxa_15``
     - RXA.15
     - Optional[List[str]]
     - optional
     -
     - Substance Lot Number: Item #1129
   * - ``rxa_16``
     - RXA.16
     - Optional[List[:ref:`TS <hl7-v2_3-TS>`]]
     - optional
     -
     - Substance Expiration Date: Item #1130
   * - ``rxa_17``
     - RXA.17
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Substance Manufacturer Name: Item #1131 | Table HL70227
   * - ``rxa_18``
     - RXA.18
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Substance Refusal Reason: Item #1136
   * - ``rxa_19``
     - RXA.19
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Indication: Item #1123
   * - ``rxa_20``
     - RXA.20
     - Optional[str]
     - optional
     -
     - Completion Status: Item #1223 | Table HL70322
   * - ``rxa_21``
     - RXA.21
     - Optional[str]
     - optional
     -
     - Action Code-RXA: Item #1224 | Table HL70323
   * - ``rxa_22``
     - RXA.22
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - System Entry Date/Time: Item #1225

.. _hl7-v2_3-RXC:

.. py:class:: hl7types.hl7.v2_3.segments.RXC.RXC
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Component Units: Item #316
   * - ``rxc_5``
     - RXC.5
     - Optional[str]
     - optional
     -
     - Component Strength: Item #1124
   * - ``rxc_6``
     - RXC.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Component Strength Units: Item #1125

.. _hl7-v2_3-RXD:

.. py:class:: hl7types.hl7.v2_3.segments.RXD.RXD
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
     - str
     - required
     -
     - Dispense Sub-ID Counter: Item #334
   * - ``rxd_2``
     - RXD.2
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Dispense/Give Code: Item #335 | Table HL70292
   * - ``rxd_3``
     - RXD.3
     - :ref:`TS <hl7-v2_3-TS>`
     - required
     -
     - Date/Time Dispensed: Item #336
   * - ``rxd_4``
     - RXD.4
     - str
     - required
     -
     - Actual Dispense Amount: Item #337
   * - ``rxd_5``
     - RXD.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Actual Dispense Units: Item #338
   * - ``rxd_6``
     - RXD.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
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
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Dispense Notes: Item #340
   * - ``rxd_10``
     - RXD.10
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
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
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     -
     - Total Daily Dose: Item #329
   * - ``rxd_13``
     - RXD.13
     - Optional[str]
     - optional
     -
     - Dispense-To Location: Item #1303
   * - ``rxd_14``
     - RXD.14
     - Optional[str]
     - optional
     -
     - Needs Human Review: Item #307 | Table HL70136
   * - ``rxd_15``
     - RXD.15
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Pharmacy/Treatment Supplier's Special Dispensing Instructions: Item #330
   * - ``rxd_16``
     - RXD.16
     - Optional[str]
     - optional
     -
     - Actual Strength: Item #1132
   * - ``rxd_17``
     - RXD.17
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Actual Strength Unit: Item #1133
   * - ``rxd_18``
     - RXD.18
     - Optional[List[str]]
     - optional
     -
     - Substance Lot Number: Item #1129
   * - ``rxd_19``
     - RXD.19
     - Optional[List[:ref:`TS <hl7-v2_3-TS>`]]
     - optional
     -
     - Substance Expiration Date: Item #1130
   * - ``rxd_20``
     - RXD.20
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Substance Manufacturer Name: Item #1131 | Table HL70227
   * - ``rxd_21``
     - RXD.21
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Indication: Item #1123
   * - ``rxd_22``
     - RXD.22
     - Optional[str]
     - optional
     -
     - Dispense Package Size: Item #1220
   * - ``rxd_23``
     - RXD.23
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Dispense Package Size Unit: Item #1221
   * - ``rxd_24``
     - RXD.24
     - Optional[str]
     - optional
     -
     - Dispense Package Method: Item #1222 | Table HL70321

.. _hl7-v2_3-RXE:

.. py:class:: hl7types.hl7.v2_3.segments.RXE.RXE
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
     - :ref:`TQ <hl7-v2_3-TQ>`
     - required
     -
     - Quantity/Timing: Item #221
   * - ``rxe_2``
     - RXE.2
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Give Units: Item #320
   * - ``rxe_6``
     - RXE.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Give Dosage Form: Item #321
   * - ``rxe_7``
     - RXE.7
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Provider's Administration Instructions: Item #298
   * - ``rxe_8``
     - RXE.8
     - Optional[str]
     - optional
     -
     - Deliver To Location: Item #299
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
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
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
     - Optional[:ref:`CN <hl7-v2_3-CN>`]
     - optional
     -
     - Ordering Provider's DEA Number: Item #305
   * - ``rxe_14``
     - RXE.14
     - Optional[:ref:`CN <hl7-v2_3-CN>`]
     - optional
     -
     - Pharmacist/Treatment Supplier's Verifier ID: Item #306
   * - ``rxe_15``
     - RXE.15
     - Optional[str]
     - optional
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
     - Number of Refills/Doses Dispensed: Item #327
   * - ``rxe_18``
     - RXE.18
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date / time of most recent refill or dose dispensed: Item #328
   * - ``rxe_19``
     - RXE.19
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     -
     - Total Daily Dose: Item #329
   * - ``rxe_20``
     - RXE.20
     - Optional[str]
     - optional
     -
     - Needs Human Review: Item #307 | Table HL70136
   * - ``rxe_21``
     - RXE.21
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Pharmacy/Treatment Supplier's Special Dispensing Instructions: Item #330
   * - ``rxe_22``
     - RXE.22
     - Optional[str]
     - optional
     -
     - Give Per (Time Unit): Item #331
   * - ``rxe_23``
     - RXE.23
     - Optional[str]
     - optional
     -
     - Give Rate Amount: Item #332
   * - ``rxe_24``
     - RXE.24
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Give Rate Units: Item #333
   * - ``rxe_25``
     - RXE.25
     - Optional[str]
     - optional
     -
     - Give Strength: Item #1126
   * - ``rxe_26``
     - RXE.26
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Give Strength Units: Item #1127
   * - ``rxe_27``
     - RXE.27
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Give Indication: Item #1128
   * - ``rxe_28``
     - RXE.28
     - Optional[str]
     - optional
     -
     - Dispense Package Size: Item #1220
   * - ``rxe_29``
     - RXE.29
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Dispense Package Size Unit: Item #1221
   * - ``rxe_30``
     - RXE.30
     - Optional[str]
     - optional
     -
     - Dispense Package Method: Item #1222 | Table HL70321

.. _hl7-v2_3-RXG:

.. py:class:: hl7types.hl7.v2_3.segments.RXG.RXG
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
     - Optional[str]
     - optional
     -
     - Give Sub-ID Counter: Item #342
   * - ``rxg_2``
     - RXG.2
     - str
     - required
     -
     - Dispense Sub-ID Counter: Item #334
   * - ``rxg_3``
     - RXG.3
     - :ref:`TQ <hl7-v2_3-TQ>`
     - required
     -
     - Quantity/Timing: Item #221
   * - ``rxg_4``
     - RXG.4
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Give Units: Item #320
   * - ``rxg_8``
     - RXG.8
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Give Dosage Form: Item #321
   * - ``rxg_9``
     - RXG.9
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
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
     - Dispense-To Location: Item #1303
   * - ``rxg_12``
     - RXG.12
     - Optional[str]
     - optional
     -
     - Needs Human Review: Item #307 | Table HL70136
   * - ``rxg_13``
     - RXG.13
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
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
     - Optional[str]
     - optional
     -
     - Give Rate Amount: Item #332
   * - ``rxg_16``
     - RXG.16
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Give Rate Units: Item #333
   * - ``rxg_17``
     - RXG.17
     - Optional[str]
     - optional
     -
     - Give Strength: Item #1126
   * - ``rxg_18``
     - RXG.18
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Give Strength Units: Item #1127
   * - ``rxg_19``
     - RXG.19
     - Optional[List[str]]
     - optional
     -
     - Substance Lot Number: Item #1129
   * - ``rxg_20``
     - RXG.20
     - Optional[List[:ref:`TS <hl7-v2_3-TS>`]]
     - optional
     -
     - Substance Expiration Date: Item #1130
   * - ``rxg_21``
     - RXG.21
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Substance Manufacturer Name: Item #1131 | Table HL70227
   * - ``rxg_22``
     - RXG.22
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Indication: Item #1123

.. _hl7-v2_3-RXO:

.. py:class:: hl7types.hl7.v2_3.segments.RXO.RXO
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
     - :ref:`CE <hl7-v2_3-CE>`
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
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Requested Give Units: Item #295
   * - ``rxo_5``
     - RXO.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Requested Dosage Form: Item #296
   * - ``rxo_6``
     - RXO.6
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Provider's Pharmacy Instructions: Item #297
   * - ``rxo_7``
     - RXO.7
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Provider's Administration Instructions: Item #298
   * - ``rxo_8``
     - RXO.8
     - Optional[str]
     - optional
     -
     - Deliver To Location: Item #299
   * - ``rxo_9``
     - RXO.9
     - Optional[str]
     - optional
     -
     - Allow Substitutions: Item #300 | Table HL70161
   * - ``rxo_10``
     - RXO.10
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
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
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
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
     - Optional[:ref:`CN <hl7-v2_3-CN>`]
     - optional
     -
     - Ordering Provider's DEA Number: Item #305
   * - ``rxo_15``
     - RXO.15
     - Optional[:ref:`CN <hl7-v2_3-CN>`]
     - optional
     -
     - Pharmacist/Treatment Supplier's Verifier ID: Item #306
   * - ``rxo_16``
     - RXO.16
     - Optional[str]
     - optional
     -
     - Needs Human Review: Item #307 | Table HL70136
   * - ``rxo_17``
     - RXO.17
     - Optional[str]
     - optional
     -
     - Requested Give Per (Time Unit): Item #308
   * - ``rxo_18``
     - RXO.18
     - Optional[str]
     - optional
     -
     - Requested Give Strength: Item #1121
   * - ``rxo_19``
     - RXO.19
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Requested Give Strength Units: Item #1122
   * - ``rxo_20``
     - RXO.20
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Indication: Item #1123
   * - ``rxo_21``
     - RXO.21
     - Optional[str]
     - optional
     -
     - Requested Give Rate Amount: Item #1218
   * - ``rxo_22``
     - RXO.22
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Requested Give Rate Units: Item #1219

.. _hl7-v2_3-RXR:

.. py:class:: hl7types.hl7.v2_3.segments.RXR.RXR
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
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Route: Item #309 | Table HL70162
   * - ``rxr_2``
     - RXR.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Site: Item #310 | Table HL70163
   * - ``rxr_3``
     - RXR.3
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Administration Device: Item #311 | Table HL70164
   * - ``rxr_4``
     - RXR.4
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Administration Method: Item #312 | Table HL70165

.. _hl7-v2_3-SCH:

.. py:class:: hl7types.hl7.v2_3.segments.SCH.SCH
   :noindex:

   HL7 v2 SCH segment.

SCH
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
   * - ``sch_1``
     - SCH.1
     - :ref:`EI <hl7-v2_3-EI>`
     - required
     -
     - Placer Appointment ID: Item #860
   * - ``sch_2``
     - SCH.2
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Filler Appointment ID: Item #861
   * - ``sch_3``
     - SCH.3
     - Optional[str]
     - optional
     -
     - Occurrence Number: Item #862
   * - ``sch_4``
     - SCH.4
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Placer Group Number: Item #863
   * - ``sch_5``
     - SCH.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Schedule ID: Item #864
   * - ``sch_6``
     - SCH.6
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Event Reason: Item #883
   * - ``sch_7``
     - SCH.7
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Appointment Reason: Item #866 | Table HL70276
   * - ``sch_8``
     - SCH.8
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Appointment Type: Item #867 | Table HL70277
   * - ``sch_9``
     - SCH.9
     - Optional[str]
     - optional
     -
     - Appointment Duration: Item #868
   * - ``sch_10``
     - SCH.10
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Appointment Duration Units: Item #869
   * - ``sch_11``
     - SCH.11
     - Optional[List[:ref:`TQ <hl7-v2_3-TQ>`]]
     - optional
     -
     - Appointment Timing Quantity: Item #884
   * - ``sch_12``
     - SCH.12
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Placer Contact Person: Item #874
   * - ``sch_13``
     - SCH.13
     - Optional[:ref:`XTN <hl7-v2_3-XTN>`]
     - optional
     -
     - Placer Contact Phone Number: Item #875
   * - ``sch_14``
     - SCH.14
     - Optional[:ref:`XAD <hl7-v2_3-XAD>`]
     - optional
     -
     - Placer Contact Address: Item #876
   * - ``sch_15``
     - SCH.15
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Placer Contact Location: Item #877
   * - ``sch_16``
     - SCH.16
     - :ref:`XCN <hl7-v2_3-XCN>`
     - required
     -
     - Filler Contact Person: Item #885
   * - ``sch_17``
     - SCH.17
     - Optional[:ref:`XTN <hl7-v2_3-XTN>`]
     - optional
     -
     - Filler Contact Phone Number: Item #886
   * - ``sch_18``
     - SCH.18
     - Optional[:ref:`XAD <hl7-v2_3-XAD>`]
     - optional
     -
     - Filler Contact Address: Item #887
   * - ``sch_19``
     - SCH.19
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Filler Contact Location: Item #888
   * - ``sch_20``
     - SCH.20
     - :ref:`XCN <hl7-v2_3-XCN>`
     - required
     -
     - Entered By Person: Item #878
   * - ``sch_21``
     - SCH.21
     - Optional[List[:ref:`XTN <hl7-v2_3-XTN>`]]
     - optional
     -
     - Entered By Phone Number: Item #879
   * - ``sch_22``
     - SCH.22
     - Optional[:ref:`PL <hl7-v2_3-PL>`]
     - optional
     -
     - Entered By Location: Item #880
   * - ``sch_23``
     - SCH.23
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Parent Placer Appointment ID: Item #881
   * - ``sch_24``
     - SCH.24
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Parent Filler Appointment ID: Item #882
   * - ``sch_25``
     - SCH.25
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Filler Status Code: Item #889 | Table HL70278

.. _hl7-v2_3-SPR:

.. py:class:: hl7types.hl7.v2_3.segments.SPR.SPR
   :noindex:

   HL7 v2 SPR segment.

SPR
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
   * - ``spr_1``
     - SPR.1
     - Optional[str]
     - optional
     -
     - Query tag: Item #696
   * - ``spr_2``
     - SPR.2
     - str
     - required
     -
     - Query/ Response Format Code: Item #697 | Table HL70106
   * - ``spr_3``
     - SPR.3
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Stored procedure name: Item #704
   * - ``spr_4``
     - SPR.4
     - Optional[List[:ref:`QIP <hl7-v2_3-QIP>`]]
     - optional
     -
     - Input parameter list: Item #705

.. _hl7-v2_3-STF:

.. py:class:: hl7types.hl7.v2_3.segments.STF.STF
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
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - STF - Primary Key Value: Item #671
   * - ``stf_2``
     - STF.2
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Staff ID Code: Item #672
   * - ``stf_3``
     - STF.3
     - Optional[:ref:`XPN <hl7-v2_3-XPN>`]
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Date of Birth: Item #110
   * - ``stf_7``
     - STF.7
     - Optional[str]
     - optional
     -
     - Active/Inactive Flag: Item #675 | Table HL70183
   * - ``stf_8``
     - STF.8
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - Department: Item #676 | Table HL70184
   * - ``stf_9``
     - STF.9
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
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
     - Optional[List[:ref:`AD <hl7-v2_3-AD>`]]
     - optional
     -
     - Office/Home Address: Item #679
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
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
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
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Preferred Method of Contact: Item #684 | Table HL70185
   * - ``stf_17``
     - STF.17
     - Optional[List[str]]
     - optional
     -
     - Marital Status: Item #119 | Table HL70002
   * - ``stf_18``
     - STF.18
     - Optional[str]
     - optional
     -
     - Job Title: Item #785
   * - ``stf_19``
     - STF.19
     - Optional[:ref:`JCC <hl7-v2_3-JCC>`]
     - optional
     -
     - Job Code/Class: Item #786
   * - ``stf_20``
     - STF.20
     - Optional[str]
     - optional
     -
     - Employment Status: Item #1276 | Table HL70066
   * - ``stf_21``
     - STF.21
     - Optional[str]
     - optional
     -
     - Additional Insured on Auto: Item #1275 | Table HL70136
   * - ``stf_22``
     - STF.22
     - Optional[:ref:`DLN <hl7-v2_3-DLN>`]
     - optional
     -
     - Driver's License Number: Item #123
   * - ``stf_23``
     - STF.23
     - Optional[str]
     - optional
     -
     - Copy Auto Ins: Item #1229 | Table HL70136
   * - ``stf_24``
     - STF.24
     - Optional[str]
     - optional
     -
     - Auto Ins. Expires: Item #1232
   * - ``stf_25``
     - STF.25
     - Optional[str]
     - optional
     -
     - Date Last DMV Review: Item #1298
   * - ``stf_26``
     - STF.26
     - Optional[str]
     - optional
     -
     - Date Next DMV Review: Item #1297

.. _hl7-v2_3-TXA:

.. py:class:: hl7types.hl7.v2_3.segments.TXA.TXA
   :noindex:

   HL7 v2 TXA segment.

TXA
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
   * - ``txa_1``
     - TXA.1
     - str
     - required
     -
     - Set ID- TXA: Item #914
   * - ``txa_2``
     - TXA.2
     - str
     - required
     -
     - Document Type: Item #915 | Table HL70270
   * - ``txa_3``
     - TXA.3
     - Optional[str]
     - optional
     -
     - Document Content Presentation: Item #916 | Table HL70191
   * - ``txa_4``
     - TXA.4
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Activity Date/Time: Item #917
   * - ``txa_5``
     - TXA.5
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Primary Activity Provider Code/Name: Item #918
   * - ``txa_6``
     - TXA.6
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Origination Date/Time: Item #919
   * - ``txa_7``
     - TXA.7
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Transcription Date/Time: Item #920
   * - ``txa_8``
     - TXA.8
     - Optional[List[:ref:`TS <hl7-v2_3-TS>`]]
     - optional
     -
     - Edit Date/Time: Item #921
   * - ``txa_9``
     - TXA.9
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Originator Code/Name: Item #922
   * - ``txa_10``
     - TXA.10
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Assigned Document Authenticator: Item #923
   * - ``txa_11``
     - TXA.11
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Transcriptionist Code/Name: Item #924
   * - ``txa_12``
     - TXA.12
     - :ref:`EI <hl7-v2_3-EI>`
     - required
     -
     - Unique Document Number: Item #925
   * - ``txa_13``
     - TXA.13
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Parent Document Number: Item #926
   * - ``txa_14``
     - TXA.14
     - Optional[List[:ref:`EI <hl7-v2_3-EI>`]]
     - optional
     -
     - Placer Order Number: Item #216
   * - ``txa_15``
     - TXA.15
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     -
     - Filler Order Number: Item #217
   * - ``txa_16``
     - TXA.16
     - Optional[str]
     - optional
     -
     - Unique Document File Name: Item #927
   * - ``txa_17``
     - TXA.17
     - List[str]
     - required
     -
     - Document Completion Status: Item #928 | Table HL70271
   * - ``txa_18``
     - TXA.18
     - Optional[str]
     - optional
     -
     - Document Confidentiality Status: Item #929 | Table HL70272
   * - ``txa_19``
     - TXA.19
     - Optional[str]
     - optional
     -
     - Document Availability Status: Item #930 | Table HL70273
   * - ``txa_20``
     - TXA.20
     - Optional[str]
     - optional
     -
     - Document Storage Status: Item #932 | Table HL70275
   * - ``txa_21``
     - TXA.21
     - Optional[str]
     - optional
     -
     - Document Change Reason: Item #933
   * - ``txa_22``
     - TXA.22
     - Optional[List[:ref:`PPN <hl7-v2_3-PPN>`]]
     - optional
     -
     - Authentication Person, Time Stamp: Item #934
   * - ``txa_23``
     - TXA.23
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - Distributed Copies (Code and Name of Recipients): Item #935

.. _hl7-v2_3-UB1:

.. py:class:: hl7types.hl7.v2_3.segments.UB1.UB1
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
     - Set ID - UB1: Item #530
   * - ``ub1_2``
     - UB1.2
     - Optional[str]
     - optional
     -
     - Blood Deductible  (43): Item #531
   * - ``ub1_3``
     - UB1.3
     - Optional[str]
     - optional
     -
     - Blood Furnished Pints Of (40): Item #532
   * - ``ub1_4``
     - UB1.4
     - Optional[str]
     - optional
     -
     - Blood Replaced Pints (41): Item #533
   * - ``ub1_5``
     - UB1.5
     - Optional[str]
     - optional
     -
     - Blood Not Replaced Pints(42): Item #534
   * - ``ub1_6``
     - UB1.6
     - Optional[str]
     - optional
     -
     - Co Insurance Days (25): Item #535
   * - ``ub1_7``
     - UB1.7
     - Optional[List[str]]
     - optional
     -
     - Condition Code (35-39): Item #536 | Table HL70043
   * - ``ub1_8``
     - UB1.8
     - Optional[str]
     - optional
     -
     - Covered Days   (23): Item #537
   * - ``ub1_9``
     - UB1.9
     - Optional[str]
     - optional
     -
     - Non Covered Days   (24): Item #538
   * - ``ub1_10``
     - UB1.10
     - Optional[List[str]]
     - optional
     -
     - Value Amount & Code (46-49): Item #539 | Table HL70153
   * - ``ub1_11``
     - UB1.11
     - Optional[str]
     - optional
     -
     - Number Of Grace Days (90): Item #540
   * - ``ub1_12``
     - UB1.12
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Spec Program Indicator (44): Item #541
   * - ``ub1_13``
     - UB1.13
     - Optional[str]
     - optional
     -
     - PSRO/UR Approval Indicator (87): Item #542
   * - ``ub1_14``
     - UB1.14
     - Optional[str]
     - optional
     -
     - PSRO/UR Approved Stay Fm (88): Item #543
   * - ``ub1_15``
     - UB1.15
     - Optional[str]
     - optional
     -
     - PSRO/UR Approved Stay To (89): Item #544
   * - ``ub1_16``
     - UB1.16
     - Optional[List[str]]
     - optional
     -
     - Occurrence (28 32): Item #545
   * - ``ub1_17``
     - UB1.17
     - Optional[str]
     - optional
     -
     - Occurrence Span (33): Item #546
   * - ``ub1_18``
     - UB1.18
     - Optional[str]
     - optional
     -
     - Occur Span Start Date(33): Item #547
   * - ``ub1_19``
     - UB1.19
     - Optional[str]
     - optional
     -
     - Occur Span End Date (33): Item #548
   * - ``ub1_20``
     - UB1.20
     - Optional[str]
     - optional
     -
     - UB 82 Locator 2: Item #549
   * - ``ub1_21``
     - UB1.21
     - Optional[str]
     - optional
     -
     - UB 82 Locator 9: Item #550
   * - ``ub1_22``
     - UB1.22
     - Optional[str]
     - optional
     -
     - UB 82 Locator 27: Item #551
   * - ``ub1_23``
     - UB1.23
     - Optional[str]
     - optional
     -
     - UB 82 Locator 45: Item #552

.. _hl7-v2_3-UB2:

.. py:class:: hl7types.hl7.v2_3.segments.UB2.UB2
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
     - Set ID - UB2: Item #553
   * - ``ub2_2``
     - UB2.2
     - Optional[str]
     - optional
     -
     - Co-Insurance Days (9): Item #554
   * - ``ub2_3``
     - UB2.3
     - Optional[List[str]]
     - optional
     -
     - Condition Code (24-30): Item #555 | Table HL70043
   * - ``ub2_4``
     - UB2.4
     - Optional[str]
     - optional
     -
     - Covered Days (7): Item #556
   * - ``ub2_5``
     - UB2.5
     - Optional[str]
     - optional
     -
     - Non-Covered Days (8): Item #557
   * - ``ub2_6``
     - UB2.6
     - Optional[List[str]]
     - optional
     -
     - Value Amount & Code: Item #558
   * - ``ub2_7``
     - UB2.7
     - Optional[List[str]]
     - optional
     -
     - Occurrence Code & Date (32-35): Item #559
   * - ``ub2_8``
     - UB2.8
     - Optional[List[str]]
     - optional
     -
     - Occurrence Span Code/Dates (36): Item #560
   * - ``ub2_9``
     - UB2.9
     - Optional[List[str]]
     - optional
     -
     - UB92 Locator 2 (State): Item #561
   * - ``ub2_10``
     - UB2.10
     - Optional[List[str]]
     - optional
     -
     - UB92 Locator 11 (State): Item #562
   * - ``ub2_11``
     - UB2.11
     - Optional[str]
     - optional
     -
     - UB92 Locator 31 (National): Item #563
   * - ``ub2_12``
     - UB2.12
     - Optional[List[str]]
     - optional
     -
     - Document Control Number: Item #564
   * - ``ub2_13``
     - UB2.13
     - Optional[List[str]]
     - optional
     -
     - UB92 Locator 49 (National): Item #565
   * - ``ub2_14``
     - UB2.14
     - Optional[List[str]]
     - optional
     -
     - UB92 Locator 56 (State): Item #566
   * - ``ub2_15``
     - UB2.15
     - Optional[str]
     - optional
     -
     - UB92 Locator 57 (National): Item #567
   * - ``ub2_16``
     - UB2.16
     - Optional[List[str]]
     - optional
     -
     - UB92 Locator 78 (State): Item #568
   * - ``ub2_17``
     - UB2.17
     - Optional[str]
     - optional
     -
     - Special Visit Count: Item #815

.. _hl7-v2_3-URD:

.. py:class:: hl7types.hl7.v2_3.segments.URD.URD
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - R/U Date/Time: Item #45
   * - ``urd_2``
     - URD.2
     - Optional[str]
     - optional
     -
     - Report Priority: Item #46 | Table HL70109
   * - ``urd_3``
     - URD.3
     - Optional[List[:ref:`XCN <hl7-v2_3-XCN>`]]
     - optional
     -
     - R/U Who Subject Definition: Item #47
   * - ``urd_4``
     - URD.4
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - R/U What Subject Definition: Item #48 | Table HL70048
   * - ``urd_5``
     - URD.5
     - Optional[List[:ref:`CE <hl7-v2_3-CE>`]]
     - optional
     -
     - R/U What Department Code: Item #49
   * - ``urd_6``
     - URD.6
     - Optional[List[str]]
     - optional
     -
     - R/U Display/Print Locations: Item #50
   * - ``urd_7``
     - URD.7
     - Optional[str]
     - optional
     -
     - R/U Results Level: Item #51 | Table HL70108

.. _hl7-v2_3-URS:

.. py:class:: hl7types.hl7.v2_3.segments.URS.URS
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
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - R/U When Data Start Date/Time: Item #53
   * - ``urs_3``
     - URS.3
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - R/U When Data End Date/Time: Item #54
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
     - R/U Which Date/Time Qualifier: Item #57 | Table HL70156
   * - ``urs_7``
     - URS.7
     - Optional[List[str]]
     - optional
     -
     - R/U Which Date/Time Status Qualifier: Item #58 | Table HL70157
   * - ``urs_8``
     - URS.8
     - Optional[List[str]]
     - optional
     -
     - R/U Date/Time Selection Qualifier: Item #59 | Table HL70158
   * - ``urs_9``
     - URS.9
     - Optional[:ref:`TQ <hl7-v2_3-TQ>`]
     - optional
     -
     - R/U Quantity/Timing Qualifier: Item #695

.. _hl7-v2_3-VAR:

.. py:class:: hl7types.hl7.v2_3.segments.VAR.VAR
   :noindex:

   HL7 v2 VAR segment.

VAR
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
   * - ``var_1``
     - VAR.1
     - :ref:`EI <hl7-v2_3-EI>`
     - required
     -
     - Variance Instance ID: Item #1212
   * - ``var_2``
     - VAR.2
     - :ref:`TS <hl7-v2_3-TS>`
     - required
     -
     - Documented Date/Time: Item #1213
   * - ``var_3``
     - VAR.3
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     -
     - Stated Variance Date/Time: Item #1214
   * - ``var_4``
     - VAR.4
     - Optional[:ref:`XCN <hl7-v2_3-XCN>`]
     - optional
     -
     - Variance Originator: Item #1215
   * - ``var_5``
     - VAR.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     -
     - Variance Classification: Item #1216
   * - ``var_6``
     - VAR.6
     - Optional[List[str]]
     - optional
     -
     - Variance Description: Item #1217

.. _hl7-v2_3-VTQ:

.. py:class:: hl7types.hl7.v2_3.segments.VTQ.VTQ
   :noindex:

   HL7 v2 VTQ segment.

VTQ
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
   * - ``vtq_1``
     - VTQ.1
     - Optional[str]
     - optional
     -
     - Query tag: Item #696
   * - ``vtq_2``
     - VTQ.2
     - str
     - required
     -
     - Query/ Response Format Code: Item #697 | Table HL70106
   * - ``vtq_3``
     - VTQ.3
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - VT Query Name: Item #698
   * - ``vtq_4``
     - VTQ.4
     - :ref:`CE <hl7-v2_3-CE>`
     - required
     -
     - Virtual Table Name: Item #699
   * - ``vtq_5``
     - VTQ.5
     - Optional[List[:ref:`QSC <hl7-v2_3-QSC>`]]
     - optional
     -
     - Selection Criteria: Item #700
