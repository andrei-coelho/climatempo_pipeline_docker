from util.config import get_session 
from sqlalchemy.orm import Session

def config():
    print("get_session: ", isinstance(get_session(), Session))