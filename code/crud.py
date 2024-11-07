from fastapi import Query
from sqlalchemy.orm import Session
from sqlalchemy import func, desc, distinct
import models
from schemas import *

PAGING_START = 0
PAGING_LEN = 10

overall_data = models.OverallData
barcodes_meta_data = models.BarcodesMetaData
WT_gene_activity_data = models.GeneActivityWT
KO_gene_activity_data = models.GeneActivityKO
'''
通用
'''


def get_paging_attrs(paging: Paging) -> (int, int):
    if paging is not None:
        return paging.start, paging.length
    return PAGING_START, PAGING_LEN


def get_order_attr(model_name: str, seq: object):
    order_attr = None
    if seq is not None:
        for key, val in seq.dict().items():
            if val is not None:
                seq_key = eval(f'{model_name}.{key[:-4]}')  # 去除末尾_seq
                order_attr = seq_key if val == 1 else desc(seq_key)
    return order_attr


'''
db查询操作
'''


# 获取总体overall_data
def get_overall_data(db: Session, browser_filter: BrowserFilter = None, paging: Paging = None) -> (Query, int):
    filters = []
    if browser_filter is not None:
        if browser_filter.id is not None:
            filters.append(overall_data.id == browser_filter.id)
        if browser_filter.geo_id is not None:
            filters.append(overall_data.geo_id.like(f'%{browser_filter.geo_id}%'))
        if browser_filter.pb_gene is not None:
            filters.append(overall_data.pb_gene.like(f'%{browser_filter.pb_gene}%'))
        if browser_filter.pb_ensembl is not None:
            filters.append(overall_data.pb_ensembl.like(f'%{browser_filter.pb_ensembl}%'))
        if browser_filter.celline is not None:
            filters.append(overall_data.celline.like(f'%{browser_filter.celline}%'))
        if browser_filter.method is not None:
            filters.append(overall_data.method.like(f'%{browser_filter.method}%'))
        if browser_filter.datasource is not None:
            filters.append(overall_data.datasource.like(f'%{browser_filter.datasource}%'))
        if browser_filter.n_sample_greater is not None:
            filters.append(overall_data.n_sample >= browser_filter.n_sample_greater)
        if browser_filter.n_sample_less is not None:
            filters.append(overall_data.n_sample <= browser_filter.n_sample_less)

    paging_start, paging_len = get_paging_attrs(paging)

    query_data = db.query(overall_data).filter(*filters).offset(paging_start).limit(paging_len).all()
    records_sum = db.query(func.count(overall_data.id)).filter(*filters).scalar()

    return query_data, records_sum


# 获取cell meta data
def get_barcodes_meta_data(db: Session, paging: Paging = None) -> (Query, int):
    paging_start, paging_len = get_paging_attrs(paging)

    query_data = db.query(barcodes_meta_data).offset(paging_start).limit(paging_len).all()
    records_sum = db.query(func.count(barcodes_meta_data.id)).scalar()

    return query_data, records_sum


# 获取 WT gene activity
def get_WT_gene_activity(db: Session, paging: Paging = None) -> (Query, int):
    paging_start, paging_len = get_paging_attrs(paging)

    query_data = db.query(WT_gene_activity_data).offset(paging_start).limit(paging_len).all()
    records_sum = db.query(func.count(WT_gene_activity_data.id)).scalar()

    return query_data, records_sum


# 获取 KO gene activity
def get_KO_gene_activity(db: Session, paging: Paging = None) -> (Query, int):
    paging_start, paging_len = get_paging_attrs(paging)

    query_data = db.query(KO_gene_activity_data).offset(paging_start).limit(paging_len).all()
    records_sum = db.query(func.count(KO_gene_activity_data.id)).scalar()

    return query_data, records_sum
