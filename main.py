from fastapi import FastAPI
from db import database
from sqlalchemy.sql.expression import select
from models import ipv4, ipv6, asinfo, providers, prefix_count, as_neighbors
import uvicorn
import re


app = FastAPI(title="Ifreedomlab_api")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/api/ipv4@limit={limit}&offset={offset}")
async def get_ipv4(limit,offset):
    query=(
        select (
            [
                ipv4.c.network,
                ipv4.c.netmask,
                ipv4.c.addresses_count,
                ipv4.c.country,
                ipv4.c.date_from,
                ipv4.c.date_to
            ]
        )
        .limit(limit)
        .offset(offset)
        # .where(ipv4.c.date_from > '2021-01-01')
    )
    return await database.fetch_all(query)

@app.get("/api/ipv6@limit={limit}&offset={offset}")
async def get_ipv6(limit,offset):
    query=(
        select (
            [
                ipv6.c.network,
                ipv6.c.netmask,
                ipv6.c.addresses_count,
                ipv6.c.country,
                ipv6.c.date_from,
                ipv6.c.date_to
            ]
        )
        .limit(limit)
        .offset(offset)
        # .where(ipv6.c.date_from > '2021-05-01')
    )
    return await database.fetch_all(query)

@app.get("/api/asinfo@limit={limit}&offset={offset}")
async def get_asinfo(limit,offset):
    query=(
        select (
            [
                asinfo.c.id,
                asinfo.c.name,
                asinfo.c.org,
                asinfo.c.owner,
                asinfo.c.country
            ]
        )
        .limit(limit)
        .offset(offset)
    )
    return await database.fetch_all(query)

@app.get("/api/providers@limit={limit}&offset={offset}")
async def get_providers(limit,offset):
    query=(
        select (
            [
                providers.c.ProviderID,
                providers.c.ProviderName,
                providers.c.Organization,
                providers.c.Description,
                providers.c.CountryCode
            ]
        )
        .limit(limit)
        .offset(offset)
    )
    return await database.fetch_all(query)

@app.get("/api/as-prefix-count@limit={limit}&offset={offset}")
async def get_prefixes(limit,offset):
    query=(
        select (
            [
                prefix_count.c.as_num,
                prefix_count.c.company,
                prefix_count.c.description,
                prefix_count.c.prefixes
            ]
        )
        .limit(limit)
        .offset(offset)
    )
    return await database.fetch_all(query)

@app.get("/api/as_neighbors@as={as_num}")
async def get_neighbors(as_num):
    query=(select([as_neighbors.c.neighbors]).where(as_neighbors.c.as_num == as_num))
    result = await database.fetch_all(query)
    find_all = re.findall(r"\d+", str(result[0]))
    query2=(
        select (
            [
                asinfo.c.id,
                asinfo.c.name,
                asinfo.c.owner
            ]
        )
        .where(asinfo.c.id.in_(find_all)))
    return await database.fetch_all(query2)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3434, log_level="info")

