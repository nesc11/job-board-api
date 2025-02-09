from typing import Annotated

from fastapi import APIRouter, Query, status, HTTPException
from sqlmodel import select

from ..models import Job, JobCreate, JobPublic, JobUpdate
from ..dependencies import SessionDep

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/", response_model=list[JobPublic])
def read_jobs(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=10)] = 10,
):
    jobs = session.exec(select(Job).offset(offset).limit(limit)).all()
    return jobs


@router.post("/", response_model=JobPublic)
def create_job(
    job: JobCreate,
    session: SessionDep,
):
    db_job = Job.model_validate(job)
    session.add(db_job)
    session.commit()
    session.refresh(db_job)
    return db_job


@router.get("/{job_id}", response_model=JobPublic)
def read_job(
    job_id: int,
    session: SessionDep,
):
    job = session.get(Job, job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job not found"
        )
    return job


@router.patch("/{job_id}", response_model=JobPublic)
def update_job(
    job_id: int,
    job: JobUpdate,
    session: SessionDep,
):
    job_db = session.get(Job, job_id)
    if not job_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job not found"
        )
    job_data = job.model_dump(exclude_unset=True)
    job_db.sqlmodel_update(job_data)
    session.add(job_db)
    session.commit()
    session.refresh(job_db)
    return job_db


@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    session: SessionDep,
):
    job = session.get(Job, job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job not found"
        )
    session.delete(job)
    session.commit()
    return {"ok": True}
