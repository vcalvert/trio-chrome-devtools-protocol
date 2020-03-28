# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.database
from cdp.database import (
    AddDatabase,
    Database,
    DatabaseId,
    Error
)


async def disable() -> None:
    '''
    Disables database tracking, prevents database events from being sent to the client.
    '''
    session = get_session_context('database.disable')
    return await session.execute(cdp.database.disable())


async def enable() -> None:
    '''
    Enables database tracking, database events will now be delivered to the client.
    '''
    session = get_session_context('database.enable')
    return await session.execute(cdp.database.enable())


async def execute_sql(
        database_id: DatabaseId,
        query: str
    ) -> typing.Tuple[typing.Optional[typing.List[str]], typing.Optional[typing.List[typing.Any]], typing.Optional[Error]]:
    '''
    :param database_id:
    :param query:
    :returns: A tuple with the following items:

        0. **columnNames** – 
        1. **values** – 
        2. **sqlError** – 
    '''
    session = get_session_context('database.execute_sql')
    return await session.execute(cdp.database.execute_sql(database_id, query))


async def get_database_table_names(
        database_id: DatabaseId
    ) -> typing.List[str]:
    '''
    :param database_id:
    :returns: 
    '''
    session = get_session_context('database.get_database_table_names')
    return await session.execute(cdp.database.get_database_table_names(database_id))
