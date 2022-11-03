"""Model logic for the users domain."""

from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from structlog import get_logger

from lms.api.v1 import fields
from lms.domain.generic.service import GenericService
from lms.domain.repositories import exceptions
from lms.utils.jwt import create_access_token, create_refresh_token
from lms.utils.password import verify_password, get_hashed_password

logger = get_logger(__name__)


class UsersService(GenericService[fields.AdminOut, fields.AdminCreate, fields.AdminUpdate]):

    async def exist(self, *args):
        """
        """
        return await self.table.find_one(*args)

    async def create(self, data_object: fields.AdminCreate, **kwargs) -> fields.AdminOut:
        """Create a user.
        Args:
            data_object (AdminCreate): input data.
        Returns:
            AdminOut: representation of the created user.
        """
        # user = await self.exist(self.table.email == data_object.email)
        # if user:
        #     raise exceptions.DoesExistError(message=f"User with {data_object.email} exists")

        data_object.password = get_hashed_password(data_object.password)
        logger.info("Creating admin", data=data_object.to_dict())
        try:
            return await super().create(data_object, exclude={'password'})
        except DuplicateKeyError:
            raise exceptions.DoesExistError(message=f"User with {data_object.email} exists")

    async def login(self, username: str, password: str) -> fields.AuthToken:
        admin_exists = await self.exist(self.table.email == username)

        if not admin_exists:
            raise exceptions.DoesNotExistError(message="Incorrect email or password")

        password = verify_password(password, admin_exists.password)

        if not password:
            raise exceptions.DoesNotExistError(message="Incorrect email or password")

        return fields.AuthToken(**{
            "email": admin_exists.email,
            "full_name": admin_exists.full_name,
            "access_token": create_access_token(username),
            "refresh_token": create_refresh_token(username),
        })
