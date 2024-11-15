from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, status
from utility.security import verify_jwt
from services.s3_service import upload_file_to_s3, delete_file_from_s3
from services.document_service import store_metadata, get_user_documents, delete_metadata
from schemas.document import DocumentResponse, DocumentMetadata
from uuid import uuid4
from sqlalchemy.orm import Session
from core.dependencies import get_db

router = APIRouter()


@router.post("/upload", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
async def upload_document(db: Session = Depends(get_db), file: UploadFile = File(...), user=Depends(verify_jwt)):
    file_id = str(uuid4())
    filename = f"{file_id}_{file.filename}"
    s3_url = upload_file_to_s3(file, filename)

    if not s3_url:
        raise HTTPException(status_code=500, detail="File upload failed")

    metadata = DocumentMetadata(
        id=file_id, filename=filename, username=user['sub'], s3_url=s3_url)
    store_metadata(metadata)

    return {"filename": filename, "s3_url": s3_url}


@router.get("/documents", response_model=list[DocumentMetadata])
async def list_documents(db: Session = Depends(get_db), user=Depends(verify_jwt)):
    print(user['sub'])
    return get_user_documents(user['sub'])


@router.delete("/documents/{file_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_document(file_id: str, db: Session = Depends(get_db),  user=Depends(verify_jwt)):
    metadata = delete_metadata(file_id, user['sub'])
    if not metadata:
        raise HTTPException(status_code=404, detail="Document not found")

    if not delete_file_from_s3(metadata.filename):
        raise HTTPException(
            status_code=500, detail="Failed to delete document from S3")
    return {"detail": "Document deleted"}


@router.get("/foo")
def foo():
    return {"foo": "bar"}
