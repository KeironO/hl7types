v2.8.2 Segments
===============

.. _hl7-v2_8_2-ABS:

.. py:class:: hl7types.hl7.v2_8_2.segments.ABS.ABS
   :noindex:

   HL7 v2 ABS segment.

ABS
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``abs_1``
     - ABS.1
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Discharge Care Provider: Item #1514 | Table HL70010
   * - ``abs_2``
     - ABS.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Transfer Medical Service Code: Item #1515 | Table HL70069
   * - ``abs_3``
     - ABS.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Severity of Illness Code: Item #1516 | Table HL70421
   * - ``abs_4``
     - ABS.4
     - Optional[str]
     - optional
     - Date/Time of Attestation: Item #1517
   * - ``abs_5``
     - ABS.5
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Attested By: Item #1518
   * - ``abs_6``
     - ABS.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Triage Code: Item #1519 | Table HL70422
   * - ``abs_7``
     - ABS.7
     - Optional[str]
     - optional
     - Abstract Completion Date/Time: Item #1520
   * - ``abs_8``
     - ABS.8
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Abstracted By: Item #1521
   * - ``abs_9``
     - ABS.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Case Category Code: Item #1522 | Table HL70423
   * - ``abs_10``
     - ABS.10
     - Optional[str]
     - optional
     - Caesarian Section Indicator: Item #1523 | Table HL70136
   * - ``abs_11``
     - ABS.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Gestation Category Code: Item #1524 | Table HL70424
   * - ``abs_12``
     - ABS.12
     - Optional[str]
     - optional
     - Gestation Period - Weeks: Item #1525
   * - ``abs_13``
     - ABS.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Newborn Code: Item #1526 | Table HL70425
   * - ``abs_14``
     - ABS.14
     - Optional[str]
     - optional
     - Stillborn Indicator: Item #1527 | Table HL70136

.. _hl7-v2_8_2-ACC:

.. py:class:: hl7types.hl7.v2_8_2.segments.ACC.ACC
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
     - Description
   * - ``acc_1``
     - ACC.1
     - Optional[str]
     - optional
     - Accident Date/Time: Item #527
   * - ``acc_2``
     - ACC.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Accident Code: Item #528 | Table HL70050
   * - ``acc_3``
     - ACC.3
     - Optional[str]
     - optional
     - Accident Location: Item #529
   * - ``acc_4``
     - ACC.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Auto Accident State: Item #812 | Table HL70347
   * - ``acc_5``
     - ACC.5
     - Optional[str]
     - optional
     - Accident Job Related Indicator: Item #813 | Table HL70136
   * - ``acc_6``
     - ACC.6
     - Optional[str]
     - optional
     - Accident Death Indicator: Item #814 | Table HL70136
   * - ``acc_7``
     - ACC.7
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Entered By: Item #224
   * - ``acc_8``
     - ACC.8
     - Optional[str]
     - optional
     - Accident Description: Item #1503
   * - ``acc_9``
     - ACC.9
     - Optional[str]
     - optional
     - Brought In By: Item #1504
   * - ``acc_10``
     - ACC.10
     - Optional[str]
     - optional
     - Police Notified Indicator: Item #1505 | Table HL70136
   * - ``acc_11``
     - ACC.11
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - Accident Address: Item #1853
   * - ``acc_12``
     - ACC.12
     - Optional[str]
     - optional
     - Degree of patient liability: Item #2374
   * - ``acc_13``
     - ACC.13
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Accident Identifier: Item #3338

.. _hl7-v2_8_2-ADD:

.. py:class:: hl7types.hl7.v2_8_2.segments.ADD.ADD
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
     - Description
   * - ``add_1``
     - ADD.1
     - Optional[str]
     - optional
     - Addendum Continuation Pointer: Item #66

.. _hl7-v2_8_2-ADJ:

.. py:class:: hl7types.hl7.v2_8_2.segments.ADJ.ADJ
   :noindex:

   HL7 v2 ADJ segment.

ADJ
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``adj_1``
     - ADJ.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Provider Adjustment Number: Item #2003
   * - ``adj_2``
     - ADJ.2
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Payer Adjustment Number: Item #2004
   * - ``adj_3``
     - ADJ.3
     - str
     - required
     - Adjustment Sequence Number: Item #2005
   * - ``adj_4``
     - ADJ.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Adjustment Category: Item #2006 | Table HL70564
   * - ``adj_5``
     - ADJ.5
     - Optional[List[:ref:`CP <hl7-v2_8_2-CP>`]]
     - optional
     - Adjustment Amount: Item #2007
   * - ``adj_6``
     - ADJ.6
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Adjustment Quantity: Item #2008 | Table HL70560
   * - ``adj_7``
     - ADJ.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Adjustment Reason PA: Item #2009 | Table HL70565
   * - ``adj_8``
     - ADJ.8
     - Optional[str]
     - optional
     - Adjustment Description: Item #2010
   * - ``adj_9``
     - ADJ.9
     - Optional[str]
     - optional
     - Original Value: Item #2011
   * - ``adj_10``
     - ADJ.10
     - Optional[str]
     - optional
     - Substitute Value: Item #2012
   * - ``adj_11``
     - ADJ.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Adjustment Action: Item #2013 | Table HL70569
   * - ``adj_12``
     - ADJ.12
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Provider Adjustment Number Cross Reference: Item #2014
   * - ``adj_13``
     - ADJ.13
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Provider Product/Service Line Item Number Cross Reference: Item #2015
   * - ``adj_14``
     - ADJ.14
     - str
     - required
     - Adjustment Date: Item #2016
   * - ``adj_15``
     - ADJ.15
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Responsible Organization: Item #2017

.. _hl7-v2_8_2-AFF:

.. py:class:: hl7types.hl7.v2_8_2.segments.AFF.AFF
   :noindex:

   HL7 v2 AFF segment.

AFF
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``aff_1``
     - AFF.1
     - str
     - required
     - Set ID - AFF: Item #1427
   * - ``aff_2``
     - AFF.2
     - :ref:`XON <hl7-v2_8_2-XON>`
     - required
     - Professional Organization: Item #1444
   * - ``aff_3``
     - AFF.3
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - Professional Organization Address: Item #1445
   * - ``aff_4``
     - AFF.4
     - Optional[List[:ref:`DR <hl7-v2_8_2-DR>`]]
     - optional
     - Professional Organization Affiliation Date Range: Item #1446
   * - ``aff_5``
     - AFF.5
     - Optional[str]
     - optional
     - Professional Affiliation Additional Information: Item #1447

.. _hl7-v2_8_2-AIG:

.. py:class:: hl7types.hl7.v2_8_2.segments.AIG.AIG
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
     - Description
   * - ``aig_1``
     - AIG.1
     - str
     - required
     - Set ID - AIG: Item #896
   * - ``aig_2``
     - AIG.2
     - Optional[str]
     - optional
     - Segment Action Code: Item #763 | Table HL70206
   * - ``aig_3``
     - AIG.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Resource ID: Item #897
   * - ``aig_4``
     - AIG.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Resource Type: Item #898
   * - ``aig_5``
     - AIG.5
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Resource Group: Item #899
   * - ``aig_6``
     - AIG.6
     - Optional[str]
     - optional
     - Resource Quantity: Item #900
   * - ``aig_7``
     - AIG.7
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Resource Quantity Units: Item #901
   * - ``aig_8``
     - AIG.8
     - Optional[str]
     - optional
     - Start Date/Time: Item #1202
   * - ``aig_9``
     - AIG.9
     - Optional[str]
     - optional
     - Start Date/Time Offset: Item #891
   * - ``aig_10``
     - AIG.10
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Start Date/Time Offset Units: Item #892
   * - ``aig_11``
     - AIG.11
     - Optional[str]
     - optional
     - Duration: Item #893
   * - ``aig_12``
     - AIG.12
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Duration Units: Item #894
   * - ``aig_13``
     - AIG.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Allow Substitution Code: Item #895 | Table HL70279
   * - ``aig_14``
     - AIG.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Filler Status Code: Item #889 | Table HL70278

.. _hl7-v2_8_2-AIL:

.. py:class:: hl7types.hl7.v2_8_2.segments.AIL.AIL
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
     - Description
   * - ``ail_1``
     - AIL.1
     - str
     - required
     - Set ID - AIL: Item #902
   * - ``ail_2``
     - AIL.2
     - Optional[str]
     - optional
     - Segment Action Code: Item #763 | Table HL70206
   * - ``ail_3``
     - AIL.3
     - Optional[List[:ref:`PL <hl7-v2_8_2-PL>`]]
     - optional
     - Location Resource ID: Item #903
   * - ``ail_4``
     - AIL.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Location Type - AIL: Item #904 | Table HL70305
   * - ``ail_5``
     - AIL.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Location Group: Item #905
   * - ``ail_6``
     - AIL.6
     - Optional[str]
     - optional
     - Start Date/Time: Item #1202
   * - ``ail_7``
     - AIL.7
     - Optional[str]
     - optional
     - Start Date/Time Offset: Item #891
   * - ``ail_8``
     - AIL.8
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Start Date/Time Offset Units: Item #892
   * - ``ail_9``
     - AIL.9
     - Optional[str]
     - optional
     - Duration: Item #893
   * - ``ail_10``
     - AIL.10
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Duration Units: Item #894
   * - ``ail_11``
     - AIL.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Allow Substitution Code: Item #895 | Table HL70279
   * - ``ail_12``
     - AIL.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Filler Status Code: Item #889 | Table HL70278

.. _hl7-v2_8_2-AIP:

.. py:class:: hl7types.hl7.v2_8_2.segments.AIP.AIP
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
     - Description
   * - ``aip_1``
     - AIP.1
     - str
     - required
     - Set ID - AIP: Item #906
   * - ``aip_2``
     - AIP.2
     - Optional[str]
     - optional
     - Segment Action Code: Item #763 | Table HL70206
   * - ``aip_3``
     - AIP.3
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Personnel Resource ID: Item #913
   * - ``aip_4``
     - AIP.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Resource Type: Item #907 | Table HL70182
   * - ``aip_5``
     - AIP.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Resource Group: Item #899
   * - ``aip_6``
     - AIP.6
     - Optional[str]
     - optional
     - Start Date/Time: Item #1202
   * - ``aip_7``
     - AIP.7
     - Optional[str]
     - optional
     - Start Date/Time Offset: Item #891
   * - ``aip_8``
     - AIP.8
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Start Date/Time Offset Units: Item #892
   * - ``aip_9``
     - AIP.9
     - Optional[str]
     - optional
     - Duration: Item #893
   * - ``aip_10``
     - AIP.10
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Duration Units: Item #894
   * - ``aip_11``
     - AIP.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Allow Substitution Code: Item #895 | Table HL70279
   * - ``aip_12``
     - AIP.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Filler Status Code: Item #889 | Table HL70278

.. _hl7-v2_8_2-AIS:

.. py:class:: hl7types.hl7.v2_8_2.segments.AIS.AIS
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
     - Description
   * - ``ais_1``
     - AIS.1
     - str
     - required
     - Set ID - AIS: Item #890
   * - ``ais_2``
     - AIS.2
     - Optional[str]
     - optional
     - Segment Action Code: Item #763 | Table HL70206
   * - ``ais_3``
     - AIS.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Universal Service Identifier: Item #238
   * - ``ais_4``
     - AIS.4
     - Optional[str]
     - optional
     - Start Date/Time: Item #1202
   * - ``ais_5``
     - AIS.5
     - Optional[str]
     - optional
     - Start Date/Time Offset: Item #891
   * - ``ais_6``
     - AIS.6
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Start Date/Time Offset Units: Item #892
   * - ``ais_7``
     - AIS.7
     - Optional[str]
     - optional
     - Duration: Item #893
   * - ``ais_8``
     - AIS.8
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Duration Units: Item #894
   * - ``ais_9``
     - AIS.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Allow Substitution Code: Item #895 | Table HL70279
   * - ``ais_10``
     - AIS.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Filler Status Code: Item #889 | Table HL70278
   * - ``ais_11``
     - AIS.11
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Placer Supplemental Service Information: Item #1474 | Table HL70411
   * - ``ais_12``
     - AIS.12
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Filler Supplemental Service Information: Item #1475 | Table HL70411

.. _hl7-v2_8_2-AL1:

.. py:class:: hl7types.hl7.v2_8_2.segments.AL1.AL1
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
     - Description
   * - ``al1_1``
     - AL1.1
     - str
     - required
     - Set ID - AL1: Item #203
   * - ``al1_2``
     - AL1.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Allergen Type Code: Item #204 | Table HL70127
   * - ``al1_3``
     - AL1.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Allergen Code/Mnemonic/Description: Item #205
   * - ``al1_4``
     - AL1.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Allergy Severity Code: Item #206 | Table HL70128
   * - ``al1_5``
     - AL1.5
     - Optional[List[str]]
     - optional
     - Allergy Reaction Code: Item #207

.. _hl7-v2_8_2-APR:

.. py:class:: hl7types.hl7.v2_8_2.segments.APR.APR
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
     - Description
   * - ``apr_1``
     - APR.1
     - Optional[List[:ref:`SCV <hl7-v2_8_2-SCV>`]]
     - optional
     - Time Selection Criteria: Item #908 | Table HL70294
   * - ``apr_2``
     - APR.2
     - Optional[List[:ref:`SCV <hl7-v2_8_2-SCV>`]]
     - optional
     - Resource Selection Criteria: Item #909 | Table HL70294
   * - ``apr_3``
     - APR.3
     - Optional[List[:ref:`SCV <hl7-v2_8_2-SCV>`]]
     - optional
     - Location Selection Criteria: Item #910 | Table HL70294
   * - ``apr_4``
     - APR.4
     - Optional[str]
     - optional
     - Slot Spacing Criteria: Item #911
   * - ``apr_5``
     - APR.5
     - Optional[List[:ref:`SCV <hl7-v2_8_2-SCV>`]]
     - optional
     - Filler Override Criteria: Item #912

.. _hl7-v2_8_2-ARQ:

.. py:class:: hl7types.hl7.v2_8_2.segments.ARQ.ARQ
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
     - Description
   * - ``arq_1``
     - ARQ.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Placer Appointment ID: Item #860
   * - ``arq_2``
     - ARQ.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Filler Appointment ID: Item #861
   * - ``arq_3``
     - ARQ.3
     - Optional[str]
     - optional
     - Occurrence Number: Item #862
   * - ``arq_4``
     - ARQ.4
     - Optional[:ref:`EIP <hl7-v2_8_2-EIP>`]
     - optional
     - Placer Group Number: Item #218
   * - ``arq_5``
     - ARQ.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Schedule ID: Item #864
   * - ``arq_6``
     - ARQ.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Request Event Reason: Item #865
   * - ``arq_7``
     - ARQ.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Appointment Reason: Item #866 | Table HL70276
   * - ``arq_8``
     - ARQ.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Appointment Type: Item #867 | Table HL70277
   * - ``arq_9``
     - ARQ.9
     - Optional[str]
     - optional
     - Appointment Duration: Item #868
   * - ``arq_10``
     - ARQ.10
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Appointment Duration Units: Item #869
   * - ``arq_11``
     - ARQ.11
     - Optional[List[:ref:`DR <hl7-v2_8_2-DR>`]]
     - optional
     - Requested Start Date/Time Range: Item #870
   * - ``arq_12``
     - ARQ.12
     - Optional[str]
     - optional
     - Priority-ARQ: Item #871
   * - ``arq_13``
     - ARQ.13
     - Optional[:ref:`RI <hl7-v2_8_2-RI>`]
     - optional
     - Repeating Interval: Item #872
   * - ``arq_14``
     - ARQ.14
     - Optional[str]
     - optional
     - Repeating Interval Duration: Item #873
   * - ``arq_15``
     - ARQ.15
     - List[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - required
     - Placer Contact Person: Item #874
   * - ``arq_16``
     - ARQ.16
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Placer Contact Phone Number: Item #875
   * - ``arq_17``
     - ARQ.17
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Placer Contact Address: Item #876
   * - ``arq_18``
     - ARQ.18
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Placer Contact Location: Item #877
   * - ``arq_19``
     - ARQ.19
     - List[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - required
     - Entered By Person: Item #878
   * - ``arq_20``
     - ARQ.20
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Entered By Phone Number: Item #879
   * - ``arq_21``
     - ARQ.21
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Entered By Location: Item #880
   * - ``arq_22``
     - ARQ.22
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Parent Placer Appointment ID: Item #881
   * - ``arq_23``
     - ARQ.23
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Parent Filler Appointment ID: Item #882
   * - ``arq_24``
     - ARQ.24
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Placer Order Number: Item #216
   * - ``arq_25``
     - ARQ.25
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Filler Order Number: Item #217

.. _hl7-v2_8_2-ARV:

.. py:class:: hl7types.hl7.v2_8_2.segments.ARV.ARV
   :noindex:

   HL7 v2 ARV segment.

ARV
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``arv_1``
     - ARV.1
     - Optional[str]
     - optional
     - Set ID: Item #2143
   * - ``arv_2``
     - ARV.2
     - :ref:`CNE <hl7-v2_8_2-CNE>`
     - required
     - Access Restriction Action Code: Item #2144 | Table HL70206
   * - ``arv_3``
     - ARV.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Access Restriction Value: Item #2145 | Table HL70717
   * - ``arv_4``
     - ARV.4
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Access Restriction Reason: Item #2146 | Table HL70719
   * - ``arv_5``
     - ARV.5
     - Optional[List[str]]
     - optional
     - Special Access Restriction Instructions: Item #2147
   * - ``arv_6``
     - ARV.6
     - Optional[:ref:`DR <hl7-v2_8_2-DR>`]
     - optional
     - Access Restriction Date Range: Item #2148

.. _hl7-v2_8_2-AUT:

.. py:class:: hl7types.hl7.v2_8_2.segments.AUT.AUT
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
     - Description
   * - ``aut_1``
     - AUT.1
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Authorizing Payor, Plan ID: Item #1146 | Table HL70072
   * - ``aut_2``
     - AUT.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Authorizing Payor, Company ID: Item #1147 | Table HL70285
   * - ``aut_3``
     - AUT.3
     - Optional[str]
     - optional
     - Authorizing Payor, Company Name: Item #1148
   * - ``aut_4``
     - AUT.4
     - Optional[str]
     - optional
     - Authorization Effective Date: Item #1149
   * - ``aut_5``
     - AUT.5
     - Optional[str]
     - optional
     - Authorization Expiration Date: Item #1150
   * - ``aut_6``
     - AUT.6
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Authorization Identifier: Item #1151
   * - ``aut_7``
     - AUT.7
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Reimbursement Limit: Item #1152
   * - ``aut_8``
     - AUT.8
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Requested Number of Treatments: Item #1153
   * - ``aut_9``
     - AUT.9
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Authorized Number of Treatments: Item #1154
   * - ``aut_10``
     - AUT.10
     - Optional[str]
     - optional
     - Process Date: Item #1145
   * - ``aut_11``
     - AUT.11
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Requested Discipline(s): Item #2375
   * - ``aut_12``
     - AUT.12
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Authorized Discipline(s): Item #2376
   * - ``aut_13``
     - AUT.13
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Authorization Referral Type: Item #3413
   * - ``aut_14``
     - AUT.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Approval Status: Item #3414
   * - ``aut_15``
     - AUT.15
     - Optional[str]
     - optional
     - Planned Treatment Stop Date: Item #3415
   * - ``aut_16``
     - AUT.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Clinical Service: Item #3416
   * - ``aut_17``
     - AUT.17
     - Optional[str]
     - optional
     - Reason Text: Item #3417
   * - ``aut_18``
     - AUT.18
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Number of Authorized Treatments/Units: Item #3418
   * - ``aut_19``
     - AUT.19
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Number of Used Treatments/Units: Item #3419
   * - ``aut_20``
     - AUT.20
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Number of Schedule Treatments/Units: Item #3420
   * - ``aut_21``
     - AUT.21
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Encounter Type: Item #3421
   * - ``aut_22``
     - AUT.22
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Remaining Benefit Amount: Item #3422
   * - ``aut_23``
     - AUT.23
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Authorized Provider: Item #3423
   * - ``aut_24``
     - AUT.24
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Authorized Health Professional: Item #3424
   * - ``aut_25``
     - AUT.25
     - Optional[str]
     - optional
     - Source Text: Item #3425
   * - ``aut_26``
     - AUT.26
     - Optional[str]
     - optional
     - Source Date: Item #3426
   * - ``aut_27``
     - AUT.27
     - Optional[:ref:`XTN <hl7-v2_8_2-XTN>`]
     - optional
     - Source Phone: Item #3427
   * - ``aut_28``
     - AUT.28
     - Optional[str]
     - optional
     - Comment: Item #3428
   * - ``aut_29``
     - AUT.29
     - Optional[str]
     - optional
     - Action Code: Item #3429 | Table HL70206

.. _hl7-v2_8_2-BHS:

.. py:class:: hl7types.hl7.v2_8_2.segments.BHS.BHS
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
     - Description
   * - ``bhs_1``
     - BHS.1
     - str
     - optional
     - Batch Field Separator: Item #81
   * - ``bhs_2``
     - BHS.2
     - str
     - optional
     - Batch Encoding Characters: Item #82
   * - ``bhs_3``
     - BHS.3
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Batch Sending Application: Item #83
   * - ``bhs_4``
     - BHS.4
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Batch Sending Facility: Item #84
   * - ``bhs_5``
     - BHS.5
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Batch Receiving Application: Item #85
   * - ``bhs_6``
     - BHS.6
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Batch Receiving Facility: Item #86
   * - ``bhs_7``
     - BHS.7
     - Optional[str]
     - optional
     - Batch Creation Date/Time: Item #87
   * - ``bhs_8``
     - BHS.8
     - Optional[str]
     - optional
     - Batch Security: Item #88
   * - ``bhs_9``
     - BHS.9
     - Optional[str]
     - optional
     - Batch Name/ID/Type: Item #89
   * - ``bhs_10``
     - BHS.10
     - Optional[str]
     - optional
     - Batch Comment: Item #90
   * - ``bhs_11``
     - BHS.11
     - Optional[str]
     - optional
     - Batch Control ID: Item #91
   * - ``bhs_12``
     - BHS.12
     - Optional[str]
     - optional
     - Reference Batch Control ID: Item #92
   * - ``bhs_13``
     - BHS.13
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Batch Sending Network Address: Item #2271
   * - ``bhs_14``
     - BHS.14
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Batch Receiving Network Address: Item #2272

.. _hl7-v2_8_2-BLC:

.. py:class:: hl7types.hl7.v2_8_2.segments.BLC.BLC
   :noindex:

   HL7 v2 BLC segment.

BLC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``blc_1``
     - BLC.1
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Blood Product Code: Item #1528 | Table HL70426
   * - ``blc_2``
     - BLC.2
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Blood Amount: Item #1529

.. _hl7-v2_8_2-BLG:

.. py:class:: hl7types.hl7.v2_8_2.segments.BLG.BLG
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
     - Description
   * - ``blg_1``
     - BLG.1
     - Optional[:ref:`CCD <hl7-v2_8_2-CCD>`]
     - optional
     - When to Charge: Item #234 | Table HL70100
   * - ``blg_2``
     - BLG.2
     - Optional[str]
     - optional
     - Charge Type: Item #235 | Table HL70122
   * - ``blg_3``
     - BLG.3
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Account ID: Item #236
   * - ``blg_4``
     - BLG.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Charge Type Reason: Item #1645 | Table HL70475

.. _hl7-v2_8_2-BPO:

.. py:class:: hl7types.hl7.v2_8_2.segments.BPO.BPO
   :noindex:

   HL7 v2 BPO segment.

BPO
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``bpo_1``
     - BPO.1
     - str
     - required
     - Set ID - BPO: Item #1700
   * - ``bpo_2``
     - BPO.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - BP Universal Service Identifier: Item #1701 | Table HL79999
   * - ``bpo_3``
     - BPO.3
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - BP  Processing Requirements: Item #1702 | Table HL70508
   * - ``bpo_4``
     - BPO.4
     - str
     - required
     - BP Quantity: Item #1703
   * - ``bpo_5``
     - BPO.5
     - Optional[str]
     - optional
     - BP Amount: Item #1704
   * - ``bpo_6``
     - BPO.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - BP Units: Item #1705 | Table HL79999
   * - ``bpo_7``
     - BPO.7
     - Optional[str]
     - optional
     - BP Intended Use Date/Time: Item #1706
   * - ``bpo_8``
     - BPO.8
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - BP Intended Dispense From Location: Item #1707
   * - ``bpo_9``
     - BPO.9
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - BP Intended Dispense From Address: Item #1708
   * - ``bpo_10``
     - BPO.10
     - Optional[str]
     - optional
     - BP Requested Dispense Date/Time: Item #1709
   * - ``bpo_11``
     - BPO.11
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - BP Requested Dispense To Location: Item #1710
   * - ``bpo_12``
     - BPO.12
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - BP Requested Dispense To Address: Item #1711
   * - ``bpo_13``
     - BPO.13
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - BP Indication for Use: Item #1712 | Table HL70509
   * - ``bpo_14``
     - BPO.14
     - Optional[str]
     - optional
     - BP Informed Consent Indicator: Item #1713 | Table HL70136

.. _hl7-v2_8_2-BPX:

.. py:class:: hl7types.hl7.v2_8_2.segments.BPX.BPX
   :noindex:

   HL7 v2 BPX segment.

BPX
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``bpx_1``
     - BPX.1
     - str
     - required
     - Set ID - BPX: Item #1714
   * - ``bpx_2``
     - BPX.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - BP Dispense Status: Item #1715 | Table HL70510
   * - ``bpx_3``
     - BPX.3
     - str
     - required
     - BP Status: Item #1716 | Table HL70511
   * - ``bpx_4``
     - BPX.4
     - str
     - required
     - BP Date/Time of Status: Item #1717
   * - ``bpx_5``
     - BPX.5
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - BC Donation ID: Item #1718
   * - ``bpx_6``
     - BPX.6
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - BC Component: Item #1719 | Table HL79999
   * - ``bpx_7``
     - BPX.7
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - BC Donation Type / Intended Use: Item #1720 | Table HL79999
   * - ``bpx_8``
     - BPX.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - CP Commercial Product: Item #1721 | Table HL70512
   * - ``bpx_9``
     - BPX.9
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - CP Manufacturer: Item #1722
   * - ``bpx_10``
     - BPX.10
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - CP Lot Number: Item #1723
   * - ``bpx_11``
     - BPX.11
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - BP Blood Group: Item #1724 | Table HL79999
   * - ``bpx_12``
     - BPX.12
     - Optional[List[:ref:`CNE <hl7-v2_8_2-CNE>`]]
     - optional
     - BC Special Testing: Item #1725 | Table HL79999
   * - ``bpx_13``
     - BPX.13
     - Optional[str]
     - optional
     - BP Expiration Date/Time: Item #1726
   * - ``bpx_14``
     - BPX.14
     - str
     - required
     - BP Quantity: Item #1727
   * - ``bpx_15``
     - BPX.15
     - Optional[str]
     - optional
     - BP Amount: Item #1728
   * - ``bpx_16``
     - BPX.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - BP Units: Item #1729 | Table HL79999
   * - ``bpx_17``
     - BPX.17
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - BP Unique ID: Item #1730
   * - ``bpx_18``
     - BPX.18
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - BP Actual Dispensed To Location: Item #1731
   * - ``bpx_19``
     - BPX.19
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - BP Actual Dispensed To Address: Item #1732
   * - ``bpx_20``
     - BPX.20
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - BP Dispensed to Receiver: Item #1733
   * - ``bpx_21``
     - BPX.21
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - BP Dispensing Individual: Item #1734

.. _hl7-v2_8_2-BTS:

.. py:class:: hl7types.hl7.v2_8_2.segments.BTS.BTS
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
     - Description
   * - ``bts_1``
     - BTS.1
     - Optional[str]
     - optional
     - Batch Message Count: Item #93
   * - ``bts_2``
     - BTS.2
     - Optional[str]
     - optional
     - Batch Comment: Item #90
   * - ``bts_3``
     - BTS.3
     - Optional[List[str]]
     - optional
     - Batch Totals: Item #95

.. _hl7-v2_8_2-BTX:

.. py:class:: hl7types.hl7.v2_8_2.segments.BTX.BTX
   :noindex:

   HL7 v2 BTX segment.

BTX
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``btx_1``
     - BTX.1
     - str
     - required
     - Set ID - BTX: Item #1735
   * - ``btx_2``
     - BTX.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - BC Donation ID: Item #1736
   * - ``btx_3``
     - BTX.3
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - BC Component: Item #1737 | Table HL79999
   * - ``btx_4``
     - BTX.4
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - BC Blood Group: Item #1738 | Table HL79999
   * - ``btx_5``
     - BTX.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - CP Commercial Product: Item #1739 | Table HL70512
   * - ``btx_6``
     - BTX.6
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - CP Manufacturer: Item #1740
   * - ``btx_7``
     - BTX.7
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - CP Lot Number: Item #1741
   * - ``btx_8``
     - BTX.8
     - str
     - required
     - BP Quantity: Item #1742
   * - ``btx_9``
     - BTX.9
     - Optional[str]
     - optional
     - BP Amount: Item #1743
   * - ``btx_10``
     - BTX.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - BP Units: Item #1744 | Table HL79999
   * - ``btx_11``
     - BTX.11
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - BP Transfusion/Disposition Status: Item #1745 | Table HL70513
   * - ``btx_12``
     - BTX.12
     - str
     - required
     - BP Message Status: Item #1746 | Table HL70511
   * - ``btx_13``
     - BTX.13
     - str
     - required
     - BP Date/Time of Status: Item #1747
   * - ``btx_14``
     - BTX.14
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - BP Transfusion Administrator: Item #1748
   * - ``btx_15``
     - BTX.15
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - BP Transfusion Verifier: Item #1749
   * - ``btx_16``
     - BTX.16
     - Optional[str]
     - optional
     - BP Transfusion Start Date/Time of Status: Item #1750
   * - ``btx_17``
     - BTX.17
     - Optional[str]
     - optional
     - BP Transfusion End Date/Time of Status: Item #1751
   * - ``btx_18``
     - BTX.18
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - BP Adverse Reaction Type: Item #1752 | Table HL70514
   * - ``btx_19``
     - BTX.19
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - BP Transfusion Interrupted Reason: Item #1753 | Table HL70515
   * - ``btx_20``
     - BTX.20
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - BP Unique ID: Item #3391

.. _hl7-v2_8_2-BUI:

.. py:class:: hl7types.hl7.v2_8_2.segments.BUI.BUI
   :noindex:

   HL7 v2 BUI segment.

BUI
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``bui_1``
     - BUI.1
     - Optional[str]
     - optional
     - Set ID - BUI: Item #3373
   * - ``bui_2``
     - BUI.2
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Blood Unit Identifier: Item #3374
   * - ``bui_3``
     - BUI.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Blood Unit Type: Item #3375 | Table HL70566
   * - ``bui_4``
     - BUI.4
     - str
     - required
     - Blood Unit Weight: Item #3376
   * - ``bui_5``
     - BUI.5
     - :ref:`CNE <hl7-v2_8_2-CNE>`
     - required
     - Weight Units: Item #3377 | Table HL70929
   * - ``bui_6``
     - BUI.6
     - str
     - required
     - Blood Unit Volume: Item #3378
   * - ``bui_7``
     - BUI.7
     - :ref:`CNE <hl7-v2_8_2-CNE>`
     - required
     - Volume Units: Item #3379 | Table HL70930
   * - ``bui_8``
     - BUI.8
     - str
     - required
     - Container Catalog Number: Item #3380
   * - ``bui_9``
     - BUI.9
     - str
     - required
     - Container Lot Number: Item #3381
   * - ``bui_10``
     - BUI.10
     - :ref:`XON <hl7-v2_8_2-XON>`
     - required
     - Container Manufacturer: Item #3382
   * - ``bui_11``
     - BUI.11
     - :ref:`NR <hl7-v2_8_2-NR>`
     - required
     - Transport Temperature: Item #3383
   * - ``bui_12``
     - BUI.12
     - :ref:`CNE <hl7-v2_8_2-CNE>`
     - required
     - Transport Temperature Units: Item #3384 | Table HL70931

.. _hl7-v2_8_2-CDM:

.. py:class:: hl7types.hl7.v2_8_2.segments.CDM.CDM
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
     - Description
   * - ``cdm_1``
     - CDM.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Primary Key Value - CDM: Item #1306
   * - ``cdm_2``
     - CDM.2
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Charge Code Alias: Item #983 | Table HL70132
   * - ``cdm_3``
     - CDM.3
     - str
     - required
     - Charge Description Short: Item #984
   * - ``cdm_4``
     - CDM.4
     - Optional[str]
     - optional
     - Charge Description Long: Item #985
   * - ``cdm_5``
     - CDM.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Description Override Indicator: Item #986 | Table HL70268
   * - ``cdm_6``
     - CDM.6
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Exploding Charges: Item #987 | Table HL70132
   * - ``cdm_7``
     - CDM.7
     - Optional[List[:ref:`CNE <hl7-v2_8_2-CNE>`]]
     - optional
     - Procedure Code: Item #393 | Table HL70088
   * - ``cdm_8``
     - CDM.8
     - Optional[str]
     - optional
     - Active/Inactive Flag: Item #675 | Table HL70183
   * - ``cdm_9``
     - CDM.9
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Inventory Number: Item #990 | Table HL70463
   * - ``cdm_10``
     - CDM.10
     - Optional[str]
     - optional
     - Resource Load: Item #991
   * - ``cdm_11``
     - CDM.11
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Contract Number: Item #992
   * - ``cdm_12``
     - CDM.12
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Contract Organization: Item #993
   * - ``cdm_13``
     - CDM.13
     - Optional[str]
     - optional
     - Room Fee Indicator: Item #994 | Table HL70136

.. _hl7-v2_8_2-CDO:

.. py:class:: hl7types.hl7.v2_8_2.segments.CDO.CDO
   :noindex:

   HL7 v2 CDO segment.

CDO
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cdo_1``
     - CDO.1
     - Optional[str]
     - optional
     - Set ID - CDO: Item #3430
   * - ``cdo_2``
     - CDO.2
     - Optional[str]
     - optional
     - Action Code: Item #816 | Table HL70206
   * - ``cdo_3``
     - CDO.3
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Cumulative Dosage Limit: Item #3397
   * - ``cdo_4``
     - CDO.4
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Cumulative Dosage Limit Time Interval: Item #3398 | Table HL70924

.. _hl7-v2_8_2-CER:

.. py:class:: hl7types.hl7.v2_8_2.segments.CER.CER
   :noindex:

   HL7 v2 CER segment.

CER
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cer_1``
     - CER.1
     - str
     - required
     - Set ID - CER: Item #1856
   * - ``cer_2``
     - CER.2
     - Optional[str]
     - optional
     - Serial Number: Item #1857
   * - ``cer_3``
     - CER.3
     - Optional[str]
     - optional
     - Version: Item #1858
   * - ``cer_4``
     - CER.4
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Granting Authority: Item #1859
   * - ``cer_5``
     - CER.5
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Issuing Authority: Item #1860
   * - ``cer_6``
     - CER.6
     - Optional[:ref:`ED <hl7-v2_8_2-ED>`]
     - optional
     - Signature: Item #1861
   * - ``cer_7``
     - CER.7
     - Optional[str]
     - optional
     - Granting Country: Item #1862 | Table HL70399
   * - ``cer_8``
     - CER.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Granting State/Province: Item #1863 | Table HL70347
   * - ``cer_9``
     - CER.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Granting County/Parish: Item #1864 | Table HL70289
   * - ``cer_10``
     - CER.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Certificate Type: Item #1865
   * - ``cer_11``
     - CER.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Certificate Domain: Item #1866
   * - ``cer_12``
     - CER.12
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Subject ID: Item #1867
   * - ``cer_13``
     - CER.13
     - str
     - required
     - Subject Name: Item #1907
   * - ``cer_14``
     - CER.14
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Subject Directory Attribute Extension: Item #1868
   * - ``cer_15``
     - CER.15
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Subject Public Key Info: Item #1869
   * - ``cer_16``
     - CER.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Authority Key Identifier: Item #1870
   * - ``cer_17``
     - CER.17
     - Optional[str]
     - optional
     - Basic Constraint: Item #1871 | Table HL70136
   * - ``cer_18``
     - CER.18
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - CRL Distribution Point: Item #1872
   * - ``cer_19``
     - CER.19
     - Optional[str]
     - optional
     - Jurisdiction Country: Item #1875 | Table HL70399
   * - ``cer_20``
     - CER.20
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Jurisdiction State/Province: Item #1873 | Table HL70347
   * - ``cer_21``
     - CER.21
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Jurisdiction County/Parish: Item #1874 | Table HL70289
   * - ``cer_22``
     - CER.22
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Jurisdiction Breadth: Item #1895 | Table HL70547
   * - ``cer_23``
     - CER.23
     - Optional[str]
     - optional
     - Granting Date: Item #1876
   * - ``cer_24``
     - CER.24
     - Optional[str]
     - optional
     - Issuing Date: Item #1877
   * - ``cer_25``
     - CER.25
     - Optional[str]
     - optional
     - Activation Date: Item #1878
   * - ``cer_26``
     - CER.26
     - Optional[str]
     - optional
     - Inactivation Date: Item #1879
   * - ``cer_27``
     - CER.27
     - Optional[str]
     - optional
     - Expiration Date: Item #1880
   * - ``cer_28``
     - CER.28
     - Optional[str]
     - optional
     - Renewal Date: Item #1881
   * - ``cer_29``
     - CER.29
     - Optional[str]
     - optional
     - Revocation Date: Item #1882
   * - ``cer_30``
     - CER.30
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Revocation Reason Code: Item #1883
   * - ``cer_31``
     - CER.31
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Certificate Status Code: Item #1884 | Table HL70536

.. _hl7-v2_8_2-CM0:

.. py:class:: hl7types.hl7.v2_8_2.segments.CM0.CM0
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
     - Description
   * - ``cm0_1``
     - CM0.1
     - Optional[str]
     - optional
     - Set ID - CM0: Item #1010
   * - ``cm0_2``
     - CM0.2
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Sponsor Study ID: Item #1011
   * - ``cm0_3``
     - CM0.3
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Alternate Study ID: Item #1036
   * - ``cm0_4``
     - CM0.4
     - str
     - required
     - Title of Study: Item #1013
   * - ``cm0_5``
     - CM0.5
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Chairman of Study: Item #1014
   * - ``cm0_6``
     - CM0.6
     - Optional[str]
     - optional
     - Last IRB Approval Date: Item #1015
   * - ``cm0_7``
     - CM0.7
     - Optional[str]
     - optional
     - Total Accrual to Date: Item #1016
   * - ``cm0_8``
     - CM0.8
     - Optional[str]
     - optional
     - Last Accrual Date: Item #1017
   * - ``cm0_9``
     - CM0.9
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Contact for Study: Item #1018
   * - ``cm0_10``
     - CM0.10
     - Optional[:ref:`XTN <hl7-v2_8_2-XTN>`]
     - optional
     - Contact's Telephone Number: Item #1019
   * - ``cm0_11``
     - CM0.11
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Contact's Address: Item #1020

.. _hl7-v2_8_2-CM1:

.. py:class:: hl7types.hl7.v2_8_2.segments.CM1.CM1
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
     - Description
   * - ``cm1_1``
     - CM1.1
     - str
     - required
     - Set ID - CM1: Item #1021
   * - ``cm1_2``
     - CM1.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Study Phase Identifier: Item #1022
   * - ``cm1_3``
     - CM1.3
     - str
     - required
     - Description of Study Phase: Item #1023

.. _hl7-v2_8_2-CM2:

.. py:class:: hl7types.hl7.v2_8_2.segments.CM2.CM2
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
     - Description
   * - ``cm2_1``
     - CM2.1
     - Optional[str]
     - optional
     - Set ID- CM2: Item #1024
   * - ``cm2_2``
     - CM2.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Scheduled Time Point: Item #1025
   * - ``cm2_3``
     - CM2.3
     - Optional[str]
     - optional
     - Description of Time Point: Item #1026
   * - ``cm2_4``
     - CM2.4
     - List[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - required
     - Events Scheduled This Time Point: Item #1027

.. _hl7-v2_8_2-CNS:

.. py:class:: hl7types.hl7.v2_8_2.segments.CNS.CNS
   :noindex:

   HL7 v2 CNS segment.

CNS
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cns_1``
     - CNS.1
     - Optional[str]
     - optional
     - Starting Notification Reference Number: Item #1402
   * - ``cns_2``
     - CNS.2
     - Optional[str]
     - optional
     - Ending Notification Reference Number: Item #1403
   * - ``cns_3``
     - CNS.3
     - Optional[str]
     - optional
     - Starting Notification Date/Time: Item #1404
   * - ``cns_4``
     - CNS.4
     - Optional[str]
     - optional
     - Ending Notification Date/Time: Item #1405
   * - ``cns_5``
     - CNS.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Starting Notification Code: Item #1406 | Table HL79999
   * - ``cns_6``
     - CNS.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Ending Notification Code: Item #1407 | Table HL79999

.. _hl7-v2_8_2-CON:

.. py:class:: hl7types.hl7.v2_8_2.segments.CON.CON
   :noindex:

   HL7 v2 CON segment.

CON
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``con_1``
     - CON.1
     - str
     - required
     - Set ID - CON: Item #1776
   * - ``con_2``
     - CON.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Consent Type: Item #1777 | Table HL70496
   * - ``con_3``
     - CON.3
     - Optional[str]
     - optional
     - Consent Form ID and Version: Item #1778
   * - ``con_4``
     - CON.4
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Consent Form Number: Item #1779
   * - ``con_5``
     - CON.5
     - Optional[List[:ref:`FT <hl7-v2_8_2-FT>`]]
     - optional
     - Consent Text: Item #1780
   * - ``con_6``
     - CON.6
     - Optional[List[:ref:`FT <hl7-v2_8_2-FT>`]]
     - optional
     - Subject-specific Consent Text: Item #1781
   * - ``con_7``
     - CON.7
     - Optional[List[:ref:`FT <hl7-v2_8_2-FT>`]]
     - optional
     - Consent Background Information: Item #1782
   * - ``con_8``
     - CON.8
     - Optional[List[:ref:`FT <hl7-v2_8_2-FT>`]]
     - optional
     - Subject-specific Consent Background Text: Item #1783
   * - ``con_9``
     - CON.9
     - Optional[List[:ref:`FT <hl7-v2_8_2-FT>`]]
     - optional
     - Consenter-imposed limitations: Item #1784
   * - ``con_10``
     - CON.10
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Consent Mode: Item #1785 | Table HL70497
   * - ``con_11``
     - CON.11
     - :ref:`CNE <hl7-v2_8_2-CNE>`
     - required
     - Consent Status: Item #1786 | Table HL70498
   * - ``con_12``
     - CON.12
     - Optional[str]
     - optional
     - Consent Discussion Date/Time: Item #1787
   * - ``con_13``
     - CON.13
     - Optional[str]
     - optional
     - Consent Decision Date/Time: Item #1788
   * - ``con_14``
     - CON.14
     - Optional[str]
     - optional
     - Consent Effective Date/Time: Item #1789
   * - ``con_15``
     - CON.15
     - Optional[str]
     - optional
     - Consent End Date/Time: Item #1790
   * - ``con_16``
     - CON.16
     - Optional[str]
     - optional
     - Subject Competence Indicator: Item #1791 | Table HL70136
   * - ``con_17``
     - CON.17
     - Optional[str]
     - optional
     - Translator Assistance Indicator: Item #1792 | Table HL70136
   * - ``con_18``
     - CON.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Language Translated To: Item #1793 | Table HL70296
   * - ``con_19``
     - CON.19
     - Optional[str]
     - optional
     - Informational Material Supplied Indicator: Item #1794 | Table HL70136
   * - ``con_20``
     - CON.20
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Consent Bypass Reason: Item #1795 | Table HL70499
   * - ``con_21``
     - CON.21
     - Optional[str]
     - optional
     - Consent Disclosure Level: Item #1796 | Table HL70500
   * - ``con_22``
     - CON.22
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Consent Non-disclosure Reason: Item #1797 | Table HL70501
   * - ``con_23``
     - CON.23
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Non-subject Consenter Reason: Item #1798 | Table HL70502
   * - ``con_24``
     - CON.24
     - List[:ref:`XPN <hl7-v2_8_2-XPN>`]
     - required
     - Consenter ID: Item #1909
   * - ``con_25``
     - CON.25
     - List[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - required
     - Relationship to Subject: Item #1898 | Table HL70548

.. _hl7-v2_8_2-CSP:

.. py:class:: hl7types.hl7.v2_8_2.segments.CSP.CSP
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
     - Description
   * - ``csp_1``
     - CSP.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Study Phase Identifier: Item #1022
   * - ``csp_2``
     - CSP.2
     - str
     - required
     - Date/time Study Phase Began: Item #1052
   * - ``csp_3``
     - CSP.3
     - Optional[str]
     - optional
     - Date/time Study Phase Ended: Item #1053
   * - ``csp_4``
     - CSP.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Study Phase Evaluability: Item #1054 | Table HL79999

.. _hl7-v2_8_2-CSR:

.. py:class:: hl7types.hl7.v2_8_2.segments.CSR.CSR
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
     - Description
   * - ``csr_1``
     - CSR.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Sponsor Study ID: Item #1011
   * - ``csr_2``
     - CSR.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Alternate Study ID: Item #1036
   * - ``csr_3``
     - CSR.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Institution Registering the Patient: Item #1037 | Table HL79999
   * - ``csr_4``
     - CSR.4
     - :ref:`CX <hl7-v2_8_2-CX>`
     - required
     - Sponsor Patient ID: Item #1038
   * - ``csr_5``
     - CSR.5
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Alternate Patient ID - CSR: Item #1039
   * - ``csr_6``
     - CSR.6
     - str
     - required
     - Date/Time of Patient Study Registration: Item #1040
   * - ``csr_7``
     - CSR.7
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Person Performing Study Registration: Item #1041
   * - ``csr_8``
     - CSR.8
     - List[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - required
     - Study Authorizing Provider: Item #1042
   * - ``csr_9``
     - CSR.9
     - Optional[str]
     - optional
     - Date/Time Patient Study Consent Signed: Item #1043
   * - ``csr_10``
     - CSR.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Patient Study Eligibility Status: Item #1044 | Table HL79999
   * - ``csr_11``
     - CSR.11
     - Optional[List[str]]
     - optional
     - Study Randomization Date/time: Item #1045
   * - ``csr_12``
     - CSR.12
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Randomized Study Arm: Item #1046 | Table HL79999
   * - ``csr_13``
     - CSR.13
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Stratum for Study Randomization: Item #1047 | Table HL79999
   * - ``csr_14``
     - CSR.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Patient Evaluability Status: Item #1048 | Table HL79999
   * - ``csr_15``
     - CSR.15
     - Optional[str]
     - optional
     - Date/Time Ended Study: Item #1049
   * - ``csr_16``
     - CSR.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Reason Ended Study: Item #1050 | Table HL79999

.. _hl7-v2_8_2-CSS:

.. py:class:: hl7types.hl7.v2_8_2.segments.CSS.CSS
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
     - Description
   * - ``css_1``
     - CSS.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Study Scheduled Time Point: Item #1055 | Table HL79999
   * - ``css_2``
     - CSS.2
     - Optional[str]
     - optional
     - Study Scheduled Patient Time Point: Item #1056
   * - ``css_3``
     - CSS.3
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Study Quality Control Codes: Item #1057 | Table HL79999

.. _hl7-v2_8_2-CTD:

.. py:class:: hl7types.hl7.v2_8_2.segments.CTD.CTD
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
     - Description
   * - ``ctd_1``
     - CTD.1
     - List[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - required
     - Contact Role: Item #196 | Table HL70131
   * - ``ctd_2``
     - CTD.2
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Contact Name: Item #1165
   * - ``ctd_3``
     - CTD.3
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Contact Address: Item #1166
   * - ``ctd_4``
     - CTD.4
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Contact Location: Item #1167
   * - ``ctd_5``
     - CTD.5
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Contact Communication Information: Item #1168
   * - ``ctd_6``
     - CTD.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Preferred Method of Contact: Item #684 | Table HL70185
   * - ``ctd_7``
     - CTD.7
     - Optional[List[:ref:`PLN <hl7-v2_8_2-PLN>`]]
     - optional
     - Contact Identifiers: Item #1171 | Table HL70338

.. _hl7-v2_8_2-CTI:

.. py:class:: hl7types.hl7.v2_8_2.segments.CTI.CTI
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
     - Description
   * - ``cti_1``
     - CTI.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Sponsor Study ID: Item #1011
   * - ``cti_2``
     - CTI.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Study Phase Identifier: Item #1022
   * - ``cti_3``
     - CTI.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Study Scheduled Time Point: Item #1055 | Table HL79999

.. _hl7-v2_8_2-DB1:

.. py:class:: hl7types.hl7.v2_8_2.segments.DB1.DB1
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
     - Description
   * - ``db1_1``
     - DB1.1
     - str
     - required
     - Set ID - DB1: Item #1283
   * - ``db1_2``
     - DB1.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Disabled Person Code: Item #1284 | Table HL70334
   * - ``db1_3``
     - DB1.3
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Disabled Person Identifier: Item #1285
   * - ``db1_4``
     - DB1.4
     - Optional[str]
     - optional
     - Disability Indicator: Item #1286 | Table HL70136
   * - ``db1_5``
     - DB1.5
     - Optional[str]
     - optional
     - Disability Start Date: Item #1287
   * - ``db1_6``
     - DB1.6
     - Optional[str]
     - optional
     - Disability End Date: Item #1288
   * - ``db1_7``
     - DB1.7
     - Optional[str]
     - optional
     - Disability Return to Work Date: Item #1289
   * - ``db1_8``
     - DB1.8
     - Optional[str]
     - optional
     - Disability Unable to Work Date: Item #1290

.. _hl7-v2_8_2-DG1:

.. py:class:: hl7types.hl7.v2_8_2.segments.DG1.DG1
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
     - Description
   * - ``dg1_1``
     - DG1.1
     - str
     - required
     - Set ID - DG1: Item #375
   * - ``dg1_3``
     - DG1.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Diagnosis Code - DG1: Item #377 | Table HL70051
   * - ``dg1_5``
     - DG1.5
     - Optional[str]
     - optional
     - Diagnosis Date/Time: Item #379
   * - ``dg1_6``
     - DG1.6
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Diagnosis Type: Item #380 | Table HL70052
   * - ``dg1_15``
     - DG1.15
     - Optional[str]
     - optional
     - Diagnosis Priority: Item #389 | Table HL70359
   * - ``dg1_16``
     - DG1.16
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Diagnosing Clinician: Item #390
   * - ``dg1_17``
     - DG1.17
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Diagnosis Classification: Item #766 | Table HL70228
   * - ``dg1_18``
     - DG1.18
     - Optional[str]
     - optional
     - Confidential Indicator: Item #767 | Table HL70136
   * - ``dg1_19``
     - DG1.19
     - Optional[str]
     - optional
     - Attestation Date/Time: Item #768
   * - ``dg1_20``
     - DG1.20
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Diagnosis Identifier: Item #1850
   * - ``dg1_21``
     - DG1.21
     - Optional[str]
     - optional
     - Diagnosis Action Code: Item #1894 | Table HL70206
   * - ``dg1_22``
     - DG1.22
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Parent Diagnosis: Item #2152
   * - ``dg1_23``
     - DG1.23
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - DRG CCL Value Code: Item #2153 | Table HL70728
   * - ``dg1_24``
     - DG1.24
     - Optional[str]
     - optional
     - DRG Grouping Usage: Item #2154 | Table HL70136
   * - ``dg1_25``
     - DG1.25
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - DRG Diagnosis Determination Status: Item #2155 | Table HL70731
   * - ``dg1_26``
     - DG1.26
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Present On Admission (POA) Indicator: Item #2288 | Table HL70895

.. _hl7-v2_8_2-DMI:

.. py:class:: hl7types.hl7.v2_8_2.segments.DMI.DMI
   :noindex:

   HL7 v2 DMI segment.

DMI
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``dmi_1``
     - DMI.1
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Diagnostic Related Group: Item #382 | Table HL70055
   * - ``dmi_2``
     - DMI.2
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Major Diagnostic Category: Item #381 | Table HL70118
   * - ``dmi_3``
     - DMI.3
     - Optional[:ref:`NR <hl7-v2_8_2-NR>`]
     - optional
     - Lower and Upper Trim Points: Item #2231
   * - ``dmi_4``
     - DMI.4
     - Optional[str]
     - optional
     - Average Length of Stay: Item #2232
   * - ``dmi_5``
     - DMI.5
     - Optional[str]
     - optional
     - Relative Weight: Item #2233

.. _hl7-v2_8_2-DON:

.. py:class:: hl7types.hl7.v2_8_2.segments.DON.DON
   :noindex:

   HL7 v2 DON segment.

DON
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``don_1``
     - DON.1
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Donation Identification Number - DIN: Item #3340
   * - ``don_2``
     - DON.2
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Donation Type: Item #3341
   * - ``don_3``
     - DON.3
     - str
     - required
     - Phlebotomy Start Date/Time: Item #3342
   * - ``don_4``
     - DON.4
     - str
     - required
     - Phlebotomy End Date/Time: Item #3343
   * - ``don_5``
     - DON.5
     - str
     - required
     - Donation Duration: Item #3344
   * - ``don_6``
     - DON.6
     - :ref:`CNE <hl7-v2_8_2-CNE>`
     - required
     - Donation Duration Units: Item #3345 | Table HL70932
   * - ``don_7``
     - DON.7
     - List[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - required
     - Intended Procedure Type: Item #3346 | Table HL70933
   * - ``don_8``
     - DON.8
     - List[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - required
     - Actual Procedure Type: Item #3347 | Table HL70933
   * - ``don_9``
     - DON.9
     - str
     - required
     - Donor Eligibility Flag: Item #3348 | Table HL70136
   * - ``don_10``
     - DON.10
     - List[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - required
     - Donor Eligibility Procedure Type: Item #3349 | Table HL70933
   * - ``don_11``
     - DON.11
     - str
     - required
     - Donor Eligibility Date: Item #3350
   * - ``don_12``
     - DON.12
     - :ref:`CNE <hl7-v2_8_2-CNE>`
     - required
     - Process Interruption: Item #3351 | Table HL70923
   * - ``don_13``
     - DON.13
     - :ref:`CNE <hl7-v2_8_2-CNE>`
     - required
     - Process Interruption Reason: Item #3352 | Table HL70935
   * - ``don_14``
     - DON.14
     - List[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - required
     - Phlebotomy Issue: Item #3353 | Table HL70925
   * - ``don_15``
     - DON.15
     - str
     - required
     - Intended Recipient Blood Relative: Item #3354 | Table HL70136
   * - ``don_16``
     - DON.16
     - :ref:`XPN <hl7-v2_8_2-XPN>`
     - required
     - Intended Recipient Name: Item #3355
   * - ``don_17``
     - DON.17
     - str
     - required
     - Intended Recipient DOB: Item #3356
   * - ``don_18``
     - DON.18
     - :ref:`XON <hl7-v2_8_2-XON>`
     - required
     - Intended Recipient Facility: Item #3357
   * - ``don_19``
     - DON.19
     - str
     - required
     - Intended Recipient Procedure Date: Item #3358
   * - ``don_20``
     - DON.20
     - :ref:`XPN <hl7-v2_8_2-XPN>`
     - required
     - Intended Recipient Ordering Provider: Item #3359
   * - ``don_21``
     - DON.21
     - :ref:`CNE <hl7-v2_8_2-CNE>`
     - required
     - Phlebotomy Status: Item #3360 | Table HL70926
   * - ``don_22``
     - DON.22
     - :ref:`CNE <hl7-v2_8_2-CNE>`
     - required
     - Arm Stick: Item #3361 | Table HL70927
   * - ``don_23``
     - DON.23
     - :ref:`XPN <hl7-v2_8_2-XPN>`
     - required
     - Bleed Start Phlebotomist: Item #3362
   * - ``don_24``
     - DON.24
     - :ref:`XPN <hl7-v2_8_2-XPN>`
     - required
     - Bleed End Phlebotomist: Item #3363
   * - ``don_25``
     - DON.25
     - str
     - required
     - Aphaeresis Type Machine: Item #3364
   * - ``don_26``
     - DON.26
     - str
     - required
     - Aphaeresis Machine Serial Number: Item #3365
   * - ``don_27``
     - DON.27
     - str
     - required
     - Donor Reaction: Item #3366 | Table HL70136
   * - ``don_28``
     - DON.28
     - :ref:`XPN <hl7-v2_8_2-XPN>`
     - required
     - Final Review Staff ID: Item #3367
   * - ``don_29``
     - DON.29
     - str
     - required
     - Final Review Date/Time: Item #3368
   * - ``don_30``
     - DON.30
     - str
     - required
     - Number of Tubes Collected: Item #3369
   * - ``don_31``
     - DON.31
     - List[:ref:`EI <hl7-v2_8_2-EI>`]
     - required
     - Donation Sample Identifier: Item #3370
   * - ``don_32``
     - DON.32
     - :ref:`XCN <hl7-v2_8_2-XCN>`
     - required
     - Donation Accept Staff: Item #3371
   * - ``don_33``
     - DON.33
     - List[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - required
     - Donation Material Review Staff: Item #3372

.. _hl7-v2_8_2-DPS:

.. py:class:: hl7types.hl7.v2_8_2.segments.DPS.DPS
   :noindex:

   HL7 v2 DPS segment.

DPS
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``dps_1``
     - DPS.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Diagnosis Code - MCP: Item #3472 | Table HL70051
   * - ``dps_2``
     - DPS.2
     - List[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - required
     - Procedure Code: Item #3484 | Table HL70941
   * - ``dps_3``
     - DPS.3
     - Optional[str]
     - optional
     - Effective Date/Time: Item #662
   * - ``dps_4``
     - DPS.4
     - Optional[str]
     - optional
     - Expiration Date/Time: Item #3473
   * - ``dps_5``
     - DPS.5
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Type of Limitation: Item #3474 | Table HL70940

.. _hl7-v2_8_2-DRG:

.. py:class:: hl7types.hl7.v2_8_2.segments.DRG.DRG
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
     - Description
   * - ``drg_1``
     - DRG.1
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Diagnostic Related Group: Item #382 | Table HL70055
   * - ``drg_2``
     - DRG.2
     - Optional[str]
     - optional
     - DRG Assigned Date/Time: Item #769
   * - ``drg_3``
     - DRG.3
     - Optional[str]
     - optional
     - DRG Approval Indicator: Item #383 | Table HL70136
   * - ``drg_4``
     - DRG.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - DRG Grouper Review Code: Item #384 | Table HL70056
   * - ``drg_5``
     - DRG.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Outlier Type: Item #385 | Table HL70083
   * - ``drg_6``
     - DRG.6
     - Optional[str]
     - optional
     - Outlier Days: Item #386
   * - ``drg_7``
     - DRG.7
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Outlier Cost: Item #387
   * - ``drg_8``
     - DRG.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - DRG Payor: Item #770 | Table HL70229
   * - ``drg_9``
     - DRG.9
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Outlier Reimbursement: Item #771
   * - ``drg_10``
     - DRG.10
     - Optional[str]
     - optional
     - Confidential Indicator: Item #767 | Table HL70136
   * - ``drg_11``
     - DRG.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - DRG Transfer Type: Item #1500 | Table HL70415
   * - ``drg_12``
     - DRG.12
     - Optional[:ref:`XPN <hl7-v2_8_2-XPN>`]
     - optional
     - Name of Coder: Item #2156
   * - ``drg_13``
     - DRG.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Grouper Status: Item #2157 | Table HL70734
   * - ``drg_14``
     - DRG.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - PCCL Value Code: Item #2158 | Table HL70728
   * - ``drg_15``
     - DRG.15
     - Optional[str]
     - optional
     - Effective Weight: Item #2159
   * - ``drg_16``
     - DRG.16
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Monetary Amount: Item #2160
   * - ``drg_17``
     - DRG.17
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Status Patient: Item #2161 | Table HL70739
   * - ``drg_18``
     - DRG.18
     - Optional[str]
     - optional
     - Grouper Software Name: Item #2162
   * - ``drg_19``
     - DRG.19
     - Optional[str]
     - optional
     - Grouper Software Version: Item #2282
   * - ``drg_20``
     - DRG.20
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Status Financial Calculation: Item #2163 | Table HL70742
   * - ``drg_21``
     - DRG.21
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Relative Discount/Surcharge: Item #2164
   * - ``drg_22``
     - DRG.22
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Basic Charge: Item #2165
   * - ``drg_23``
     - DRG.23
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Total Charge: Item #2166
   * - ``drg_24``
     - DRG.24
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Discount/Surcharge: Item #2167
   * - ``drg_25``
     - DRG.25
     - Optional[str]
     - optional
     - Calculated Days: Item #2168
   * - ``drg_26``
     - DRG.26
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Status Gender: Item #2169 | Table HL70749
   * - ``drg_27``
     - DRG.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Status Age: Item #2170 | Table HL70749
   * - ``drg_28``
     - DRG.28
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Status Length of Stay: Item #2171 | Table HL70749
   * - ``drg_29``
     - DRG.29
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Status Same Day Flag: Item #2172 | Table HL70749
   * - ``drg_30``
     - DRG.30
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Status Separation Mode: Item #2173 | Table HL70749
   * - ``drg_31``
     - DRG.31
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Status Weight at Birth: Item #2174 | Table HL70755
   * - ``drg_32``
     - DRG.32
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Status Respiration Minutes: Item #2175 | Table HL70757
   * - ``drg_33``
     - DRG.33
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Status Admission: Item #2176 | Table HL70759

.. _hl7-v2_8_2-DSC:

.. py:class:: hl7types.hl7.v2_8_2.segments.DSC.DSC
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
     - Description
   * - ``dsc_1``
     - DSC.1
     - Optional[str]
     - optional
     - Continuation Pointer: Item #14
   * - ``dsc_2``
     - DSC.2
     - Optional[str]
     - optional
     - Continuation Style: Item #1354 | Table HL70398

.. _hl7-v2_8_2-DSP:

.. py:class:: hl7types.hl7.v2_8_2.segments.DSP.DSP
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
     - Description
   * - ``dsp_1``
     - DSP.1
     - Optional[str]
     - optional
     - Set ID - DSP: Item #61
   * - ``dsp_2``
     - DSP.2
     - Optional[str]
     - optional
     - Display Level: Item #62
   * - ``dsp_3``
     - DSP.3
     - :ref:`TX <hl7-v2_8_2-TX>`
     - required
     - Data Line: Item #63
   * - ``dsp_4``
     - DSP.4
     - Optional[str]
     - optional
     - Logical Break Point: Item #64
   * - ``dsp_5``
     - DSP.5
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Result ID: Item #65

.. _hl7-v2_8_2-ECD:

.. py:class:: hl7types.hl7.v2_8_2.segments.ECD.ECD
   :noindex:

   HL7 v2 ECD segment.

ECD
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ecd_1``
     - ECD.1
     - str
     - required
     - Reference Command Number: Item #1390
   * - ``ecd_2``
     - ECD.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Remote Control Command: Item #1391 | Table HL70368
   * - ``ecd_3``
     - ECD.3
     - Optional[str]
     - optional
     - Response Required: Item #1392 | Table HL70136
   * - ``ecd_5``
     - ECD.5
     - Optional[List[:ref:`TX <hl7-v2_8_2-TX>`]]
     - optional
     - Parameters: Item #1394

.. _hl7-v2_8_2-ECR:

.. py:class:: hl7types.hl7.v2_8_2.segments.ECR.ECR
   :noindex:

   HL7 v2 ECR segment.

ECR
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ecr_1``
     - ECR.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Command Response: Item #1395 | Table HL70387
   * - ``ecr_2``
     - ECR.2
     - str
     - required
     - Date/Time Completed: Item #1396
   * - ``ecr_3``
     - ECR.3
     - Optional[List[:ref:`TX <hl7-v2_8_2-TX>`]]
     - optional
     - Command Response Parameters: Item #1397

.. _hl7-v2_8_2-EDU:

.. py:class:: hl7types.hl7.v2_8_2.segments.EDU.EDU
   :noindex:

   HL7 v2 EDU segment.

EDU
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``edu_1``
     - EDU.1
     - str
     - required
     - Set ID - EDU: Item #1448
   * - ``edu_2``
     - EDU.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Academic Degree: Item #1449 | Table HL70360
   * - ``edu_3``
     - EDU.3
     - Optional[:ref:`DR <hl7-v2_8_2-DR>`]
     - optional
     - Academic Degree Program Date Range: Item #1597
   * - ``edu_4``
     - EDU.4
     - Optional[:ref:`DR <hl7-v2_8_2-DR>`]
     - optional
     - Academic Degree Program Participation Date Range: Item #1450
   * - ``edu_5``
     - EDU.5
     - Optional[str]
     - optional
     - Academic Degree Granted Date: Item #1451
   * - ``edu_6``
     - EDU.6
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - School: Item #1452
   * - ``edu_7``
     - EDU.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - School Type Code: Item #1453 | Table HL70402
   * - ``edu_8``
     - EDU.8
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - School Address: Item #1454
   * - ``edu_9``
     - EDU.9
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Major Field of Study: Item #1885

.. _hl7-v2_8_2-EQP:

.. py:class:: hl7types.hl7.v2_8_2.segments.EQP.EQP
   :noindex:

   HL7 v2 EQP segment.

EQP
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``eqp_1``
     - EQP.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Event type: Item #1430 | Table HL70450
   * - ``eqp_2``
     - EQP.2
     - Optional[str]
     - optional
     - File Name: Item #1431
   * - ``eqp_3``
     - EQP.3
     - str
     - required
     - Start Date/Time: Item #1202
   * - ``eqp_4``
     - EQP.4
     - Optional[str]
     - optional
     - End Date/Time: Item #1432
   * - ``eqp_5``
     - EQP.5
     - :ref:`FT <hl7-v2_8_2-FT>`
     - required
     - Transaction Data: Item #1433

.. _hl7-v2_8_2-EQU:

.. py:class:: hl7types.hl7.v2_8_2.segments.EQU.EQU
   :noindex:

   HL7 v2 EQU segment.

EQU
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``equ_1``
     - EQU.1
     - List[:ref:`EI <hl7-v2_8_2-EI>`]
     - required
     - Equipment Instance Identifier: Item #1479
   * - ``equ_2``
     - EQU.2
     - str
     - required
     - Event Date/Time: Item #1322
   * - ``equ_3``
     - EQU.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Equipment State: Item #1323 | Table HL70365
   * - ``equ_4``
     - EQU.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Local/Remote Control State: Item #1324 | Table HL70366
   * - ``equ_5``
     - EQU.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Alert Level: Item #1325 | Table HL70367

.. _hl7-v2_8_2-ERR:

.. py:class:: hl7types.hl7.v2_8_2.segments.ERR.ERR
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
     - Description
   * - ``err_2``
     - ERR.2
     - Optional[List[:ref:`ERL <hl7-v2_8_2-ERL>`]]
     - optional
     - Error Location: Item #1812
   * - ``err_3``
     - ERR.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - HL7 Error Code: Item #1813 | Table HL70357
   * - ``err_4``
     - ERR.4
     - str
     - required
     - Severity: Item #1814 | Table HL70516
   * - ``err_5``
     - ERR.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Application Error Code: Item #1815 | Table HL70533
   * - ``err_6``
     - ERR.6
     - Optional[List[str]]
     - optional
     - Application Error Parameter: Item #1816
   * - ``err_7``
     - ERR.7
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Diagnostic Information: Item #1817
   * - ``err_8``
     - ERR.8
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - User Message: Item #1818
   * - ``err_9``
     - ERR.9
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Inform Person Indicator: Item #1819 | Table HL70517
   * - ``err_10``
     - ERR.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Override Type: Item #1820 | Table HL70518
   * - ``err_11``
     - ERR.11
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Override Reason Code: Item #1821 | Table HL70519
   * - ``err_12``
     - ERR.12
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Help Desk Contact Point: Item #1822

.. _hl7-v2_8_2-EVN:

.. py:class:: hl7types.hl7.v2_8_2.segments.EVN.EVN
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
     - Description
   * - ``evn_2``
     - EVN.2
     - str
     - required
     - Recorded Date/Time: Item #100
   * - ``evn_3``
     - EVN.3
     - Optional[str]
     - optional
     - Date/Time Planned Event: Item #101
   * - ``evn_4``
     - EVN.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Event Reason Code: Item #102 | Table HL70062
   * - ``evn_5``
     - EVN.5
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Operator ID: Item #103 | Table HL70188
   * - ``evn_6``
     - EVN.6
     - Optional[str]
     - optional
     - Event Occurred: Item #1278
   * - ``evn_7``
     - EVN.7
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Event Facility: Item #1534

.. _hl7-v2_8_2-FAC:

.. py:class:: hl7types.hl7.v2_8_2.segments.FAC.FAC
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
     - Description
   * - ``fac_1``
     - FAC.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Facility ID-FAC: Item #1262
   * - ``fac_2``
     - FAC.2
     - Optional[str]
     - optional
     - Facility Type: Item #1263 | Table HL70331
   * - ``fac_3``
     - FAC.3
     - List[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - required
     - Facility Address: Item #1264
   * - ``fac_4``
     - FAC.4
     - :ref:`XTN <hl7-v2_8_2-XTN>`
     - required
     - Facility Telecommunication: Item #1265
   * - ``fac_5``
     - FAC.5
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Contact Person: Item #1266
   * - ``fac_6``
     - FAC.6
     - Optional[List[str]]
     - optional
     - Contact Title: Item #1267
   * - ``fac_7``
     - FAC.7
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Contact Address: Item #1166
   * - ``fac_8``
     - FAC.8
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Contact Telecommunication: Item #1269
   * - ``fac_9``
     - FAC.9
     - List[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - required
     - Signature Authority: Item #1270
   * - ``fac_10``
     - FAC.10
     - Optional[str]
     - optional
     - Signature Authority Title: Item #1271
   * - ``fac_11``
     - FAC.11
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Signature Authority Address: Item #1272
   * - ``fac_12``
     - FAC.12
     - Optional[:ref:`XTN <hl7-v2_8_2-XTN>`]
     - optional
     - Signature Authority Telecommunication: Item #1273

.. _hl7-v2_8_2-FHS:

.. py:class:: hl7types.hl7.v2_8_2.segments.FHS.FHS
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
     - Description
   * - ``fhs_1``
     - FHS.1
     - str
     - optional
     - File Field Separator: Item #67
   * - ``fhs_2``
     - FHS.2
     - str
     - optional
     - File Encoding Characters: Item #68
   * - ``fhs_3``
     - FHS.3
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - File Sending Application: Item #69
   * - ``fhs_4``
     - FHS.4
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - File Sending Facility: Item #70
   * - ``fhs_5``
     - FHS.5
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - File Receiving Application: Item #71
   * - ``fhs_6``
     - FHS.6
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - File Receiving Facility: Item #72
   * - ``fhs_7``
     - FHS.7
     - Optional[str]
     - optional
     - File Creation Date/Time: Item #73
   * - ``fhs_8``
     - FHS.8
     - Optional[str]
     - optional
     - File Security: Item #74
   * - ``fhs_9``
     - FHS.9
     - Optional[str]
     - optional
     - File Name/ID: Item #75
   * - ``fhs_10``
     - FHS.10
     - Optional[str]
     - optional
     - File Header Comment: Item #76
   * - ``fhs_11``
     - FHS.11
     - Optional[str]
     - optional
     - File Control ID: Item #77
   * - ``fhs_12``
     - FHS.12
     - Optional[str]
     - optional
     - Reference File Control ID: Item #78
   * - ``fhs_13``
     - FHS.13
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - File Sending Network Address: Item #2269
   * - ``fhs_14``
     - FHS.14
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - File Receiving Network Address: Item #2270

.. _hl7-v2_8_2-FT1:

.. py:class:: hl7types.hl7.v2_8_2.segments.FT1.FT1
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
     - Description
   * - ``ft1_1``
     - FT1.1
     - Optional[str]
     - optional
     - Set ID - FT1: Item #355
   * - ``ft1_2``
     - FT1.2
     - Optional[str]
     - optional
     - Transaction ID: Item #356
   * - ``ft1_3``
     - FT1.3
     - Optional[str]
     - optional
     - Transaction Batch ID: Item #357
   * - ``ft1_4``
     - FT1.4
     - :ref:`DR <hl7-v2_8_2-DR>`
     - required
     - Transaction Date: Item #358
   * - ``ft1_5``
     - FT1.5
     - Optional[str]
     - optional
     - Transaction Posting Date: Item #359
   * - ``ft1_6``
     - FT1.6
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Transaction Type: Item #360 | Table HL70017
   * - ``ft1_7``
     - FT1.7
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Transaction Code: Item #361 | Table HL70132
   * - ``ft1_10``
     - FT1.10
     - Optional[str]
     - optional
     - Transaction Quantity: Item #364
   * - ``ft1_11``
     - FT1.11
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Transaction Amount - Extended: Item #365
   * - ``ft1_12``
     - FT1.12
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Transaction amount - unit: Item #366
   * - ``ft1_13``
     - FT1.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Department Code: Item #367 | Table HL70049
   * - ``ft1_14``
     - FT1.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Health Plan ID: Item #368 | Table HL70072
   * - ``ft1_15``
     - FT1.15
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Insurance Amount: Item #369
   * - ``ft1_16``
     - FT1.16
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Assigned Patient Location: Item #133
   * - ``ft1_17``
     - FT1.17
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Fee Schedule: Item #370 | Table HL70024
   * - ``ft1_18``
     - FT1.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Patient Type: Item #148 | Table HL70018
   * - ``ft1_19``
     - FT1.19
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Diagnosis Code - FT1: Item #371 | Table HL70051
   * - ``ft1_20``
     - FT1.20
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Performed By Code: Item #372 | Table HL70084
   * - ``ft1_21``
     - FT1.21
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Ordered By Code: Item #373
   * - ``ft1_22``
     - FT1.22
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Unit Cost: Item #374
   * - ``ft1_23``
     - FT1.23
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Filler Order Number: Item #217
   * - ``ft1_24``
     - FT1.24
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Entered By Code: Item #765
   * - ``ft1_25``
     - FT1.25
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Procedure Code: Item #393 | Table HL70088
   * - ``ft1_26``
     - FT1.26
     - Optional[List[:ref:`CNE <hl7-v2_8_2-CNE>`]]
     - optional
     - Procedure Code Modifier: Item #1316 | Table HL70340
   * - ``ft1_27``
     - FT1.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Advanced Beneficiary Notice Code: Item #1310 | Table HL70339
   * - ``ft1_28``
     - FT1.28
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Medically Necessary Duplicate Procedure Reason: Item #1646 | Table HL70476
   * - ``ft1_29``
     - FT1.29
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - NDC Code: Item #1845 | Table HL70549
   * - ``ft1_30``
     - FT1.30
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Payment Reference ID: Item #1846
   * - ``ft1_31``
     - FT1.31
     - Optional[List[str]]
     - optional
     - Transaction Reference Key: Item #1847
   * - ``ft1_32``
     - FT1.32
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Performing Facility: Item #2361
   * - ``ft1_33``
     - FT1.33
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Ordering Facility: Item #2362
   * - ``ft1_34``
     - FT1.34
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Item Number: Item #2363
   * - ``ft1_35``
     - FT1.35
     - Optional[str]
     - optional
     - Model Number: Item #2364
   * - ``ft1_36``
     - FT1.36
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Special Processing Code: Item #2365
   * - ``ft1_37``
     - FT1.37
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Clinic Code: Item #2366
   * - ``ft1_38``
     - FT1.38
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Referral Number: Item #2367
   * - ``ft1_39``
     - FT1.39
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Authorization Number: Item #2368
   * - ``ft1_40``
     - FT1.40
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Service Provider Taxonomy Code: Item #2369
   * - ``ft1_41``
     - FT1.41
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Revenue Code: Item #1600 | Table HL70456
   * - ``ft1_42``
     - FT1.42
     - Optional[str]
     - optional
     - Prescription Number: Item #325
   * - ``ft1_43``
     - FT1.43
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - NDC Qty and UOM: Item #2370

.. _hl7-v2_8_2-FTS:

.. py:class:: hl7types.hl7.v2_8_2.segments.FTS.FTS
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
     - Description
   * - ``fts_1``
     - FTS.1
     - Optional[str]
     - optional
     - File Batch Count: Item #79
   * - ``fts_2``
     - FTS.2
     - Optional[str]
     - optional
     - File Trailer Comment: Item #80

.. _hl7-v2_8_2-GOL:

.. py:class:: hl7types.hl7.v2_8_2.segments.GOL.GOL
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
     - Description
   * - ``gol_1``
     - GOL.1
     - str
     - required
     - Action Code: Item #816 | Table HL70206
   * - ``gol_2``
     - GOL.2
     - str
     - required
     - Action Date/Time: Item #817
   * - ``gol_3``
     - GOL.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Goal ID: Item #818
   * - ``gol_4``
     - GOL.4
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Goal Instance ID: Item #819
   * - ``gol_5``
     - GOL.5
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Episode of Care ID: Item #820
   * - ``gol_6``
     - GOL.6
     - Optional[str]
     - optional
     - Goal List Priority: Item #821
   * - ``gol_7``
     - GOL.7
     - Optional[str]
     - optional
     - Goal Established Date/Time: Item #822
   * - ``gol_8``
     - GOL.8
     - Optional[str]
     - optional
     - Expected Goal Achieve Date/Time: Item #824
   * - ``gol_9``
     - GOL.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Goal Classification: Item #825
   * - ``gol_10``
     - GOL.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Goal Management Discipline: Item #826
   * - ``gol_11``
     - GOL.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Current Goal Review Status: Item #827
   * - ``gol_12``
     - GOL.12
     - Optional[str]
     - optional
     - Current Goal Review Date/Time: Item #828
   * - ``gol_13``
     - GOL.13
     - Optional[str]
     - optional
     - Next Goal Review Date/Time: Item #829
   * - ``gol_14``
     - GOL.14
     - Optional[str]
     - optional
     - Previous Goal Review Date/Time: Item #830
   * - ``gol_16``
     - GOL.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Goal Evaluation: Item #832
   * - ``gol_17``
     - GOL.17
     - Optional[List[str]]
     - optional
     - Goal Evaluation Comment: Item #833
   * - ``gol_18``
     - GOL.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Goal Life Cycle Status: Item #834
   * - ``gol_19``
     - GOL.19
     - Optional[str]
     - optional
     - Goal Life Cycle Status Date/Time: Item #835
   * - ``gol_20``
     - GOL.20
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Goal Target Type: Item #836
   * - ``gol_21``
     - GOL.21
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Goal Target Name: Item #837
   * - ``gol_22``
     - GOL.22
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Mood Code: Item #2182 | Table HL70725

.. _hl7-v2_8_2-GP1:

.. py:class:: hl7types.hl7.v2_8_2.segments.GP1.GP1
   :noindex:

   HL7 v2 GP1 segment.

GP1
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``gp1_1``
     - GP1.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Type of Bill Code: Item #1599 | Table HL70455
   * - ``gp1_2``
     - GP1.2
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Revenue Code: Item #1600 | Table HL70456
   * - ``gp1_3``
     - GP1.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Overall Claim Disposition Code: Item #1601 | Table HL70457
   * - ``gp1_4``
     - GP1.4
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - OCE Edits per Visit Code: Item #1602 | Table HL70458
   * - ``gp1_5``
     - GP1.5
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Outlier Cost: Item #387

.. _hl7-v2_8_2-GP2:

.. py:class:: hl7types.hl7.v2_8_2.segments.GP2.GP2
   :noindex:

   HL7 v2 GP2 segment.

GP2
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``gp2_1``
     - GP2.1
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Revenue Code: Item #1600 | Table HL70456
   * - ``gp2_2``
     - GP2.2
     - Optional[str]
     - optional
     - Number of Service Units: Item #1604
   * - ``gp2_3``
     - GP2.3
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Charge: Item #1605
   * - ``gp2_4``
     - GP2.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Reimbursement Action Code: Item #1606 | Table HL70459
   * - ``gp2_5``
     - GP2.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Denial or Rejection Code: Item #1607 | Table HL70460
   * - ``gp2_6``
     - GP2.6
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - OCE Edit Code: Item #1608 | Table HL70458
   * - ``gp2_7``
     - GP2.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Ambulatory Payment Classification Code: Item #1609 | Table HL70466
   * - ``gp2_8``
     - GP2.8
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Modifier Edit Code: Item #1610 | Table HL70467
   * - ``gp2_9``
     - GP2.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Payment Adjustment Code: Item #1611 | Table HL70468
   * - ``gp2_10``
     - GP2.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Packaging Status Code: Item #1617 | Table HL70469
   * - ``gp2_11``
     - GP2.11
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Expected CMS Payment Amount: Item #1618
   * - ``gp2_12``
     - GP2.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Reimbursement Type Code: Item #1619 | Table HL70470
   * - ``gp2_13``
     - GP2.13
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Co-Pay Amount: Item #1620
   * - ``gp2_14``
     - GP2.14
     - Optional[str]
     - optional
     - Pay Rate per Service Unit: Item #1621

.. _hl7-v2_8_2-GT1:

.. py:class:: hl7types.hl7.v2_8_2.segments.GT1.GT1
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
     - Description
   * - ``gt1_1``
     - GT1.1
     - str
     - required
     - Set ID - GT1: Item #405
   * - ``gt1_2``
     - GT1.2
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Guarantor Number: Item #406
   * - ``gt1_3``
     - GT1.3
     - List[:ref:`XPN <hl7-v2_8_2-XPN>`]
     - required
     - Guarantor Name: Item #407
   * - ``gt1_4``
     - GT1.4
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Guarantor Spouse Name: Item #408
   * - ``gt1_5``
     - GT1.5
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Guarantor Address: Item #409
   * - ``gt1_6``
     - GT1.6
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Guarantor Ph Num - Home: Item #410
   * - ``gt1_7``
     - GT1.7
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Guarantor Ph Num - Business: Item #411
   * - ``gt1_8``
     - GT1.8
     - Optional[str]
     - optional
     - Guarantor Date/Time Of Birth: Item #412
   * - ``gt1_9``
     - GT1.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Guarantor Administrative Sex: Item #413 | Table HL70001
   * - ``gt1_10``
     - GT1.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Guarantor Type: Item #414 | Table HL70068
   * - ``gt1_11``
     - GT1.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Guarantor Relationship: Item #415 | Table HL70063
   * - ``gt1_12``
     - GT1.12
     - Optional[str]
     - optional
     - Guarantor SSN: Item #416
   * - ``gt1_13``
     - GT1.13
     - Optional[str]
     - optional
     - Guarantor Date - Begin: Item #417
   * - ``gt1_14``
     - GT1.14
     - Optional[str]
     - optional
     - Guarantor Date - End: Item #418
   * - ``gt1_15``
     - GT1.15
     - Optional[str]
     - optional
     - Guarantor Priority: Item #419
   * - ``gt1_16``
     - GT1.16
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Guarantor Employer Name: Item #420
   * - ``gt1_17``
     - GT1.17
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Guarantor Employer Address: Item #421
   * - ``gt1_18``
     - GT1.18
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Guarantor Employer Phone Number: Item #422
   * - ``gt1_19``
     - GT1.19
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Guarantor Employee ID Number: Item #423
   * - ``gt1_20``
     - GT1.20
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Guarantor Employment Status: Item #424 | Table HL70066
   * - ``gt1_21``
     - GT1.21
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Guarantor Organization Name: Item #425
   * - ``gt1_22``
     - GT1.22
     - Optional[str]
     - optional
     - Guarantor Billing Hold Flag: Item #773 | Table HL70136
   * - ``gt1_23``
     - GT1.23
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Guarantor Credit Rating Code: Item #774 | Table HL70341
   * - ``gt1_24``
     - GT1.24
     - Optional[str]
     - optional
     - Guarantor Death Date And Time: Item #775
   * - ``gt1_25``
     - GT1.25
     - Optional[str]
     - optional
     - Guarantor Death Flag: Item #776 | Table HL70136
   * - ``gt1_26``
     - GT1.26
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Guarantor Charge Adjustment Code: Item #777 | Table HL70218
   * - ``gt1_27``
     - GT1.27
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Guarantor Household Annual Income: Item #778
   * - ``gt1_28``
     - GT1.28
     - Optional[str]
     - optional
     - Guarantor Household Size: Item #779
   * - ``gt1_29``
     - GT1.29
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Guarantor Employer ID Number: Item #780
   * - ``gt1_30``
     - GT1.30
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Guarantor Marital Status Code: Item #781 | Table HL70002
   * - ``gt1_31``
     - GT1.31
     - Optional[str]
     - optional
     - Guarantor Hire Effective Date: Item #782
   * - ``gt1_32``
     - GT1.32
     - Optional[str]
     - optional
     - Employment Stop Date: Item #783
   * - ``gt1_33``
     - GT1.33
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Living Dependency: Item #755 | Table HL70223
   * - ``gt1_34``
     - GT1.34
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Ambulatory Status: Item #145 | Table HL70009
   * - ``gt1_35``
     - GT1.35
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Citizenship: Item #129 | Table HL70171
   * - ``gt1_36``
     - GT1.36
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Primary Language: Item #118 | Table HL70296
   * - ``gt1_37``
     - GT1.37
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Living Arrangement: Item #742 | Table HL70220
   * - ``gt1_38``
     - GT1.38
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Publicity Code: Item #743 | Table HL70215
   * - ``gt1_39``
     - GT1.39
     - Optional[str]
     - optional
     - Protection Indicator: Item #744 | Table HL70136
   * - ``gt1_40``
     - GT1.40
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Student Indicator: Item #745 | Table HL70231
   * - ``gt1_41``
     - GT1.41
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Religion: Item #120 | Table HL70006
   * - ``gt1_42``
     - GT1.42
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Mother's Maiden Name: Item #109
   * - ``gt1_43``
     - GT1.43
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Nationality: Item #739 | Table HL70212
   * - ``gt1_44``
     - GT1.44
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Ethnic Group: Item #125 | Table HL70189
   * - ``gt1_45``
     - GT1.45
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Contact Person's Name: Item #748
   * - ``gt1_46``
     - GT1.46
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Contact Person's Telephone Number: Item #749
   * - ``gt1_47``
     - GT1.47
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Contact Reason: Item #747 | Table HL70222
   * - ``gt1_48``
     - GT1.48
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Contact Relationship: Item #784 | Table HL70063
   * - ``gt1_49``
     - GT1.49
     - Optional[str]
     - optional
     - Job Title: Item #785
   * - ``gt1_50``
     - GT1.50
     - Optional[:ref:`JCC <hl7-v2_8_2-JCC>`]
     - optional
     - Job Code/Class: Item #786
   * - ``gt1_51``
     - GT1.51
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Guarantor Employer's Organization Name: Item #1299
   * - ``gt1_52``
     - GT1.52
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Handicap: Item #753 | Table HL70295
   * - ``gt1_53``
     - GT1.53
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Job Status: Item #752 | Table HL70311
   * - ``gt1_54``
     - GT1.54
     - Optional[:ref:`FC <hl7-v2_8_2-FC>`]
     - optional
     - Guarantor Financial Class: Item #1231
   * - ``gt1_55``
     - GT1.55
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Guarantor Race: Item #1291 | Table HL70005
   * - ``gt1_56``
     - GT1.56
     - Optional[str]
     - optional
     - Guarantor Birth Place: Item #1851
   * - ``gt1_57``
     - GT1.57
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - VIP Indicator: Item #146 | Table HL70099

.. _hl7-v2_8_2-IAM:

.. py:class:: hl7types.hl7.v2_8_2.segments.IAM.IAM
   :noindex:

   HL7 v2 IAM segment.

IAM
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``iam_1``
     - IAM.1
     - str
     - required
     - Set ID - IAM: Item #1612
   * - ``iam_2``
     - IAM.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Allergen Type Code: Item #204 | Table HL70127
   * - ``iam_3``
     - IAM.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Allergen Code/Mnemonic/Description: Item #205
   * - ``iam_4``
     - IAM.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Allergy Severity Code: Item #206 | Table HL70128
   * - ``iam_5``
     - IAM.5
     - Optional[List[str]]
     - optional
     - Allergy Reaction Code: Item #207
   * - ``iam_6``
     - IAM.6
     - :ref:`CNE <hl7-v2_8_2-CNE>`
     - required
     - Allergy Action Code: Item #1551 | Table HL70206
   * - ``iam_7``
     - IAM.7
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Allergy Unique Identifier: Item #1552
   * - ``iam_8``
     - IAM.8
     - Optional[str]
     - optional
     - Action Reason: Item #1553
   * - ``iam_9``
     - IAM.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Sensitivity to Causative Agent Code: Item #1554 | Table HL70436
   * - ``iam_10``
     - IAM.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Allergen Group Code/Mnemonic/Description: Item #1555
   * - ``iam_11``
     - IAM.11
     - Optional[str]
     - optional
     - Onset Date: Item #1556
   * - ``iam_12``
     - IAM.12
     - Optional[str]
     - optional
     - Onset Date Text: Item #1557
   * - ``iam_13``
     - IAM.13
     - Optional[str]
     - optional
     - Reported Date/Time: Item #1558
   * - ``iam_14``
     - IAM.14
     - Optional[:ref:`XPN <hl7-v2_8_2-XPN>`]
     - optional
     - Reported By: Item #1559
   * - ``iam_15``
     - IAM.15
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Relationship to Patient Code: Item #1560 | Table HL70063
   * - ``iam_16``
     - IAM.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Alert Device Code: Item #1561 | Table HL70437
   * - ``iam_17``
     - IAM.17
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Allergy Clinical Status Code: Item #1562 | Table HL70438
   * - ``iam_18``
     - IAM.18
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Statused by Person: Item #1563
   * - ``iam_19``
     - IAM.19
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Statused by Organization: Item #1564
   * - ``iam_20``
     - IAM.20
     - Optional[str]
     - optional
     - Statused at Date/Time: Item #1565
   * - ``iam_21``
     - IAM.21
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Inactivated by Person: Item #2294
   * - ``iam_22``
     - IAM.22
     - Optional[str]
     - optional
     - Inactivated Date/Time: Item #2295
   * - ``iam_23``
     - IAM.23
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Initially Recorded by Person: Item #2296
   * - ``iam_24``
     - IAM.24
     - Optional[str]
     - optional
     - Initially Recorded Date/Time: Item #2297
   * - ``iam_25``
     - IAM.25
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Modified by Person: Item #2298
   * - ``iam_26``
     - IAM.26
     - Optional[str]
     - optional
     - Modified Date/Time: Item #2299
   * - ``iam_27``
     - IAM.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Clinician Identified Code: Item #2300
   * - ``iam_28``
     - IAM.28
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Initially Recorded by Organization: Item #3293
   * - ``iam_29``
     - IAM.29
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Modified by Organization: Item #3294
   * - ``iam_30``
     - IAM.30
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Inactivated by Organization: Item #3295

.. _hl7-v2_8_2-IAR:

.. py:class:: hl7types.hl7.v2_8_2.segments.IAR.IAR
   :noindex:

   HL7 v2 IAR segment.

IAR
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``iar_1``
     - IAR.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Allergy Reaction Code: Item #3296
   * - ``iar_2``
     - IAR.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Allergy Severity Code: Item #3297 | Table HL70128
   * - ``iar_3``
     - IAR.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Sensitivity to Causative Agent Code: Item #3298 | Table HL70436
   * - ``iar_4``
     - IAR.4
     - Optional[str]
     - optional
     - Management: Item #3299

.. _hl7-v2_8_2-IIM:

.. py:class:: hl7types.hl7.v2_8_2.segments.IIM.IIM
   :noindex:

   HL7 v2 IIM segment.

IIM
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``iim_1``
     - IIM.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Primary Key Value - IIM: Item #1897
   * - ``iim_2``
     - IIM.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Service Item Code: Item #1799
   * - ``iim_3``
     - IIM.3
     - Optional[str]
     - optional
     - Inventory Lot Number: Item #1800
   * - ``iim_4``
     - IIM.4
     - Optional[str]
     - optional
     - Inventory Expiration Date: Item #1801
   * - ``iim_5``
     - IIM.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Inventory Manufacturer Name: Item #1802
   * - ``iim_6``
     - IIM.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Inventory Location: Item #1803
   * - ``iim_7``
     - IIM.7
     - Optional[str]
     - optional
     - Inventory Received Date: Item #1804
   * - ``iim_8``
     - IIM.8
     - Optional[str]
     - optional
     - Inventory Received Quantity: Item #1805
   * - ``iim_9``
     - IIM.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Inventory Received Quantity Unit: Item #1806
   * - ``iim_10``
     - IIM.10
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Inventory Received Item Cost: Item #1807
   * - ``iim_11``
     - IIM.11
     - Optional[str]
     - optional
     - Inventory On Hand Date: Item #1808
   * - ``iim_12``
     - IIM.12
     - Optional[str]
     - optional
     - Inventory On Hand Quantity: Item #1809
   * - ``iim_13``
     - IIM.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Inventory On Hand Quantity Unit: Item #1810
   * - ``iim_14``
     - IIM.14
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Procedure Code: Item #393 | Table HL70088
   * - ``iim_15``
     - IIM.15
     - Optional[List[:ref:`CNE <hl7-v2_8_2-CNE>`]]
     - optional
     - Procedure Code Modifier: Item #1316 | Table HL70340

.. _hl7-v2_8_2-ILT:

.. py:class:: hl7types.hl7.v2_8_2.segments.ILT.ILT
   :noindex:

   HL7 v2 ILT segment.

ILT
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ilt_1``
     - ILT.1
     - str
     - required
     - Set Id - ILT: Item #2086
   * - ``ilt_2``
     - ILT.2
     - str
     - required
     - Inventory Lot Number: Item #1800
   * - ``ilt_3``
     - ILT.3
     - Optional[str]
     - optional
     - Inventory Expiration Date: Item #1801
   * - ``ilt_4``
     - ILT.4
     - Optional[str]
     - optional
     - Inventory Received Date: Item #1804
   * - ``ilt_5``
     - ILT.5
     - Optional[str]
     - optional
     - Inventory Received Quantity: Item #1805
   * - ``ilt_6``
     - ILT.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Inventory Received Quantity Unit: Item #1806
   * - ``ilt_7``
     - ILT.7
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Inventory Received Item Cost: Item #1807
   * - ``ilt_8``
     - ILT.8
     - Optional[str]
     - optional
     - Inventory On Hand Date: Item #1808
   * - ``ilt_9``
     - ILT.9
     - Optional[str]
     - optional
     - Inventory On Hand Quantity: Item #1809
   * - ``ilt_10``
     - ILT.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Inventory On Hand Quantity Unit: Item #1810

.. _hl7-v2_8_2-IN1:

.. py:class:: hl7types.hl7.v2_8_2.segments.IN1.IN1
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
     - Description
   * - ``in1_1``
     - IN1.1
     - str
     - required
     - Set ID - IN1: Item #426
   * - ``in1_2``
     - IN1.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Health Plan ID: Item #368 | Table HL70072
   * - ``in1_3``
     - IN1.3
     - List[:ref:`CX <hl7-v2_8_2-CX>`]
     - required
     - Insurance Company ID: Item #428
   * - ``in1_4``
     - IN1.4
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Insurance Company Name: Item #429
   * - ``in1_5``
     - IN1.5
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Insurance Company Address: Item #430
   * - ``in1_6``
     - IN1.6
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Insurance Co Contact Person: Item #431
   * - ``in1_7``
     - IN1.7
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Insurance Co Phone Number: Item #432
   * - ``in1_8``
     - IN1.8
     - Optional[str]
     - optional
     - Group Number: Item #433
   * - ``in1_9``
     - IN1.9
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Group Name: Item #434
   * - ``in1_10``
     - IN1.10
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Insured's Group Emp ID: Item #435
   * - ``in1_11``
     - IN1.11
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Insured's Group Emp Name: Item #436
   * - ``in1_12``
     - IN1.12
     - Optional[str]
     - optional
     - Plan Effective Date: Item #437
   * - ``in1_13``
     - IN1.13
     - Optional[str]
     - optional
     - Plan Expiration Date: Item #438
   * - ``in1_14``
     - IN1.14
     - Optional[:ref:`AUI <hl7-v2_8_2-AUI>`]
     - optional
     - Authorization Information: Item #439
   * - ``in1_15``
     - IN1.15
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Plan Type: Item #440 | Table HL70086
   * - ``in1_16``
     - IN1.16
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Name Of Insured: Item #441
   * - ``in1_17``
     - IN1.17
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Insured's Relationship To Patient: Item #442 | Table HL70063
   * - ``in1_18``
     - IN1.18
     - Optional[str]
     - optional
     - Insured's Date Of Birth: Item #443
   * - ``in1_19``
     - IN1.19
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Insured's Address: Item #444
   * - ``in1_20``
     - IN1.20
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Assignment Of Benefits: Item #445 | Table HL70135
   * - ``in1_21``
     - IN1.21
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Coordination Of Benefits: Item #446 | Table HL70173
   * - ``in1_22``
     - IN1.22
     - Optional[str]
     - optional
     - Coord Of Ben. Priority: Item #447
   * - ``in1_23``
     - IN1.23
     - Optional[str]
     - optional
     - Notice Of Admission Flag: Item #448 | Table HL70136
   * - ``in1_24``
     - IN1.24
     - Optional[str]
     - optional
     - Notice Of Admission Date: Item #449
   * - ``in1_25``
     - IN1.25
     - Optional[str]
     - optional
     - Report Of Eligibility Flag: Item #450 | Table HL70136
   * - ``in1_26``
     - IN1.26
     - Optional[str]
     - optional
     - Report Of Eligibility Date: Item #451
   * - ``in1_27``
     - IN1.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Release Information Code: Item #452 | Table HL70093
   * - ``in1_28``
     - IN1.28
     - Optional[str]
     - optional
     - Pre-Admit Cert (PAC): Item #453
   * - ``in1_29``
     - IN1.29
     - Optional[str]
     - optional
     - Verification Date/Time: Item #454
   * - ``in1_30``
     - IN1.30
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Verification By: Item #455
   * - ``in1_31``
     - IN1.31
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Type Of Agreement Code: Item #456 | Table HL70098
   * - ``in1_32``
     - IN1.32
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Billing Status: Item #457 | Table HL70022
   * - ``in1_33``
     - IN1.33
     - Optional[str]
     - optional
     - Lifetime Reserve Days: Item #458
   * - ``in1_34``
     - IN1.34
     - Optional[str]
     - optional
     - Delay Before L.R. Day: Item #459
   * - ``in1_35``
     - IN1.35
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Company Plan Code: Item #460 | Table HL70042
   * - ``in1_36``
     - IN1.36
     - Optional[str]
     - optional
     - Policy Number: Item #461
   * - ``in1_37``
     - IN1.37
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Policy Deductible: Item #462
   * - ``in1_39``
     - IN1.39
     - Optional[str]
     - optional
     - Policy Limit - Days: Item #464
   * - ``in1_42``
     - IN1.42
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Insured's Employment Status: Item #467 | Table HL70066
   * - ``in1_43``
     - IN1.43
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Insured's Administrative Sex: Item #468 | Table HL70001
   * - ``in1_44``
     - IN1.44
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Insured's Employer's Address: Item #469
   * - ``in1_45``
     - IN1.45
     - Optional[str]
     - optional
     - Verification Status: Item #470
   * - ``in1_46``
     - IN1.46
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Prior Insurance Plan ID: Item #471 | Table HL70072
   * - ``in1_47``
     - IN1.47
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Coverage Type: Item #1227 | Table HL70309
   * - ``in1_48``
     - IN1.48
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Handicap: Item #753 | Table HL70295
   * - ``in1_49``
     - IN1.49
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Insured's ID Number: Item #1230
   * - ``in1_50``
     - IN1.50
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Signature Code: Item #1854 | Table HL70535
   * - ``in1_51``
     - IN1.51
     - Optional[str]
     - optional
     - Signature Code Date: Item #1855
   * - ``in1_52``
     - IN1.52
     - Optional[str]
     - optional
     - Insured's Birth Place: Item #1899
   * - ``in1_53``
     - IN1.53
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - VIP Indicator: Item #1852 | Table HL70099
   * - ``in1_54``
     - IN1.54
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - External Health Plan Identifiers: Item #3292
   * - ``in1_55``
     - IN1.55
     - Optional[str]
     - optional
     - Insurance Action Code: Item #3335 | Table HL70206

.. _hl7-v2_8_2-IN2:

.. py:class:: hl7types.hl7.v2_8_2.segments.IN2.IN2
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
     - Description
   * - ``in2_1``
     - IN2.1
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Insured's Employee ID: Item #472
   * - ``in2_2``
     - IN2.2
     - Optional[str]
     - optional
     - Insured's Social Security Number: Item #473
   * - ``in2_3``
     - IN2.3
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Insured's Employer's Name and ID: Item #474
   * - ``in2_4``
     - IN2.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Employer Information Data: Item #475 | Table HL70139
   * - ``in2_5``
     - IN2.5
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Mail Claim Party: Item #476 | Table HL70137
   * - ``in2_6``
     - IN2.6
     - Optional[str]
     - optional
     - Medicare Health Ins Card Number: Item #477
   * - ``in2_7``
     - IN2.7
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Medicaid Case Name: Item #478
   * - ``in2_8``
     - IN2.8
     - Optional[str]
     - optional
     - Medicaid Case Number: Item #479
   * - ``in2_9``
     - IN2.9
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Military Sponsor Name: Item #480
   * - ``in2_10``
     - IN2.10
     - Optional[str]
     - optional
     - Military ID Number: Item #481
   * - ``in2_11``
     - IN2.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Dependent Of Military Recipient: Item #482 | Table HL70342
   * - ``in2_12``
     - IN2.12
     - Optional[str]
     - optional
     - Military Organization: Item #483
   * - ``in2_13``
     - IN2.13
     - Optional[str]
     - optional
     - Military Station: Item #484
   * - ``in2_14``
     - IN2.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Military Service: Item #485 | Table HL70140
   * - ``in2_15``
     - IN2.15
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Military Rank/Grade: Item #486 | Table HL70141
   * - ``in2_16``
     - IN2.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Military Status: Item #487 | Table HL70142
   * - ``in2_17``
     - IN2.17
     - Optional[str]
     - optional
     - Military Retire Date: Item #488
   * - ``in2_18``
     - IN2.18
     - Optional[str]
     - optional
     - Military Non-Avail Cert On File: Item #489 | Table HL70136
   * - ``in2_19``
     - IN2.19
     - Optional[str]
     - optional
     - Baby Coverage: Item #490 | Table HL70136
   * - ``in2_20``
     - IN2.20
     - Optional[str]
     - optional
     - Combine Baby Bill: Item #491 | Table HL70136
   * - ``in2_21``
     - IN2.21
     - Optional[str]
     - optional
     - Blood Deductible: Item #492
   * - ``in2_22``
     - IN2.22
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Special Coverage Approval Name: Item #493
   * - ``in2_23``
     - IN2.23
     - Optional[str]
     - optional
     - Special Coverage Approval Title: Item #494
   * - ``in2_24``
     - IN2.24
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Non-Covered Insurance Code: Item #495 | Table HL70143
   * - ``in2_25``
     - IN2.25
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Payor ID: Item #496
   * - ``in2_26``
     - IN2.26
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Payor Subscriber ID: Item #497
   * - ``in2_27``
     - IN2.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Eligibility Source: Item #498 | Table HL70144
   * - ``in2_28``
     - IN2.28
     - Optional[List[:ref:`RMC <hl7-v2_8_2-RMC>`]]
     - optional
     - Room Coverage Type/Amount: Item #499
   * - ``in2_29``
     - IN2.29
     - Optional[List[:ref:`PTA <hl7-v2_8_2-PTA>`]]
     - optional
     - Policy Type/Amount: Item #500
   * - ``in2_30``
     - IN2.30
     - Optional[:ref:`DDI <hl7-v2_8_2-DDI>`]
     - optional
     - Daily Deductible: Item #501
   * - ``in2_31``
     - IN2.31
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Living Dependency: Item #755 | Table HL70223
   * - ``in2_32``
     - IN2.32
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Ambulatory Status: Item #145 | Table HL70009
   * - ``in2_33``
     - IN2.33
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Citizenship: Item #129 | Table HL70171
   * - ``in2_34``
     - IN2.34
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Primary Language: Item #118 | Table HL70296
   * - ``in2_35``
     - IN2.35
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Living Arrangement: Item #742 | Table HL70220
   * - ``in2_36``
     - IN2.36
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Publicity Code: Item #743 | Table HL70215
   * - ``in2_37``
     - IN2.37
     - Optional[str]
     - optional
     - Protection Indicator: Item #744 | Table HL70136
   * - ``in2_38``
     - IN2.38
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Student Indicator: Item #745 | Table HL70231
   * - ``in2_39``
     - IN2.39
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Religion: Item #120 | Table HL70006
   * - ``in2_40``
     - IN2.40
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Mother's Maiden Name: Item #109
   * - ``in2_41``
     - IN2.41
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Nationality: Item #739 | Table HL70212
   * - ``in2_42``
     - IN2.42
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Ethnic Group: Item #125 | Table HL70189
   * - ``in2_43``
     - IN2.43
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Marital Status: Item #119 | Table HL70002
   * - ``in2_44``
     - IN2.44
     - Optional[str]
     - optional
     - Insured's Employment Start Date: Item #787
   * - ``in2_45``
     - IN2.45
     - Optional[str]
     - optional
     - Employment Stop Date: Item #783
   * - ``in2_46``
     - IN2.46
     - Optional[str]
     - optional
     - Job Title: Item #785
   * - ``in2_47``
     - IN2.47
     - Optional[:ref:`JCC <hl7-v2_8_2-JCC>`]
     - optional
     - Job Code/Class: Item #786
   * - ``in2_48``
     - IN2.48
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Job Status: Item #752 | Table HL70311
   * - ``in2_49``
     - IN2.49
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Employer Contact Person Name: Item #789
   * - ``in2_50``
     - IN2.50
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Employer Contact Person Phone Number: Item #790
   * - ``in2_51``
     - IN2.51
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Employer Contact Reason: Item #791 | Table HL70222
   * - ``in2_52``
     - IN2.52
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Insured's Contact Person's Name: Item #792
   * - ``in2_53``
     - IN2.53
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Insured's Contact Person Phone Number: Item #793
   * - ``in2_54``
     - IN2.54
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Insured's Contact Person Reason: Item #794 | Table HL70222
   * - ``in2_55``
     - IN2.55
     - Optional[str]
     - optional
     - Relationship to the Patient Start Date: Item #795
   * - ``in2_56``
     - IN2.56
     - Optional[List[str]]
     - optional
     - Relationship to the Patient Stop Date: Item #796
   * - ``in2_57``
     - IN2.57
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Insurance Co Contact Reason: Item #797 | Table HL70232
   * - ``in2_58``
     - IN2.58
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Insurance Co Contact Phone Number: Item #798
   * - ``in2_59``
     - IN2.59
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Policy Scope: Item #799 | Table HL70312
   * - ``in2_60``
     - IN2.60
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Policy Source: Item #800 | Table HL70313
   * - ``in2_61``
     - IN2.61
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Patient Member Number: Item #801
   * - ``in2_62``
     - IN2.62
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Guarantor's Relationship to Insured: Item #802 | Table HL70063
   * - ``in2_63``
     - IN2.63
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Insured's Phone Number - Home: Item #803
   * - ``in2_64``
     - IN2.64
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Insured's Employer Phone Number: Item #804
   * - ``in2_65``
     - IN2.65
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Military Handicapped Program: Item #805 | Table HL70343
   * - ``in2_66``
     - IN2.66
     - Optional[str]
     - optional
     - Suspend Flag: Item #806 | Table HL70136
   * - ``in2_67``
     - IN2.67
     - Optional[str]
     - optional
     - Copay Limit Flag: Item #807 | Table HL70136
   * - ``in2_68``
     - IN2.68
     - Optional[str]
     - optional
     - Stoploss Limit Flag: Item #808 | Table HL70136
   * - ``in2_69``
     - IN2.69
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Insured Organization Name and ID: Item #809
   * - ``in2_70``
     - IN2.70
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Insured Employer Organization Name and ID: Item #810
   * - ``in2_71``
     - IN2.71
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Race: Item #113 | Table HL70005
   * - ``in2_72``
     - IN2.72
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Patient's Relationship to Insured: Item #811 | Table HL70344

.. _hl7-v2_8_2-IN3:

.. py:class:: hl7types.hl7.v2_8_2.segments.IN3.IN3
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
     - Description
   * - ``in3_1``
     - IN3.1
     - str
     - required
     - Set ID - IN3: Item #502
   * - ``in3_2``
     - IN3.2
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Certification Number: Item #503
   * - ``in3_3``
     - IN3.3
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Certified By: Item #504
   * - ``in3_4``
     - IN3.4
     - Optional[str]
     - optional
     - Certification Required: Item #505 | Table HL70136
   * - ``in3_5``
     - IN3.5
     - Optional[:ref:`MOP <hl7-v2_8_2-MOP>`]
     - optional
     - Penalty: Item #506
   * - ``in3_6``
     - IN3.6
     - Optional[str]
     - optional
     - Certification Date/Time: Item #507
   * - ``in3_7``
     - IN3.7
     - Optional[str]
     - optional
     - Certification Modify Date/Time: Item #508
   * - ``in3_8``
     - IN3.8
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Operator: Item #509
   * - ``in3_9``
     - IN3.9
     - Optional[str]
     - optional
     - Certification Begin Date: Item #510
   * - ``in3_10``
     - IN3.10
     - Optional[str]
     - optional
     - Certification End Date: Item #511
   * - ``in3_11``
     - IN3.11
     - Optional[:ref:`DTN <hl7-v2_8_2-DTN>`]
     - optional
     - Days: Item #512
   * - ``in3_12``
     - IN3.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Non-Concur Code/Description: Item #513 | Table HL70233
   * - ``in3_13``
     - IN3.13
     - Optional[str]
     - optional
     - Non-Concur Effective Date/Time: Item #514
   * - ``in3_14``
     - IN3.14
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Physician Reviewer: Item #515 | Table HL70010
   * - ``in3_15``
     - IN3.15
     - Optional[str]
     - optional
     - Certification Contact: Item #516
   * - ``in3_16``
     - IN3.16
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Certification Contact Phone Number: Item #517
   * - ``in3_17``
     - IN3.17
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Appeal Reason: Item #518 | Table HL70345
   * - ``in3_18``
     - IN3.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Certification Agency: Item #519 | Table HL70346
   * - ``in3_19``
     - IN3.19
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Certification Agency Phone Number: Item #520
   * - ``in3_20``
     - IN3.20
     - Optional[List[:ref:`ICD <hl7-v2_8_2-ICD>`]]
     - optional
     - Pre-Certification Requirement: Item #521 | Table HL70136
   * - ``in3_21``
     - IN3.21
     - Optional[str]
     - optional
     - Case Manager: Item #522
   * - ``in3_22``
     - IN3.22
     - Optional[str]
     - optional
     - Second Opinion Date: Item #523
   * - ``in3_23``
     - IN3.23
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Second Opinion Status: Item #524 | Table HL70151
   * - ``in3_24``
     - IN3.24
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Second Opinion Documentation Received: Item #525 | Table HL70152
   * - ``in3_25``
     - IN3.25
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Second Opinion Physician: Item #526 | Table HL70010
   * - ``in3_26``
     - IN3.26
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Certification Type: Item #3336 | Table HL70921
   * - ``in3_27``
     - IN3.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Certification Category: Item #3337 | Table HL70922

.. _hl7-v2_8_2-INV:

.. py:class:: hl7types.hl7.v2_8_2.segments.INV.INV
   :noindex:

   HL7 v2 INV segment.

INV
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``inv_1``
     - INV.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Substance Identifier: Item #1372 | Table HL70451
   * - ``inv_2``
     - INV.2
     - List[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - required
     - Substance Status: Item #1373 | Table HL70383
   * - ``inv_3``
     - INV.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Substance Type: Item #1374 | Table HL70384
   * - ``inv_4``
     - INV.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Inventory Container Identifier: Item #1532 | Table HL79999
   * - ``inv_5``
     - INV.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Container Carrier Identifier: Item #1376 | Table HL79999
   * - ``inv_6``
     - INV.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Position on Carrier: Item #1377 | Table HL79999
   * - ``inv_7``
     - INV.7
     - Optional[str]
     - optional
     - Initial Quantity: Item #1378
   * - ``inv_8``
     - INV.8
     - Optional[str]
     - optional
     - Current Quantity: Item #1379
   * - ``inv_9``
     - INV.9
     - Optional[str]
     - optional
     - Available Quantity: Item #1380
   * - ``inv_10``
     - INV.10
     - Optional[str]
     - optional
     - Consumption Quantity: Item #1381
   * - ``inv_11``
     - INV.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Quantity Units: Item #1382 | Table HL79999
   * - ``inv_12``
     - INV.12
     - Optional[str]
     - optional
     - Expiration Date/Time: Item #1383
   * - ``inv_13``
     - INV.13
     - Optional[str]
     - optional
     - First Used Date/Time: Item #1384
   * - ``inv_15``
     - INV.15
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Test/Fluid Identifier(s): Item #1386 | Table HL79999
   * - ``inv_16``
     - INV.16
     - Optional[str]
     - optional
     - Manufacturer Lot Number: Item #1387
   * - ``inv_17``
     - INV.17
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Manufacturer Identifier: Item #286 | Table HL70385
   * - ``inv_18``
     - INV.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Supplier Identifier: Item #1389 | Table HL70386
   * - ``inv_19``
     - INV.19
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - On Board Stability Time: Item #1626
   * - ``inv_20``
     - INV.20
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Target Value: Item #1896

.. _hl7-v2_8_2-IPC:

.. py:class:: hl7types.hl7.v2_8_2.segments.IPC.IPC
   :noindex:

   HL7 v2 IPC segment.

IPC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ipc_1``
     - IPC.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Accession Identifier: Item #1330
   * - ``ipc_2``
     - IPC.2
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Requested Procedure ID: Item #1658
   * - ``ipc_3``
     - IPC.3
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Study Instance UID: Item #1659
   * - ``ipc_4``
     - IPC.4
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Scheduled Procedure Step ID: Item #1660
   * - ``ipc_5``
     - IPC.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Modality: Item #1661 | Table HL79999
   * - ``ipc_6``
     - IPC.6
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Protocol Code: Item #1662 | Table HL79999
   * - ``ipc_7``
     - IPC.7
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Scheduled Station Name: Item #1663
   * - ``ipc_8``
     - IPC.8
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Scheduled Procedure Step Location: Item #1664 | Table HL79999
   * - ``ipc_9``
     - IPC.9
     - Optional[str]
     - optional
     - Scheduled Station AE Title: Item #1665

.. _hl7-v2_8_2-IPR:

.. py:class:: hl7types.hl7.v2_8_2.segments.IPR.IPR
   :noindex:

   HL7 v2 IPR segment.

IPR
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ipr_1``
     - IPR.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - IPR Identifier: Item #2030
   * - ``ipr_2``
     - IPR.2
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Provider Cross Reference Identifier: Item #2031
   * - ``ipr_3``
     - IPR.3
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Payer Cross Reference Identifier: Item #2032
   * - ``ipr_4``
     - IPR.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - IPR Status: Item #2033 | Table HL70571
   * - ``ipr_5``
     - IPR.5
     - str
     - required
     - IPR Date/Time: Item #2034
   * - ``ipr_6``
     - IPR.6
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Adjudicated/Paid Amount: Item #2035
   * - ``ipr_7``
     - IPR.7
     - Optional[str]
     - optional
     - Expected Payment Date/Time: Item #2036
   * - ``ipr_8``
     - IPR.8
     - str
     - required
     - IPR Checksum: Item #2037

.. _hl7-v2_8_2-ISD:

.. py:class:: hl7types.hl7.v2_8_2.segments.ISD.ISD
   :noindex:

   HL7 v2 ISD segment.

ISD
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``isd_1``
     - ISD.1
     - str
     - required
     - Reference Interaction Number: Item #1326
   * - ``isd_2``
     - ISD.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Interaction Type Identifier: Item #1327 | Table HL70368
   * - ``isd_3``
     - ISD.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Interaction Active State: Item #1328 | Table HL70387

.. _hl7-v2_8_2-ITM:

.. py:class:: hl7types.hl7.v2_8_2.segments.ITM.ITM
   :noindex:

   HL7 v2 ITM segment.

ITM
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``itm_1``
     - ITM.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Item Identifier: Item #2186
   * - ``itm_2``
     - ITM.2
     - Optional[str]
     - optional
     - Item Description: Item #2274
   * - ``itm_3``
     - ITM.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Item Status: Item #2187 | Table HL70776
   * - ``itm_4``
     - ITM.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Item Type: Item #2188 | Table HL70778
   * - ``itm_5``
     - ITM.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Item Category: Item #2189
   * - ``itm_6``
     - ITM.6
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Subject to Expiration Indicator: Item #2190 | Table HL70532
   * - ``itm_7``
     - ITM.7
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Manufacturer Identifier: Item #2191
   * - ``itm_8``
     - ITM.8
     - Optional[str]
     - optional
     - Manufacturer Name: Item #2275
   * - ``itm_9``
     - ITM.9
     - Optional[str]
     - optional
     - Manufacturer Catalog Number: Item #2192
   * - ``itm_10``
     - ITM.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Manufacturer Labeler Identification Code: Item #2193
   * - ``itm_11``
     - ITM.11
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Patient Chargeable Indicator: Item #2070 | Table HL70532
   * - ``itm_12``
     - ITM.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Transaction Code: Item #361 | Table HL70132
   * - ``itm_13``
     - ITM.13
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Transaction amount - unit: Item #366
   * - ``itm_14``
     - ITM.14
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Stocked Item Indicator: Item #2197 | Table HL70532
   * - ``itm_15``
     - ITM.15
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Supply Risk Codes: Item #2266 | Table HL70871
   * - ``itm_16``
     - ITM.16
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Approving Regulatory Agency: Item #2199 | Table HL70790
   * - ``itm_17``
     - ITM.17
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Latex Indicator: Item #2200 | Table HL70532
   * - ``itm_18``
     - ITM.18
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Ruling Act: Item #2201 | Table HL70793
   * - ``itm_19``
     - ITM.19
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Item Natural Account Code: Item #282 | Table HL70320
   * - ``itm_20``
     - ITM.20
     - Optional[str]
     - optional
     - Approved To Buy Quantity: Item #2203
   * - ``itm_21``
     - ITM.21
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Approved To Buy Price: Item #2204
   * - ``itm_22``
     - ITM.22
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Taxable Item Indicator: Item #2205 | Table HL70532
   * - ``itm_23``
     - ITM.23
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Freight Charge Indicator: Item #2206 | Table HL70532
   * - ``itm_24``
     - ITM.24
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Item Set Indicator: Item #2207 | Table HL70532
   * - ``itm_25``
     - ITM.25
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Item Set Identifier: Item #2208
   * - ``itm_26``
     - ITM.26
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Track Department Usage Indicator: Item #2209 | Table HL70532
   * - ``itm_27``
     - ITM.27
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Procedure Code: Item #393 | Table HL70088
   * - ``itm_28``
     - ITM.28
     - Optional[List[:ref:`CNE <hl7-v2_8_2-CNE>`]]
     - optional
     - Procedure Code Modifier: Item #1316 | Table HL70340
   * - ``itm_29``
     - ITM.29
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Special Handling Code: Item #1370 | Table HL70376
   * - ``itm_30``
     - ITM.30
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Hazardous Indicator: Item #3388 | Table HL70532
   * - ``itm_31``
     - ITM.31
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Sterile Indicator: Item #3304 | Table HL70532
   * - ``itm_32``
     - ITM.32
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Material Data Safety Sheet Number: Item #3305
   * - ``itm_33``
     - ITM.33
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - United Nations Standard Products and Services Code (UNSPSC): Item #3306 | Table HL70396

.. _hl7-v2_8_2-IVC:

.. py:class:: hl7types.hl7.v2_8_2.segments.IVC.IVC
   :noindex:

   HL7 v2 IVC segment.

IVC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ivc_1``
     - IVC.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Provider Invoice Number: Item #1914
   * - ``ivc_2``
     - IVC.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Payer Invoice Number: Item #1915
   * - ``ivc_3``
     - IVC.3
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Contract/Agreement Number: Item #1916
   * - ``ivc_4``
     - IVC.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Invoice Control: Item #1917 | Table HL70553
   * - ``ivc_5``
     - IVC.5
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Invoice Reason: Item #1918 | Table HL70554
   * - ``ivc_6``
     - IVC.6
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Invoice Type: Item #1919 | Table HL70555
   * - ``ivc_7``
     - IVC.7
     - str
     - required
     - Invoice Date/Time: Item #1920
   * - ``ivc_8``
     - IVC.8
     - :ref:`CP <hl7-v2_8_2-CP>`
     - required
     - Invoice Amount: Item #1921
   * - ``ivc_9``
     - IVC.9
     - Optional[str]
     - optional
     - Payment Terms: Item #1922
   * - ``ivc_10``
     - IVC.10
     - :ref:`XON <hl7-v2_8_2-XON>`
     - required
     - Provider Organization: Item #1923
   * - ``ivc_11``
     - IVC.11
     - :ref:`XON <hl7-v2_8_2-XON>`
     - required
     - Payer Organization: Item #1924
   * - ``ivc_12``
     - IVC.12
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Attention: Item #1925
   * - ``ivc_13``
     - IVC.13
     - Optional[str]
     - optional
     - Last Invoice Indicator: Item #1926 | Table HL70136
   * - ``ivc_14``
     - IVC.14
     - Optional[str]
     - optional
     - Invoice Booking Period: Item #1927
   * - ``ivc_15``
     - IVC.15
     - Optional[str]
     - optional
     - Origin: Item #1928
   * - ``ivc_16``
     - IVC.16
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Invoice Fixed Amount: Item #1929
   * - ``ivc_17``
     - IVC.17
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Special Costs: Item #1930
   * - ``ivc_18``
     - IVC.18
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Amount for Doctors Treatment: Item #1931
   * - ``ivc_19``
     - IVC.19
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Responsible Physician: Item #1932
   * - ``ivc_20``
     - IVC.20
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Cost Center: Item #1933
   * - ``ivc_21``
     - IVC.21
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Invoice Prepaid Amount: Item #1934
   * - ``ivc_22``
     - IVC.22
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Total Invoice Amount without Prepaid Amount: Item #1935
   * - ``ivc_23``
     - IVC.23
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Total-Amount of VAT: Item #1936
   * - ``ivc_24``
     - IVC.24
     - Optional[List[str]]
     - optional
     - VAT-Rates applied: Item #1937
   * - ``ivc_25``
     - IVC.25
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Benefit Group: Item #1938 | Table HL70556
   * - ``ivc_26``
     - IVC.26
     - Optional[str]
     - optional
     - Provider Tax ID: Item #2038
   * - ``ivc_27``
     - IVC.27
     - Optional[str]
     - optional
     - Payer Tax ID: Item #2039
   * - ``ivc_28``
     - IVC.28
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Provider Tax Status: Item #2040 | Table HL70572
   * - ``ivc_29``
     - IVC.29
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Payer Tax Status: Item #2041 | Table HL70572
   * - ``ivc_30``
     - IVC.30
     - Optional[str]
     - optional
     - Sales Tax ID: Item #2042

.. _hl7-v2_8_2-IVT:

.. py:class:: hl7types.hl7.v2_8_2.segments.IVT.IVT
   :noindex:

   HL7 v2 IVT segment.

IVT
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ivt_1``
     - IVT.1
     - str
     - required
     - Set Id - IVT: Item #2062
   * - ``ivt_2``
     - IVT.2
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Inventory Location Identifier: Item #2063
   * - ``ivt_3``
     - IVT.3
     - Optional[str]
     - optional
     - Inventory Location Name: Item #2277
   * - ``ivt_4``
     - IVT.4
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Source Location Identifier: Item #2064
   * - ``ivt_5``
     - IVT.5
     - Optional[str]
     - optional
     - Source Location Name: Item #2278
   * - ``ivt_6``
     - IVT.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Item Status: Item #2065 | Table HL70625
   * - ``ivt_7``
     - IVT.7
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Bin Location Identifier: Item #2066
   * - ``ivt_8``
     - IVT.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Order Packaging: Item #2067 | Table HL70818
   * - ``ivt_9``
     - IVT.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Issue Packaging: Item #2068
   * - ``ivt_10``
     - IVT.10
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Default Inventory Asset Account: Item #2069
   * - ``ivt_11``
     - IVT.11
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Patient Chargeable Indicator: Item #2070 | Table HL70532
   * - ``ivt_12``
     - IVT.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Transaction Code: Item #361 | Table HL70132
   * - ``ivt_13``
     - IVT.13
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Transaction amount - unit: Item #366
   * - ``ivt_14``
     - IVT.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Item Importance Code: Item #2073 | Table HL70634
   * - ``ivt_15``
     - IVT.15
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Stocked Item Indicator: Item #2074 | Table HL70532
   * - ``ivt_16``
     - IVT.16
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Consignment Item Indicator: Item #2075 | Table HL70532
   * - ``ivt_17``
     - IVT.17
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Reusable Item Indicator: Item #2076 | Table HL70532
   * - ``ivt_18``
     - IVT.18
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Reusable Cost: Item #2077
   * - ``ivt_19``
     - IVT.19
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Substitute Item Identifier: Item #2078
   * - ``ivt_20``
     - IVT.20
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Latex-Free Substitute Item Identifier: Item #2079
   * - ``ivt_21``
     - IVT.21
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Recommended Reorder Theory: Item #2080 | Table HL70642
   * - ``ivt_22``
     - IVT.22
     - Optional[str]
     - optional
     - Recommended Safety Stock Days: Item #2081
   * - ``ivt_23``
     - IVT.23
     - Optional[str]
     - optional
     - Recommended Maximum Days Inventory: Item #2082
   * - ``ivt_24``
     - IVT.24
     - Optional[str]
     - optional
     - Recommended Order Point: Item #2083
   * - ``ivt_25``
     - IVT.25
     - Optional[str]
     - optional
     - Recommended Order Amount: Item #2084
   * - ``ivt_26``
     - IVT.26
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Operating Room Par Level Indicator: Item #2085 | Table HL70532

.. _hl7-v2_8_2-LAN:

.. py:class:: hl7types.hl7.v2_8_2.segments.LAN.LAN
   :noindex:

   HL7 v2 LAN segment.

LAN
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``lan_1``
     - LAN.1
     - str
     - required
     - Set ID - LAN: Item #1455
   * - ``lan_2``
     - LAN.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Language Code: Item #1456 | Table HL70296
   * - ``lan_3``
     - LAN.3
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Language Ability Code: Item #1457 | Table HL70403
   * - ``lan_4``
     - LAN.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Language Proficiency Code: Item #1458 | Table HL70404

.. _hl7-v2_8_2-LCC:

.. py:class:: hl7types.hl7.v2_8_2.segments.LCC.LCC
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
     - Description
   * - ``lcc_1``
     - LCC.1
     - :ref:`PL <hl7-v2_8_2-PL>`
     - required
     - Primary Key Value - LCC: Item #979
   * - ``lcc_2``
     - LCC.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Location Department: Item #964 | Table HL70264
   * - ``lcc_3``
     - LCC.3
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Accommodation Type: Item #980 | Table HL70129
   * - ``lcc_4``
     - LCC.4
     - List[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - required
     - Charge Code: Item #981 | Table HL70132

.. _hl7-v2_8_2-LCH:

.. py:class:: hl7types.hl7.v2_8_2.segments.LCH.LCH
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
     - Description
   * - ``lch_1``
     - LCH.1
     - :ref:`PL <hl7-v2_8_2-PL>`
     - required
     - Primary Key Value - LCH: Item #1305
   * - ``lch_2``
     - LCH.2
     - Optional[str]
     - optional
     - Segment Action Code: Item #763 | Table HL70206
   * - ``lch_3``
     - LCH.3
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Segment Unique Key: Item #764
   * - ``lch_4``
     - LCH.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Location Characteristic ID: Item #1295 | Table HL70324
   * - ``lch_5``
     - LCH.5
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Location Characteristic Value - LCH: Item #1294 | Table HL70136

.. _hl7-v2_8_2-LDP:

.. py:class:: hl7types.hl7.v2_8_2.segments.LDP.LDP
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
     - Description
   * - ``ldp_1``
     - LDP.1
     - :ref:`PL <hl7-v2_8_2-PL>`
     - required
     - Primary Key Value - LDP: Item #963
   * - ``ldp_2``
     - LDP.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Location Department: Item #964 | Table HL70264
   * - ``ldp_3``
     - LDP.3
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Location Service: Item #965 | Table HL70069
   * - ``ldp_4``
     - LDP.4
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Specialty Type: Item #966 | Table HL70265
   * - ``ldp_5``
     - LDP.5
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Valid Patient Classes: Item #967 | Table HL70004
   * - ``ldp_6``
     - LDP.6
     - Optional[str]
     - optional
     - Active/Inactive Flag: Item #675 | Table HL70183
   * - ``ldp_7``
     - LDP.7
     - Optional[str]
     - optional
     - Activation Date - LDP: Item #969
   * - ``ldp_8``
     - LDP.8
     - Optional[str]
     - optional
     - Inactivation Date - LDP: Item #970
   * - ``ldp_9``
     - LDP.9
     - Optional[str]
     - optional
     - Inactivated Reason: Item #971
   * - ``ldp_10``
     - LDP.10
     - Optional[List[:ref:`VH <hl7-v2_8_2-VH>`]]
     - optional
     - Visiting Hours: Item #976 | Table HL70267
   * - ``ldp_11``
     - LDP.11
     - Optional[:ref:`XTN <hl7-v2_8_2-XTN>`]
     - optional
     - Contact Phone: Item #978
   * - ``ldp_12``
     - LDP.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Location Cost Center: Item #1584 | Table HL70462

.. _hl7-v2_8_2-LOC:

.. py:class:: hl7types.hl7.v2_8_2.segments.LOC.LOC
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
     - Description
   * - ``loc_1``
     - LOC.1
     - :ref:`PL <hl7-v2_8_2-PL>`
     - required
     - Primary Key Value - LOC: Item #1307
   * - ``loc_2``
     - LOC.2
     - Optional[str]
     - optional
     - Location Description: Item #944
   * - ``loc_3``
     - LOC.3
     - List[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - required
     - Location Type - LOC: Item #945 | Table HL70260
   * - ``loc_4``
     - LOC.4
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Organization Name - LOC: Item #947
   * - ``loc_5``
     - LOC.5
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Location Address: Item #948
   * - ``loc_6``
     - LOC.6
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Location Phone: Item #949
   * - ``loc_7``
     - LOC.7
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - License Number: Item #951 | Table HL70461
   * - ``loc_8``
     - LOC.8
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Location Equipment: Item #953 | Table HL70261
   * - ``loc_9``
     - LOC.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Location Service Code: Item #1583 | Table HL70442

.. _hl7-v2_8_2-LRL:

.. py:class:: hl7types.hl7.v2_8_2.segments.LRL.LRL
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
     - Description
   * - ``lrl_1``
     - LRL.1
     - :ref:`PL <hl7-v2_8_2-PL>`
     - required
     - Primary Key Value - LRL: Item #943
   * - ``lrl_2``
     - LRL.2
     - Optional[str]
     - optional
     - Segment Action Code: Item #763 | Table HL70206
   * - ``lrl_3``
     - LRL.3
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Segment Unique Key: Item #764
   * - ``lrl_4``
     - LRL.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Location Relationship ID: Item #1277 | Table HL70325
   * - ``lrl_5``
     - LRL.5
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Organizational Location Relationship Value: Item #1301
   * - ``lrl_6``
     - LRL.6
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Patient Location Relationship Value: Item #1292

.. _hl7-v2_8_2-MCP:

.. py:class:: hl7types.hl7.v2_8_2.segments.MCP.MCP
   :noindex:

   HL7 v2 MCP segment.

MCP
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``mcp_1``
     - MCP.1
     - str
     - required
     - Set ID - MCP: Item #3468
   * - ``mcp_2``
     - MCP.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Producer's Service/Test/Observation ID: Item #587
   * - ``mcp_3``
     - MCP.3
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Universal Service Price Range - Low Value: Item #3469
   * - ``mcp_4``
     - MCP.4
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Universal Service Price Range - High Value: Item #3470
   * - ``mcp_5``
     - MCP.5
     - Optional[str]
     - optional
     - Reason for Universal Service Cost Range: Item #3471

.. _hl7-v2_8_2-MFA:

.. py:class:: hl7types.hl7.v2_8_2.segments.MFA.MFA
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
     - Description
   * - ``mfa_1``
     - MFA.1
     - str
     - required
     - Record-Level Event Code: Item #664 | Table HL70180
   * - ``mfa_2``
     - MFA.2
     - Optional[str]
     - optional
     - MFN Control ID: Item #665
   * - ``mfa_3``
     - MFA.3
     - Optional[str]
     - optional
     - Event Completion Date/Time: Item #668
   * - ``mfa_4``
     - MFA.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - MFN Record Level Error Return: Item #669 | Table HL70181
   * - ``mfa_5``
     - MFA.5
     - List[varies]
     - required
     - Primary Key Value - MFA: Item #1308 | Table HL79999
   * - ``mfa_6``
     - MFA.6
     - List[str]
     - required
     - Primary Key Value Type - MFA: Item #1320 | Table HL70355

.. _hl7-v2_8_2-MFE:

.. py:class:: hl7types.hl7.v2_8_2.segments.MFE.MFE
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
     - Description
   * - ``mfe_1``
     - MFE.1
     - str
     - required
     - Record-Level Event Code: Item #664 | Table HL70180
   * - ``mfe_2``
     - MFE.2
     - Optional[str]
     - optional
     - MFN Control ID: Item #665
   * - ``mfe_3``
     - MFE.3
     - Optional[str]
     - optional
     - Effective Date/Time: Item #662
   * - ``mfe_4``
     - MFE.4
     - List[varies]
     - required
     - Primary Key Value - MFE: Item #667 | Table HL79999
   * - ``mfe_5``
     - MFE.5
     - List[str]
     - required
     - Primary Key Value Type: Item #1319 | Table HL70355
   * - ``mfe_6``
     - MFE.6
     - Optional[str]
     - optional
     - Entered Date/Time: Item #661
   * - ``mfe_7``
     - MFE.7
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Entered By: Item #224

.. _hl7-v2_8_2-MFI:

.. py:class:: hl7types.hl7.v2_8_2.segments.MFI.MFI
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
     - Description
   * - ``mfi_1``
     - MFI.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Master File Identifier: Item #658 | Table HL70175
   * - ``mfi_2``
     - MFI.2
     - Optional[List[:ref:`HD <hl7-v2_8_2-HD>`]]
     - optional
     - Master File Application Identifier: Item #659 | Table HL70361
   * - ``mfi_3``
     - MFI.3
     - str
     - required
     - File-Level Event Code: Item #660 | Table HL70178
   * - ``mfi_4``
     - MFI.4
     - Optional[str]
     - optional
     - Entered Date/Time: Item #661
   * - ``mfi_5``
     - MFI.5
     - Optional[str]
     - optional
     - Effective Date/Time: Item #662
   * - ``mfi_6``
     - MFI.6
     - str
     - required
     - Response Level Code: Item #663 | Table HL70179

.. _hl7-v2_8_2-MRG:

.. py:class:: hl7types.hl7.v2_8_2.segments.MRG.MRG
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
     - Description
   * - ``mrg_1``
     - MRG.1
     - List[:ref:`CX <hl7-v2_8_2-CX>`]
     - required
     - Prior Patient Identifier List: Item #211 | Table HL70061
   * - ``mrg_3``
     - MRG.3
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Prior Patient Account Number: Item #213 | Table HL70061
   * - ``mrg_5``
     - MRG.5
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Prior Visit Number: Item #1279 | Table HL70061
   * - ``mrg_6``
     - MRG.6
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Prior Alternate Visit ID: Item #1280 | Table HL70061
   * - ``mrg_7``
     - MRG.7
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Prior Patient Name: Item #1281 | Table HL70200

.. _hl7-v2_8_2-MSA:

.. py:class:: hl7types.hl7.v2_8_2.segments.MSA.MSA
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
     - Description
   * - ``msa_1``
     - MSA.1
     - str
     - required
     - Acknowledgment Code: Item #18 | Table HL70008
   * - ``msa_2``
     - MSA.2
     - str
     - required
     - Message Control ID: Item #10
   * - ``msa_4``
     - MSA.4
     - Optional[str]
     - optional
     - Expected Sequence Number: Item #21
   * - ``msa_7``
     - MSA.7
     - Optional[str]
     - optional
     - Message Waiting Number: Item #1827
   * - ``msa_8``
     - MSA.8
     - Optional[str]
     - optional
     - Message Waiting Priority: Item #1828 | Table HL70520

.. _hl7-v2_8_2-MSH:

.. py:class:: hl7types.hl7.v2_8_2.segments.MSH.MSH
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
     - Description
   * - ``msh_1``
     - MSH.1
     - str
     - optional
     - Field Separator: Item #1
   * - ``msh_2``
     - MSH.2
     - str
     - optional
     - Encoding Characters: Item #2
   * - ``msh_3``
     - MSH.3
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Sending Application: Item #3 | Table HL70361
   * - ``msh_4``
     - MSH.4
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Sending Facility: Item #4 | Table HL70362
   * - ``msh_5``
     - MSH.5
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Receiving Application: Item #5 | Table HL70361
   * - ``msh_6``
     - MSH.6
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Receiving Facility: Item #6 | Table HL70362
   * - ``msh_7``
     - MSH.7
     - str
     - required
     - Date/Time of Message: Item #7
   * - ``msh_8``
     - MSH.8
     - Optional[str]
     - optional
     - Security: Item #8
   * - ``msh_9``
     - MSH.9
     - :ref:`MSG <hl7-v2_8_2-MSG>`
     - required
     - Message Type: Item #9
   * - ``msh_10``
     - MSH.10
     - str
     - required
     - Message Control ID: Item #10
   * - ``msh_11``
     - MSH.11
     - :ref:`PT <hl7-v2_8_2-PT>`
     - required
     - Processing ID: Item #11
   * - ``msh_12``
     - MSH.12
     - :ref:`VID <hl7-v2_8_2-VID>`
     - required
     - Version ID: Item #12
   * - ``msh_13``
     - MSH.13
     - Optional[str]
     - optional
     - Sequence Number: Item #13
   * - ``msh_14``
     - MSH.14
     - Optional[str]
     - optional
     - Continuation Pointer: Item #14
   * - ``msh_15``
     - MSH.15
     - Optional[str]
     - optional
     - Accept Acknowledgment Type: Item #15 | Table HL70155
   * - ``msh_16``
     - MSH.16
     - Optional[str]
     - optional
     - Application Acknowledgment Type: Item #16 | Table HL70155
   * - ``msh_17``
     - MSH.17
     - Optional[str]
     - optional
     - Country Code: Item #17 | Table HL70399
   * - ``msh_18``
     - MSH.18
     - Optional[List[str]]
     - optional
     - Character Set: Item #692 | Table HL70211
   * - ``msh_19``
     - MSH.19
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Principal Language Of Message: Item #693
   * - ``msh_20``
     - MSH.20
     - Optional[str]
     - optional
     - Alternate Character Set Handling Scheme: Item #1317 | Table HL70356
   * - ``msh_21``
     - MSH.21
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Message Profile Identifier: Item #1598
   * - ``msh_22``
     - MSH.22
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Sending Responsible Organization: Item #1823
   * - ``msh_23``
     - MSH.23
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Receiving Responsible Organization: Item #1824
   * - ``msh_24``
     - MSH.24
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Sending Network Address: Item #1825
   * - ``msh_25``
     - MSH.25
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Receiving Network Address: Item #1826

.. _hl7-v2_8_2-NCK:

.. py:class:: hl7types.hl7.v2_8_2.segments.NCK.NCK
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
     - Description
   * - ``nck_1``
     - NCK.1
     - str
     - required
     - System Date/Time: Item #1172

.. _hl7-v2_8_2-NDS:

.. py:class:: hl7types.hl7.v2_8_2.segments.NDS.NDS
   :noindex:

   HL7 v2 NDS segment.

NDS
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``nds_1``
     - NDS.1
     - str
     - required
     - Notification Reference Number: Item #1398
   * - ``nds_2``
     - NDS.2
     - str
     - required
     - Notification Date/Time: Item #1399
   * - ``nds_3``
     - NDS.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Notification Alert Severity: Item #1400 | Table HL70367
   * - ``nds_4``
     - NDS.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Notification Code: Item #1401 | Table HL79999

.. _hl7-v2_8_2-NK1:

.. py:class:: hl7types.hl7.v2_8_2.segments.NK1.NK1
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
     - Description
   * - ``nk1_1``
     - NK1.1
     - str
     - required
     - Set ID - NK1: Item #190
   * - ``nk1_2``
     - NK1.2
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Name: Item #191 | Table HL70200
   * - ``nk1_3``
     - NK1.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Relationship: Item #192 | Table HL70063
   * - ``nk1_4``
     - NK1.4
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Address: Item #193
   * - ``nk1_5``
     - NK1.5
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Phone Number: Item #194
   * - ``nk1_6``
     - NK1.6
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Business Phone Number: Item #195
   * - ``nk1_7``
     - NK1.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Contact Role: Item #196 | Table HL70131
   * - ``nk1_8``
     - NK1.8
     - Optional[str]
     - optional
     - Start Date: Item #197
   * - ``nk1_9``
     - NK1.9
     - Optional[str]
     - optional
     - End Date: Item #198
   * - ``nk1_10``
     - NK1.10
     - Optional[str]
     - optional
     - Next of Kin / Associated Parties Job Title: Item #199
   * - ``nk1_11``
     - NK1.11
     - Optional[:ref:`JCC <hl7-v2_8_2-JCC>`]
     - optional
     - Next of Kin / Associated Parties Job Code/Class: Item #200
   * - ``nk1_12``
     - NK1.12
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Next of Kin / Associated Parties Employee Number: Item #201
   * - ``nk1_13``
     - NK1.13
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Organization Name - NK1: Item #202
   * - ``nk1_14``
     - NK1.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Marital Status: Item #119 | Table HL70002
   * - ``nk1_15``
     - NK1.15
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Administrative Sex: Item #111 | Table HL70001
   * - ``nk1_16``
     - NK1.16
     - Optional[str]
     - optional
     - Date/Time of Birth: Item #110
   * - ``nk1_17``
     - NK1.17
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Living Dependency: Item #755 | Table HL70223
   * - ``nk1_18``
     - NK1.18
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Ambulatory Status: Item #145 | Table HL70009
   * - ``nk1_19``
     - NK1.19
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Citizenship: Item #129 | Table HL70171
   * - ``nk1_20``
     - NK1.20
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Primary Language: Item #118 | Table HL70296
   * - ``nk1_21``
     - NK1.21
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Living Arrangement: Item #742 | Table HL70220
   * - ``nk1_22``
     - NK1.22
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Publicity Code: Item #743 | Table HL70215
   * - ``nk1_23``
     - NK1.23
     - Optional[str]
     - optional
     - Protection Indicator: Item #744 | Table HL70136
   * - ``nk1_24``
     - NK1.24
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Student Indicator: Item #745 | Table HL70231
   * - ``nk1_25``
     - NK1.25
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Religion: Item #120 | Table HL70006
   * - ``nk1_26``
     - NK1.26
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Mother's Maiden Name: Item #109
   * - ``nk1_27``
     - NK1.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Nationality: Item #739 | Table HL70212
   * - ``nk1_28``
     - NK1.28
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Ethnic Group: Item #125 | Table HL70189
   * - ``nk1_29``
     - NK1.29
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Contact Reason: Item #747 | Table HL70222
   * - ``nk1_30``
     - NK1.30
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Contact Person's Name: Item #748
   * - ``nk1_31``
     - NK1.31
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Contact Person's Telephone Number: Item #749
   * - ``nk1_32``
     - NK1.32
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Contact Person's Address: Item #750
   * - ``nk1_33``
     - NK1.33
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Next of Kin/Associated Party's Identifiers: Item #751
   * - ``nk1_34``
     - NK1.34
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Job Status: Item #752 | Table HL70311
   * - ``nk1_35``
     - NK1.35
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Race: Item #113 | Table HL70005
   * - ``nk1_36``
     - NK1.36
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Handicap: Item #753 | Table HL70295
   * - ``nk1_37``
     - NK1.37
     - Optional[str]
     - optional
     - Contact Person Social Security Number: Item #754
   * - ``nk1_38``
     - NK1.38
     - Optional[str]
     - optional
     - Next of Kin Birth Place: Item #1905
   * - ``nk1_39``
     - NK1.39
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - VIP Indicator: Item #146 | Table HL70099
   * - ``nk1_40``
     - NK1.40
     - Optional[:ref:`XTN <hl7-v2_8_2-XTN>`]
     - optional
     - Next of Kin Telecommunication Information: Item #2292
   * - ``nk1_41``
     - NK1.41
     - Optional[:ref:`XTN <hl7-v2_8_2-XTN>`]
     - optional
     - Contact Person's Telecommunication Information: Item #2293

.. _hl7-v2_8_2-NPU:

.. py:class:: hl7types.hl7.v2_8_2.segments.NPU.NPU
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
     - Description
   * - ``npu_1``
     - NPU.1
     - :ref:`PL <hl7-v2_8_2-PL>`
     - required
     - Bed Location: Item #209
   * - ``npu_2``
     - NPU.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Bed Status: Item #170 | Table HL70116

.. _hl7-v2_8_2-NSC:

.. py:class:: hl7types.hl7.v2_8_2.segments.NSC.NSC
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
     - Description
   * - ``nsc_1``
     - NSC.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Application Change Type: Item #1188 | Table HL70409
   * - ``nsc_2``
     - NSC.2
     - Optional[str]
     - optional
     - Current CPU: Item #1189
   * - ``nsc_3``
     - NSC.3
     - Optional[str]
     - optional
     - Current Fileserver: Item #1190
   * - ``nsc_4``
     - NSC.4
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Current Application: Item #1191 | Table HL70361
   * - ``nsc_5``
     - NSC.5
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Current Facility: Item #1192 | Table HL70362
   * - ``nsc_6``
     - NSC.6
     - Optional[str]
     - optional
     - New CPU: Item #1193
   * - ``nsc_7``
     - NSC.7
     - Optional[str]
     - optional
     - New Fileserver: Item #1194
   * - ``nsc_8``
     - NSC.8
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - New Application: Item #1195 | Table HL70361
   * - ``nsc_9``
     - NSC.9
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - New Facility: Item #1196 | Table HL70362

.. _hl7-v2_8_2-NST:

.. py:class:: hl7types.hl7.v2_8_2.segments.NST.NST
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
     - Description
   * - ``nst_1``
     - NST.1
     - str
     - required
     - Statistics Available: Item #1173 | Table HL70136
   * - ``nst_2``
     - NST.2
     - Optional[str]
     - optional
     - Source Identifier: Item #1174
   * - ``nst_3``
     - NST.3
     - Optional[str]
     - optional
     - Source Type: Item #1175 | Table HL70332
   * - ``nst_4``
     - NST.4
     - Optional[str]
     - optional
     - Statistics Start: Item #1176
   * - ``nst_5``
     - NST.5
     - Optional[str]
     - optional
     - Statistics End: Item #1177
   * - ``nst_6``
     - NST.6
     - Optional[str]
     - optional
     - Receive Character Count: Item #1178
   * - ``nst_7``
     - NST.7
     - Optional[str]
     - optional
     - Send Character Count: Item #1179
   * - ``nst_8``
     - NST.8
     - Optional[str]
     - optional
     - Messages Received: Item #1180
   * - ``nst_9``
     - NST.9
     - Optional[str]
     - optional
     - Messages Sent: Item #1181
   * - ``nst_10``
     - NST.10
     - Optional[str]
     - optional
     - Checksum Errors Received: Item #1182
   * - ``nst_11``
     - NST.11
     - Optional[str]
     - optional
     - Length Errors Received: Item #1183
   * - ``nst_12``
     - NST.12
     - Optional[str]
     - optional
     - Other Errors Received: Item #1184
   * - ``nst_13``
     - NST.13
     - Optional[str]
     - optional
     - Connect Timeouts: Item #1185
   * - ``nst_14``
     - NST.14
     - Optional[str]
     - optional
     - Receive Timeouts: Item #1186
   * - ``nst_15``
     - NST.15
     - Optional[str]
     - optional
     - Application control-level Errors: Item #1187

.. _hl7-v2_8_2-NTE:

.. py:class:: hl7types.hl7.v2_8_2.segments.NTE.NTE
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
     - Description
   * - ``nte_1``
     - NTE.1
     - Optional[str]
     - optional
     - Set ID - NTE: Item #96
   * - ``nte_2``
     - NTE.2
     - Optional[str]
     - optional
     - Source of Comment: Item #97 | Table HL70105
   * - ``nte_3``
     - NTE.3
     - Optional[List[:ref:`FT <hl7-v2_8_2-FT>`]]
     - optional
     - Comment: Item #98
   * - ``nte_4``
     - NTE.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Comment Type: Item #1318 | Table HL70364
   * - ``nte_5``
     - NTE.5
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Entered By: Item #224
   * - ``nte_6``
     - NTE.6
     - Optional[str]
     - optional
     - Entered Date/Time: Item #661
   * - ``nte_7``
     - NTE.7
     - Optional[str]
     - optional
     - Effective Start Date: Item #1004
   * - ``nte_8``
     - NTE.8
     - Optional[str]
     - optional
     - Expiration Date: Item #2185

.. _hl7-v2_8_2-OBR:

.. py:class:: hl7types.hl7.v2_8_2.segments.OBR.OBR
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
     - Description
   * - ``obr_1``
     - OBR.1
     - Optional[str]
     - optional
     - Set ID - OBR: Item #237
   * - ``obr_2``
     - OBR.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Placer Order Number: Item #216
   * - ``obr_3``
     - OBR.3
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Filler Order Number: Item #217
   * - ``obr_4``
     - OBR.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Universal Service Identifier: Item #238
   * - ``obr_7``
     - OBR.7
     - Optional[str]
     - optional
     - Observation Date/Time #: Item #241
   * - ``obr_8``
     - OBR.8
     - Optional[str]
     - optional
     - Observation End Date/Time #: Item #242
   * - ``obr_9``
     - OBR.9
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Collection Volume *: Item #243
   * - ``obr_10``
     - OBR.10
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Collector Identifier *: Item #244
   * - ``obr_11``
     - OBR.11
     - Optional[str]
     - optional
     - Specimen Action Code *: Item #245 | Table HL70065
   * - ``obr_12``
     - OBR.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Danger Code: Item #246 | Table HL79999
   * - ``obr_13``
     - OBR.13
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Relevant Clinical Information: Item #247 | Table HL70916
   * - ``obr_16``
     - OBR.16
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Ordering Provider: Item #226
   * - ``obr_17``
     - OBR.17
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Order Callback Phone Number: Item #250
   * - ``obr_18``
     - OBR.18
     - Optional[str]
     - optional
     - Placer Field 1: Item #251
   * - ``obr_19``
     - OBR.19
     - Optional[str]
     - optional
     - Placer Field 2: Item #252
   * - ``obr_20``
     - OBR.20
     - Optional[str]
     - optional
     - Filler Field 1 +: Item #253
   * - ``obr_21``
     - OBR.21
     - Optional[str]
     - optional
     - Filler Field 2 +: Item #254
   * - ``obr_22``
     - OBR.22
     - Optional[str]
     - optional
     - Results Rpt/Status Chng - Date/Time +: Item #255
   * - ``obr_23``
     - OBR.23
     - Optional[:ref:`MOC <hl7-v2_8_2-MOC>`]
     - optional
     - Charge to Practice +: Item #256
   * - ``obr_24``
     - OBR.24
     - Optional[str]
     - optional
     - Diagnostic Serv Sect ID: Item #257 | Table HL70074
   * - ``obr_25``
     - OBR.25
     - Optional[str]
     - optional
     - Result Status +: Item #258 | Table HL70123
   * - ``obr_26``
     - OBR.26
     - Optional[:ref:`PRL <hl7-v2_8_2-PRL>`]
     - optional
     - Parent Result +: Item #259
   * - ``obr_28``
     - OBR.28
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Result Copies To: Item #260
   * - ``obr_29``
     - OBR.29
     - Optional[:ref:`EIP <hl7-v2_8_2-EIP>`]
     - optional
     - Parent  Results Observation Identifier: Item #261
   * - ``obr_30``
     - OBR.30
     - Optional[str]
     - optional
     - Transportation Mode: Item #262 | Table HL70124
   * - ``obr_31``
     - OBR.31
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Reason for Study: Item #263 | Table HL79999
   * - ``obr_32``
     - OBR.32
     - Optional[:ref:`NDL <hl7-v2_8_2-NDL>`]
     - optional
     - Principal Result Interpreter +: Item #264
   * - ``obr_33``
     - OBR.33
     - Optional[List[:ref:`NDL <hl7-v2_8_2-NDL>`]]
     - optional
     - Assistant Result Interpreter +: Item #265
   * - ``obr_34``
     - OBR.34
     - Optional[List[:ref:`NDL <hl7-v2_8_2-NDL>`]]
     - optional
     - Technician +: Item #266
   * - ``obr_35``
     - OBR.35
     - Optional[List[:ref:`NDL <hl7-v2_8_2-NDL>`]]
     - optional
     - Transcriptionist +: Item #267
   * - ``obr_36``
     - OBR.36
     - Optional[str]
     - optional
     - Scheduled Date/Time +: Item #268
   * - ``obr_37``
     - OBR.37
     - Optional[str]
     - optional
     - Number of Sample Containers *: Item #1028
   * - ``obr_38``
     - OBR.38
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Transport Logistics of Collected Sample *: Item #1029 | Table HL79999
   * - ``obr_39``
     - OBR.39
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Collector's Comment *: Item #1030 | Table HL79999
   * - ``obr_40``
     - OBR.40
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Transport Arrangement Responsibility: Item #1031 | Table HL79999
   * - ``obr_41``
     - OBR.41
     - Optional[str]
     - optional
     - Transport Arranged: Item #1032 | Table HL70224
   * - ``obr_42``
     - OBR.42
     - Optional[str]
     - optional
     - Escort Required: Item #1033 | Table HL70225
   * - ``obr_43``
     - OBR.43
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Planned Patient Transport Comment: Item #1034 | Table HL79999
   * - ``obr_44``
     - OBR.44
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Procedure Code: Item #393 | Table HL70088
   * - ``obr_45``
     - OBR.45
     - Optional[List[:ref:`CNE <hl7-v2_8_2-CNE>`]]
     - optional
     - Procedure Code Modifier: Item #1316 | Table HL70340
   * - ``obr_46``
     - OBR.46
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Placer Supplemental Service Information: Item #1474 | Table HL70411
   * - ``obr_47``
     - OBR.47
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Filler Supplemental Service Information: Item #1475 | Table HL70411
   * - ``obr_48``
     - OBR.48
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Medically Necessary Duplicate Procedure Reason: Item #1646 | Table HL70476
   * - ``obr_49``
     - OBR.49
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Result Handling: Item #1647 | Table HL70507
   * - ``obr_50``
     - OBR.50
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Parent Universal Service Identifier: Item #2286
   * - ``obr_51``
     - OBR.51
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Observation Group ID: Item #2307
   * - ``obr_52``
     - OBR.52
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Parent Observation Group ID: Item #2308
   * - ``obr_53``
     - OBR.53
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Alternate Placer Order Number: Item #3303
   * - ``obr_54``
     - OBR.54
     - Optional[:ref:`EIP <hl7-v2_8_2-EIP>`]
     - optional
     - Parent Order: Item #222

.. _hl7-v2_8_2-OBX:

.. py:class:: hl7types.hl7.v2_8_2.segments.OBX.OBX
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
     - Description
   * - ``obx_1``
     - OBX.1
     - Optional[str]
     - optional
     - Set ID - OBX: Item #569
   * - ``obx_2``
     - OBX.2
     - Optional[str]
     - optional
     - Value Type: Item #570 | Table HL70125
   * - ``obx_3``
     - OBX.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Observation Identifier: Item #571 | Table HL79999
   * - ``obx_4``
     - OBX.4
     - Optional[:ref:`OG <hl7-v2_8_2-OG>`]
     - optional
     - Observation Sub-ID: Item #572
   * - ``obx_5``
     - OBX.5
     - Optional[List[varies]]
     - optional
     - Observation Value: Item #573
   * - ``obx_6``
     - OBX.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Units: Item #574 | Table HL79999
   * - ``obx_7``
     - OBX.7
     - Optional[str]
     - optional
     - References Range: Item #575
   * - ``obx_8``
     - OBX.8
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Interpretation Codes: Item #576 | Table HL70078
   * - ``obx_9``
     - OBX.9
     - Optional[str]
     - optional
     - Probability: Item #577
   * - ``obx_10``
     - OBX.10
     - Optional[List[str]]
     - optional
     - Nature of Abnormal Test: Item #578 | Table HL70080
   * - ``obx_11``
     - OBX.11
     - str
     - required
     - Observation Result Status: Item #579 | Table HL70085
   * - ``obx_12``
     - OBX.12
     - Optional[str]
     - optional
     - Effective Date of Reference Range: Item #580
   * - ``obx_13``
     - OBX.13
     - Optional[str]
     - optional
     - User Defined Access Checks: Item #581
   * - ``obx_14``
     - OBX.14
     - Optional[str]
     - optional
     - Date/Time of the Observation: Item #582
   * - ``obx_15``
     - OBX.15
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Producer's ID: Item #583 | Table HL79999
   * - ``obx_16``
     - OBX.16
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Responsible Observer: Item #584
   * - ``obx_17``
     - OBX.17
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Observation Method: Item #936 | Table HL79999
   * - ``obx_18``
     - OBX.18
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Equipment Instance Identifier: Item #1479
   * - ``obx_19``
     - OBX.19
     - Optional[str]
     - optional
     - Date/Time of the Analysis: Item #1480
   * - ``obx_20``
     - OBX.20
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Observation Site: Item #2179 | Table HL70163
   * - ``obx_21``
     - OBX.21
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Observation Instance Identifier: Item #2180
   * - ``obx_22``
     - OBX.22
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Mood Code: Item #2182 | Table HL70725
   * - ``obx_23``
     - OBX.23
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Performing Organization Name: Item #2283
   * - ``obx_24``
     - OBX.24
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - Performing Organization Address: Item #2284
   * - ``obx_25``
     - OBX.25
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Performing Organization Medical Director: Item #2285
   * - ``obx_26``
     - OBX.26
     - Optional[str]
     - optional
     - Patient Results Release Category: Item #2313 | Table HL70909
   * - ``obx_27``
     - OBX.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Root Cause: Item #3308 | Table HL70914
   * - ``obx_28``
     - OBX.28
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Local Process Control: Item #3309 | Table HL70915
   * - ``obx_29``
     - OBX.29
     - Optional[str]
     - optional
     - Observation Type: Item #3432 | Table HL70936
   * - ``obx_30``
     - OBX.30
     - Optional[str]
     - optional
     - Observation Sub-Type: Item #3475 | Table HL70937

.. _hl7-v2_8_2-ODS:

.. py:class:: hl7types.hl7.v2_8_2.segments.ODS.ODS
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
     - Description
   * - ``ods_1``
     - ODS.1
     - str
     - required
     - Type: Item #269 | Table HL70159
   * - ``ods_2``
     - ODS.2
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Service Period: Item #270 | Table HL79999
   * - ``ods_3``
     - ODS.3
     - List[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - required
     - Diet, Supplement, or Preference Code: Item #271 | Table HL79999
   * - ``ods_4``
     - ODS.4
     - Optional[List[str]]
     - optional
     - Text Instruction: Item #272

.. _hl7-v2_8_2-ODT:

.. py:class:: hl7types.hl7.v2_8_2.segments.ODT.ODT
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
     - Description
   * - ``odt_1``
     - ODT.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Tray Type: Item #273 | Table HL70160
   * - ``odt_2``
     - ODT.2
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Service Period: Item #270 | Table HL79999
   * - ``odt_3``
     - ODT.3
     - Optional[str]
     - optional
     - Text Instruction: Item #272

.. _hl7-v2_8_2-OM1:

.. py:class:: hl7types.hl7.v2_8_2.segments.OM1.OM1
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
     - Description
   * - ``om1_1``
     - OM1.1
     - str
     - required
     - Sequence Number - Test/Observation Master File: Item #586
   * - ``om1_2``
     - OM1.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Producer's Service/Test/Observation ID: Item #587
   * - ``om1_3``
     - OM1.3
     - Optional[List[str]]
     - optional
     - Permitted Data Types: Item #588 | Table HL70125
   * - ``om1_4``
     - OM1.4
     - str
     - required
     - Specimen Required: Item #589 | Table HL70136
   * - ``om1_5``
     - OM1.5
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Producer ID: Item #590 | Table HL79999
   * - ``om1_6``
     - OM1.6
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Observation Description: Item #591
   * - ``om1_7``
     - OM1.7
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Other Service/Test/Observation IDs for the Observation: Item #592 | Table HL79999
   * - ``om1_8``
     - OM1.8
     - Optional[List[str]]
     - optional
     - Other Names: Item #593
   * - ``om1_9``
     - OM1.9
     - Optional[str]
     - optional
     - Preferred Report Name for the Observation: Item #594
   * - ``om1_10``
     - OM1.10
     - Optional[str]
     - optional
     - Preferred Short Name or Mnemonic for the Observation: Item #595
   * - ``om1_11``
     - OM1.11
     - Optional[str]
     - optional
     - Preferred Long Name for the Observation: Item #596
   * - ``om1_12``
     - OM1.12
     - Optional[str]
     - optional
     - Orderability: Item #597 | Table HL70136
   * - ``om1_13``
     - OM1.13
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Identity of Instrument Used to Perform this Study: Item #598 | Table HL79999
   * - ``om1_14``
     - OM1.14
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Coded Representation of Method: Item #599 | Table HL79999
   * - ``om1_15``
     - OM1.15
     - Optional[str]
     - optional
     - Portable Device Indicator: Item #600 | Table HL70136
   * - ``om1_16``
     - OM1.16
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Observation Producing Department/Section: Item #601 | Table HL79999
   * - ``om1_17``
     - OM1.17
     - Optional[:ref:`XTN <hl7-v2_8_2-XTN>`]
     - optional
     - Telephone Number of Section: Item #602
   * - ``om1_18``
     - OM1.18
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Nature of Service/Test/Observation: Item #603 | Table HL70174
   * - ``om1_19``
     - OM1.19
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Report Subheader: Item #604 | Table HL79999
   * - ``om1_20``
     - OM1.20
     - Optional[str]
     - optional
     - Report Display Order: Item #605
   * - ``om1_21``
     - OM1.21
     - Optional[str]
     - optional
     - Date/Time Stamp for Any Change in Definition for the Observation: Item #606
   * - ``om1_22``
     - OM1.22
     - Optional[str]
     - optional
     - Effective Date/Time of Change: Item #607
   * - ``om1_23``
     - OM1.23
     - Optional[str]
     - optional
     - Typical Turn-Around Time: Item #608
   * - ``om1_24``
     - OM1.24
     - Optional[str]
     - optional
     - Processing Time: Item #609
   * - ``om1_25``
     - OM1.25
     - Optional[List[str]]
     - optional
     - Processing Priority: Item #610 | Table HL70168
   * - ``om1_26``
     - OM1.26
     - Optional[str]
     - optional
     - Reporting Priority: Item #611 | Table HL70169
   * - ``om1_27``
     - OM1.27
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Outside Site(s) Where Observation May Be Performed: Item #612 | Table HL79999
   * - ``om1_28``
     - OM1.28
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Address of Outside Site(s): Item #613
   * - ``om1_29``
     - OM1.29
     - Optional[:ref:`XTN <hl7-v2_8_2-XTN>`]
     - optional
     - Phone Number of Outside Site: Item #614
   * - ``om1_30``
     - OM1.30
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Confidentiality Code: Item #615 | Table HL70177
   * - ``om1_31``
     - OM1.31
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Observations Required to Interpret this Observation: Item #616 | Table HL79999
   * - ``om1_32``
     - OM1.32
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Interpretation of Observations: Item #617
   * - ``om1_33``
     - OM1.33
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Contraindications to Observations: Item #618 | Table HL79999
   * - ``om1_34``
     - OM1.34
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Reflex Tests/Observations: Item #619 | Table HL79999
   * - ``om1_35``
     - OM1.35
     - Optional[List[:ref:`TX <hl7-v2_8_2-TX>`]]
     - optional
     - Rules that Trigger Reflex Testing: Item #620
   * - ``om1_36``
     - OM1.36
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Fixed Canned Message: Item #621 | Table HL79999
   * - ``om1_37``
     - OM1.37
     - Optional[List[:ref:`TX <hl7-v2_8_2-TX>`]]
     - optional
     - Patient Preparation: Item #622
   * - ``om1_38``
     - OM1.38
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Procedure Medication: Item #623 | Table HL79999
   * - ``om1_39``
     - OM1.39
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Factors that may Affect the Observation: Item #624
   * - ``om1_40``
     - OM1.40
     - Optional[List[str]]
     - optional
     - Service/Test/Observation Performance Schedule: Item #625
   * - ``om1_41``
     - OM1.41
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Description of Test Methods: Item #626
   * - ``om1_42``
     - OM1.42
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Kind of Quantity Observed: Item #937 | Table HL70254
   * - ``om1_43``
     - OM1.43
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Point Versus Interval: Item #938 | Table HL70255
   * - ``om1_44``
     - OM1.44
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Challenge Information: Item #939 | Table HL70256
   * - ``om1_45``
     - OM1.45
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Relationship Modifier: Item #940 | Table HL70258
   * - ``om1_46``
     - OM1.46
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Target Anatomic Site Of Test: Item #941 | Table HL79999
   * - ``om1_47``
     - OM1.47
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Modality of Imaging Measurement: Item #942 | Table HL70910
   * - ``om1_48``
     - OM1.48
     - Optional[str]
     - optional
     - Exclusive Test: Item #3310 | Table HL70919
   * - ``om1_49``
     - OM1.49
     - Optional[str]
     - optional
     - Diagnostic Serv Sect ID: Item #257 | Table HL70074
   * - ``om1_50``
     - OM1.50
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Taxonomic Classification Code: Item #1539
   * - ``om1_51``
     - OM1.51
     - Optional[List[str]]
     - optional
     - Other Names: Item #3399
   * - ``om1_52``
     - OM1.52
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Replacement Producer's Service/Test/Observation ID: Item #3433 | Table HL79999
   * - ``om1_53``
     - OM1.53
     - Optional[List[:ref:`TX <hl7-v2_8_2-TX>`]]
     - optional
     - Prior Resuts Instructions: Item #3434
   * - ``om1_54``
     - OM1.54
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Special Instructions: Item #3435
   * - ``om1_55``
     - OM1.55
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Test Category: Item #3436
   * - ``om1_56``
     - OM1.56
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Observation/Identifier associated with Producer's Service/Test/Observation ID: Item #3437 | Table HL79999
   * - ``om1_57``
     - OM1.57
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Typical Turn-Around Time: Item #3438
   * - ``om1_58``
     - OM1.58
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Gender Restriction: Item #3439 | Table HL70001
   * - ``om1_59``
     - OM1.59
     - Optional[List[:ref:`NR <hl7-v2_8_2-NR>`]]
     - optional
     - Age Restriction: Item #3440

.. _hl7-v2_8_2-OM2:

.. py:class:: hl7types.hl7.v2_8_2.segments.OM2.OM2
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
     - Description
   * - ``om2_1``
     - OM2.1
     - Optional[str]
     - optional
     - Sequence Number - Test/Observation Master File: Item #586
   * - ``om2_2``
     - OM2.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Units of Measure: Item #627 | Table HL79999
   * - ``om2_3``
     - OM2.3
     - Optional[List[str]]
     - optional
     - Range of Decimal Precision: Item #628
   * - ``om2_4``
     - OM2.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Corresponding SI Units of Measure: Item #629 | Table HL79999
   * - ``om2_5``
     - OM2.5
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - SI Conversion Factor: Item #630
   * - ``om2_6``
     - OM2.6
     - Optional[List[:ref:`RFR <hl7-v2_8_2-RFR>`]]
     - optional
     - Reference (Normal) Range for Ordinal and Continuous Observations: Item #631
   * - ``om2_7``
     - OM2.7
     - Optional[List[:ref:`RFR <hl7-v2_8_2-RFR>`]]
     - optional
     - Critical Range for Ordinal and Continuous Observations: Item #632
   * - ``om2_8``
     - OM2.8
     - Optional[:ref:`RFR <hl7-v2_8_2-RFR>`]
     - optional
     - Absolute Range for Ordinal and Continuous Observations: Item #633
   * - ``om2_9``
     - OM2.9
     - Optional[List[:ref:`DLT <hl7-v2_8_2-DLT>`]]
     - optional
     - Delta Check Criteria: Item #634
   * - ``om2_10``
     - OM2.10
     - Optional[str]
     - optional
     - Minimum Meaningful Increments: Item #635

.. _hl7-v2_8_2-OM3:

.. py:class:: hl7types.hl7.v2_8_2.segments.OM3.OM3
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
     - Description
   * - ``om3_1``
     - OM3.1
     - Optional[str]
     - optional
     - Sequence Number - Test/Observation Master File: Item #586
   * - ``om3_2``
     - OM3.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Preferred Coding System: Item #636 | Table HL79999
   * - ``om3_3``
     - OM3.3
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Valid Coded "Answers": Item #637 | Table HL79999
   * - ``om3_4``
     - OM3.4
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Normal Text/Codes for Categorical Observations: Item #638 | Table HL79999
   * - ``om3_5``
     - OM3.5
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Abnormal Text/Codes for Categorical Observations: Item #639 | Table HL79999
   * - ``om3_6``
     - OM3.6
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Critical Text/Codes for Categorical Observations: Item #640 | Table HL79999
   * - ``om3_7``
     - OM3.7
     - Optional[str]
     - optional
     - Value Type: Item #570 | Table HL70125

.. _hl7-v2_8_2-OM4:

.. py:class:: hl7types.hl7.v2_8_2.segments.OM4.OM4
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
     - Description
   * - ``om4_1``
     - OM4.1
     - Optional[str]
     - optional
     - Sequence Number - Test/Observation Master File: Item #586
   * - ``om4_2``
     - OM4.2
     - Optional[str]
     - optional
     - Derived Specimen: Item #642 | Table HL70170
   * - ``om4_3``
     - OM4.3
     - Optional[List[:ref:`TX <hl7-v2_8_2-TX>`]]
     - optional
     - Container Description: Item #643
   * - ``om4_4``
     - OM4.4
     - Optional[List[str]]
     - optional
     - Container Volume: Item #644
   * - ``om4_5``
     - OM4.5
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Container Units: Item #645 | Table HL79999
   * - ``om4_6``
     - OM4.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Specimen: Item #646 | Table HL79999
   * - ``om4_7``
     - OM4.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Additive: Item #647 | Table HL70371
   * - ``om4_8``
     - OM4.8
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Preparation: Item #648
   * - ``om4_9``
     - OM4.9
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Special Handling Requirements: Item #649
   * - ``om4_10``
     - OM4.10
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Normal Collection Volume: Item #650
   * - ``om4_11``
     - OM4.11
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Minimum Collection Volume: Item #651
   * - ``om4_12``
     - OM4.12
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Specimen Requirements: Item #652
   * - ``om4_13``
     - OM4.13
     - Optional[List[str]]
     - optional
     - Specimen Priorities: Item #653 | Table HL70027
   * - ``om4_14``
     - OM4.14
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Specimen Retention Time: Item #654
   * - ``om4_15``
     - OM4.15
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Specimen Handling Code: Item #1908 | Table HL70376
   * - ``om4_16``
     - OM4.16
     - Optional[str]
     - optional
     - Specimen Preference: Item #3311 | Table HL70920
   * - ``om4_17``
     - OM4.17
     - Optional[str]
     - optional
     - Preferred Specimen/Attribture Sequence ID: Item #3312
   * - ``om4_18``
     - OM4.18
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Taxonomic Classification Code: Item #1539

.. _hl7-v2_8_2-OM5:

.. py:class:: hl7types.hl7.v2_8_2.segments.OM5.OM5
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
     - Description
   * - ``om5_1``
     - OM5.1
     - Optional[str]
     - optional
     - Sequence Number - Test/Observation Master File: Item #586
   * - ``om5_2``
     - OM5.2
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Test/Observations Included Within an Ordered Test Battery: Item #655 | Table HL79999
   * - ``om5_3``
     - OM5.3
     - Optional[str]
     - optional
     - Observation ID Suffixes: Item #656

.. _hl7-v2_8_2-OM6:

.. py:class:: hl7types.hl7.v2_8_2.segments.OM6.OM6
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
     - Description
   * - ``om6_1``
     - OM6.1
     - Optional[str]
     - optional
     - Sequence Number - Test/Observation Master File: Item #586
   * - ``om6_2``
     - OM6.2
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Derivation Rule: Item #657

.. _hl7-v2_8_2-OM7:

.. py:class:: hl7types.hl7.v2_8_2.segments.OM7.OM7
   :noindex:

   HL7 v2 OM7 segment.

OM7
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``om7_1``
     - OM7.1
     - str
     - required
     - Sequence Number - Test/Observation Master File: Item #586
   * - ``om7_2``
     - OM7.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Universal Service Identifier: Item #238
   * - ``om7_3``
     - OM7.3
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Category Identifier: Item #1481 | Table HL70412
   * - ``om7_4``
     - OM7.4
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Category Description: Item #1482
   * - ``om7_5``
     - OM7.5
     - Optional[List[str]]
     - optional
     - Category Synonym: Item #1483
   * - ``om7_6``
     - OM7.6
     - Optional[str]
     - optional
     - Effective Test/Service Start Date/Time: Item #1484
   * - ``om7_7``
     - OM7.7
     - Optional[str]
     - optional
     - Effective Test/Service End Date/Time: Item #1485
   * - ``om7_8``
     - OM7.8
     - Optional[str]
     - optional
     - Test/Service Default Duration Quantity: Item #1486
   * - ``om7_9``
     - OM7.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Test/Service Default Duration Units: Item #1487 | Table HL79999
   * - ``om7_10``
     - OM7.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Test/Service Default Frequency: Item #1488
   * - ``om7_11``
     - OM7.11
     - Optional[str]
     - optional
     - Consent Indicator: Item #1489 | Table HL70136
   * - ``om7_12``
     - OM7.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Consent Identifier: Item #1490 | Table HL70413
   * - ``om7_13``
     - OM7.13
     - Optional[str]
     - optional
     - Consent Effective Start Date/Time: Item #1491
   * - ``om7_14``
     - OM7.14
     - Optional[str]
     - optional
     - Consent Effective End Date/Time: Item #1492
   * - ``om7_15``
     - OM7.15
     - Optional[str]
     - optional
     - Consent Interval Quantity: Item #1493
   * - ``om7_16``
     - OM7.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Consent Interval Units: Item #1494 | Table HL70414
   * - ``om7_17``
     - OM7.17
     - Optional[str]
     - optional
     - Consent Waiting Period Quantity: Item #1495
   * - ``om7_18``
     - OM7.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Consent Waiting Period Units: Item #1496 | Table HL70414
   * - ``om7_19``
     - OM7.19
     - Optional[str]
     - optional
     - Effective Date/Time of Change: Item #607
   * - ``om7_20``
     - OM7.20
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Entered By: Item #224
   * - ``om7_21``
     - OM7.21
     - Optional[List[:ref:`PL <hl7-v2_8_2-PL>`]]
     - optional
     - Orderable-at Location: Item #1497
   * - ``om7_22``
     - OM7.22
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Formulary Status: Item #1498 | Table HL70473
   * - ``om7_23``
     - OM7.23
     - Optional[str]
     - optional
     - Special Order Indicator: Item #1499 | Table HL70136
   * - ``om7_24``
     - OM7.24
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Primary Key Value - CDM: Item #1306

.. _hl7-v2_8_2-OMC:

.. py:class:: hl7types.hl7.v2_8_2.segments.OMC.OMC
   :noindex:

   HL7 v2 OMC segment.

OMC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``omc_1``
     - OMC.1
     - Optional[str]
     - optional
     - Sequence Number - Test/Observation Master File: Item #586
   * - ``omc_2``
     - OMC.2
     - Optional[str]
     - optional
     - Segment Action Code: Item #763 | Table HL70206
   * - ``omc_3``
     - OMC.3
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Segment Unique Key: Item #764
   * - ``omc_4``
     - OMC.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Clinical Information Request: Item #3444 | Table HL79999
   * - ``omc_5``
     - OMC.5
     - List[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - required
     - Collection Event/Process Step: Item #3445 | Table HL70938
   * - ``omc_6``
     - OMC.6
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Communication Location: Item #3446 | Table HL70939
   * - ``omc_7``
     - OMC.7
     - Optional[str]
     - optional
     - Answer Required: Item #3447 | Table HL70136
   * - ``omc_8``
     - OMC.8
     - Optional[str]
     - optional
     - Hint/Help Text: Item #3448
   * - ``omc_9``
     - OMC.9
     - Optional[varies]
     - optional
     - Type of Answer: Item #3449 | Table HL70125
   * - ``omc_10``
     - OMC.10
     - Optional[str]
     - optional
     - Multiple Answers Allowed: Item #3450 | Table HL70136
   * - ``omc_11``
     - OMC.11
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Answer Choices: Item #3451 | Table HL79999
   * - ``omc_12``
     - OMC.12
     - Optional[str]
     - optional
     - Character Limit: Item #3452
   * - ``omc_13``
     - OMC.13
     - Optional[str]
     - optional
     - Number of Decimals: Item #3453

.. _hl7-v2_8_2-ORC:

.. py:class:: hl7types.hl7.v2_8_2.segments.ORC.ORC
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
     - Description
   * - ``orc_1``
     - ORC.1
     - str
     - required
     - Order Control: Item #215 | Table HL70119
   * - ``orc_2``
     - ORC.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Placer Order Number: Item #216
   * - ``orc_3``
     - ORC.3
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Filler Order Number: Item #217
   * - ``orc_4``
     - ORC.4
     - Optional[:ref:`EIP <hl7-v2_8_2-EIP>`]
     - optional
     - Placer Group Number: Item #218
   * - ``orc_5``
     - ORC.5
     - Optional[str]
     - optional
     - Order Status: Item #219 | Table HL70038
   * - ``orc_6``
     - ORC.6
     - Optional[str]
     - optional
     - Response Flag: Item #220 | Table HL70121
   * - ``orc_8``
     - ORC.8
     - Optional[:ref:`EIP <hl7-v2_8_2-EIP>`]
     - optional
     - Parent Order: Item #222
   * - ``orc_9``
     - ORC.9
     - Optional[str]
     - optional
     - Date/Time of Transaction: Item #223
   * - ``orc_10``
     - ORC.10
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Entered By: Item #224
   * - ``orc_11``
     - ORC.11
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Verified By: Item #225
   * - ``orc_12``
     - ORC.12
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Ordering Provider: Item #226
   * - ``orc_13``
     - ORC.13
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Enterer's Location: Item #227
   * - ``orc_14``
     - ORC.14
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Call Back Phone Number: Item #228
   * - ``orc_15``
     - ORC.15
     - Optional[str]
     - optional
     - Order Effective Date/Time: Item #229
   * - ``orc_16``
     - ORC.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Order Control Code Reason: Item #230 | Table HL79999
   * - ``orc_17``
     - ORC.17
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Entering Organization: Item #231 | Table HL79999
   * - ``orc_18``
     - ORC.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Entering Device: Item #232 | Table HL79999
   * - ``orc_19``
     - ORC.19
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Action By: Item #233
   * - ``orc_20``
     - ORC.20
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Advanced Beneficiary Notice Code: Item #1310 | Table HL70339
   * - ``orc_21``
     - ORC.21
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Ordering Facility Name: Item #1311
   * - ``orc_22``
     - ORC.22
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Ordering Facility Address: Item #1312
   * - ``orc_23``
     - ORC.23
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Ordering Facility Phone Number: Item #1313
   * - ``orc_24``
     - ORC.24
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Ordering Provider Address: Item #1314
   * - ``orc_25``
     - ORC.25
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Order Status Modifier: Item #1473 | Table HL79999
   * - ``orc_26``
     - ORC.26
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Advanced Beneficiary Notice Override Reason: Item #1641 | Table HL70552
   * - ``orc_27``
     - ORC.27
     - Optional[str]
     - optional
     - Filler's Expected Availability Date/Time: Item #1642
   * - ``orc_28``
     - ORC.28
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Confidentiality Code: Item #615 | Table HL70177
   * - ``orc_29``
     - ORC.29
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Order Type: Item #1643 | Table HL70482
   * - ``orc_30``
     - ORC.30
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Enterer Authorization Mode: Item #1644 | Table HL70483
   * - ``orc_31``
     - ORC.31
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Parent Universal Service Identifier: Item #2287
   * - ``orc_32``
     - ORC.32
     - Optional[str]
     - optional
     - Advanced Beneficiary Notice Date: Item #2301
   * - ``orc_33``
     - ORC.33
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Alternate Placer Order Number: Item #3300
   * - ``orc_34``
     - ORC.34
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Order Workflow Profile: Item #3387 | Table HL70934

.. _hl7-v2_8_2-ORG:

.. py:class:: hl7types.hl7.v2_8_2.segments.ORG.ORG
   :noindex:

   HL7 v2 ORG segment.

ORG
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``org_1``
     - ORG.1
     - str
     - required
     - Set ID - ORG: Item #1459
   * - ``org_2``
     - ORG.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Organization Unit Code: Item #1460 | Table HL70405
   * - ``org_3``
     - ORG.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Organization Unit Type Code: Item #1625 | Table HL70474
   * - ``org_4``
     - ORG.4
     - Optional[str]
     - optional
     - Primary Org Unit Indicator: Item #1462 | Table HL70136
   * - ``org_5``
     - ORG.5
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Practitioner Org Unit Identifier: Item #1463
   * - ``org_6``
     - ORG.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Health Care Provider Type Code: Item #1464 | Table HL70452
   * - ``org_7``
     - ORG.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Health Care Provider Classification Code: Item #1614 | Table HL70453
   * - ``org_8``
     - ORG.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Health Care Provider Area of Specialization Code: Item #1615 | Table HL70454
   * - ``org_9``
     - ORG.9
     - Optional[:ref:`DR <hl7-v2_8_2-DR>`]
     - optional
     - Effective Date Range: Item #1465
   * - ``org_10``
     - ORG.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Employment Status Code: Item #1276 | Table HL70066
   * - ``org_11``
     - ORG.11
     - Optional[str]
     - optional
     - Board Approval Indicator: Item #1467 | Table HL70136
   * - ``org_12``
     - ORG.12
     - Optional[str]
     - optional
     - Primary Care Physician Indicator: Item #1468 | Table HL70136
   * - ``org_13``
     - ORG.13
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Cost Center Code: Item #1891 | Table HL70539

.. _hl7-v2_8_2-OVR:

.. py:class:: hl7types.hl7.v2_8_2.segments.OVR.OVR
   :noindex:

   HL7 v2 OVR segment.

OVR
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ovr_1``
     - OVR.1
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Business Rule Override Type: Item #1829 | Table HL70518
   * - ``ovr_2``
     - OVR.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Business Rule Override Code: Item #1830 | Table HL70521
   * - ``ovr_3``
     - OVR.3
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Override Comments: Item #1831
   * - ``ovr_4``
     - OVR.4
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Override Entered By: Item #1832
   * - ``ovr_5``
     - OVR.5
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Override Authorized By: Item #1833

.. _hl7-v2_8_2-PAC:

.. py:class:: hl7types.hl7.v2_8_2.segments.PAC.PAC
   :noindex:

   HL7 v2 PAC segment.

PAC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pac_1``
     - PAC.1
     - str
     - required
     - Set Id - PAC: Item #2350
   * - ``pac_2``
     - PAC.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Package ID: Item #2351
   * - ``pac_3``
     - PAC.3
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Parent Package ID: Item #2352
   * - ``pac_4``
     - PAC.4
     - Optional[:ref:`NA <hl7-v2_8_2-NA>`]
     - optional
     - Position in Parent Package: Item #2353
   * - ``pac_5``
     - PAC.5
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Package Type: Item #2354 | Table HL70908
   * - ``pac_6``
     - PAC.6
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Package Condition: Item #2355 | Table HL70544
   * - ``pac_7``
     - PAC.7
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Package Handling Code: Item #2356 | Table HL70376
   * - ``pac_8``
     - PAC.8
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Package Risk Code: Item #2357 | Table HL70489

.. _hl7-v2_8_2-PCE:

.. py:class:: hl7types.hl7.v2_8_2.segments.PCE.PCE
   :noindex:

   HL7 v2 PCE segment.

PCE
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pce_1``
     - PCE.1
     - str
     - required
     - Set ID - PCE: Item #2228
   * - ``pce_2``
     - PCE.2
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Cost Center Account Number: Item #281 | Table HL70319
   * - ``pce_3``
     - PCE.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Transaction Code: Item #361 | Table HL70132
   * - ``pce_4``
     - PCE.4
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Transaction amount - unit: Item #366

.. _hl7-v2_8_2-PCR:

.. py:class:: hl7types.hl7.v2_8_2.segments.PCR.PCR
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
     - Description
   * - ``pcr_1``
     - PCR.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Implicated Product: Item #1098 | Table HL79999
   * - ``pcr_2``
     - PCR.2
     - Optional[str]
     - optional
     - Generic Product: Item #1099 | Table HL70249
   * - ``pcr_3``
     - PCR.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Product Class: Item #1100 | Table HL79999
   * - ``pcr_4``
     - PCR.4
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Total Duration Of Therapy: Item #1101
   * - ``pcr_5``
     - PCR.5
     - Optional[str]
     - optional
     - Product Manufacture Date: Item #1102
   * - ``pcr_6``
     - PCR.6
     - Optional[str]
     - optional
     - Product Expiration Date: Item #1103
   * - ``pcr_7``
     - PCR.7
     - Optional[str]
     - optional
     - Product Implantation Date: Item #1104
   * - ``pcr_8``
     - PCR.8
     - Optional[str]
     - optional
     - Product Explantation Date: Item #1105
   * - ``pcr_9``
     - PCR.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Single Use Device: Item #1106 | Table HL70244
   * - ``pcr_10``
     - PCR.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Indication For Product Use: Item #1107 | Table HL79999
   * - ``pcr_11``
     - PCR.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Product Problem: Item #1108 | Table HL70245
   * - ``pcr_12``
     - PCR.12
     - Optional[List[str]]
     - optional
     - Product Serial/Lot Number: Item #1109
   * - ``pcr_13``
     - PCR.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Product Available For Inspection: Item #1110 | Table HL70246
   * - ``pcr_14``
     - PCR.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Product Evaluation Performed: Item #1111 | Table HL79999
   * - ``pcr_15``
     - PCR.15
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Product Evaluation Status: Item #1112 | Table HL70247
   * - ``pcr_16``
     - PCR.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Product Evaluation Results: Item #1113 | Table HL79999
   * - ``pcr_17``
     - PCR.17
     - Optional[str]
     - optional
     - Evaluated Product Source: Item #1114 | Table HL70248
   * - ``pcr_18``
     - PCR.18
     - Optional[str]
     - optional
     - Date Product Returned To Manufacturer: Item #1115
   * - ``pcr_19``
     - PCR.19
     - Optional[str]
     - optional
     - Device Operator Qualifications: Item #1116 | Table HL70242
   * - ``pcr_20``
     - PCR.20
     - Optional[str]
     - optional
     - Relatedness Assessment: Item #1117 | Table HL70250
   * - ``pcr_21``
     - PCR.21
     - Optional[List[str]]
     - optional
     - Action Taken In Response To The Event: Item #1118 | Table HL70251
   * - ``pcr_22``
     - PCR.22
     - Optional[List[str]]
     - optional
     - Event Causality Observations: Item #1119 | Table HL70252
   * - ``pcr_23``
     - PCR.23
     - Optional[List[str]]
     - optional
     - Indirect Exposure Mechanism: Item #1120 | Table HL70253

.. _hl7-v2_8_2-PD1:

.. py:class:: hl7types.hl7.v2_8_2.segments.PD1.PD1
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
     - Description
   * - ``pd1_1``
     - PD1.1
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Living Dependency: Item #755 | Table HL70223
   * - ``pd1_2``
     - PD1.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Living Arrangement: Item #742 | Table HL70220
   * - ``pd1_3``
     - PD1.3
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Patient Primary Facility: Item #756 | Table HL70204
   * - ``pd1_5``
     - PD1.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Student Indicator: Item #745 | Table HL70231
   * - ``pd1_6``
     - PD1.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Handicap: Item #753 | Table HL70295
   * - ``pd1_7``
     - PD1.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Living Will Code: Item #759 | Table HL70315
   * - ``pd1_8``
     - PD1.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Organ Donor Code: Item #760 | Table HL70316
   * - ``pd1_9``
     - PD1.9
     - Optional[str]
     - optional
     - Separate Bill: Item #761 | Table HL70136
   * - ``pd1_10``
     - PD1.10
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Duplicate Patient: Item #762
   * - ``pd1_11``
     - PD1.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Publicity Code: Item #743 | Table HL70215
   * - ``pd1_12``
     - PD1.12
     - Optional[str]
     - optional
     - Protection Indicator: Item #744 | Table HL70136
   * - ``pd1_13``
     - PD1.13
     - Optional[str]
     - optional
     - Protection Indicator Effective Date: Item #1566
   * - ``pd1_14``
     - PD1.14
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Place of Worship: Item #1567
   * - ``pd1_15``
     - PD1.15
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Advance Directive Code: Item #1548 | Table HL70435
   * - ``pd1_16``
     - PD1.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Immunization Registry Status: Item #1569 | Table HL70441
   * - ``pd1_17``
     - PD1.17
     - Optional[str]
     - optional
     - Immunization Registry Status Effective Date: Item #1570
   * - ``pd1_18``
     - PD1.18
     - Optional[str]
     - optional
     - Publicity Code Effective Date: Item #1571
   * - ``pd1_19``
     - PD1.19
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Military Branch: Item #1572 | Table HL70140
   * - ``pd1_20``
     - PD1.20
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Military Rank/Grade: Item #486 | Table HL70141
   * - ``pd1_21``
     - PD1.21
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Military Status: Item #1573 | Table HL70142
   * - ``pd1_22``
     - PD1.22
     - Optional[str]
     - optional
     - Advance Directive Last Verified Date: Item #2141

.. _hl7-v2_8_2-PDA:

.. py:class:: hl7types.hl7.v2_8_2.segments.PDA.PDA
   :noindex:

   HL7 v2 PDA segment.

PDA
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pda_1``
     - PDA.1
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Death Cause Code: Item #1574
   * - ``pda_2``
     - PDA.2
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Death Location: Item #1575
   * - ``pda_3``
     - PDA.3
     - Optional[str]
     - optional
     - Death Certified Indicator: Item #1576 | Table HL70136
   * - ``pda_4``
     - PDA.4
     - Optional[str]
     - optional
     - Death Certificate Signed Date/Time: Item #1577
   * - ``pda_5``
     - PDA.5
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Death Certified By: Item #1578
   * - ``pda_6``
     - PDA.6
     - Optional[str]
     - optional
     - Autopsy Indicator: Item #1579 | Table HL70136
   * - ``pda_7``
     - PDA.7
     - Optional[:ref:`DR <hl7-v2_8_2-DR>`]
     - optional
     - Autopsy Start and End Date/Time: Item #1580
   * - ``pda_8``
     - PDA.8
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Autopsy Performed By: Item #1581
   * - ``pda_9``
     - PDA.9
     - Optional[str]
     - optional
     - Coroner Indicator: Item #1582 | Table HL70136

.. _hl7-v2_8_2-PDC:

.. py:class:: hl7types.hl7.v2_8_2.segments.PDC.PDC
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
     - Description
   * - ``pdc_1``
     - PDC.1
     - List[:ref:`XON <hl7-v2_8_2-XON>`]
     - required
     - Manufacturer/Distributor: Item #1247
   * - ``pdc_2``
     - PDC.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Country: Item #1248 | Table HL79999
   * - ``pdc_3``
     - PDC.3
     - str
     - required
     - Brand Name: Item #1249
   * - ``pdc_4``
     - PDC.4
     - Optional[str]
     - optional
     - Device Family Name: Item #1250
   * - ``pdc_5``
     - PDC.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Generic Name: Item #1251 | Table HL79999
   * - ``pdc_6``
     - PDC.6
     - Optional[List[str]]
     - optional
     - Model Identifier: Item #1252
   * - ``pdc_7``
     - PDC.7
     - Optional[str]
     - optional
     - Catalogue Identifier: Item #1253
   * - ``pdc_8``
     - PDC.8
     - Optional[List[str]]
     - optional
     - Other Identifier: Item #1254
   * - ``pdc_9``
     - PDC.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Product Code: Item #1255 | Table HL79999
   * - ``pdc_10``
     - PDC.10
     - Optional[str]
     - optional
     - Marketing Basis: Item #1256 | Table HL70330
   * - ``pdc_11``
     - PDC.11
     - Optional[str]
     - optional
     - Marketing Approval ID: Item #1257
   * - ``pdc_12``
     - PDC.12
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Labeled Shelf Life: Item #1258
   * - ``pdc_13``
     - PDC.13
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Expected Shelf Life: Item #1259
   * - ``pdc_14``
     - PDC.14
     - Optional[str]
     - optional
     - Date First Marketed: Item #1260
   * - ``pdc_15``
     - PDC.15
     - Optional[str]
     - optional
     - Date Last Marketed: Item #1261

.. _hl7-v2_8_2-PEO:

.. py:class:: hl7types.hl7.v2_8_2.segments.PEO.PEO
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
     - Description
   * - ``peo_1``
     - PEO.1
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Event Identifiers Used: Item #1073 | Table HL79999
   * - ``peo_2``
     - PEO.2
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Event Symptom/Diagnosis Code: Item #1074 | Table HL79999
   * - ``peo_3``
     - PEO.3
     - str
     - required
     - Event Onset Date/Time: Item #1075
   * - ``peo_4``
     - PEO.4
     - Optional[str]
     - optional
     - Event Exacerbation Date/Time: Item #1076
   * - ``peo_5``
     - PEO.5
     - Optional[str]
     - optional
     - Event Improved Date/Time: Item #1077
   * - ``peo_6``
     - PEO.6
     - Optional[str]
     - optional
     - Event Ended Data/Time: Item #1078
   * - ``peo_7``
     - PEO.7
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Event Location Occurred Address: Item #1079
   * - ``peo_8``
     - PEO.8
     - Optional[List[str]]
     - optional
     - Event Qualification: Item #1080 | Table HL70237
   * - ``peo_9``
     - PEO.9
     - Optional[str]
     - optional
     - Event Serious: Item #1081 | Table HL70238
   * - ``peo_10``
     - PEO.10
     - Optional[str]
     - optional
     - Event Expected: Item #1082 | Table HL70239
   * - ``peo_11``
     - PEO.11
     - Optional[List[str]]
     - optional
     - Event Outcome: Item #1083 | Table HL70240
   * - ``peo_12``
     - PEO.12
     - Optional[str]
     - optional
     - Patient Outcome: Item #1084 | Table HL70241
   * - ``peo_13``
     - PEO.13
     - Optional[List[:ref:`FT <hl7-v2_8_2-FT>`]]
     - optional
     - Event Description from Others: Item #1085
   * - ``peo_14``
     - PEO.14
     - Optional[List[:ref:`FT <hl7-v2_8_2-FT>`]]
     - optional
     - Event Description from Original Reporter: Item #1086
   * - ``peo_15``
     - PEO.15
     - Optional[List[:ref:`FT <hl7-v2_8_2-FT>`]]
     - optional
     - Event Description from Patient: Item #1087
   * - ``peo_16``
     - PEO.16
     - Optional[List[:ref:`FT <hl7-v2_8_2-FT>`]]
     - optional
     - Event Description from Practitioner: Item #1088
   * - ``peo_17``
     - PEO.17
     - Optional[List[:ref:`FT <hl7-v2_8_2-FT>`]]
     - optional
     - Event Description from Autopsy: Item #1089
   * - ``peo_18``
     - PEO.18
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Cause Of Death: Item #1090 | Table HL79999
   * - ``peo_19``
     - PEO.19
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Primary Observer Name: Item #1091
   * - ``peo_20``
     - PEO.20
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Primary Observer Address: Item #1092
   * - ``peo_21``
     - PEO.21
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Primary Observer Telephone: Item #1093
   * - ``peo_22``
     - PEO.22
     - Optional[str]
     - optional
     - Primary Observer's Qualification: Item #1094 | Table HL70242
   * - ``peo_23``
     - PEO.23
     - Optional[str]
     - optional
     - Confirmation Provided By: Item #1095 | Table HL70242
   * - ``peo_24``
     - PEO.24
     - Optional[str]
     - optional
     - Primary Observer Aware Date/Time: Item #1096
   * - ``peo_25``
     - PEO.25
     - Optional[str]
     - optional
     - Primary Observer's identity May Be Divulged: Item #1097 | Table HL70243

.. _hl7-v2_8_2-PES:

.. py:class:: hl7types.hl7.v2_8_2.segments.PES.PES
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
     - Description
   * - ``pes_1``
     - PES.1
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Sender Organization Name: Item #1059
   * - ``pes_2``
     - PES.2
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Sender Individual Name: Item #1060
   * - ``pes_3``
     - PES.3
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Sender Address: Item #1062
   * - ``pes_4``
     - PES.4
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Sender Telephone: Item #1063
   * - ``pes_5``
     - PES.5
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Sender Event Identifier: Item #1064
   * - ``pes_6``
     - PES.6
     - Optional[str]
     - optional
     - Sender Sequence Number: Item #1065
   * - ``pes_7``
     - PES.7
     - Optional[List[:ref:`FT <hl7-v2_8_2-FT>`]]
     - optional
     - Sender Event Description: Item #1066
   * - ``pes_8``
     - PES.8
     - Optional[:ref:`FT <hl7-v2_8_2-FT>`]
     - optional
     - Sender Comment: Item #1067
   * - ``pes_9``
     - PES.9
     - Optional[str]
     - optional
     - Sender Aware Date/Time: Item #1068
   * - ``pes_10``
     - PES.10
     - str
     - required
     - Event Report Date: Item #1069
   * - ``pes_11``
     - PES.11
     - Optional[List[str]]
     - optional
     - Event Report Timing/Type: Item #1070 | Table HL70234
   * - ``pes_12``
     - PES.12
     - Optional[str]
     - optional
     - Event Report Source: Item #1071 | Table HL70235
   * - ``pes_13``
     - PES.13
     - Optional[List[str]]
     - optional
     - Event Reported To: Item #1072 | Table HL70236

.. _hl7-v2_8_2-PID:

.. py:class:: hl7types.hl7.v2_8_2.segments.PID.PID
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
     - Description
   * - ``pid_1``
     - PID.1
     - Optional[str]
     - optional
     - Set ID - PID: Item #104
   * - ``pid_3``
     - PID.3
     - List[:ref:`CX <hl7-v2_8_2-CX>`]
     - required
     - Patient Identifier List: Item #106
   * - ``pid_5``
     - PID.5
     - List[:ref:`XPN <hl7-v2_8_2-XPN>`]
     - required
     - Patient Name: Item #108 | Table HL70200
   * - ``pid_6``
     - PID.6
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Mother's Maiden Name: Item #109
   * - ``pid_7``
     - PID.7
     - Optional[str]
     - optional
     - Date/Time of Birth: Item #110
   * - ``pid_8``
     - PID.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Administrative Sex: Item #111 | Table HL70001
   * - ``pid_10``
     - PID.10
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Race: Item #113 | Table HL70005
   * - ``pid_11``
     - PID.11
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Patient Address: Item #114
   * - ``pid_13``
     - PID.13
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Phone Number - Home: Item #116
   * - ``pid_14``
     - PID.14
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Phone Number - Business: Item #117
   * - ``pid_15``
     - PID.15
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Primary Language: Item #118 | Table HL70296
   * - ``pid_16``
     - PID.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Marital Status: Item #119 | Table HL70002
   * - ``pid_17``
     - PID.17
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Religion: Item #120 | Table HL70006
   * - ``pid_18``
     - PID.18
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Patient Account Number: Item #121
   * - ``pid_21``
     - PID.21
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Mother's Identifier: Item #124
   * - ``pid_22``
     - PID.22
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Ethnic Group: Item #125 | Table HL70189
   * - ``pid_23``
     - PID.23
     - Optional[str]
     - optional
     - Birth Place: Item #126
   * - ``pid_24``
     - PID.24
     - Optional[str]
     - optional
     - Multiple Birth Indicator: Item #127 | Table HL70136
   * - ``pid_25``
     - PID.25
     - Optional[str]
     - optional
     - Birth Order: Item #128
   * - ``pid_26``
     - PID.26
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Citizenship: Item #129 | Table HL70171
   * - ``pid_27``
     - PID.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Veterans Military Status: Item #130 | Table HL70172
   * - ``pid_29``
     - PID.29
     - Optional[str]
     - optional
     - Patient Death Date and Time: Item #740
   * - ``pid_30``
     - PID.30
     - Optional[str]
     - optional
     - Patient Death Indicator: Item #741 | Table HL70136
   * - ``pid_31``
     - PID.31
     - Optional[str]
     - optional
     - Identity Unknown Indicator: Item #1535 | Table HL70136
   * - ``pid_32``
     - PID.32
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Identity Reliability Code: Item #1536 | Table HL70445
   * - ``pid_33``
     - PID.33
     - Optional[str]
     - optional
     - Last Update Date/Time: Item #1537
   * - ``pid_34``
     - PID.34
     - Optional[:ref:`HD <hl7-v2_8_2-HD>`]
     - optional
     - Last Update Facility: Item #1538
   * - ``pid_35``
     - PID.35
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Taxonomic Classification Code: Item #1539
   * - ``pid_36``
     - PID.36
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Breed Code: Item #1540 | Table HL70447
   * - ``pid_37``
     - PID.37
     - Optional[str]
     - optional
     - Strain: Item #1541
   * - ``pid_38``
     - PID.38
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Production Class Code: Item #1542 | Table HL70429
   * - ``pid_39``
     - PID.39
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Tribal Citizenship: Item #1840 | Table HL70171
   * - ``pid_40``
     - PID.40
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Patient Telecommunication Information: Item #2289

.. _hl7-v2_8_2-PKG:

.. py:class:: hl7types.hl7.v2_8_2.segments.PKG.PKG
   :noindex:

   HL7 v2 PKG segment.

PKG
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pkg_1``
     - PKG.1
     - str
     - required
     - Set Id - PKG: Item #2221
   * - ``pkg_2``
     - PKG.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Packaging Units: Item #2222 | Table HL70818
   * - ``pkg_3``
     - PKG.3
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Default Order Unit Of Measure Indicator: Item #2223 | Table HL70532
   * - ``pkg_4``
     - PKG.4
     - Optional[str]
     - optional
     - Package Quantity: Item #2224
   * - ``pkg_5``
     - PKG.5
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Price: Item #2225
   * - ``pkg_6``
     - PKG.6
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Future Item Price: Item #2226
   * - ``pkg_7``
     - PKG.7
     - Optional[str]
     - optional
     - Future Item Price Effective Date: Item #2227
   * - ``pkg_8``
     - PKG.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Global Trade Item Number: Item #3307

.. _hl7-v2_8_2-PM1:

.. py:class:: hl7types.hl7.v2_8_2.segments.PM1.PM1
   :noindex:

   HL7 v2 PM1 segment.

PM1
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pm1_1``
     - PM1.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Health Plan ID: Item #368 | Table HL70072
   * - ``pm1_2``
     - PM1.2
     - List[:ref:`CX <hl7-v2_8_2-CX>`]
     - required
     - Insurance Company ID: Item #428
   * - ``pm1_3``
     - PM1.3
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Insurance Company Name: Item #429
   * - ``pm1_4``
     - PM1.4
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Insurance Company Address: Item #430
   * - ``pm1_5``
     - PM1.5
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Insurance Co Contact Person: Item #431
   * - ``pm1_6``
     - PM1.6
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Insurance Co Phone Number: Item #432
   * - ``pm1_7``
     - PM1.7
     - Optional[str]
     - optional
     - Group Number: Item #433
   * - ``pm1_8``
     - PM1.8
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Group Name: Item #434
   * - ``pm1_9``
     - PM1.9
     - Optional[str]
     - optional
     - Plan Effective Date: Item #437
   * - ``pm1_10``
     - PM1.10
     - Optional[str]
     - optional
     - Plan Expiration Date: Item #438
   * - ``pm1_11``
     - PM1.11
     - Optional[str]
     - optional
     - Patient DOB Required: Item #3454 | Table HL70136
   * - ``pm1_12``
     - PM1.12
     - Optional[str]
     - optional
     - Patient Gender Required: Item #3455 | Table HL70136
   * - ``pm1_13``
     - PM1.13
     - Optional[str]
     - optional
     - Patient Relationship Required: Item #3456 | Table HL70136
   * - ``pm1_14``
     - PM1.14
     - Optional[str]
     - optional
     - Patient Signature Required: Item #3457 | Table HL70136
   * - ``pm1_15``
     - PM1.15
     - Optional[str]
     - optional
     - Diagnosis Required: Item #3458 | Table HL70136
   * - ``pm1_16``
     - PM1.16
     - Optional[str]
     - optional
     - Service Required: Item #3459 | Table HL70136
   * - ``pm1_17``
     - PM1.17
     - Optional[str]
     - optional
     - Patient Name Required: Item #3460 | Table HL70136
   * - ``pm1_18``
     - PM1.18
     - Optional[str]
     - optional
     - Patient Address Required: Item #3461 | Table HL70136
   * - ``pm1_19``
     - PM1.19
     - Optional[str]
     - optional
     - Subscribers Name Required: Item #3462 | Table HL70136
   * - ``pm1_20``
     - PM1.20
     - Optional[str]
     - optional
     - Workman's Comp Indicator: Item #3463 | Table HL70136
   * - ``pm1_21``
     - PM1.21
     - Optional[str]
     - optional
     - Bill Type Required: Item #3464 | Table HL70136
   * - ``pm1_22``
     - PM1.22
     - Optional[str]
     - optional
     - Commercial Carrier Name and Address Required: Item #3465 | Table HL70136
   * - ``pm1_23``
     - PM1.23
     - Optional[str]
     - optional
     - Policy Number Pattern: Item #3466
   * - ``pm1_24``
     - PM1.24
     - Optional[str]
     - optional
     - Group Number Pattern: Item #3467

.. _hl7-v2_8_2-PMT:

.. py:class:: hl7types.hl7.v2_8_2.segments.PMT.PMT
   :noindex:

   HL7 v2 PMT segment.

PMT
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pmt_1``
     - PMT.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Payment/Remittance Advice Number: Item #2018
   * - ``pmt_2``
     - PMT.2
     - str
     - required
     - Payment/Remittance Effective Date/Time: Item #2019
   * - ``pmt_3``
     - PMT.3
     - str
     - required
     - Payment/Remittance Expiration Date/Time: Item #2020
   * - ``pmt_4``
     - PMT.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Payment Method: Item #2021 | Table HL70570
   * - ``pmt_5``
     - PMT.5
     - str
     - required
     - Payment/Remittance Date/Time: Item #2022
   * - ``pmt_6``
     - PMT.6
     - :ref:`CP <hl7-v2_8_2-CP>`
     - required
     - Payment/Remittance Amount: Item #2023
   * - ``pmt_7``
     - PMT.7
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Check Number: Item #2024
   * - ``pmt_8``
     - PMT.8
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Payee Bank Identification: Item #2025
   * - ``pmt_9``
     - PMT.9
     - Optional[str]
     - optional
     - Payee Transit Number: Item #2026
   * - ``pmt_10``
     - PMT.10
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Payee Bank Account ID: Item #2027
   * - ``pmt_11``
     - PMT.11
     - :ref:`XON <hl7-v2_8_2-XON>`
     - required
     - Payment Organization: Item #2028
   * - ``pmt_12``
     - PMT.12
     - Optional[str]
     - optional
     - ESR-Code-Line: Item #2029

.. _hl7-v2_8_2-PR1:

.. py:class:: hl7types.hl7.v2_8_2.segments.PR1.PR1
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
     - Description
   * - ``pr1_1``
     - PR1.1
     - str
     - required
     - Set ID - PR1: Item #391
   * - ``pr1_3``
     - PR1.3
     - :ref:`CNE <hl7-v2_8_2-CNE>`
     - required
     - Procedure Code: Item #393 | Table HL70088
   * - ``pr1_5``
     - PR1.5
     - str
     - required
     - Procedure Date/Time: Item #395
   * - ``pr1_6``
     - PR1.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Procedure Functional Type: Item #396 | Table HL70230
   * - ``pr1_7``
     - PR1.7
     - Optional[str]
     - optional
     - Procedure Minutes: Item #397
   * - ``pr1_9``
     - PR1.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Anesthesia Code: Item #399 | Table HL70019
   * - ``pr1_10``
     - PR1.10
     - Optional[str]
     - optional
     - Anesthesia Minutes: Item #400
   * - ``pr1_13``
     - PR1.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Consent Code: Item #403 | Table HL70059
   * - ``pr1_14``
     - PR1.14
     - Optional[str]
     - optional
     - Procedure Priority: Item #404 | Table HL70418
   * - ``pr1_15``
     - PR1.15
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Associated Diagnosis Code: Item #772 | Table HL70051
   * - ``pr1_16``
     - PR1.16
     - Optional[List[:ref:`CNE <hl7-v2_8_2-CNE>`]]
     - optional
     - Procedure Code Modifier: Item #1316 | Table HL70340
   * - ``pr1_17``
     - PR1.17
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Procedure DRG Type: Item #1501 | Table HL70416
   * - ``pr1_18``
     - PR1.18
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Tissue Type Code: Item #1502 | Table HL70417
   * - ``pr1_19``
     - PR1.19
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Procedure Identifier: Item #1848
   * - ``pr1_20``
     - PR1.20
     - Optional[str]
     - optional
     - Procedure Action Code: Item #1849 | Table HL70206
   * - ``pr1_21``
     - PR1.21
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - DRG Procedure Determination Status: Item #2177 | Table HL70761
   * - ``pr1_22``
     - PR1.22
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - DRG Procedure Relevance: Item #2178 | Table HL70763
   * - ``pr1_23``
     - PR1.23
     - Optional[List[:ref:`PL <hl7-v2_8_2-PL>`]]
     - optional
     - Treating Organizational Unit: Item #2371
   * - ``pr1_24``
     - PR1.24
     - Optional[str]
     - optional
     - Respiratory Within Surgery: Item #2372 | Table HL70136
   * - ``pr1_25``
     - PR1.25
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Parent Procedure ID: Item #2373

.. _hl7-v2_8_2-PRA:

.. py:class:: hl7types.hl7.v2_8_2.segments.PRA.PRA
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
     - Description
   * - ``pra_1``
     - PRA.1
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Primary Key Value - PRA: Item #685 | Table HL79999
   * - ``pra_2``
     - PRA.2
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Practitioner Group: Item #686 | Table HL70358
   * - ``pra_3``
     - PRA.3
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Practitioner Category: Item #687 | Table HL70186
   * - ``pra_4``
     - PRA.4
     - Optional[str]
     - optional
     - Provider Billing: Item #688 | Table HL70187
   * - ``pra_5``
     - PRA.5
     - Optional[List[:ref:`SPD <hl7-v2_8_2-SPD>`]]
     - optional
     - Specialty: Item #689 | Table HL70337
   * - ``pra_6``
     - PRA.6
     - Optional[List[:ref:`PLN <hl7-v2_8_2-PLN>`]]
     - optional
     - Practitioner ID Numbers: Item #690 | Table HL70338
   * - ``pra_7``
     - PRA.7
     - Optional[List[:ref:`PIP <hl7-v2_8_2-PIP>`]]
     - optional
     - Privileges: Item #691
   * - ``pra_8``
     - PRA.8
     - Optional[str]
     - optional
     - Date Entered Practice: Item #1296
   * - ``pra_9``
     - PRA.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Institution: Item #1613 | Table HL70537
   * - ``pra_10``
     - PRA.10
     - Optional[str]
     - optional
     - Date Left Practice: Item #1348
   * - ``pra_11``
     - PRA.11
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Government Reimbursement Billing Eligibility: Item #1388 | Table HL70401
   * - ``pra_12``
     - PRA.12
     - Optional[str]
     - optional
     - Set ID - PRA: Item #1616

.. _hl7-v2_8_2-PRB:

.. py:class:: hl7types.hl7.v2_8_2.segments.PRB.PRB
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
     - Description
   * - ``prb_1``
     - PRB.1
     - str
     - required
     - Action Code: Item #816 | Table HL70206
   * - ``prb_2``
     - PRB.2
     - str
     - required
     - Action Date/Time: Item #817
   * - ``prb_3``
     - PRB.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Problem ID: Item #838
   * - ``prb_4``
     - PRB.4
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Problem Instance ID: Item #839
   * - ``prb_5``
     - PRB.5
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Episode of Care ID: Item #820
   * - ``prb_6``
     - PRB.6
     - Optional[str]
     - optional
     - Problem List Priority: Item #841
   * - ``prb_7``
     - PRB.7
     - Optional[str]
     - optional
     - Problem Established Date/Time: Item #842
   * - ``prb_8``
     - PRB.8
     - Optional[str]
     - optional
     - Anticipated Problem Resolution Date/Time: Item #843
   * - ``prb_9``
     - PRB.9
     - Optional[str]
     - optional
     - Actual Problem Resolution Date/Time: Item #844
   * - ``prb_10``
     - PRB.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Problem Classification: Item #845
   * - ``prb_11``
     - PRB.11
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Problem Management Discipline: Item #846
   * - ``prb_12``
     - PRB.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Problem Persistence: Item #847
   * - ``prb_13``
     - PRB.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Problem Confirmation Status: Item #848
   * - ``prb_14``
     - PRB.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Problem Life Cycle Status: Item #849
   * - ``prb_15``
     - PRB.15
     - Optional[str]
     - optional
     - Problem Life Cycle Status Date/Time: Item #850
   * - ``prb_16``
     - PRB.16
     - Optional[str]
     - optional
     - Problem Date of Onset: Item #851
   * - ``prb_17``
     - PRB.17
     - Optional[str]
     - optional
     - Problem Onset Text: Item #852
   * - ``prb_18``
     - PRB.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Problem Ranking: Item #853
   * - ``prb_19``
     - PRB.19
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Certainty of Problem: Item #854
   * - ``prb_20``
     - PRB.20
     - Optional[str]
     - optional
     - Probability of Problem (0-1): Item #855
   * - ``prb_21``
     - PRB.21
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Individual Awareness of Problem: Item #856
   * - ``prb_22``
     - PRB.22
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Problem Prognosis: Item #857
   * - ``prb_23``
     - PRB.23
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Individual Awareness of Prognosis: Item #858
   * - ``prb_24``
     - PRB.24
     - Optional[str]
     - optional
     - Family/Significant Other Awareness of Problem/Prognosis: Item #859
   * - ``prb_25``
     - PRB.25
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Security/Sensitivity: Item #823
   * - ``prb_26``
     - PRB.26
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Problem Severity: Item #2234 | Table HL70836
   * - ``prb_27``
     - PRB.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Problem Perspective: Item #2235 | Table HL70838
   * - ``prb_28``
     - PRB.28
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Mood Code: Item #2237 | Table HL70725

.. _hl7-v2_8_2-PRC:

.. py:class:: hl7types.hl7.v2_8_2.segments.PRC.PRC
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
     - Description
   * - ``prc_1``
     - PRC.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Primary Key Value - PRC: Item #982 | Table HL70132
   * - ``prc_2``
     - PRC.2
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Facility ID - PRC: Item #995 | Table HL70464
   * - ``prc_3``
     - PRC.3
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Department: Item #676 | Table HL70184
   * - ``prc_4``
     - PRC.4
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Valid Patient Classes: Item #967 | Table HL70004
   * - ``prc_5``
     - PRC.5
     - Optional[List[:ref:`CP <hl7-v2_8_2-CP>`]]
     - optional
     - Price: Item #998
   * - ``prc_6``
     - PRC.6
     - Optional[List[str]]
     - optional
     - Formula: Item #999
   * - ``prc_7``
     - PRC.7
     - Optional[str]
     - optional
     - Minimum Quantity: Item #1000
   * - ``prc_8``
     - PRC.8
     - Optional[str]
     - optional
     - Maximum Quantity: Item #1001
   * - ``prc_9``
     - PRC.9
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Minimum Price: Item #1002
   * - ``prc_10``
     - PRC.10
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Maximum Price: Item #1003
   * - ``prc_11``
     - PRC.11
     - Optional[str]
     - optional
     - Effective Start Date: Item #1004
   * - ``prc_12``
     - PRC.12
     - Optional[str]
     - optional
     - Effective End Date: Item #1005
   * - ``prc_13``
     - PRC.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Price Override Flag: Item #1006 | Table HL70268
   * - ``prc_14``
     - PRC.14
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Billing Category: Item #1007 | Table HL70293
   * - ``prc_15``
     - PRC.15
     - Optional[str]
     - optional
     - Chargeable Flag: Item #1008 | Table HL70136
   * - ``prc_16``
     - PRC.16
     - Optional[str]
     - optional
     - Active/Inactive Flag: Item #675 | Table HL70183
   * - ``prc_17``
     - PRC.17
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Cost: Item #989
   * - ``prc_18``
     - PRC.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Charge on Indicator: Item #1009 | Table HL70269

.. _hl7-v2_8_2-PRD:

.. py:class:: hl7types.hl7.v2_8_2.segments.PRD.PRD
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
     - Description
   * - ``prd_1``
     - PRD.1
     - List[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - required
     - Provider Role: Item #1155 | Table HL70286
   * - ``prd_2``
     - PRD.2
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Provider Name: Item #1156
   * - ``prd_3``
     - PRD.3
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Provider Address: Item #1157
   * - ``prd_4``
     - PRD.4
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Provider Location: Item #1158
   * - ``prd_5``
     - PRD.5
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Provider Communication Information: Item #1159
   * - ``prd_6``
     - PRD.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Preferred Method of Contact: Item #684 | Table HL70185
   * - ``prd_7``
     - PRD.7
     - Optional[List[:ref:`PLN <hl7-v2_8_2-PLN>`]]
     - optional
     - Provider Identifiers: Item #1162 | Table HL70338
   * - ``prd_8``
     - PRD.8
     - Optional[str]
     - optional
     - Effective Start Date of Provider Role: Item #1163
   * - ``prd_9``
     - PRD.9
     - Optional[List[str]]
     - optional
     - Effective End Date of Provider Role: Item #1164
   * - ``prd_10``
     - PRD.10
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Provider Organization Name and Identifier: Item #2256
   * - ``prd_11``
     - PRD.11
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Provider Organization Address: Item #2257
   * - ``prd_12``
     - PRD.12
     - Optional[List[:ref:`PL <hl7-v2_8_2-PL>`]]
     - optional
     - Provider Organization Location Information: Item #2258
   * - ``prd_13``
     - PRD.13
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Provider Organization Communication Information: Item #2259
   * - ``prd_14``
     - PRD.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Provider Organization Method of Contact: Item #2260 | Table HL70185

.. _hl7-v2_8_2-PRT:

.. py:class:: hl7types.hl7.v2_8_2.segments.PRT.PRT
   :noindex:

   HL7 v2 PRT segment.

PRT
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``prt_1``
     - PRT.1
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Participation Instance ID: Item #2379
   * - ``prt_2``
     - PRT.2
     - str
     - required
     - Action Code: Item #816 | Table HL70206
   * - ``prt_3``
     - PRT.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Action Reason: Item #2380
   * - ``prt_4``
     - PRT.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Participation: Item #2381 | Table HL70912
   * - ``prt_5``
     - PRT.5
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Participation Person: Item #2382
   * - ``prt_6``
     - PRT.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Participation Person Provider Type: Item #2383
   * - ``prt_7``
     - PRT.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Participant Organization Unit Type: Item #2384 | Table HL70406
   * - ``prt_8``
     - PRT.8
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Participation Organization: Item #2385
   * - ``prt_9``
     - PRT.9
     - Optional[List[:ref:`PL <hl7-v2_8_2-PL>`]]
     - optional
     - Participant Location: Item #2386
   * - ``prt_10``
     - PRT.10
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Participation Device: Item #2348
   * - ``prt_11``
     - PRT.11
     - Optional[str]
     - optional
     - Participation Begin Date/Time (arrival time): Item #2387
   * - ``prt_12``
     - PRT.12
     - Optional[str]
     - optional
     - Participation End Date/Time (departure time): Item #2388
   * - ``prt_13``
     - PRT.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Participation Qualitative Duration: Item #2389
   * - ``prt_14``
     - PRT.14
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Participation Address: Item #2390
   * - ``prt_15``
     - PRT.15
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Participant Telecommunication Address: Item #2391
   * - ``prt_16``
     - PRT.16
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Participant Device Identifier: Item #3476
   * - ``prt_17``
     - PRT.17
     - Optional[str]
     - optional
     - Participant Device Manufacture Date: Item #3477
   * - ``prt_18``
     - PRT.18
     - Optional[str]
     - optional
     - Participant Device Expiry Date: Item #3478
   * - ``prt_19``
     - PRT.19
     - Optional[str]
     - optional
     - Participant Device Lot Number: Item #3479
   * - ``prt_20``
     - PRT.20
     - Optional[str]
     - optional
     - Participant Device Serial Number: Item #3480
   * - ``prt_21``
     - PRT.21
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Participant Device Donation Identification: Item #3481
   * - ``prt_22``
     - PRT.22
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Participation Device Type: Item #3483

.. _hl7-v2_8_2-PSG:

.. py:class:: hl7types.hl7.v2_8_2.segments.PSG.PSG
   :noindex:

   HL7 v2 PSG segment.

PSG
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``psg_1``
     - PSG.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Provider Product/Service Group Number: Item #1950
   * - ``psg_2``
     - PSG.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Payer Product/Service Group Number: Item #1951
   * - ``psg_3``
     - PSG.3
     - str
     - required
     - Product/Service Group Sequence Number: Item #1952
   * - ``psg_4``
     - PSG.4
     - str
     - required
     - Adjudicate as Group: Item #1953 | Table HL70136
   * - ``psg_5``
     - PSG.5
     - :ref:`CP <hl7-v2_8_2-CP>`
     - required
     - Product/Service Group Billed Amount: Item #1954
   * - ``psg_6``
     - PSG.6
     - str
     - required
     - Product/Service Group Description: Item #2044

.. _hl7-v2_8_2-PSH:

.. py:class:: hl7types.hl7.v2_8_2.segments.PSH.PSH
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
     - Description
   * - ``psh_1``
     - PSH.1
     - str
     - required
     - Report Type: Item #1233
   * - ``psh_2``
     - PSH.2
     - Optional[str]
     - optional
     - Report Form Identifier: Item #1297
   * - ``psh_3``
     - PSH.3
     - str
     - required
     - Report Date: Item #1235
   * - ``psh_4``
     - PSH.4
     - Optional[str]
     - optional
     - Report Interval Start Date: Item #1236
   * - ``psh_5``
     - PSH.5
     - Optional[str]
     - optional
     - Report Interval End Date: Item #1237
   * - ``psh_6``
     - PSH.6
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Quantity Manufactured: Item #1238
   * - ``psh_7``
     - PSH.7
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Quantity Distributed: Item #1239
   * - ``psh_8``
     - PSH.8
     - Optional[str]
     - optional
     - Quantity Distributed Method: Item #1240 | Table HL70329
   * - ``psh_9``
     - PSH.9
     - Optional[:ref:`FT <hl7-v2_8_2-FT>`]
     - optional
     - Quantity Distributed Comment: Item #1241
   * - ``psh_10``
     - PSH.10
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Quantity in Use: Item #1242
   * - ``psh_11``
     - PSH.11
     - Optional[str]
     - optional
     - Quantity in Use Method: Item #1243 | Table HL70329
   * - ``psh_12``
     - PSH.12
     - Optional[:ref:`FT <hl7-v2_8_2-FT>`]
     - optional
     - Quantity in Use Comment: Item #1244
   * - ``psh_13``
     - PSH.13
     - Optional[List[str]]
     - optional
     - Number of Product Experience Reports Filed by Facility: Item #1245
   * - ``psh_14``
     - PSH.14
     - Optional[List[str]]
     - optional
     - Number of Product Experience Reports Filed by Distributor: Item #1246

.. _hl7-v2_8_2-PSL:

.. py:class:: hl7types.hl7.v2_8_2.segments.PSL.PSL
   :noindex:

   HL7 v2 PSL segment.

PSL
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``psl_1``
     - PSL.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Provider Product/Service Line Item Number: Item #1955
   * - ``psl_2``
     - PSL.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Payer Product/Service Line Item Number: Item #1956
   * - ``psl_3``
     - PSL.3
     - str
     - required
     - Product/Service Line Item Sequence Number: Item #1957
   * - ``psl_4``
     - PSL.4
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Provider Tracking ID: Item #1958
   * - ``psl_5``
     - PSL.5
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Payer Tracking ID: Item #1959
   * - ``psl_6``
     - PSL.6
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Product/Service Line Item Status: Item #1960 | Table HL70559
   * - ``psl_7``
     - PSL.7
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Product/Service Code: Item #1961 | Table HL70879
   * - ``psl_8``
     - PSL.8
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Product/Service Code Modifier: Item #1962 | Table HL70880
   * - ``psl_9``
     - PSL.9
     - Optional[str]
     - optional
     - Product/Service Code Description: Item #1963
   * - ``psl_10``
     - PSL.10
     - Optional[str]
     - optional
     - Product/Service Effective Date: Item #1964
   * - ``psl_11``
     - PSL.11
     - Optional[str]
     - optional
     - Product/Service Expiration Date: Item #1965
   * - ``psl_12``
     - PSL.12
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Product/Service Quantity: Item #1966 | Table HL70560
   * - ``psl_13``
     - PSL.13
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Product/Service Unit Cost: Item #1967
   * - ``psl_14``
     - PSL.14
     - Optional[str]
     - optional
     - Number of Items per Unit: Item #1968
   * - ``psl_15``
     - PSL.15
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Product/Service Gross Amount: Item #1969
   * - ``psl_16``
     - PSL.16
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Product/Service Billed Amount: Item #1970
   * - ``psl_17``
     - PSL.17
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Product/Service Clarification Code Type: Item #1971 | Table HL70561
   * - ``psl_18``
     - PSL.18
     - Optional[List[str]]
     - optional
     - Product/Service Clarification Code Value: Item #1972
   * - ``psl_19``
     - PSL.19
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Health Document Reference Identifier: Item #1973
   * - ``psl_20``
     - PSL.20
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Processing Consideration Code: Item #1974 | Table HL70562
   * - ``psl_21``
     - PSL.21
     - str
     - required
     - Restricted Disclosure Indicator: Item #1975 | Table HL70532
   * - ``psl_22``
     - PSL.22
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Related Product/Service Code Indicator: Item #1976 | Table HL70879
   * - ``psl_23``
     - PSL.23
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Product/Service Amount for Physician: Item #1977
   * - ``psl_24``
     - PSL.24
     - Optional[str]
     - optional
     - Product/Service Cost Factor: Item #1978
   * - ``psl_25``
     - PSL.25
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Cost Center: Item #1933
   * - ``psl_26``
     - PSL.26
     - Optional[:ref:`DR <hl7-v2_8_2-DR>`]
     - optional
     - Billing Period: Item #1980
   * - ``psl_27``
     - PSL.27
     - Optional[str]
     - optional
     - Days without Billing: Item #1981
   * - ``psl_28``
     - PSL.28
     - Optional[str]
     - optional
     - Session-No: Item #1982
   * - ``psl_29``
     - PSL.29
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Executing Physician ID: Item #1983
   * - ``psl_30``
     - PSL.30
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Responsible Physician ID: Item #1984
   * - ``psl_31``
     - PSL.31
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Role Executing Physician: Item #1985 | Table HL70881
   * - ``psl_32``
     - PSL.32
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Medical Role Executing Physician: Item #1986 | Table HL70882
   * - ``psl_33``
     - PSL.33
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Side of body: Item #1987 | Table HL70894
   * - ``psl_34``
     - PSL.34
     - Optional[str]
     - optional
     - Number of TP's PP: Item #1988
   * - ``psl_35``
     - PSL.35
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - TP-Value PP: Item #1989
   * - ``psl_36``
     - PSL.36
     - Optional[str]
     - optional
     - Internal Scaling Factor PP: Item #1990
   * - ``psl_37``
     - PSL.37
     - Optional[str]
     - optional
     - External Scaling Factor PP: Item #1991
   * - ``psl_38``
     - PSL.38
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Amount PP: Item #1992
   * - ``psl_39``
     - PSL.39
     - Optional[str]
     - optional
     - Number of TP's Technical Part: Item #1993
   * - ``psl_40``
     - PSL.40
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - TP-Value Technical Part: Item #1994
   * - ``psl_41``
     - PSL.41
     - Optional[str]
     - optional
     - Internal Scaling Factor Technical Part: Item #1995
   * - ``psl_42``
     - PSL.42
     - Optional[str]
     - optional
     - External Scaling Factor Technical Part: Item #1996
   * - ``psl_43``
     - PSL.43
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Amount Technical Part: Item #1997
   * - ``psl_44``
     - PSL.44
     - Optional[:ref:`CP <hl7-v2_8_2-CP>`]
     - optional
     - Total Amount Professional Part + Technical Part: Item #1998
   * - ``psl_45``
     - PSL.45
     - Optional[str]
     - optional
     - VAT-Rate: Item #1999
   * - ``psl_46``
     - PSL.46
     - Optional[str]
     - optional
     - Main-Service: Item #2000
   * - ``psl_47``
     - PSL.47
     - Optional[str]
     - optional
     - Validation: Item #2001 | Table HL70136
   * - ``psl_48``
     - PSL.48
     - Optional[str]
     - optional
     - Comment: Item #2002

.. _hl7-v2_8_2-PSS:

.. py:class:: hl7types.hl7.v2_8_2.segments.PSS.PSS
   :noindex:

   HL7 v2 PSS segment.

PSS
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pss_1``
     - PSS.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Provider Product/Service Section Number: Item #1946
   * - ``pss_2``
     - PSS.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Payer Product/Service Section Number: Item #1947
   * - ``pss_3``
     - PSS.3
     - str
     - required
     - Product/Service Section Sequence Number: Item #1948
   * - ``pss_4``
     - PSS.4
     - :ref:`CP <hl7-v2_8_2-CP>`
     - required
     - Billed Amount: Item #1949
   * - ``pss_5``
     - PSS.5
     - str
     - required
     - Section Description or Heading: Item #2043

.. _hl7-v2_8_2-PTH:

.. py:class:: hl7types.hl7.v2_8_2.segments.PTH.PTH
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
     - Description
   * - ``pth_1``
     - PTH.1
     - str
     - required
     - Action Code: Item #816 | Table HL70206
   * - ``pth_2``
     - PTH.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Pathway ID: Item #1207
   * - ``pth_3``
     - PTH.3
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Pathway Instance ID: Item #1208
   * - ``pth_4``
     - PTH.4
     - str
     - required
     - Pathway Established Date/Time: Item #1209
   * - ``pth_5``
     - PTH.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Pathway Life Cycle Status: Item #1210
   * - ``pth_6``
     - PTH.6
     - Optional[str]
     - optional
     - Change Pathway Life Cycle Status Date/Time: Item #1211
   * - ``pth_7``
     - PTH.7
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Mood Code: Item #2239 | Table HL70725

.. _hl7-v2_8_2-PV1:

.. py:class:: hl7types.hl7.v2_8_2.segments.PV1.PV1
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
     - Description
   * - ``pv1_1``
     - PV1.1
     - Optional[str]
     - optional
     - Set ID - PV1: Item #131
   * - ``pv1_2``
     - PV1.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Patient Class: Item #132 | Table HL70004
   * - ``pv1_3``
     - PV1.3
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Assigned Patient Location: Item #133
   * - ``pv1_4``
     - PV1.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Admission Type: Item #134 | Table HL70007
   * - ``pv1_5``
     - PV1.5
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Preadmit Number: Item #135
   * - ``pv1_6``
     - PV1.6
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Prior Patient Location: Item #136
   * - ``pv1_7``
     - PV1.7
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Attending Doctor: Item #137 | Table HL70010
   * - ``pv1_8``
     - PV1.8
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Referring Doctor: Item #138 | Table HL70010
   * - ``pv1_9``
     - PV1.9
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Consulting Doctor: Item #139
   * - ``pv1_10``
     - PV1.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Hospital Service: Item #140 | Table HL70069
   * - ``pv1_11``
     - PV1.11
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Temporary Location: Item #141
   * - ``pv1_12``
     - PV1.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Preadmit Test Indicator: Item #142 | Table HL70087
   * - ``pv1_13``
     - PV1.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Re-admission Indicator: Item #143 | Table HL70092
   * - ``pv1_14``
     - PV1.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Admit Source: Item #144 | Table HL70023
   * - ``pv1_15``
     - PV1.15
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Ambulatory Status: Item #145 | Table HL70009
   * - ``pv1_16``
     - PV1.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - VIP Indicator: Item #146 | Table HL70099
   * - ``pv1_17``
     - PV1.17
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Admitting Doctor: Item #147 | Table HL70010
   * - ``pv1_18``
     - PV1.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Patient Type: Item #148 | Table HL70018
   * - ``pv1_19``
     - PV1.19
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Visit Number: Item #149
   * - ``pv1_20``
     - PV1.20
     - Optional[List[:ref:`FC <hl7-v2_8_2-FC>`]]
     - optional
     - Financial Class: Item #150 | Table HL70064
   * - ``pv1_21``
     - PV1.21
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Charge Price Indicator: Item #151 | Table HL70032
   * - ``pv1_22``
     - PV1.22
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Courtesy Code: Item #152 | Table HL70045
   * - ``pv1_23``
     - PV1.23
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Credit Rating: Item #153 | Table HL70046
   * - ``pv1_24``
     - PV1.24
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Contract Code: Item #154 | Table HL70044
   * - ``pv1_25``
     - PV1.25
     - Optional[List[str]]
     - optional
     - Contract Effective Date: Item #155
   * - ``pv1_26``
     - PV1.26
     - Optional[List[str]]
     - optional
     - Contract Amount: Item #156
   * - ``pv1_27``
     - PV1.27
     - Optional[List[str]]
     - optional
     - Contract Period: Item #157
   * - ``pv1_28``
     - PV1.28
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Interest Code: Item #158 | Table HL70073
   * - ``pv1_29``
     - PV1.29
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Transfer to Bad Debt Code: Item #159 | Table HL70110
   * - ``pv1_30``
     - PV1.30
     - Optional[str]
     - optional
     - Transfer to Bad Debt Date: Item #160
   * - ``pv1_31``
     - PV1.31
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Bad Debt Agency Code: Item #161 | Table HL70021
   * - ``pv1_32``
     - PV1.32
     - Optional[str]
     - optional
     - Bad Debt Transfer Amount: Item #162
   * - ``pv1_33``
     - PV1.33
     - Optional[str]
     - optional
     - Bad Debt Recovery Amount: Item #163
   * - ``pv1_34``
     - PV1.34
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Delete Account Indicator: Item #164 | Table HL70111
   * - ``pv1_35``
     - PV1.35
     - Optional[str]
     - optional
     - Delete Account Date: Item #165
   * - ``pv1_36``
     - PV1.36
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Discharge Disposition: Item #166 | Table HL70112
   * - ``pv1_37``
     - PV1.37
     - Optional[:ref:`DLD <hl7-v2_8_2-DLD>`]
     - optional
     - Discharged to Location: Item #167 | Table HL70113
   * - ``pv1_38``
     - PV1.38
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Diet Type: Item #168 | Table HL70114
   * - ``pv1_39``
     - PV1.39
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Servicing Facility: Item #169 | Table HL70115
   * - ``pv1_41``
     - PV1.41
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Account Status: Item #171 | Table HL70117
   * - ``pv1_42``
     - PV1.42
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Pending Location: Item #172
   * - ``pv1_43``
     - PV1.43
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Prior Temporary Location: Item #173
   * - ``pv1_44``
     - PV1.44
     - Optional[str]
     - optional
     - Admit Date/Time: Item #174
   * - ``pv1_45``
     - PV1.45
     - Optional[str]
     - optional
     - Discharge Date/Time: Item #175
   * - ``pv1_46``
     - PV1.46
     - Optional[str]
     - optional
     - Current Patient Balance: Item #176
   * - ``pv1_47``
     - PV1.47
     - Optional[str]
     - optional
     - Total Charges: Item #177
   * - ``pv1_48``
     - PV1.48
     - Optional[str]
     - optional
     - Total Adjustments: Item #178
   * - ``pv1_49``
     - PV1.49
     - Optional[str]
     - optional
     - Total Payments: Item #179
   * - ``pv1_50``
     - PV1.50
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Alternate Visit ID: Item #180 | Table HL70203
   * - ``pv1_51``
     - PV1.51
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Visit Indicator: Item #1226 | Table HL70326
   * - ``pv1_53``
     - PV1.53
     - Optional[str]
     - optional
     - Service Episode Description: Item #2290
   * - ``pv1_54``
     - PV1.54
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Service Episode Identifier: Item #2291

.. _hl7-v2_8_2-PV2:

.. py:class:: hl7types.hl7.v2_8_2.segments.PV2.PV2
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
     - Description
   * - ``pv2_1``
     - PV2.1
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Prior Pending Location: Item #181
   * - ``pv2_2``
     - PV2.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Accommodation Code: Item #182 | Table HL70129
   * - ``pv2_3``
     - PV2.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Admit Reason: Item #183
   * - ``pv2_4``
     - PV2.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Transfer Reason: Item #184
   * - ``pv2_5``
     - PV2.5
     - Optional[List[str]]
     - optional
     - Patient Valuables: Item #185
   * - ``pv2_6``
     - PV2.6
     - Optional[str]
     - optional
     - Patient Valuables Location: Item #186
   * - ``pv2_7``
     - PV2.7
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Visit User Code: Item #187 | Table HL70130
   * - ``pv2_8``
     - PV2.8
     - Optional[str]
     - optional
     - Expected Admit Date/Time: Item #188
   * - ``pv2_9``
     - PV2.9
     - Optional[str]
     - optional
     - Expected Discharge Date/Time: Item #189
   * - ``pv2_10``
     - PV2.10
     - Optional[str]
     - optional
     - Estimated Length of Inpatient Stay: Item #711
   * - ``pv2_11``
     - PV2.11
     - Optional[str]
     - optional
     - Actual Length of Inpatient Stay: Item #712
   * - ``pv2_12``
     - PV2.12
     - Optional[str]
     - optional
     - Visit Description: Item #713
   * - ``pv2_13``
     - PV2.13
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Referral Source Code: Item #714
   * - ``pv2_14``
     - PV2.14
     - Optional[str]
     - optional
     - Previous Service Date: Item #715
   * - ``pv2_15``
     - PV2.15
     - Optional[str]
     - optional
     - Employment Illness Related Indicator: Item #716 | Table HL70136
   * - ``pv2_16``
     - PV2.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Purge Status Code: Item #717 | Table HL70213
   * - ``pv2_17``
     - PV2.17
     - Optional[str]
     - optional
     - Purge Status Date: Item #718
   * - ``pv2_18``
     - PV2.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Special Program Code: Item #719 | Table HL70214
   * - ``pv2_19``
     - PV2.19
     - Optional[str]
     - optional
     - Retention Indicator: Item #720 | Table HL70136
   * - ``pv2_20``
     - PV2.20
     - Optional[str]
     - optional
     - Expected Number of Insurance Plans: Item #721
   * - ``pv2_21``
     - PV2.21
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Visit Publicity Code: Item #722 | Table HL70215
   * - ``pv2_22``
     - PV2.22
     - Optional[str]
     - optional
     - Visit Protection Indicator: Item #723 | Table HL70136
   * - ``pv2_23``
     - PV2.23
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Clinic Organization Name: Item #724
   * - ``pv2_24``
     - PV2.24
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Patient Status Code: Item #725 | Table HL70216
   * - ``pv2_25``
     - PV2.25
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Visit Priority Code: Item #726 | Table HL70217
   * - ``pv2_26``
     - PV2.26
     - Optional[str]
     - optional
     - Previous Treatment Date: Item #727
   * - ``pv2_27``
     - PV2.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Expected Discharge Disposition: Item #728 | Table HL70112
   * - ``pv2_28``
     - PV2.28
     - Optional[str]
     - optional
     - Signature on File Date: Item #729
   * - ``pv2_29``
     - PV2.29
     - Optional[str]
     - optional
     - First Similar Illness Date: Item #730
   * - ``pv2_30``
     - PV2.30
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Patient Charge Adjustment Code: Item #731 | Table HL70218
   * - ``pv2_31``
     - PV2.31
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Recurring Service Code: Item #732 | Table HL70219
   * - ``pv2_32``
     - PV2.32
     - Optional[str]
     - optional
     - Billing Media Code: Item #733 | Table HL70136
   * - ``pv2_33``
     - PV2.33
     - Optional[str]
     - optional
     - Expected Surgery Date and Time: Item #734
   * - ``pv2_34``
     - PV2.34
     - Optional[str]
     - optional
     - Military Partnership Code: Item #735 | Table HL70136
   * - ``pv2_35``
     - PV2.35
     - Optional[str]
     - optional
     - Military Non-Availability Code: Item #736 | Table HL70136
   * - ``pv2_36``
     - PV2.36
     - Optional[str]
     - optional
     - Newborn Baby Indicator: Item #737 | Table HL70136
   * - ``pv2_37``
     - PV2.37
     - Optional[str]
     - optional
     - Baby Detained Indicator: Item #738 | Table HL70136
   * - ``pv2_38``
     - PV2.38
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Mode of Arrival Code: Item #1543 | Table HL70430
   * - ``pv2_39``
     - PV2.39
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Recreational Drug Use Code: Item #1544 | Table HL70431
   * - ``pv2_40``
     - PV2.40
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Admission Level of Care Code: Item #1545 | Table HL70432
   * - ``pv2_41``
     - PV2.41
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Precaution Code: Item #1546 | Table HL70433
   * - ``pv2_42``
     - PV2.42
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Patient Condition Code: Item #1547 | Table HL70434
   * - ``pv2_43``
     - PV2.43
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Living Will Code: Item #759 | Table HL70315
   * - ``pv2_44``
     - PV2.44
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Organ Donor Code: Item #760 | Table HL70316
   * - ``pv2_45``
     - PV2.45
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Advance Directive Code: Item #1548 | Table HL70435
   * - ``pv2_46``
     - PV2.46
     - Optional[str]
     - optional
     - Patient Status Effective Date: Item #1549
   * - ``pv2_47``
     - PV2.47
     - Optional[str]
     - optional
     - Expected LOA Return Date/Time: Item #1550
   * - ``pv2_48``
     - PV2.48
     - Optional[str]
     - optional
     - Expected Pre-admission Testing Date/Time: Item #1841
   * - ``pv2_49``
     - PV2.49
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Notify Clergy Code: Item #1842 | Table HL70534
   * - ``pv2_50``
     - PV2.50
     - Optional[str]
     - optional
     - Advance Directive Last Verified Date: Item #2141

.. _hl7-v2_8_2-PYE:

.. py:class:: hl7types.hl7.v2_8_2.segments.PYE.PYE
   :noindex:

   HL7 v2 PYE segment.

PYE
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pye_1``
     - PYE.1
     - str
     - required
     - Set ID - PYE: Item #1939
   * - ``pye_2``
     - PYE.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Payee Type: Item #1940 | Table HL70557
   * - ``pye_3``
     - PYE.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Payee Relationship to Invoice (Patient): Item #1941 | Table HL70558
   * - ``pye_4``
     - PYE.4
     - Optional[List[:ref:`XON <hl7-v2_8_2-XON>`]]
     - optional
     - Payee Identification List: Item #1942
   * - ``pye_5``
     - PYE.5
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Payee Person Name: Item #1943
   * - ``pye_6``
     - PYE.6
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Payee Address: Item #1944
   * - ``pye_7``
     - PYE.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Payment Method: Item #1945 | Table HL70570

.. _hl7-v2_8_2-QAK:

.. py:class:: hl7types.hl7.v2_8_2.segments.QAK.QAK
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
     - Description
   * - ``qak_1``
     - QAK.1
     - Optional[str]
     - optional
     - Query Tag: Item #696
   * - ``qak_2``
     - QAK.2
     - Optional[str]
     - optional
     - Query Response Status: Item #708 | Table HL70208
   * - ``qak_3``
     - QAK.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Message Query Name: Item #1375 | Table HL70471
   * - ``qak_4``
     - QAK.4
     - Optional[str]
     - optional
     - Hit Count Total: Item #1434
   * - ``qak_5``
     - QAK.5
     - Optional[str]
     - optional
     - This payload: Item #1622
   * - ``qak_6``
     - QAK.6
     - Optional[str]
     - optional
     - Hits remaining: Item #1623

.. _hl7-v2_8_2-QID:

.. py:class:: hl7types.hl7.v2_8_2.segments.QID.QID
   :noindex:

   HL7 v2 QID segment.

QID
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``qid_1``
     - QID.1
     - str
     - required
     - Query Tag: Item #696
   * - ``qid_2``
     - QID.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Message Query Name: Item #1375 | Table HL70471

.. _hl7-v2_8_2-QPD:

.. py:class:: hl7types.hl7.v2_8_2.segments.QPD.QPD
   :noindex:

   HL7 v2 QPD segment.

QPD
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``qpd_1``
     - QPD.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Message Query Name: Item #1375 | Table HL70471
   * - ``qpd_2``
     - QPD.2
     - Optional[str]
     - optional
     - Query Tag: Item #696
   * - ``qpd_3``
     - QPD.3
     - Optional[varies]
     - optional
     - User Parameters (in successive fields): Item #1435

.. _hl7-v2_8_2-QRI:

.. py:class:: hl7types.hl7.v2_8_2.segments.QRI.QRI
   :noindex:

   HL7 v2 QRI segment.

QRI
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``qri_1``
     - QRI.1
     - Optional[str]
     - optional
     - Candidate Confidence: Item #1436
   * - ``qri_2``
     - QRI.2
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Match Reason Code: Item #1437 | Table HL70392
   * - ``qri_3``
     - QRI.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Algorithm Descriptor: Item #1438 | Table HL70393

.. _hl7-v2_8_2-RCP:

.. py:class:: hl7types.hl7.v2_8_2.segments.RCP.RCP
   :noindex:

   HL7 v2 RCP segment.

RCP
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rcp_1``
     - RCP.1
     - Optional[str]
     - optional
     - Query Priority: Item #27 | Table HL70091
   * - ``rcp_2``
     - RCP.2
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Quantity Limited Request: Item #31 | Table HL70126
   * - ``rcp_3``
     - RCP.3
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Response Modality: Item #1440 | Table HL70394
   * - ``rcp_4``
     - RCP.4
     - Optional[str]
     - optional
     - Execution and Delivery Time: Item #1441
   * - ``rcp_5``
     - RCP.5
     - Optional[str]
     - optional
     - Modify Indicator: Item #1443 | Table HL70395
   * - ``rcp_6``
     - RCP.6
     - Optional[List[:ref:`SRT <hl7-v2_8_2-SRT>`]]
     - optional
     - Sort-by Field: Item #1624
   * - ``rcp_7``
     - RCP.7
     - Optional[List[str]]
     - optional
     - Segment group inclusion: Item #1594 | Table HL70391

.. _hl7-v2_8_2-RDF:

.. py:class:: hl7types.hl7.v2_8_2.segments.RDF.RDF
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
     - Description
   * - ``rdf_1``
     - RDF.1
     - str
     - required
     - Number of Columns per Row: Item #701
   * - ``rdf_2``
     - RDF.2
     - List[:ref:`RCD <hl7-v2_8_2-RCD>`]
     - required
     - Column Description: Item #702 | Table HL70440

.. _hl7-v2_8_2-RDT:

.. py:class:: hl7types.hl7.v2_8_2.segments.RDT.RDT
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
     - Description
   * - ``rdt_1``
     - RDT.1
     - varies
     - required
     - Column Value: Item #703

.. _hl7-v2_8_2-REL:

.. py:class:: hl7types.hl7.v2_8_2.segments.REL.REL
   :noindex:

   HL7 v2 REL segment.

REL
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rel_1``
     - REL.1
     - Optional[str]
     - optional
     - Set ID -REL: Item #2240
   * - ``rel_2``
     - REL.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Relationship Type: Item #2241
   * - ``rel_3``
     - REL.3
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - This Relationship Instance Identifier: Item #2242
   * - ``rel_4``
     - REL.4
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Source Information Instance Identifier: Item #2243
   * - ``rel_5``
     - REL.5
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Target Information Instance Identifier: Item #2244
   * - ``rel_6``
     - REL.6
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Asserting Entity Instance ID: Item #2245
   * - ``rel_7``
     - REL.7
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Asserting Person: Item #2246
   * - ``rel_8``
     - REL.8
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Asserting Organization: Item #2247
   * - ``rel_9``
     - REL.9
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - Assertor Address: Item #2248
   * - ``rel_10``
     - REL.10
     - Optional[:ref:`XTN <hl7-v2_8_2-XTN>`]
     - optional
     - Assertor Contact: Item #2249
   * - ``rel_11``
     - REL.11
     - Optional[:ref:`DR <hl7-v2_8_2-DR>`]
     - optional
     - Assertion Date Range: Item #2250
   * - ``rel_12``
     - REL.12
     - Optional[str]
     - optional
     - Negation Indicator: Item #2251 | Table HL70136
   * - ``rel_13``
     - REL.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Certainty of Relationship: Item #2252
   * - ``rel_14``
     - REL.14
     - Optional[str]
     - optional
     - Priority No: Item #2253
   * - ``rel_15``
     - REL.15
     - Optional[str]
     - optional
     - Priority  Sequence No (rel preference for consideration): Item #2254
   * - ``rel_16``
     - REL.16
     - Optional[str]
     - optional
     - Separability Indicator: Item #2255 | Table HL70136

.. _hl7-v2_8_2-RF1:

.. py:class:: hl7types.hl7.v2_8_2.segments.RF1.RF1
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
     - Description
   * - ``rf1_1``
     - RF1.1
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Referral Status: Item #1137 | Table HL70283
   * - ``rf1_2``
     - RF1.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Referral Priority: Item #1138 | Table HL70280
   * - ``rf1_3``
     - RF1.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Referral Type: Item #1139 | Table HL70281
   * - ``rf1_4``
     - RF1.4
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Referral Disposition: Item #1140 | Table HL70282
   * - ``rf1_5``
     - RF1.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Referral Category: Item #1141 | Table HL70284
   * - ``rf1_6``
     - RF1.6
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Originating Referral Identifier: Item #1142
   * - ``rf1_7``
     - RF1.7
     - Optional[str]
     - optional
     - Effective Date: Item #1143
   * - ``rf1_8``
     - RF1.8
     - Optional[str]
     - optional
     - Expiration Date: Item #1144
   * - ``rf1_9``
     - RF1.9
     - Optional[str]
     - optional
     - Process Date: Item #1145
   * - ``rf1_10``
     - RF1.10
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Referral Reason: Item #1228 | Table HL70336
   * - ``rf1_11``
     - RF1.11
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - External Referral Identifier: Item #1300
   * - ``rf1_12``
     - RF1.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Referral Documentation Completion Status: Item #2262 | Table HL70865
   * - ``rf1_13``
     - RF1.13
     - Optional[str]
     - optional
     - Planned Treatment Stop Date: Item #3400
   * - ``rf1_14``
     - RF1.14
     - Optional[str]
     - optional
     - Referral Reason Text: Item #3401
   * - ``rf1_15``
     - RF1.15
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Number of Authorized Treatments/Units: Item #3402
   * - ``rf1_16``
     - RF1.16
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Number of Used Treatments/Units: Item #3403
   * - ``rf1_17``
     - RF1.17
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Number of Schedule Treatments/Units: Item #3404
   * - ``rf1_18``
     - RF1.18
     - Optional[:ref:`MO <hl7-v2_8_2-MO>`]
     - optional
     - Remaining Benefit Amount: Item #3405
   * - ``rf1_19``
     - RF1.19
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Authorized Provider: Item #3406
   * - ``rf1_20``
     - RF1.20
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Authorized Health Professional: Item #3407
   * - ``rf1_21``
     - RF1.21
     - Optional[str]
     - optional
     - Source Text: Item #3408
   * - ``rf1_22``
     - RF1.22
     - Optional[str]
     - optional
     - Source Date: Item #3409
   * - ``rf1_23``
     - RF1.23
     - Optional[:ref:`XTN <hl7-v2_8_2-XTN>`]
     - optional
     - Source Phone: Item #3410
   * - ``rf1_24``
     - RF1.24
     - Optional[str]
     - optional
     - Comment: Item #3411
   * - ``rf1_25``
     - RF1.25
     - Optional[str]
     - optional
     - Action Code: Item #3412 | Table HL70206

.. _hl7-v2_8_2-RFI:

.. py:class:: hl7types.hl7.v2_8_2.segments.RFI.RFI
   :noindex:

   HL7 v2 RFI segment.

RFI
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rfi_1``
     - RFI.1
     - str
     - required
     - Request Date: Item #1910
   * - ``rfi_2``
     - RFI.2
     - str
     - required
     - Response Due Date: Item #1911
   * - ``rfi_3``
     - RFI.3
     - Optional[str]
     - optional
     - Patient Consent: Item #1912 | Table HL70136
   * - ``rfi_4``
     - RFI.4
     - Optional[str]
     - optional
     - Date Additional Information Was Submitted: Item #1913

.. _hl7-v2_8_2-RGS:

.. py:class:: hl7types.hl7.v2_8_2.segments.RGS.RGS
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
     - Description
   * - ``rgs_1``
     - RGS.1
     - str
     - required
     - Set ID - RGS: Item #1203
   * - ``rgs_2``
     - RGS.2
     - Optional[str]
     - optional
     - Segment Action Code: Item #763 | Table HL70206
   * - ``rgs_3``
     - RGS.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Resource Group ID: Item #1204

.. _hl7-v2_8_2-RMI:

.. py:class:: hl7types.hl7.v2_8_2.segments.RMI.RMI
   :noindex:

   HL7 v2 RMI segment.

RMI
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rmi_1``
     - RMI.1
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Risk Management Incident Code: Item #1530 | Table HL70427
   * - ``rmi_2``
     - RMI.2
     - Optional[str]
     - optional
     - Date/Time Incident: Item #1531
   * - ``rmi_3``
     - RMI.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Incident Type Code: Item #1533 | Table HL70428

.. _hl7-v2_8_2-ROL:

.. py:class:: hl7types.hl7.v2_8_2.segments.ROL.ROL
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
     - Description
   * - ``rol_1``
     - ROL.1
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Role Instance ID: Item #1206
   * - ``rol_2``
     - ROL.2
     - str
     - required
     - Action Code: Item #816 | Table HL70206
   * - ``rol_3``
     - ROL.3
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Role-ROL: Item #1197 | Table HL70443
   * - ``rol_4``
     - ROL.4
     - List[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - required
     - Role Person: Item #1198
   * - ``rol_5``
     - ROL.5
     - Optional[str]
     - optional
     - Role Begin Date/Time: Item #1199
   * - ``rol_6``
     - ROL.6
     - Optional[str]
     - optional
     - Role End Date/Time: Item #1200
   * - ``rol_7``
     - ROL.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Role Duration: Item #1201
   * - ``rol_8``
     - ROL.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Role Action Reason: Item #1205
   * - ``rol_9``
     - ROL.9
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Provider Type: Item #1510
   * - ``rol_10``
     - ROL.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Organization Unit Type: Item #1461 | Table HL70406
   * - ``rol_11``
     - ROL.11
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Office/Home Address/Birthplace: Item #679
   * - ``rol_12``
     - ROL.12
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Phone: Item #678
   * - ``rol_13``
     - ROL.13
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Person's Location: Item #2183
   * - ``rol_14``
     - ROL.14
     - Optional[:ref:`XON <hl7-v2_8_2-XON>`]
     - optional
     - Organization: Item #2377

.. _hl7-v2_8_2-RQ1:

.. py:class:: hl7types.hl7.v2_8_2.segments.RQ1.RQ1
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
     - Description
   * - ``rq1_1``
     - RQ1.1
     - Optional[str]
     - optional
     - Anticipated Price: Item #285
   * - ``rq1_2``
     - RQ1.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Manufacturer Identifier: Item #286 | Table HL70385
   * - ``rq1_3``
     - RQ1.3
     - Optional[str]
     - optional
     - Manufacturer's Catalog: Item #287
   * - ``rq1_4``
     - RQ1.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Vendor ID: Item #288 | Table HL79999
   * - ``rq1_5``
     - RQ1.5
     - Optional[str]
     - optional
     - Vendor Catalog: Item #289
   * - ``rq1_6``
     - RQ1.6
     - Optional[str]
     - optional
     - Taxable: Item #290 | Table HL70136
   * - ``rq1_7``
     - RQ1.7
     - Optional[str]
     - optional
     - Substitute Allowed: Item #291 | Table HL70136

.. _hl7-v2_8_2-RQD:

.. py:class:: hl7types.hl7.v2_8_2.segments.RQD.RQD
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
     - Description
   * - ``rqd_1``
     - RQD.1
     - Optional[str]
     - optional
     - Requisition Line Number: Item #275
   * - ``rqd_2``
     - RQD.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Item Code - Internal: Item #276 | Table HL79999
   * - ``rqd_3``
     - RQD.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Item Code - External: Item #277 | Table HL79999
   * - ``rqd_4``
     - RQD.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Hospital Item Code: Item #278 | Table HL79999
   * - ``rqd_5``
     - RQD.5
     - Optional[str]
     - optional
     - Requisition Quantity: Item #279
   * - ``rqd_6``
     - RQD.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Requisition Unit of Measure: Item #280 | Table HL79999
   * - ``rqd_7``
     - RQD.7
     - Optional[:ref:`CX <hl7-v2_8_2-CX>`]
     - optional
     - Cost Center Account Number: Item #281 | Table HL70319
   * - ``rqd_8``
     - RQD.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Item Natural Account Code: Item #282 | Table HL70320
   * - ``rqd_9``
     - RQD.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Deliver To ID: Item #283 | Table HL79999
   * - ``rqd_10``
     - RQD.10
     - Optional[str]
     - optional
     - Date Needed: Item #284

.. _hl7-v2_8_2-RXA:

.. py:class:: hl7types.hl7.v2_8_2.segments.RXA.RXA
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
     - Description
   * - ``rxa_1``
     - RXA.1
     - str
     - required
     - Give Sub-ID Counter: Item #342
   * - ``rxa_2``
     - RXA.2
     - str
     - required
     - Administration Sub-ID Counter: Item #344
   * - ``rxa_3``
     - RXA.3
     - str
     - required
     - Date/Time Start of Administration: Item #345
   * - ``rxa_4``
     - RXA.4
     - str
     - required
     - Date/Time End of Administration: Item #346
   * - ``rxa_5``
     - RXA.5
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Administered Code: Item #347 | Table HL70292
   * - ``rxa_6``
     - RXA.6
     - str
     - required
     - Administered Amount: Item #348
   * - ``rxa_7``
     - RXA.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Administered Units: Item #349 | Table HL79999
   * - ``rxa_8``
     - RXA.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Administered Dosage Form: Item #350 | Table HL79999
   * - ``rxa_9``
     - RXA.9
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Administration Notes: Item #351 | Table HL79999
   * - ``rxa_10``
     - RXA.10
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Administering Provider: Item #352
   * - ``rxa_12``
     - RXA.12
     - Optional[str]
     - optional
     - Administered Per (Time Unit): Item #354
   * - ``rxa_13``
     - RXA.13
     - Optional[str]
     - optional
     - Administered Strength: Item #1134
   * - ``rxa_14``
     - RXA.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Administered Strength Units: Item #1135 | Table HL79999
   * - ``rxa_15``
     - RXA.15
     - Optional[List[str]]
     - optional
     - Substance Lot Number: Item #1129
   * - ``rxa_16``
     - RXA.16
     - Optional[List[str]]
     - optional
     - Substance Expiration Date: Item #1130
   * - ``rxa_17``
     - RXA.17
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Substance Manufacturer Name: Item #1131
   * - ``rxa_18``
     - RXA.18
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Substance/Treatment Refusal Reason: Item #1136 | Table HL79999
   * - ``rxa_19``
     - RXA.19
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Indication: Item #1123 | Table HL79999
   * - ``rxa_20``
     - RXA.20
     - Optional[str]
     - optional
     - Completion Status: Item #1223 | Table HL70322
   * - ``rxa_21``
     - RXA.21
     - Optional[str]
     - optional
     - Action Code - RXA: Item #1224 | Table HL70206
   * - ``rxa_22``
     - RXA.22
     - Optional[str]
     - optional
     - System Entry Date/Time: Item #1225
   * - ``rxa_23``
     - RXA.23
     - Optional[str]
     - optional
     - Administered Drug Strength Volume: Item #1696
   * - ``rxa_24``
     - RXA.24
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Administered Drug Strength Volume Units: Item #1697 | Table HL79999
   * - ``rxa_25``
     - RXA.25
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Administered Barcode Identifier: Item #1698 | Table HL79999
   * - ``rxa_26``
     - RXA.26
     - Optional[str]
     - optional
     - Pharmacy Order Type: Item #1699 | Table HL70480
   * - ``rxa_27``
     - RXA.27
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Administer-at: Item #2264
   * - ``rxa_28``
     - RXA.28
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - Administered-at Address: Item #2265
   * - ``rxa_29``
     - RXA.29
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Administered Tag Identifier: Item #3396

.. _hl7-v2_8_2-RXC:

.. py:class:: hl7types.hl7.v2_8_2.segments.RXC.RXC
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
     - Description
   * - ``rxc_1``
     - RXC.1
     - str
     - required
     - RX Component Type: Item #313 | Table HL70166
   * - ``rxc_2``
     - RXC.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Component Code: Item #314 | Table HL79999
   * - ``rxc_3``
     - RXC.3
     - str
     - required
     - Component Amount: Item #315
   * - ``rxc_4``
     - RXC.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Component Units: Item #316 | Table HL79999
   * - ``rxc_5``
     - RXC.5
     - Optional[str]
     - optional
     - Component Strength: Item #1124
   * - ``rxc_6``
     - RXC.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Component Strength Units: Item #1125 | Table HL79999
   * - ``rxc_7``
     - RXC.7
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Supplementary Code: Item #1476 | Table HL79999
   * - ``rxc_8``
     - RXC.8
     - Optional[str]
     - optional
     - Component Drug Strength Volume: Item #1671
   * - ``rxc_9``
     - RXC.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Component Drug Strength Volume Units: Item #1672 | Table HL79999
   * - ``rxc_10``
     - RXC.10
     - Optional[str]
     - optional
     - Dispense Amount: Item #3314
   * - ``rxc_11``
     - RXC.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Dispense Units: Item #3315 | Table HL79999

.. _hl7-v2_8_2-RXD:

.. py:class:: hl7types.hl7.v2_8_2.segments.RXD.RXD
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
     - Description
   * - ``rxd_1``
     - RXD.1
     - str
     - required
     - Dispense Sub-ID Counter: Item #334
   * - ``rxd_2``
     - RXD.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Dispense/Give Code: Item #335 | Table HL70292
   * - ``rxd_3``
     - RXD.3
     - str
     - required
     - Date/Time Dispensed: Item #336
   * - ``rxd_4``
     - RXD.4
     - str
     - required
     - Actual Dispense Amount: Item #337
   * - ``rxd_5``
     - RXD.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Actual Dispense Units: Item #338 | Table HL79999
   * - ``rxd_6``
     - RXD.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Actual Dosage Form: Item #339 | Table HL79999
   * - ``rxd_7``
     - RXD.7
     - str
     - required
     - Prescription Number: Item #325
   * - ``rxd_8``
     - RXD.8
     - Optional[str]
     - optional
     - Number of Refills Remaining: Item #326
   * - ``rxd_9``
     - RXD.9
     - Optional[List[str]]
     - optional
     - Dispense Notes: Item #340
   * - ``rxd_10``
     - RXD.10
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Dispensing Provider: Item #341
   * - ``rxd_11``
     - RXD.11
     - Optional[str]
     - optional
     - Substitution Status: Item #322 | Table HL70167
   * - ``rxd_12``
     - RXD.12
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Total Daily Dose: Item #329
   * - ``rxd_14``
     - RXD.14
     - Optional[str]
     - optional
     - Needs Human Review: Item #307 | Table HL70136
   * - ``rxd_15``
     - RXD.15
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Special Dispensing Instructions: Item #330 | Table HL79999
   * - ``rxd_16``
     - RXD.16
     - Optional[str]
     - optional
     - Actual Strength: Item #1132
   * - ``rxd_17``
     - RXD.17
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Actual Strength Unit: Item #1133 | Table HL79999
   * - ``rxd_18``
     - RXD.18
     - Optional[List[str]]
     - optional
     - Substance Lot Number: Item #1129
   * - ``rxd_19``
     - RXD.19
     - Optional[List[str]]
     - optional
     - Substance Expiration Date: Item #1130
   * - ``rxd_20``
     - RXD.20
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Substance Manufacturer Name: Item #1131
   * - ``rxd_21``
     - RXD.21
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Indication: Item #1123 | Table HL79999
   * - ``rxd_22``
     - RXD.22
     - Optional[str]
     - optional
     - Dispense Package Size: Item #1220
   * - ``rxd_23``
     - RXD.23
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Dispense Package Size Unit: Item #1221 | Table HL79999
   * - ``rxd_24``
     - RXD.24
     - Optional[str]
     - optional
     - Dispense Package Method: Item #1222 | Table HL70321
   * - ``rxd_25``
     - RXD.25
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Supplementary Code: Item #1476 | Table HL79999
   * - ``rxd_26``
     - RXD.26
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Initiating Location: Item #1477 | Table HL79999
   * - ``rxd_27``
     - RXD.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Packaging/Assembly Location: Item #1478 | Table HL79999
   * - ``rxd_28``
     - RXD.28
     - Optional[str]
     - optional
     - Actual Drug Strength Volume: Item #1686
   * - ``rxd_29``
     - RXD.29
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Actual Drug Strength Volume Units: Item #1687 | Table HL79999
   * - ``rxd_30``
     - RXD.30
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Dispense to Pharmacy: Item #1688 | Table HL79999
   * - ``rxd_31``
     - RXD.31
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - Dispense to Pharmacy Address: Item #1689
   * - ``rxd_32``
     - RXD.32
     - Optional[str]
     - optional
     - Pharmacy Order Type: Item #1690 | Table HL70480
   * - ``rxd_33``
     - RXD.33
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Dispense Type: Item #1691 | Table HL70484
   * - ``rxd_34``
     - RXD.34
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Pharmacy Phone Number: Item #2311
   * - ``rxd_35``
     - RXD.35
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Dispense Tag Identifier: Item #3392

.. _hl7-v2_8_2-RXE:

.. py:class:: hl7types.hl7.v2_8_2.segments.RXE.RXE
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
     - Description
   * - ``rxe_2``
     - RXE.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Give Code: Item #317 | Table HL70292
   * - ``rxe_3``
     - RXE.3
     - str
     - required
     - Give Amount - Minimum: Item #318
   * - ``rxe_4``
     - RXE.4
     - Optional[str]
     - optional
     - Give Amount - Maximum: Item #319
   * - ``rxe_5``
     - RXE.5
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Give Units: Item #320 | Table HL79999
   * - ``rxe_6``
     - RXE.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Give Dosage Form: Item #321 | Table HL79999
   * - ``rxe_7``
     - RXE.7
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Provider's Administration Instructions: Item #298 | Table HL79999
   * - ``rxe_9``
     - RXE.9
     - Optional[str]
     - optional
     - Substitution Status: Item #322 | Table HL70167
   * - ``rxe_10``
     - RXE.10
     - Optional[str]
     - optional
     - Dispense Amount: Item #323
   * - ``rxe_11``
     - RXE.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Dispense Units: Item #324 | Table HL79999
   * - ``rxe_12``
     - RXE.12
     - Optional[str]
     - optional
     - Number Of Refills: Item #304
   * - ``rxe_13``
     - RXE.13
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Ordering Provider's DEA Number: Item #305
   * - ``rxe_14``
     - RXE.14
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Pharmacist/Treatment Supplier's Verifier ID: Item #306
   * - ``rxe_15``
     - RXE.15
     - Optional[str]
     - optional
     - Prescription Number: Item #325
   * - ``rxe_16``
     - RXE.16
     - Optional[str]
     - optional
     - Number of Refills Remaining: Item #326
   * - ``rxe_17``
     - RXE.17
     - Optional[str]
     - optional
     - Number of Refills/Doses Dispensed: Item #327
   * - ``rxe_18``
     - RXE.18
     - Optional[str]
     - optional
     - D/T of Most Recent Refill or Dose Dispensed: Item #328
   * - ``rxe_19``
     - RXE.19
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Total Daily Dose: Item #329
   * - ``rxe_20``
     - RXE.20
     - Optional[str]
     - optional
     - Needs Human Review: Item #307 | Table HL70136
   * - ``rxe_21``
     - RXE.21
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Special Dispensing Instructions: Item #330 | Table HL79999
   * - ``rxe_22``
     - RXE.22
     - Optional[str]
     - optional
     - Give Per (Time Unit): Item #331
   * - ``rxe_23``
     - RXE.23
     - Optional[str]
     - optional
     - Give Rate Amount: Item #332
   * - ``rxe_24``
     - RXE.24
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Give Rate Units: Item #333 | Table HL79999
   * - ``rxe_25``
     - RXE.25
     - Optional[str]
     - optional
     - Give Strength: Item #1126
   * - ``rxe_26``
     - RXE.26
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Give Strength Units: Item #1127 | Table HL79999
   * - ``rxe_27``
     - RXE.27
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Give Indication: Item #1128 | Table HL79999
   * - ``rxe_28``
     - RXE.28
     - Optional[str]
     - optional
     - Dispense Package Size: Item #1220
   * - ``rxe_29``
     - RXE.29
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Dispense Package Size Unit: Item #1221 | Table HL79999
   * - ``rxe_30``
     - RXE.30
     - Optional[str]
     - optional
     - Dispense Package Method: Item #1222 | Table HL70321
   * - ``rxe_31``
     - RXE.31
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Supplementary Code: Item #1476 | Table HL79999
   * - ``rxe_32``
     - RXE.32
     - Optional[str]
     - optional
     - Original Order Date/Time: Item #1673
   * - ``rxe_33``
     - RXE.33
     - Optional[str]
     - optional
     - Give Drug Strength Volume: Item #1674
   * - ``rxe_34``
     - RXE.34
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Give Drug Strength Volume Units: Item #1675 | Table HL79999
   * - ``rxe_35``
     - RXE.35
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Controlled Substance Schedule: Item #1676 | Table HL70477
   * - ``rxe_36``
     - RXE.36
     - Optional[str]
     - optional
     - Formulary Status: Item #1677 | Table HL70478
   * - ``rxe_37``
     - RXE.37
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Pharmaceutical Substance Alternative: Item #1678 | Table HL79999
   * - ``rxe_38``
     - RXE.38
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Pharmacy of Most Recent Fill: Item #1679 | Table HL79999
   * - ``rxe_39``
     - RXE.39
     - Optional[str]
     - optional
     - Initial Dispense Amount: Item #1680
   * - ``rxe_40``
     - RXE.40
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Dispensing Pharmacy: Item #1681 | Table HL79999
   * - ``rxe_41``
     - RXE.41
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - Dispensing Pharmacy Address: Item #1682
   * - ``rxe_42``
     - RXE.42
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Deliver-to Patient Location: Item #1683
   * - ``rxe_43``
     - RXE.43
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - Deliver-to Address: Item #1684
   * - ``rxe_44``
     - RXE.44
     - Optional[str]
     - optional
     - Pharmacy Order Type: Item #1685 | Table HL70480
   * - ``rxe_45``
     - RXE.45
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Pharmacy Phone Number: Item #2310

.. _hl7-v2_8_2-RXG:

.. py:class:: hl7types.hl7.v2_8_2.segments.RXG.RXG
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
     - Description
   * - ``rxg_1``
     - RXG.1
     - str
     - required
     - Give Sub-ID Counter: Item #342
   * - ``rxg_2``
     - RXG.2
     - Optional[str]
     - optional
     - Dispense Sub-ID Counter: Item #334
   * - ``rxg_4``
     - RXG.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Give Code: Item #317 | Table HL70292
   * - ``rxg_5``
     - RXG.5
     - str
     - required
     - Give Amount - Minimum: Item #318
   * - ``rxg_6``
     - RXG.6
     - Optional[str]
     - optional
     - Give Amount - Maximum: Item #319
   * - ``rxg_7``
     - RXG.7
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Give Units: Item #320 | Table HL79999
   * - ``rxg_8``
     - RXG.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Give Dosage Form: Item #321 | Table HL79999
   * - ``rxg_9``
     - RXG.9
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Administration Notes: Item #351 | Table HL79999
   * - ``rxg_10``
     - RXG.10
     - Optional[str]
     - optional
     - Substitution Status: Item #322 | Table HL70167
   * - ``rxg_12``
     - RXG.12
     - Optional[str]
     - optional
     - Needs Human Review: Item #307 | Table HL70136
   * - ``rxg_13``
     - RXG.13
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Special Administration Instructions: Item #343 | Table HL79999
   * - ``rxg_14``
     - RXG.14
     - Optional[str]
     - optional
     - Give Per (Time Unit): Item #331
   * - ``rxg_15``
     - RXG.15
     - Optional[str]
     - optional
     - Give Rate Amount: Item #332
   * - ``rxg_16``
     - RXG.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Give Rate Units: Item #333 | Table HL79999
   * - ``rxg_17``
     - RXG.17
     - Optional[str]
     - optional
     - Give Strength: Item #1126
   * - ``rxg_18``
     - RXG.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Give Strength Units: Item #1127 | Table HL79999
   * - ``rxg_19``
     - RXG.19
     - Optional[List[str]]
     - optional
     - Substance Lot Number: Item #1129
   * - ``rxg_20``
     - RXG.20
     - Optional[List[str]]
     - optional
     - Substance Expiration Date: Item #1130
   * - ``rxg_21``
     - RXG.21
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Substance Manufacturer Name: Item #1131
   * - ``rxg_22``
     - RXG.22
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Indication: Item #1123 | Table HL79999
   * - ``rxg_23``
     - RXG.23
     - Optional[str]
     - optional
     - Give Drug Strength Volume: Item #1692
   * - ``rxg_24``
     - RXG.24
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Give Drug Strength Volume Units: Item #1693 | Table HL79999
   * - ``rxg_25``
     - RXG.25
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Give Barcode Identifier: Item #1694 | Table HL79999
   * - ``rxg_26``
     - RXG.26
     - Optional[str]
     - optional
     - Pharmacy Order Type: Item #1695 | Table HL70480
   * - ``rxg_27``
     - RXG.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Dispense to Pharmacy: Item #1688 | Table HL79999
   * - ``rxg_28``
     - RXG.28
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - Dispense to Pharmacy Address: Item #1689
   * - ``rxg_29``
     - RXG.29
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Deliver-to Patient Location: Item #1683
   * - ``rxg_30``
     - RXG.30
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - Deliver-to Address: Item #1684
   * - ``rxg_31``
     - RXG.31
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Give Tag Identifier: Item #3393
   * - ``rxg_32``
     - RXG.32
     - Optional[str]
     - optional
     - Dispense Amount: Item #3316
   * - ``rxg_33``
     - RXG.33
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Dispense Units: Item #3317 | Table HL79999

.. _hl7-v2_8_2-RXO:

.. py:class:: hl7types.hl7.v2_8_2.segments.RXO.RXO
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
     - Description
   * - ``rxo_1``
     - RXO.1
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Requested Give Code: Item #292 | Table HL79999
   * - ``rxo_2``
     - RXO.2
     - Optional[str]
     - optional
     - Requested Give Amount - Minimum: Item #293
   * - ``rxo_3``
     - RXO.3
     - Optional[str]
     - optional
     - Requested Give Amount - Maximum: Item #294
   * - ``rxo_4``
     - RXO.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Requested Give Units: Item #295 | Table HL79999
   * - ``rxo_5``
     - RXO.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Requested Dosage Form: Item #296 | Table HL79999
   * - ``rxo_6``
     - RXO.6
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Provider's Pharmacy/Treatment Instructions: Item #297 | Table HL79999
   * - ``rxo_7``
     - RXO.7
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Provider's Administration Instructions: Item #298 | Table HL79999
   * - ``rxo_9``
     - RXO.9
     - Optional[str]
     - optional
     - Allow Substitutions: Item #300 | Table HL70161
   * - ``rxo_10``
     - RXO.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Requested Dispense Code: Item #301 | Table HL79999
   * - ``rxo_11``
     - RXO.11
     - Optional[str]
     - optional
     - Requested Dispense Amount: Item #302
   * - ``rxo_12``
     - RXO.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Requested Dispense Units: Item #303 | Table HL79999
   * - ``rxo_13``
     - RXO.13
     - Optional[str]
     - optional
     - Number Of Refills: Item #304
   * - ``rxo_14``
     - RXO.14
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Ordering Provider's DEA Number: Item #305
   * - ``rxo_15``
     - RXO.15
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Pharmacist/Treatment Supplier's Verifier ID: Item #306
   * - ``rxo_16``
     - RXO.16
     - Optional[str]
     - optional
     - Needs Human Review: Item #307 | Table HL70136
   * - ``rxo_17``
     - RXO.17
     - Optional[str]
     - optional
     - Requested Give Per (Time Unit): Item #308
   * - ``rxo_18``
     - RXO.18
     - Optional[str]
     - optional
     - Requested Give Strength: Item #1121
   * - ``rxo_19``
     - RXO.19
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Requested Give Strength Units: Item #1122 | Table HL79999
   * - ``rxo_20``
     - RXO.20
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Indication: Item #1123 | Table HL79999
   * - ``rxo_21``
     - RXO.21
     - Optional[str]
     - optional
     - Requested Give Rate Amount: Item #1218
   * - ``rxo_22``
     - RXO.22
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Requested Give Rate Units: Item #1219 | Table HL79999
   * - ``rxo_23``
     - RXO.23
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Total Daily Dose: Item #329
   * - ``rxo_24``
     - RXO.24
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Supplementary Code: Item #1476 | Table HL79999
   * - ``rxo_25``
     - RXO.25
     - Optional[str]
     - optional
     - Requested Drug Strength Volume: Item #1666
   * - ``rxo_26``
     - RXO.26
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Requested Drug Strength Volume Units: Item #1667 | Table HL79999
   * - ``rxo_27``
     - RXO.27
     - Optional[str]
     - optional
     - Pharmacy Order Type: Item #1668 | Table HL70480
   * - ``rxo_28``
     - RXO.28
     - Optional[str]
     - optional
     - Dispensing Interval: Item #1669
   * - ``rxo_29``
     - RXO.29
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Medication Instance Identifier: Item #2149
   * - ``rxo_30``
     - RXO.30
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Segment Instance Identifier: Item #2150
   * - ``rxo_31``
     - RXO.31
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Mood Code: Item #2151 | Table HL70725
   * - ``rxo_32``
     - RXO.32
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Dispensing Pharmacy: Item #1681 | Table HL79999
   * - ``rxo_33``
     - RXO.33
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - Dispensing Pharmacy Address: Item #1682
   * - ``rxo_34``
     - RXO.34
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Deliver-to Patient Location: Item #1683
   * - ``rxo_35``
     - RXO.35
     - Optional[:ref:`XAD <hl7-v2_8_2-XAD>`]
     - optional
     - Deliver-to Address: Item #1684
   * - ``rxo_36``
     - RXO.36
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Pharmacy Phone Number: Item #2309

.. _hl7-v2_8_2-RXR:

.. py:class:: hl7types.hl7.v2_8_2.segments.RXR.RXR
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
     - Description
   * - ``rxr_1``
     - RXR.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Route: Item #309 | Table HL70162
   * - ``rxr_2``
     - RXR.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Administration Site: Item #310 | Table HL70550
   * - ``rxr_3``
     - RXR.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Administration Device: Item #311 | Table HL70164
   * - ``rxr_4``
     - RXR.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Administration Method: Item #312 | Table HL70165
   * - ``rxr_5``
     - RXR.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Routing Instruction: Item #1315 | Table HL79999
   * - ``rxr_6``
     - RXR.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Administration Site Modifier: Item #1670 | Table HL70495

.. _hl7-v2_8_2-RXV:

.. py:class:: hl7types.hl7.v2_8_2.segments.RXV.RXV
   :noindex:

   HL7 v2 RXV segment.

RXV
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rxv_1``
     - RXV.1
     - Optional[str]
     - optional
     - Set ID - RXV: Item #3318
   * - ``rxv_2``
     - RXV.2
     - str
     - required
     - Bolus Type: Item #3319 | Table HL70917
   * - ``rxv_3``
     - RXV.3
     - Optional[str]
     - optional
     - Bolus Dose Amount: Item #3320
   * - ``rxv_4``
     - RXV.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Bolus Dose Amount Units: Item #3321 | Table HL79999
   * - ``rxv_5``
     - RXV.5
     - Optional[str]
     - optional
     - Bolus Dose Volume: Item #3322
   * - ``rxv_6``
     - RXV.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Bolus Dose Volume Units: Item #3323 | Table HL79999
   * - ``rxv_7``
     - RXV.7
     - str
     - required
     - PCA Type: Item #3324 | Table HL70918
   * - ``rxv_8``
     - RXV.8
     - Optional[str]
     - optional
     - PCA Dose Amount: Item #3325
   * - ``rxv_9``
     - RXV.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - PCA Dose Amount Units: Item #3326 | Table HL79999
   * - ``rxv_10``
     - RXV.10
     - Optional[str]
     - optional
     - PCA Dose Amount Volume: Item #3327
   * - ``rxv_11``
     - RXV.11
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - PCA Dose Amount Volume Units: Item #3328 | Table HL79999
   * - ``rxv_12``
     - RXV.12
     - Optional[str]
     - optional
     - Max Dose Amount: Item #3329
   * - ``rxv_13``
     - RXV.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Max Dose Amount Units: Item #3330 | Table HL79999
   * - ``rxv_14``
     - RXV.14
     - Optional[str]
     - optional
     - Max Dose Amount Volume: Item #3331
   * - ``rxv_15``
     - RXV.15
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Max Dose Amount Volume Units: Item #3332 | Table HL79999
   * - ``rxv_16``
     - RXV.16
     - :ref:`CQ <hl7-v2_8_2-CQ>`
     - required
     - Max Dose per Time: Item #3333
   * - ``rxv_17``
     - RXV.17
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Lockout Interval: Item #3334
   * - ``rxv_18``
     - RXV.18
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Syringe Manufacturer: Item #3339
   * - ``rxv_19``
     - RXV.19
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Syringe Model Number: Item #3385
   * - ``rxv_20``
     - RXV.20
     - Optional[str]
     - optional
     - Syringe Size: Item #3386
   * - ``rxv_21``
     - RXV.21
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Syringe Size Units: Item #3431
   * - ``rxv_22``
     - RXV.22
     - Optional[str]
     - optional
     - Action Code: Item #816 | Table HL70206

.. _hl7-v2_8_2-SAC:

.. py:class:: hl7types.hl7.v2_8_2.segments.SAC.SAC
   :noindex:

   HL7 v2 SAC segment.

SAC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``sac_1``
     - SAC.1
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - External Accession Identifier: Item #1329
   * - ``sac_2``
     - SAC.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Accession Identifier: Item #1330
   * - ``sac_3``
     - SAC.3
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Container Identifier: Item #1331
   * - ``sac_4``
     - SAC.4
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Primary (Parent) Container Identifier: Item #1332
   * - ``sac_5``
     - SAC.5
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Equipment Container Identifier: Item #1333
   * - ``sac_7``
     - SAC.7
     - Optional[str]
     - optional
     - Registration Date/Time: Item #1334
   * - ``sac_8``
     - SAC.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Container Status: Item #1335 | Table HL70370
   * - ``sac_9``
     - SAC.9
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Carrier Type: Item #1336 | Table HL70378
   * - ``sac_10``
     - SAC.10
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Carrier Identifier: Item #1337
   * - ``sac_11``
     - SAC.11
     - Optional[:ref:`NA <hl7-v2_8_2-NA>`]
     - optional
     - Position in Carrier: Item #1338
   * - ``sac_12``
     - SAC.12
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Tray Type - SAC: Item #1339 | Table HL70379
   * - ``sac_13``
     - SAC.13
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Tray Identifier: Item #1340
   * - ``sac_14``
     - SAC.14
     - Optional[:ref:`NA <hl7-v2_8_2-NA>`]
     - optional
     - Position in Tray: Item #1341
   * - ``sac_15``
     - SAC.15
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Location: Item #1342 | Table HL79999
   * - ``sac_16``
     - SAC.16
     - Optional[str]
     - optional
     - Container Height: Item #1343
   * - ``sac_17``
     - SAC.17
     - Optional[str]
     - optional
     - Container Diameter: Item #1344
   * - ``sac_18``
     - SAC.18
     - Optional[str]
     - optional
     - Barrier Delta: Item #1345
   * - ``sac_19``
     - SAC.19
     - Optional[str]
     - optional
     - Bottom Delta: Item #1346
   * - ``sac_20``
     - SAC.20
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Container Height/Diameter/Delta Units: Item #1347 | Table HL79999
   * - ``sac_21``
     - SAC.21
     - Optional[str]
     - optional
     - Container Volume: Item #644
   * - ``sac_22``
     - SAC.22
     - Optional[str]
     - optional
     - Available Specimen Volume: Item #1349
   * - ``sac_23``
     - SAC.23
     - Optional[str]
     - optional
     - Initial Specimen Volume: Item #1350
   * - ``sac_24``
     - SAC.24
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Volume Units: Item #1351 | Table HL79999
   * - ``sac_25``
     - SAC.25
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Separator Type: Item #1352 | Table HL70380
   * - ``sac_26``
     - SAC.26
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Cap Type: Item #1353 | Table HL70381
   * - ``sac_27``
     - SAC.27
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Additive: Item #647 | Table HL70371
   * - ``sac_28``
     - SAC.28
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Specimen Component: Item #1355 | Table HL70372
   * - ``sac_29``
     - SAC.29
     - Optional[:ref:`SN <hl7-v2_8_2-SN>`]
     - optional
     - Dilution Factor: Item #1356
   * - ``sac_30``
     - SAC.30
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Treatment: Item #1357 | Table HL70373
   * - ``sac_31``
     - SAC.31
     - Optional[:ref:`SN <hl7-v2_8_2-SN>`]
     - optional
     - Temperature: Item #1358
   * - ``sac_32``
     - SAC.32
     - Optional[str]
     - optional
     - Hemolysis Index: Item #1359
   * - ``sac_33``
     - SAC.33
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Hemolysis Index Units: Item #1360 | Table HL79999
   * - ``sac_34``
     - SAC.34
     - Optional[str]
     - optional
     - Lipemia Index: Item #1361
   * - ``sac_35``
     - SAC.35
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Lipemia Index Units: Item #1362 | Table HL79999
   * - ``sac_36``
     - SAC.36
     - Optional[str]
     - optional
     - Icterus Index: Item #1363
   * - ``sac_37``
     - SAC.37
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Icterus Index Units: Item #1364 | Table HL79999
   * - ``sac_38``
     - SAC.38
     - Optional[str]
     - optional
     - Fibrin Index: Item #1365
   * - ``sac_39``
     - SAC.39
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Fibrin Index Units: Item #1366 | Table HL79999
   * - ``sac_40``
     - SAC.40
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - System Induced Contaminants: Item #1367 | Table HL70374
   * - ``sac_41``
     - SAC.41
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Drug Interference: Item #1368 | Table HL70382
   * - ``sac_42``
     - SAC.42
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Artificial Blood: Item #1369 | Table HL70375
   * - ``sac_43``
     - SAC.43
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Special Handling Code: Item #1370 | Table HL70376
   * - ``sac_44``
     - SAC.44
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Other Environmental Factors: Item #1371 | Table HL70377

.. _hl7-v2_8_2-SCD:

.. py:class:: hl7types.hl7.v2_8_2.segments.SCD.SCD
   :noindex:

   HL7 v2 SCD segment.

SCD
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``scd_1``
     - SCD.1
     - Optional[str]
     - optional
     - Cycle Start Time: Item #2104
   * - ``scd_2``
     - SCD.2
     - Optional[str]
     - optional
     - Cycle Count: Item #2105
   * - ``scd_3``
     - SCD.3
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Temp Max: Item #2106
   * - ``scd_4``
     - SCD.4
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Temp Min: Item #2107
   * - ``scd_5``
     - SCD.5
     - Optional[str]
     - optional
     - Load Number: Item #2108
   * - ``scd_6``
     - SCD.6
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Condition Time: Item #2109
   * - ``scd_7``
     - SCD.7
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Sterilize Time: Item #2110
   * - ``scd_8``
     - SCD.8
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Exhaust Time: Item #2111
   * - ``scd_9``
     - SCD.9
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Total Cycle Time: Item #2112
   * - ``scd_10``
     - SCD.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Device Status: Item #2113 | Table HL70682
   * - ``scd_11``
     - SCD.11
     - Optional[str]
     - optional
     - Cycle Start Date/Time: Item #2114
   * - ``scd_12``
     - SCD.12
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Dry Time: Item #2115
   * - ``scd_13``
     - SCD.13
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Leak Rate: Item #2116
   * - ``scd_14``
     - SCD.14
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Control Temperature: Item #2117
   * - ``scd_15``
     - SCD.15
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Sterilizer Temperature: Item #2118
   * - ``scd_16``
     - SCD.16
     - Optional[str]
     - optional
     - Cycle Complete Time: Item #2119
   * - ``scd_17``
     - SCD.17
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Under Temperature: Item #2120
   * - ``scd_18``
     - SCD.18
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Over Temperature: Item #2121
   * - ``scd_19``
     - SCD.19
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Abort Cycle: Item #2122 | Table HL70532
   * - ``scd_20``
     - SCD.20
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Alarm: Item #2123 | Table HL70532
   * - ``scd_21``
     - SCD.21
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Long in Charge Phase: Item #2124 | Table HL70532
   * - ``scd_22``
     - SCD.22
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Long in Exhaust Phase: Item #2125 | Table HL70532
   * - ``scd_23``
     - SCD.23
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Long in Fast Exhaust Phase: Item #2126 | Table HL70532
   * - ``scd_24``
     - SCD.24
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Reset: Item #2127 | Table HL70532
   * - ``scd_25``
     - SCD.25
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Operator - Unload: Item #2128
   * - ``scd_26``
     - SCD.26
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Door Open: Item #2129 | Table HL70532
   * - ``scd_27``
     - SCD.27
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Reading Failure: Item #2130 | Table HL70532
   * - ``scd_28``
     - SCD.28
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Cycle Type: Item #2131 | Table HL70702
   * - ``scd_29``
     - SCD.29
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Thermal Rinse Time: Item #2132
   * - ``scd_30``
     - SCD.30
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Wash Time: Item #2133
   * - ``scd_31``
     - SCD.31
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Injection Rate: Item #2134
   * - ``scd_32``
     - SCD.32
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Procedure Code: Item #393 | Table HL70088
   * - ``scd_33``
     - SCD.33
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Patient Identifier List: Item #106
   * - ``scd_34``
     - SCD.34
     - Optional[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - optional
     - Attending Doctor: Item #137 | Table HL70010
   * - ``scd_35``
     - SCD.35
     - Optional[:ref:`SN <hl7-v2_8_2-SN>`]
     - optional
     - Dilution Factor: Item #1356
   * - ``scd_36``
     - SCD.36
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Fill Time: Item #2139
   * - ``scd_37``
     - SCD.37
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Inlet Temperature: Item #2140

.. _hl7-v2_8_2-SCH:

.. py:class:: hl7types.hl7.v2_8_2.segments.SCH.SCH
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
     - Description
   * - ``sch_1``
     - SCH.1
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Placer Appointment ID: Item #860
   * - ``sch_2``
     - SCH.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Filler Appointment ID: Item #861
   * - ``sch_3``
     - SCH.3
     - Optional[str]
     - optional
     - Occurrence Number: Item #862
   * - ``sch_4``
     - SCH.4
     - Optional[:ref:`EIP <hl7-v2_8_2-EIP>`]
     - optional
     - Placer Group Number: Item #218
   * - ``sch_5``
     - SCH.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Schedule ID: Item #864
   * - ``sch_6``
     - SCH.6
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Event Reason: Item #883
   * - ``sch_7``
     - SCH.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Appointment Reason: Item #866 | Table HL70276
   * - ``sch_8``
     - SCH.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Appointment Type: Item #867 | Table HL70277
   * - ``sch_10``
     - SCH.10
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Appointment Duration Units: Item #869
   * - ``sch_12``
     - SCH.12
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Placer Contact Person: Item #874
   * - ``sch_13``
     - SCH.13
     - Optional[:ref:`XTN <hl7-v2_8_2-XTN>`]
     - optional
     - Placer Contact Phone Number: Item #875
   * - ``sch_14``
     - SCH.14
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Placer Contact Address: Item #876
   * - ``sch_15``
     - SCH.15
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Placer Contact Location: Item #877
   * - ``sch_16``
     - SCH.16
     - List[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - required
     - Filler Contact Person: Item #885
   * - ``sch_17``
     - SCH.17
     - Optional[:ref:`XTN <hl7-v2_8_2-XTN>`]
     - optional
     - Filler Contact Phone Number: Item #886
   * - ``sch_18``
     - SCH.18
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Filler Contact Address: Item #887
   * - ``sch_19``
     - SCH.19
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Filler Contact Location: Item #888
   * - ``sch_20``
     - SCH.20
     - List[:ref:`XCN <hl7-v2_8_2-XCN>`]
     - required
     - Entered By Person: Item #878
   * - ``sch_21``
     - SCH.21
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Entered By Phone Number: Item #879
   * - ``sch_22``
     - SCH.22
     - Optional[:ref:`PL <hl7-v2_8_2-PL>`]
     - optional
     - Entered By Location: Item #880
   * - ``sch_23``
     - SCH.23
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Parent Placer Appointment ID: Item #881
   * - ``sch_24``
     - SCH.24
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Parent Filler Appointment ID: Item #882
   * - ``sch_25``
     - SCH.25
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Filler Status Code: Item #889 | Table HL70278
   * - ``sch_26``
     - SCH.26
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Placer Order Number: Item #216
   * - ``sch_27``
     - SCH.27
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Filler Order Number: Item #217

.. _hl7-v2_8_2-SCP:

.. py:class:: hl7types.hl7.v2_8_2.segments.SCP.SCP
   :noindex:

   HL7 v2 SCP segment.

SCP
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``scp_1``
     - SCP.1
     - Optional[str]
     - optional
     - Number Of Decontamination/Sterilization Devices: Item #2087
   * - ``scp_2``
     - SCP.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Labor Calculation Type: Item #2088 | Table HL70651
   * - ``scp_3``
     - SCP.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Date Format: Item #2089 | Table HL70653
   * - ``scp_4``
     - SCP.4
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Device Number: Item #2090
   * - ``scp_5``
     - SCP.5
     - Optional[str]
     - optional
     - Device Name: Item #2279
   * - ``scp_6``
     - SCP.6
     - Optional[str]
     - optional
     - Device Model Name: Item #2091
   * - ``scp_7``
     - SCP.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Device Type: Item #2092 | Table HL70657
   * - ``scp_8``
     - SCP.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Lot Control: Item #2093 | Table HL70659

.. _hl7-v2_8_2-SDD:

.. py:class:: hl7types.hl7.v2_8_2.segments.SDD.SDD
   :noindex:

   HL7 v2 SDD segment.

SDD
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``sdd_1``
     - SDD.1
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Lot Number: Item #2098
   * - ``sdd_2``
     - SDD.2
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Device Number: Item #2099
   * - ``sdd_3``
     - SDD.3
     - Optional[str]
     - optional
     - Device Name: Item #2281
   * - ``sdd_4``
     - SDD.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Device Data State: Item #2100 | Table HL70667
   * - ``sdd_5``
     - SDD.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Load Status: Item #2101 | Table HL70669
   * - ``sdd_6``
     - SDD.6
     - Optional[str]
     - optional
     - Control Code: Item #2102
   * - ``sdd_7``
     - SDD.7
     - Optional[str]
     - optional
     - Operator Name: Item #2103

.. _hl7-v2_8_2-SFT:

.. py:class:: hl7types.hl7.v2_8_2.segments.SFT.SFT
   :noindex:

   HL7 v2 SFT segment.

SFT
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``sft_1``
     - SFT.1
     - :ref:`XON <hl7-v2_8_2-XON>`
     - required
     - Software Vendor Organization: Item #1834
   * - ``sft_2``
     - SFT.2
     - str
     - required
     - Software Certified Version or Release Number: Item #1835
   * - ``sft_3``
     - SFT.3
     - str
     - required
     - Software Product Name: Item #1836
   * - ``sft_4``
     - SFT.4
     - str
     - required
     - Software Binary ID: Item #1837
   * - ``sft_5``
     - SFT.5
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Software Product Information: Item #1838
   * - ``sft_6``
     - SFT.6
     - Optional[str]
     - optional
     - Software Install Date: Item #1839

.. _hl7-v2_8_2-SGH:

.. py:class:: hl7types.hl7.v2_8_2.segments.SGH.SGH
   :noindex:

   HL7 v2 SGH segment.

SGH
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``sgh_1``
     - SGH.1
     - str
     - required
     - Set ID - SGH: Item #3389
   * - ``sgh_2``
     - SGH.2
     - Optional[str]
     - optional
     - Segment Group Name: Item #3390

.. _hl7-v2_8_2-SGT:

.. py:class:: hl7types.hl7.v2_8_2.segments.SGT.SGT
   :noindex:

   HL7 v2 SGT segment.

SGT
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``sgt_1``
     - SGT.1
     - str
     - required
     - Set ID - SGT: Item #3394
   * - ``sgt_2``
     - SGT.2
     - Optional[str]
     - optional
     - Segment Group Name: Item #3395

.. _hl7-v2_8_2-SHP:

.. py:class:: hl7types.hl7.v2_8_2.segments.SHP.SHP
   :noindex:

   HL7 v2 SHP segment.

SHP
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``shp_1``
     - SHP.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Shipment ID: Item #2317
   * - ``shp_2``
     - SHP.2
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Internal Shipment ID: Item #2318
   * - ``shp_3``
     - SHP.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Shipment Status: Item #2319 | Table HL70905
   * - ``shp_4``
     - SHP.4
     - str
     - required
     - Shipment Status Date/Time: Item #2320
   * - ``shp_5``
     - SHP.5
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Shipment Status Reason: Item #2321
   * - ``shp_6``
     - SHP.6
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Shipment Priority: Item #2322 | Table HL70906
   * - ``shp_7``
     - SHP.7
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Shipment Confidentiality: Item #2323 | Table HL70907
   * - ``shp_8``
     - SHP.8
     - Optional[str]
     - optional
     - Number of Packages in Shipment: Item #2324
   * - ``shp_9``
     - SHP.9
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Shipment Condition: Item #2325 | Table HL70544
   * - ``shp_10``
     - SHP.10
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Shipment Handling Code: Item #2326 | Table HL70376
   * - ``shp_11``
     - SHP.11
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Shipment Risk Code: Item #2327 | Table HL70489

.. _hl7-v2_8_2-SID:

.. py:class:: hl7types.hl7.v2_8_2.segments.SID.SID
   :noindex:

   HL7 v2 SID segment.

SID
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``sid_1``
     - SID.1
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Application/Method Identifier: Item #1426 | Table HL79999
   * - ``sid_2``
     - SID.2
     - Optional[str]
     - optional
     - Substance Lot Number: Item #1129
   * - ``sid_3``
     - SID.3
     - Optional[str]
     - optional
     - Substance Container Identifier: Item #1428
   * - ``sid_4``
     - SID.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Substance Manufacturer Identifier: Item #1429 | Table HL70385

.. _hl7-v2_8_2-SLT:

.. py:class:: hl7types.hl7.v2_8_2.segments.SLT.SLT
   :noindex:

   HL7 v2 SLT segment.

SLT
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``slt_1``
     - SLT.1
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Device Number: Item #2094
   * - ``slt_2``
     - SLT.2
     - Optional[str]
     - optional
     - Device Name: Item #2280
   * - ``slt_3``
     - SLT.3
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Lot Number: Item #2095
   * - ``slt_4``
     - SLT.4
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Item Identifier: Item #2096
   * - ``slt_5``
     - SLT.5
     - Optional[str]
     - optional
     - Bar Code: Item #2097

.. _hl7-v2_8_2-SPM:

.. py:class:: hl7types.hl7.v2_8_2.segments.SPM.SPM
   :noindex:

   HL7 v2 SPM segment.

SPM
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``spm_1``
     - SPM.1
     - Optional[str]
     - optional
     - Set ID - SPM: Item #1754
   * - ``spm_2``
     - SPM.2
     - Optional[:ref:`EIP <hl7-v2_8_2-EIP>`]
     - optional
     - Specimen ID: Item #1755
   * - ``spm_3``
     - SPM.3
     - Optional[List[:ref:`EIP <hl7-v2_8_2-EIP>`]]
     - optional
     - Specimen Parent IDs: Item #1756
   * - ``spm_4``
     - SPM.4
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Specimen Type: Item #1900 | Table HL70487
   * - ``spm_5``
     - SPM.5
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Specimen Type Modifier: Item #1757 | Table HL70541
   * - ``spm_6``
     - SPM.6
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Specimen Additives: Item #1758 | Table HL70371
   * - ``spm_7``
     - SPM.7
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Specimen Collection Method: Item #1759 | Table HL70488
   * - ``spm_8``
     - SPM.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Specimen Source Site: Item #1901 | Table HL79999
   * - ``spm_9``
     - SPM.9
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Specimen Source Site Modifier: Item #1760 | Table HL70542
   * - ``spm_10``
     - SPM.10
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Specimen Collection Site: Item #1761 | Table HL70543
   * - ``spm_11``
     - SPM.11
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Specimen Role: Item #1762 | Table HL70369
   * - ``spm_12``
     - SPM.12
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Specimen Collection Amount: Item #1902
   * - ``spm_13``
     - SPM.13
     - Optional[str]
     - optional
     - Grouped Specimen Count: Item #1763
   * - ``spm_14``
     - SPM.14
     - Optional[List[str]]
     - optional
     - Specimen Description: Item #1764
   * - ``spm_15``
     - SPM.15
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Specimen Handling Code: Item #1908 | Table HL70376
   * - ``spm_16``
     - SPM.16
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Specimen Risk Code: Item #1903 | Table HL70489
   * - ``spm_17``
     - SPM.17
     - Optional[:ref:`DR <hl7-v2_8_2-DR>`]
     - optional
     - Specimen Collection Date/Time: Item #1765
   * - ``spm_18``
     - SPM.18
     - Optional[str]
     - optional
     - Specimen Received Date/Time *: Item #248
   * - ``spm_19``
     - SPM.19
     - Optional[str]
     - optional
     - Specimen Expiration Date/Time: Item #1904
   * - ``spm_20``
     - SPM.20
     - Optional[str]
     - optional
     - Specimen Availability: Item #1766 | Table HL70136
   * - ``spm_21``
     - SPM.21
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Specimen Reject Reason: Item #1767 | Table HL70490
   * - ``spm_22``
     - SPM.22
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Specimen Quality: Item #1768 | Table HL70491
   * - ``spm_23``
     - SPM.23
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Specimen Appropriateness: Item #1769 | Table HL70492
   * - ``spm_24``
     - SPM.24
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Specimen Condition: Item #1770 | Table HL70493
   * - ``spm_25``
     - SPM.25
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Specimen Current Quantity: Item #1771
   * - ``spm_26``
     - SPM.26
     - Optional[str]
     - optional
     - Number of Specimen Containers: Item #1772
   * - ``spm_27``
     - SPM.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Container Type: Item #1773 | Table HL79999
   * - ``spm_28``
     - SPM.28
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Container Condition: Item #1774 | Table HL70544
   * - ``spm_29``
     - SPM.29
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Specimen Child Role: Item #1775 | Table HL70494
   * - ``spm_30``
     - SPM.30
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Accession ID: Item #2314
   * - ``spm_31``
     - SPM.31
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Other Specimen ID: Item #2315
   * - ``spm_32``
     - SPM.32
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Shipment ID: Item #2316

.. _hl7-v2_8_2-STF:

.. py:class:: hl7types.hl7.v2_8_2.segments.STF.STF
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
     - Description
   * - ``stf_1``
     - STF.1
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Primary Key Value - STF: Item #671 | Table HL79999
   * - ``stf_2``
     - STF.2
     - Optional[List[:ref:`CX <hl7-v2_8_2-CX>`]]
     - optional
     - Staff Identifier List: Item #672 | Table HL70061
   * - ``stf_3``
     - STF.3
     - Optional[List[:ref:`XPN <hl7-v2_8_2-XPN>`]]
     - optional
     - Staff Name: Item #673
   * - ``stf_4``
     - STF.4
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Staff Type: Item #674 | Table HL70182
   * - ``stf_5``
     - STF.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Administrative Sex: Item #111 | Table HL70001
   * - ``stf_6``
     - STF.6
     - Optional[str]
     - optional
     - Date/Time of Birth: Item #110
   * - ``stf_7``
     - STF.7
     - Optional[str]
     - optional
     - Active/Inactive Flag: Item #675 | Table HL70183
   * - ``stf_8``
     - STF.8
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Department: Item #676 | Table HL70184
   * - ``stf_9``
     - STF.9
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Hospital Service - STF: Item #677 | Table HL70069
   * - ``stf_10``
     - STF.10
     - Optional[List[:ref:`XTN <hl7-v2_8_2-XTN>`]]
     - optional
     - Phone: Item #678
   * - ``stf_11``
     - STF.11
     - Optional[List[:ref:`XAD <hl7-v2_8_2-XAD>`]]
     - optional
     - Office/Home Address/Birthplace: Item #679
   * - ``stf_12``
     - STF.12
     - Optional[List[:ref:`DIN <hl7-v2_8_2-DIN>`]]
     - optional
     - Institution Activation Date: Item #680 | Table HL70537
   * - ``stf_13``
     - STF.13
     - Optional[List[:ref:`DIN <hl7-v2_8_2-DIN>`]]
     - optional
     - Institution Inactivation Date: Item #681 | Table HL70537
   * - ``stf_14``
     - STF.14
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Backup Person ID: Item #682
   * - ``stf_15``
     - STF.15
     - Optional[List[str]]
     - optional
     - E-Mail Address: Item #683
   * - ``stf_16``
     - STF.16
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Preferred Method of Contact: Item #684 | Table HL70185
   * - ``stf_17``
     - STF.17
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Marital Status: Item #119 | Table HL70002
   * - ``stf_18``
     - STF.18
     - Optional[str]
     - optional
     - Job Title: Item #785
   * - ``stf_19``
     - STF.19
     - Optional[:ref:`JCC <hl7-v2_8_2-JCC>`]
     - optional
     - Job Code/Class: Item #786
   * - ``stf_20``
     - STF.20
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Employment Status Code: Item #1276 | Table HL70066
   * - ``stf_21``
     - STF.21
     - Optional[str]
     - optional
     - Additional Insured on Auto: Item #1275 | Table HL70136
   * - ``stf_22``
     - STF.22
     - Optional[:ref:`DLN <hl7-v2_8_2-DLN>`]
     - optional
     - Driver's License Number - Staff: Item #1302
   * - ``stf_23``
     - STF.23
     - Optional[str]
     - optional
     - Copy Auto Ins: Item #1229 | Table HL70136
   * - ``stf_24``
     - STF.24
     - Optional[str]
     - optional
     - Auto Ins Expires: Item #1232
   * - ``stf_25``
     - STF.25
     - Optional[str]
     - optional
     - Date Last DMV Review: Item #1298
   * - ``stf_26``
     - STF.26
     - Optional[str]
     - optional
     - Date Next DMV Review: Item #1234
   * - ``stf_27``
     - STF.27
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Race: Item #113 | Table HL70005
   * - ``stf_28``
     - STF.28
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Ethnic Group: Item #125 | Table HL70189
   * - ``stf_29``
     - STF.29
     - Optional[str]
     - optional
     - Re-activation Approval Indicator: Item #1596 | Table HL70136
   * - ``stf_30``
     - STF.30
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Citizenship: Item #129 | Table HL70171
   * - ``stf_31``
     - STF.31
     - Optional[str]
     - optional
     - Date/Time of Death: Item #1886
   * - ``stf_32``
     - STF.32
     - Optional[str]
     - optional
     - Death Indicator: Item #1887 | Table HL70136
   * - ``stf_33``
     - STF.33
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Institution Relationship Type Code: Item #1888 | Table HL70538
   * - ``stf_34``
     - STF.34
     - Optional[:ref:`DR <hl7-v2_8_2-DR>`]
     - optional
     - Institution Relationship Period: Item #1889
   * - ``stf_35``
     - STF.35
     - Optional[str]
     - optional
     - Expected Return Date: Item #1890
   * - ``stf_36``
     - STF.36
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Cost Center Code: Item #1891 | Table HL70539
   * - ``stf_37``
     - STF.37
     - Optional[str]
     - optional
     - Generic Classification Indicator: Item #1892 | Table HL70136
   * - ``stf_38``
     - STF.38
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Inactive Reason Code: Item #1893 | Table HL70540
   * - ``stf_39``
     - STF.39
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Generic resource type or category: Item #2184 | Table HL70771
   * - ``stf_40``
     - STF.40
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Religion: Item #120 | Table HL70006
   * - ``stf_41``
     - STF.41
     - Optional[:ref:`ED <hl7-v2_8_2-ED>`]
     - optional
     - Signature: Item #1861

.. _hl7-v2_8_2-STZ:

.. py:class:: hl7types.hl7.v2_8_2.segments.STZ.STZ
   :noindex:

   HL7 v2 STZ segment.

STZ
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``stz_1``
     - STZ.1
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Sterilization Type: Item #2213 | Table HL70806
   * - ``stz_2``
     - STZ.2
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Sterilization Cycle: Item #2214 | Table HL70702
   * - ``stz_3``
     - STZ.3
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Maintenance Cycle: Item #2215 | Table HL70809
   * - ``stz_4``
     - STZ.4
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Maintenance Type: Item #2216 | Table HL70811

.. _hl7-v2_8_2-TCC:

.. py:class:: hl7types.hl7.v2_8_2.segments.TCC.TCC
   :noindex:

   HL7 v2 TCC segment.

TCC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``tcc_1``
     - TCC.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Universal Service Identifier: Item #238
   * - ``tcc_2``
     - TCC.2
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Equipment Test Application Identifier: Item #1408
   * - ``tcc_4``
     - TCC.4
     - Optional[:ref:`SN <hl7-v2_8_2-SN>`]
     - optional
     - Auto-Dilution Factor Default: Item #1410
   * - ``tcc_5``
     - TCC.5
     - Optional[:ref:`SN <hl7-v2_8_2-SN>`]
     - optional
     - Rerun Dilution Factor Default: Item #1411
   * - ``tcc_6``
     - TCC.6
     - Optional[:ref:`SN <hl7-v2_8_2-SN>`]
     - optional
     - Pre-Dilution Factor Default: Item #1412
   * - ``tcc_7``
     - TCC.7
     - Optional[:ref:`SN <hl7-v2_8_2-SN>`]
     - optional
     - Endogenous Content of Pre-Dilution Diluent: Item #1413
   * - ``tcc_8``
     - TCC.8
     - Optional[str]
     - optional
     - Inventory Limits Warning Level: Item #1414
   * - ``tcc_9``
     - TCC.9
     - Optional[str]
     - optional
     - Automatic Rerun Allowed: Item #1415 | Table HL70136
   * - ``tcc_10``
     - TCC.10
     - Optional[str]
     - optional
     - Automatic Repeat Allowed: Item #1416 | Table HL70136
   * - ``tcc_11``
     - TCC.11
     - Optional[str]
     - optional
     - Automatic Reflex Allowed: Item #1417 | Table HL70136
   * - ``tcc_12``
     - TCC.12
     - Optional[:ref:`SN <hl7-v2_8_2-SN>`]
     - optional
     - Equipment Dynamic Range: Item #1418
   * - ``tcc_13``
     - TCC.13
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Units: Item #574 | Table HL79999
   * - ``tcc_14``
     - TCC.14
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Processing Type: Item #1419 | Table HL70388
   * - ``tcc_15``
     - TCC.15
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Test Criticality: Item #3313

.. _hl7-v2_8_2-TCD:

.. py:class:: hl7types.hl7.v2_8_2.segments.TCD.TCD
   :noindex:

   HL7 v2 TCD segment.

TCD
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``tcd_1``
     - TCD.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Universal Service Identifier: Item #238
   * - ``tcd_2``
     - TCD.2
     - Optional[:ref:`SN <hl7-v2_8_2-SN>`]
     - optional
     - Auto-Dilution Factor: Item #1420
   * - ``tcd_3``
     - TCD.3
     - Optional[:ref:`SN <hl7-v2_8_2-SN>`]
     - optional
     - Rerun Dilution Factor: Item #1421
   * - ``tcd_4``
     - TCD.4
     - Optional[:ref:`SN <hl7-v2_8_2-SN>`]
     - optional
     - Pre-Dilution Factor: Item #1422
   * - ``tcd_5``
     - TCD.5
     - Optional[:ref:`SN <hl7-v2_8_2-SN>`]
     - optional
     - Endogenous Content of Pre-Dilution Diluent: Item #1413
   * - ``tcd_6``
     - TCD.6
     - Optional[str]
     - optional
     - Automatic Repeat Allowed: Item #1416 | Table HL70136
   * - ``tcd_7``
     - TCD.7
     - Optional[str]
     - optional
     - Reflex Allowed: Item #1424 | Table HL70136
   * - ``tcd_8``
     - TCD.8
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Analyte Repeat Status: Item #1425 | Table HL70389

.. _hl7-v2_8_2-TQ1:

.. py:class:: hl7types.hl7.v2_8_2.segments.TQ1.TQ1
   :noindex:

   HL7 v2 TQ1 segment.

TQ1
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``tq1_1``
     - TQ1.1
     - Optional[str]
     - optional
     - Set ID - TQ1: Item #1627
   * - ``tq1_2``
     - TQ1.2
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Quantity: Item #1628
   * - ``tq1_3``
     - TQ1.3
     - Optional[List[:ref:`RPT <hl7-v2_8_2-RPT>`]]
     - optional
     - Repeat Pattern: Item #1629
   * - ``tq1_4``
     - TQ1.4
     - Optional[List[str]]
     - optional
     - Explicit Time: Item #1630
   * - ``tq1_5``
     - TQ1.5
     - Optional[List[:ref:`CQ <hl7-v2_8_2-CQ>`]]
     - optional
     - Relative Time and Units: Item #1631
   * - ``tq1_6``
     - TQ1.6
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Service Duration: Item #1632
   * - ``tq1_7``
     - TQ1.7
     - Optional[str]
     - optional
     - Start date/time: Item #1633
   * - ``tq1_8``
     - TQ1.8
     - Optional[str]
     - optional
     - End date/time: Item #1634
   * - ``tq1_9``
     - TQ1.9
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Priority: Item #1635 | Table HL70485
   * - ``tq1_10``
     - TQ1.10
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Condition text: Item #1636
   * - ``tq1_11``
     - TQ1.11
     - Optional[:ref:`TX <hl7-v2_8_2-TX>`]
     - optional
     - Text instruction: Item #1637
   * - ``tq1_12``
     - TQ1.12
     - Optional[str]
     - optional
     - Conjunction: Item #1638 | Table HL70472
   * - ``tq1_13``
     - TQ1.13
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Occurrence duration: Item #1639
   * - ``tq1_14``
     - TQ1.14
     - Optional[str]
     - optional
     - Total occurrences: Item #1640

.. _hl7-v2_8_2-TQ2:

.. py:class:: hl7types.hl7.v2_8_2.segments.TQ2.TQ2
   :noindex:

   HL7 v2 TQ2 segment.

TQ2
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``tq2_1``
     - TQ2.1
     - Optional[str]
     - optional
     - Set ID - TQ2: Item #1648
   * - ``tq2_2``
     - TQ2.2
     - Optional[str]
     - optional
     - Sequence/Results Flag: Item #1649 | Table HL70503
   * - ``tq2_3``
     - TQ2.3
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Related Placer Number: Item #1650
   * - ``tq2_4``
     - TQ2.4
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Related Filler Number: Item #1651
   * - ``tq2_5``
     - TQ2.5
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Related Placer Group Number: Item #1652
   * - ``tq2_6``
     - TQ2.6
     - Optional[str]
     - optional
     - Sequence Condition Code: Item #1653 | Table HL70504
   * - ``tq2_7``
     - TQ2.7
     - Optional[str]
     - optional
     - Cyclic Entry/Exit Indicator: Item #1654 | Table HL70505
   * - ``tq2_8``
     - TQ2.8
     - Optional[:ref:`CQ <hl7-v2_8_2-CQ>`]
     - optional
     - Sequence Condition Time Interval: Item #1655
   * - ``tq2_9``
     - TQ2.9
     - Optional[str]
     - optional
     - Cyclic Group Maximum Number of Repeats: Item #1656
   * - ``tq2_10``
     - TQ2.10
     - Optional[str]
     - optional
     - Special Service Request Relationship: Item #1657 | Table HL70506

.. _hl7-v2_8_2-TXA:

.. py:class:: hl7types.hl7.v2_8_2.segments.TXA.TXA
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
     - Description
   * - ``txa_1``
     - TXA.1
     - str
     - required
     - Set ID- TXA: Item #914
   * - ``txa_2``
     - TXA.2
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - Document Type: Item #915 | Table HL70270
   * - ``txa_3``
     - TXA.3
     - Optional[str]
     - optional
     - Document Content Presentation: Item #916 | Table HL70191
   * - ``txa_4``
     - TXA.4
     - Optional[str]
     - optional
     - Activity Date/Time: Item #917
   * - ``txa_5``
     - TXA.5
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Primary Activity Provider Code/Name: Item #918
   * - ``txa_6``
     - TXA.6
     - Optional[str]
     - optional
     - Origination Date/Time: Item #919
   * - ``txa_7``
     - TXA.7
     - Optional[str]
     - optional
     - Transcription Date/Time: Item #920
   * - ``txa_8``
     - TXA.8
     - Optional[List[str]]
     - optional
     - Edit Date/Time: Item #921
   * - ``txa_9``
     - TXA.9
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Originator Code/Name: Item #922
   * - ``txa_10``
     - TXA.10
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Assigned Document Authenticator: Item #923
   * - ``txa_11``
     - TXA.11
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Transcriptionist Code/Name: Item #924
   * - ``txa_12``
     - TXA.12
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Unique Document Number: Item #925
   * - ``txa_13``
     - TXA.13
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Parent Document Number: Item #926
   * - ``txa_14``
     - TXA.14
     - Optional[List[:ref:`EI <hl7-v2_8_2-EI>`]]
     - optional
     - Placer Order Number: Item #216
   * - ``txa_15``
     - TXA.15
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Filler Order Number: Item #217
   * - ``txa_16``
     - TXA.16
     - Optional[str]
     - optional
     - Unique Document File Name: Item #927
   * - ``txa_17``
     - TXA.17
     - str
     - required
     - Document Completion Status: Item #928 | Table HL70271
   * - ``txa_18``
     - TXA.18
     - Optional[str]
     - optional
     - Document Confidentiality Status: Item #929 | Table HL70272
   * - ``txa_19``
     - TXA.19
     - Optional[str]
     - optional
     - Document Availability Status: Item #930 | Table HL70273
   * - ``txa_20``
     - TXA.20
     - Optional[str]
     - optional
     - Document Storage Status: Item #932 | Table HL70275
   * - ``txa_21``
     - TXA.21
     - Optional[str]
     - optional
     - Document Change Reason: Item #933
   * - ``txa_22``
     - TXA.22
     - Optional[List[:ref:`PPN <hl7-v2_8_2-PPN>`]]
     - optional
     - Authentication Person, Time Stamp (set): Item #934
   * - ``txa_23``
     - TXA.23
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Distributed Copies (Code and Name of Recipient(s) ): Item #935
   * - ``txa_24``
     - TXA.24
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Folder Assignment: Item #2378
   * - ``txa_25``
     - TXA.25
     - Optional[List[str]]
     - optional
     - Document Title: Item #3301
   * - ``txa_26``
     - TXA.26
     - Optional[str]
     - optional
     - Agreed Due Date/Time: Item #3302

.. _hl7-v2_8_2-UAC:

.. py:class:: hl7types.hl7.v2_8_2.segments.UAC.UAC
   :noindex:

   HL7 v2 UAC segment.

UAC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``uac_1``
     - UAC.1
     - :ref:`CWE <hl7-v2_8_2-CWE>`
     - required
     - User Authentication Credential Type Code: Item #2267 | Table HL70615
   * - ``uac_2``
     - UAC.2
     - :ref:`ED <hl7-v2_8_2-ED>`
     - required
     - User Authentication Credential: Item #2268

.. _hl7-v2_8_2-UB2:

.. py:class:: hl7types.hl7.v2_8_2.segments.UB2.UB2
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
     - Description
   * - ``ub2_1``
     - UB2.1
     - Optional[str]
     - optional
     - Set ID - UB2: Item #553
   * - ``ub2_2``
     - UB2.2
     - Optional[str]
     - optional
     - Co-Insurance Days (9): Item #554
   * - ``ub2_3``
     - UB2.3
     - Optional[List[:ref:`CWE <hl7-v2_8_2-CWE>`]]
     - optional
     - Condition Code (24-30): Item #555 | Table HL70043
   * - ``ub2_4``
     - UB2.4
     - Optional[str]
     - optional
     - Covered Days (7): Item #556
   * - ``ub2_5``
     - UB2.5
     - Optional[str]
     - optional
     - Non-Covered Days (8): Item #557
   * - ``ub2_6``
     - UB2.6
     - Optional[List[:ref:`UVC <hl7-v2_8_2-UVC>`]]
     - optional
     - Value Amount & Code (39-41): Item #558
   * - ``ub2_7``
     - UB2.7
     - Optional[List[:ref:`OCD <hl7-v2_8_2-OCD>`]]
     - optional
     - Occurrence Code & Date (32-35): Item #559
   * - ``ub2_8``
     - UB2.8
     - Optional[List[:ref:`OSP <hl7-v2_8_2-OSP>`]]
     - optional
     - Occurrence Span Code/Dates (36): Item #560
   * - ``ub2_9``
     - UB2.9
     - Optional[List[str]]
     - optional
     - Uniform Billing Locator 2 (state): Item #561
   * - ``ub2_10``
     - UB2.10
     - Optional[List[str]]
     - optional
     - Uniform Billing Locator 11 (state): Item #562
   * - ``ub2_11``
     - UB2.11
     - Optional[str]
     - optional
     - Uniform Billing Locator 31 (national): Item #563
   * - ``ub2_12``
     - UB2.12
     - Optional[List[str]]
     - optional
     - Document Control Number: Item #564
   * - ``ub2_13``
     - UB2.13
     - Optional[List[str]]
     - optional
     - Uniform Billing Locator 49 (national): Item #565
   * - ``ub2_14``
     - UB2.14
     - Optional[List[str]]
     - optional
     - Uniform Billing Locator 56 (state): Item #566
   * - ``ub2_15``
     - UB2.15
     - Optional[str]
     - optional
     - Uniform Billing Locator 57 (sational): Item #567
   * - ``ub2_16``
     - UB2.16
     - Optional[List[str]]
     - optional
     - Uniform Billing Locator 78 (state): Item #568
   * - ``ub2_17``
     - UB2.17
     - Optional[str]
     - optional
     - Special Visit Count: Item #815

.. _hl7-v2_8_2-VAR:

.. py:class:: hl7types.hl7.v2_8_2.segments.VAR.VAR
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
     - Description
   * - ``var_1``
     - VAR.1
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Variance Instance ID: Item #1212
   * - ``var_2``
     - VAR.2
     - str
     - required
     - Documented Date/Time: Item #1213
   * - ``var_3``
     - VAR.3
     - Optional[str]
     - optional
     - Stated Variance Date/Time: Item #1214
   * - ``var_4``
     - VAR.4
     - Optional[List[:ref:`XCN <hl7-v2_8_2-XCN>`]]
     - optional
     - Variance Originator: Item #1215
   * - ``var_5``
     - VAR.5
     - Optional[:ref:`CWE <hl7-v2_8_2-CWE>`]
     - optional
     - Variance Classification: Item #1216
   * - ``var_6``
     - VAR.6
     - Optional[List[str]]
     - optional
     - Variance Description: Item #1217

.. _hl7-v2_8_2-VND:

.. py:class:: hl7types.hl7.v2_8_2.segments.VND.VND
   :noindex:

   HL7 v2 VND segment.

VND
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``vnd_1``
     - VND.1
     - str
     - required
     - Set Id - VND: Item #2217
   * - ``vnd_2``
     - VND.2
     - :ref:`EI <hl7-v2_8_2-EI>`
     - required
     - Vendor Identifier: Item #2218
   * - ``vnd_3``
     - VND.3
     - Optional[str]
     - optional
     - Vendor Name: Item #2276
   * - ``vnd_4``
     - VND.4
     - Optional[:ref:`EI <hl7-v2_8_2-EI>`]
     - optional
     - Vendor Catalog Number: Item #2219
   * - ``vnd_5``
     - VND.5
     - Optional[:ref:`CNE <hl7-v2_8_2-CNE>`]
     - optional
     - Primary Vendor Indicator: Item #2220 | Table HL70532
