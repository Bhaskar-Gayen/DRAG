from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.document import Document
from schemas.document import DocumentCreate, DocumentResponse, DocumentMetadata
from datetime import datetime


def store_metadata(db: Session, document: DocumentMetadata, username: str) -> DocumentResponse:
    """
    Store document metadata in the database.

    Args:
        db (Session): SQLAlchemy session.
        document (DocumentCreate): Document data to be stored.
        username (str): The user ID to associate the document with.

    Returns:
        DocumentResponse: The document data including ID and upload time.
    """
    try:
        # Create a new Document instance
        db_document = Document(
            filename=document.filename,
            username=username,
            s3_url=document.s3_url,
            uploaded_at=datetime.now()
        )

        # Add the document to the session and commit to the database
        db.add(db_document)
        db.commit()

        # Refresh to get the new document's ID
        db.refresh(db_document)

        # Return the document metadata as a response schema
        return DocumentResponse(
            id=db_document.id,
            filename=db_document.filename,
            s3_url=db_document.s3_url,
            uploaded_at=db_document.uploaded_at,
            username=db_document.username
        )
    except SQLAlchemyError as e:
        db.rollback()  # Rollback the transaction in case of error
        raise e


def get_user_documents(db: Session, username: str) -> list[DocumentMetadata]:
    """
    Get all documents associated with a specific user.

    Args:
        db (Session): SQLAlchemy session.
        username (str): The user ID whose documents to fetch.

    Returns:
        list[DocumentMetadata]: A list of document metadata.
    """
    try:
        # Query documents that belong to the user
        documents = db.query(Document).filter(
            Document.username == username).all()

        # Map the result to DocumentMetadata schema for response
        return [
            DocumentMetadata(
                id=doc.id,
                filename=doc.filename,
                s3_url=doc.s3_url,
                uploaded_at=doc.uploaded_at,
                username=doc.username
            )
            for doc in documents
        ]
    except SQLAlchemyError as e:
        raise e


def delete_metadata(db: Session, document_id: int) -> bool:
    """
    Delete a document's metadata from the database.

    Args:
        db (Session): SQLAlchemy session.
        document_id (int): The ID of the document to be deleted.

    Returns:
        bool: True if the deletion was successful, False otherwise.
    """
    try:
        # Query the document by its ID
        document = db.query(Document).filter(
            Document.id == document_id).first()

        if document is None:
            return False  # Document not found

        # Delete the document from the database
        db.delete(document)
        db.commit()

        return True
    except SQLAlchemyError as e:
        db.rollback()  # Rollback the transaction in case of error
        raise e
