import os

JWT_SECRET_KEY = os.environ['SLACKBOTR_SECRET_KEY']
JWT_ALGORITHM = 'HS256'

# Expiry is omitted for "never expires".
# JWT_EXPIRY_MINUTES = ?

# A JWT can contain any JSON-serializable data. This could be used, for example, to
# issue different tokens containing username, or containing role (e.g. read-only vs.
# read-write).
#
# WARNING: Don NOT put any sensitive data in the JWT_DATA object; it is NOT encrypted,
# only encoded.
#
# For now we only need one token:
JWT_DATA = 'slackbotr'
