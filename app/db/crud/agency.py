from db.models.agency import Agency
from schemas.agency import AgencyCreate
from sqlalchemy.orm import Session


def create_new_agency(agency: AgencyCreate, db: Session):
    agency_object = Agency(**agency.dict())
    db.add(agency_object)
    db.commit()
    db.refresh(agency_object)
    return agency_object


def retreive_agency(id: int, db: Session):
    item = db.query(Agency).filter(Agency.id == id).first()
    return item


def list_agencies(db: Session):
    agencies = db.query(Agency).all()
    return agencies


def update_agency_by_id(id: int, agency: AgencyCreate, db: Session):
    existing_agency = db.query(Agency).filter(Agency.id == id)
    if not existing_agency.first():
        return 0
    existing_agency.update(agency.__dict__)
    db.commit()
    return 1


def delete_agency_by_id(id: int, db: Session):
    existing_agency = db.query(Agency).filter(Agency.id == id)
    if not existing_agency.first():
        return 0
    existing_agency.delete(synchronize_session=False)
    db.commit()
    return 1


def search_agency(query: str, db: Session):
    agency = db.query(Agency).filter(Agency.nome_agencia.contains(query))
    return agency