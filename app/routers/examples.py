import logging
from fastapi import APIRouter

from app.models.tasks import *
from app.models.jwt import *


router = APIRouter(
    prefix='/examples',
    tags=['examples'],
)


@router.get('/warning')
async def list_tasks():
    logging.warning('This is an example warning log')
    return 'warning logged'

@router.get('/error')
async def list_tasks():
    logging.error('This is an example error log')
    return 'error logged'

@router.get('/exception')
async def list_tasks():
    raise Exception('Intentional exception')

    return 'Exception raised' # unreachable code

