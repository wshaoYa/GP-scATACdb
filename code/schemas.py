from pydantic import BaseModel

'''
分页
'''


# 分页paging
class Paging(BaseModel):
    start: int = 0
    length: int = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


'''
overall_data
'''


# 总体dataset
class OverallData(BaseModel):
    id: int
    geo_id: str
    pb_gene: str
    pb_ensembl: str
    n_sample: int
    celline: str
    method: str
    conditions: str
    accession: str
    datasource: str

    class Config:
        orm_mode = True


# 无id版本的 overall data
class OverallDataNoId(BaseModel):
    geo_id: str
    pb_gene: str
    pb_ensembl: str
    n_sample: int
    celline: str
    method: str
    conditions: str
    accession: str
    datasource: str

    class Config:
        orm_mode = True


# browser页filter
class BrowserFilter(BaseModel):
    id: int = None
    geo_id: str = None
    pb_gene: str = None
    pb_ensembl: str = None
    n_sample_greater: int = None
    n_sample_less: int = None
    celline: str = None
    method: str = None
    datasource: str = None


# 单个数据 resp
class SingleDataResponse(BaseModel):
    data: OverallDataNoId

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


'''
barcodes meta data
'''


# barcodes meta data
class BarcodesMetaData(BaseModel):
    id: int
    barcode: str
    nCount_peaks: int
    nFeature_peaks: int
    nucleosome_signal: float
    nucleosome_percentile: float
    tss_enrichment: float
    tss_percentile: float
    high_tss: str
    seurat_clusters: int
    sample_type: str
    nCount_RNA: int
    nFeature_RNA: int

    class Config:
        orm_mode = True


'''
gene activity
'''


# gene activity data
class GeneActivity(BaseModel):
    id: int
    gene_symbol: str
    cluster_0: float
    cluster_1: float
    cluster_2: float
    cluster_3: float
    cluster_4: float
    cluster_5: float
    cluster_6: float
    cluster_7: float

    class Config:
        orm_mode = True


'''
通用 resp
'''


# 分页表格 resp
class TableDataResponse(BaseModel):
    data: list[OverallData] | list[GeneActivity] | list[BarcodesMetaData] | list[object]
    records_sum: int

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# 枚举值 resp
class EnumDataResp(BaseModel):
    data: list[str] | list[object]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


'''
通用 request
'''


# download request
class DownloadRequest(BaseModel):
    id: int
    pb_gene: str
    celline: str
    filter: None = None
    seq: None = None
    paging: Paging = None
