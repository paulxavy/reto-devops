#!/usr/bin/env python3
import jwt
import uuid
import time
import os
import argparse

JWT_SECRET = os.getenv("JWT_SECRET", "mi_secret_seguro")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

def generate_jwt(exp_seconds=60):
    now = int(time.time())
    payload = {
        "jti": str(uuid.uuid4()),
        "iat": now,
        "nbf": now,
        "exp": now + exp_seconds,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    # In pyjwt>=2 encode returns str, else bytes
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    return token

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp", type=int, default=60, help="seconds before JWT expires")
    args = parser.parse_args()
    print(generate_jwt(args.exp))
