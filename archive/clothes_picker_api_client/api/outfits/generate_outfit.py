from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.outfit_response import OutfitResponse
from ...models.recommendation_request import RecommendationRequest
from ...types import Response


def _get_kwargs(
    *,
    body: RecommendationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/outfits/recommend",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | OutfitResponse | None:
    if response.status_code == 200:
        response_200 = OutfitResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | OutfitResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendationRequest,
) -> Response[Any | OutfitResponse]:
    r"""Generate an AI Outfit Recommendation

     Asks the AI to generate an outfit based on date, weather, and user constraints.
    This is the \"Magic Button\" endpoint.

    Args:
        body (RecommendationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OutfitResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendationRequest,
) -> Any | OutfitResponse | None:
    r"""Generate an AI Outfit Recommendation

     Asks the AI to generate an outfit based on date, weather, and user constraints.
    This is the \"Magic Button\" endpoint.

    Args:
        body (RecommendationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OutfitResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendationRequest,
) -> Response[Any | OutfitResponse]:
    r"""Generate an AI Outfit Recommendation

     Asks the AI to generate an outfit based on date, weather, and user constraints.
    This is the \"Magic Button\" endpoint.

    Args:
        body (RecommendationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OutfitResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendationRequest,
) -> Any | OutfitResponse | None:
    r"""Generate an AI Outfit Recommendation

     Asks the AI to generate an outfit based on date, weather, and user constraints.
    This is the \"Magic Button\" endpoint.

    Args:
        body (RecommendationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OutfitResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
