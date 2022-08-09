import sqlalchemy

metadata = sqlalchemy.MetaData()

ipv4 = sqlalchemy.Table(
    "ipv4-by-date",
    metadata,
    sqlalchemy.Column("network", sqlalchemy.VARCHAR),
    sqlalchemy.Column("netmask", sqlalchemy.INTEGER),
    sqlalchemy.Column("addresses_count", sqlalchemy.INTEGER),
    sqlalchemy.Column("country", sqlalchemy.CHAR),
    sqlalchemy.Column("date_from", sqlalchemy.DATE),
    sqlalchemy.Column("date_to", sqlalchemy.DATE),
)

ipv6 = sqlalchemy.Table(
    "ipv6-by-date",
    metadata,
    sqlalchemy.Column("network", sqlalchemy.VARCHAR),
    sqlalchemy.Column("netmask", sqlalchemy.INTEGER),
    sqlalchemy.Column("addresses_count", sqlalchemy.INTEGER),
    sqlalchemy.Column("country", sqlalchemy.CHAR),
    sqlalchemy.Column("date_from", sqlalchemy.DATE),
    sqlalchemy.Column("date_to", sqlalchemy.DATE),
)

asinfo = sqlalchemy.Table(
    "as-info-v1",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR),
    sqlalchemy.Column("org", sqlalchemy.VARCHAR),
    sqlalchemy.Column("owner", sqlalchemy.VARCHAR),
    sqlalchemy.Column("country", sqlalchemy.CHAR),
)

providers = sqlalchemy.Table(
    "Providers",
    metadata,
    sqlalchemy.Column("ProviderID", sqlalchemy.INTEGER),
    sqlalchemy.Column("ProviderName", sqlalchemy.VARCHAR),
    sqlalchemy.Column("Organization", sqlalchemy.VARCHAR),
    sqlalchemy.Column("Description", sqlalchemy.VARCHAR),
    sqlalchemy.Column("CountryCode", sqlalchemy.CHAR),
)

prefix_count = sqlalchemy.Table(
    "as-prefix-count",
    metadata,
    sqlalchemy.Column("as_num", sqlalchemy.INTEGER),
    sqlalchemy.Column("company", sqlalchemy.VARCHAR),
    sqlalchemy.Column("description", sqlalchemy.VARCHAR),
    sqlalchemy.Column("prefixes", sqlalchemy.INTEGER),
)

as_neighbors = sqlalchemy.Table(
    "as_neighbors",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER),
    sqlalchemy.Column("as_num", sqlalchemy.INTEGER),
    sqlalchemy.Column("neighbors", sqlalchemy.TEXT),
)
