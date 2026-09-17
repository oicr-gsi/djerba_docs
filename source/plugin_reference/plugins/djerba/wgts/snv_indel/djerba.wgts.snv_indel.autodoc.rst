==============================
djerba: wgts.snv_indel: v1.0.0
==============================


        * :ref:`djerba.wgts.snv_indel_summary`
        * :ref:`djerba.wgts.snv_indel_generic_params`
        * :ref:`djerba.wgts.snv_indel_specific_params`
        * :ref:`djerba.wgts.snv_indel_description`

        
For explanation of each section, see the main :ref:`plugin-reference` page.
        .. _djerba.wgts.snv_indel_summary:

***********************************
Summary
***********************************
The ``wgts.snv_indel`` plugin reports SNVs and indels in WGTS/WGS data.

It is important for displaying variants and identifying treatment options in clinical reporting.

Plugin actions include:

* Filtering the input data to discard unwanted variant calls
* Annotation of calls using `OncoKB`_ to find oncogenic status and treatment options, if any
* Computing the Loss of Heterozygosity (LOH) status for each variant
* Producing a table of data for each variant, and summary metrics for the genome
* Generating a histogram of variant allele frequency (VAF)
* Generating Integrative Genomics Viewer (IGV) links for the `OICR Whizbam server`_

.. _OICR Whizbam server : https://whizbam.oicr.on.ca/
.. _OncoKB: https://www.oncokb.org/

.. _djerba.wgts.snv_indel_specific_params:

***********************************
Specific Parameters
***********************************

=============== ======================================================= =====
Parameter       Default                                                 Notes
=============== ======================================================= =====
apply cache     False                                                        
maf_path        N/A                                                          
normal_id       N/A                                                          
oncokb cache    /.mounts/labs/CGI/gsi/tools/djerba/oncokb_cache/scratch      
oncotree_code   N/A                                                          
project         N/A                                                          
tumour_id       N/A                                                          
update cache    False                                                        
whizbam_project N/A                                                          
=============== ======================================================= =====


.. _djerba.wgts.snv_indel_generic_params:

***********************************
Generic Parameters
***********************************

================== ======== =====
Parameter          Default  Notes
================== ======== =====
attributes         clinical      
configure_priority 700           
depends_configure  (empty)       
depends_extract    (empty)       
extract_priority   800           
render_priority    700           
================== ======== =====


.. _djerba.wgts.snv_indel_description:

***********************************
Description
***********************************


Prerequisites
=============

The following Python libraries are used for plotting:

* `pandas`_
* `matplotlib`_
* `seaborn`_

.. _pandas: https://pandas.pydata.org/
.. _matplotlib: https://matplotlib.org/
.. _seaborn: https://seaborn.pydata.org/

Input
=====

Required
--------

A gzip-compressed MAF file with extension ``.maf.gz``, as output by the `variantEffectPredictor`_ workflow.

.. _variantEffectPredictor: https://github.com/oicr-gsi/variantEffectPredictor

Optional
--------

If the Djerba `expression helper`_ has written output to the workspace, it will be used to display gene expression metrics.

.. _expression helper: https://github.com/oicr-gsi/djerba/tree/main/src/lib/djerba/helpers/expression_helper
.. TODO link to expression helper documentation when available

Data Processing
===============

Filtering
---------

Rows from the input MAF file are `filtered`_ using a strict set of criteria, which typically discards >99.9% of inputs.

Filtering is based on column values from the MAF file, such as ``t_depth``. Consult the `MAF documentation`_ for further details.

A MAF input row is **kept** for downstream analysis if **all** of the following statements are true:

1. ``t_depth >= 1``
2. ``t_alt_count >= 3``
3. Above the minimum VAF threshold: ``t_alt_count/t_depth >= 0.1``
4. Either of the following is true:

   1. ``Matched_Norm_Sample_Barcode`` is **not** ``unmatched``, *OR*
   2. ``gnomAD_AF`` is non-empty and less than 0.001

5. ``biotype`` is ``protein_coding``
6. ``variant_classification`` is any of:

   1. ``5'Flank``
   2. ``Frame_Shift_Del``
   3. ``Frame_Shift_Ins``
   4. ``In_Frame_Del``
   5. ``In_Frame_Ins``
   6. ``Missense_Mutation``
   7. ``Nonsense_Mutation``
   8. ``Nonstop_Mutation``
   9. ``Silent``
   10. ``Splice_Region``
   11. ``Splice_Site``
   12. ``Targeted_Region``
   13. ``Translation_Start_Site``

7. Flags in ``FILTER`` do **not** include:

   1. ``str_contraction``, *OR*
   2. ``t_lod_fstar``

8. Either of the following is true:

   1. ``variant_classification`` is **not** ``5'Flank``, *OR*
   2. ``hugo_symbol`` is ``TERT``

9. Either of the following is true:

   1. ``hugo_symbol`` is **not** ``TERT``, *OR*
   2. The variant is **not** either of the following "*TERT* hotspots":

      1. nucleotide polymorphism G > A (chr5, 1295113 assembly GRCh38), *OR*
      2. nucleotide polymorphism G > A (chr5, 1295135 assembly GRCh38)

.. _filtered: https://github.com/oicr-gsi/djerba/blob/a45e70a30485bb415723d019b47fdfc6400e7775/src/lib/djerba/plugins/wgts/snv_indel/tools.py#L85
.. _MAF documentation: https://docs.gdc.cancer.gov/Data/File_Formats/MAF_Format/

Variant Annotation
------------------

Somatic mutations are annotated using `OncoKB`_, as described in the `Djerba documentation`_.

`OncoKB`_ categorizes mutations by the level of evidence they are oncogenic; and identifies treatment options, if known.

.. _Djerba documentation: https://djerba.readthedocs.io/en/latest/user_guide/user_guide.html#variant-annotation
.. _OncoKB: https://www.oncokb.org/


Loss of Heterozygosity
----------------------

We define the following quantities:

* *p* = sample purity
* *v* = tumour VAF
* *n* = copy number, ``CN`` column in the MAF file
* *m* = minor allele copy number, ``MACN`` column in the MAF file

`Loss of heterozygosity`_ (LOH) occurs when **both** of the following statements are true:

.. math::

   \frac{vn}{p} > n - 0.5
   
.. math::

   m \le 0.5

.. _Loss of heterozygosity: https://github.com/oicr-gsi/djerba/blob/a45e70a30485bb415723d019b47fdfc6400e7775/src/lib/djerba/plugins/wgts/snv_indel/tools.py#L139


Special Cases for Protein Names
-------------------------------

If the input MAF file lists the gene as *BRAF* and the protein as p.V640E, the protein name is changed to p.V600E for output.

For splice site mutations, the protein is denoted by the HGVS coding sequence name, in the ``HGVSc`` column of the MAF file.


Downstream Dependency for TMB
-----------------------------

The  `genomic landscape plugin`_ uses the ``data_mutations_extended.txt`` file written to the workspace by this plugin, in order to compute tumour mutation burden (TMB).

The following ``variant_classification`` values are *included* by the MAF filter, but *excluded* from TMB in the `genomic landscape plugin`_.

1. ``3'Flank``
2. ``3'UTR``
3. ``5'Flank``
4. ``5'UTR``
5. ``Silent``
6. ``Splice_Region``
7. ``Targeted_Region``

.. _genomic landscape plugin: https://github.com/oicr-gsi/djerba/tree/main/src/lib/djerba/plugins/genomic_landscape

.. TODO make a note of this in genomic_landscape documentation

Output
======

Summary metrics
---------------

* Total somatic mutations
* Total coding sequence mutations
* Total oncogenic mutations as identified by OncoKB

Table columns
-------------

The output table reports any variants with an OncoKB category of N2 (Likely Oncogenic) or higher.

1. Gene name and link to OncoKB
2. Chromosome and chromosomal arm
3. Protein name and link to OncoKB
4. Type of mutation
5. Variant Allele Frequency (VAF)
6. Depth: Variant reads / Total reads
7. Percentile of expression, computed in TPM (transcripts per million) with reference to the TCGA cohort. Not available in WGS reports.
8. LOH: True or False
9. OncoKB level

Plots
-------

* Histogram of VAF for all somatic mutations

Whizbam Links
-------------

The plugin generates Integrative Genomics Viewer (IGV) links for the `OICR Whizbam server`_, and inserts them as the final column in ``data_mutations_extended.txt`` and ``data_mutations_extended_oncogenic.txt``.

.. _OICR Whizbam server : https://whizbam.oicr.on.ca/

Workspace Files
----------------

The following files are written to the workspace, from earliest to latest:

1. ``filtered_maf.tsv``: Variants after initial filtering of the input MAF file
2. ``oncokb_clinical_info.txt``: File with the sample ID and Oncotree code, used as argument to the oncokb-annotator scripts
3. ``annotated_maf.tsv``: Variants from ``filtered_maf.tsv``, with annotation by onckb-annotator
4. ``data_mutations_extended.txt``: Variants from ``annotated_maf.tsv``, with Whizbam links
5. ``data_mutations_extended_oncogenic.txt``: As above, but for oncogenic mutations only
6. ``vaf_plot.svg``: VAF histogram for the report
7. ``whizbam_all.txt``: Whizbam column from ``data_mutations_extended_oncogenic.txt``, copied to a separate file for easier reading
8. ``whizbam_oncogenic.txt``: As above, but for oncogenic mutations only


Example Report Output
---------------------

.. image:: wgts.snv_indel_output.png

**Figure 1**: Example output from the wgts.snv_indel plugin. Expression values are omitted because this was a WGS report.

