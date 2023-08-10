import typing
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from pydantic import BaseModel, AnyUrl, EmailStr
from auth0.v3.exceptions import Auth0Error

from project_snow.security.funcs import verify_token
from project_snow.core.dependencies import get_auth0_users_client, get_auth0_management_client, authentication, management
from project_snow.core.config import get_settings, Settings


router = APIRouter()

settings: Settings = get_settings()

@router.get("/me")
async def read_user_me(
    access_token: str = Depends(verify_token), 
    auth0_users: authentication.Users = Depends(get_auth0_users_client)
) -> dict:
    try:
        userinfo = auth0_users.userinfo(access_token=access_token)   
    except Auth0Error as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)
    return userinfo

@router.post("/")
async def create_new_user(
    create_user: CreateUser,
    auth0_mgmt_client: management.Auth0 = Depends(get_auth0_management_client)
):
    """
    Create user in auth0.
    if verify_email=True -> send verification mail
    """
    # Create user in auth0 db
    try:
        response = auth0_mgmt_client.users.create(
            body=create_user.dict(exclude_none=True)
        )
    except Auth0Error as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)
    return  response

@router.delete("/{user_id}", dependencies=[Depends(verify_token)])
async def delete_user(
    user_id: str,
    auth0_mgmt_client: management.Auth0 = Depends(get_auth0_management_client)
):
    """
    Remove user from auth0.
    """
    try:
        response = auth0_mgmt_client.users.delete(id=user_id)
    except Auth0Error as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)
    return {
        "auth0": response
    }