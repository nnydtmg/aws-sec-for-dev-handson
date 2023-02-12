import secrets
import json
import base64
from datetime import datetime

def generate_session(username):
    ### Generate sessionID
    session_obj = {"username": username, "timestamp": datetime.now().isoformat(), "salt": secrets.token_urlsafe()}
    session_id = base64.b64encode(json.dumps(session_obj).encode("utf-8"))
    return session_id

def parse_session(session_obj):
    ### Parse sessionId
    session_obj = json.loads(base64.b64decode(session_obj).decode("utf-8"))
    return session_obj
