v2.3.1 Segments
===============

.. _hl7-v2_3_1-ACC:

ACC ACC - accident segment (S6.4.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.ACC.ACC
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #527
   * - ``acc_2``
     - ACC.2
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #528 | Table HL70050
   * - ``acc_3``
     - ACC.3
     - Optional[str]
     - optional
     - Item #529
   * - ``acc_4``
     - ACC.4
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
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

.. _hl7-v2_3_1-ADD:

ADD ADD - addendum segment (S2.24.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.ADD.ADD
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

.. _hl7-v2_3_1-AIG:

AIG AIG - appointment information - general resource segment (S10.5.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.AIG.AIG
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #897
   * - ``aig_4``
     - AIG.4
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #898
   * - ``aig_5``
     - AIG.5
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #899
   * - ``aig_6``
     - AIG.6
     - Optional[str]
     - optional
     - Item #900
   * - ``aig_7``
     - AIG.7
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #901
   * - ``aig_8``
     - AIG.8
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1202
   * - ``aig_9``
     - AIG.9
     - Optional[str]
     - optional
     - Item #891
   * - ``aig_10``
     - AIG.10
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #892
   * - ``aig_11``
     - AIG.11
     - Optional[str]
     - optional
     - Item #893
   * - ``aig_12``
     - AIG.12
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #894
   * - ``aig_13``
     - AIG.13
     - Optional[str]
     - optional
     - Item #895 | Table HL70279
   * - ``aig_14``
     - AIG.14
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #889 | Table HL70278

.. _hl7-v2_3_1-AIL:

AIL AIL - appointment information - location resource segment (S10.5.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.AIL.AIL
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
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #903
   * - ``ail_4``
     - AIL.4
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #904
   * - ``ail_5``
     - AIL.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #905
   * - ``ail_6``
     - AIL.6
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1202
   * - ``ail_7``
     - AIL.7
     - Optional[str]
     - optional
     - Item #891
   * - ``ail_8``
     - AIL.8
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #892
   * - ``ail_9``
     - AIL.9
     - Optional[str]
     - optional
     - Item #893
   * - ``ail_10``
     - AIL.10
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #894
   * - ``ail_11``
     - AIL.11
     - Optional[str]
     - optional
     - Item #895 | Table HL70279
   * - ``ail_12``
     - AIL.12
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #889 | Table HL70278

.. _hl7-v2_3_1-AIP:

AIP AIP - appointment information - personnel resource segment (S10.5.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.AIP.AIP
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
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #913
   * - ``aip_4``
     - AIP.4
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #907
   * - ``aip_5``
     - AIP.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #899
   * - ``aip_6``
     - AIP.6
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1202
   * - ``aip_7``
     - AIP.7
     - Optional[str]
     - optional
     - Item #891
   * - ``aip_8``
     - AIP.8
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #892
   * - ``aip_9``
     - AIP.9
     - Optional[str]
     - optional
     - Item #893
   * - ``aip_10``
     - AIP.10
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #894
   * - ``aip_11``
     - AIP.11
     - Optional[str]
     - optional
     - Item #895 | Table HL70279
   * - ``aip_12``
     - AIP.12
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #889 | Table HL70278

.. _hl7-v2_3_1-AIS:

AIS AIS - appointment information - service segment (S10.5.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.AIS.AIS
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #238
   * - ``ais_4``
     - AIS.4
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1202
   * - ``ais_5``
     - AIS.5
     - Optional[str]
     - optional
     - Item #891
   * - ``ais_6``
     - AIS.6
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #892
   * - ``ais_7``
     - AIS.7
     - Optional[str]
     - optional
     - Item #893
   * - ``ais_8``
     - AIS.8
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #894
   * - ``ais_9``
     - AIS.9
     - Optional[str]
     - optional
     - Item #895 | Table HL70279
   * - ``ais_10``
     - AIS.10
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #889 | Table HL70278

.. _hl7-v2_3_1-AL1:

AL1 AL1 - patient allergy information segment (S3.3.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.AL1.AL1
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #205
   * - ``al1_4``
     - AL1.4
     - Optional[str]
     - optional
     - Item #206 | Table HL70128
   * - ``al1_5``
     - AL1.5
     - Optional[List[str]]
     - optional
     - Item #207
   * - ``al1_6``
     - AL1.6
     - Optional[str]
     - optional
     - Item #208

.. _hl7-v2_3_1-APR:

APR APR - appointment preferences segment (S10.5.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.APR.APR
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
     - Optional[List[:ref:`SCV <hl7-v2_3_1-SCV>`]]
     - optional
     - Item #908 | Table HL70294
   * - ``apr_2``
     - APR.2
     - Optional[List[:ref:`SCV <hl7-v2_3_1-SCV>`]]
     - optional
     - Item #909 | Table HL70294
   * - ``apr_3``
     - APR.3
     - Optional[List[:ref:`SCV <hl7-v2_3_1-SCV>`]]
     - optional
     - Item #910 | Table HL70294
   * - ``apr_4``
     - APR.4
     - Optional[str]
     - optional
     - Item #911
   * - ``apr_5``
     - APR.5
     - Optional[List[:ref:`SCV <hl7-v2_3_1-SCV>`]]
     - optional
     - Item #912

.. _hl7-v2_3_1-ARQ:

ARQ ARQ - appointment request segment (S10.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.ARQ.ARQ
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
     - :ref:`EI <hl7-v2_3_1-EI>`
     - required
     - Item #860
   * - ``arq_2``
     - ARQ.2
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #861
   * - ``arq_3``
     - ARQ.3
     - Optional[str]
     - optional
     - Item #862
   * - ``arq_4``
     - ARQ.4
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #218
   * - ``arq_5``
     - ARQ.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #864
   * - ``arq_6``
     - ARQ.6
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #865
   * - ``arq_7``
     - ARQ.7
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #866 | Table HL70276
   * - ``arq_8``
     - ARQ.8
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #867 | Table HL70277
   * - ``arq_9``
     - ARQ.9
     - Optional[str]
     - optional
     - Item #868
   * - ``arq_10``
     - ARQ.10
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #869
   * - ``arq_11``
     - ARQ.11
     - Optional[List[:ref:`DR <hl7-v2_3_1-DR>`]]
     - optional
     - Item #870
   * - ``arq_12``
     - ARQ.12
     - Optional[str]
     - optional
     - Item #871
   * - ``arq_13``
     - ARQ.13
     - Optional[:ref:`RI <hl7-v2_3_1-RI>`]
     - optional
     - Item #872
   * - ``arq_14``
     - ARQ.14
     - Optional[str]
     - optional
     - Item #873
   * - ``arq_15``
     - ARQ.15
     - List[:ref:`XCN <hl7-v2_3_1-XCN>`]
     - required
     - Item #874
   * - ``arq_16``
     - ARQ.16
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #875
   * - ``arq_17``
     - ARQ.17
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #876
   * - ``arq_18``
     - ARQ.18
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #877
   * - ``arq_19``
     - ARQ.19
     - List[:ref:`XCN <hl7-v2_3_1-XCN>`]
     - required
     - Item #878
   * - ``arq_20``
     - ARQ.20
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #879
   * - ``arq_21``
     - ARQ.21
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #880
   * - ``arq_22``
     - ARQ.22
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #881
   * - ``arq_23``
     - ARQ.23
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #882

.. _hl7-v2_3_1-AUT:

AUT Authorization Information (S11.5.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.AUT.AUT
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1146 | Table HL70072
   * - ``aut_2``
     - AUT.2
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #1147 | Table HL70285
   * - ``aut_3``
     - AUT.3
     - Optional[str]
     - optional
     - Item #1148
   * - ``aut_4``
     - AUT.4
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1149
   * - ``aut_5``
     - AUT.5
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1150
   * - ``aut_6``
     - AUT.6
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #1151
   * - ``aut_7``
     - AUT.7
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
     - optional
     - Item #1152
   * - ``aut_8``
     - AUT.8
     - Optional[str]
     - optional
     - Item #1153
   * - ``aut_9``
     - AUT.9
     - Optional[str]
     - optional
     - Item #1154
   * - ``aut_10``
     - AUT.10
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1145

.. _hl7-v2_3_1-BHS:

BHS BHS - batch header segment (S2.24.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.BHS.BHS
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
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

.. _hl7-v2_3_1-BLG:

BLG BLG - billing segment (S4.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.BLG.BLG
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
     - Optional[:ref:`CCD <hl7-v2_3_1-CCD>`]
     - optional
     - Item #234 | Table HL70100
   * - ``blg_2``
     - BLG.2
     - Optional[str]
     - optional
     - Item #235 | Table HL70122
   * - ``blg_3``
     - BLG.3
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #236

.. _hl7-v2_3_1-BTS:

BTS BTS - batch trailer segment (S2.24.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.BTS.BTS
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

.. _hl7-v2_3_1-CDM:

CDM CDM -  charge description master segment (S8.9.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.CDM.CDM
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #1306 | Table HL70132
   * - ``cdm_2``
     - CDM.2
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #983
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
     - Optional[str]
     - optional
     - Item #986 | Table HL70268
   * - ``cdm_6``
     - CDM.6
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #987
   * - ``cdm_7``
     - CDM.7
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #393 | Table HL70088
   * - ``cdm_8``
     - CDM.8
     - Optional[str]
     - optional
     - Item #675 | Table HL70183
   * - ``cdm_9``
     - CDM.9
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #990
   * - ``cdm_10``
     - CDM.10
     - Optional[str]
     - optional
     - Item #991
   * - ``cdm_11``
     - CDM.11
     - Optional[List[:ref:`CK <hl7-v2_3_1-CK>`]]
     - optional
     - Item #992
   * - ``cdm_12``
     - CDM.12
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #993
   * - ``cdm_13``
     - CDM.13
     - Optional[str]
     - optional
     - Item #994 | Table HL70136

.. _hl7-v2_3_1-CM0:

CM0 CM0 - clinical study master segment (S8.10.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.CM0.CM0
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
     - :ref:`EI <hl7-v2_3_1-EI>`
     - required
     - Item #1011
   * - ``cm0_3``
     - CM0.3
     - Optional[List[:ref:`EI <hl7-v2_3_1-EI>`]]
     - optional
     - Item #1036
   * - ``cm0_4``
     - CM0.4
     - str
     - required
     - Item #1013
   * - ``cm0_5``
     - CM0.5
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
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
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #1018
   * - ``cm0_10``
     - CM0.10
     - Optional[:ref:`XTN <hl7-v2_3_1-XTN>`]
     - optional
     - Item #1019
   * - ``cm0_11``
     - CM0.11
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #1020

.. _hl7-v2_3_1-CM1:

CM1 CM1 - clinical study phase master segment (S8.10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.CM1.CM1
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #1022
   * - ``cm1_3``
     - CM1.3
     - str
     - required
     - Item #1023

.. _hl7-v2_3_1-CM2:

CM2 CM2 - clinical study schedule master segment (S8.10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.CM2.CM2
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #1025
   * - ``cm2_3``
     - CM2.3
     - Optional[str]
     - optional
     - Item #1026
   * - ``cm2_4``
     - CM2.4
     - List[:ref:`CE <hl7-v2_3_1-CE>`]
     - required
     - Item #1027

.. _hl7-v2_3_1-CSP:

CSP CSP - clinical study phase segment (S7.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.CSP.CSP
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #1022
   * - ``csp_2``
     - CSP.2
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #1052
   * - ``csp_3``
     - CSP.3
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1053
   * - ``csp_4``
     - CSP.4
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1054

.. _hl7-v2_3_1-CSR:

CSR CSR - clinical study registration segment (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.CSR.CSR
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
     - :ref:`EI <hl7-v2_3_1-EI>`
     - required
     - Item #1011
   * - ``csr_2``
     - CSR.2
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #1036
   * - ``csr_3``
     - CSR.3
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1037
   * - ``csr_4``
     - CSR.4
     - :ref:`CX <hl7-v2_3_1-CX>`
     - required
     - Item #1038
   * - ``csr_5``
     - CSR.5
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #1039
   * - ``csr_6``
     - CSR.6
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #1040
   * - ``csr_7``
     - CSR.7
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #1041
   * - ``csr_8``
     - CSR.8
     - List[:ref:`XCN <hl7-v2_3_1-XCN>`]
     - required
     - Item #1042
   * - ``csr_9``
     - CSR.9
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1043
   * - ``csr_10``
     - CSR.10
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1044
   * - ``csr_11``
     - CSR.11
     - Optional[List[:ref:`TS <hl7-v2_3_1-TS>`]]
     - optional
     - Item #1045
   * - ``csr_12``
     - CSR.12
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1046
   * - ``csr_13``
     - CSR.13
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1047
   * - ``csr_14``
     - CSR.14
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1048
   * - ``csr_15``
     - CSR.15
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1049
   * - ``csr_16``
     - CSR.16
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1050

.. _hl7-v2_3_1-CSS:

CSS CSS - clinical study data schedule segment (S7.7.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.CSS.CSS
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #1055
   * - ``css_2``
     - CSS.2
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1056
   * - ``css_3``
     - CSS.3
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1057

.. _hl7-v2_3_1-CTD:

CTD Contact Data (S11.5.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.CTD.CTD
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
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #196 | Table HL70131
   * - ``ctd_2``
     - CTD.2
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #1165
   * - ``ctd_3``
     - CTD.3
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #1166
   * - ``ctd_4``
     - CTD.4
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #1167
   * - ``ctd_5``
     - CTD.5
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #1168
   * - ``ctd_6``
     - CTD.6
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #684 | Table HL70185
   * - ``ctd_7``
     - CTD.7
     - Optional[List[:ref:`PI <hl7-v2_3_1-PI>`]]
     - optional
     - Item #1171

.. _hl7-v2_3_1-CTI:

CTI CTI - clinical trial identification segment (S7.7.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.CTI.CTI
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
     - :ref:`EI <hl7-v2_3_1-EI>`
     - required
     - Item #1011
   * - ``cti_2``
     - CTI.2
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1022
   * - ``cti_3``
     - CTI.3
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1055

.. _hl7-v2_3_1-DB1:

DB1 DB1 - Disability segment (S3.3.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.DB1.DB1
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
     - Optional[str]
     - optional
     - Item #1284 | Table HL70334
   * - ``db1_3``
     - DB1.3
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
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

.. _hl7-v2_3_1-DG1:

DG1 DG1 - diagnosis segment (S6.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.DG1.DG1
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
     - Optional[str]
     - optional
     - Item #376 | Table HL70053
   * - ``dg1_3``
     - DG1.3
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #377 | Table HL70051
   * - ``dg1_4``
     - DG1.4
     - Optional[str]
     - optional
     - Item #378
   * - ``dg1_5``
     - DG1.5
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #379
   * - ``dg1_6``
     - DG1.6
     - str
     - required
     - Item #380 | Table HL70052
   * - ``dg1_7``
     - DG1.7
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #381 | Table HL70118
   * - ``dg1_8``
     - DG1.8
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #382 | Table HL70055
   * - ``dg1_9``
     - DG1.9
     - Optional[str]
     - optional
     - Item #383 | Table HL70136
   * - ``dg1_10``
     - DG1.10
     - Optional[str]
     - optional
     - Item #384 | Table HL70056
   * - ``dg1_11``
     - DG1.11
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #385 | Table HL70083
   * - ``dg1_12``
     - DG1.12
     - Optional[str]
     - optional
     - Item #386
   * - ``dg1_13``
     - DG1.13
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
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
     - Item #389 | Table HL70359
   * - ``dg1_16``
     - DG1.16
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #390
   * - ``dg1_17``
     - DG1.17
     - Optional[str]
     - optional
     - Item #766 | Table HL70228
   * - ``dg1_18``
     - DG1.18
     - Optional[str]
     - optional
     - Item #767 | Table HL70136
   * - ``dg1_19``
     - DG1.19
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #768

.. _hl7-v2_3_1-DRG:

DRG DRG - diagnosis related group segment (S6.4.3.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.DRG.DRG
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #382 | Table HL70055
   * - ``drg_2``
     - DRG.2
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #769
   * - ``drg_3``
     - DRG.3
     - Optional[str]
     - optional
     - Item #383 | Table HL70136
   * - ``drg_4``
     - DRG.4
     - Optional[str]
     - optional
     - Item #384 | Table HL70056
   * - ``drg_5``
     - DRG.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #385 | Table HL70083
   * - ``drg_6``
     - DRG.6
     - Optional[str]
     - optional
     - Item #386
   * - ``drg_7``
     - DRG.7
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
     - optional
     - Item #387
   * - ``drg_8``
     - DRG.8
     - Optional[str]
     - optional
     - Item #770 | Table HL70229
   * - ``drg_9``
     - DRG.9
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
     - optional
     - Item #771
   * - ``drg_10``
     - DRG.10
     - Optional[str]
     - optional
     - Item #767 | Table HL70136

.. _hl7-v2_3_1-DSC:

DSC DSC - Continuation pointer segment (S2.24.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.DSC.DSC
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

.. _hl7-v2_3_1-DSP:

DSP DSP - display data segment (S2.24.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.DSP.DSP
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

.. _hl7-v2_3_1-EQL:

EQL EQL - embedded query language segment (S2.24.16.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.EQL.EQL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``eql_1``
     - EQL.1
     - Optional[str]
     - optional
     - Item #696
   * - ``eql_2``
     - EQL.2
     - str
     - required
     - Item #697 | Table HL70106
   * - ``eql_3``
     - EQL.3
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #709
   * - ``eql_4``
     - EQL.4
     - str
     - required
     - Item #710

.. _hl7-v2_3_1-ERQ:

ERQ ERQ - event replay query segment (S2.24.21).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.ERQ.ERQ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``erq_1``
     - ERQ.1
     - Optional[str]
     - optional
     - Item #696
   * - ``erq_2``
     - ERQ.2
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #706
   * - ``erq_3``
     - ERQ.3
     - Optional[List[:ref:`QIP <hl7-v2_3_1-QIP>`]]
     - optional
     - Item #705

.. _hl7-v2_3_1-ERR:

ERR ERR - error segment (S2.24.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.ERR.ERR
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
     - List[:ref:`ELD <hl7-v2_3_1-ELD>`]
     - required
     - Item #24

.. _hl7-v2_3_1-EVN:

EVN EVN - event type segment (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.EVN.EVN
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
     - Optional[str]
     - optional
     - Item #99 | Table HL70003
   * - ``evn_2``
     - EVN.2
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #100
   * - ``evn_3``
     - EVN.3
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #101
   * - ``evn_4``
     - EVN.4
     - Optional[str]
     - optional
     - Item #102 | Table HL70062
   * - ``evn_5``
     - EVN.5
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #103 | Table HL70188
   * - ``evn_6``
     - EVN.6
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1278

.. _hl7-v2_3_1-FAC:

FAC FAC - facility segment (S7.11.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.FAC.FAC
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
     - :ref:`EI <hl7-v2_3_1-EI>`
     - required
     - Item #1262
   * - ``fac_2``
     - FAC.2
     - Optional[str]
     - optional
     - Item #1263 | Table HL70331
   * - ``fac_3``
     - FAC.3
     - List[:ref:`XAD <hl7-v2_3_1-XAD>`]
     - required
     - Item #1264
   * - ``fac_4``
     - FAC.4
     - :ref:`XTN <hl7-v2_3_1-XTN>`
     - required
     - Item #1265
   * - ``fac_5``
     - FAC.5
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #1266
   * - ``fac_6``
     - FAC.6
     - Optional[List[str]]
     - optional
     - Item #1267
   * - ``fac_7``
     - FAC.7
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #1166
   * - ``fac_8``
     - FAC.8
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #1269
   * - ``fac_9``
     - FAC.9
     - List[:ref:`XCN <hl7-v2_3_1-XCN>`]
     - required
     - Item #1270
   * - ``fac_10``
     - FAC.10
     - Optional[str]
     - optional
     - Item #1271
   * - ``fac_11``
     - FAC.11
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #1272
   * - ``fac_12``
     - FAC.12
     - Optional[:ref:`XTN <hl7-v2_3_1-XTN>`]
     - optional
     - Item #1273

.. _hl7-v2_3_1-FHS:

FHS FHS - file header segment (S2.24.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.FHS.FHS
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
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

.. _hl7-v2_3_1-FT1:

FT1 FT1 - financial transaction segment (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.FT1.FT1
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
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #358
   * - ``ft1_5``
     - FT1.5
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #359
   * - ``ft1_6``
     - FT1.6
     - str
     - required
     - Item #360 | Table HL70017
   * - ``ft1_7``
     - FT1.7
     - :ref:`CE <hl7-v2_3_1-CE>`
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
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
     - optional
     - Item #365
   * - ``ft1_12``
     - FT1.12
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
     - optional
     - Item #366
   * - ``ft1_13``
     - FT1.13
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #367 | Table HL70049
   * - ``ft1_14``
     - FT1.14
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #368 | Table HL70072
   * - ``ft1_15``
     - FT1.15
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
     - optional
     - Item #369
   * - ``ft1_16``
     - FT1.16
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #133
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
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #371 | Table HL70051
   * - ``ft1_20``
     - FT1.20
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #372 | Table HL70084
   * - ``ft1_21``
     - FT1.21
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #373
   * - ``ft1_22``
     - FT1.22
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
     - optional
     - Item #374
   * - ``ft1_23``
     - FT1.23
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #217
   * - ``ft1_24``
     - FT1.24
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #765
   * - ``ft1_25``
     - FT1.25
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #393 | Table HL70088
   * - ``ft1_26``
     - FT1.26
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1316 | Table HL70340

.. _hl7-v2_3_1-FTS:

FTS FTS - file trailer segment (S2.24.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.FTS.FTS
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

.. _hl7-v2_3_1-GOL:

GOL Goal Detail (S12.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.GOL.GOL
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
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #817
   * - ``gol_3``
     - GOL.3
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #818
   * - ``gol_4``
     - GOL.4
     - :ref:`EI <hl7-v2_3_1-EI>`
     - required
     - Item #819
   * - ``gol_5``
     - GOL.5
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #820
   * - ``gol_6``
     - GOL.6
     - Optional[str]
     - optional
     - Item #821
   * - ``gol_7``
     - GOL.7
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #822
   * - ``gol_8``
     - GOL.8
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #824
   * - ``gol_9``
     - GOL.9
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #825
   * - ``gol_10``
     - GOL.10
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #826
   * - ``gol_11``
     - GOL.11
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #827
   * - ``gol_12``
     - GOL.12
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #828
   * - ``gol_13``
     - GOL.13
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #829
   * - ``gol_14``
     - GOL.14
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #830
   * - ``gol_15``
     - GOL.15
     - Optional[:ref:`TQ <hl7-v2_3_1-TQ>`]
     - optional
     - Item #831
   * - ``gol_16``
     - GOL.16
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #832
   * - ``gol_17``
     - GOL.17
     - Optional[List[str]]
     - optional
     - Item #833
   * - ``gol_18``
     - GOL.18
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #834
   * - ``gol_19``
     - GOL.19
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #835
   * - ``gol_20``
     - GOL.20
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #836
   * - ``gol_21``
     - GOL.21
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #837

.. _hl7-v2_3_1-GT1:

GT1 GT1 - guarantor segment (S6.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.GT1.GT1
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
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #406
   * - ``gt1_3``
     - GT1.3
     - List[:ref:`XPN <hl7-v2_3_1-XPN>`]
     - required
     - Item #407
   * - ``gt1_4``
     - GT1.4
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #408
   * - ``gt1_5``
     - GT1.5
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #409
   * - ``gt1_6``
     - GT1.6
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #410
   * - ``gt1_7``
     - GT1.7
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #411
   * - ``gt1_8``
     - GT1.8
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
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
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #420
   * - ``gt1_17``
     - GT1.17
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #421
   * - ``gt1_18``
     - GT1.18
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #422
   * - ``gt1_19``
     - GT1.19
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #423
   * - ``gt1_20``
     - GT1.20
     - Optional[str]
     - optional
     - Item #424 | Table HL70066
   * - ``gt1_21``
     - GT1.21
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #425
   * - ``gt1_22``
     - GT1.22
     - Optional[str]
     - optional
     - Item #773 | Table HL70136
   * - ``gt1_23``
     - GT1.23
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #774 | Table HL70341
   * - ``gt1_24``
     - GT1.24
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #775
   * - ``gt1_25``
     - GT1.25
     - Optional[str]
     - optional
     - Item #776 | Table HL70136
   * - ``gt1_26``
     - GT1.26
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #777 | Table HL70218
   * - ``gt1_27``
     - GT1.27
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
     - optional
     - Item #778
   * - ``gt1_28``
     - GT1.28
     - Optional[str]
     - optional
     - Item #779
   * - ``gt1_29``
     - GT1.29
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #780
   * - ``gt1_30``
     - GT1.30
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
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
     - Optional[str]
     - optional
     - Item #755 | Table HL70223
   * - ``gt1_34``
     - GT1.34
     - Optional[List[str]]
     - optional
     - Item #145 | Table HL70009
   * - ``gt1_35``
     - GT1.35
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #129 | Table HL70171
   * - ``gt1_36``
     - GT1.36
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #118 | Table HL70296
   * - ``gt1_37``
     - GT1.37
     - Optional[str]
     - optional
     - Item #742 | Table HL70220
   * - ``gt1_38``
     - GT1.38
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #743 | Table HL70215
   * - ``gt1_39``
     - GT1.39
     - Optional[str]
     - optional
     - Item #744 | Table HL70136
   * - ``gt1_40``
     - GT1.40
     - Optional[str]
     - optional
     - Item #745 | Table HL70231
   * - ``gt1_41``
     - GT1.41
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #120 | Table HL70006
   * - ``gt1_42``
     - GT1.42
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #109
   * - ``gt1_43``
     - GT1.43
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #739 | Table HL70212
   * - ``gt1_44``
     - GT1.44
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #125 | Table HL70189
   * - ``gt1_45``
     - GT1.45
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #748
   * - ``gt1_46``
     - GT1.46
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #749
   * - ``gt1_47``
     - GT1.47
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #747 | Table HL70222
   * - ``gt1_48``
     - GT1.48
     - Optional[str]
     - optional
     - Item #784 | Table HL70063
   * - ``gt1_49``
     - GT1.49
     - Optional[str]
     - optional
     - Item #785
   * - ``gt1_50``
     - GT1.50
     - Optional[:ref:`JCC <hl7-v2_3_1-JCC>`]
     - optional
     - Item #786 | Table HL70327
   * - ``gt1_51``
     - GT1.51
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #1299
   * - ``gt1_52``
     - GT1.52
     - Optional[str]
     - optional
     - Item #753 | Table HL70295
   * - ``gt1_53``
     - GT1.53
     - Optional[str]
     - optional
     - Item #752 | Table HL70311
   * - ``gt1_54``
     - GT1.54
     - Optional[:ref:`FC <hl7-v2_3_1-FC>`]
     - optional
     - Item #1231 | Table HL70064
   * - ``gt1_55``
     - GT1.55
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1291 | Table HL70005

.. _hl7-v2_3_1-IN1:

IN1 IN1 - insurance segment (S6.4.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.IN1.IN1
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #368 | Table HL70072
   * - ``in1_3``
     - IN1.3
     - List[:ref:`CX <hl7-v2_3_1-CX>`]
     - required
     - Item #428
   * - ``in1_4``
     - IN1.4
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #429
   * - ``in1_5``
     - IN1.5
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #430
   * - ``in1_6``
     - IN1.6
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #431
   * - ``in1_7``
     - IN1.7
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #432
   * - ``in1_8``
     - IN1.8
     - Optional[str]
     - optional
     - Item #433
   * - ``in1_9``
     - IN1.9
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #434
   * - ``in1_10``
     - IN1.10
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #435
   * - ``in1_11``
     - IN1.11
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
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
     - Optional[:ref:`AUI <hl7-v2_3_1-AUI>`]
     - optional
     - Item #439
   * - ``in1_15``
     - IN1.15
     - Optional[str]
     - optional
     - Item #440 | Table HL70086
   * - ``in1_16``
     - IN1.16
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #441
   * - ``in1_17``
     - IN1.17
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #442 | Table HL70063
   * - ``in1_18``
     - IN1.18
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #443
   * - ``in1_19``
     - IN1.19
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
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
     - Item #450 | Table HL70136
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #454
   * - ``in1_30``
     - IN1.30
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
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
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
     - optional
     - Item #462
   * - ``in1_38``
     - IN1.38
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
     - optional
     - Item #463
   * - ``in1_39``
     - IN1.39
     - Optional[str]
     - optional
     - Item #464
   * - ``in1_40``
     - IN1.40
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
     - optional
     - Item #465
   * - ``in1_41``
     - IN1.41
     - Optional[:ref:`CP <hl7-v2_3_1-CP>`]
     - optional
     - Item #466
   * - ``in1_42``
     - IN1.42
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #467 | Table HL70066
   * - ``in1_43``
     - IN1.43
     - Optional[str]
     - optional
     - Item #468 | Table HL70001
   * - ``in1_44``
     - IN1.44
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
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
   * - ``in1_47``
     - IN1.47
     - Optional[str]
     - optional
     - Item #1227 | Table HL70309
   * - ``in1_48``
     - IN1.48
     - Optional[str]
     - optional
     - Item #753 | Table HL70295
   * - ``in1_49``
     - IN1.49
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #1230

.. _hl7-v2_3_1-IN2:

IN2 IN2 - insurance additional information segment (S6.4.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.IN2.IN2
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
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #472
   * - ``in2_2``
     - IN2.2
     - Optional[str]
     - optional
     - Item #473
   * - ``in2_3``
     - IN2.3
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #474
   * - ``in2_4``
     - IN2.4
     - Optional[str]
     - optional
     - Item #475 | Table HL70139
   * - ``in2_5``
     - IN2.5
     - Optional[List[str]]
     - optional
     - Item #476 | Table HL70137
   * - ``in2_6``
     - IN2.6
     - Optional[str]
     - optional
     - Item #477
   * - ``in2_7``
     - IN2.7
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #478
   * - ``in2_8``
     - IN2.8
     - Optional[str]
     - optional
     - Item #479
   * - ``in2_9``
     - IN2.9
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #480
   * - ``in2_10``
     - IN2.10
     - Optional[str]
     - optional
     - Item #481
   * - ``in2_11``
     - IN2.11
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
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
     - Item #492
   * - ``in2_22``
     - IN2.22
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
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
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #496
   * - ``in2_26``
     - IN2.26
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #497
   * - ``in2_27``
     - IN2.27
     - Optional[str]
     - optional
     - Item #498 | Table HL70144
   * - ``in2_28``
     - IN2.28
     - Optional[List[:ref:`RMC <hl7-v2_3_1-RMC>`]]
     - optional
     - Item #499 | Table HL70145
   * - ``in2_29``
     - IN2.29
     - Optional[List[:ref:`PTA <hl7-v2_3_1-PTA>`]]
     - optional
     - Item #500 | Table HL70147
   * - ``in2_30``
     - IN2.30
     - Optional[:ref:`DDI <hl7-v2_3_1-DDI>`]
     - optional
     - Item #501
   * - ``in2_31``
     - IN2.31
     - Optional[str]
     - optional
     - Item #755 | Table HL70223
   * - ``in2_32``
     - IN2.32
     - Optional[List[str]]
     - optional
     - Item #145 | Table HL70009
   * - ``in2_33``
     - IN2.33
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #129 | Table HL70171
   * - ``in2_34``
     - IN2.34
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #118 | Table HL70296
   * - ``in2_35``
     - IN2.35
     - Optional[str]
     - optional
     - Item #742 | Table HL70220
   * - ``in2_36``
     - IN2.36
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #743 | Table HL70215
   * - ``in2_37``
     - IN2.37
     - Optional[str]
     - optional
     - Item #744 | Table HL70136
   * - ``in2_38``
     - IN2.38
     - Optional[str]
     - optional
     - Item #745 | Table HL70231
   * - ``in2_39``
     - IN2.39
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #120 | Table HL70006
   * - ``in2_40``
     - IN2.40
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #109
   * - ``in2_41``
     - IN2.41
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #739 | Table HL70212
   * - ``in2_42``
     - IN2.42
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #125 | Table HL70189
   * - ``in2_43``
     - IN2.43
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
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
     - Optional[:ref:`JCC <hl7-v2_3_1-JCC>`]
     - optional
     - Item #786 | Table HL70327
   * - ``in2_48``
     - IN2.48
     - Optional[str]
     - optional
     - Item #752 | Table HL70311
   * - ``in2_49``
     - IN2.49
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #789
   * - ``in2_50``
     - IN2.50
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #790
   * - ``in2_51``
     - IN2.51
     - Optional[str]
     - optional
     - Item #791 | Table HL70222
   * - ``in2_52``
     - IN2.52
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #792
   * - ``in2_53``
     - IN2.53
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #793
   * - ``in2_54``
     - IN2.54
     - Optional[List[str]]
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
     - Optional[str]
     - optional
     - Item #797 | Table HL70232
   * - ``in2_58``
     - IN2.58
     - Optional[:ref:`XTN <hl7-v2_3_1-XTN>`]
     - optional
     - Item #798
   * - ``in2_59``
     - IN2.59
     - Optional[str]
     - optional
     - Item #799 | Table HL70312
   * - ``in2_60``
     - IN2.60
     - Optional[str]
     - optional
     - Item #800 | Table HL70313
   * - ``in2_61``
     - IN2.61
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #801
   * - ``in2_62``
     - IN2.62
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #802 | Table HL70063
   * - ``in2_63``
     - IN2.63
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #803
   * - ``in2_64``
     - IN2.64
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #804
   * - ``in2_65``
     - IN2.65
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
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
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #809
   * - ``in2_70``
     - IN2.70
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #810
   * - ``in2_71``
     - IN2.71
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #113 | Table HL70005
   * - ``in2_72``
     - IN2.72
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #811 | Table HL70344

.. _hl7-v2_3_1-IN3:

IN3 IN3 - insurance additional information, certification segment (S6.4.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.IN3.IN3
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
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #503
   * - ``in3_3``
     - IN3.3
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #504
   * - ``in3_4``
     - IN3.4
     - Optional[str]
     - optional
     - Item #505 | Table HL70136
   * - ``in3_5``
     - IN3.5
     - Optional[:ref:`MOP <hl7-v2_3_1-MOP>`]
     - optional
     - Item #506 | Table HL70148
   * - ``in3_6``
     - IN3.6
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #507
   * - ``in3_7``
     - IN3.7
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #508
   * - ``in3_8``
     - IN3.8
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
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
     - Optional[:ref:`DTN <hl7-v2_3_1-DTN>`]
     - optional
     - Item #512 | Table HL70149
   * - ``in3_12``
     - IN3.12
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #513 | Table HL70233
   * - ``in3_13``
     - IN3.13
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #514
   * - ``in3_14``
     - IN3.14
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #515 | Table HL70010
   * - ``in3_15``
     - IN3.15
     - Optional[str]
     - optional
     - Item #516
   * - ``in3_16``
     - IN3.16
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #517
   * - ``in3_17``
     - IN3.17
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #518 | Table HL70345
   * - ``in3_18``
     - IN3.18
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #519 | Table HL70346
   * - ``in3_19``
     - IN3.19
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #520
   * - ``in3_20``
     - IN3.20
     - Optional[List[:ref:`PCF <hl7-v2_3_1-PCF>`]]
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
     - Optional[List[str]]
     - optional
     - Item #525 | Table HL70152
   * - ``in3_25``
     - IN3.25
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #526 | Table HL70010

.. _hl7-v2_3_1-LCC:

LCC LCC - location charge code segment (S8.8.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.LCC.LCC
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
     - :ref:`PL <hl7-v2_3_1-PL>`
     - required
     - Item #979
   * - ``lcc_2``
     - LCC.2
     - str
     - required
     - Item #964 | Table HL70264
   * - ``lcc_3``
     - LCC.3
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #980 | Table HL70129
   * - ``lcc_4``
     - LCC.4
     - List[:ref:`CE <hl7-v2_3_1-CE>`]
     - required
     - Item #981 | Table HL70132

.. _hl7-v2_3_1-LCH:

LCH LCH - location characteristic segment (S8.8.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.LCH.LCH
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
     - :ref:`PL <hl7-v2_3_1-PL>`
     - required
     - Item #1305
   * - ``lch_2``
     - LCH.2
     - Optional[str]
     - optional
     - Item #763 | Table HL70206
   * - ``lch_3``
     - LCH.3
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #764
   * - ``lch_4``
     - LCH.4
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #1295 | Table HL70324
   * - ``lch_5``
     - LCH.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1294

.. _hl7-v2_3_1-LDP:

LDP LDP - location department segment (S8.8.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.LDP.LDP
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
     - :ref:`PL <hl7-v2_3_1-PL>`
     - required
     - Item #963
   * - ``ldp_2``
     - LDP.2
     - str
     - required
     - Item #964 | Table HL70264
   * - ``ldp_3``
     - LDP.3
     - Optional[List[str]]
     - optional
     - Item #965 | Table HL70069
   * - ``ldp_4``
     - LDP.4
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #966 | Table HL70265
   * - ``ldp_5``
     - LDP.5
     - Optional[List[str]]
     - optional
     - Item #967 | Table HL70004
   * - ``ldp_6``
     - LDP.6
     - Optional[str]
     - optional
     - Item #675 | Table HL70183
   * - ``ldp_7``
     - LDP.7
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #969
   * - ``ldp_8``
     - LDP.8
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #970
   * - ``ldp_9``
     - LDP.9
     - Optional[str]
     - optional
     - Item #971
   * - ``ldp_10``
     - LDP.10
     - Optional[List[:ref:`VH <hl7-v2_3_1-VH>`]]
     - optional
     - Item #976 | Table HL70267
   * - ``ldp_11``
     - LDP.11
     - Optional[:ref:`XTN <hl7-v2_3_1-XTN>`]
     - optional
     - Item #978

.. _hl7-v2_3_1-LOC:

LOC LOC - location identification segment (S8.8.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.LOC.LOC
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
     - :ref:`PL <hl7-v2_3_1-PL>`
     - required
     - Item #1307
   * - ``loc_2``
     - LOC.2
     - Optional[str]
     - optional
     - Item #944
   * - ``loc_3``
     - LOC.3
     - List[str]
     - required
     - Item #945 | Table HL70260
   * - ``loc_4``
     - LOC.4
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #947
   * - ``loc_5``
     - LOC.5
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #948
   * - ``loc_6``
     - LOC.6
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #949
   * - ``loc_7``
     - LOC.7
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #951
   * - ``loc_8``
     - LOC.8
     - Optional[List[str]]
     - optional
     - Item #953 | Table HL70261

.. _hl7-v2_3_1-LRL:

LRL LRL - location relationship segment (S8.8.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.LRL.LRL
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
     - :ref:`PL <hl7-v2_3_1-PL>`
     - required
     - Item #943
   * - ``lrl_2``
     - LRL.2
     - Optional[str]
     - optional
     - Item #763 | Table HL70206
   * - ``lrl_3``
     - LRL.3
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #764
   * - ``lrl_4``
     - LRL.4
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1277 | Table HL70325
   * - ``lrl_5``
     - LRL.5
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #1301
   * - ``lrl_6``
     - LRL.6
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #1292

.. _hl7-v2_3_1-MFA:

MFA MFA - master file acknowledgment segment (S8.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.MFA.MFA
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #668
   * - ``mfa_4``
     - MFA.4
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #669 | Table HL70181
   * - ``mfa_5``
     - MFA.5
     - List[:ref:`CE <hl7-v2_3_1-CE>`]
     - required
     - Item #1308
   * - ``mfa_6``
     - MFA.6
     - List[str]
     - required
     - Item #1320 | Table HL70355

.. _hl7-v2_3_1-MFE:

MFE MFE - master file entry segment (S8.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.MFE.MFE
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #662
   * - ``mfe_4``
     - MFE.4
     - List[str]
     - required
     - Item #667
   * - ``mfe_5``
     - MFE.5
     - List[str]
     - required
     - Item #1319 | Table HL70355

.. _hl7-v2_3_1-MFI:

MFI MFI - master file identification segment (S8.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.MFI.MFI
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #658 | Table HL70175
   * - ``mfi_2``
     - MFI.2
     - Optional[:ref:`HD <hl7-v2_3_1-HD>`]
     - optional
     - Item #659
   * - ``mfi_3``
     - MFI.3
     - str
     - required
     - Item #660 | Table HL70178
   * - ``mfi_4``
     - MFI.4
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #661
   * - ``mfi_5``
     - MFI.5
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #662
   * - ``mfi_6``
     - MFI.6
     - str
     - required
     - Item #663 | Table HL70179

.. _hl7-v2_3_1-MRG:

MRG MRG - merge patient information segment- (S3.3.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.MRG.MRG
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
     - List[:ref:`CX <hl7-v2_3_1-CX>`]
     - required
     - Item #211
   * - ``mrg_2``
     - MRG.2
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #212
   * - ``mrg_3``
     - MRG.3
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #213
   * - ``mrg_4``
     - MRG.4
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #214
   * - ``mrg_5``
     - MRG.5
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #1279
   * - ``mrg_6``
     - MRG.6
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #1280
   * - ``mrg_7``
     - MRG.7
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #1281

.. _hl7-v2_3_1-MSA:

MSA MSA - message acknowledgment segment (S2.24.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.MSA.MSA
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #23

.. _hl7-v2_3_1-MSH:

MSH MSH - message header segment (S2.24.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.MSH.MSH
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
     - Optional[:ref:`HD <hl7-v2_3_1-HD>`]
     - optional
     - Item #3 | Table HL70361
   * - ``msh_4``
     - MSH.4
     - Optional[:ref:`HD <hl7-v2_3_1-HD>`]
     - optional
     - Item #4 | Table HL70362
   * - ``msh_5``
     - MSH.5
     - Optional[:ref:`HD <hl7-v2_3_1-HD>`]
     - optional
     - Item #5 | Table HL70361
   * - ``msh_6``
     - MSH.6
     - Optional[:ref:`HD <hl7-v2_3_1-HD>`]
     - optional
     - Item #6 | Table HL70362
   * - ``msh_7``
     - MSH.7
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #7
   * - ``msh_8``
     - MSH.8
     - Optional[str]
     - optional
     - Item #8
   * - ``msh_9``
     - MSH.9
     - :ref:`MSG <hl7-v2_3_1-MSG>`
     - required
     - Item #9 | Table HL70076
   * - ``msh_10``
     - MSH.10
     - str
     - required
     - Item #10
   * - ``msh_11``
     - MSH.11
     - :ref:`PT <hl7-v2_3_1-PT>`
     - required
     - Item #11
   * - ``msh_12``
     - MSH.12
     - :ref:`VID <hl7-v2_3_1-VID>`
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
   * - ``msh_18``
     - MSH.18
     - Optional[List[str]]
     - optional
     - Item #692 | Table HL70211
   * - ``msh_19``
     - MSH.19
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #693
   * - ``msh_20``
     - MSH.20
     - Optional[str]
     - optional
     - Item #1317 | Table HL70356

.. _hl7-v2_3_1-NCK:

NCK System Clock (SC.2.1.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.NCK.NCK
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1172

.. _hl7-v2_3_1-NK1:

NK1 NK1 - next of kin / associated parties segment- (S3.3.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.NK1.NK1
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
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #191
   * - ``nk1_3``
     - NK1.3
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #192 | Table HL70063
   * - ``nk1_4``
     - NK1.4
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #193
   * - ``nk1_5``
     - NK1.5
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #194
   * - ``nk1_6``
     - NK1.6
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #195
   * - ``nk1_7``
     - NK1.7
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
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
     - Optional[:ref:`JCC <hl7-v2_3_1-JCC>`]
     - optional
     - Item #200 | Table HL70327
   * - ``nk1_12``
     - NK1.12
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #201
   * - ``nk1_13``
     - NK1.13
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #202
   * - ``nk1_14``
     - NK1.14
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #119 | Table HL70002
   * - ``nk1_15``
     - NK1.15
     - Optional[str]
     - optional
     - Item #111 | Table HL70001
   * - ``nk1_16``
     - NK1.16
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #110
   * - ``nk1_17``
     - NK1.17
     - Optional[List[str]]
     - optional
     - Item #755 | Table HL70223
   * - ``nk1_18``
     - NK1.18
     - Optional[List[str]]
     - optional
     - Item #145 | Table HL70009
   * - ``nk1_19``
     - NK1.19
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #129 | Table HL70171
   * - ``nk1_20``
     - NK1.20
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #118 | Table HL70296
   * - ``nk1_21``
     - NK1.21
     - Optional[str]
     - optional
     - Item #742 | Table HL70220
   * - ``nk1_22``
     - NK1.22
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #743 | Table HL70215
   * - ``nk1_23``
     - NK1.23
     - Optional[str]
     - optional
     - Item #744 | Table HL70136
   * - ``nk1_24``
     - NK1.24
     - Optional[str]
     - optional
     - Item #745 | Table HL70231
   * - ``nk1_25``
     - NK1.25
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #120 | Table HL70006
   * - ``nk1_26``
     - NK1.26
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #109
   * - ``nk1_27``
     - NK1.27
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #739 | Table HL70212
   * - ``nk1_28``
     - NK1.28
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #125 | Table HL70189
   * - ``nk1_29``
     - NK1.29
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #747 | Table HL70222
   * - ``nk1_30``
     - NK1.30
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #748
   * - ``nk1_31``
     - NK1.31
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #749
   * - ``nk1_32``
     - NK1.32
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #750
   * - ``nk1_33``
     - NK1.33
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #751
   * - ``nk1_34``
     - NK1.34
     - Optional[str]
     - optional
     - Item #752 | Table HL70311
   * - ``nk1_35``
     - NK1.35
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #113 | Table HL70005
   * - ``nk1_36``
     - NK1.36
     - Optional[str]
     - optional
     - Item #753 | Table HL70295
   * - ``nk1_37``
     - NK1.37
     - Optional[str]
     - optional
     - Item #754

.. _hl7-v2_3_1-NPU:

NPU NPU - bed status update segment (S3.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.NPU.NPU
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
     - :ref:`PL <hl7-v2_3_1-PL>`
     - required
     - Item #209
   * - ``npu_2``
     - NPU.2
     - Optional[str]
     - optional
     - Item #170 | Table HL70116

.. _hl7-v2_3_1-NSC:

NSC Application status change (SC.2.3.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.NSC.NSC
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
     - Optional[str]
     - optional
     - Item #1188 | Table HL70333
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
     - Optional[str]
     - optional
     - Item #1191
   * - ``nsc_5``
     - NSC.5
     - Optional[str]
     - optional
     - Item #1192
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
     - Optional[str]
     - optional
     - Item #1195
   * - ``nsc_9``
     - NSC.9
     - Optional[str]
     - optional
     - Item #1196

.. _hl7-v2_3_1-NST:

NST Application control level statistics (SC.2.2.16).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.NST.NST
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
     - Optional[str]
     - optional
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
     - Item #1175
   * - ``nst_4``
     - NST.4
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1176
   * - ``nst_5``
     - NST.5
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
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

.. _hl7-v2_3_1-NTE:

NTE NTE - notes and comments segment (S2.24.15).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.NTE.NTE
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1318 | Table HL70364

.. _hl7-v2_3_1-OBR:

OBR OBR - observation request segment (S7.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.OBR.OBR
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
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #216
   * - ``obr_3``
     - OBR.3
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #217
   * - ``obr_4``
     - OBR.4
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #238
   * - ``obr_5``
     - OBR.5
     - Optional[str]
     - optional
     - Item #239
   * - ``obr_6``
     - OBR.6
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #240
   * - ``obr_7``
     - OBR.7
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #241
   * - ``obr_8``
     - OBR.8
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #242
   * - ``obr_9``
     - OBR.9
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
     - optional
     - Item #243
   * - ``obr_10``
     - OBR.10
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #244
   * - ``obr_11``
     - OBR.11
     - Optional[str]
     - optional
     - Item #245 | Table HL70065
   * - ``obr_12``
     - OBR.12
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #246
   * - ``obr_13``
     - OBR.13
     - Optional[str]
     - optional
     - Item #247
   * - ``obr_14``
     - OBR.14
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #248
   * - ``obr_15``
     - OBR.15
     - Optional[:ref:`SPS <hl7-v2_3_1-SPS>`]
     - optional
     - Item #249 | Table HL70070
   * - ``obr_16``
     - OBR.16
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #226
   * - ``obr_17``
     - OBR.17
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #255
   * - ``obr_23``
     - OBR.23
     - Optional[:ref:`MOC <hl7-v2_3_1-MOC>`]
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
     - Optional[:ref:`PRL <hl7-v2_3_1-PRL>`]
     - optional
     - Item #259
   * - ``obr_27``
     - OBR.27
     - Optional[List[:ref:`TQ <hl7-v2_3_1-TQ>`]]
     - optional
     - Item #221
   * - ``obr_28``
     - OBR.28
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #260
   * - ``obr_29``
     - OBR.29
     - Optional[:ref:`EIP <hl7-v2_3_1-EIP>`]
     - optional
     - Item #261
   * - ``obr_30``
     - OBR.30
     - Optional[str]
     - optional
     - Item #262 | Table HL70124
   * - ``obr_31``
     - OBR.31
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #263
   * - ``obr_32``
     - OBR.32
     - Optional[:ref:`NDL <hl7-v2_3_1-NDL>`]
     - optional
     - Item #264
   * - ``obr_33``
     - OBR.33
     - Optional[List[:ref:`NDL <hl7-v2_3_1-NDL>`]]
     - optional
     - Item #265
   * - ``obr_34``
     - OBR.34
     - Optional[List[:ref:`NDL <hl7-v2_3_1-NDL>`]]
     - optional
     - Item #266
   * - ``obr_35``
     - OBR.35
     - Optional[List[:ref:`NDL <hl7-v2_3_1-NDL>`]]
     - optional
     - Item #267
   * - ``obr_36``
     - OBR.36
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #268
   * - ``obr_37``
     - OBR.37
     - Optional[str]
     - optional
     - Item #1028
   * - ``obr_38``
     - OBR.38
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1029
   * - ``obr_39``
     - OBR.39
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1030
   * - ``obr_40``
     - OBR.40
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1031
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
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1034
   * - ``obr_44``
     - OBR.44
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #393 | Table HL70088
   * - ``obr_45``
     - OBR.45
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1316 | Table HL70340

.. _hl7-v2_3_1-OBX:

OBX OBX - observation/result segment (S9.5.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.OBX.OBX
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #571
   * - ``obx_4``
     - OBX.4
     - str
     - required
     - Item #572
   * - ``obx_5``
     - OBX.5
     - Optional[List[str]]
     - optional
     - Item #573
   * - ``obx_6``
     - OBX.6
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
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
     - Optional[List[str]]
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #580
   * - ``obx_13``
     - OBX.13
     - Optional[str]
     - optional
     - Item #581
   * - ``obx_14``
     - OBX.14
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #582
   * - ``obx_15``
     - OBX.15
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #583
   * - ``obx_16``
     - OBX.16
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #584
   * - ``obx_17``
     - OBX.17
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #936

.. _hl7-v2_3_1-ODS:

ODS ODS - dietary orders, supplements, and preferences segment (S4.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.ODS.ODS
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
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #270
   * - ``ods_3``
     - ODS.3
     - List[:ref:`CE <hl7-v2_3_1-CE>`]
     - required
     - Item #271
   * - ``ods_4``
     - ODS.4
     - Optional[List[str]]
     - optional
     - Item #272

.. _hl7-v2_3_1-ODT:

ODT ODT - diet tray instructions segment (S4.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.ODT.ODT
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #273 | Table HL70160
   * - ``odt_2``
     - ODT.2
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #270
   * - ``odt_3``
     - ODT.3
     - Optional[str]
     - optional
     - Item #272

.. _hl7-v2_3_1-OM1:

OM1 OM1 - general segment (fields that apply to most observations) (S8.7.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.OM1.OM1
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
     - Item #586
   * - ``om1_2``
     - OM1.2
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #587
   * - ``om1_3``
     - OM1.3
     - Optional[List[str]]
     - optional
     - Item #588 | Table HL70125
   * - ``om1_4``
     - OM1.4
     - Optional[str]
     - optional
     - Item #589 | Table HL70136
   * - ``om1_5``
     - OM1.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #590
   * - ``om1_6``
     - OM1.6
     - Optional[str]
     - optional
     - Item #591
   * - ``om1_7``
     - OM1.7
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #592
   * - ``om1_8``
     - OM1.8
     - Optional[List[str]]
     - optional
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
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #598
   * - ``om1_14``
     - OM1.14
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #599
   * - ``om1_15``
     - OM1.15
     - Optional[str]
     - optional
     - Item #600 | Table HL70136
   * - ``om1_16``
     - OM1.16
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #601
   * - ``om1_17``
     - OM1.17
     - Optional[:ref:`XTN <hl7-v2_3_1-XTN>`]
     - optional
     - Item #602
   * - ``om1_18``
     - OM1.18
     - str
     - required
     - Item #603 | Table HL70174
   * - ``om1_19``
     - OM1.19
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #604
   * - ``om1_20``
     - OM1.20
     - Optional[str]
     - optional
     - Item #605
   * - ``om1_21``
     - OM1.21
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #606
   * - ``om1_22``
     - OM1.22
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
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
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #612
   * - ``om1_28``
     - OM1.28
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #613
   * - ``om1_29``
     - OM1.29
     - Optional[:ref:`XTN <hl7-v2_3_1-XTN>`]
     - optional
     - Item #614
   * - ``om1_30``
     - OM1.30
     - Optional[str]
     - optional
     - Item #615 | Table HL70177
   * - ``om1_31``
     - OM1.31
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #616
   * - ``om1_32``
     - OM1.32
     - Optional[str]
     - optional
     - Item #617
   * - ``om1_33``
     - OM1.33
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #618
   * - ``om1_34``
     - OM1.34
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #619
   * - ``om1_35``
     - OM1.35
     - Optional[str]
     - optional
     - Item #620
   * - ``om1_36``
     - OM1.36
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #621
   * - ``om1_37``
     - OM1.37
     - Optional[str]
     - optional
     - Item #622
   * - ``om1_38``
     - OM1.38
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #623
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #937 | Table HL70254
   * - ``om1_43``
     - OM1.43
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #938 | Table HL70255
   * - ``om1_44``
     - OM1.44
     - Optional[str]
     - optional
     - Item #939 | Table HL70256
   * - ``om1_45``
     - OM1.45
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #940 | Table HL70258
   * - ``om1_46``
     - OM1.46
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #941
   * - ``om1_47``
     - OM1.47
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #942 | Table HL70259

.. _hl7-v2_3_1-OM2:

OM2 OM2 - numeric observation segment (S8.7.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.OM2.OM2
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #627
   * - ``om2_3``
     - OM2.3
     - Optional[List[str]]
     - optional
     - Item #628
   * - ``om2_4``
     - OM2.4
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #629
   * - ``om2_5``
     - OM2.5
     - Optional[str]
     - optional
     - Item #630
   * - ``om2_6``
     - OM2.6
     - Optional[:ref:`RFR <hl7-v2_3_1-RFR>`]
     - optional
     - Item #631
   * - ``om2_7``
     - OM2.7
     - Optional[:ref:`NR <hl7-v2_3_1-NR>`]
     - optional
     - Item #632
   * - ``om2_8``
     - OM2.8
     - Optional[:ref:`RFR <hl7-v2_3_1-RFR>`]
     - optional
     - Item #633
   * - ``om2_9``
     - OM2.9
     - Optional[List[:ref:`DLT <hl7-v2_3_1-DLT>`]]
     - optional
     - Item #634
   * - ``om2_10``
     - OM2.10
     - Optional[str]
     - optional
     - Item #635

.. _hl7-v2_3_1-OM3:

OM3 OM3 - categorical test/observation segment (S8.7.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.OM3.OM3
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #636
   * - ``om3_3``
     - OM3.3
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #637
   * - ``om3_4``
     - OM3.4
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #638
   * - ``om3_5``
     - OM3.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #639
   * - ``om3_6``
     - OM3.6
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #640
   * - ``om3_7``
     - OM3.7
     - Optional[str]
     - optional
     - Item #570 | Table HL70125

.. _hl7-v2_3_1-OM4:

OM4 OM4 - observations that require specimens segment (S8.7.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.OM4.OM4
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #645
   * - ``om4_6``
     - OM4.6
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #646
   * - ``om4_7``
     - OM4.7
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #647
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
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
     - optional
     - Item #650
   * - ``om4_11``
     - OM4.11
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
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
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
     - optional
     - Item #654

.. _hl7-v2_3_1-OM5:

OM5 OM5 - observation batteries (sets)  segment (S8.7.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.OM5.OM5
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
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #655
   * - ``om5_3``
     - OM5.3
     - Optional[str]
     - optional
     - Item #656

.. _hl7-v2_3_1-OM6:

OM6 OM6 - Observations that are calculated from other observations segment (S8.7.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.OM6.OM6
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

.. _hl7-v2_3_1-ORC:

ORC ORC - common order segment (S4.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.ORC.ORC
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
     - Optional[str]
     - optional
     - Item #215 | Table HL70119
   * - ``orc_2``
     - ORC.2
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #216
   * - ``orc_3``
     - ORC.3
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #217
   * - ``orc_4``
     - ORC.4
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
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
     - Optional[:ref:`TQ <hl7-v2_3_1-TQ>`]
     - optional
     - Item #221
   * - ``orc_8``
     - ORC.8
     - Optional[:ref:`EIP <hl7-v2_3_1-EIP>`]
     - optional
     - Item #222
   * - ``orc_9``
     - ORC.9
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #223
   * - ``orc_10``
     - ORC.10
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #224
   * - ``orc_11``
     - ORC.11
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #225
   * - ``orc_12``
     - ORC.12
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #226
   * - ``orc_13``
     - ORC.13
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #227
   * - ``orc_14``
     - ORC.14
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #228
   * - ``orc_15``
     - ORC.15
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #229
   * - ``orc_16``
     - ORC.16
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #230
   * - ``orc_17``
     - ORC.17
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #231
   * - ``orc_18``
     - ORC.18
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #232
   * - ``orc_19``
     - ORC.19
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #233
   * - ``orc_20``
     - ORC.20
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1310 | Table HL70339
   * - ``orc_21``
     - ORC.21
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #1311
   * - ``orc_22``
     - ORC.22
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #1312
   * - ``orc_23``
     - ORC.23
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #1313
   * - ``orc_24``
     - ORC.24
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #1314

.. _hl7-v2_3_1-PCR:

PCR PCR - possible causal relationship segment (S7.11.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PCR.PCR
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #1098
   * - ``pcr_2``
     - PCR.2
     - Optional[str]
     - optional
     - Item #1099 | Table HL70249
   * - ``pcr_3``
     - PCR.3
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1100
   * - ``pcr_4``
     - PCR.4
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
     - optional
     - Item #1101
   * - ``pcr_5``
     - PCR.5
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1102
   * - ``pcr_6``
     - PCR.6
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1103
   * - ``pcr_7``
     - PCR.7
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1104
   * - ``pcr_8``
     - PCR.8
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1105
   * - ``pcr_9``
     - PCR.9
     - Optional[str]
     - optional
     - Item #1106 | Table HL70244
   * - ``pcr_10``
     - PCR.10
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1107
   * - ``pcr_11``
     - PCR.11
     - Optional[str]
     - optional
     - Item #1108 | Table HL70245
   * - ``pcr_12``
     - PCR.12
     - Optional[List[str]]
     - optional
     - Item #1109
   * - ``pcr_13``
     - PCR.13
     - Optional[str]
     - optional
     - Item #1110 | Table HL70246
   * - ``pcr_14``
     - PCR.14
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1111
   * - ``pcr_15``
     - PCR.15
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1112 | Table HL70247
   * - ``pcr_16``
     - PCR.16
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1113
   * - ``pcr_17``
     - PCR.17
     - Optional[str]
     - optional
     - Item #1114 | Table HL70248
   * - ``pcr_18``
     - PCR.18
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
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

.. _hl7-v2_3_1-PD1:

PD1 PD1 - patient additional demographic segment (S3.3.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PD1.PD1
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
     - Optional[List[str]]
     - optional
     - Item #755 | Table HL70223
   * - ``pd1_2``
     - PD1.2
     - Optional[str]
     - optional
     - Item #742 | Table HL70220
   * - ``pd1_3``
     - PD1.3
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #756
   * - ``pd1_4``
     - PD1.4
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #757
   * - ``pd1_5``
     - PD1.5
     - Optional[str]
     - optional
     - Item #745 | Table HL70231
   * - ``pd1_6``
     - PD1.6
     - Optional[str]
     - optional
     - Item #753 | Table HL70295
   * - ``pd1_7``
     - PD1.7
     - Optional[str]
     - optional
     - Item #759 | Table HL70315
   * - ``pd1_8``
     - PD1.8
     - Optional[str]
     - optional
     - Item #760 | Table HL70316
   * - ``pd1_9``
     - PD1.9
     - Optional[str]
     - optional
     - Item #761 | Table HL70136
   * - ``pd1_10``
     - PD1.10
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #762
   * - ``pd1_11``
     - PD1.11
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #743 | Table HL70215
   * - ``pd1_12``
     - PD1.12
     - Optional[str]
     - optional
     - Item #744 | Table HL70136

.. _hl7-v2_3_1-PDC:

PDC PDC - product detail country segment (S7.11.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PDC.PDC
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
     - List[:ref:`XON <hl7-v2_3_1-XON>`]
     - required
     - Item #1247
   * - ``pdc_2``
     - PDC.2
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #1248
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1251
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1255
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
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
     - optional
     - Item #1258
   * - ``pdc_13``
     - PDC.13
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
     - optional
     - Item #1259
   * - ``pdc_14``
     - PDC.14
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1260
   * - ``pdc_15``
     - PDC.15
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1261

.. _hl7-v2_3_1-PEO:

PEO PEO - product experience observation segment (S7.11.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PEO.PEO
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
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1073
   * - ``peo_2``
     - PEO.2
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1074
   * - ``peo_3``
     - PEO.3
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #1075
   * - ``peo_4``
     - PEO.4
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1076
   * - ``peo_5``
     - PEO.5
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1077
   * - ``peo_6``
     - PEO.6
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1078
   * - ``peo_7``
     - PEO.7
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
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
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1090
   * - ``peo_19``
     - PEO.19
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #1091
   * - ``peo_20``
     - PEO.20
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #1092
   * - ``peo_21``
     - PEO.21
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1096
   * - ``peo_25``
     - PEO.25
     - Optional[str]
     - optional
     - Item #1097 | Table HL70243

.. _hl7-v2_3_1-PES:

PES PES - product experience sender segment (S7.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PES.PES
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
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #1059
   * - ``pes_2``
     - PES.2
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #1060
   * - ``pes_3``
     - PES.3
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #1062
   * - ``pes_4``
     - PES.4
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #1063
   * - ``pes_5``
     - PES.5
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1068
   * - ``pes_10``
     - PES.10
     - :ref:`TS <hl7-v2_3_1-TS>`
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

.. _hl7-v2_3_1-PID:

PID PID - patient identification segment (S3.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PID.PID
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
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #105
   * - ``pid_3``
     - PID.3
     - List[:ref:`CX <hl7-v2_3_1-CX>`]
     - required
     - Item #106
   * - ``pid_4``
     - PID.4
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #107
   * - ``pid_5``
     - PID.5
     - List[:ref:`XPN <hl7-v2_3_1-XPN>`]
     - required
     - Item #108
   * - ``pid_6``
     - PID.6
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #109
   * - ``pid_7``
     - PID.7
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #110
   * - ``pid_8``
     - PID.8
     - Optional[str]
     - optional
     - Item #111 | Table HL70001
   * - ``pid_9``
     - PID.9
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #112
   * - ``pid_10``
     - PID.10
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #113 | Table HL70005
   * - ``pid_11``
     - PID.11
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #114
   * - ``pid_12``
     - PID.12
     - Optional[str]
     - optional
     - Item #115 | Table HL70289
   * - ``pid_13``
     - PID.13
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #116
   * - ``pid_14``
     - PID.14
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #117
   * - ``pid_15``
     - PID.15
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #118 | Table HL70296
   * - ``pid_16``
     - PID.16
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #119 | Table HL70002
   * - ``pid_17``
     - PID.17
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #120 | Table HL70006
   * - ``pid_18``
     - PID.18
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #121
   * - ``pid_19``
     - PID.19
     - Optional[str]
     - optional
     - Item #122
   * - ``pid_20``
     - PID.20
     - Optional[:ref:`DLN <hl7-v2_3_1-DLN>`]
     - optional
     - Item #123
   * - ``pid_21``
     - PID.21
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #124
   * - ``pid_22``
     - PID.22
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
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
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #129 | Table HL70171
   * - ``pid_27``
     - PID.27
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #130 | Table HL70172
   * - ``pid_28``
     - PID.28
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #739 | Table HL70212
   * - ``pid_29``
     - PID.29
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #740
   * - ``pid_30``
     - PID.30
     - Optional[str]
     - optional
     - Item #741 | Table HL70136

.. _hl7-v2_3_1-PR1:

PR1 PR1 - procedures segment (S6.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PR1.PR1
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
     - Optional[str]
     - optional
     - Item #392 | Table HL70089
   * - ``pr1_3``
     - PR1.3
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #393 | Table HL70088
   * - ``pr1_4``
     - PR1.4
     - Optional[str]
     - optional
     - Item #394
   * - ``pr1_5``
     - PR1.5
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #395
   * - ``pr1_6``
     - PR1.6
     - str
     - required
     - Item #396 | Table HL70230
   * - ``pr1_7``
     - PR1.7
     - Optional[str]
     - optional
     - Item #397
   * - ``pr1_8``
     - PR1.8
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
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
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #401 | Table HL70010
   * - ``pr1_12``
     - PR1.12
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #402 | Table HL70010
   * - ``pr1_13``
     - PR1.13
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #403 | Table HL70059
   * - ``pr1_14``
     - PR1.14
     - Optional[str]
     - optional
     - Item #404
   * - ``pr1_15``
     - PR1.15
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #772 | Table HL70051
   * - ``pr1_16``
     - PR1.16
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1316 | Table HL70340

.. _hl7-v2_3_1-PRA:

PRA PRA - practitioner detail segment (S8.6.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PRA.PRA
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #685
   * - ``pra_2``
     - PRA.2
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #686 | Table HL70358
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
     - Optional[List[:ref:`SPD <hl7-v2_3_1-SPD>`]]
     - optional
     - Item #689 | Table HL70337
   * - ``pra_6``
     - PRA.6
     - Optional[List[:ref:`PLN <hl7-v2_3_1-PLN>`]]
     - optional
     - Item #690 | Table HL70338
   * - ``pra_7``
     - PRA.7
     - Optional[List[:ref:`PIP <hl7-v2_3_1-PIP>`]]
     - optional
     - Item #691
   * - ``pra_8``
     - PRA.8
     - Optional[str]
     - optional
     - Item #1296

.. _hl7-v2_3_1-PRB:

PRB Problem Detail (S12.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PRB.PRB
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
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #817
   * - ``prb_3``
     - PRB.3
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #838
   * - ``prb_4``
     - PRB.4
     - :ref:`EI <hl7-v2_3_1-EI>`
     - required
     - Item #839
   * - ``prb_5``
     - PRB.5
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #820
   * - ``prb_6``
     - PRB.6
     - Optional[str]
     - optional
     - Item #841
   * - ``prb_7``
     - PRB.7
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #842
   * - ``prb_8``
     - PRB.8
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #843
   * - ``prb_9``
     - PRB.9
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #844
   * - ``prb_10``
     - PRB.10
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #845
   * - ``prb_11``
     - PRB.11
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #846
   * - ``prb_12``
     - PRB.12
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #847
   * - ``prb_13``
     - PRB.13
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #848
   * - ``prb_14``
     - PRB.14
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #849
   * - ``prb_15``
     - PRB.15
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #850
   * - ``prb_16``
     - PRB.16
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #851
   * - ``prb_17``
     - PRB.17
     - Optional[str]
     - optional
     - Item #852
   * - ``prb_18``
     - PRB.18
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #853
   * - ``prb_19``
     - PRB.19
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #854
   * - ``prb_20``
     - PRB.20
     - Optional[str]
     - optional
     - Item #855
   * - ``prb_21``
     - PRB.21
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #856
   * - ``prb_22``
     - PRB.22
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #857
   * - ``prb_23``
     - PRB.23
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #858
   * - ``prb_24``
     - PRB.24
     - Optional[str]
     - optional
     - Item #859
   * - ``prb_25``
     - PRB.25
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #823

.. _hl7-v2_3_1-PRC:

PRC PRC -  pricing segment (S8.9.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PRC.PRC
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #982 | Table HL70132
   * - ``prc_2``
     - PRC.2
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #995
   * - ``prc_3``
     - PRC.3
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #676 | Table HL70184
   * - ``prc_4``
     - PRC.4
     - Optional[List[str]]
     - optional
     - Item #967 | Table HL70004
   * - ``prc_5``
     - PRC.5
     - Optional[List[:ref:`CP <hl7-v2_3_1-CP>`]]
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
     - Optional[:ref:`MO <hl7-v2_3_1-MO>`]
     - optional
     - Item #1002
   * - ``prc_10``
     - PRC.10
     - Optional[:ref:`MO <hl7-v2_3_1-MO>`]
     - optional
     - Item #1003
   * - ``prc_11``
     - PRC.11
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1004
   * - ``prc_12``
     - PRC.12
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1005
   * - ``prc_13``
     - PRC.13
     - Optional[str]
     - optional
     - Item #1006 | Table HL70268
   * - ``prc_14``
     - PRC.14
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
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
     - Optional[:ref:`MO <hl7-v2_3_1-MO>`]
     - optional
     - Item #989
   * - ``prc_18``
     - PRC.18
     - Optional[str]
     - optional
     - Item #1009 | Table HL70269

.. _hl7-v2_3_1-PRD:

PRD Provider Data (S11.5.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PRD.PRD
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
     - List[:ref:`CE <hl7-v2_3_1-CE>`]
     - required
     - Item #1155 | Table HL70286
   * - ``prd_2``
     - PRD.2
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
     - optional
     - Item #1156
   * - ``prd_3``
     - PRD.3
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #1157
   * - ``prd_4``
     - PRD.4
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #1158
   * - ``prd_5``
     - PRD.5
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #1159
   * - ``prd_6``
     - PRD.6
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #684 | Table HL70185
   * - ``prd_7``
     - PRD.7
     - Optional[List[:ref:`PI <hl7-v2_3_1-PI>`]]
     - optional
     - Item #1162
   * - ``prd_8``
     - PRD.8
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1163
   * - ``prd_9``
     - PRD.9
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1164

.. _hl7-v2_3_1-PSH:

PSH PSH - product summary header segment (S7.11.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PSH.PSH
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
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #1235
   * - ``psh_4``
     - PSH.4
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1236
   * - ``psh_5``
     - PSH.5
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1237
   * - ``psh_6``
     - PSH.6
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
     - optional
     - Item #1238
   * - ``psh_7``
     - PSH.7
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
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
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
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

.. _hl7-v2_3_1-PTH:

PTH Pathway (S12.3.4).
~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PTH.PTH
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #1207
   * - ``pth_3``
     - PTH.3
     - :ref:`EI <hl7-v2_3_1-EI>`
     - required
     - Item #1208
   * - ``pth_4``
     - PTH.4
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #1209
   * - ``pth_5``
     - PTH.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1210
   * - ``pth_6``
     - PTH.6
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1211

.. _hl7-v2_3_1-PV1:

PV1 PV1 - patient visit segment- (S3.3.3.53).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PV1.PV1
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
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #133
   * - ``pv1_4``
     - PV1.4
     - Optional[str]
     - optional
     - Item #134 | Table HL70007
   * - ``pv1_5``
     - PV1.5
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #135
   * - ``pv1_6``
     - PV1.6
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #136
   * - ``pv1_7``
     - PV1.7
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #137 | Table HL70010
   * - ``pv1_8``
     - PV1.8
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #138 | Table HL70010
   * - ``pv1_9``
     - PV1.9
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #139 | Table HL70010
   * - ``pv1_10``
     - PV1.10
     - Optional[str]
     - optional
     - Item #140 | Table HL70069
   * - ``pv1_11``
     - PV1.11
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #141
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
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #147 | Table HL70010
   * - ``pv1_18``
     - PV1.18
     - Optional[str]
     - optional
     - Item #148 | Table HL70018
   * - ``pv1_19``
     - PV1.19
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #149
   * - ``pv1_20``
     - PV1.20
     - Optional[List[:ref:`FC <hl7-v2_3_1-FC>`]]
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
     - Optional[:ref:`DLD <hl7-v2_3_1-DLD>`]
     - optional
     - Item #167 | Table HL70113
   * - ``pv1_38``
     - PV1.38
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
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
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #172
   * - ``pv1_43``
     - PV1.43
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #173
   * - ``pv1_44``
     - PV1.44
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #174
   * - ``pv1_45``
     - PV1.45
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
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
     - Optional[:ref:`CX <hl7-v2_3_1-CX>`]
     - optional
     - Item #180 | Table HL70203
   * - ``pv1_51``
     - PV1.51
     - Optional[str]
     - optional
     - Item #1226 | Table HL70326
   * - ``pv1_52``
     - PV1.52
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #1274 | Table HL70010

.. _hl7-v2_3_1-PV2:

PV2 PV2 - patient visit - additional information segment (S3.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.PV2.PV2
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
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #181
   * - ``pv2_2``
     - PV2.2
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #182 | Table HL70129
   * - ``pv2_3``
     - PV2.3
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #183
   * - ``pv2_4``
     - PV2.4
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #188
   * - ``pv2_9``
     - PV2.9
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
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
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
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
     - Optional[str]
     - optional
     - Item #717 | Table HL70213
   * - ``pv2_17``
     - PV2.17
     - Optional[str]
     - optional
     - Item #718
   * - ``pv2_18``
     - PV2.18
     - Optional[str]
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
     - Optional[str]
     - optional
     - Item #722 | Table HL70215
   * - ``pv2_22``
     - PV2.22
     - Optional[str]
     - optional
     - Item #723 | Table HL70136
   * - ``pv2_23``
     - PV2.23
     - Optional[List[:ref:`XON <hl7-v2_3_1-XON>`]]
     - optional
     - Item #724
   * - ``pv2_24``
     - PV2.24
     - Optional[str]
     - optional
     - Item #725 | Table HL70216
   * - ``pv2_25``
     - PV2.25
     - Optional[str]
     - optional
     - Item #726 | Table HL70217
   * - ``pv2_26``
     - PV2.26
     - Optional[str]
     - optional
     - Item #727
   * - ``pv2_27``
     - PV2.27
     - Optional[str]
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #731 | Table HL70218
   * - ``pv2_31``
     - PV2.31
     - Optional[str]
     - optional
     - Item #732 | Table HL70219
   * - ``pv2_32``
     - PV2.32
     - Optional[str]
     - optional
     - Item #733 | Table HL70136
   * - ``pv2_33``
     - PV2.33
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
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

.. _hl7-v2_3_1-QAK:

QAK Query Acknowledgement (S2.24.22).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.QAK.QAK
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

.. _hl7-v2_3_1-QRD:

QRD QRD - original-style query definition segment (SC.2.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.QRD.QRD
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
     - :ref:`TS <hl7-v2_3_1-TS>`
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #30
   * - ``qrd_7``
     - QRD.7
     - :ref:`CQ <hl7-v2_3_1-CQ>`
     - required
     - Item #31 | Table HL70126
   * - ``qrd_8``
     - QRD.8
     - List[:ref:`XCN <hl7-v2_3_1-XCN>`]
     - required
     - Item #32
   * - ``qrd_9``
     - QRD.9
     - List[:ref:`CE <hl7-v2_3_1-CE>`]
     - required
     - Item #33 | Table HL70048
   * - ``qrd_10``
     - QRD.10
     - List[:ref:`CE <hl7-v2_3_1-CE>`]
     - required
     - Item #34
   * - ``qrd_11``
     - QRD.11
     - Optional[List[:ref:`VR <hl7-v2_3_1-VR>`]]
     - optional
     - Item #35
   * - ``qrd_12``
     - QRD.12
     - Optional[str]
     - optional
     - Item #36 | Table HL70108

.. _hl7-v2_3_1-QRF:

QRF QRF - original style query filter segment (S2.24.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.QRF.QRF
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #38
   * - ``qrf_3``
     - QRF.3
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
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
   * - ``qrf_9``
     - QRF.9
     - Optional[:ref:`TQ <hl7-v2_3_1-TQ>`]
     - optional
     - Item #694

.. _hl7-v2_3_1-RDF:

RDF RDF - table row definition segment (S2.24.18).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RDF.RDF
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
     - List[:ref:`RCD <hl7-v2_3_1-RCD>`]
     - required
     - Item #702

.. _hl7-v2_3_1-RDT:

RDT RDT - table row data segment (S2.24.19).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RDT.RDT
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
     - Optional[str]
     - optional
     - Item #703

.. _hl7-v2_3_1-RF1:

RF1 Referral Infomation (S11.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RF1.RF1
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1137 | Table HL70283
   * - ``rf1_2``
     - RF1.2
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1138 | Table HL70280
   * - ``rf1_3``
     - RF1.3
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1139 | Table HL70281
   * - ``rf1_4``
     - RF1.4
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1140 | Table HL70282
   * - ``rf1_5``
     - RF1.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1141 | Table HL70284
   * - ``rf1_6``
     - RF1.6
     - :ref:`EI <hl7-v2_3_1-EI>`
     - required
     - Item #1142
   * - ``rf1_7``
     - RF1.7
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1143
   * - ``rf1_8``
     - RF1.8
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1144
   * - ``rf1_9``
     - RF1.9
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1145
   * - ``rf1_10``
     - RF1.10
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1228 | Table HL70336
   * - ``rf1_11``
     - RF1.11
     - Optional[List[:ref:`EI <hl7-v2_3_1-EI>`]]
     - optional
     - Item #1300

.. _hl7-v2_3_1-RGS:

RGS RGS - resource group segment (S10.5.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RGS.RGS
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1204

.. _hl7-v2_3_1-ROL:

ROL Role (S12.3.3).
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.ROL.ROL
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
     - :ref:`EI <hl7-v2_3_1-EI>`
     - required
     - Item #1206
   * - ``rol_2``
     - ROL.2
     - str
     - required
     - Item #816 | Table HL70287
   * - ``rol_3``
     - ROL.3
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #1197
   * - ``rol_4``
     - ROL.4
     - List[:ref:`XCN <hl7-v2_3_1-XCN>`]
     - required
     - Item #1198
   * - ``rol_5``
     - ROL.5
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1199
   * - ``rol_6``
     - ROL.6
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1200
   * - ``rol_7``
     - ROL.7
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1201
   * - ``rol_8``
     - ROL.8
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1205

.. _hl7-v2_3_1-RQ1:

RQ1 RQ1 - requisition detail-1 segment (S4.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RQ1.RQ1
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #286
   * - ``rq1_3``
     - RQ1.3
     - Optional[str]
     - optional
     - Item #287
   * - ``rq1_4``
     - RQ1.4
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
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

.. _hl7-v2_3_1-RQD:

RQD RQD - requisition detail segment (S4.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RQD.RQD
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #276
   * - ``rqd_3``
     - RQD.3
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #277
   * - ``rqd_4``
     - RQD.4
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #278
   * - ``rqd_5``
     - RQD.5
     - Optional[str]
     - optional
     - Item #279
   * - ``rqd_6``
     - RQD.6
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #280
   * - ``rqd_7``
     - RQD.7
     - Optional[str]
     - optional
     - Item #281 | Table HL70319
   * - ``rqd_8``
     - RQD.8
     - Optional[str]
     - optional
     - Item #282 | Table HL70320
   * - ``rqd_9``
     - RQD.9
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #283
   * - ``rqd_10``
     - RQD.10
     - Optional[str]
     - optional
     - Item #284

.. _hl7-v2_3_1-RXA:

RXA RXA - pharmacy/treatment administration segment (S4.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RXA.RXA
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
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #345
   * - ``rxa_4``
     - RXA.4
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #346
   * - ``rxa_5``
     - RXA.5
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #347 | Table HL70292
   * - ``rxa_6``
     - RXA.6
     - str
     - required
     - Item #348
   * - ``rxa_7``
     - RXA.7
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #349
   * - ``rxa_8``
     - RXA.8
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #350
   * - ``rxa_9``
     - RXA.9
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #351
   * - ``rxa_10``
     - RXA.10
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #352
   * - ``rxa_11``
     - RXA.11
     - Optional[:ref:`LA2 <hl7-v2_3_1-LA2>`]
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1135
   * - ``rxa_15``
     - RXA.15
     - Optional[List[str]]
     - optional
     - Item #1129
   * - ``rxa_16``
     - RXA.16
     - Optional[List[:ref:`TS <hl7-v2_3_1-TS>`]]
     - optional
     - Item #1130
   * - ``rxa_17``
     - RXA.17
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1131 | Table HL70227
   * - ``rxa_18``
     - RXA.18
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1136
   * - ``rxa_19``
     - RXA.19
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1123
   * - ``rxa_20``
     - RXA.20
     - Optional[str]
     - optional
     - Item #1223 | Table HL70322
   * - ``rxa_21``
     - RXA.21
     - Optional[str]
     - optional
     - Item #1224 | Table HL70323
   * - ``rxa_22``
     - RXA.22
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1225

.. _hl7-v2_3_1-RXC:

RXC RXC - pharmacy/treatment component order segment (S4.8.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RXC.RXC
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #314
   * - ``rxc_3``
     - RXC.3
     - str
     - required
     - Item #315
   * - ``rxc_4``
     - RXC.4
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #316
   * - ``rxc_5``
     - RXC.5
     - Optional[str]
     - optional
     - Item #1124
   * - ``rxc_6``
     - RXC.6
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1125

.. _hl7-v2_3_1-RXD:

RXD RXD - pharmacy/treatment dispense segment (S4.8.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RXD.RXD
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #335 | Table HL70292
   * - ``rxd_3``
     - RXD.3
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #336
   * - ``rxd_4``
     - RXD.4
     - str
     - required
     - Item #337
   * - ``rxd_5``
     - RXD.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #338
   * - ``rxd_6``
     - RXD.6
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
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
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #341
   * - ``rxd_11``
     - RXD.11
     - Optional[str]
     - optional
     - Item #322 | Table HL70167
   * - ``rxd_12``
     - RXD.12
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
     - optional
     - Item #329
   * - ``rxd_13``
     - RXD.13
     - Optional[:ref:`LA2 <hl7-v2_3_1-LA2>`]
     - optional
     - Item #1303
   * - ``rxd_14``
     - RXD.14
     - Optional[str]
     - optional
     - Item #307 | Table HL70136
   * - ``rxd_15``
     - RXD.15
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #330
   * - ``rxd_16``
     - RXD.16
     - Optional[str]
     - optional
     - Item #1132
   * - ``rxd_17``
     - RXD.17
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1133
   * - ``rxd_18``
     - RXD.18
     - Optional[List[str]]
     - optional
     - Item #1129
   * - ``rxd_19``
     - RXD.19
     - Optional[List[:ref:`TS <hl7-v2_3_1-TS>`]]
     - optional
     - Item #1130
   * - ``rxd_20``
     - RXD.20
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1131 | Table HL70227
   * - ``rxd_21``
     - RXD.21
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1123
   * - ``rxd_22``
     - RXD.22
     - Optional[str]
     - optional
     - Item #1220
   * - ``rxd_23``
     - RXD.23
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1221
   * - ``rxd_24``
     - RXD.24
     - Optional[str]
     - optional
     - Item #1222 | Table HL70321

.. _hl7-v2_3_1-RXE:

RXE RXE - pharmacy/treatment encoded order segment (S4.8.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RXE.RXE
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
     - :ref:`TQ <hl7-v2_3_1-TQ>`
     - required
     - Item #221
   * - ``rxe_2``
     - RXE.2
     - :ref:`CE <hl7-v2_3_1-CE>`
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #320
   * - ``rxe_6``
     - RXE.6
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #321
   * - ``rxe_7``
     - RXE.7
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #298
   * - ``rxe_8``
     - RXE.8
     - Optional[:ref:`LA1 <hl7-v2_3_1-LA1>`]
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #324
   * - ``rxe_12``
     - RXE.12
     - Optional[str]
     - optional
     - Item #304
   * - ``rxe_13``
     - RXE.13
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #305
   * - ``rxe_14``
     - RXE.14
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #328
   * - ``rxe_19``
     - RXE.19
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
     - optional
     - Item #329
   * - ``rxe_20``
     - RXE.20
     - Optional[str]
     - optional
     - Item #307 | Table HL70136
   * - ``rxe_21``
     - RXE.21
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #330
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #333
   * - ``rxe_25``
     - RXE.25
     - Optional[str]
     - optional
     - Item #1126
   * - ``rxe_26``
     - RXE.26
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1127
   * - ``rxe_27``
     - RXE.27
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1128
   * - ``rxe_28``
     - RXE.28
     - Optional[str]
     - optional
     - Item #1220
   * - ``rxe_29``
     - RXE.29
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1221
   * - ``rxe_30``
     - RXE.30
     - Optional[str]
     - optional
     - Item #1222 | Table HL70321

.. _hl7-v2_3_1-RXG:

RXG RXG - pharmacy/treatment give segment (S4.8.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RXG.RXG
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
     - :ref:`TQ <hl7-v2_3_1-TQ>`
     - required
     - Item #221
   * - ``rxg_4``
     - RXG.4
     - :ref:`CE <hl7-v2_3_1-CE>`
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #320
   * - ``rxg_8``
     - RXG.8
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #321
   * - ``rxg_9``
     - RXG.9
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #351
   * - ``rxg_10``
     - RXG.10
     - Optional[str]
     - optional
     - Item #322 | Table HL70167
   * - ``rxg_11``
     - RXG.11
     - Optional[:ref:`LA2 <hl7-v2_3_1-LA2>`]
     - optional
     - Item #1303
   * - ``rxg_12``
     - RXG.12
     - Optional[str]
     - optional
     - Item #307 | Table HL70136
   * - ``rxg_13``
     - RXG.13
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #343
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #333
   * - ``rxg_17``
     - RXG.17
     - Optional[str]
     - optional
     - Item #1126
   * - ``rxg_18``
     - RXG.18
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1127
   * - ``rxg_19``
     - RXG.19
     - Optional[List[str]]
     - optional
     - Item #1129
   * - ``rxg_20``
     - RXG.20
     - Optional[List[:ref:`TS <hl7-v2_3_1-TS>`]]
     - optional
     - Item #1130
   * - ``rxg_21``
     - RXG.21
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1131 | Table HL70227
   * - ``rxg_22``
     - RXG.22
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1123

.. _hl7-v2_3_1-RXO:

RXO RXO - pharmacy/treatment order segment (S4.8.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RXO.RXO
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #292
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #295
   * - ``rxo_5``
     - RXO.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #296
   * - ``rxo_6``
     - RXO.6
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #297
   * - ``rxo_7``
     - RXO.7
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #298
   * - ``rxo_8``
     - RXO.8
     - Optional[:ref:`LA1 <hl7-v2_3_1-LA1>`]
     - optional
     - Item #299
   * - ``rxo_9``
     - RXO.9
     - Optional[str]
     - optional
     - Item #300 | Table HL70161
   * - ``rxo_10``
     - RXO.10
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #301
   * - ``rxo_11``
     - RXO.11
     - Optional[str]
     - optional
     - Item #302
   * - ``rxo_12``
     - RXO.12
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #303
   * - ``rxo_13``
     - RXO.13
     - Optional[str]
     - optional
     - Item #304
   * - ``rxo_14``
     - RXO.14
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #305
   * - ``rxo_15``
     - RXO.15
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
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
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1122
   * - ``rxo_20``
     - RXO.20
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #1123
   * - ``rxo_21``
     - RXO.21
     - Optional[str]
     - optional
     - Item #1218
   * - ``rxo_22``
     - RXO.22
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1219
   * - ``rxo_23``
     - RXO.23
     - Optional[:ref:`CQ <hl7-v2_3_1-CQ>`]
     - optional
     - Item #329

.. _hl7-v2_3_1-RXR:

RXR RXR - pharmacy/treatment route segment (S4.8.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.RXR.RXR
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #309 | Table HL70162
   * - ``rxr_2``
     - RXR.2
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #310 | Table HL70163
   * - ``rxr_3``
     - RXR.3
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #311 | Table HL70164
   * - ``rxr_4``
     - RXR.4
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #312 | Table HL70165
   * - ``rxr_5``
     - RXR.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1315

.. _hl7-v2_3_1-SCH:

SCH SCH - schedule activity information segment (S10.5.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.SCH.SCH
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
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #860
   * - ``sch_2``
     - SCH.2
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #861
   * - ``sch_3``
     - SCH.3
     - Optional[str]
     - optional
     - Item #862
   * - ``sch_4``
     - SCH.4
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #218
   * - ``sch_5``
     - SCH.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #864
   * - ``sch_6``
     - SCH.6
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #883
   * - ``sch_7``
     - SCH.7
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #866 | Table HL70276
   * - ``sch_8``
     - SCH.8
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #867 | Table HL70277
   * - ``sch_9``
     - SCH.9
     - Optional[str]
     - optional
     - Item #868
   * - ``sch_10``
     - SCH.10
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #869
   * - ``sch_11``
     - SCH.11
     - List[:ref:`TQ <hl7-v2_3_1-TQ>`]
     - required
     - Item #884
   * - ``sch_12``
     - SCH.12
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #874
   * - ``sch_13``
     - SCH.13
     - Optional[:ref:`XTN <hl7-v2_3_1-XTN>`]
     - optional
     - Item #875
   * - ``sch_14``
     - SCH.14
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #876
   * - ``sch_15``
     - SCH.15
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #877
   * - ``sch_16``
     - SCH.16
     - List[:ref:`XCN <hl7-v2_3_1-XCN>`]
     - required
     - Item #885
   * - ``sch_17``
     - SCH.17
     - Optional[:ref:`XTN <hl7-v2_3_1-XTN>`]
     - optional
     - Item #886
   * - ``sch_18``
     - SCH.18
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #887
   * - ``sch_19``
     - SCH.19
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #888
   * - ``sch_20``
     - SCH.20
     - List[:ref:`XCN <hl7-v2_3_1-XCN>`]
     - required
     - Item #878
   * - ``sch_21``
     - SCH.21
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #879
   * - ``sch_22``
     - SCH.22
     - Optional[:ref:`PL <hl7-v2_3_1-PL>`]
     - optional
     - Item #880
   * - ``sch_23``
     - SCH.23
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #881
   * - ``sch_24``
     - SCH.24
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #882
   * - ``sch_25``
     - SCH.25
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #889 | Table HL70278

.. _hl7-v2_3_1-SPR:

SPR SPR - stored procedure request definition segment (S2.24.20).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.SPR.SPR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``spr_1``
     - SPR.1
     - Optional[str]
     - optional
     - Item #696
   * - ``spr_2``
     - SPR.2
     - str
     - required
     - Item #697 | Table HL70106
   * - ``spr_3``
     - SPR.3
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #704
   * - ``spr_4``
     - SPR.4
     - Optional[List[:ref:`QIP <hl7-v2_3_1-QIP>`]]
     - optional
     - Item #705

.. _hl7-v2_3_1-STF:

STF STF - staff identification segment (S8.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.STF.STF
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
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #671
   * - ``stf_2``
     - STF.2
     - Optional[List[:ref:`CX <hl7-v2_3_1-CX>`]]
     - optional
     - Item #672
   * - ``stf_3``
     - STF.3
     - Optional[List[:ref:`XPN <hl7-v2_3_1-XPN>`]]
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #110
   * - ``stf_7``
     - STF.7
     - Optional[str]
     - optional
     - Item #675 | Table HL70183
   * - ``stf_8``
     - STF.8
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #676 | Table HL70184
   * - ``stf_9``
     - STF.9
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #677 | Table HL70069
   * - ``stf_10``
     - STF.10
     - Optional[List[:ref:`XTN <hl7-v2_3_1-XTN>`]]
     - optional
     - Item #678
   * - ``stf_11``
     - STF.11
     - Optional[List[:ref:`XAD <hl7-v2_3_1-XAD>`]]
     - optional
     - Item #679
   * - ``stf_12``
     - STF.12
     - Optional[List[:ref:`DIN <hl7-v2_3_1-DIN>`]]
     - optional
     - Item #680
   * - ``stf_13``
     - STF.13
     - Optional[List[:ref:`DIN <hl7-v2_3_1-DIN>`]]
     - optional
     - Item #681
   * - ``stf_14``
     - STF.14
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #682
   * - ``stf_15``
     - STF.15
     - Optional[List[str]]
     - optional
     - Item #683
   * - ``stf_16``
     - STF.16
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #684 | Table HL70185
   * - ``stf_17``
     - STF.17
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #119 | Table HL70002
   * - ``stf_18``
     - STF.18
     - Optional[str]
     - optional
     - Item #785
   * - ``stf_19``
     - STF.19
     - Optional[:ref:`JCC <hl7-v2_3_1-JCC>`]
     - optional
     - Item #786 | Table HL70327
   * - ``stf_20``
     - STF.20
     - Optional[str]
     - optional
     - Item #1276 | Table HL70066
   * - ``stf_21``
     - STF.21
     - Optional[str]
     - optional
     - Item #1275 | Table HL70136
   * - ``stf_22``
     - STF.22
     - Optional[:ref:`DLN <hl7-v2_3_1-DLN>`]
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

.. _hl7-v2_3_1-TXA:

TXA Document notification segment (S9.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.TXA.TXA
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
     - str
     - required
     - Item #915 | Table HL70270
   * - ``txa_3``
     - TXA.3
     - Optional[str]
     - optional
     - Item #916 | Table HL70191
   * - ``txa_4``
     - TXA.4
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #917
   * - ``txa_5``
     - TXA.5
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #918
   * - ``txa_6``
     - TXA.6
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #919
   * - ``txa_7``
     - TXA.7
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #920
   * - ``txa_8``
     - TXA.8
     - Optional[List[:ref:`TS <hl7-v2_3_1-TS>`]]
     - optional
     - Item #921
   * - ``txa_9``
     - TXA.9
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #922
   * - ``txa_10``
     - TXA.10
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #923
   * - ``txa_11``
     - TXA.11
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #924
   * - ``txa_12``
     - TXA.12
     - :ref:`EI <hl7-v2_3_1-EI>`
     - required
     - Item #925
   * - ``txa_13``
     - TXA.13
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
     - optional
     - Item #926
   * - ``txa_14``
     - TXA.14
     - Optional[List[:ref:`EI <hl7-v2_3_1-EI>`]]
     - optional
     - Item #216
   * - ``txa_15``
     - TXA.15
     - Optional[:ref:`EI <hl7-v2_3_1-EI>`]
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
     - Optional[List[:ref:`PPN <hl7-v2_3_1-PPN>`]]
     - optional
     - Item #934
   * - ``txa_23``
     - TXA.23
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #935

.. _hl7-v2_3_1-UB1:

UB1 UB1 - UB82 data segment (S6.4.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.UB1.UB1
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
     - Item #531
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
     - Optional[List[:ref:`UVC <hl7-v2_3_1-UVC>`]]
     - optional
     - Item #539 | Table HL70153
   * - ``ub1_11``
     - UB1.11
     - Optional[str]
     - optional
     - Item #540
   * - ``ub1_12``
     - UB1.12
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #541 | Table HL70348
   * - ``ub1_13``
     - UB1.13
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #542 | Table HL70349
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
     - Optional[List[:ref:`OCD <hl7-v2_3_1-OCD>`]]
     - optional
     - Item #545 | Table HL70350
   * - ``ub1_17``
     - UB1.17
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #546 | Table HL70351
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

.. _hl7-v2_3_1-UB2:

UB2 UB2 - UB92 data segment (S6.4.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.UB2.UB2
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
     - Optional[List[:ref:`UVC <hl7-v2_3_1-UVC>`]]
     - optional
     - Item #558 | Table HL70153
   * - ``ub2_7``
     - UB2.7
     - Optional[List[:ref:`OCD <hl7-v2_3_1-OCD>`]]
     - optional
     - Item #559 | Table HL70350
   * - ``ub2_8``
     - UB2.8
     - Optional[List[:ref:`OSP <hl7-v2_3_1-OSP>`]]
     - optional
     - Item #560 | Table HL70351
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

.. _hl7-v2_3_1-URD:

URD URD - results/update definition segment (S2.24.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.URD.URD
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #45
   * - ``urd_2``
     - URD.2
     - Optional[str]
     - optional
     - Item #46 | Table HL70109
   * - ``urd_3``
     - URD.3
     - List[:ref:`XCN <hl7-v2_3_1-XCN>`]
     - required
     - Item #47
   * - ``urd_4``
     - URD.4
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
     - optional
     - Item #48 | Table HL70048
   * - ``urd_5``
     - URD.5
     - Optional[List[:ref:`CE <hl7-v2_3_1-CE>`]]
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

.. _hl7-v2_3_1-URS:

URS URS - unsolicited selection segment (S2.24.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.URS.URS
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
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #53
   * - ``urs_3``
     - URS.3
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
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
   * - ``urs_9``
     - URS.9
     - Optional[:ref:`TQ <hl7-v2_3_1-TQ>`]
     - optional
     - Item #695

.. _hl7-v2_3_1-VAR:

VAR Variance (S12.3.5).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.VAR.VAR
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
     - :ref:`EI <hl7-v2_3_1-EI>`
     - required
     - Item #1212
   * - ``var_2``
     - VAR.2
     - :ref:`TS <hl7-v2_3_1-TS>`
     - required
     - Item #1213
   * - ``var_3``
     - VAR.3
     - Optional[:ref:`TS <hl7-v2_3_1-TS>`]
     - optional
     - Item #1214
   * - ``var_4``
     - VAR.4
     - Optional[List[:ref:`XCN <hl7-v2_3_1-XCN>`]]
     - optional
     - Item #1215
   * - ``var_5``
     - VAR.5
     - Optional[:ref:`CE <hl7-v2_3_1-CE>`]
     - optional
     - Item #1216
   * - ``var_6``
     - VAR.6
     - Optional[List[str]]
     - optional
     - Item #1217

.. _hl7-v2_3_1-VTQ:

VTQ VTQ - virtual table query request segment (S2.24.17).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3_1.segments.VTQ.VTQ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``vtq_1``
     - VTQ.1
     - Optional[str]
     - optional
     - Item #696
   * - ``vtq_2``
     - VTQ.2
     - str
     - required
     - Item #697 | Table HL70106
   * - ``vtq_3``
     - VTQ.3
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #698
   * - ``vtq_4``
     - VTQ.4
     - :ref:`CE <hl7-v2_3_1-CE>`
     - required
     - Item #699
   * - ``vtq_5``
     - VTQ.5
     - Optional[List[:ref:`QSC <hl7-v2_3_1-QSC>`]]
     - optional
     - Item #700
