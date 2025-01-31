# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ..commons.errors.access_denied_error import AccessDeniedError
from ..commons.errors.error import Error
from ..commons.errors.method_not_allowed_error import MethodNotAllowedError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.errors.unauthorized_error import UnauthorizedError
from ..commons.types.create_generation_request import CreateGenerationRequest
from ..commons.types.observation import Observation
from .types.generations import Generations
from .types.update_generation_request import UpdateGenerationRequest


class GenerationsClient:
    def __init__(
        self,
        *,
        environment: str,
        x_langfuse_sdk_name: typing.Optional[str] = None,
        x_langfuse_sdk_version: typing.Optional[str] = None,
        username: str,
        password: str,
    ):
        self._environment = environment
        self.x_langfuse_sdk_name = x_langfuse_sdk_name
        self.x_langfuse_sdk_version = x_langfuse_sdk_version
        self._username = username
        self._password = password

    def log(self, *, request: CreateGenerationRequest) -> Observation:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", "api/public/generations"),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers(
                {"X-Langfuse-Sdk-Name": self.x_langfuse_sdk_name, "X-Langfuse-Sdk-Version": self.x_langfuse_sdk_version}
            ),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Observation, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(self, *, request: UpdateGenerationRequest) -> Observation:
        _response = httpx.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._environment}/", "api/public/generations"),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers(
                {"X-Langfuse-Sdk-Name": self.x_langfuse_sdk_name, "X-Langfuse-Sdk-Version": self.x_langfuse_sdk_version}
            ),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Observation, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
    ) -> Generations:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", "api/public/generations"),
            params={"page": page, "limit": limit, "name": name},
            headers=remove_none_from_headers(
                {"X-Langfuse-Sdk-Name": self.x_langfuse_sdk_name, "X-Langfuse-Sdk-Version": self.x_langfuse_sdk_version}
            ),
            auth=(self._username, self._password)
            if self._username is not None and self._password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Generations, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncGenerationsClient:
    def __init__(
        self,
        *,
        environment: str,
        x_langfuse_sdk_name: typing.Optional[str] = None,
        x_langfuse_sdk_version: typing.Optional[str] = None,
        username: str,
        password: str,
    ):
        self._environment = environment
        self.x_langfuse_sdk_name = x_langfuse_sdk_name
        self.x_langfuse_sdk_version = x_langfuse_sdk_version
        self._username = username
        self._password = password

    async def log(self, *, request: CreateGenerationRequest) -> Observation:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment}/", "api/public/generations"),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers(
                    {
                        "X-Langfuse-Sdk-Name": self.x_langfuse_sdk_name,
                        "X-Langfuse-Sdk-Version": self.x_langfuse_sdk_version,
                    }
                ),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Observation, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(self, *, request: UpdateGenerationRequest) -> Observation:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PATCH",
                urllib.parse.urljoin(f"{self._environment}/", "api/public/generations"),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers(
                    {
                        "X-Langfuse-Sdk-Name": self.x_langfuse_sdk_name,
                        "X-Langfuse-Sdk-Version": self.x_langfuse_sdk_version,
                    }
                ),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Observation, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
    ) -> Generations:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment}/", "api/public/generations"),
                params={"page": page, "limit": limit, "name": name},
                headers=remove_none_from_headers(
                    {
                        "X-Langfuse-Sdk-Name": self.x_langfuse_sdk_name,
                        "X-Langfuse-Sdk-Version": self.x_langfuse_sdk_version,
                    }
                ),
                auth=(self._username, self._password)
                if self._username is not None and self._password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Generations, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(str, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
