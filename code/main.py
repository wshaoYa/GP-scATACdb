from datetime import datetime
from fastapi import Depends, FastAPI, Body, HTTPException
from sqlalchemy.orm import Session
# from fastapi.responses import FileResponse
from starlette.responses import FileResponse
import sys
import crud
import models
from database import SessionLocal, engine
from schemas import *
import pandas
import os, tarfile
import paramiko
from scp import SCPClient, SCPException
import subprocess

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


'''
get系列
'''


@app.post("/get_overall_data", response_model=TableDataResponse)
def get_overall_data(db: Session = Depends(get_db), filter: BrowserFilter = None, paging: Paging = None):
    data, records_sum = crud.get_overall_data(db, filter, paging)
    overall_data = TableDataResponse(data=data, records_sum=records_sum)

    for i in range(len(overall_data.data)):
        GSE_id = overall_data.data[i].accession.split('acc=')[1]
        overall_data.data[i].accession = f"<a href='{overall_data.data[i].accession}' target='_blank'>{GSE_id}</a>"
    return overall_data


@app.post("/get_barcodes_meta_data", response_model=TableDataResponse)
def get_barcodes_meta_data(db: Session = Depends(get_db), paging: Paging = None):
    data, records_sum = crud.get_barcodes_meta_data(db, paging)
    barcodes_meta_data = TableDataResponse(data=data, records_sum=records_sum)
    return barcodes_meta_data


@app.post("/get_WT_gene_activity", response_model=TableDataResponse)
def get_WT_gene_activity(db: Session = Depends(get_db), paging: Paging = None):
    data, records_sum = crud.get_WT_gene_activity(db, paging)
    WT_gene_activity_data = TableDataResponse(data=data, records_sum=records_sum)
    return WT_gene_activity_data


@app.post("/get_KO_gene_activity", response_model=TableDataResponse)
def get_KO_gene_activity(db: Session = Depends(get_db), paging: Paging = None):
    data, records_sum = crud.get_KO_gene_activity(db, paging)
    KO_gene_activity_data = TableDataResponse(data=data, records_sum=records_sum)
    return KO_gene_activity_data
