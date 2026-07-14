v2.7.1 Segments
===============

.. _hl7-v2_7_1-ABS:

ABS Abstract (S6.5.12).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ABS.ABS
   :noindex:

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
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1514 | Table HL70010
   * - ``abs_2``
     - ABS.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1515 | Table HL70069
   * - ``abs_3``
     - ABS.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1516 | Table HL70421
   * - ``abs_4``
     - ABS.4
     - Optional[str]
     - optional
     - Item #1517
   * - ``abs_5``
     - ABS.5
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1518
   * - ``abs_6``
     - ABS.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1519 | Table HL70422
   * - ``abs_7``
     - ABS.7
     - Optional[str]
     - optional
     - Item #1520
   * - ``abs_8``
     - ABS.8
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1521
   * - ``abs_9``
     - ABS.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1522 | Table HL70423
   * - ``abs_10``
     - ABS.10
     - Optional[str]
     - optional
     - Item #1523 | Table HL70136
   * - ``abs_11``
     - ABS.11
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1524 | Table HL70424
   * - ``abs_12``
     - ABS.12
     - Optional[str]
     - optional
     - Item #1525
   * - ``abs_13``
     - ABS.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1526 | Table HL70425
   * - ``abs_14``
     - ABS.14
     - Optional[str]
     - optional
     - Item #1527 | Table HL70136

.. _hl7-v2_7_1-ACC:

ACC Accident (S6.5.9).
~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ACC.ACC
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
     - Optional[str]
     - optional
     - Item #527
   * - ``acc_2``
     - ACC.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #528 | Table HL70050
   * - ``acc_3``
     - ACC.3
     - Optional[str]
     - optional
     - Item #529
   * - ``acc_4``
     - ACC.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #812 | Table HL70347
   * - ``acc_5``
     - ACC.5
     - Optional[str]
     - optional
     - Item #813 | Table HL70136
   * - ``acc_6``
     - ACC.6
     - Optional[str]
     - optional
     - Item #814 | Table HL70136
   * - ``acc_7``
     - ACC.7
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #224
   * - ``acc_8``
     - ACC.8
     - Optional[str]
     - optional
     - Item #1503
   * - ``acc_9``
     - ACC.9
     - Optional[str]
     - optional
     - Item #1504
   * - ``acc_10``
     - ACC.10
     - Optional[str]
     - optional
     - Item #1505 | Table HL70136
   * - ``acc_11``
     - ACC.11
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1853
   * - ``acc_12``
     - ACC.12
     - Optional[str]
     - optional
     - Item #2374

.. _hl7-v2_7_1-ADD:

ADD Addendum (S2.14.1).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ADD.ADD
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

.. _hl7-v2_7_1-ADJ:

ADJ Adjustment (S16.4.7).
~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ADJ.ADJ
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2003
   * - ``adj_2``
     - ADJ.2
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2004
   * - ``adj_3``
     - ADJ.3
     - str
     - required
     - Item #2005
   * - ``adj_4``
     - ADJ.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #2006 | Table HL70564
   * - ``adj_5``
     - ADJ.5
     - Optional[List[:ref:`CP <hl7-v2_7_1-CP>`]]
     - optional
     - Item #2007
   * - ``adj_6``
     - ADJ.6
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2008 | Table HL70560
   * - ``adj_7``
     - ADJ.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2009 | Table HL70565
   * - ``adj_8``
     - ADJ.8
     - Optional[str]
     - optional
     - Item #2010
   * - ``adj_9``
     - ADJ.9
     - Optional[str]
     - optional
     - Item #2011
   * - ``adj_10``
     - ADJ.10
     - Optional[str]
     - optional
     - Item #2012
   * - ``adj_11``
     - ADJ.11
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2013 | Table HL70569
   * - ``adj_12``
     - ADJ.12
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2014
   * - ``adj_13``
     - ADJ.13
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2015
   * - ``adj_14``
     - ADJ.14
     - str
     - required
     - Item #2016
   * - ``adj_15``
     - ADJ.15
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #2017

.. _hl7-v2_7_1-AFF:

AFF Professional Affiliation (S15.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.AFF.AFF
   :noindex:

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
     - Item #1427
   * - ``aff_2``
     - AFF.2
     - :ref:`XON <hl7-v2_7_1-XON>`
     - required
     - Item #1444
   * - ``aff_3``
     - AFF.3
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1445
   * - ``aff_4``
     - AFF.4
     - Optional[List[:ref:`DR <hl7-v2_7_1-DR>`]]
     - optional
     - Item #1446
   * - ``aff_5``
     - AFF.5
     - Optional[str]
     - optional
     - Item #1447

.. _hl7-v2_7_1-AIG:

AIG Appointment Information - General Resource (S10.6.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.AIG.AIG
   :noindex:

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
     - Item #896
   * - ``aig_2``
     - AIG.2
     - Optional[str]
     - optional
     - Item #763 | Table HL70206
   * - ``aig_3``
     - AIG.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #897
   * - ``aig_4``
     - AIG.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #898
   * - ``aig_5``
     - AIG.5
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #899
   * - ``aig_6``
     - AIG.6
     - Optional[str]
     - optional
     - Item #900
   * - ``aig_7``
     - AIG.7
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #901
   * - ``aig_8``
     - AIG.8
     - Optional[str]
     - optional
     - Item #1202
   * - ``aig_9``
     - AIG.9
     - Optional[str]
     - optional
     - Item #891
   * - ``aig_10``
     - AIG.10
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #892
   * - ``aig_11``
     - AIG.11
     - Optional[str]
     - optional
     - Item #893
   * - ``aig_12``
     - AIG.12
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #894
   * - ``aig_13``
     - AIG.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #895 | Table HL70279
   * - ``aig_14``
     - AIG.14
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #889 | Table HL70278

.. _hl7-v2_7_1-AIL:

AIL Appointment Information - Location Resource (S10.6.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.AIL.AIL
   :noindex:

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
     - Item #902
   * - ``ail_2``
     - AIL.2
     - Optional[str]
     - optional
     - Item #763 | Table HL70206
   * - ``ail_3``
     - AIL.3
     - Optional[List[:ref:`PL <hl7-v2_7_1-PL>`]]
     - optional
     - Item #903
   * - ``ail_4``
     - AIL.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #904 | Table HL70305
   * - ``ail_5``
     - AIL.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #905
   * - ``ail_6``
     - AIL.6
     - Optional[str]
     - optional
     - Item #1202
   * - ``ail_7``
     - AIL.7
     - Optional[str]
     - optional
     - Item #891
   * - ``ail_8``
     - AIL.8
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #892
   * - ``ail_9``
     - AIL.9
     - Optional[str]
     - optional
     - Item #893
   * - ``ail_10``
     - AIL.10
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #894
   * - ``ail_11``
     - AIL.11
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #895 | Table HL70279
   * - ``ail_12``
     - AIL.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #889 | Table HL70278

.. _hl7-v2_7_1-AIP:

AIP Appointment Information - Personnel Resource (S10.6.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.AIP.AIP
   :noindex:

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
     - Item #906
   * - ``aip_2``
     - AIP.2
     - Optional[str]
     - optional
     - Item #763 | Table HL70206
   * - ``aip_3``
     - AIP.3
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #913
   * - ``aip_4``
     - AIP.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #907 | Table HL70182
   * - ``aip_5``
     - AIP.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #899
   * - ``aip_6``
     - AIP.6
     - Optional[str]
     - optional
     - Item #1202
   * - ``aip_7``
     - AIP.7
     - Optional[str]
     - optional
     - Item #891
   * - ``aip_8``
     - AIP.8
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #892
   * - ``aip_9``
     - AIP.9
     - Optional[str]
     - optional
     - Item #893
   * - ``aip_10``
     - AIP.10
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #894
   * - ``aip_11``
     - AIP.11
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #895 | Table HL70279
   * - ``aip_12``
     - AIP.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #889 | Table HL70278

.. _hl7-v2_7_1-AIS:

AIS Appointment Information (S10.6.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.AIS.AIS
   :noindex:

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
     - Item #890
   * - ``ais_2``
     - AIS.2
     - Optional[str]
     - optional
     - Item #763 | Table HL70206
   * - ``ais_3``
     - AIS.3
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #238
   * - ``ais_4``
     - AIS.4
     - Optional[str]
     - optional
     - Item #1202
   * - ``ais_5``
     - AIS.5
     - Optional[str]
     - optional
     - Item #891
   * - ``ais_6``
     - AIS.6
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #892
   * - ``ais_7``
     - AIS.7
     - Optional[str]
     - optional
     - Item #893
   * - ``ais_8``
     - AIS.8
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #894
   * - ``ais_9``
     - AIS.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #895 | Table HL70279
   * - ``ais_10``
     - AIS.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #889 | Table HL70278
   * - ``ais_11``
     - AIS.11
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1474 | Table HL70411
   * - ``ais_12``
     - AIS.12
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1475 | Table HL70411

.. _hl7-v2_7_1-AL1:

AL1 Patient Allergy Information (S3.4.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.AL1.AL1
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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #204 | Table HL70127
   * - ``al1_3``
     - AL1.3
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #205
   * - ``al1_4``
     - AL1.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #206 | Table HL70128
   * - ``al1_5``
     - AL1.5
     - Optional[List[str]]
     - optional
     - Item #207

.. _hl7-v2_7_1-APR:

APR Appointment Preferences (S10.6.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.APR.APR
   :noindex:

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
     - Optional[List[:ref:`SCV <hl7-v2_7_1-SCV>`]]
     - optional
     - Item #908 | Table HL70294
   * - ``apr_2``
     - APR.2
     - Optional[List[:ref:`SCV <hl7-v2_7_1-SCV>`]]
     - optional
     - Item #909 | Table HL70294
   * - ``apr_3``
     - APR.3
     - Optional[List[:ref:`SCV <hl7-v2_7_1-SCV>`]]
     - optional
     - Item #910 | Table HL70294
   * - ``apr_4``
     - APR.4
     - Optional[str]
     - optional
     - Item #911
   * - ``apr_5``
     - APR.5
     - Optional[List[:ref:`SCV <hl7-v2_7_1-SCV>`]]
     - optional
     - Item #912

.. _hl7-v2_7_1-ARQ:

ARQ Appointment Request (S10.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ARQ.ARQ
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #860
   * - ``arq_2``
     - ARQ.2
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #861
   * - ``arq_3``
     - ARQ.3
     - Optional[str]
     - optional
     - Item #862
   * - ``arq_4``
     - ARQ.4
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #218
   * - ``arq_5``
     - ARQ.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #864
   * - ``arq_6``
     - ARQ.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #865
   * - ``arq_7``
     - ARQ.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #866 | Table HL70276
   * - ``arq_8``
     - ARQ.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #867 | Table HL70277
   * - ``arq_9``
     - ARQ.9
     - Optional[str]
     - optional
     - Item #868
   * - ``arq_10``
     - ARQ.10
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #869
   * - ``arq_11``
     - ARQ.11
     - Optional[List[:ref:`DR <hl7-v2_7_1-DR>`]]
     - optional
     - Item #870
   * - ``arq_12``
     - ARQ.12
     - Optional[str]
     - optional
     - Item #871
   * - ``arq_13``
     - ARQ.13
     - Optional[:ref:`RI <hl7-v2_7_1-RI>`]
     - optional
     - Item #872
   * - ``arq_14``
     - ARQ.14
     - Optional[str]
     - optional
     - Item #873
   * - ``arq_15``
     - ARQ.15
     - List[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - required
     - Item #874
   * - ``arq_16``
     - ARQ.16
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #875
   * - ``arq_17``
     - ARQ.17
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #876
   * - ``arq_18``
     - ARQ.18
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #877
   * - ``arq_19``
     - ARQ.19
     - List[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - required
     - Item #878
   * - ``arq_20``
     - ARQ.20
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #879
   * - ``arq_21``
     - ARQ.21
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #880
   * - ``arq_22``
     - ARQ.22
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #881
   * - ``arq_23``
     - ARQ.23
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #882
   * - ``arq_24``
     - ARQ.24
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #216
   * - ``arq_25``
     - ARQ.25
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #217

.. _hl7-v2_7_1-ARV:

ARV Access Restriction (S3.4.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ARV.ARV
   :noindex:

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
     - Item #2143
   * - ``arv_2``
     - ARV.2
     - :ref:`CNE <hl7-v2_7_1-CNE>`
     - required
     - Item #2144 | Table HL70206
   * - ``arv_3``
     - ARV.3
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #2145 | Table HL70717
   * - ``arv_4``
     - ARV.4
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2146 | Table HL70719
   * - ``arv_5``
     - ARV.5
     - Optional[List[str]]
     - optional
     - Item #2147
   * - ``arv_6``
     - ARV.6
     - Optional[:ref:`DR <hl7-v2_7_1-DR>`]
     - optional
     - Item #2148

.. _hl7-v2_7_1-AUT:

AUT Authorization Information (S11.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.AUT.AUT
   :noindex:

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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1146 | Table HL70072
   * - ``aut_2``
     - AUT.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1147 | Table HL70285
   * - ``aut_3``
     - AUT.3
     - Optional[str]
     - optional
     - Item #1148
   * - ``aut_4``
     - AUT.4
     - Optional[str]
     - optional
     - Item #1149
   * - ``aut_5``
     - AUT.5
     - Optional[str]
     - optional
     - Item #1150
   * - ``aut_6``
     - AUT.6
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1151
   * - ``aut_7``
     - AUT.7
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1152
   * - ``aut_8``
     - AUT.8
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1153
   * - ``aut_9``
     - AUT.9
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1154
   * - ``aut_10``
     - AUT.10
     - Optional[str]
     - optional
     - Item #1145
   * - ``aut_11``
     - AUT.11
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2375
   * - ``aut_12``
     - AUT.12
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2376

.. _hl7-v2_7_1-BHS:

BHS Batch Header (S2.14.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.BHS.BHS
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
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #83
   * - ``bhs_4``
     - BHS.4
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #84
   * - ``bhs_5``
     - BHS.5
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #85
   * - ``bhs_6``
     - BHS.6
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #86
   * - ``bhs_7``
     - BHS.7
     - Optional[str]
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
   * - ``bhs_13``
     - BHS.13
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #2271
   * - ``bhs_14``
     - BHS.14
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #2272

.. _hl7-v2_7_1-BLC:

BLC Blood Code (S6.5.13).
~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.BLC.BLC
   :noindex:

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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1528 | Table HL70426
   * - ``blc_2``
     - BLC.2
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1529

.. _hl7-v2_7_1-BLG:

BLG Billing (S4.4.2).
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.BLG.BLG
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
     - Optional[:ref:`CCD <hl7-v2_7_1-CCD>`]
     - optional
     - Item #234 | Table HL70100
   * - ``blg_2``
     - BLG.2
     - Optional[str]
     - optional
     - Item #235 | Table HL70122
   * - ``blg_3``
     - BLG.3
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #236
   * - ``blg_4``
     - BLG.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1645 | Table HL70475

.. _hl7-v2_7_1-BPO:

BPO Blood product order (S4.13.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.BPO.BPO
   :noindex:

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
     - Item #1700
   * - ``bpo_2``
     - BPO.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1701 | Table HL79999
   * - ``bpo_3``
     - BPO.3
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1702 | Table HL70508
   * - ``bpo_4``
     - BPO.4
     - str
     - required
     - Item #1703
   * - ``bpo_5``
     - BPO.5
     - Optional[str]
     - optional
     - Item #1704
   * - ``bpo_6``
     - BPO.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1705 | Table HL79999
   * - ``bpo_7``
     - BPO.7
     - Optional[str]
     - optional
     - Item #1706
   * - ``bpo_8``
     - BPO.8
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #1707
   * - ``bpo_9``
     - BPO.9
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1708
   * - ``bpo_10``
     - BPO.10
     - Optional[str]
     - optional
     - Item #1709
   * - ``bpo_11``
     - BPO.11
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #1710
   * - ``bpo_12``
     - BPO.12
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1711
   * - ``bpo_13``
     - BPO.13
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1712 | Table HL70509
   * - ``bpo_14``
     - BPO.14
     - Optional[str]
     - optional
     - Item #1713 | Table HL70136

.. _hl7-v2_7_1-BPX:

BPX Blood product dispense status (S4.13.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.BPX.BPX
   :noindex:

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
     - Item #1714
   * - ``bpx_2``
     - BPX.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1715 | Table HL70510
   * - ``bpx_3``
     - BPX.3
     - str
     - required
     - Item #1716 | Table HL70511
   * - ``bpx_4``
     - BPX.4
     - str
     - required
     - Item #1717
   * - ``bpx_5``
     - BPX.5
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1718
   * - ``bpx_6``
     - BPX.6
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #1719 | Table HL79999
   * - ``bpx_7``
     - BPX.7
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #1720 | Table HL79999
   * - ``bpx_8``
     - BPX.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1721 | Table HL70512
   * - ``bpx_9``
     - BPX.9
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #1722
   * - ``bpx_10``
     - BPX.10
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1723
   * - ``bpx_11``
     - BPX.11
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #1724 | Table HL79999
   * - ``bpx_12``
     - BPX.12
     - Optional[List[:ref:`CNE <hl7-v2_7_1-CNE>`]]
     - optional
     - Item #1725 | Table HL79999
   * - ``bpx_13``
     - BPX.13
     - Optional[str]
     - optional
     - Item #1726
   * - ``bpx_14``
     - BPX.14
     - str
     - required
     - Item #1727
   * - ``bpx_15``
     - BPX.15
     - Optional[str]
     - optional
     - Item #1728
   * - ``bpx_16``
     - BPX.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1729 | Table HL79999
   * - ``bpx_17``
     - BPX.17
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1730
   * - ``bpx_18``
     - BPX.18
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #1731
   * - ``bpx_19``
     - BPX.19
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1732
   * - ``bpx_20``
     - BPX.20
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1733
   * - ``bpx_21``
     - BPX.21
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1734

.. _hl7-v2_7_1-BTS:

BTS Batch Trailer (S2.14.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.BTS.BTS
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
     - Item #90
   * - ``bts_3``
     - BTS.3
     - Optional[List[str]]
     - optional
     - Item #95

.. _hl7-v2_7_1-BTX:

BTX Blood Product Transfusion/Disposition (S4.13.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.BTX.BTX
   :noindex:

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
     - Item #1735
   * - ``btx_2``
     - BTX.2
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1736
   * - ``btx_3``
     - BTX.3
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #1737 | Table HL79999
   * - ``btx_4``
     - BTX.4
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #1738 | Table HL79999
   * - ``btx_5``
     - BTX.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1739 | Table HL70512
   * - ``btx_6``
     - BTX.6
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #1740
   * - ``btx_7``
     - BTX.7
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1741
   * - ``btx_8``
     - BTX.8
     - str
     - required
     - Item #1742
   * - ``btx_9``
     - BTX.9
     - Optional[str]
     - optional
     - Item #1743
   * - ``btx_10``
     - BTX.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1744 | Table HL79999
   * - ``btx_11``
     - BTX.11
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1745 | Table HL70513
   * - ``btx_12``
     - BTX.12
     - str
     - required
     - Item #1746 | Table HL70511
   * - ``btx_13``
     - BTX.13
     - str
     - required
     - Item #1747
   * - ``btx_14``
     - BTX.14
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1748
   * - ``btx_15``
     - BTX.15
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1749
   * - ``btx_16``
     - BTX.16
     - Optional[str]
     - optional
     - Item #1750
   * - ``btx_17``
     - BTX.17
     - Optional[str]
     - optional
     - Item #1751
   * - ``btx_18``
     - BTX.18
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1752 | Table HL70514
   * - ``btx_19``
     - BTX.19
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1753 | Table HL70515

.. _hl7-v2_7_1-CDM:

CDM Charge Description Master (S8.10.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.CDM.CDM
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1306 | Table HL70132
   * - ``cdm_2``
     - CDM.2
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #983 | Table HL70132
   * - ``cdm_3``
     - CDM.3
     - str
     - required
     - Item #984
   * - ``cdm_4``
     - CDM.4
     - Optional[str]
     - optional
     - Item #985
   * - ``cdm_5``
     - CDM.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #986 | Table HL70268
   * - ``cdm_6``
     - CDM.6
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #987 | Table HL70132
   * - ``cdm_7``
     - CDM.7
     - Optional[List[:ref:`CNE <hl7-v2_7_1-CNE>`]]
     - optional
     - Item #393 | Table HL70088
   * - ``cdm_8``
     - CDM.8
     - Optional[str]
     - optional
     - Item #675 | Table HL70183
   * - ``cdm_9``
     - CDM.9
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #990 | Table HL70463
   * - ``cdm_10``
     - CDM.10
     - Optional[str]
     - optional
     - Item #991
   * - ``cdm_11``
     - CDM.11
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #992
   * - ``cdm_12``
     - CDM.12
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #993
   * - ``cdm_13``
     - CDM.13
     - Optional[str]
     - optional
     - Item #994 | Table HL70136

.. _hl7-v2_7_1-CER:

CER Certificate Detail (S15.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.CER.CER
   :noindex:

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
     - Item #1856
   * - ``cer_2``
     - CER.2
     - Optional[str]
     - optional
     - Item #1857
   * - ``cer_3``
     - CER.3
     - Optional[str]
     - optional
     - Item #1858
   * - ``cer_4``
     - CER.4
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #1859
   * - ``cer_5``
     - CER.5
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1860
   * - ``cer_6``
     - CER.6
     - Optional[:ref:`ED <hl7-v2_7_1-ED>`]
     - optional
     - Item #1861
   * - ``cer_7``
     - CER.7
     - Optional[str]
     - optional
     - Item #1862 | Table HL70399
   * - ``cer_8``
     - CER.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1863 | Table HL70347
   * - ``cer_9``
     - CER.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1864 | Table HL70289
   * - ``cer_10``
     - CER.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1865
   * - ``cer_11``
     - CER.11
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1866
   * - ``cer_12``
     - CER.12
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1867
   * - ``cer_13``
     - CER.13
     - str
     - required
     - Item #1907
   * - ``cer_14``
     - CER.14
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1868
   * - ``cer_15``
     - CER.15
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1869
   * - ``cer_16``
     - CER.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1870
   * - ``cer_17``
     - CER.17
     - Optional[str]
     - optional
     - Item #1871 | Table HL70136
   * - ``cer_18``
     - CER.18
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1872
   * - ``cer_19``
     - CER.19
     - Optional[str]
     - optional
     - Item #1875 | Table HL70399
   * - ``cer_20``
     - CER.20
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1873 | Table HL70347
   * - ``cer_21``
     - CER.21
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1874 | Table HL70289
   * - ``cer_22``
     - CER.22
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1895 | Table HL70547
   * - ``cer_23``
     - CER.23
     - Optional[str]
     - optional
     - Item #1876
   * - ``cer_24``
     - CER.24
     - Optional[str]
     - optional
     - Item #1877
   * - ``cer_25``
     - CER.25
     - Optional[str]
     - optional
     - Item #1878
   * - ``cer_26``
     - CER.26
     - Optional[str]
     - optional
     - Item #1879
   * - ``cer_27``
     - CER.27
     - Optional[str]
     - optional
     - Item #1880
   * - ``cer_28``
     - CER.28
     - Optional[str]
     - optional
     - Item #1881
   * - ``cer_29``
     - CER.29
     - Optional[str]
     - optional
     - Item #1882
   * - ``cer_30``
     - CER.30
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1883
   * - ``cer_31``
     - CER.31
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1884 | Table HL70536

.. _hl7-v2_7_1-CM0:

CM0 Clinical Study Master (S8.11.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.CM0.CM0
   :noindex:

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
     - Item #1010
   * - ``cm0_2``
     - CM0.2
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1011
   * - ``cm0_3``
     - CM0.3
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #1036
   * - ``cm0_4``
     - CM0.4
     - str
     - required
     - Item #1013
   * - ``cm0_5``
     - CM0.5
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #1014
   * - ``cm0_6``
     - CM0.6
     - Optional[str]
     - optional
     - Item #1015
   * - ``cm0_7``
     - CM0.7
     - Optional[str]
     - optional
     - Item #1016
   * - ``cm0_8``
     - CM0.8
     - Optional[str]
     - optional
     - Item #1017
   * - ``cm0_9``
     - CM0.9
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #1018
   * - ``cm0_10``
     - CM0.10
     - Optional[:ref:`XTN <hl7-v2_7_1-XTN>`]
     - optional
     - Item #1019
   * - ``cm0_11``
     - CM0.11
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #1020

.. _hl7-v2_7_1-CM1:

CM1 Clinical Study Phase Master (S8.11.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.CM1.CM1
   :noindex:

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
     - Item #1021
   * - ``cm1_2``
     - CM1.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1022 | Table HL79999
   * - ``cm1_3``
     - CM1.3
     - str
     - required
     - Item #1023

.. _hl7-v2_7_1-CM2:

CM2 Clinical Study Schedule Master (S8.11.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.CM2.CM2
   :noindex:

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
     - Item #1024
   * - ``cm2_2``
     - CM2.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1025
   * - ``cm2_3``
     - CM2.3
     - Optional[str]
     - optional
     - Item #1026
   * - ``cm2_4``
     - CM2.4
     - List[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - required
     - Item #1027

.. _hl7-v2_7_1-CNS:

CNS Clear Notification (S13.4.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.CNS.CNS
   :noindex:

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
     - Item #1402
   * - ``cns_2``
     - CNS.2
     - Optional[str]
     - optional
     - Item #1403
   * - ``cns_3``
     - CNS.3
     - Optional[str]
     - optional
     - Item #1404
   * - ``cns_4``
     - CNS.4
     - Optional[str]
     - optional
     - Item #1405
   * - ``cns_5``
     - CNS.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1406 | Table HL79999
   * - ``cns_6``
     - CNS.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1407 | Table HL79999

.. _hl7-v2_7_1-CON:

CON Consent Segment (S9.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.CON.CON
   :noindex:

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
     - Item #1776
   * - ``con_2``
     - CON.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1777 | Table HL70496
   * - ``con_3``
     - CON.3
     - Optional[str]
     - optional
     - Item #1778
   * - ``con_4``
     - CON.4
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1779
   * - ``con_5``
     - CON.5
     - Optional[List[str]]
     - optional
     - Item #1780
   * - ``con_6``
     - CON.6
     - Optional[List[str]]
     - optional
     - Item #1781
   * - ``con_7``
     - CON.7
     - Optional[List[str]]
     - optional
     - Item #1782
   * - ``con_8``
     - CON.8
     - Optional[List[str]]
     - optional
     - Item #1783
   * - ``con_9``
     - CON.9
     - Optional[List[str]]
     - optional
     - Item #1784
   * - ``con_10``
     - CON.10
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #1785 | Table HL70497
   * - ``con_11``
     - CON.11
     - :ref:`CNE <hl7-v2_7_1-CNE>`
     - required
     - Item #1786 | Table HL70498
   * - ``con_12``
     - CON.12
     - Optional[str]
     - optional
     - Item #1787
   * - ``con_13``
     - CON.13
     - Optional[str]
     - optional
     - Item #1788
   * - ``con_14``
     - CON.14
     - Optional[str]
     - optional
     - Item #1789
   * - ``con_15``
     - CON.15
     - Optional[str]
     - optional
     - Item #1790
   * - ``con_16``
     - CON.16
     - Optional[str]
     - optional
     - Item #1791 | Table HL70136
   * - ``con_17``
     - CON.17
     - Optional[str]
     - optional
     - Item #1792 | Table HL70136
   * - ``con_18``
     - CON.18
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1793 | Table HL70296
   * - ``con_19``
     - CON.19
     - Optional[str]
     - optional
     - Item #1794 | Table HL70136
   * - ``con_20``
     - CON.20
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1795 | Table HL70499
   * - ``con_21``
     - CON.21
     - Optional[str]
     - optional
     - Item #1796 | Table HL70500
   * - ``con_22``
     - CON.22
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1797 | Table HL70501
   * - ``con_23``
     - CON.23
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1798 | Table HL70502
   * - ``con_24``
     - CON.24
     - List[:ref:`XPN <hl7-v2_7_1-XPN>`]
     - required
     - Item #1909
   * - ``con_25``
     - CON.25
     - List[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - required
     - Item #1898 | Table HL70548

.. _hl7-v2_7_1-CSP:

CSP Clinical Study Phase (S7.8.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.CSP.CSP
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1022 | Table HL79999
   * - ``csp_2``
     - CSP.2
     - str
     - required
     - Item #1052
   * - ``csp_3``
     - CSP.3
     - Optional[str]
     - optional
     - Item #1053
   * - ``csp_4``
     - CSP.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1054 | Table HL79999

.. _hl7-v2_7_1-CSR:

CSR Clinical Study Registration (S7.8.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.CSR.CSR
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1011
   * - ``csr_2``
     - CSR.2
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1036
   * - ``csr_3``
     - CSR.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1037 | Table HL79999
   * - ``csr_4``
     - CSR.4
     - :ref:`CX <hl7-v2_7_1-CX>`
     - required
     - Item #1038
   * - ``csr_5``
     - CSR.5
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #1039
   * - ``csr_6``
     - CSR.6
     - str
     - required
     - Item #1040
   * - ``csr_7``
     - CSR.7
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #1041
   * - ``csr_8``
     - CSR.8
     - List[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - required
     - Item #1042
   * - ``csr_9``
     - CSR.9
     - Optional[str]
     - optional
     - Item #1043
   * - ``csr_10``
     - CSR.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1044 | Table HL79999
   * - ``csr_11``
     - CSR.11
     - Optional[List[str]]
     - optional
     - Item #1045
   * - ``csr_12``
     - CSR.12
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1046 | Table HL79999
   * - ``csr_13``
     - CSR.13
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1047 | Table HL79999
   * - ``csr_14``
     - CSR.14
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1048 | Table HL79999
   * - ``csr_15``
     - CSR.15
     - Optional[str]
     - optional
     - Item #1049
   * - ``csr_16``
     - CSR.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1050 | Table HL79999

.. _hl7-v2_7_1-CSS:

CSS Clinical Study Data Schedule Segment (S7.8.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.CSS.CSS
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1055 | Table HL79999
   * - ``css_2``
     - CSS.2
     - Optional[str]
     - optional
     - Item #1056
   * - ``css_3``
     - CSS.3
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1057 | Table HL79999

.. _hl7-v2_7_1-CTD:

CTD Contact Data (S11.7.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.CTD.CTD
   :noindex:

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
     - List[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - required
     - Item #196 | Table HL70131
   * - ``ctd_2``
     - CTD.2
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #1165
   * - ``ctd_3``
     - CTD.3
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #1166
   * - ``ctd_4``
     - CTD.4
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #1167
   * - ``ctd_5``
     - CTD.5
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #1168
   * - ``ctd_6``
     - CTD.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #684 | Table HL70185
   * - ``ctd_7``
     - CTD.7
     - Optional[List[:ref:`PLN <hl7-v2_7_1-PLN>`]]
     - optional
     - Item #1171 | Table HL70338

.. _hl7-v2_7_1-CTI:

CTI Clinical Trial Identification (S7.8.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.CTI.CTI
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1011
   * - ``cti_2``
     - CTI.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1022 | Table HL79999
   * - ``cti_3``
     - CTI.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1055 | Table HL79999

.. _hl7-v2_7_1-DB1:

DB1 Disability (S3.4.12).
~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.DB1.DB1
   :noindex:

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
     - Item #1283
   * - ``db1_2``
     - DB1.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1284 | Table HL70334
   * - ``db1_3``
     - DB1.3
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #1285
   * - ``db1_4``
     - DB1.4
     - Optional[str]
     - optional
     - Item #1286 | Table HL70136
   * - ``db1_5``
     - DB1.5
     - Optional[str]
     - optional
     - Item #1287
   * - ``db1_6``
     - DB1.6
     - Optional[str]
     - optional
     - Item #1288
   * - ``db1_7``
     - DB1.7
     - Optional[str]
     - optional
     - Item #1289
   * - ``db1_8``
     - DB1.8
     - Optional[str]
     - optional
     - Item #1290

.. _hl7-v2_7_1-DG1:

DG1 Diagnosis (S6.5.2).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.DG1.DG1
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
   * - ``dg1_3``
     - DG1.3
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #377 | Table HL70051
   * - ``dg1_5``
     - DG1.5
     - Optional[str]
     - optional
     - Item #379
   * - ``dg1_6``
     - DG1.6
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #380 | Table HL70052
   * - ``dg1_15``
     - DG1.15
     - Optional[str]
     - optional
     - Item #389 | Table HL70359
   * - ``dg1_16``
     - DG1.16
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #390
   * - ``dg1_17``
     - DG1.17
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #766 | Table HL70228
   * - ``dg1_18``
     - DG1.18
     - Optional[str]
     - optional
     - Item #767 | Table HL70136
   * - ``dg1_19``
     - DG1.19
     - Optional[str]
     - optional
     - Item #768
   * - ``dg1_20``
     - DG1.20
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1850
   * - ``dg1_21``
     - DG1.21
     - Optional[str]
     - optional
     - Item #1894 | Table HL70206
   * - ``dg1_22``
     - DG1.22
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2152
   * - ``dg1_23``
     - DG1.23
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2153 | Table HL70728
   * - ``dg1_24``
     - DG1.24
     - Optional[str]
     - optional
     - Item #2154 | Table HL70136
   * - ``dg1_25``
     - DG1.25
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2155 | Table HL70731
   * - ``dg1_26``
     - DG1.26
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2288 | Table HL70895

.. _hl7-v2_7_1-DMI:

DMI DRG Master File Information (S8.13.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.DMI.DMI
   :noindex:

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
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #382 | Table HL70055
   * - ``dmi_2``
     - DMI.2
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #381 | Table HL70118
   * - ``dmi_3``
     - DMI.3
     - Optional[:ref:`NR <hl7-v2_7_1-NR>`]
     - optional
     - Item #2231
   * - ``dmi_4``
     - DMI.4
     - Optional[str]
     - optional
     - Item #2232
   * - ``dmi_5``
     - DMI.5
     - Optional[str]
     - optional
     - Item #2233

.. _hl7-v2_7_1-DRG:

DRG Diagnosis Related Group (S6.5.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.DRG.DRG
   :noindex:

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
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #382 | Table HL70055
   * - ``drg_2``
     - DRG.2
     - Optional[str]
     - optional
     - Item #769
   * - ``drg_3``
     - DRG.3
     - Optional[str]
     - optional
     - Item #383 | Table HL70136
   * - ``drg_4``
     - DRG.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #384 | Table HL70056
   * - ``drg_5``
     - DRG.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #385 | Table HL70083
   * - ``drg_6``
     - DRG.6
     - Optional[str]
     - optional
     - Item #386
   * - ``drg_7``
     - DRG.7
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #387
   * - ``drg_8``
     - DRG.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #770 | Table HL70229
   * - ``drg_9``
     - DRG.9
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #771
   * - ``drg_10``
     - DRG.10
     - Optional[str]
     - optional
     - Item #767 | Table HL70136
   * - ``drg_11``
     - DRG.11
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1500 | Table HL70415
   * - ``drg_12``
     - DRG.12
     - Optional[:ref:`XPN <hl7-v2_7_1-XPN>`]
     - optional
     - Item #2156
   * - ``drg_13``
     - DRG.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2157 | Table HL70734
   * - ``drg_14``
     - DRG.14
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2158 | Table HL70728
   * - ``drg_15``
     - DRG.15
     - Optional[str]
     - optional
     - Item #2159
   * - ``drg_16``
     - DRG.16
     - Optional[:ref:`MO <hl7-v2_7_1-MO>`]
     - optional
     - Item #2160
   * - ``drg_17``
     - DRG.17
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2161 | Table HL70739
   * - ``drg_18``
     - DRG.18
     - Optional[str]
     - optional
     - Item #2162
   * - ``drg_19``
     - DRG.19
     - Optional[str]
     - optional
     - Item #2282
   * - ``drg_20``
     - DRG.20
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2163 | Table HL70742
   * - ``drg_21``
     - DRG.21
     - Optional[:ref:`MO <hl7-v2_7_1-MO>`]
     - optional
     - Item #2164
   * - ``drg_22``
     - DRG.22
     - Optional[:ref:`MO <hl7-v2_7_1-MO>`]
     - optional
     - Item #2165
   * - ``drg_23``
     - DRG.23
     - Optional[:ref:`MO <hl7-v2_7_1-MO>`]
     - optional
     - Item #2166
   * - ``drg_24``
     - DRG.24
     - Optional[:ref:`MO <hl7-v2_7_1-MO>`]
     - optional
     - Item #2167
   * - ``drg_25``
     - DRG.25
     - Optional[str]
     - optional
     - Item #2168
   * - ``drg_26``
     - DRG.26
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2169 | Table HL70749
   * - ``drg_27``
     - DRG.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2170 | Table HL70749
   * - ``drg_28``
     - DRG.28
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2171 | Table HL70749
   * - ``drg_29``
     - DRG.29
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2172 | Table HL70749
   * - ``drg_30``
     - DRG.30
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2173 | Table HL70749
   * - ``drg_31``
     - DRG.31
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2174 | Table HL70755
   * - ``drg_32``
     - DRG.32
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2175 | Table HL70757
   * - ``drg_33``
     - DRG.33
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2176 | Table HL70759

.. _hl7-v2_7_1-DSC:

DSC Continuation Pointer (S2.14.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.DSC.DSC
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
     - Item #14
   * - ``dsc_2``
     - DSC.2
     - Optional[str]
     - optional
     - Item #1354 | Table HL70398

.. _hl7-v2_7_1-DSP:

DSP Display Data (S5.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.DSP.DSP
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

.. _hl7-v2_7_1-ECD:

ECD Equipment Command (S13.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ECD.ECD
   :noindex:

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
     - Item #1390
   * - ``ecd_2``
     - ECD.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1391 | Table HL70368
   * - ``ecd_3``
     - ECD.3
     - Optional[str]
     - optional
     - Item #1392 | Table HL70136
   * - ``ecd_5``
     - ECD.5
     - Optional[List[str]]
     - optional
     - Item #1394

.. _hl7-v2_7_1-ECR:

ECR Equipment Command Response (S13.4.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ECR.ECR
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1395 | Table HL70387
   * - ``ecr_2``
     - ECR.2
     - str
     - required
     - Item #1396
   * - ``ecr_3``
     - ECR.3
     - Optional[List[str]]
     - optional
     - Item #1397

.. _hl7-v2_7_1-EDU:

EDU Educational Detail (S15.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.EDU.EDU
   :noindex:

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
     - Item #1448
   * - ``edu_2``
     - EDU.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1449 | Table HL70360
   * - ``edu_3``
     - EDU.3
     - Optional[:ref:`DR <hl7-v2_7_1-DR>`]
     - optional
     - Item #1597
   * - ``edu_4``
     - EDU.4
     - Optional[:ref:`DR <hl7-v2_7_1-DR>`]
     - optional
     - Item #1450
   * - ``edu_5``
     - EDU.5
     - Optional[str]
     - optional
     - Item #1451
   * - ``edu_6``
     - EDU.6
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #1452
   * - ``edu_7``
     - EDU.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1453 | Table HL70402
   * - ``edu_8``
     - EDU.8
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1454
   * - ``edu_9``
     - EDU.9
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1885

.. _hl7-v2_7_1-EQP:

EQP Equipment/log Service (S13.4.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.EQP.EQP
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1430 | Table HL70450
   * - ``eqp_2``
     - EQP.2
     - Optional[str]
     - optional
     - Item #1431
   * - ``eqp_3``
     - EQP.3
     - str
     - required
     - Item #1202
   * - ``eqp_4``
     - EQP.4
     - Optional[str]
     - optional
     - Item #1432
   * - ``eqp_5``
     - EQP.5
     - str
     - required
     - Item #1433

.. _hl7-v2_7_1-EQU:

EQU Equipment Detail (S13.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.EQU.EQU
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1479
   * - ``equ_2``
     - EQU.2
     - str
     - required
     - Item #1322
   * - ``equ_3``
     - EQU.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1323 | Table HL70365
   * - ``equ_4``
     - EQU.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1324 | Table HL70366
   * - ``equ_5``
     - EQU.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1325 | Table HL70367

.. _hl7-v2_7_1-ERR:

ERR Error (S2.14.5).
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ERR.ERR
   :noindex:

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
     - Optional[List[:ref:`ERL <hl7-v2_7_1-ERL>`]]
     - optional
     - Item #1812
   * - ``err_3``
     - ERR.3
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1813 | Table HL70357
   * - ``err_4``
     - ERR.4
     - str
     - required
     - Item #1814 | Table HL70516
   * - ``err_5``
     - ERR.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1815 | Table HL70533
   * - ``err_6``
     - ERR.6
     - Optional[List[str]]
     - optional
     - Item #1816
   * - ``err_7``
     - ERR.7
     - Optional[str]
     - optional
     - Item #1817
   * - ``err_8``
     - ERR.8
     - Optional[str]
     - optional
     - Item #1818
   * - ``err_9``
     - ERR.9
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1819 | Table HL70517
   * - ``err_10``
     - ERR.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1820 | Table HL70518
   * - ``err_11``
     - ERR.11
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1821 | Table HL70519
   * - ``err_12``
     - ERR.12
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #1822

.. _hl7-v2_7_1-EVN:

EVN Event Type (S3.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.EVN.EVN
   :noindex:

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
     - Item #100
   * - ``evn_3``
     - EVN.3
     - Optional[str]
     - optional
     - Item #101
   * - ``evn_4``
     - EVN.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #102 | Table HL70062
   * - ``evn_5``
     - EVN.5
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #103 | Table HL70188
   * - ``evn_6``
     - EVN.6
     - Optional[str]
     - optional
     - Item #1278
   * - ``evn_7``
     - EVN.7
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #1534

.. _hl7-v2_7_1-FAC:

FAC Facility (S7.12.6).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.FAC.FAC
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1262
   * - ``fac_2``
     - FAC.2
     - Optional[str]
     - optional
     - Item #1263 | Table HL70331
   * - ``fac_3``
     - FAC.3
     - List[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - required
     - Item #1264
   * - ``fac_4``
     - FAC.4
     - :ref:`XTN <hl7-v2_7_1-XTN>`
     - required
     - Item #1265
   * - ``fac_5``
     - FAC.5
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #1266
   * - ``fac_6``
     - FAC.6
     - Optional[List[str]]
     - optional
     - Item #1267
   * - ``fac_7``
     - FAC.7
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #1166
   * - ``fac_8``
     - FAC.8
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #1269
   * - ``fac_9``
     - FAC.9
     - List[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - required
     - Item #1270
   * - ``fac_10``
     - FAC.10
     - Optional[str]
     - optional
     - Item #1271
   * - ``fac_11``
     - FAC.11
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #1272
   * - ``fac_12``
     - FAC.12
     - Optional[:ref:`XTN <hl7-v2_7_1-XTN>`]
     - optional
     - Item #1273

.. _hl7-v2_7_1-FHS:

FHS File Header (S2.14.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.FHS.FHS
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
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #69
   * - ``fhs_4``
     - FHS.4
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #70
   * - ``fhs_5``
     - FHS.5
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #71
   * - ``fhs_6``
     - FHS.6
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #72
   * - ``fhs_7``
     - FHS.7
     - Optional[str]
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
   * - ``fhs_13``
     - FHS.13
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #2269
   * - ``fhs_14``
     - FHS.14
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #2270

.. _hl7-v2_7_1-FT1:

FT1 Financial Transaction (S6.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.FT1.FT1
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
     - :ref:`DR <hl7-v2_7_1-DR>`
     - required
     - Item #358
   * - ``ft1_5``
     - FT1.5
     - Optional[str]
     - optional
     - Item #359
   * - ``ft1_6``
     - FT1.6
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #360 | Table HL70017
   * - ``ft1_7``
     - FT1.7
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #361 | Table HL70132
   * - ``ft1_10``
     - FT1.10
     - Optional[str]
     - optional
     - Item #364
   * - ``ft1_11``
     - FT1.11
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #365
   * - ``ft1_12``
     - FT1.12
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #366
   * - ``ft1_13``
     - FT1.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #367 | Table HL70049
   * - ``ft1_14``
     - FT1.14
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #368 | Table HL70072
   * - ``ft1_15``
     - FT1.15
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #369
   * - ``ft1_16``
     - FT1.16
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #133
   * - ``ft1_17``
     - FT1.17
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #370 | Table HL70024
   * - ``ft1_18``
     - FT1.18
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #148 | Table HL70018
   * - ``ft1_19``
     - FT1.19
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #371 | Table HL70051
   * - ``ft1_20``
     - FT1.20
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #372 | Table HL70084
   * - ``ft1_21``
     - FT1.21
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #373
   * - ``ft1_22``
     - FT1.22
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #374
   * - ``ft1_23``
     - FT1.23
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #217
   * - ``ft1_24``
     - FT1.24
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #765
   * - ``ft1_25``
     - FT1.25
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #393 | Table HL70088
   * - ``ft1_26``
     - FT1.26
     - Optional[List[:ref:`CNE <hl7-v2_7_1-CNE>`]]
     - optional
     - Item #1316 | Table HL70340
   * - ``ft1_27``
     - FT1.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1310 | Table HL70339
   * - ``ft1_28``
     - FT1.28
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1646 | Table HL70476
   * - ``ft1_29``
     - FT1.29
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1845 | Table HL70549
   * - ``ft1_30``
     - FT1.30
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #1846
   * - ``ft1_31``
     - FT1.31
     - Optional[List[str]]
     - optional
     - Item #1847
   * - ``ft1_32``
     - FT1.32
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #2361
   * - ``ft1_33``
     - FT1.33
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #2362
   * - ``ft1_34``
     - FT1.34
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2363
   * - ``ft1_35``
     - FT1.35
     - Optional[str]
     - optional
     - Item #2364
   * - ``ft1_36``
     - FT1.36
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2365
   * - ``ft1_37``
     - FT1.37
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2366
   * - ``ft1_38``
     - FT1.38
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #2367
   * - ``ft1_39``
     - FT1.39
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #2368
   * - ``ft1_40``
     - FT1.40
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2369
   * - ``ft1_41``
     - FT1.41
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1600 | Table HL70456
   * - ``ft1_42``
     - FT1.42
     - Optional[str]
     - optional
     - Item #325
   * - ``ft1_43``
     - FT1.43
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2370

.. _hl7-v2_7_1-FTS:

FTS File Trailer (S2.14.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.FTS.FTS
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

.. _hl7-v2_7_1-GOL:

GOL Goal Detail (S12.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.GOL.GOL
   :noindex:

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
     - Item #816 | Table HL70287
   * - ``gol_2``
     - GOL.2
     - str
     - required
     - Item #817
   * - ``gol_3``
     - GOL.3
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #818
   * - ``gol_4``
     - GOL.4
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #819
   * - ``gol_5``
     - GOL.5
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #820
   * - ``gol_6``
     - GOL.6
     - Optional[str]
     - optional
     - Item #821
   * - ``gol_7``
     - GOL.7
     - Optional[str]
     - optional
     - Item #822
   * - ``gol_8``
     - GOL.8
     - Optional[str]
     - optional
     - Item #824
   * - ``gol_9``
     - GOL.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #825
   * - ``gol_10``
     - GOL.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #826
   * - ``gol_11``
     - GOL.11
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #827
   * - ``gol_12``
     - GOL.12
     - Optional[str]
     - optional
     - Item #828
   * - ``gol_13``
     - GOL.13
     - Optional[str]
     - optional
     - Item #829
   * - ``gol_14``
     - GOL.14
     - Optional[str]
     - optional
     - Item #830
   * - ``gol_16``
     - GOL.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #832
   * - ``gol_17``
     - GOL.17
     - Optional[List[str]]
     - optional
     - Item #833
   * - ``gol_18``
     - GOL.18
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #834
   * - ``gol_19``
     - GOL.19
     - Optional[str]
     - optional
     - Item #835
   * - ``gol_20``
     - GOL.20
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #836
   * - ``gol_21``
     - GOL.21
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #837
   * - ``gol_22``
     - GOL.22
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2182 | Table HL70725

.. _hl7-v2_7_1-GP1:

GP1 Grouping/Reimbursement - Visit (S6.5.15).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.GP1.GP1
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1599 | Table HL70455
   * - ``gp1_2``
     - GP1.2
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1600 | Table HL70456
   * - ``gp1_3``
     - GP1.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1601 | Table HL70457
   * - ``gp1_4``
     - GP1.4
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1602 | Table HL70458
   * - ``gp1_5``
     - GP1.5
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #387

.. _hl7-v2_7_1-GP2:

GP2 Grouping/Reimbursement - Procedure Line Item (S6.5.16).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.GP2.GP2
   :noindex:

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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1600 | Table HL70456
   * - ``gp2_2``
     - GP2.2
     - Optional[str]
     - optional
     - Item #1604
   * - ``gp2_3``
     - GP2.3
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1605
   * - ``gp2_4``
     - GP2.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1606 | Table HL70459
   * - ``gp2_5``
     - GP2.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1607 | Table HL70460
   * - ``gp2_6``
     - GP2.6
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1608 | Table HL70458
   * - ``gp2_7``
     - GP2.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1609 | Table HL70466
   * - ``gp2_8``
     - GP2.8
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1610 | Table HL70467
   * - ``gp2_9``
     - GP2.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1611 | Table HL70468
   * - ``gp2_10``
     - GP2.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1617 | Table HL70469
   * - ``gp2_11``
     - GP2.11
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1618
   * - ``gp2_12``
     - GP2.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1619 | Table HL70470
   * - ``gp2_13``
     - GP2.13
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1620
   * - ``gp2_14``
     - GP2.14
     - Optional[str]
     - optional
     - Item #1621

.. _hl7-v2_7_1-GT1:

GT1 Guarantor (S6.5.5).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.GT1.GT1
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
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #406
   * - ``gt1_3``
     - GT1.3
     - List[:ref:`XPN <hl7-v2_7_1-XPN>`]
     - required
     - Item #407
   * - ``gt1_4``
     - GT1.4
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #408
   * - ``gt1_5``
     - GT1.5
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #409
   * - ``gt1_6``
     - GT1.6
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #410
   * - ``gt1_7``
     - GT1.7
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #411
   * - ``gt1_8``
     - GT1.8
     - Optional[str]
     - optional
     - Item #412
   * - ``gt1_9``
     - GT1.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #413 | Table HL70001
   * - ``gt1_10``
     - GT1.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #414 | Table HL70068
   * - ``gt1_11``
     - GT1.11
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
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
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #420
   * - ``gt1_17``
     - GT1.17
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #421
   * - ``gt1_18``
     - GT1.18
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #422
   * - ``gt1_19``
     - GT1.19
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #423
   * - ``gt1_20``
     - GT1.20
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #424 | Table HL70066
   * - ``gt1_21``
     - GT1.21
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #425
   * - ``gt1_22``
     - GT1.22
     - Optional[str]
     - optional
     - Item #773 | Table HL70136
   * - ``gt1_23``
     - GT1.23
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #774 | Table HL70341
   * - ``gt1_24``
     - GT1.24
     - Optional[str]
     - optional
     - Item #775
   * - ``gt1_25``
     - GT1.25
     - Optional[str]
     - optional
     - Item #776 | Table HL70136
   * - ``gt1_26``
     - GT1.26
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #777 | Table HL70218
   * - ``gt1_27``
     - GT1.27
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #778
   * - ``gt1_28``
     - GT1.28
     - Optional[str]
     - optional
     - Item #779
   * - ``gt1_29``
     - GT1.29
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #780
   * - ``gt1_30``
     - GT1.30
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #781 | Table HL70002
   * - ``gt1_31``
     - GT1.31
     - Optional[str]
     - optional
     - Item #782
   * - ``gt1_32``
     - GT1.32
     - Optional[str]
     - optional
     - Item #783
   * - ``gt1_33``
     - GT1.33
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #755 | Table HL70223
   * - ``gt1_34``
     - GT1.34
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #145 | Table HL70009
   * - ``gt1_35``
     - GT1.35
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #129 | Table HL70171
   * - ``gt1_36``
     - GT1.36
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #118 | Table HL70296
   * - ``gt1_37``
     - GT1.37
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #742 | Table HL70220
   * - ``gt1_38``
     - GT1.38
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #743 | Table HL70215
   * - ``gt1_39``
     - GT1.39
     - Optional[str]
     - optional
     - Item #744 | Table HL70136
   * - ``gt1_40``
     - GT1.40
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #745 | Table HL70231
   * - ``gt1_41``
     - GT1.41
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #120 | Table HL70006
   * - ``gt1_42``
     - GT1.42
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #109
   * - ``gt1_43``
     - GT1.43
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #739 | Table HL70212
   * - ``gt1_44``
     - GT1.44
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #125 | Table HL70189
   * - ``gt1_45``
     - GT1.45
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #748 | Table HL70200
   * - ``gt1_46``
     - GT1.46
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #749
   * - ``gt1_47``
     - GT1.47
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #747 | Table HL70222
   * - ``gt1_48``
     - GT1.48
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #784 | Table HL70063
   * - ``gt1_49``
     - GT1.49
     - Optional[str]
     - optional
     - Item #785
   * - ``gt1_50``
     - GT1.50
     - Optional[:ref:`JCC <hl7-v2_7_1-JCC>`]
     - optional
     - Item #786 | Table HL70327
   * - ``gt1_51``
     - GT1.51
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #1299
   * - ``gt1_52``
     - GT1.52
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #753 | Table HL70295
   * - ``gt1_53``
     - GT1.53
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #752 | Table HL70311
   * - ``gt1_54``
     - GT1.54
     - Optional[:ref:`FC <hl7-v2_7_1-FC>`]
     - optional
     - Item #1231
   * - ``gt1_55``
     - GT1.55
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1291 | Table HL70005
   * - ``gt1_56``
     - GT1.56
     - Optional[str]
     - optional
     - Item #1851
   * - ``gt1_57``
     - GT1.57
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #146 | Table HL70099

.. _hl7-v2_7_1-IAM:

IAM Patient Adverse Reaction Information (S3.4.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.IAM.IAM
   :noindex:

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
     - Item #1612
   * - ``iam_2``
     - IAM.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #204 | Table HL70127
   * - ``iam_3``
     - IAM.3
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #205
   * - ``iam_4``
     - IAM.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #206 | Table HL70128
   * - ``iam_5``
     - IAM.5
     - Optional[List[str]]
     - optional
     - Item #207
   * - ``iam_6``
     - IAM.6
     - :ref:`CNE <hl7-v2_7_1-CNE>`
     - required
     - Item #1551 | Table HL70206
   * - ``iam_7``
     - IAM.7
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1552
   * - ``iam_8``
     - IAM.8
     - Optional[str]
     - optional
     - Item #1553
   * - ``iam_9``
     - IAM.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1554 | Table HL70436
   * - ``iam_10``
     - IAM.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1555
   * - ``iam_11``
     - IAM.11
     - Optional[str]
     - optional
     - Item #1556
   * - ``iam_12``
     - IAM.12
     - Optional[str]
     - optional
     - Item #1557
   * - ``iam_13``
     - IAM.13
     - Optional[str]
     - optional
     - Item #1558
   * - ``iam_14``
     - IAM.14
     - Optional[:ref:`XPN <hl7-v2_7_1-XPN>`]
     - optional
     - Item #1559
   * - ``iam_15``
     - IAM.15
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1560 | Table HL70063
   * - ``iam_16``
     - IAM.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1561 | Table HL70437
   * - ``iam_17``
     - IAM.17
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1562 | Table HL70438
   * - ``iam_18``
     - IAM.18
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1563
   * - ``iam_19``
     - IAM.19
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #1564
   * - ``iam_20``
     - IAM.20
     - Optional[str]
     - optional
     - Item #1565
   * - ``iam_21``
     - IAM.21
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #2294
   * - ``iam_22``
     - IAM.22
     - Optional[str]
     - optional
     - Item #2295
   * - ``iam_23``
     - IAM.23
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #2296
   * - ``iam_24``
     - IAM.24
     - Optional[str]
     - optional
     - Item #2297
   * - ``iam_25``
     - IAM.25
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #2298
   * - ``iam_26``
     - IAM.26
     - Optional[str]
     - optional
     - Item #2299
   * - ``iam_27``
     - IAM.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2300
   * - ``iam_28``
     - IAM.28
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #3293
   * - ``iam_29``
     - IAM.29
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #3294
   * - ``iam_30``
     - IAM.30
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #3295

.. _hl7-v2_7_1-IAR:

IAR allergy reaction (S3.4.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.IAR.IAR
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #3296
   * - ``iar_2``
     - IAR.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #3297 | Table HL70128
   * - ``iar_3``
     - IAR.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #3298 | Table HL70436
   * - ``iar_4``
     - IAR.4
     - Optional[str]
     - optional
     - Item #3299

.. _hl7-v2_7_1-IIM:

IIM Inventory Item Master (S17.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.IIM.IIM
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1897
   * - ``iim_2``
     - IIM.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1799
   * - ``iim_3``
     - IIM.3
     - Optional[str]
     - optional
     - Item #1800
   * - ``iim_4``
     - IIM.4
     - Optional[str]
     - optional
     - Item #1801
   * - ``iim_5``
     - IIM.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1802
   * - ``iim_6``
     - IIM.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1803
   * - ``iim_7``
     - IIM.7
     - Optional[str]
     - optional
     - Item #1804
   * - ``iim_8``
     - IIM.8
     - Optional[str]
     - optional
     - Item #1805
   * - ``iim_9``
     - IIM.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1806
   * - ``iim_10``
     - IIM.10
     - Optional[:ref:`MO <hl7-v2_7_1-MO>`]
     - optional
     - Item #1807
   * - ``iim_11``
     - IIM.11
     - Optional[str]
     - optional
     - Item #1808
   * - ``iim_12``
     - IIM.12
     - Optional[str]
     - optional
     - Item #1809
   * - ``iim_13``
     - IIM.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1810
   * - ``iim_14``
     - IIM.14
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #393 | Table HL70088
   * - ``iim_15``
     - IIM.15
     - Optional[List[:ref:`CNE <hl7-v2_7_1-CNE>`]]
     - optional
     - Item #1316 | Table HL70340

.. _hl7-v2_7_1-ILT:

ILT Material Lot (S17.4.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ILT.ILT
   :noindex:

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
     - Item #2086
   * - ``ilt_2``
     - ILT.2
     - str
     - required
     - Item #1800
   * - ``ilt_3``
     - ILT.3
     - Optional[str]
     - optional
     - Item #1801
   * - ``ilt_4``
     - ILT.4
     - Optional[str]
     - optional
     - Item #1804
   * - ``ilt_5``
     - ILT.5
     - Optional[str]
     - optional
     - Item #1805
   * - ``ilt_6``
     - ILT.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1806
   * - ``ilt_7``
     - ILT.7
     - Optional[:ref:`MO <hl7-v2_7_1-MO>`]
     - optional
     - Item #1807
   * - ``ilt_8``
     - ILT.8
     - Optional[str]
     - optional
     - Item #1808
   * - ``ilt_9``
     - ILT.9
     - Optional[str]
     - optional
     - Item #1809
   * - ``ilt_10``
     - ILT.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1810

.. _hl7-v2_7_1-IN1:

IN1 Insurance (S6.5.6).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.IN1.IN1
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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #368 | Table HL70072
   * - ``in1_3``
     - IN1.3
     - List[:ref:`CX <hl7-v2_7_1-CX>`]
     - required
     - Item #428
   * - ``in1_4``
     - IN1.4
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #429
   * - ``in1_5``
     - IN1.5
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #430
   * - ``in1_6``
     - IN1.6
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #431
   * - ``in1_7``
     - IN1.7
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #432
   * - ``in1_8``
     - IN1.8
     - Optional[str]
     - optional
     - Item #433
   * - ``in1_9``
     - IN1.9
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #434
   * - ``in1_10``
     - IN1.10
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #435
   * - ``in1_11``
     - IN1.11
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
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
     - Optional[:ref:`AUI <hl7-v2_7_1-AUI>`]
     - optional
     - Item #439
   * - ``in1_15``
     - IN1.15
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #440 | Table HL70086
   * - ``in1_16``
     - IN1.16
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #441
   * - ``in1_17``
     - IN1.17
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #442 | Table HL70063
   * - ``in1_18``
     - IN1.18
     - Optional[str]
     - optional
     - Item #443
   * - ``in1_19``
     - IN1.19
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #444
   * - ``in1_20``
     - IN1.20
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #445 | Table HL70135
   * - ``in1_21``
     - IN1.21
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
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
     - Item #450 | Table HL70136
   * - ``in1_26``
     - IN1.26
     - Optional[str]
     - optional
     - Item #451
   * - ``in1_27``
     - IN1.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #452 | Table HL70093
   * - ``in1_28``
     - IN1.28
     - Optional[str]
     - optional
     - Item #453
   * - ``in1_29``
     - IN1.29
     - Optional[str]
     - optional
     - Item #454
   * - ``in1_30``
     - IN1.30
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #455
   * - ``in1_31``
     - IN1.31
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #456 | Table HL70098
   * - ``in1_32``
     - IN1.32
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #460 | Table HL70042
   * - ``in1_36``
     - IN1.36
     - Optional[str]
     - optional
     - Item #461
   * - ``in1_37``
     - IN1.37
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #462
   * - ``in1_39``
     - IN1.39
     - Optional[str]
     - optional
     - Item #464
   * - ``in1_42``
     - IN1.42
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #467 | Table HL70066
   * - ``in1_43``
     - IN1.43
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #468 | Table HL70001
   * - ``in1_44``
     - IN1.44
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #469
   * - ``in1_45``
     - IN1.45
     - Optional[str]
     - optional
     - Item #470
   * - ``in1_46``
     - IN1.46
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #471 | Table HL70072
   * - ``in1_47``
     - IN1.47
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1227 | Table HL70309
   * - ``in1_48``
     - IN1.48
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #753 | Table HL70295
   * - ``in1_49``
     - IN1.49
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #1230
   * - ``in1_50``
     - IN1.50
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1854 | Table HL70535
   * - ``in1_51``
     - IN1.51
     - Optional[str]
     - optional
     - Item #1855
   * - ``in1_52``
     - IN1.52
     - Optional[str]
     - optional
     - Item #1899
   * - ``in1_53``
     - IN1.53
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1852 | Table HL70099
   * - ``in1_54``
     - IN1.54
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #3292

.. _hl7-v2_7_1-IN2:

IN2 Insurance Additional Information (S6.5.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.IN2.IN2
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
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #472
   * - ``in2_2``
     - IN2.2
     - Optional[str]
     - optional
     - Item #473
   * - ``in2_3``
     - IN2.3
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #474
   * - ``in2_4``
     - IN2.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #475 | Table HL70139
   * - ``in2_5``
     - IN2.5
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #476 | Table HL70137
   * - ``in2_6``
     - IN2.6
     - Optional[str]
     - optional
     - Item #477
   * - ``in2_7``
     - IN2.7
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #478
   * - ``in2_8``
     - IN2.8
     - Optional[str]
     - optional
     - Item #479
   * - ``in2_9``
     - IN2.9
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #480
   * - ``in2_10``
     - IN2.10
     - Optional[str]
     - optional
     - Item #481
   * - ``in2_11``
     - IN2.11
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #482 | Table HL70342
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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #485 | Table HL70140
   * - ``in2_15``
     - IN2.15
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #486 | Table HL70141
   * - ``in2_16``
     - IN2.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
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
     - Item #492
   * - ``in2_22``
     - IN2.22
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #493
   * - ``in2_23``
     - IN2.23
     - Optional[str]
     - optional
     - Item #494
   * - ``in2_24``
     - IN2.24
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #495 | Table HL70143
   * - ``in2_25``
     - IN2.25
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #496
   * - ``in2_26``
     - IN2.26
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #497
   * - ``in2_27``
     - IN2.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #498 | Table HL70144
   * - ``in2_28``
     - IN2.28
     - Optional[List[:ref:`RMC <hl7-v2_7_1-RMC>`]]
     - optional
     - Item #499
   * - ``in2_29``
     - IN2.29
     - Optional[List[:ref:`PTA <hl7-v2_7_1-PTA>`]]
     - optional
     - Item #500
   * - ``in2_30``
     - IN2.30
     - Optional[:ref:`DDI <hl7-v2_7_1-DDI>`]
     - optional
     - Item #501
   * - ``in2_31``
     - IN2.31
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #755 | Table HL70223
   * - ``in2_32``
     - IN2.32
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #145 | Table HL70009
   * - ``in2_33``
     - IN2.33
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #129 | Table HL70171
   * - ``in2_34``
     - IN2.34
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #118 | Table HL70296
   * - ``in2_35``
     - IN2.35
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #742 | Table HL70220
   * - ``in2_36``
     - IN2.36
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #743 | Table HL70215
   * - ``in2_37``
     - IN2.37
     - Optional[str]
     - optional
     - Item #744 | Table HL70136
   * - ``in2_38``
     - IN2.38
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #745 | Table HL70231
   * - ``in2_39``
     - IN2.39
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #120 | Table HL70006
   * - ``in2_40``
     - IN2.40
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #109
   * - ``in2_41``
     - IN2.41
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #739 | Table HL70212
   * - ``in2_42``
     - IN2.42
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #125 | Table HL70189
   * - ``in2_43``
     - IN2.43
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #119 | Table HL70002
   * - ``in2_44``
     - IN2.44
     - Optional[str]
     - optional
     - Item #787
   * - ``in2_45``
     - IN2.45
     - Optional[str]
     - optional
     - Item #783
   * - ``in2_46``
     - IN2.46
     - Optional[str]
     - optional
     - Item #785
   * - ``in2_47``
     - IN2.47
     - Optional[:ref:`JCC <hl7-v2_7_1-JCC>`]
     - optional
     - Item #786 | Table HL70327
   * - ``in2_48``
     - IN2.48
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #752 | Table HL70311
   * - ``in2_49``
     - IN2.49
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #789
   * - ``in2_50``
     - IN2.50
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #790
   * - ``in2_51``
     - IN2.51
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #791 | Table HL70222
   * - ``in2_52``
     - IN2.52
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #792
   * - ``in2_53``
     - IN2.53
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #793
   * - ``in2_54``
     - IN2.54
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #794 | Table HL70222
   * - ``in2_55``
     - IN2.55
     - Optional[str]
     - optional
     - Item #795
   * - ``in2_56``
     - IN2.56
     - Optional[List[str]]
     - optional
     - Item #796
   * - ``in2_57``
     - IN2.57
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #797 | Table HL70232
   * - ``in2_58``
     - IN2.58
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #798
   * - ``in2_59``
     - IN2.59
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #799 | Table HL70312
   * - ``in2_60``
     - IN2.60
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #800 | Table HL70313
   * - ``in2_61``
     - IN2.61
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #801
   * - ``in2_62``
     - IN2.62
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #802 | Table HL70063
   * - ``in2_63``
     - IN2.63
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #803
   * - ``in2_64``
     - IN2.64
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #804
   * - ``in2_65``
     - IN2.65
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #805 | Table HL70343
   * - ``in2_66``
     - IN2.66
     - Optional[str]
     - optional
     - Item #806 | Table HL70136
   * - ``in2_67``
     - IN2.67
     - Optional[str]
     - optional
     - Item #807 | Table HL70136
   * - ``in2_68``
     - IN2.68
     - Optional[str]
     - optional
     - Item #808 | Table HL70136
   * - ``in2_69``
     - IN2.69
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #809
   * - ``in2_70``
     - IN2.70
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #810
   * - ``in2_71``
     - IN2.71
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #113 | Table HL70005
   * - ``in2_72``
     - IN2.72
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #811 | Table HL70344

.. _hl7-v2_7_1-IN3:

IN3 Insurance Additional Information, Certification (S6.5.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.IN3.IN3
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
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #503
   * - ``in3_3``
     - IN3.3
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #504
   * - ``in3_4``
     - IN3.4
     - Optional[str]
     - optional
     - Item #505 | Table HL70136
   * - ``in3_5``
     - IN3.5
     - Optional[:ref:`MOP <hl7-v2_7_1-MOP>`]
     - optional
     - Item #506
   * - ``in3_6``
     - IN3.6
     - Optional[str]
     - optional
     - Item #507
   * - ``in3_7``
     - IN3.7
     - Optional[str]
     - optional
     - Item #508
   * - ``in3_8``
     - IN3.8
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
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
     - Optional[:ref:`DTN <hl7-v2_7_1-DTN>`]
     - optional
     - Item #512
   * - ``in3_12``
     - IN3.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #513 | Table HL70233
   * - ``in3_13``
     - IN3.13
     - Optional[str]
     - optional
     - Item #514
   * - ``in3_14``
     - IN3.14
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #515 | Table HL70010
   * - ``in3_15``
     - IN3.15
     - Optional[str]
     - optional
     - Item #516
   * - ``in3_16``
     - IN3.16
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #517
   * - ``in3_17``
     - IN3.17
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #518 | Table HL70345
   * - ``in3_18``
     - IN3.18
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #519 | Table HL70346
   * - ``in3_19``
     - IN3.19
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #520
   * - ``in3_20``
     - IN3.20
     - Optional[List[:ref:`ICD <hl7-v2_7_1-ICD>`]]
     - optional
     - Item #521
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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #524 | Table HL70151
   * - ``in3_24``
     - IN3.24
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #525 | Table HL70152
   * - ``in3_25``
     - IN3.25
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #526 | Table HL70010

.. _hl7-v2_7_1-INV:

INV Inventory Detail (S13.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.INV.INV
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1372 | Table HL70451
   * - ``inv_2``
     - INV.2
     - List[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - required
     - Item #1373 | Table HL70383
   * - ``inv_3``
     - INV.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1374 | Table HL70384
   * - ``inv_4``
     - INV.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1532 | Table HL79999
   * - ``inv_5``
     - INV.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1376 | Table HL79999
   * - ``inv_6``
     - INV.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1377 | Table HL79999
   * - ``inv_7``
     - INV.7
     - Optional[str]
     - optional
     - Item #1378
   * - ``inv_8``
     - INV.8
     - Optional[str]
     - optional
     - Item #1379
   * - ``inv_9``
     - INV.9
     - Optional[str]
     - optional
     - Item #1380
   * - ``inv_10``
     - INV.10
     - Optional[str]
     - optional
     - Item #1381
   * - ``inv_11``
     - INV.11
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1382 | Table HL79999
   * - ``inv_12``
     - INV.12
     - Optional[str]
     - optional
     - Item #1383
   * - ``inv_13``
     - INV.13
     - Optional[str]
     - optional
     - Item #1384
   * - ``inv_15``
     - INV.15
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1386 | Table HL79999
   * - ``inv_16``
     - INV.16
     - Optional[str]
     - optional
     - Item #1387
   * - ``inv_17``
     - INV.17
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #286 | Table HL70385
   * - ``inv_18``
     - INV.18
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1389 | Table HL70386
   * - ``inv_19``
     - INV.19
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1626
   * - ``inv_20``
     - INV.20
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1896

.. _hl7-v2_7_1-IPC:

IPC Imaging Procedure Control Segment (S4.4.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.IPC.IPC
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1330
   * - ``ipc_2``
     - IPC.2
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1658
   * - ``ipc_3``
     - IPC.3
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1659
   * - ``ipc_4``
     - IPC.4
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1660
   * - ``ipc_5``
     - IPC.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1661 | Table HL79999
   * - ``ipc_6``
     - IPC.6
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1662 | Table HL79999
   * - ``ipc_7``
     - IPC.7
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1663
   * - ``ipc_8``
     - IPC.8
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1664 | Table HL79999
   * - ``ipc_9``
     - IPC.9
     - Optional[str]
     - optional
     - Item #1665

.. _hl7-v2_7_1-IPR:

IPR Invoice Processing Results (S16.4.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.IPR.IPR
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2030
   * - ``ipr_2``
     - IPR.2
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2031
   * - ``ipr_3``
     - IPR.3
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2032
   * - ``ipr_4``
     - IPR.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #2033 | Table HL70571
   * - ``ipr_5``
     - IPR.5
     - str
     - required
     - Item #2034
   * - ``ipr_6``
     - IPR.6
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #2035
   * - ``ipr_7``
     - IPR.7
     - Optional[str]
     - optional
     - Item #2036
   * - ``ipr_8``
     - IPR.8
     - str
     - required
     - Item #2037

.. _hl7-v2_7_1-ISD:

ISD Interaction Status Detail (S13.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ISD.ISD
   :noindex:

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
     - Item #1326
   * - ``isd_2``
     - ISD.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1327 | Table HL70368
   * - ``isd_3``
     - ISD.3
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1328 | Table HL70387

.. _hl7-v2_7_1-ITM:

ITM Material Item (S17.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ITM.ITM
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2186
   * - ``itm_2``
     - ITM.2
     - Optional[str]
     - optional
     - Item #2274
   * - ``itm_3``
     - ITM.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2187 | Table HL70776
   * - ``itm_4``
     - ITM.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2188 | Table HL70778
   * - ``itm_5``
     - ITM.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2189
   * - ``itm_6``
     - ITM.6
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2190 | Table HL70532
   * - ``itm_7``
     - ITM.7
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2191
   * - ``itm_8``
     - ITM.8
     - Optional[str]
     - optional
     - Item #2275
   * - ``itm_9``
     - ITM.9
     - Optional[str]
     - optional
     - Item #2192
   * - ``itm_10``
     - ITM.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2193
   * - ``itm_11``
     - ITM.11
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2070 | Table HL70532
   * - ``itm_12``
     - ITM.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #361 | Table HL70132
   * - ``itm_13``
     - ITM.13
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #366
   * - ``itm_14``
     - ITM.14
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2197 | Table HL70532
   * - ``itm_15``
     - ITM.15
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2266 | Table HL70871
   * - ``itm_16``
     - ITM.16
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #2199 | Table HL70790
   * - ``itm_17``
     - ITM.17
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2200 | Table HL70532
   * - ``itm_18``
     - ITM.18
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2201 | Table HL70793
   * - ``itm_19``
     - ITM.19
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #282 | Table HL70320
   * - ``itm_20``
     - ITM.20
     - Optional[str]
     - optional
     - Item #2203
   * - ``itm_21``
     - ITM.21
     - Optional[:ref:`MO <hl7-v2_7_1-MO>`]
     - optional
     - Item #2204
   * - ``itm_22``
     - ITM.22
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2205 | Table HL70532
   * - ``itm_23``
     - ITM.23
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2206 | Table HL70532
   * - ``itm_24``
     - ITM.24
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2207 | Table HL70532
   * - ``itm_25``
     - ITM.25
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2208
   * - ``itm_26``
     - ITM.26
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2209 | Table HL70532
   * - ``itm_27``
     - ITM.27
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #393 | Table HL70088
   * - ``itm_28``
     - ITM.28
     - Optional[List[:ref:`CNE <hl7-v2_7_1-CNE>`]]
     - optional
     - Item #1316 | Table HL70340
   * - ``itm_29``
     - ITM.29
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1370 | Table HL70376

.. _hl7-v2_7_1-IVC:

IVC Invoice Segment (S16.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.IVC.IVC
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1914
   * - ``ivc_2``
     - IVC.2
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1915
   * - ``ivc_3``
     - IVC.3
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1916
   * - ``ivc_4``
     - IVC.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1917 | Table HL70553
   * - ``ivc_5``
     - IVC.5
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1918 | Table HL70554
   * - ``ivc_6``
     - IVC.6
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1919 | Table HL70555
   * - ``ivc_7``
     - IVC.7
     - str
     - required
     - Item #1920
   * - ``ivc_8``
     - IVC.8
     - :ref:`CP <hl7-v2_7_1-CP>`
     - required
     - Item #1921
   * - ``ivc_9``
     - IVC.9
     - Optional[str]
     - optional
     - Item #1922
   * - ``ivc_10``
     - IVC.10
     - :ref:`XON <hl7-v2_7_1-XON>`
     - required
     - Item #1923
   * - ``ivc_11``
     - IVC.11
     - :ref:`XON <hl7-v2_7_1-XON>`
     - required
     - Item #1924
   * - ``ivc_12``
     - IVC.12
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1925
   * - ``ivc_13``
     - IVC.13
     - Optional[str]
     - optional
     - Item #1926 | Table HL70136
   * - ``ivc_14``
     - IVC.14
     - Optional[str]
     - optional
     - Item #1927
   * - ``ivc_15``
     - IVC.15
     - Optional[str]
     - optional
     - Item #1928
   * - ``ivc_16``
     - IVC.16
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1929
   * - ``ivc_17``
     - IVC.17
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1930
   * - ``ivc_18``
     - IVC.18
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1931
   * - ``ivc_19``
     - IVC.19
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1932
   * - ``ivc_20``
     - IVC.20
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #1933
   * - ``ivc_21``
     - IVC.21
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1934
   * - ``ivc_22``
     - IVC.22
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1935
   * - ``ivc_23``
     - IVC.23
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1936
   * - ``ivc_24``
     - IVC.24
     - Optional[List[str]]
     - optional
     - Item #1937
   * - ``ivc_25``
     - IVC.25
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1938 | Table HL70556
   * - ``ivc_26``
     - IVC.26
     - Optional[str]
     - optional
     - Item #2038
   * - ``ivc_27``
     - IVC.27
     - Optional[str]
     - optional
     - Item #2039
   * - ``ivc_28``
     - IVC.28
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2040 | Table HL70572
   * - ``ivc_29``
     - IVC.29
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2041 | Table HL70572
   * - ``ivc_30``
     - IVC.30
     - Optional[str]
     - optional
     - Item #2042

.. _hl7-v2_7_1-IVT:

IVT Material Location (S17.4.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.IVT.IVT
   :noindex:

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
     - Item #2062
   * - ``ivt_2``
     - IVT.2
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2063
   * - ``ivt_3``
     - IVT.3
     - Optional[str]
     - optional
     - Item #2277
   * - ``ivt_4``
     - IVT.4
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2064
   * - ``ivt_5``
     - IVT.5
     - Optional[str]
     - optional
     - Item #2278
   * - ``ivt_6``
     - IVT.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2065 | Table HL70625
   * - ``ivt_7``
     - IVT.7
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #2066
   * - ``ivt_8``
     - IVT.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2067 | Table HL70818
   * - ``ivt_9``
     - IVT.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2068
   * - ``ivt_10``
     - IVT.10
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2069
   * - ``ivt_11``
     - IVT.11
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2070 | Table HL70532
   * - ``ivt_12``
     - IVT.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #361 | Table HL70132
   * - ``ivt_13``
     - IVT.13
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #366
   * - ``ivt_14``
     - IVT.14
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2073 | Table HL70634
   * - ``ivt_15``
     - IVT.15
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2074 | Table HL70532
   * - ``ivt_16``
     - IVT.16
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2075 | Table HL70532
   * - ``ivt_17``
     - IVT.17
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2076 | Table HL70532
   * - ``ivt_18``
     - IVT.18
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #2077
   * - ``ivt_19``
     - IVT.19
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #2078
   * - ``ivt_20``
     - IVT.20
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2079
   * - ``ivt_21``
     - IVT.21
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2080 | Table HL70642
   * - ``ivt_22``
     - IVT.22
     - Optional[str]
     - optional
     - Item #2081
   * - ``ivt_23``
     - IVT.23
     - Optional[str]
     - optional
     - Item #2082
   * - ``ivt_24``
     - IVT.24
     - Optional[str]
     - optional
     - Item #2083
   * - ``ivt_25``
     - IVT.25
     - Optional[str]
     - optional
     - Item #2084
   * - ``ivt_26``
     - IVT.26
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2085 | Table HL70532

.. _hl7-v2_7_1-LAN:

LAN Language Detail (S15.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.LAN.LAN
   :noindex:

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
     - Item #1455
   * - ``lan_2``
     - LAN.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1456 | Table HL70296
   * - ``lan_3``
     - LAN.3
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1457 | Table HL70403
   * - ``lan_4``
     - LAN.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1458 | Table HL70404

.. _hl7-v2_7_1-LCC:

LCC Location Charge Code (S8.9.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.LCC.LCC
   :noindex:

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
     - :ref:`PL <hl7-v2_7_1-PL>`
     - required
     - Item #979
   * - ``lcc_2``
     - LCC.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #964 | Table HL70264
   * - ``lcc_3``
     - LCC.3
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #980 | Table HL70129
   * - ``lcc_4``
     - LCC.4
     - List[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - required
     - Item #981 | Table HL70132

.. _hl7-v2_7_1-LCH:

LCH Location Characteristic (S8.9.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.LCH.LCH
   :noindex:

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
     - :ref:`PL <hl7-v2_7_1-PL>`
     - required
     - Item #1305
   * - ``lch_2``
     - LCH.2
     - Optional[str]
     - optional
     - Item #763 | Table HL70206
   * - ``lch_3``
     - LCH.3
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #764
   * - ``lch_4``
     - LCH.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1295 | Table HL70324
   * - ``lch_5``
     - LCH.5
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1294 | Table HL70136

.. _hl7-v2_7_1-LDP:

LDP Location Department (S8.9.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.LDP.LDP
   :noindex:

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
     - :ref:`PL <hl7-v2_7_1-PL>`
     - required
     - Item #963
   * - ``ldp_2``
     - LDP.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #964 | Table HL70264
   * - ``ldp_3``
     - LDP.3
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #965 | Table HL70069
   * - ``ldp_4``
     - LDP.4
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #966 | Table HL70265
   * - ``ldp_5``
     - LDP.5
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #967 | Table HL70004
   * - ``ldp_6``
     - LDP.6
     - Optional[str]
     - optional
     - Item #675 | Table HL70183
   * - ``ldp_7``
     - LDP.7
     - Optional[str]
     - optional
     - Item #969
   * - ``ldp_8``
     - LDP.8
     - Optional[str]
     - optional
     - Item #970
   * - ``ldp_9``
     - LDP.9
     - Optional[str]
     - optional
     - Item #971
   * - ``ldp_10``
     - LDP.10
     - Optional[List[:ref:`VH <hl7-v2_7_1-VH>`]]
     - optional
     - Item #976 | Table HL70267
   * - ``ldp_11``
     - LDP.11
     - Optional[:ref:`XTN <hl7-v2_7_1-XTN>`]
     - optional
     - Item #978
   * - ``ldp_12``
     - LDP.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1584 | Table HL70462

.. _hl7-v2_7_1-LOC:

LOC Location Identification (S8.9.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.LOC.LOC
   :noindex:

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
     - :ref:`PL <hl7-v2_7_1-PL>`
     - required
     - Item #1307
   * - ``loc_2``
     - LOC.2
     - Optional[str]
     - optional
     - Item #944
   * - ``loc_3``
     - LOC.3
     - List[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - required
     - Item #945 | Table HL70260
   * - ``loc_4``
     - LOC.4
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #947
   * - ``loc_5``
     - LOC.5
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #948
   * - ``loc_6``
     - LOC.6
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #949
   * - ``loc_7``
     - LOC.7
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #951 | Table HL70461
   * - ``loc_8``
     - LOC.8
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #953 | Table HL70261
   * - ``loc_9``
     - LOC.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1583 | Table HL70442

.. _hl7-v2_7_1-LRL:

LRL Location Relationship (S8.9.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.LRL.LRL
   :noindex:

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
     - :ref:`PL <hl7-v2_7_1-PL>`
     - required
     - Item #943
   * - ``lrl_2``
     - LRL.2
     - Optional[str]
     - optional
     - Item #763 | Table HL70206
   * - ``lrl_3``
     - LRL.3
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #764
   * - ``lrl_4``
     - LRL.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1277 | Table HL70325
   * - ``lrl_5``
     - LRL.5
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #1301
   * - ``lrl_6``
     - LRL.6
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #1292

.. _hl7-v2_7_1-MFA:

MFA Master File Acknowledgment (S8.5.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.MFA.MFA
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
     - Optional[str]
     - optional
     - Item #668
   * - ``mfa_4``
     - MFA.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #669 | Table HL70181
   * - ``mfa_5``
     - MFA.5
     - List[varies]
     - required
     - Item #1308 | Table HL79999
   * - ``mfa_6``
     - MFA.6
     - List[str]
     - required
     - Item #1320 | Table HL70355

.. _hl7-v2_7_1-MFE:

MFE Master File Entry (S8.5.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.MFE.MFE
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
     - Optional[str]
     - optional
     - Item #662
   * - ``mfe_4``
     - MFE.4
     - List[varies]
     - required
     - Item #667 | Table HL79999
   * - ``mfe_5``
     - MFE.5
     - List[str]
     - required
     - Item #1319 | Table HL70355
   * - ``mfe_6``
     - MFE.6
     - Optional[str]
     - optional
     - Item #661
   * - ``mfe_7``
     - MFE.7
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #224

.. _hl7-v2_7_1-MFI:

MFI Master File Identification (S8.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.MFI.MFI
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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #658 | Table HL70175
   * - ``mfi_2``
     - MFI.2
     - Optional[List[:ref:`HD <hl7-v2_7_1-HD>`]]
     - optional
     - Item #659 | Table HL70361
   * - ``mfi_3``
     - MFI.3
     - str
     - required
     - Item #660 | Table HL70178
   * - ``mfi_4``
     - MFI.4
     - Optional[str]
     - optional
     - Item #661
   * - ``mfi_5``
     - MFI.5
     - Optional[str]
     - optional
     - Item #662
   * - ``mfi_6``
     - MFI.6
     - str
     - required
     - Item #663 | Table HL70179

.. _hl7-v2_7_1-MRG:

MRG Merge Patient Information (S3.4.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.MRG.MRG
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
     - List[:ref:`CX <hl7-v2_7_1-CX>`]
     - required
     - Item #211 | Table HL70061
   * - ``mrg_3``
     - MRG.3
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #213 | Table HL70061
   * - ``mrg_5``
     - MRG.5
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #1279 | Table HL70061
   * - ``mrg_6``
     - MRG.6
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #1280 | Table HL70061
   * - ``mrg_7``
     - MRG.7
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #1281 | Table HL70200

.. _hl7-v2_7_1-MSA:

MSA Message Acknowledgment (S2.14.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.MSA.MSA
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
   * - ``msa_4``
     - MSA.4
     - Optional[str]
     - optional
     - Item #21
   * - ``msa_7``
     - MSA.7
     - Optional[str]
     - optional
     - Item #1827
   * - ``msa_8``
     - MSA.8
     - Optional[str]
     - optional
     - Item #1828 | Table HL70520

.. _hl7-v2_7_1-MSH:

MSH Message Header (S2.14.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.MSH.MSH
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
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #3 | Table HL70361
   * - ``msh_4``
     - MSH.4
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #4 | Table HL70362
   * - ``msh_5``
     - MSH.5
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #5 | Table HL70361
   * - ``msh_6``
     - MSH.6
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #6 | Table HL70362
   * - ``msh_7``
     - MSH.7
     - str
     - required
     - Item #7
   * - ``msh_8``
     - MSH.8
     - Optional[str]
     - optional
     - Item #8
   * - ``msh_9``
     - MSH.9
     - :ref:`MSG <hl7-v2_7_1-MSG>`
     - required
     - Item #9
   * - ``msh_10``
     - MSH.10
     - str
     - required
     - Item #10
   * - ``msh_11``
     - MSH.11
     - :ref:`PT <hl7-v2_7_1-PT>`
     - required
     - Item #11
   * - ``msh_12``
     - MSH.12
     - :ref:`VID <hl7-v2_7_1-VID>`
     - required
     - Item #12
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
     - Item #17 | Table HL70399
   * - ``msh_18``
     - MSH.18
     - Optional[List[str]]
     - optional
     - Item #692 | Table HL70211
   * - ``msh_19``
     - MSH.19
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #693
   * - ``msh_20``
     - MSH.20
     - Optional[str]
     - optional
     - Item #1317 | Table HL70356
   * - ``msh_21``
     - MSH.21
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #1598
   * - ``msh_22``
     - MSH.22
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #1823
   * - ``msh_23``
     - MSH.23
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #1824
   * - ``msh_24``
     - MSH.24
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #1825
   * - ``msh_25``
     - MSH.25
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #1826

.. _hl7-v2_7_1-NCK:

NCK System Clock (S14.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.NCK.NCK
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
     - str
     - required
     - Item #1172

.. _hl7-v2_7_1-NDS:

NDS Notification Detail (S13.4.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.NDS.NDS
   :noindex:

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
     - Item #1398
   * - ``nds_2``
     - NDS.2
     - str
     - required
     - Item #1399
   * - ``nds_3``
     - NDS.3
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1400 | Table HL70367
   * - ``nds_4``
     - NDS.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1401 | Table HL79999

.. _hl7-v2_7_1-NK1:

NK1 Next of Kin / Associated Parties (S3.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.NK1.NK1
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
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #191 | Table HL70200
   * - ``nk1_3``
     - NK1.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #192 | Table HL70063
   * - ``nk1_4``
     - NK1.4
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #193
   * - ``nk1_5``
     - NK1.5
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #194
   * - ``nk1_6``
     - NK1.6
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #195
   * - ``nk1_7``
     - NK1.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
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
     - Optional[:ref:`JCC <hl7-v2_7_1-JCC>`]
     - optional
     - Item #200
   * - ``nk1_12``
     - NK1.12
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #201
   * - ``nk1_13``
     - NK1.13
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #202
   * - ``nk1_14``
     - NK1.14
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #119 | Table HL70002
   * - ``nk1_15``
     - NK1.15
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #111 | Table HL70001
   * - ``nk1_16``
     - NK1.16
     - Optional[str]
     - optional
     - Item #110
   * - ``nk1_17``
     - NK1.17
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #755 | Table HL70223
   * - ``nk1_18``
     - NK1.18
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #145 | Table HL70009
   * - ``nk1_19``
     - NK1.19
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #129 | Table HL70171
   * - ``nk1_20``
     - NK1.20
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #118 | Table HL70296
   * - ``nk1_21``
     - NK1.21
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #742 | Table HL70220
   * - ``nk1_22``
     - NK1.22
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #743 | Table HL70215
   * - ``nk1_23``
     - NK1.23
     - Optional[str]
     - optional
     - Item #744 | Table HL70136
   * - ``nk1_24``
     - NK1.24
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #745 | Table HL70231
   * - ``nk1_25``
     - NK1.25
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #120 | Table HL70006
   * - ``nk1_26``
     - NK1.26
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #109
   * - ``nk1_27``
     - NK1.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #739 | Table HL70212
   * - ``nk1_28``
     - NK1.28
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #125 | Table HL70189
   * - ``nk1_29``
     - NK1.29
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #747 | Table HL70222
   * - ``nk1_30``
     - NK1.30
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #748 | Table HL70200
   * - ``nk1_31``
     - NK1.31
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #749
   * - ``nk1_32``
     - NK1.32
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #750
   * - ``nk1_33``
     - NK1.33
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #751
   * - ``nk1_34``
     - NK1.34
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #752 | Table HL70311
   * - ``nk1_35``
     - NK1.35
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #113 | Table HL70005
   * - ``nk1_36``
     - NK1.36
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #753 | Table HL70295
   * - ``nk1_37``
     - NK1.37
     - Optional[str]
     - optional
     - Item #754
   * - ``nk1_38``
     - NK1.38
     - Optional[str]
     - optional
     - Item #1905
   * - ``nk1_39``
     - NK1.39
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #146 | Table HL70099
   * - ``nk1_40``
     - NK1.40
     - Optional[:ref:`XTN <hl7-v2_7_1-XTN>`]
     - optional
     - Item #2292
   * - ``nk1_41``
     - NK1.41
     - Optional[:ref:`XTN <hl7-v2_7_1-XTN>`]
     - optional
     - Item #2293

.. _hl7-v2_7_1-NPU:

NPU Bed Status Update (S3.4.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.NPU.NPU
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
     - :ref:`PL <hl7-v2_7_1-PL>`
     - required
     - Item #209
   * - ``npu_2``
     - NPU.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #170 | Table HL70116

.. _hl7-v2_7_1-NSC:

NSC Application Status Change (S14.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.NSC.NSC
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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1188 | Table HL70409
   * - ``nsc_2``
     - NSC.2
     - Optional[str]
     - optional
     - Item #1189
   * - ``nsc_3``
     - NSC.3
     - Optional[str]
     - optional
     - Item #1190
   * - ``nsc_4``
     - NSC.4
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #1191 | Table HL70361
   * - ``nsc_5``
     - NSC.5
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #1192 | Table HL70362
   * - ``nsc_6``
     - NSC.6
     - Optional[str]
     - optional
     - Item #1193
   * - ``nsc_7``
     - NSC.7
     - Optional[str]
     - optional
     - Item #1194
   * - ``nsc_8``
     - NSC.8
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #1195 | Table HL70361
   * - ``nsc_9``
     - NSC.9
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #1196 | Table HL70362

.. _hl7-v2_7_1-NST:

NST Application control level statistics (S14.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.NST.NST
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
     - Item #1173 | Table HL70136
   * - ``nst_2``
     - NST.2
     - Optional[str]
     - optional
     - Item #1174
   * - ``nst_3``
     - NST.3
     - Optional[str]
     - optional
     - Item #1175 | Table HL70332
   * - ``nst_4``
     - NST.4
     - Optional[str]
     - optional
     - Item #1176
   * - ``nst_5``
     - NST.5
     - Optional[str]
     - optional
     - Item #1177
   * - ``nst_6``
     - NST.6
     - Optional[str]
     - optional
     - Item #1178
   * - ``nst_7``
     - NST.7
     - Optional[str]
     - optional
     - Item #1179
   * - ``nst_8``
     - NST.8
     - Optional[str]
     - optional
     - Item #1180
   * - ``nst_9``
     - NST.9
     - Optional[str]
     - optional
     - Item #1181
   * - ``nst_10``
     - NST.10
     - Optional[str]
     - optional
     - Item #1182
   * - ``nst_11``
     - NST.11
     - Optional[str]
     - optional
     - Item #1183
   * - ``nst_12``
     - NST.12
     - Optional[str]
     - optional
     - Item #1184
   * - ``nst_13``
     - NST.13
     - Optional[str]
     - optional
     - Item #1185
   * - ``nst_14``
     - NST.14
     - Optional[str]
     - optional
     - Item #1186
   * - ``nst_15``
     - NST.15
     - Optional[str]
     - optional
     - Item #1187

.. _hl7-v2_7_1-NTE:

NTE Notes and Comments (S2.14.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.NTE.NTE
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
   * - ``nte_4``
     - NTE.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1318 | Table HL70364
   * - ``nte_5``
     - NTE.5
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #224
   * - ``nte_6``
     - NTE.6
     - Optional[str]
     - optional
     - Item #661
   * - ``nte_7``
     - NTE.7
     - Optional[str]
     - optional
     - Item #1004
   * - ``nte_8``
     - NTE.8
     - Optional[str]
     - optional
     - Item #2185

.. _hl7-v2_7_1-OBR:

OBR Observation Request (S4.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.OBR.OBR
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
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #216
   * - ``obr_3``
     - OBR.3
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #217
   * - ``obr_4``
     - OBR.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #238
   * - ``obr_7``
     - OBR.7
     - Optional[str]
     - optional
     - Item #241
   * - ``obr_8``
     - OBR.8
     - Optional[str]
     - optional
     - Item #242
   * - ``obr_9``
     - OBR.9
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #243
   * - ``obr_10``
     - OBR.10
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #244
   * - ``obr_11``
     - OBR.11
     - Optional[str]
     - optional
     - Item #245 | Table HL70065
   * - ``obr_12``
     - OBR.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #246 | Table HL79999
   * - ``obr_13``
     - OBR.13
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #247 | Table HL70916
   * - ``obr_16``
     - OBR.16
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #226
   * - ``obr_17``
     - OBR.17
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
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
     - Optional[str]
     - optional
     - Item #255
   * - ``obr_23``
     - OBR.23
     - Optional[:ref:`MOC <hl7-v2_7_1-MOC>`]
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
     - Optional[:ref:`PRL <hl7-v2_7_1-PRL>`]
     - optional
     - Item #259
   * - ``obr_28``
     - OBR.28
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #260
   * - ``obr_29``
     - OBR.29
     - Optional[:ref:`EIP <hl7-v2_7_1-EIP>`]
     - optional
     - Item #261
   * - ``obr_30``
     - OBR.30
     - Optional[str]
     - optional
     - Item #262 | Table HL70124
   * - ``obr_31``
     - OBR.31
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #263 | Table HL79999
   * - ``obr_32``
     - OBR.32
     - Optional[:ref:`NDL <hl7-v2_7_1-NDL>`]
     - optional
     - Item #264
   * - ``obr_33``
     - OBR.33
     - Optional[List[:ref:`NDL <hl7-v2_7_1-NDL>`]]
     - optional
     - Item #265
   * - ``obr_34``
     - OBR.34
     - Optional[List[:ref:`NDL <hl7-v2_7_1-NDL>`]]
     - optional
     - Item #266
   * - ``obr_35``
     - OBR.35
     - Optional[List[:ref:`NDL <hl7-v2_7_1-NDL>`]]
     - optional
     - Item #267
   * - ``obr_36``
     - OBR.36
     - Optional[str]
     - optional
     - Item #268
   * - ``obr_37``
     - OBR.37
     - Optional[str]
     - optional
     - Item #1028
   * - ``obr_38``
     - OBR.38
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1029 | Table HL79999
   * - ``obr_39``
     - OBR.39
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1030 | Table HL79999
   * - ``obr_40``
     - OBR.40
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1031 | Table HL79999
   * - ``obr_41``
     - OBR.41
     - Optional[str]
     - optional
     - Item #1032 | Table HL70224
   * - ``obr_42``
     - OBR.42
     - Optional[str]
     - optional
     - Item #1033 | Table HL70225
   * - ``obr_43``
     - OBR.43
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1034 | Table HL79999
   * - ``obr_44``
     - OBR.44
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #393 | Table HL70088
   * - ``obr_45``
     - OBR.45
     - Optional[List[:ref:`CNE <hl7-v2_7_1-CNE>`]]
     - optional
     - Item #1316 | Table HL70340
   * - ``obr_46``
     - OBR.46
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1474 | Table HL70411
   * - ``obr_47``
     - OBR.47
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1475 | Table HL70411
   * - ``obr_48``
     - OBR.48
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1646 | Table HL70476
   * - ``obr_49``
     - OBR.49
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1647 | Table HL70507
   * - ``obr_50``
     - OBR.50
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2286
   * - ``obr_51``
     - OBR.51
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2307
   * - ``obr_52``
     - OBR.52
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2308
   * - ``obr_53``
     - OBR.53
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #3303
   * - ``obr_54``
     - OBR.54
     - Optional[:ref:`EIP <hl7-v2_7_1-EIP>`]
     - optional
     - Item #222

.. _hl7-v2_7_1-OBX:

OBX Observation/Result (S7.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.OBX.OBX
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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #571 | Table HL79999
   * - ``obx_4``
     - OBX.4
     - str
     - required
     - Item #572
   * - ``obx_5``
     - OBX.5
     - Optional[List[varies]]
     - optional
     - Item #573
   * - ``obx_6``
     - OBX.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #574 | Table HL79999
   * - ``obx_7``
     - OBX.7
     - Optional[str]
     - optional
     - Item #575
   * - ``obx_8``
     - OBX.8
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #576 | Table HL70078
   * - ``obx_9``
     - OBX.9
     - Optional[str]
     - optional
     - Item #577
   * - ``obx_10``
     - OBX.10
     - Optional[List[str]]
     - optional
     - Item #578 | Table HL70080
   * - ``obx_11``
     - OBX.11
     - str
     - required
     - Item #579 | Table HL70085
   * - ``obx_12``
     - OBX.12
     - Optional[str]
     - optional
     - Item #580
   * - ``obx_13``
     - OBX.13
     - Optional[str]
     - optional
     - Item #581
   * - ``obx_14``
     - OBX.14
     - Optional[str]
     - optional
     - Item #582
   * - ``obx_15``
     - OBX.15
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #583 | Table HL79999
   * - ``obx_16``
     - OBX.16
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #584
   * - ``obx_17``
     - OBX.17
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #936 | Table HL79999
   * - ``obx_18``
     - OBX.18
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #1479
   * - ``obx_19``
     - OBX.19
     - Optional[str]
     - optional
     - Item #1480
   * - ``obx_20``
     - OBX.20
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2179 | Table HL70163
   * - ``obx_21``
     - OBX.21
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2180
   * - ``obx_22``
     - OBX.22
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2182 | Table HL70725
   * - ``obx_23``
     - OBX.23
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #2283
   * - ``obx_24``
     - OBX.24
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #2284
   * - ``obx_25``
     - OBX.25
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #2285
   * - ``obx_26``
     - OBX.26
     - Optional[str]
     - optional
     - Item #2313 | Table HL70909

.. _hl7-v2_7_1-ODS:

ODS Dietary Orders, Supplements, and Preferences (S4.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ODS.ODS
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
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #270 | Table HL79999
   * - ``ods_3``
     - ODS.3
     - List[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - required
     - Item #271 | Table HL79999
   * - ``ods_4``
     - ODS.4
     - Optional[List[str]]
     - optional
     - Item #272

.. _hl7-v2_7_1-ODT:

ODT Diet Tray Instructions (S4.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ODT.ODT
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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #273 | Table HL70160
   * - ``odt_2``
     - ODT.2
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #270 | Table HL79999
   * - ``odt_3``
     - ODT.3
     - Optional[str]
     - optional
     - Item #272

.. _hl7-v2_7_1-OM1:

OM1 General Segment (S8.8.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.OM1.OM1
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
     - str
     - required
     - Item #586
   * - ``om1_2``
     - OM1.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #587 | Table HL79999
   * - ``om1_3``
     - OM1.3
     - Optional[List[str]]
     - optional
     - Item #588 | Table HL70125
   * - ``om1_4``
     - OM1.4
     - str
     - required
     - Item #589 | Table HL70136
   * - ``om1_5``
     - OM1.5
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #590 | Table HL79999
   * - ``om1_6``
     - OM1.6
     - Optional[str]
     - optional
     - Item #591
   * - ``om1_7``
     - OM1.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #592 | Table HL79999
   * - ``om1_8``
     - OM1.8
     - List[str]
     - required
     - Item #593
   * - ``om1_9``
     - OM1.9
     - Optional[str]
     - optional
     - Item #594
   * - ``om1_10``
     - OM1.10
     - Optional[str]
     - optional
     - Item #595
   * - ``om1_11``
     - OM1.11
     - Optional[str]
     - optional
     - Item #596
   * - ``om1_12``
     - OM1.12
     - Optional[str]
     - optional
     - Item #597 | Table HL70136
   * - ``om1_13``
     - OM1.13
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #598 | Table HL79999
   * - ``om1_14``
     - OM1.14
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #599 | Table HL79999
   * - ``om1_15``
     - OM1.15
     - Optional[str]
     - optional
     - Item #600 | Table HL70136
   * - ``om1_16``
     - OM1.16
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #601 | Table HL79999
   * - ``om1_17``
     - OM1.17
     - Optional[:ref:`XTN <hl7-v2_7_1-XTN>`]
     - optional
     - Item #602
   * - ``om1_18``
     - OM1.18
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #603 | Table HL70174
   * - ``om1_19``
     - OM1.19
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #604 | Table HL79999
   * - ``om1_20``
     - OM1.20
     - Optional[str]
     - optional
     - Item #605
   * - ``om1_21``
     - OM1.21
     - Optional[str]
     - optional
     - Item #606
   * - ``om1_22``
     - OM1.22
     - Optional[str]
     - optional
     - Item #607
   * - ``om1_23``
     - OM1.23
     - Optional[str]
     - optional
     - Item #608
   * - ``om1_24``
     - OM1.24
     - Optional[str]
     - optional
     - Item #609
   * - ``om1_25``
     - OM1.25
     - Optional[List[str]]
     - optional
     - Item #610 | Table HL70168
   * - ``om1_26``
     - OM1.26
     - Optional[str]
     - optional
     - Item #611 | Table HL70169
   * - ``om1_27``
     - OM1.27
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #612 | Table HL79999
   * - ``om1_28``
     - OM1.28
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #613
   * - ``om1_29``
     - OM1.29
     - Optional[:ref:`XTN <hl7-v2_7_1-XTN>`]
     - optional
     - Item #614
   * - ``om1_30``
     - OM1.30
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #615 | Table HL70177
   * - ``om1_31``
     - OM1.31
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #616 | Table HL79999
   * - ``om1_32``
     - OM1.32
     - Optional[str]
     - optional
     - Item #617
   * - ``om1_33``
     - OM1.33
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #618 | Table HL79999
   * - ``om1_34``
     - OM1.34
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #619 | Table HL79999
   * - ``om1_35``
     - OM1.35
     - Optional[str]
     - optional
     - Item #620
   * - ``om1_36``
     - OM1.36
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #621 | Table HL79999
   * - ``om1_37``
     - OM1.37
     - Optional[str]
     - optional
     - Item #622
   * - ``om1_38``
     - OM1.38
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #623 | Table HL79999
   * - ``om1_39``
     - OM1.39
     - Optional[str]
     - optional
     - Item #624
   * - ``om1_40``
     - OM1.40
     - Optional[List[str]]
     - optional
     - Item #625
   * - ``om1_41``
     - OM1.41
     - Optional[str]
     - optional
     - Item #626
   * - ``om1_42``
     - OM1.42
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #937 | Table HL70254
   * - ``om1_43``
     - OM1.43
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #938 | Table HL70255
   * - ``om1_44``
     - OM1.44
     - Optional[str]
     - optional
     - Item #939 | Table HL70256
   * - ``om1_45``
     - OM1.45
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #940 | Table HL70258
   * - ``om1_46``
     - OM1.46
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #941 | Table HL79999
   * - ``om1_47``
     - OM1.47
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #942 | Table HL70910

.. _hl7-v2_7_1-OM2:

OM2 Numeric Observation (S8.8.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.OM2.OM2
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
     - Item #586
   * - ``om2_2``
     - OM2.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #627 | Table HL79999
   * - ``om2_3``
     - OM2.3
     - Optional[List[str]]
     - optional
     - Item #628
   * - ``om2_4``
     - OM2.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #629 | Table HL79999
   * - ``om2_5``
     - OM2.5
     - Optional[str]
     - optional
     - Item #630
   * - ``om2_6``
     - OM2.6
     - Optional[List[:ref:`RFR <hl7-v2_7_1-RFR>`]]
     - optional
     - Item #631
   * - ``om2_7``
     - OM2.7
     - Optional[List[:ref:`RFR <hl7-v2_7_1-RFR>`]]
     - optional
     - Item #632
   * - ``om2_8``
     - OM2.8
     - Optional[:ref:`RFR <hl7-v2_7_1-RFR>`]
     - optional
     - Item #633
   * - ``om2_9``
     - OM2.9
     - Optional[List[:ref:`DLT <hl7-v2_7_1-DLT>`]]
     - optional
     - Item #634
   * - ``om2_10``
     - OM2.10
     - Optional[str]
     - optional
     - Item #635

.. _hl7-v2_7_1-OM3:

OM3 Categorical Service/Test/Observation (S8.8.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.OM3.OM3
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
     - Item #586
   * - ``om3_2``
     - OM3.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #636 | Table HL79999
   * - ``om3_3``
     - OM3.3
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #637 | Table HL79999
   * - ``om3_4``
     - OM3.4
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #638 | Table HL79999
   * - ``om3_5``
     - OM3.5
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #639 | Table HL79999
   * - ``om3_6``
     - OM3.6
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #640 | Table HL79999
   * - ``om3_7``
     - OM3.7
     - Optional[str]
     - optional
     - Item #570 | Table HL70125

.. _hl7-v2_7_1-OM4:

OM4 Observations that Require Specimens (S8.8.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.OM4.OM4
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
     - Item #586
   * - ``om4_2``
     - OM4.2
     - Optional[str]
     - optional
     - Item #642 | Table HL70170
   * - ``om4_3``
     - OM4.3
     - Optional[str]
     - optional
     - Item #643
   * - ``om4_4``
     - OM4.4
     - Optional[str]
     - optional
     - Item #644
   * - ``om4_5``
     - OM4.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #645 | Table HL79999
   * - ``om4_6``
     - OM4.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #646 | Table HL79999
   * - ``om4_7``
     - OM4.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #647 | Table HL70371
   * - ``om4_8``
     - OM4.8
     - Optional[str]
     - optional
     - Item #648
   * - ``om4_9``
     - OM4.9
     - Optional[str]
     - optional
     - Item #649
   * - ``om4_10``
     - OM4.10
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #650
   * - ``om4_11``
     - OM4.11
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #651
   * - ``om4_12``
     - OM4.12
     - Optional[str]
     - optional
     - Item #652
   * - ``om4_13``
     - OM4.13
     - Optional[List[str]]
     - optional
     - Item #653 | Table HL70027
   * - ``om4_14``
     - OM4.14
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #654

.. _hl7-v2_7_1-OM5:

OM5 Observation Batteries (Sets) (S8.8.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.OM5.OM5
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
     - Item #586
   * - ``om5_2``
     - OM5.2
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #655 | Table HL79999
   * - ``om5_3``
     - OM5.3
     - Optional[str]
     - optional
     - Item #656

.. _hl7-v2_7_1-OM6:

OM6 Observations that are Calculated from Other Observations (S8.8.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.OM6.OM6
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
     - Item #586
   * - ``om6_2``
     - OM6.2
     - Optional[str]
     - optional
     - Item #657

.. _hl7-v2_7_1-OM7:

OM7 Additional Basic Attributes (S8.8.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.OM7.OM7
   :noindex:

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
     - Item #586
   * - ``om7_2``
     - OM7.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #238
   * - ``om7_3``
     - OM7.3
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1481 | Table HL70412
   * - ``om7_4``
     - OM7.4
     - Optional[str]
     - optional
     - Item #1482
   * - ``om7_5``
     - OM7.5
     - Optional[List[str]]
     - optional
     - Item #1483
   * - ``om7_6``
     - OM7.6
     - Optional[str]
     - optional
     - Item #1484
   * - ``om7_7``
     - OM7.7
     - Optional[str]
     - optional
     - Item #1485
   * - ``om7_8``
     - OM7.8
     - Optional[str]
     - optional
     - Item #1486
   * - ``om7_9``
     - OM7.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1487 | Table HL79999
   * - ``om7_10``
     - OM7.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1488
   * - ``om7_11``
     - OM7.11
     - Optional[str]
     - optional
     - Item #1489 | Table HL70136
   * - ``om7_12``
     - OM7.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1490 | Table HL70413
   * - ``om7_13``
     - OM7.13
     - Optional[str]
     - optional
     - Item #1491
   * - ``om7_14``
     - OM7.14
     - Optional[str]
     - optional
     - Item #1492
   * - ``om7_15``
     - OM7.15
     - Optional[str]
     - optional
     - Item #1493
   * - ``om7_16``
     - OM7.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1494 | Table HL70414
   * - ``om7_17``
     - OM7.17
     - Optional[str]
     - optional
     - Item #1495
   * - ``om7_18``
     - OM7.18
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1496 | Table HL70414
   * - ``om7_19``
     - OM7.19
     - Optional[str]
     - optional
     - Item #607
   * - ``om7_20``
     - OM7.20
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #224
   * - ``om7_21``
     - OM7.21
     - Optional[List[:ref:`PL <hl7-v2_7_1-PL>`]]
     - optional
     - Item #1497
   * - ``om7_22``
     - OM7.22
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1498 | Table HL70473
   * - ``om7_23``
     - OM7.23
     - Optional[str]
     - optional
     - Item #1499 | Table HL70136
   * - ``om7_24``
     - OM7.24
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1306 | Table HL70132

.. _hl7-v2_7_1-ORC:

ORC Common Order (S4.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ORC.ORC
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
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #216
   * - ``orc_3``
     - ORC.3
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #217
   * - ``orc_4``
     - ORC.4
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
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
   * - ``orc_8``
     - ORC.8
     - Optional[:ref:`EIP <hl7-v2_7_1-EIP>`]
     - optional
     - Item #222
   * - ``orc_9``
     - ORC.9
     - Optional[str]
     - optional
     - Item #223
   * - ``orc_10``
     - ORC.10
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #224
   * - ``orc_11``
     - ORC.11
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #225
   * - ``orc_12``
     - ORC.12
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #226
   * - ``orc_13``
     - ORC.13
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #227
   * - ``orc_14``
     - ORC.14
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #228
   * - ``orc_15``
     - ORC.15
     - Optional[str]
     - optional
     - Item #229
   * - ``orc_16``
     - ORC.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #230 | Table HL79999
   * - ``orc_17``
     - ORC.17
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #231 | Table HL79999
   * - ``orc_18``
     - ORC.18
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #232 | Table HL79999
   * - ``orc_19``
     - ORC.19
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #233
   * - ``orc_20``
     - ORC.20
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1310 | Table HL70339
   * - ``orc_21``
     - ORC.21
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #1311
   * - ``orc_22``
     - ORC.22
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #1312
   * - ``orc_23``
     - ORC.23
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #1313
   * - ``orc_24``
     - ORC.24
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #1314
   * - ``orc_25``
     - ORC.25
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1473 | Table HL79999
   * - ``orc_26``
     - ORC.26
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1641 | Table HL70552
   * - ``orc_27``
     - ORC.27
     - Optional[str]
     - optional
     - Item #1642
   * - ``orc_28``
     - ORC.28
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #615 | Table HL70177
   * - ``orc_29``
     - ORC.29
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1643 | Table HL70482
   * - ``orc_30``
     - ORC.30
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #1644 | Table HL70483
   * - ``orc_31``
     - ORC.31
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2287
   * - ``orc_32``
     - ORC.32
     - Optional[str]
     - optional
     - Item #2301
   * - ``orc_33``
     - ORC.33
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #3300

.. _hl7-v2_7_1-ORG:

ORG Practitioner Organization Unit s (S15.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ORG.ORG
   :noindex:

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
     - Item #1459
   * - ``org_2``
     - ORG.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1460 | Table HL70405
   * - ``org_3``
     - ORG.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1625 | Table HL70474
   * - ``org_4``
     - ORG.4
     - Optional[str]
     - optional
     - Item #1462 | Table HL70136
   * - ``org_5``
     - ORG.5
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #1463
   * - ``org_6``
     - ORG.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1464 | Table HL70452
   * - ``org_7``
     - ORG.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1614 | Table HL70453
   * - ``org_8``
     - ORG.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1615 | Table HL70454
   * - ``org_9``
     - ORG.9
     - Optional[:ref:`DR <hl7-v2_7_1-DR>`]
     - optional
     - Item #1465
   * - ``org_10``
     - ORG.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1276 | Table HL70066
   * - ``org_11``
     - ORG.11
     - Optional[str]
     - optional
     - Item #1467 | Table HL70136
   * - ``org_12``
     - ORG.12
     - Optional[str]
     - optional
     - Item #1468 | Table HL70136
   * - ``org_13``
     - ORG.13
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1891 | Table HL70539

.. _hl7-v2_7_1-OVR:

OVR Override Segment (S2.14.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.OVR.OVR
   :noindex:

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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1829 | Table HL70518
   * - ``ovr_2``
     - OVR.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1830 | Table HL70521
   * - ``ovr_3``
     - OVR.3
     - Optional[str]
     - optional
     - Item #1831
   * - ``ovr_4``
     - OVR.4
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1832
   * - ``ovr_5``
     - OVR.5
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1833

.. _hl7-v2_7_1-PAC:

PAC Shipment Package (S7.18.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PAC.PAC
   :noindex:

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
     - Item #2350
   * - ``pac_2``
     - PAC.2
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2351
   * - ``pac_3``
     - PAC.3
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2352
   * - ``pac_4``
     - PAC.4
     - Optional[:ref:`NA <hl7-v2_7_1-NA>`]
     - optional
     - Item #2353
   * - ``pac_5``
     - PAC.5
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #2354 | Table HL70908
   * - ``pac_6``
     - PAC.6
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2355 | Table HL70544
   * - ``pac_7``
     - PAC.7
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2356 | Table HL70376
   * - ``pac_8``
     - PAC.8
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2357 | Table HL70489

.. _hl7-v2_7_1-PCE:

PCE Patient Charge Cost Center Exceptions (S17.4.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PCE.PCE
   :noindex:

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
     - Item #2228
   * - ``pce_2``
     - PCE.2
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #281 | Table HL70319
   * - ``pce_3``
     - PCE.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #361 | Table HL70132
   * - ``pce_4``
     - PCE.4
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #366

.. _hl7-v2_7_1-PCR:

PCR Possible Causal Relationship (S7.12.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PCR.PCR
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1098 | Table HL79999
   * - ``pcr_2``
     - PCR.2
     - Optional[str]
     - optional
     - Item #1099 | Table HL70249
   * - ``pcr_3``
     - PCR.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1100 | Table HL79999
   * - ``pcr_4``
     - PCR.4
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1101
   * - ``pcr_5``
     - PCR.5
     - Optional[str]
     - optional
     - Item #1102
   * - ``pcr_6``
     - PCR.6
     - Optional[str]
     - optional
     - Item #1103
   * - ``pcr_7``
     - PCR.7
     - Optional[str]
     - optional
     - Item #1104
   * - ``pcr_8``
     - PCR.8
     - Optional[str]
     - optional
     - Item #1105
   * - ``pcr_9``
     - PCR.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1106 | Table HL70244
   * - ``pcr_10``
     - PCR.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1107 | Table HL79999
   * - ``pcr_11``
     - PCR.11
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1108 | Table HL70245
   * - ``pcr_12``
     - PCR.12
     - Optional[List[str]]
     - optional
     - Item #1109
   * - ``pcr_13``
     - PCR.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1110 | Table HL70246
   * - ``pcr_14``
     - PCR.14
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1111 | Table HL79999
   * - ``pcr_15``
     - PCR.15
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1112 | Table HL70247
   * - ``pcr_16``
     - PCR.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1113 | Table HL79999
   * - ``pcr_17``
     - PCR.17
     - Optional[str]
     - optional
     - Item #1114 | Table HL70248
   * - ``pcr_18``
     - PCR.18
     - Optional[str]
     - optional
     - Item #1115
   * - ``pcr_19``
     - PCR.19
     - Optional[str]
     - optional
     - Item #1116 | Table HL70242
   * - ``pcr_20``
     - PCR.20
     - Optional[str]
     - optional
     - Item #1117 | Table HL70250
   * - ``pcr_21``
     - PCR.21
     - Optional[List[str]]
     - optional
     - Item #1118 | Table HL70251
   * - ``pcr_22``
     - PCR.22
     - Optional[List[str]]
     - optional
     - Item #1119 | Table HL70252
   * - ``pcr_23``
     - PCR.23
     - Optional[List[str]]
     - optional
     - Item #1120 | Table HL70253

.. _hl7-v2_7_1-PD1:

PD1 Patient Additional Demographic (S3.4.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PD1.PD1
   :noindex:

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
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #755 | Table HL70223
   * - ``pd1_2``
     - PD1.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #742 | Table HL70220
   * - ``pd1_3``
     - PD1.3
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #756 | Table HL70204
   * - ``pd1_5``
     - PD1.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #745 | Table HL70231
   * - ``pd1_6``
     - PD1.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #753 | Table HL70295
   * - ``pd1_7``
     - PD1.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #759 | Table HL70315
   * - ``pd1_8``
     - PD1.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #760 | Table HL70316
   * - ``pd1_9``
     - PD1.9
     - Optional[str]
     - optional
     - Item #761 | Table HL70136
   * - ``pd1_10``
     - PD1.10
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #762
   * - ``pd1_11``
     - PD1.11
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #743 | Table HL70215
   * - ``pd1_12``
     - PD1.12
     - Optional[str]
     - optional
     - Item #744 | Table HL70136
   * - ``pd1_13``
     - PD1.13
     - Optional[str]
     - optional
     - Item #1566
   * - ``pd1_14``
     - PD1.14
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #1567
   * - ``pd1_15``
     - PD1.15
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1548 | Table HL70435
   * - ``pd1_16``
     - PD1.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1569 | Table HL70441
   * - ``pd1_17``
     - PD1.17
     - Optional[str]
     - optional
     - Item #1570
   * - ``pd1_18``
     - PD1.18
     - Optional[str]
     - optional
     - Item #1571
   * - ``pd1_19``
     - PD1.19
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1572 | Table HL70140
   * - ``pd1_20``
     - PD1.20
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #486 | Table HL70141
   * - ``pd1_21``
     - PD1.21
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1573 | Table HL70142
   * - ``pd1_22``
     - PD1.22
     - Optional[str]
     - optional
     - Item #2141

.. _hl7-v2_7_1-PDA:

PDA Patient Death and Autopsy (S3.4.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PDA.PDA
   :noindex:

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
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1574
   * - ``pda_2``
     - PDA.2
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #1575
   * - ``pda_3``
     - PDA.3
     - Optional[str]
     - optional
     - Item #1576 | Table HL70136
   * - ``pda_4``
     - PDA.4
     - Optional[str]
     - optional
     - Item #1577
   * - ``pda_5``
     - PDA.5
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1578
   * - ``pda_6``
     - PDA.6
     - Optional[str]
     - optional
     - Item #1579 | Table HL70136
   * - ``pda_7``
     - PDA.7
     - Optional[:ref:`DR <hl7-v2_7_1-DR>`]
     - optional
     - Item #1580
   * - ``pda_8``
     - PDA.8
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1581
   * - ``pda_9``
     - PDA.9
     - Optional[str]
     - optional
     - Item #1582 | Table HL70136

.. _hl7-v2_7_1-PDC:

PDC Product Detail Country (S7.12.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PDC.PDC
   :noindex:

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
     - List[:ref:`XON <hl7-v2_7_1-XON>`]
     - required
     - Item #1247
   * - ``pdc_2``
     - PDC.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1248 | Table HL79999
   * - ``pdc_3``
     - PDC.3
     - str
     - required
     - Item #1249
   * - ``pdc_4``
     - PDC.4
     - Optional[str]
     - optional
     - Item #1250
   * - ``pdc_5``
     - PDC.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1251 | Table HL79999
   * - ``pdc_6``
     - PDC.6
     - Optional[List[str]]
     - optional
     - Item #1252
   * - ``pdc_7``
     - PDC.7
     - Optional[str]
     - optional
     - Item #1253
   * - ``pdc_8``
     - PDC.8
     - Optional[List[str]]
     - optional
     - Item #1254
   * - ``pdc_9``
     - PDC.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1255 | Table HL79999
   * - ``pdc_10``
     - PDC.10
     - Optional[str]
     - optional
     - Item #1256 | Table HL70330
   * - ``pdc_11``
     - PDC.11
     - Optional[str]
     - optional
     - Item #1257
   * - ``pdc_12``
     - PDC.12
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1258
   * - ``pdc_13``
     - PDC.13
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1259
   * - ``pdc_14``
     - PDC.14
     - Optional[str]
     - optional
     - Item #1260
   * - ``pdc_15``
     - PDC.15
     - Optional[str]
     - optional
     - Item #1261

.. _hl7-v2_7_1-PEO:

PEO Product Experience Observation (S7.12.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PEO.PEO
   :noindex:

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
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1073 | Table HL79999
   * - ``peo_2``
     - PEO.2
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1074 | Table HL79999
   * - ``peo_3``
     - PEO.3
     - str
     - required
     - Item #1075
   * - ``peo_4``
     - PEO.4
     - Optional[str]
     - optional
     - Item #1076
   * - ``peo_5``
     - PEO.5
     - Optional[str]
     - optional
     - Item #1077
   * - ``peo_6``
     - PEO.6
     - Optional[str]
     - optional
     - Item #1078
   * - ``peo_7``
     - PEO.7
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #1079
   * - ``peo_8``
     - PEO.8
     - Optional[List[str]]
     - optional
     - Item #1080 | Table HL70237
   * - ``peo_9``
     - PEO.9
     - Optional[str]
     - optional
     - Item #1081 | Table HL70238
   * - ``peo_10``
     - PEO.10
     - Optional[str]
     - optional
     - Item #1082 | Table HL70239
   * - ``peo_11``
     - PEO.11
     - Optional[List[str]]
     - optional
     - Item #1083 | Table HL70240
   * - ``peo_12``
     - PEO.12
     - Optional[str]
     - optional
     - Item #1084 | Table HL70241
   * - ``peo_13``
     - PEO.13
     - Optional[List[str]]
     - optional
     - Item #1085
   * - ``peo_14``
     - PEO.14
     - Optional[List[str]]
     - optional
     - Item #1086
   * - ``peo_15``
     - PEO.15
     - Optional[List[str]]
     - optional
     - Item #1087
   * - ``peo_16``
     - PEO.16
     - Optional[List[str]]
     - optional
     - Item #1088
   * - ``peo_17``
     - PEO.17
     - Optional[List[str]]
     - optional
     - Item #1089
   * - ``peo_18``
     - PEO.18
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1090 | Table HL79999
   * - ``peo_19``
     - PEO.19
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #1091
   * - ``peo_20``
     - PEO.20
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #1092
   * - ``peo_21``
     - PEO.21
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #1093
   * - ``peo_22``
     - PEO.22
     - Optional[str]
     - optional
     - Item #1094 | Table HL70242
   * - ``peo_23``
     - PEO.23
     - Optional[str]
     - optional
     - Item #1095 | Table HL70242
   * - ``peo_24``
     - PEO.24
     - Optional[str]
     - optional
     - Item #1096
   * - ``peo_25``
     - PEO.25
     - Optional[str]
     - optional
     - Item #1097 | Table HL70243

.. _hl7-v2_7_1-PES:

PES Product Experience Sender (S7.12.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PES.PES
   :noindex:

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
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #1059
   * - ``pes_2``
     - PES.2
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #1060
   * - ``pes_3``
     - PES.3
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #1062
   * - ``pes_4``
     - PES.4
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #1063
   * - ``pes_5``
     - PES.5
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1064
   * - ``pes_6``
     - PES.6
     - Optional[str]
     - optional
     - Item #1065
   * - ``pes_7``
     - PES.7
     - Optional[List[str]]
     - optional
     - Item #1066
   * - ``pes_8``
     - PES.8
     - Optional[str]
     - optional
     - Item #1067
   * - ``pes_9``
     - PES.9
     - Optional[str]
     - optional
     - Item #1068
   * - ``pes_10``
     - PES.10
     - str
     - required
     - Item #1069
   * - ``pes_11``
     - PES.11
     - Optional[List[str]]
     - optional
     - Item #1070 | Table HL70234
   * - ``pes_12``
     - PES.12
     - Optional[str]
     - optional
     - Item #1071 | Table HL70235
   * - ``pes_13``
     - PES.13
     - Optional[List[str]]
     - optional
     - Item #1072 | Table HL70236

.. _hl7-v2_7_1-PID:

PID Patient Identification (S3.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PID.PID
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
   * - ``pid_3``
     - PID.3
     - List[:ref:`CX <hl7-v2_7_1-CX>`]
     - required
     - Item #106
   * - ``pid_5``
     - PID.5
     - List[:ref:`XPN <hl7-v2_7_1-XPN>`]
     - required
     - Item #108 | Table HL70200
   * - ``pid_6``
     - PID.6
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #109
   * - ``pid_7``
     - PID.7
     - Optional[str]
     - optional
     - Item #110
   * - ``pid_8``
     - PID.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #111 | Table HL70001
   * - ``pid_10``
     - PID.10
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #113 | Table HL70005
   * - ``pid_11``
     - PID.11
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #114
   * - ``pid_13``
     - PID.13
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #116
   * - ``pid_14``
     - PID.14
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #117
   * - ``pid_15``
     - PID.15
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #118 | Table HL70296
   * - ``pid_16``
     - PID.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #119 | Table HL70002
   * - ``pid_17``
     - PID.17
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #120 | Table HL70006
   * - ``pid_18``
     - PID.18
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #121
   * - ``pid_21``
     - PID.21
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #124
   * - ``pid_22``
     - PID.22
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
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
     - Item #127 | Table HL70136
   * - ``pid_25``
     - PID.25
     - Optional[str]
     - optional
     - Item #128
   * - ``pid_26``
     - PID.26
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #129 | Table HL70171
   * - ``pid_27``
     - PID.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #130 | Table HL70172
   * - ``pid_29``
     - PID.29
     - Optional[str]
     - optional
     - Item #740
   * - ``pid_30``
     - PID.30
     - Optional[str]
     - optional
     - Item #741 | Table HL70136
   * - ``pid_31``
     - PID.31
     - Optional[str]
     - optional
     - Item #1535 | Table HL70136
   * - ``pid_32``
     - PID.32
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1536 | Table HL70445
   * - ``pid_33``
     - PID.33
     - Optional[str]
     - optional
     - Item #1537
   * - ``pid_34``
     - PID.34
     - Optional[:ref:`HD <hl7-v2_7_1-HD>`]
     - optional
     - Item #1538
   * - ``pid_35``
     - PID.35
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1539 | Table HL70446
   * - ``pid_36``
     - PID.36
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1540 | Table HL70447
   * - ``pid_37``
     - PID.37
     - Optional[str]
     - optional
     - Item #1541
   * - ``pid_38``
     - PID.38
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1542 | Table HL70429
   * - ``pid_39``
     - PID.39
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1840 | Table HL70171
   * - ``pid_40``
     - PID.40
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #2289

.. _hl7-v2_7_1-PKG:

PKG Item Packaging (S17.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PKG.PKG
   :noindex:

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
     - Item #2221
   * - ``pkg_2``
     - PKG.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2222 | Table HL70818
   * - ``pkg_3``
     - PKG.3
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2223 | Table HL70532
   * - ``pkg_4``
     - PKG.4
     - Optional[str]
     - optional
     - Item #2224
   * - ``pkg_5``
     - PKG.5
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #2225
   * - ``pkg_6``
     - PKG.6
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #2226
   * - ``pkg_7``
     - PKG.7
     - Optional[str]
     - optional
     - Item #2227

.. _hl7-v2_7_1-PMT:

PMT Payment Information (S16.4.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PMT.PMT
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2018
   * - ``pmt_2``
     - PMT.2
     - str
     - required
     - Item #2019
   * - ``pmt_3``
     - PMT.3
     - str
     - required
     - Item #2020
   * - ``pmt_4``
     - PMT.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #2021 | Table HL70570
   * - ``pmt_5``
     - PMT.5
     - str
     - required
     - Item #2022
   * - ``pmt_6``
     - PMT.6
     - :ref:`CP <hl7-v2_7_1-CP>`
     - required
     - Item #2023
   * - ``pmt_7``
     - PMT.7
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2024
   * - ``pmt_8``
     - PMT.8
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #2025
   * - ``pmt_9``
     - PMT.9
     - Optional[str]
     - optional
     - Item #2026
   * - ``pmt_10``
     - PMT.10
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #2027
   * - ``pmt_11``
     - PMT.11
     - :ref:`XON <hl7-v2_7_1-XON>`
     - required
     - Item #2028
   * - ``pmt_12``
     - PMT.12
     - Optional[str]
     - optional
     - Item #2029

.. _hl7-v2_7_1-PR1:

PR1 Procedures (S6.5.4).
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PR1.PR1
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
   * - ``pr1_3``
     - PR1.3
     - :ref:`CNE <hl7-v2_7_1-CNE>`
     - required
     - Item #393 | Table HL70088
   * - ``pr1_5``
     - PR1.5
     - str
     - required
     - Item #395
   * - ``pr1_6``
     - PR1.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #396 | Table HL70230
   * - ``pr1_7``
     - PR1.7
     - Optional[str]
     - optional
     - Item #397
   * - ``pr1_9``
     - PR1.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #399 | Table HL70019
   * - ``pr1_10``
     - PR1.10
     - Optional[str]
     - optional
     - Item #400
   * - ``pr1_13``
     - PR1.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #403 | Table HL70059
   * - ``pr1_14``
     - PR1.14
     - Optional[str]
     - optional
     - Item #404 | Table HL70418
   * - ``pr1_15``
     - PR1.15
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #772 | Table HL70051
   * - ``pr1_16``
     - PR1.16
     - Optional[List[:ref:`CNE <hl7-v2_7_1-CNE>`]]
     - optional
     - Item #1316 | Table HL70340
   * - ``pr1_17``
     - PR1.17
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1501 | Table HL70416
   * - ``pr1_18``
     - PR1.18
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1502 | Table HL70417
   * - ``pr1_19``
     - PR1.19
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1848
   * - ``pr1_20``
     - PR1.20
     - Optional[str]
     - optional
     - Item #1849 | Table HL70206
   * - ``pr1_21``
     - PR1.21
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2177 | Table HL70761
   * - ``pr1_22``
     - PR1.22
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2178 | Table HL70763
   * - ``pr1_23``
     - PR1.23
     - Optional[List[:ref:`PL <hl7-v2_7_1-PL>`]]
     - optional
     - Item #2371
   * - ``pr1_24``
     - PR1.24
     - Optional[str]
     - optional
     - Item #2372 | Table HL70136
   * - ``pr1_25``
     - PR1.25
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2373

.. _hl7-v2_7_1-PRA:

PRA Practitioner Detail (S15.4.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PRA.PRA
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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #685 | Table HL79999
   * - ``pra_2``
     - PRA.2
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #686 | Table HL70358
   * - ``pra_3``
     - PRA.3
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #687 | Table HL70186
   * - ``pra_4``
     - PRA.4
     - Optional[str]
     - optional
     - Item #688 | Table HL70187
   * - ``pra_5``
     - PRA.5
     - Optional[List[:ref:`SPD <hl7-v2_7_1-SPD>`]]
     - optional
     - Item #689 | Table HL70337
   * - ``pra_6``
     - PRA.6
     - Optional[List[:ref:`PLN <hl7-v2_7_1-PLN>`]]
     - optional
     - Item #690 | Table HL70338
   * - ``pra_7``
     - PRA.7
     - Optional[List[:ref:`PIP <hl7-v2_7_1-PIP>`]]
     - optional
     - Item #691
   * - ``pra_8``
     - PRA.8
     - Optional[str]
     - optional
     - Item #1296
   * - ``pra_9``
     - PRA.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1613 | Table HL70537
   * - ``pra_10``
     - PRA.10
     - Optional[str]
     - optional
     - Item #1348
   * - ``pra_11``
     - PRA.11
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1388 | Table HL70401
   * - ``pra_12``
     - PRA.12
     - Optional[str]
     - optional
     - Item #1616

.. _hl7-v2_7_1-PRB:

PRB Problem Details (S12.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PRB.PRB
   :noindex:

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
     - Item #816 | Table HL70287
   * - ``prb_2``
     - PRB.2
     - str
     - required
     - Item #817
   * - ``prb_3``
     - PRB.3
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #838
   * - ``prb_4``
     - PRB.4
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #839
   * - ``prb_5``
     - PRB.5
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #820
   * - ``prb_6``
     - PRB.6
     - Optional[str]
     - optional
     - Item #841
   * - ``prb_7``
     - PRB.7
     - Optional[str]
     - optional
     - Item #842
   * - ``prb_8``
     - PRB.8
     - Optional[str]
     - optional
     - Item #843
   * - ``prb_9``
     - PRB.9
     - Optional[str]
     - optional
     - Item #844
   * - ``prb_10``
     - PRB.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #845
   * - ``prb_11``
     - PRB.11
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #846
   * - ``prb_12``
     - PRB.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #847
   * - ``prb_13``
     - PRB.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #848
   * - ``prb_14``
     - PRB.14
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #849
   * - ``prb_15``
     - PRB.15
     - Optional[str]
     - optional
     - Item #850
   * - ``prb_16``
     - PRB.16
     - Optional[str]
     - optional
     - Item #851
   * - ``prb_17``
     - PRB.17
     - Optional[str]
     - optional
     - Item #852
   * - ``prb_18``
     - PRB.18
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #853
   * - ``prb_19``
     - PRB.19
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #854
   * - ``prb_20``
     - PRB.20
     - Optional[str]
     - optional
     - Item #855
   * - ``prb_21``
     - PRB.21
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #856
   * - ``prb_22``
     - PRB.22
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #857
   * - ``prb_23``
     - PRB.23
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #858
   * - ``prb_24``
     - PRB.24
     - Optional[str]
     - optional
     - Item #859
   * - ``prb_25``
     - PRB.25
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #823
   * - ``prb_26``
     - PRB.26
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2234 | Table HL70836
   * - ``prb_27``
     - PRB.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2235 | Table HL70838
   * - ``prb_28``
     - PRB.28
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2237 | Table HL70725

.. _hl7-v2_7_1-PRC:

PRC Pricing (S8.10.3).
~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PRC.PRC
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #982 | Table HL70132
   * - ``prc_2``
     - PRC.2
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #995 | Table HL70464
   * - ``prc_3``
     - PRC.3
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #676 | Table HL70184
   * - ``prc_4``
     - PRC.4
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #967 | Table HL70004
   * - ``prc_5``
     - PRC.5
     - Optional[List[:ref:`CP <hl7-v2_7_1-CP>`]]
     - optional
     - Item #998
   * - ``prc_6``
     - PRC.6
     - Optional[List[str]]
     - optional
     - Item #999
   * - ``prc_7``
     - PRC.7
     - Optional[str]
     - optional
     - Item #1000
   * - ``prc_8``
     - PRC.8
     - Optional[str]
     - optional
     - Item #1001
   * - ``prc_9``
     - PRC.9
     - Optional[:ref:`MO <hl7-v2_7_1-MO>`]
     - optional
     - Item #1002
   * - ``prc_10``
     - PRC.10
     - Optional[:ref:`MO <hl7-v2_7_1-MO>`]
     - optional
     - Item #1003
   * - ``prc_11``
     - PRC.11
     - Optional[str]
     - optional
     - Item #1004
   * - ``prc_12``
     - PRC.12
     - Optional[str]
     - optional
     - Item #1005
   * - ``prc_13``
     - PRC.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1006 | Table HL70268
   * - ``prc_14``
     - PRC.14
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1007 | Table HL70293
   * - ``prc_15``
     - PRC.15
     - Optional[str]
     - optional
     - Item #1008 | Table HL70136
   * - ``prc_16``
     - PRC.16
     - Optional[str]
     - optional
     - Item #675 | Table HL70183
   * - ``prc_17``
     - PRC.17
     - Optional[:ref:`MO <hl7-v2_7_1-MO>`]
     - optional
     - Item #989
   * - ``prc_18``
     - PRC.18
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1009 | Table HL70269

.. _hl7-v2_7_1-PRD:

PRD Provider Data (S11.7.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PRD.PRD
   :noindex:

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
     - List[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - required
     - Item #1155 | Table HL70286
   * - ``prd_2``
     - PRD.2
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #1156
   * - ``prd_3``
     - PRD.3
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #1157
   * - ``prd_4``
     - PRD.4
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #1158
   * - ``prd_5``
     - PRD.5
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #1159
   * - ``prd_6``
     - PRD.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #684 | Table HL70185
   * - ``prd_7``
     - PRD.7
     - Optional[List[:ref:`PLN <hl7-v2_7_1-PLN>`]]
     - optional
     - Item #1162 | Table HL70338
   * - ``prd_8``
     - PRD.8
     - Optional[str]
     - optional
     - Item #1163
   * - ``prd_9``
     - PRD.9
     - Optional[List[str]]
     - optional
     - Item #1164
   * - ``prd_10``
     - PRD.10
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #2256
   * - ``prd_11``
     - PRD.11
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #2257
   * - ``prd_12``
     - PRD.12
     - Optional[List[:ref:`PL <hl7-v2_7_1-PL>`]]
     - optional
     - Item #2258
   * - ``prd_13``
     - PRD.13
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #2259
   * - ``prd_14``
     - PRD.14
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2260 | Table HL70185

.. _hl7-v2_7_1-PRT:

PRT Participation Information (S7.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PRT.PRT
   :noindex:

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
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2379
   * - ``prt_2``
     - PRT.2
     - str
     - required
     - Item #816 | Table HL70287
   * - ``prt_3``
     - PRT.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2380
   * - ``prt_4``
     - PRT.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #2381 | Table HL70912
   * - ``prt_5``
     - PRT.5
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #2382
   * - ``prt_6``
     - PRT.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2383
   * - ``prt_7``
     - PRT.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2384 | Table HL70406
   * - ``prt_8``
     - PRT.8
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #2385
   * - ``prt_9``
     - PRT.9
     - Optional[List[:ref:`PL <hl7-v2_7_1-PL>`]]
     - optional
     - Item #2386
   * - ``prt_10``
     - PRT.10
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #2348
   * - ``prt_11``
     - PRT.11
     - Optional[str]
     - optional
     - Item #2387
   * - ``prt_12``
     - PRT.12
     - Optional[str]
     - optional
     - Item #2388
   * - ``prt_13``
     - PRT.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2389
   * - ``prt_14``
     - PRT.14
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #2390
   * - ``prt_15``
     - PRT.15
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #2391

.. _hl7-v2_7_1-PSG:

PSG Product/Service Group (S16.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PSG.PSG
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1950
   * - ``psg_2``
     - PSG.2
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1951
   * - ``psg_3``
     - PSG.3
     - str
     - required
     - Item #1952
   * - ``psg_4``
     - PSG.4
     - str
     - required
     - Item #1953 | Table HL70136
   * - ``psg_5``
     - PSG.5
     - :ref:`CP <hl7-v2_7_1-CP>`
     - required
     - Item #1954
   * - ``psg_6``
     - PSG.6
     - str
     - required
     - Item #2044

.. _hl7-v2_7_1-PSH:

PSH Product Summary Header (S7.12.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PSH.PSH
   :noindex:

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
     - Item #1233
   * - ``psh_2``
     - PSH.2
     - Optional[str]
     - optional
     - Item #1297
   * - ``psh_3``
     - PSH.3
     - str
     - required
     - Item #1235
   * - ``psh_4``
     - PSH.4
     - Optional[str]
     - optional
     - Item #1236
   * - ``psh_5``
     - PSH.5
     - Optional[str]
     - optional
     - Item #1237
   * - ``psh_6``
     - PSH.6
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1238
   * - ``psh_7``
     - PSH.7
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1239
   * - ``psh_8``
     - PSH.8
     - Optional[str]
     - optional
     - Item #1240 | Table HL70329
   * - ``psh_9``
     - PSH.9
     - Optional[str]
     - optional
     - Item #1241
   * - ``psh_10``
     - PSH.10
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1242
   * - ``psh_11``
     - PSH.11
     - Optional[str]
     - optional
     - Item #1243 | Table HL70329
   * - ``psh_12``
     - PSH.12
     - Optional[str]
     - optional
     - Item #1244
   * - ``psh_13``
     - PSH.13
     - Optional[List[str]]
     - optional
     - Item #1245
   * - ``psh_14``
     - PSH.14
     - Optional[List[str]]
     - optional
     - Item #1246

.. _hl7-v2_7_1-PSL:

PSL Product/Service Line Item (S16.4.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PSL.PSL
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1955
   * - ``psl_2``
     - PSL.2
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1956
   * - ``psl_3``
     - PSL.3
     - str
     - required
     - Item #1957
   * - ``psl_4``
     - PSL.4
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1958
   * - ``psl_5``
     - PSL.5
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1959
   * - ``psl_6``
     - PSL.6
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1960 | Table HL70559
   * - ``psl_7``
     - PSL.7
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1961 | Table HL70879
   * - ``psl_8``
     - PSL.8
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1962 | Table HL70880
   * - ``psl_9``
     - PSL.9
     - Optional[str]
     - optional
     - Item #1963
   * - ``psl_10``
     - PSL.10
     - Optional[str]
     - optional
     - Item #1964
   * - ``psl_11``
     - PSL.11
     - Optional[str]
     - optional
     - Item #1965
   * - ``psl_12``
     - PSL.12
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1966 | Table HL70560
   * - ``psl_13``
     - PSL.13
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1967
   * - ``psl_14``
     - PSL.14
     - Optional[str]
     - optional
     - Item #1968
   * - ``psl_15``
     - PSL.15
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1969
   * - ``psl_16``
     - PSL.16
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1970
   * - ``psl_17``
     - PSL.17
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1971 | Table HL70561
   * - ``psl_18``
     - PSL.18
     - Optional[List[str]]
     - optional
     - Item #1972
   * - ``psl_19``
     - PSL.19
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #1973
   * - ``psl_20``
     - PSL.20
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1974 | Table HL70562
   * - ``psl_21``
     - PSL.21
     - str
     - required
     - Item #1975 | Table HL70532
   * - ``psl_22``
     - PSL.22
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1976 | Table HL70879
   * - ``psl_23``
     - PSL.23
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1977
   * - ``psl_24``
     - PSL.24
     - Optional[str]
     - optional
     - Item #1978
   * - ``psl_25``
     - PSL.25
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #1933
   * - ``psl_26``
     - PSL.26
     - Optional[:ref:`DR <hl7-v2_7_1-DR>`]
     - optional
     - Item #1980
   * - ``psl_27``
     - PSL.27
     - Optional[str]
     - optional
     - Item #1981
   * - ``psl_28``
     - PSL.28
     - Optional[str]
     - optional
     - Item #1982
   * - ``psl_29``
     - PSL.29
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1983
   * - ``psl_30``
     - PSL.30
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #1984
   * - ``psl_31``
     - PSL.31
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1985 | Table HL70881
   * - ``psl_32``
     - PSL.32
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1986 | Table HL70882
   * - ``psl_33``
     - PSL.33
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1987 | Table HL70894
   * - ``psl_34``
     - PSL.34
     - Optional[str]
     - optional
     - Item #1988
   * - ``psl_35``
     - PSL.35
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1989
   * - ``psl_36``
     - PSL.36
     - Optional[str]
     - optional
     - Item #1990
   * - ``psl_37``
     - PSL.37
     - Optional[str]
     - optional
     - Item #1991
   * - ``psl_38``
     - PSL.38
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1992
   * - ``psl_39``
     - PSL.39
     - Optional[str]
     - optional
     - Item #1993
   * - ``psl_40``
     - PSL.40
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1994
   * - ``psl_41``
     - PSL.41
     - Optional[str]
     - optional
     - Item #1995
   * - ``psl_42``
     - PSL.42
     - Optional[str]
     - optional
     - Item #1996
   * - ``psl_43``
     - PSL.43
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1997
   * - ``psl_44``
     - PSL.44
     - Optional[:ref:`CP <hl7-v2_7_1-CP>`]
     - optional
     - Item #1998
   * - ``psl_45``
     - PSL.45
     - Optional[str]
     - optional
     - Item #1999
   * - ``psl_46``
     - PSL.46
     - Optional[str]
     - optional
     - Item #2000
   * - ``psl_47``
     - PSL.47
     - Optional[str]
     - optional
     - Item #2001 | Table HL70136
   * - ``psl_48``
     - PSL.48
     - Optional[str]
     - optional
     - Item #2002

.. _hl7-v2_7_1-PSS:

PSS Product/Service Section (S16.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PSS.PSS
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1946
   * - ``pss_2``
     - PSS.2
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1947
   * - ``pss_3``
     - PSS.3
     - str
     - required
     - Item #1948
   * - ``pss_4``
     - PSS.4
     - :ref:`CP <hl7-v2_7_1-CP>`
     - required
     - Item #1949
   * - ``pss_5``
     - PSS.5
     - str
     - required
     - Item #2043

.. _hl7-v2_7_1-PTH:

PTH Pathway (S12.4.3).
~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PTH.PTH
   :noindex:

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
     - Item #816 | Table HL70287
   * - ``pth_2``
     - PTH.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1207
   * - ``pth_3``
     - PTH.3
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1208
   * - ``pth_4``
     - PTH.4
     - str
     - required
     - Item #1209
   * - ``pth_5``
     - PTH.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1210
   * - ``pth_6``
     - PTH.6
     - Optional[str]
     - optional
     - Item #1211
   * - ``pth_7``
     - PTH.7
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2239 | Table HL70725

.. _hl7-v2_7_1-PV1:

PV1 Patient Visit (S3.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PV1.PV1
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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #132 | Table HL70004
   * - ``pv1_3``
     - PV1.3
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #133
   * - ``pv1_4``
     - PV1.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #134 | Table HL70007
   * - ``pv1_5``
     - PV1.5
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #135
   * - ``pv1_6``
     - PV1.6
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #136
   * - ``pv1_7``
     - PV1.7
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #137 | Table HL70010
   * - ``pv1_8``
     - PV1.8
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #138 | Table HL70010
   * - ``pv1_9``
     - PV1.9
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #139
   * - ``pv1_10``
     - PV1.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #140 | Table HL70069
   * - ``pv1_11``
     - PV1.11
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #141
   * - ``pv1_12``
     - PV1.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #142 | Table HL70087
   * - ``pv1_13``
     - PV1.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #143 | Table HL70092
   * - ``pv1_14``
     - PV1.14
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #144 | Table HL70023
   * - ``pv1_15``
     - PV1.15
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #145 | Table HL70009
   * - ``pv1_16``
     - PV1.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #146 | Table HL70099
   * - ``pv1_17``
     - PV1.17
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #147 | Table HL70010
   * - ``pv1_18``
     - PV1.18
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #148 | Table HL70018
   * - ``pv1_19``
     - PV1.19
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #149
   * - ``pv1_20``
     - PV1.20
     - Optional[List[:ref:`FC <hl7-v2_7_1-FC>`]]
     - optional
     - Item #150 | Table HL70064
   * - ``pv1_21``
     - PV1.21
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #151 | Table HL70032
   * - ``pv1_22``
     - PV1.22
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #152 | Table HL70045
   * - ``pv1_23``
     - PV1.23
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #153 | Table HL70046
   * - ``pv1_24``
     - PV1.24
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #158 | Table HL70073
   * - ``pv1_29``
     - PV1.29
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #159 | Table HL70110
   * - ``pv1_30``
     - PV1.30
     - Optional[str]
     - optional
     - Item #160
   * - ``pv1_31``
     - PV1.31
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #164 | Table HL70111
   * - ``pv1_35``
     - PV1.35
     - Optional[str]
     - optional
     - Item #165
   * - ``pv1_36``
     - PV1.36
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #166 | Table HL70112
   * - ``pv1_37``
     - PV1.37
     - Optional[:ref:`DLD <hl7-v2_7_1-DLD>`]
     - optional
     - Item #167 | Table HL70113
   * - ``pv1_38``
     - PV1.38
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #168 | Table HL70114
   * - ``pv1_39``
     - PV1.39
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #169 | Table HL70115
   * - ``pv1_41``
     - PV1.41
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #171 | Table HL70117
   * - ``pv1_42``
     - PV1.42
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #172
   * - ``pv1_43``
     - PV1.43
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #173
   * - ``pv1_44``
     - PV1.44
     - Optional[str]
     - optional
     - Item #174
   * - ``pv1_45``
     - PV1.45
     - Optional[str]
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
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #180 | Table HL70203
   * - ``pv1_51``
     - PV1.51
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1226 | Table HL70326
   * - ``pv1_53``
     - PV1.53
     - Optional[str]
     - optional
     - Item #2290
   * - ``pv1_54``
     - PV1.54
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #2291

.. _hl7-v2_7_1-PV2:

PV2 Patient Visit - Additional Information (S3.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PV2.PV2
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
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #181
   * - ``pv2_2``
     - PV2.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #182 | Table HL70129
   * - ``pv2_3``
     - PV2.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #183
   * - ``pv2_4``
     - PV2.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
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
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
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
   * - ``pv2_10``
     - PV2.10
     - Optional[str]
     - optional
     - Item #711
   * - ``pv2_11``
     - PV2.11
     - Optional[str]
     - optional
     - Item #712
   * - ``pv2_12``
     - PV2.12
     - Optional[str]
     - optional
     - Item #713
   * - ``pv2_13``
     - PV2.13
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #714
   * - ``pv2_14``
     - PV2.14
     - Optional[str]
     - optional
     - Item #715
   * - ``pv2_15``
     - PV2.15
     - Optional[str]
     - optional
     - Item #716 | Table HL70136
   * - ``pv2_16``
     - PV2.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #717 | Table HL70213
   * - ``pv2_17``
     - PV2.17
     - Optional[str]
     - optional
     - Item #718
   * - ``pv2_18``
     - PV2.18
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #719 | Table HL70214
   * - ``pv2_19``
     - PV2.19
     - Optional[str]
     - optional
     - Item #720 | Table HL70136
   * - ``pv2_20``
     - PV2.20
     - Optional[str]
     - optional
     - Item #721
   * - ``pv2_21``
     - PV2.21
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #722 | Table HL70215
   * - ``pv2_22``
     - PV2.22
     - Optional[str]
     - optional
     - Item #723 | Table HL70136
   * - ``pv2_23``
     - PV2.23
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #724
   * - ``pv2_24``
     - PV2.24
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #725 | Table HL70216
   * - ``pv2_25``
     - PV2.25
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #726 | Table HL70217
   * - ``pv2_26``
     - PV2.26
     - Optional[str]
     - optional
     - Item #727
   * - ``pv2_27``
     - PV2.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #728 | Table HL70112
   * - ``pv2_28``
     - PV2.28
     - Optional[str]
     - optional
     - Item #729
   * - ``pv2_29``
     - PV2.29
     - Optional[str]
     - optional
     - Item #730
   * - ``pv2_30``
     - PV2.30
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #731 | Table HL70218
   * - ``pv2_31``
     - PV2.31
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #732 | Table HL70219
   * - ``pv2_32``
     - PV2.32
     - Optional[str]
     - optional
     - Item #733 | Table HL70136
   * - ``pv2_33``
     - PV2.33
     - Optional[str]
     - optional
     - Item #734
   * - ``pv2_34``
     - PV2.34
     - Optional[str]
     - optional
     - Item #735 | Table HL70136
   * - ``pv2_35``
     - PV2.35
     - Optional[str]
     - optional
     - Item #736 | Table HL70136
   * - ``pv2_36``
     - PV2.36
     - Optional[str]
     - optional
     - Item #737 | Table HL70136
   * - ``pv2_37``
     - PV2.37
     - Optional[str]
     - optional
     - Item #738 | Table HL70136
   * - ``pv2_38``
     - PV2.38
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1543 | Table HL70430
   * - ``pv2_39``
     - PV2.39
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1544 | Table HL70431
   * - ``pv2_40``
     - PV2.40
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1545 | Table HL70432
   * - ``pv2_41``
     - PV2.41
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1546 | Table HL70433
   * - ``pv2_42``
     - PV2.42
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1547 | Table HL70434
   * - ``pv2_43``
     - PV2.43
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #759 | Table HL70315
   * - ``pv2_44``
     - PV2.44
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #760 | Table HL70316
   * - ``pv2_45``
     - PV2.45
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1548 | Table HL70435
   * - ``pv2_46``
     - PV2.46
     - Optional[str]
     - optional
     - Item #1549
   * - ``pv2_47``
     - PV2.47
     - Optional[str]
     - optional
     - Item #1550
   * - ``pv2_48``
     - PV2.48
     - Optional[str]
     - optional
     - Item #1841
   * - ``pv2_49``
     - PV2.49
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1842 | Table HL70534
   * - ``pv2_50``
     - PV2.50
     - Optional[str]
     - optional
     - Item #2141

.. _hl7-v2_7_1-PYE:

PYE Payee Information (S16.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.PYE.PYE
   :noindex:

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
     - Item #1939
   * - ``pye_2``
     - PYE.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1940 | Table HL70557
   * - ``pye_3``
     - PYE.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1941 | Table HL70558
   * - ``pye_4``
     - PYE.4
     - Optional[List[:ref:`XON <hl7-v2_7_1-XON>`]]
     - optional
     - Item #1942
   * - ``pye_5``
     - PYE.5
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #1943
   * - ``pye_6``
     - PYE.6
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #1944
   * - ``pye_7``
     - PYE.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1945 | Table HL70570

.. _hl7-v2_7_1-QAK:

QAK Query Acknowledgment (S5.5.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.QAK.QAK
   :noindex:

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
     - Item #696
   * - ``qak_2``
     - QAK.2
     - Optional[str]
     - optional
     - Item #708 | Table HL70208
   * - ``qak_3``
     - QAK.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1375 | Table HL70471
   * - ``qak_4``
     - QAK.4
     - Optional[str]
     - optional
     - Item #1434
   * - ``qak_5``
     - QAK.5
     - Optional[str]
     - optional
     - Item #1622
   * - ``qak_6``
     - QAK.6
     - Optional[str]
     - optional
     - Item #1623

.. _hl7-v2_7_1-QID:

QID Query Identification (S5.5.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.QID.QID
   :noindex:

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
     - Item #696
   * - ``qid_2``
     - QID.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1375 | Table HL70471

.. _hl7-v2_7_1-QPD:

QPD Query Parameter Definition (S5.5.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.QPD.QPD
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1375 | Table HL70471
   * - ``qpd_2``
     - QPD.2
     - Optional[str]
     - optional
     - Item #696
   * - ``qpd_3``
     - QPD.3
     - Optional[varies]
     - optional
     - Item #1435

.. _hl7-v2_7_1-QRI:

QRI Query Response Instance (S5.5.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.QRI.QRI
   :noindex:

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
     - Item #1436
   * - ``qri_2``
     - QRI.2
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1437 | Table HL70392
   * - ``qri_3``
     - QRI.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1438 | Table HL70393

.. _hl7-v2_7_1-RCP:

RCP Response Control Parameter (S5.5.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RCP.RCP
   :noindex:

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
     - Item #27 | Table HL70091
   * - ``rcp_2``
     - RCP.2
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #31 | Table HL70126
   * - ``rcp_3``
     - RCP.3
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #1440 | Table HL70394
   * - ``rcp_4``
     - RCP.4
     - Optional[str]
     - optional
     - Item #1441
   * - ``rcp_5``
     - RCP.5
     - Optional[str]
     - optional
     - Item #1443 | Table HL70395
   * - ``rcp_6``
     - RCP.6
     - Optional[List[:ref:`SRT <hl7-v2_7_1-SRT>`]]
     - optional
     - Item #1624
   * - ``rcp_7``
     - RCP.7
     - Optional[List[str]]
     - optional
     - Item #1594 | Table HL70391

.. _hl7-v2_7_1-RDF:

RDF Table Row Definition (S5.5.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RDF.RDF
   :noindex:

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
     - Item #701
   * - ``rdf_2``
     - RDF.2
     - List[:ref:`RCD <hl7-v2_7_1-RCD>`]
     - required
     - Item #702 | Table HL70440

.. _hl7-v2_7_1-RDT:

RDT Table Row Data (S5.5.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RDT.RDT
   :noindex:

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
     - Item #703

.. _hl7-v2_7_1-REL:

REL Clinical Relationship Segment (S12.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.REL.REL
   :noindex:

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
     - Item #2240
   * - ``rel_2``
     - REL.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #2241
   * - ``rel_3``
     - REL.3
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2242
   * - ``rel_4``
     - REL.4
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2243
   * - ``rel_5``
     - REL.5
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2244
   * - ``rel_6``
     - REL.6
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2245
   * - ``rel_7``
     - REL.7
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #2246
   * - ``rel_8``
     - REL.8
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #2247
   * - ``rel_9``
     - REL.9
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #2248
   * - ``rel_10``
     - REL.10
     - Optional[:ref:`XTN <hl7-v2_7_1-XTN>`]
     - optional
     - Item #2249
   * - ``rel_11``
     - REL.11
     - Optional[:ref:`DR <hl7-v2_7_1-DR>`]
     - optional
     - Item #2250
   * - ``rel_12``
     - REL.12
     - Optional[str]
     - optional
     - Item #2251 | Table HL70136
   * - ``rel_13``
     - REL.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2252
   * - ``rel_14``
     - REL.14
     - Optional[str]
     - optional
     - Item #2253
   * - ``rel_15``
     - REL.15
     - Optional[str]
     - optional
     - Item #2254
   * - ``rel_16``
     - REL.16
     - Optional[str]
     - optional
     - Item #2255 | Table HL70136

.. _hl7-v2_7_1-RF1:

RF1 Referral Information (S11.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RF1.RF1
   :noindex:

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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1137 | Table HL70283
   * - ``rf1_2``
     - RF1.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1138 | Table HL70280
   * - ``rf1_3``
     - RF1.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1139 | Table HL70281
   * - ``rf1_4``
     - RF1.4
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1140 | Table HL70282
   * - ``rf1_5``
     - RF1.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1141 | Table HL70284
   * - ``rf1_6``
     - RF1.6
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1142
   * - ``rf1_7``
     - RF1.7
     - Optional[str]
     - optional
     - Item #1143
   * - ``rf1_8``
     - RF1.8
     - Optional[str]
     - optional
     - Item #1144
   * - ``rf1_9``
     - RF1.9
     - Optional[str]
     - optional
     - Item #1145
   * - ``rf1_10``
     - RF1.10
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1228 | Table HL70336
   * - ``rf1_11``
     - RF1.11
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #1300
   * - ``rf1_12``
     - RF1.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2262 | Table HL70865

.. _hl7-v2_7_1-RFI:

RFI Request for Information (S16.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RFI.RFI
   :noindex:

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
     - Item #1910
   * - ``rfi_2``
     - RFI.2
     - str
     - required
     - Item #1911
   * - ``rfi_3``
     - RFI.3
     - Optional[str]
     - optional
     - Item #1912 | Table HL70136
   * - ``rfi_4``
     - RFI.4
     - Optional[str]
     - optional
     - Item #1913

.. _hl7-v2_7_1-RGS:

RGS Resource Group (S10.6.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RGS.RGS
   :noindex:

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
     - Item #1203
   * - ``rgs_2``
     - RGS.2
     - Optional[str]
     - optional
     - Item #763 | Table HL70206
   * - ``rgs_3``
     - RGS.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1204

.. _hl7-v2_7_1-RMI:

RMI Risk Management Incident (S6.5.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RMI.RMI
   :noindex:

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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1530 | Table HL70427
   * - ``rmi_2``
     - RMI.2
     - Optional[str]
     - optional
     - Item #1531
   * - ``rmi_3``
     - RMI.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1533 | Table HL70428

.. _hl7-v2_7_1-ROL:

ROL Role (S15.4.7).
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.ROL.ROL
   :noindex:

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
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1206
   * - ``rol_2``
     - ROL.2
     - str
     - required
     - Item #816 | Table HL70287
   * - ``rol_3``
     - ROL.3
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1197 | Table HL70443
   * - ``rol_4``
     - ROL.4
     - List[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - required
     - Item #1198
   * - ``rol_5``
     - ROL.5
     - Optional[str]
     - optional
     - Item #1199
   * - ``rol_6``
     - ROL.6
     - Optional[str]
     - optional
     - Item #1200
   * - ``rol_7``
     - ROL.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1201
   * - ``rol_8``
     - ROL.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1205
   * - ``rol_9``
     - ROL.9
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1510
   * - ``rol_10``
     - ROL.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1461 | Table HL70406
   * - ``rol_11``
     - ROL.11
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #679
   * - ``rol_12``
     - ROL.12
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #678
   * - ``rol_13``
     - ROL.13
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #2183
   * - ``rol_14``
     - ROL.14
     - Optional[:ref:`XON <hl7-v2_7_1-XON>`]
     - optional
     - Item #2377

.. _hl7-v2_7_1-RQ1:

RQ1 Requisition Detail-1 (S4.10.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RQ1.RQ1
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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #286 | Table HL70385
   * - ``rq1_3``
     - RQ1.3
     - Optional[str]
     - optional
     - Item #287
   * - ``rq1_4``
     - RQ1.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #288 | Table HL79999
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

.. _hl7-v2_7_1-RQD:

RQD Requisition Detail (S4.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RQD.RQD
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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #276 | Table HL79999
   * - ``rqd_3``
     - RQD.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #277 | Table HL79999
   * - ``rqd_4``
     - RQD.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #278 | Table HL79999
   * - ``rqd_5``
     - RQD.5
     - Optional[str]
     - optional
     - Item #279
   * - ``rqd_6``
     - RQD.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #280 | Table HL79999
   * - ``rqd_7``
     - RQD.7
     - Optional[:ref:`CX <hl7-v2_7_1-CX>`]
     - optional
     - Item #281 | Table HL70319
   * - ``rqd_8``
     - RQD.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #282 | Table HL70320
   * - ``rqd_9``
     - RQD.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #283 | Table HL79999
   * - ``rqd_10``
     - RQD.10
     - Optional[str]
     - optional
     - Item #284

.. _hl7-v2_7_1-RXA:

RXA Pharmacy/Treatment Administration (S4.A.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RXA.RXA
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
     - str
     - required
     - Item #345
   * - ``rxa_4``
     - RXA.4
     - str
     - required
     - Item #346
   * - ``rxa_5``
     - RXA.5
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #347 | Table HL70292
   * - ``rxa_6``
     - RXA.6
     - str
     - required
     - Item #348
   * - ``rxa_7``
     - RXA.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #349 | Table HL79999
   * - ``rxa_8``
     - RXA.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #350 | Table HL79999
   * - ``rxa_9``
     - RXA.9
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #351 | Table HL79999
   * - ``rxa_10``
     - RXA.10
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #352
   * - ``rxa_11``
     - RXA.11
     - Optional[:ref:`LA2 <hl7-v2_7_1-LA2>`]
     - optional
     - Item #353
   * - ``rxa_12``
     - RXA.12
     - Optional[str]
     - optional
     - Item #354
   * - ``rxa_13``
     - RXA.13
     - Optional[str]
     - optional
     - Item #1134
   * - ``rxa_14``
     - RXA.14
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1135 | Table HL79999
   * - ``rxa_15``
     - RXA.15
     - Optional[List[str]]
     - optional
     - Item #1129
   * - ``rxa_16``
     - RXA.16
     - Optional[List[str]]
     - optional
     - Item #1130
   * - ``rxa_17``
     - RXA.17
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1131 | Table HL70227
   * - ``rxa_18``
     - RXA.18
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1136 | Table HL79999
   * - ``rxa_19``
     - RXA.19
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1123 | Table HL79999
   * - ``rxa_20``
     - RXA.20
     - Optional[str]
     - optional
     - Item #1223 | Table HL70322
   * - ``rxa_21``
     - RXA.21
     - Optional[str]
     - optional
     - Item #1224 | Table HL70206
   * - ``rxa_22``
     - RXA.22
     - Optional[str]
     - optional
     - Item #1225
   * - ``rxa_23``
     - RXA.23
     - Optional[str]
     - optional
     - Item #1696
   * - ``rxa_24``
     - RXA.24
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1697 | Table HL79999
   * - ``rxa_25``
     - RXA.25
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1698 | Table HL79999
   * - ``rxa_26``
     - RXA.26
     - Optional[str]
     - optional
     - Item #1699 | Table HL70480
   * - ``rxa_27``
     - RXA.27
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #2264
   * - ``rxa_28``
     - RXA.28
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #2265

.. _hl7-v2_7_1-RXC:

RXC Pharmacy/Treatment Component Order (S4.A.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RXC.RXC
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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #314 | Table HL79999
   * - ``rxc_3``
     - RXC.3
     - str
     - required
     - Item #315
   * - ``rxc_4``
     - RXC.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #316 | Table HL79999
   * - ``rxc_5``
     - RXC.5
     - Optional[str]
     - optional
     - Item #1124
   * - ``rxc_6``
     - RXC.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1125 | Table HL79999
   * - ``rxc_7``
     - RXC.7
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1476 | Table HL79999
   * - ``rxc_8``
     - RXC.8
     - Optional[str]
     - optional
     - Item #1671
   * - ``rxc_9``
     - RXC.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1672 | Table HL79999

.. _hl7-v2_7_1-RXD:

RXD Pharmacy/Treatment Dispense (S4.A.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RXD.RXD
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
     - str
     - required
     - Item #334
   * - ``rxd_2``
     - RXD.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #335 | Table HL70292
   * - ``rxd_3``
     - RXD.3
     - str
     - required
     - Item #336
   * - ``rxd_4``
     - RXD.4
     - str
     - required
     - Item #337
   * - ``rxd_5``
     - RXD.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #338 | Table HL79999
   * - ``rxd_6``
     - RXD.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #339 | Table HL79999
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
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #341
   * - ``rxd_11``
     - RXD.11
     - Optional[str]
     - optional
     - Item #322 | Table HL70167
   * - ``rxd_12``
     - RXD.12
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #329
   * - ``rxd_13``
     - RXD.13
     - Optional[:ref:`LA2 <hl7-v2_7_1-LA2>`]
     - optional
     - Item #1303
   * - ``rxd_14``
     - RXD.14
     - Optional[str]
     - optional
     - Item #307 | Table HL70136
   * - ``rxd_15``
     - RXD.15
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #330 | Table HL79999
   * - ``rxd_16``
     - RXD.16
     - Optional[str]
     - optional
     - Item #1132
   * - ``rxd_17``
     - RXD.17
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1133 | Table HL79999
   * - ``rxd_18``
     - RXD.18
     - Optional[List[str]]
     - optional
     - Item #1129
   * - ``rxd_19``
     - RXD.19
     - Optional[List[str]]
     - optional
     - Item #1130
   * - ``rxd_20``
     - RXD.20
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1131 | Table HL70227
   * - ``rxd_21``
     - RXD.21
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1123 | Table HL79999
   * - ``rxd_22``
     - RXD.22
     - Optional[str]
     - optional
     - Item #1220
   * - ``rxd_23``
     - RXD.23
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1221 | Table HL79999
   * - ``rxd_24``
     - RXD.24
     - Optional[str]
     - optional
     - Item #1222 | Table HL70321
   * - ``rxd_25``
     - RXD.25
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1476 | Table HL79999
   * - ``rxd_26``
     - RXD.26
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1477 | Table HL79999
   * - ``rxd_27``
     - RXD.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1478 | Table HL79999
   * - ``rxd_28``
     - RXD.28
     - Optional[str]
     - optional
     - Item #1686
   * - ``rxd_29``
     - RXD.29
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1687 | Table HL79999
   * - ``rxd_30``
     - RXD.30
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1688 | Table HL79999
   * - ``rxd_31``
     - RXD.31
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1689
   * - ``rxd_32``
     - RXD.32
     - Optional[str]
     - optional
     - Item #1690 | Table HL70480
   * - ``rxd_33``
     - RXD.33
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1691 | Table HL70484
   * - ``rxd_34``
     - RXD.34
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #2311

.. _hl7-v2_7_1-RXE:

RXE Pharmacy/Treatment Encoded Order (S4.A.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RXE.RXE
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #317 | Table HL70292
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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #320 | Table HL79999
   * - ``rxe_6``
     - RXE.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #321 | Table HL79999
   * - ``rxe_7``
     - RXE.7
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #298 | Table HL79999
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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #324 | Table HL79999
   * - ``rxe_12``
     - RXE.12
     - Optional[str]
     - optional
     - Item #304
   * - ``rxe_13``
     - RXE.13
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #305
   * - ``rxe_14``
     - RXE.14
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #306
   * - ``rxe_15``
     - RXE.15
     - Optional[str]
     - optional
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
     - Optional[str]
     - optional
     - Item #328
   * - ``rxe_19``
     - RXE.19
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #329
   * - ``rxe_20``
     - RXE.20
     - Optional[str]
     - optional
     - Item #307 | Table HL70136
   * - ``rxe_21``
     - RXE.21
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #330 | Table HL79999
   * - ``rxe_22``
     - RXE.22
     - Optional[str]
     - optional
     - Item #331
   * - ``rxe_23``
     - RXE.23
     - Optional[str]
     - optional
     - Item #332
   * - ``rxe_24``
     - RXE.24
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #333 | Table HL79999
   * - ``rxe_25``
     - RXE.25
     - Optional[str]
     - optional
     - Item #1126
   * - ``rxe_26``
     - RXE.26
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1127 | Table HL79999
   * - ``rxe_27``
     - RXE.27
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1128 | Table HL79999
   * - ``rxe_28``
     - RXE.28
     - Optional[str]
     - optional
     - Item #1220
   * - ``rxe_29``
     - RXE.29
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1221 | Table HL79999
   * - ``rxe_30``
     - RXE.30
     - Optional[str]
     - optional
     - Item #1222 | Table HL70321
   * - ``rxe_31``
     - RXE.31
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1476 | Table HL79999
   * - ``rxe_32``
     - RXE.32
     - Optional[str]
     - optional
     - Item #1673
   * - ``rxe_33``
     - RXE.33
     - Optional[str]
     - optional
     - Item #1674
   * - ``rxe_34``
     - RXE.34
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1675 | Table HL79999
   * - ``rxe_35``
     - RXE.35
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1676 | Table HL70477
   * - ``rxe_36``
     - RXE.36
     - Optional[str]
     - optional
     - Item #1677 | Table HL70478
   * - ``rxe_37``
     - RXE.37
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1678 | Table HL79999
   * - ``rxe_38``
     - RXE.38
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1679 | Table HL79999
   * - ``rxe_39``
     - RXE.39
     - Optional[str]
     - optional
     - Item #1680
   * - ``rxe_40``
     - RXE.40
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1681 | Table HL79999
   * - ``rxe_41``
     - RXE.41
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1682
   * - ``rxe_42``
     - RXE.42
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #1683
   * - ``rxe_43``
     - RXE.43
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1684
   * - ``rxe_44``
     - RXE.44
     - Optional[str]
     - optional
     - Item #1685 | Table HL70480
   * - ``rxe_45``
     - RXE.45
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #2310

.. _hl7-v2_7_1-RXG:

RXG Pharmacy/Treatment Give (S4.A.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RXG.RXG
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
   * - ``rxg_4``
     - RXG.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #317 | Table HL70292
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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #320 | Table HL79999
   * - ``rxg_8``
     - RXG.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #321 | Table HL79999
   * - ``rxg_9``
     - RXG.9
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #351 | Table HL79999
   * - ``rxg_10``
     - RXG.10
     - Optional[str]
     - optional
     - Item #322 | Table HL70167
   * - ``rxg_11``
     - RXG.11
     - Optional[:ref:`LA2 <hl7-v2_7_1-LA2>`]
     - optional
     - Item #1303
   * - ``rxg_12``
     - RXG.12
     - Optional[str]
     - optional
     - Item #307 | Table HL70136
   * - ``rxg_13``
     - RXG.13
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #343 | Table HL79999
   * - ``rxg_14``
     - RXG.14
     - Optional[str]
     - optional
     - Item #331
   * - ``rxg_15``
     - RXG.15
     - Optional[str]
     - optional
     - Item #332
   * - ``rxg_16``
     - RXG.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #333 | Table HL79999
   * - ``rxg_17``
     - RXG.17
     - Optional[str]
     - optional
     - Item #1126
   * - ``rxg_18``
     - RXG.18
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1127 | Table HL79999
   * - ``rxg_19``
     - RXG.19
     - Optional[List[str]]
     - optional
     - Item #1129
   * - ``rxg_20``
     - RXG.20
     - Optional[List[str]]
     - optional
     - Item #1130
   * - ``rxg_21``
     - RXG.21
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1131 | Table HL70227
   * - ``rxg_22``
     - RXG.22
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1123 | Table HL79999
   * - ``rxg_23``
     - RXG.23
     - Optional[str]
     - optional
     - Item #1692
   * - ``rxg_24``
     - RXG.24
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1693 | Table HL79999
   * - ``rxg_25``
     - RXG.25
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1694 | Table HL79999
   * - ``rxg_26``
     - RXG.26
     - Optional[str]
     - optional
     - Item #1695 | Table HL70480
   * - ``rxg_27``
     - RXG.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1688 | Table HL79999
   * - ``rxg_28``
     - RXG.28
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1689
   * - ``rxg_29``
     - RXG.29
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #1683
   * - ``rxg_30``
     - RXG.30
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1684

.. _hl7-v2_7_1-RXO:

RXO Pharmacy/Treatment Order (S4.A.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RXO.RXO
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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #292 | Table HL79999
   * - ``rxo_2``
     - RXO.2
     - Optional[str]
     - optional
     - Item #293
   * - ``rxo_3``
     - RXO.3
     - Optional[str]
     - optional
     - Item #294
   * - ``rxo_4``
     - RXO.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #295 | Table HL79999
   * - ``rxo_5``
     - RXO.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #296 | Table HL79999
   * - ``rxo_6``
     - RXO.6
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #297 | Table HL79999
   * - ``rxo_7``
     - RXO.7
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #298 | Table HL79999
   * - ``rxo_8``
     - RXO.8
     - Optional[:ref:`LA1 <hl7-v2_7_1-LA1>`]
     - optional
     - Item #299
   * - ``rxo_9``
     - RXO.9
     - Optional[str]
     - optional
     - Item #300 | Table HL70161
   * - ``rxo_10``
     - RXO.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #301 | Table HL79999
   * - ``rxo_11``
     - RXO.11
     - Optional[str]
     - optional
     - Item #302
   * - ``rxo_12``
     - RXO.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #303 | Table HL79999
   * - ``rxo_13``
     - RXO.13
     - Optional[str]
     - optional
     - Item #304
   * - ``rxo_14``
     - RXO.14
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #305
   * - ``rxo_15``
     - RXO.15
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #306
   * - ``rxo_16``
     - RXO.16
     - Optional[str]
     - optional
     - Item #307 | Table HL70136
   * - ``rxo_17``
     - RXO.17
     - Optional[str]
     - optional
     - Item #308
   * - ``rxo_18``
     - RXO.18
     - Optional[str]
     - optional
     - Item #1121
   * - ``rxo_19``
     - RXO.19
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1122 | Table HL79999
   * - ``rxo_20``
     - RXO.20
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1123 | Table HL79999
   * - ``rxo_21``
     - RXO.21
     - Optional[str]
     - optional
     - Item #1218
   * - ``rxo_22``
     - RXO.22
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1219 | Table HL79999
   * - ``rxo_23``
     - RXO.23
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #329
   * - ``rxo_24``
     - RXO.24
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1476 | Table HL79999
   * - ``rxo_25``
     - RXO.25
     - Optional[str]
     - optional
     - Item #1666
   * - ``rxo_26``
     - RXO.26
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1667 | Table HL79999
   * - ``rxo_27``
     - RXO.27
     - Optional[str]
     - optional
     - Item #1668 | Table HL70480
   * - ``rxo_28``
     - RXO.28
     - Optional[str]
     - optional
     - Item #1669
   * - ``rxo_29``
     - RXO.29
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2149
   * - ``rxo_30``
     - RXO.30
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2150
   * - ``rxo_31``
     - RXO.31
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2151 | Table HL70725
   * - ``rxo_32``
     - RXO.32
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1681 | Table HL79999
   * - ``rxo_33``
     - RXO.33
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1682
   * - ``rxo_34``
     - RXO.34
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #1683
   * - ``rxo_35``
     - RXO.35
     - Optional[:ref:`XAD <hl7-v2_7_1-XAD>`]
     - optional
     - Item #1684
   * - ``rxo_36``
     - RXO.36
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #2309

.. _hl7-v2_7_1-RXR:

RXR Pharmacy/Treatment Route (S4.A.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.RXR.RXR
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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #309 | Table HL70162
   * - ``rxr_2``
     - RXR.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #310 | Table HL70550
   * - ``rxr_3``
     - RXR.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #311 | Table HL70164
   * - ``rxr_4``
     - RXR.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #312 | Table HL70165
   * - ``rxr_5``
     - RXR.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1315 | Table HL79999
   * - ``rxr_6``
     - RXR.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1670 | Table HL70495

.. _hl7-v2_7_1-SAC:

SAC Specimen Container detail (S13.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.SAC.SAC
   :noindex:

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
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1329
   * - ``sac_2``
     - SAC.2
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1330
   * - ``sac_3``
     - SAC.3
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1331
   * - ``sac_4``
     - SAC.4
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1332
   * - ``sac_5``
     - SAC.5
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1333
   * - ``sac_7``
     - SAC.7
     - Optional[str]
     - optional
     - Item #1334
   * - ``sac_8``
     - SAC.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1335 | Table HL70370
   * - ``sac_9``
     - SAC.9
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1336 | Table HL70378
   * - ``sac_10``
     - SAC.10
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1337
   * - ``sac_11``
     - SAC.11
     - Optional[:ref:`NA <hl7-v2_7_1-NA>`]
     - optional
     - Item #1338
   * - ``sac_12``
     - SAC.12
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1339 | Table HL70379
   * - ``sac_13``
     - SAC.13
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #1340
   * - ``sac_14``
     - SAC.14
     - Optional[:ref:`NA <hl7-v2_7_1-NA>`]
     - optional
     - Item #1341
   * - ``sac_15``
     - SAC.15
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1342 | Table HL79999
   * - ``sac_16``
     - SAC.16
     - Optional[str]
     - optional
     - Item #1343
   * - ``sac_17``
     - SAC.17
     - Optional[str]
     - optional
     - Item #1344
   * - ``sac_18``
     - SAC.18
     - Optional[str]
     - optional
     - Item #1345
   * - ``sac_19``
     - SAC.19
     - Optional[str]
     - optional
     - Item #1346
   * - ``sac_20``
     - SAC.20
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1347 | Table HL79999
   * - ``sac_21``
     - SAC.21
     - Optional[str]
     - optional
     - Item #644
   * - ``sac_22``
     - SAC.22
     - Optional[str]
     - optional
     - Item #1349
   * - ``sac_23``
     - SAC.23
     - Optional[str]
     - optional
     - Item #1350
   * - ``sac_24``
     - SAC.24
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1351 | Table HL79999
   * - ``sac_25``
     - SAC.25
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1352 | Table HL70380
   * - ``sac_26``
     - SAC.26
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1353 | Table HL70381
   * - ``sac_27``
     - SAC.27
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #647 | Table HL70371
   * - ``sac_28``
     - SAC.28
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1355 | Table HL70372
   * - ``sac_29``
     - SAC.29
     - Optional[:ref:`SN <hl7-v2_7_1-SN>`]
     - optional
     - Item #1356
   * - ``sac_30``
     - SAC.30
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1357 | Table HL70373
   * - ``sac_31``
     - SAC.31
     - Optional[:ref:`SN <hl7-v2_7_1-SN>`]
     - optional
     - Item #1358
   * - ``sac_32``
     - SAC.32
     - Optional[str]
     - optional
     - Item #1359
   * - ``sac_33``
     - SAC.33
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1360 | Table HL79999
   * - ``sac_34``
     - SAC.34
     - Optional[str]
     - optional
     - Item #1361
   * - ``sac_35``
     - SAC.35
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1362 | Table HL79999
   * - ``sac_36``
     - SAC.36
     - Optional[str]
     - optional
     - Item #1363
   * - ``sac_37``
     - SAC.37
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1364 | Table HL79999
   * - ``sac_38``
     - SAC.38
     - Optional[str]
     - optional
     - Item #1365
   * - ``sac_39``
     - SAC.39
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1366 | Table HL79999
   * - ``sac_40``
     - SAC.40
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1367 | Table HL70374
   * - ``sac_41``
     - SAC.41
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1368 | Table HL70382
   * - ``sac_42``
     - SAC.42
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1369 | Table HL70375
   * - ``sac_43``
     - SAC.43
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1370 | Table HL70376
   * - ``sac_44``
     - SAC.44
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1371 | Table HL70377

.. _hl7-v2_7_1-SCD:

SCD Anti-Microbial Cycle Data (S17.7.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.SCD.SCD
   :noindex:

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
     - Item #2104
   * - ``scd_2``
     - SCD.2
     - Optional[str]
     - optional
     - Item #2105
   * - ``scd_3``
     - SCD.3
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2106
   * - ``scd_4``
     - SCD.4
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2107
   * - ``scd_5``
     - SCD.5
     - Optional[str]
     - optional
     - Item #2108
   * - ``scd_6``
     - SCD.6
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2109
   * - ``scd_7``
     - SCD.7
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2110
   * - ``scd_8``
     - SCD.8
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2111
   * - ``scd_9``
     - SCD.9
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2112
   * - ``scd_10``
     - SCD.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2113 | Table HL70682
   * - ``scd_11``
     - SCD.11
     - Optional[str]
     - optional
     - Item #2114
   * - ``scd_12``
     - SCD.12
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2115
   * - ``scd_13``
     - SCD.13
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2116
   * - ``scd_14``
     - SCD.14
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2117
   * - ``scd_15``
     - SCD.15
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2118
   * - ``scd_16``
     - SCD.16
     - Optional[str]
     - optional
     - Item #2119
   * - ``scd_17``
     - SCD.17
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2120
   * - ``scd_18``
     - SCD.18
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2121
   * - ``scd_19``
     - SCD.19
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2122 | Table HL70532
   * - ``scd_20``
     - SCD.20
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2123 | Table HL70532
   * - ``scd_21``
     - SCD.21
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2124 | Table HL70532
   * - ``scd_22``
     - SCD.22
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2125 | Table HL70532
   * - ``scd_23``
     - SCD.23
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2126 | Table HL70532
   * - ``scd_24``
     - SCD.24
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2127 | Table HL70532
   * - ``scd_25``
     - SCD.25
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #2128
   * - ``scd_26``
     - SCD.26
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2129 | Table HL70532
   * - ``scd_27``
     - SCD.27
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2130 | Table HL70532
   * - ``scd_28``
     - SCD.28
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2131 | Table HL70702
   * - ``scd_29``
     - SCD.29
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2132
   * - ``scd_30``
     - SCD.30
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2133
   * - ``scd_31``
     - SCD.31
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2134
   * - ``scd_32``
     - SCD.32
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #393 | Table HL70088
   * - ``scd_33``
     - SCD.33
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #106
   * - ``scd_34``
     - SCD.34
     - Optional[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - optional
     - Item #137 | Table HL70010
   * - ``scd_35``
     - SCD.35
     - Optional[:ref:`SN <hl7-v2_7_1-SN>`]
     - optional
     - Item #1356
   * - ``scd_36``
     - SCD.36
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2139
   * - ``scd_37``
     - SCD.37
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #2140

.. _hl7-v2_7_1-SCH:

SCH Scheduling Activity Information (S10.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.SCH.SCH
   :noindex:

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
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #860
   * - ``sch_2``
     - SCH.2
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #861
   * - ``sch_3``
     - SCH.3
     - Optional[str]
     - optional
     - Item #862
   * - ``sch_4``
     - SCH.4
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #218
   * - ``sch_5``
     - SCH.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #864
   * - ``sch_6``
     - SCH.6
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #883
   * - ``sch_7``
     - SCH.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #866 | Table HL70276
   * - ``sch_8``
     - SCH.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #867 | Table HL70277
   * - ``sch_10``
     - SCH.10
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #869
   * - ``sch_12``
     - SCH.12
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #874
   * - ``sch_13``
     - SCH.13
     - Optional[:ref:`XTN <hl7-v2_7_1-XTN>`]
     - optional
     - Item #875
   * - ``sch_14``
     - SCH.14
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #876
   * - ``sch_15``
     - SCH.15
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #877
   * - ``sch_16``
     - SCH.16
     - List[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - required
     - Item #885
   * - ``sch_17``
     - SCH.17
     - Optional[:ref:`XTN <hl7-v2_7_1-XTN>`]
     - optional
     - Item #886
   * - ``sch_18``
     - SCH.18
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #887
   * - ``sch_19``
     - SCH.19
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #888
   * - ``sch_20``
     - SCH.20
     - List[:ref:`XCN <hl7-v2_7_1-XCN>`]
     - required
     - Item #878
   * - ``sch_21``
     - SCH.21
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #879
   * - ``sch_22``
     - SCH.22
     - Optional[:ref:`PL <hl7-v2_7_1-PL>`]
     - optional
     - Item #880
   * - ``sch_23``
     - SCH.23
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #881
   * - ``sch_24``
     - SCH.24
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #882
   * - ``sch_25``
     - SCH.25
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #889 | Table HL70278
   * - ``sch_26``
     - SCH.26
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #216
   * - ``sch_27``
     - SCH.27
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #217

.. _hl7-v2_7_1-SCP:

SCP Sterilizer Configuration (Anti-Microbial Devices) (S17.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.SCP.SCP
   :noindex:

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
     - Item #2087
   * - ``scp_2``
     - SCP.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2088 | Table HL70651
   * - ``scp_3``
     - SCP.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2089 | Table HL70653
   * - ``scp_4``
     - SCP.4
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2090
   * - ``scp_5``
     - SCP.5
     - Optional[str]
     - optional
     - Item #2279
   * - ``scp_6``
     - SCP.6
     - Optional[str]
     - optional
     - Item #2091
   * - ``scp_7``
     - SCP.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2092 | Table HL70657
   * - ``scp_8``
     - SCP.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2093 | Table HL70659

.. _hl7-v2_7_1-SDD:

SDD Sterilization Device Data (S17.7.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.SDD.SDD
   :noindex:

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
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2098
   * - ``sdd_2``
     - SDD.2
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2099
   * - ``sdd_3``
     - SDD.3
     - Optional[str]
     - optional
     - Item #2281
   * - ``sdd_4``
     - SDD.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2100 | Table HL70667
   * - ``sdd_5``
     - SDD.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2101 | Table HL70669
   * - ``sdd_6``
     - SDD.6
     - Optional[str]
     - optional
     - Item #2102
   * - ``sdd_7``
     - SDD.7
     - Optional[str]
     - optional
     - Item #2103

.. _hl7-v2_7_1-SFT:

SFT Software Segment (S2.14.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.SFT.SFT
   :noindex:

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
     - :ref:`XON <hl7-v2_7_1-XON>`
     - required
     - Item #1834
   * - ``sft_2``
     - SFT.2
     - str
     - required
     - Item #1835
   * - ``sft_3``
     - SFT.3
     - str
     - required
     - Item #1836
   * - ``sft_4``
     - SFT.4
     - str
     - required
     - Item #1837
   * - ``sft_5``
     - SFT.5
     - Optional[str]
     - optional
     - Item #1838
   * - ``sft_6``
     - SFT.6
     - Optional[str]
     - optional
     - Item #1839

.. _hl7-v2_7_1-SHP:

SHP Shipment (S7.18.2).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.SHP.SHP
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2317
   * - ``shp_2``
     - SHP.2
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #2318
   * - ``shp_3``
     - SHP.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2319 | Table HL70905
   * - ``shp_4``
     - SHP.4
     - str
     - required
     - Item #2320
   * - ``shp_5``
     - SHP.5
     - Optional[str]
     - optional
     - Item #2321
   * - ``shp_6``
     - SHP.6
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2322 | Table HL70906
   * - ``shp_7``
     - SHP.7
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2323 | Table HL70907
   * - ``shp_8``
     - SHP.8
     - Optional[str]
     - optional
     - Item #2324
   * - ``shp_9``
     - SHP.9
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2325 | Table HL70544
   * - ``shp_10``
     - SHP.10
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2326 | Table HL70376
   * - ``shp_11``
     - SHP.11
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2327 | Table HL70489

.. _hl7-v2_7_1-SID:

SID Substance Identifier (S13.4.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.SID.SID
   :noindex:

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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1426 | Table HL79999
   * - ``sid_2``
     - SID.2
     - Optional[str]
     - optional
     - Item #1129
   * - ``sid_3``
     - SID.3
     - Optional[str]
     - optional
     - Item #1428
   * - ``sid_4``
     - SID.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1429 | Table HL70385

.. _hl7-v2_7_1-SLT:

SLT Sterilization Lot (S17.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.SLT.SLT
   :noindex:

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
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2094
   * - ``slt_2``
     - SLT.2
     - Optional[str]
     - optional
     - Item #2280
   * - ``slt_3``
     - SLT.3
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2095
   * - ``slt_4``
     - SLT.4
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2096
   * - ``slt_5``
     - SLT.5
     - Optional[str]
     - optional
     - Item #2097

.. _hl7-v2_7_1-SPM:

SPM Specimen (S7.4.3).
~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.SPM.SPM
   :noindex:

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
     - Item #1754
   * - ``spm_2``
     - SPM.2
     - Optional[:ref:`EIP <hl7-v2_7_1-EIP>`]
     - optional
     - Item #1755
   * - ``spm_3``
     - SPM.3
     - Optional[List[:ref:`EIP <hl7-v2_7_1-EIP>`]]
     - optional
     - Item #1756
   * - ``spm_4``
     - SPM.4
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #1900 | Table HL70487
   * - ``spm_5``
     - SPM.5
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1757 | Table HL70541
   * - ``spm_6``
     - SPM.6
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1758 | Table HL70371
   * - ``spm_7``
     - SPM.7
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1759 | Table HL70488
   * - ``spm_8``
     - SPM.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1901 | Table HL79999
   * - ``spm_9``
     - SPM.9
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1760 | Table HL70542
   * - ``spm_10``
     - SPM.10
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1761 | Table HL70543
   * - ``spm_11``
     - SPM.11
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1762 | Table HL70369
   * - ``spm_12``
     - SPM.12
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1902
   * - ``spm_13``
     - SPM.13
     - Optional[str]
     - optional
     - Item #1763
   * - ``spm_14``
     - SPM.14
     - Optional[List[str]]
     - optional
     - Item #1764
   * - ``spm_15``
     - SPM.15
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1908 | Table HL70376
   * - ``spm_16``
     - SPM.16
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1903 | Table HL70489
   * - ``spm_17``
     - SPM.17
     - Optional[:ref:`DR <hl7-v2_7_1-DR>`]
     - optional
     - Item #1765
   * - ``spm_18``
     - SPM.18
     - Optional[str]
     - optional
     - Item #248
   * - ``spm_19``
     - SPM.19
     - Optional[str]
     - optional
     - Item #1904
   * - ``spm_20``
     - SPM.20
     - Optional[str]
     - optional
     - Item #1766 | Table HL70136
   * - ``spm_21``
     - SPM.21
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1767 | Table HL70490
   * - ``spm_22``
     - SPM.22
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1768 | Table HL70491
   * - ``spm_23``
     - SPM.23
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1769 | Table HL70492
   * - ``spm_24``
     - SPM.24
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1770 | Table HL70493
   * - ``spm_25``
     - SPM.25
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1771
   * - ``spm_26``
     - SPM.26
     - Optional[str]
     - optional
     - Item #1772
   * - ``spm_27``
     - SPM.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1773 | Table HL79999
   * - ``spm_28``
     - SPM.28
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1774 | Table HL70544
   * - ``spm_29``
     - SPM.29
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1775 | Table HL70494
   * - ``spm_30``
     - SPM.30
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #2314
   * - ``spm_31``
     - SPM.31
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #2315
   * - ``spm_32``
     - SPM.32
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2316

.. _hl7-v2_7_1-STF:

STF Staff Identification (S15.4.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.STF.STF
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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #671 | Table HL79999
   * - ``stf_2``
     - STF.2
     - Optional[List[:ref:`CX <hl7-v2_7_1-CX>`]]
     - optional
     - Item #672 | Table HL70061
   * - ``stf_3``
     - STF.3
     - Optional[List[:ref:`XPN <hl7-v2_7_1-XPN>`]]
     - optional
     - Item #673
   * - ``stf_4``
     - STF.4
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #674 | Table HL70182
   * - ``stf_5``
     - STF.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #111 | Table HL70001
   * - ``stf_6``
     - STF.6
     - Optional[str]
     - optional
     - Item #110
   * - ``stf_7``
     - STF.7
     - Optional[str]
     - optional
     - Item #675 | Table HL70183
   * - ``stf_8``
     - STF.8
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #676 | Table HL70184
   * - ``stf_9``
     - STF.9
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #677 | Table HL70069
   * - ``stf_10``
     - STF.10
     - Optional[List[:ref:`XTN <hl7-v2_7_1-XTN>`]]
     - optional
     - Item #678
   * - ``stf_11``
     - STF.11
     - Optional[List[:ref:`XAD <hl7-v2_7_1-XAD>`]]
     - optional
     - Item #679
   * - ``stf_12``
     - STF.12
     - Optional[List[:ref:`DIN <hl7-v2_7_1-DIN>`]]
     - optional
     - Item #680 | Table HL70537
   * - ``stf_13``
     - STF.13
     - Optional[List[:ref:`DIN <hl7-v2_7_1-DIN>`]]
     - optional
     - Item #681 | Table HL70537
   * - ``stf_14``
     - STF.14
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #682
   * - ``stf_15``
     - STF.15
     - Optional[List[str]]
     - optional
     - Item #683
   * - ``stf_16``
     - STF.16
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #684 | Table HL70185
   * - ``stf_17``
     - STF.17
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #119 | Table HL70002
   * - ``stf_18``
     - STF.18
     - Optional[str]
     - optional
     - Item #785
   * - ``stf_19``
     - STF.19
     - Optional[:ref:`JCC <hl7-v2_7_1-JCC>`]
     - optional
     - Item #786 | Table HL70327
   * - ``stf_20``
     - STF.20
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1276 | Table HL70066
   * - ``stf_21``
     - STF.21
     - Optional[str]
     - optional
     - Item #1275 | Table HL70136
   * - ``stf_22``
     - STF.22
     - Optional[:ref:`DLN <hl7-v2_7_1-DLN>`]
     - optional
     - Item #1302
   * - ``stf_23``
     - STF.23
     - Optional[str]
     - optional
     - Item #1229 | Table HL70136
   * - ``stf_24``
     - STF.24
     - Optional[str]
     - optional
     - Item #1232
   * - ``stf_25``
     - STF.25
     - Optional[str]
     - optional
     - Item #1298
   * - ``stf_26``
     - STF.26
     - Optional[str]
     - optional
     - Item #1234
   * - ``stf_27``
     - STF.27
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #113 | Table HL70005
   * - ``stf_28``
     - STF.28
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #125 | Table HL70189
   * - ``stf_29``
     - STF.29
     - Optional[str]
     - optional
     - Item #1596 | Table HL70136
   * - ``stf_30``
     - STF.30
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #129 | Table HL70171
   * - ``stf_31``
     - STF.31
     - Optional[str]
     - optional
     - Item #1886
   * - ``stf_32``
     - STF.32
     - Optional[str]
     - optional
     - Item #1887 | Table HL70136
   * - ``stf_33``
     - STF.33
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1888 | Table HL70538
   * - ``stf_34``
     - STF.34
     - Optional[:ref:`DR <hl7-v2_7_1-DR>`]
     - optional
     - Item #1889
   * - ``stf_35``
     - STF.35
     - Optional[str]
     - optional
     - Item #1890
   * - ``stf_36``
     - STF.36
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1891 | Table HL70539
   * - ``stf_37``
     - STF.37
     - Optional[str]
     - optional
     - Item #1892 | Table HL70136
   * - ``stf_38``
     - STF.38
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1893 | Table HL70540
   * - ``stf_39``
     - STF.39
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2184 | Table HL70771
   * - ``stf_40``
     - STF.40
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #120 | Table HL70006
   * - ``stf_41``
     - STF.41
     - Optional[:ref:`ED <hl7-v2_7_1-ED>`]
     - optional
     - Item #1861

.. _hl7-v2_7_1-STZ:

STZ Sterilization Parameter (S17.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.STZ.STZ
   :noindex:

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
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2213 | Table HL70806
   * - ``stz_2``
     - STZ.2
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2214 | Table HL70702
   * - ``stz_3``
     - STZ.3
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2215 | Table HL70809
   * - ``stz_4``
     - STZ.4
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #2216 | Table HL70811

.. _hl7-v2_7_1-TCC:

TCC Test Code Configuration (S13.4.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.TCC.TCC
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #238
   * - ``tcc_2``
     - TCC.2
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1408
   * - ``tcc_4``
     - TCC.4
     - Optional[:ref:`SN <hl7-v2_7_1-SN>`]
     - optional
     - Item #1410
   * - ``tcc_5``
     - TCC.5
     - Optional[:ref:`SN <hl7-v2_7_1-SN>`]
     - optional
     - Item #1411
   * - ``tcc_6``
     - TCC.6
     - Optional[:ref:`SN <hl7-v2_7_1-SN>`]
     - optional
     - Item #1412
   * - ``tcc_7``
     - TCC.7
     - Optional[:ref:`SN <hl7-v2_7_1-SN>`]
     - optional
     - Item #1413
   * - ``tcc_8``
     - TCC.8
     - Optional[str]
     - optional
     - Item #1414
   * - ``tcc_9``
     - TCC.9
     - Optional[str]
     - optional
     - Item #1415 | Table HL70136
   * - ``tcc_10``
     - TCC.10
     - Optional[str]
     - optional
     - Item #1416 | Table HL70136
   * - ``tcc_11``
     - TCC.11
     - Optional[str]
     - optional
     - Item #1417 | Table HL70136
   * - ``tcc_12``
     - TCC.12
     - Optional[:ref:`SN <hl7-v2_7_1-SN>`]
     - optional
     - Item #1418
   * - ``tcc_13``
     - TCC.13
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #574 | Table HL79999
   * - ``tcc_14``
     - TCC.14
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1419 | Table HL70388

.. _hl7-v2_7_1-TCD:

TCD Test Code Detail (S13.4.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.TCD.TCD
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #238
   * - ``tcd_2``
     - TCD.2
     - Optional[:ref:`SN <hl7-v2_7_1-SN>`]
     - optional
     - Item #1420
   * - ``tcd_3``
     - TCD.3
     - Optional[:ref:`SN <hl7-v2_7_1-SN>`]
     - optional
     - Item #1421
   * - ``tcd_4``
     - TCD.4
     - Optional[:ref:`SN <hl7-v2_7_1-SN>`]
     - optional
     - Item #1422
   * - ``tcd_5``
     - TCD.5
     - Optional[:ref:`SN <hl7-v2_7_1-SN>`]
     - optional
     - Item #1413
   * - ``tcd_6``
     - TCD.6
     - Optional[str]
     - optional
     - Item #1416 | Table HL70136
   * - ``tcd_7``
     - TCD.7
     - Optional[str]
     - optional
     - Item #1424 | Table HL70136
   * - ``tcd_8``
     - TCD.8
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1425 | Table HL70389

.. _hl7-v2_7_1-TQ1:

TQ1 Timing/Quantity (S4.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.TQ1.TQ1
   :noindex:

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
     - Item #1627
   * - ``tq1_2``
     - TQ1.2
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1628
   * - ``tq1_3``
     - TQ1.3
     - Optional[List[:ref:`RPT <hl7-v2_7_1-RPT>`]]
     - optional
     - Item #1629
   * - ``tq1_4``
     - TQ1.4
     - Optional[List[str]]
     - optional
     - Item #1630
   * - ``tq1_5``
     - TQ1.5
     - Optional[List[:ref:`CQ <hl7-v2_7_1-CQ>`]]
     - optional
     - Item #1631
   * - ``tq1_6``
     - TQ1.6
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1632
   * - ``tq1_7``
     - TQ1.7
     - Optional[str]
     - optional
     - Item #1633
   * - ``tq1_8``
     - TQ1.8
     - Optional[str]
     - optional
     - Item #1634
   * - ``tq1_9``
     - TQ1.9
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #1635 | Table HL70485
   * - ``tq1_10``
     - TQ1.10
     - Optional[str]
     - optional
     - Item #1636
   * - ``tq1_11``
     - TQ1.11
     - Optional[str]
     - optional
     - Item #1637
   * - ``tq1_12``
     - TQ1.12
     - Optional[str]
     - optional
     - Item #1638 | Table HL70472
   * - ``tq1_13``
     - TQ1.13
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1639
   * - ``tq1_14``
     - TQ1.14
     - Optional[str]
     - optional
     - Item #1640

.. _hl7-v2_7_1-TQ2:

TQ2 Timing/Quantity Relationship (S4.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.TQ2.TQ2
   :noindex:

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
     - Item #1648
   * - ``tq2_2``
     - TQ2.2
     - Optional[str]
     - optional
     - Item #1649 | Table HL70503
   * - ``tq2_3``
     - TQ2.3
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #1650
   * - ``tq2_4``
     - TQ2.4
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #1651
   * - ``tq2_5``
     - TQ2.5
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #1652
   * - ``tq2_6``
     - TQ2.6
     - Optional[str]
     - optional
     - Item #1653 | Table HL70504
   * - ``tq2_7``
     - TQ2.7
     - Optional[str]
     - optional
     - Item #1654 | Table HL70505
   * - ``tq2_8``
     - TQ2.8
     - Optional[:ref:`CQ <hl7-v2_7_1-CQ>`]
     - optional
     - Item #1655
   * - ``tq2_9``
     - TQ2.9
     - Optional[str]
     - optional
     - Item #1656
   * - ``tq2_10``
     - TQ2.10
     - Optional[str]
     - optional
     - Item #1657 | Table HL70506

.. _hl7-v2_7_1-TXA:

TXA Transcription Document Header (S9.7.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.TXA.TXA
   :noindex:

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
     - Item #914
   * - ``txa_2``
     - TXA.2
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #915 | Table HL70270
   * - ``txa_3``
     - TXA.3
     - Optional[str]
     - optional
     - Item #916 | Table HL70191
   * - ``txa_4``
     - TXA.4
     - Optional[str]
     - optional
     - Item #917
   * - ``txa_5``
     - TXA.5
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #918
   * - ``txa_6``
     - TXA.6
     - Optional[str]
     - optional
     - Item #919
   * - ``txa_7``
     - TXA.7
     - Optional[str]
     - optional
     - Item #920
   * - ``txa_8``
     - TXA.8
     - Optional[List[str]]
     - optional
     - Item #921
   * - ``txa_9``
     - TXA.9
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #922
   * - ``txa_10``
     - TXA.10
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #923
   * - ``txa_11``
     - TXA.11
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #924
   * - ``txa_12``
     - TXA.12
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #925
   * - ``txa_13``
     - TXA.13
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #926
   * - ``txa_14``
     - TXA.14
     - Optional[List[:ref:`EI <hl7-v2_7_1-EI>`]]
     - optional
     - Item #216
   * - ``txa_15``
     - TXA.15
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #217
   * - ``txa_16``
     - TXA.16
     - Optional[str]
     - optional
     - Item #927
   * - ``txa_17``
     - TXA.17
     - str
     - required
     - Item #928 | Table HL70271
   * - ``txa_18``
     - TXA.18
     - Optional[str]
     - optional
     - Item #929 | Table HL70272
   * - ``txa_19``
     - TXA.19
     - Optional[str]
     - optional
     - Item #930 | Table HL70273
   * - ``txa_20``
     - TXA.20
     - Optional[str]
     - optional
     - Item #932 | Table HL70275
   * - ``txa_21``
     - TXA.21
     - Optional[str]
     - optional
     - Item #933
   * - ``txa_22``
     - TXA.22
     - Optional[List[:ref:`PPN <hl7-v2_7_1-PPN>`]]
     - optional
     - Item #934
   * - ``txa_23``
     - TXA.23
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #935
   * - ``txa_24``
     - TXA.24
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
     - optional
     - Item #2378
   * - ``txa_25``
     - TXA.25
     - Optional[List[str]]
     - optional
     - Item #3301
   * - ``txa_26``
     - TXA.26
     - Optional[str]
     - optional
     - Item #3302

.. _hl7-v2_7_1-UAC:

UAC User Authentication Credential Segment (S2.14.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.UAC.UAC
   :noindex:

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
     - :ref:`CWE <hl7-v2_7_1-CWE>`
     - required
     - Item #2267 | Table HL70615
   * - ``uac_2``
     - UAC.2
     - :ref:`ED <hl7-v2_7_1-ED>`
     - required
     - Item #2268

.. _hl7-v2_7_1-UB2:

UB2 Uniform Billing Data (S6.5.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.UB2.UB2
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
     - Optional[List[:ref:`CWE <hl7-v2_7_1-CWE>`]]
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
     - Optional[List[:ref:`UVC <hl7-v2_7_1-UVC>`]]
     - optional
     - Item #558
   * - ``ub2_7``
     - UB2.7
     - Optional[List[:ref:`OCD <hl7-v2_7_1-OCD>`]]
     - optional
     - Item #559
   * - ``ub2_8``
     - UB2.8
     - Optional[List[:ref:`OSP <hl7-v2_7_1-OSP>`]]
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
   * - ``ub2_17``
     - UB2.17
     - Optional[str]
     - optional
     - Item #815

.. _hl7-v2_7_1-VAR:

VAR Variance (S12.4.4).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.VAR.VAR
   :noindex:

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
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #1212
   * - ``var_2``
     - VAR.2
     - str
     - required
     - Item #1213
   * - ``var_3``
     - VAR.3
     - Optional[str]
     - optional
     - Item #1214
   * - ``var_4``
     - VAR.4
     - Optional[List[:ref:`XCN <hl7-v2_7_1-XCN>`]]
     - optional
     - Item #1215
   * - ``var_5``
     - VAR.5
     - Optional[:ref:`CWE <hl7-v2_7_1-CWE>`]
     - optional
     - Item #1216
   * - ``var_6``
     - VAR.6
     - Optional[List[str]]
     - optional
     - Item #1217

.. _hl7-v2_7_1-VND:

VND Purchasing Vendor (S17.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_7_1.segments.VND.VND
   :noindex:

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
     - Item #2217
   * - ``vnd_2``
     - VND.2
     - :ref:`EI <hl7-v2_7_1-EI>`
     - required
     - Item #2218
   * - ``vnd_3``
     - VND.3
     - Optional[str]
     - optional
     - Item #2276
   * - ``vnd_4``
     - VND.4
     - Optional[:ref:`EI <hl7-v2_7_1-EI>`]
     - optional
     - Item #2219
   * - ``vnd_5``
     - VND.5
     - Optional[:ref:`CNE <hl7-v2_7_1-CNE>`]
     - optional
     - Item #2220 | Table HL70532
