from os import environ
from alembic import context
from .models import ipv4, entries

config = context.config

section = config.config_ini_section
config.set_section_option(section, "DB_USER", environ.get("DB_USER"))
config.set_section_option(section, "DB_PASS", environ.get("DB_PASS"))
config.set_section_option(section, "DB_NAME", environ.get("DB_NAME"))
config.set_section_option(section, "DB_HOST", environ.get("DB_HOST"))

fileConfig(config.config_file_name)

target_metadata = [ipv4.metadata, entries.metadata]