from fastapi import FastAPI
from pydantic import ValidationError
from sqlalchemy.exc import DatabaseError

from common.utils.app_response import AppErrorResponse
from .all_excepction_handler import all_exception_handler
from .database_error_handler import database_error_handler
from .generic_error_handler import generic_error_handler
from .validation_error_handler import validation_error_handler


def create_error_handlers(app: FastAPI):
    app.exception_handler(AppErrorResponse)(generic_error_handler)
    app.exception_handler(ValidationError)(validation_error_handler)
    app.exception_handler(Exception)(all_exception_handler)
    app.exception_handler(DatabaseError)(database_error_handler)
