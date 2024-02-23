import service.models
from db.database import get_db
from service import schemas, models


def create_resource(resource: schemas.ResourceCreate):
    db = next(get_db())
    db_resource = service.models.Resource(
        url=resource.url,
        keyword=resource.keyword,
        info=resource.info,
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource


def get_resource(keyword: str):
    db = next(get_db())
    if keyword:
        db_resource = db.query(models.Resource).filter(models.Resource.keyword.like("%" + keyword + "%")).all()
    else:
        db_resource = db.query(models.Resource).all()
    return db_resource
