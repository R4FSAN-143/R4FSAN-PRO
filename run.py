# Encoded By RAFSAN AHAMMED RAFI
# WhatsApp +8801305504954
# https://github.com/R4FSAN-143

import marshal, base64, zlib

exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))