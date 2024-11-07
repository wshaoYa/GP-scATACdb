from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DECIMAL, Text
from sqlalchemy.orm import relationship
from database import Base


class OverallData(Base):
    __tablename__ = "overall_data"

    id = Column(Integer, primary_key=True, nullable=False)
    geo_id = Column(String)
    pb_gene = Column(String)
    pb_ensembl = Column(String)
    n_sample = Column(Integer)
    celline = Column(String)
    method = Column(String)
    conditions = Column(String)
    accession = Column(String)
    datasource = Column(String)


class BarcodesMetaData(Base):
    __tablename__ = "barcodes_meta_data"

    id = Column(Integer, primary_key=True, nullable=False)
    barcode = Column(String, primary_key=True, nullable=False)
    nCount_peaks = Column(Integer)
    nFeature_peaks = Column(Integer)
    nucleosome_signal = Column(DECIMAL)
    nucleosome_percentile = Column(DECIMAL)
    tss_enrichment = Column(DECIMAL)
    tss_percentile = Column(DECIMAL)
    high_tss = Column(String)
    seurat_clusters = Column(Integer)
    sample_type = Column(String)
    nCount_RNA = Column(Integer)
    nFeature_RNA = Column(Integer)


class GeneActivityWT(Base):
    __tablename__ = "comb_norm_WT_mat"

    id = Column(Integer, primary_key=True, nullable=False)
    gene_symbol = Column(String, primary_key=True, nullable=False)
    cluster_0 = Column(DECIMAL)
    cluster_1 = Column(DECIMAL)
    cluster_2 = Column(DECIMAL)
    cluster_3 = Column(DECIMAL)
    cluster_4 = Column(DECIMAL)
    cluster_5 = Column(DECIMAL)
    cluster_6 = Column(DECIMAL)
    cluster_7 = Column(DECIMAL)


class GeneActivityKO(Base):
    __tablename__ = "comb_norm_KO_mat"

    id = Column(Integer, primary_key=True, nullable=False)
    gene_symbol = Column(String, primary_key=True, nullable=False)
    cluster_0 = Column(DECIMAL)
    cluster_1 = Column(DECIMAL)
    cluster_2 = Column(DECIMAL)
    cluster_3 = Column(DECIMAL)
    cluster_4 = Column(DECIMAL)
    cluster_5 = Column(DECIMAL)
    cluster_6 = Column(DECIMAL)
    cluster_7 = Column(DECIMAL)
