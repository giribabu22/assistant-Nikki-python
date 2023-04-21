# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Sequence,
    Tuple,
    Optional,
    Iterator,
)

from google.cloud.speech_v2.types import cloud_speech


class ListRecognizersPager:
    """A pager for iterating through ``list_recognizers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.speech_v2.types.ListRecognizersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``recognizers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRecognizers`` requests and continue to iterate
    through the ``recognizers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.speech_v2.types.ListRecognizersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_speech.ListRecognizersResponse],
        request: cloud_speech.ListRecognizersRequest,
        response: cloud_speech.ListRecognizersResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.speech_v2.types.ListRecognizersRequest):
                The initial request object.
            response (google.cloud.speech_v2.types.ListRecognizersResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_speech.ListRecognizersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_speech.ListRecognizersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[cloud_speech.Recognizer]:
        for page in self.pages:
            yield from page.recognizers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRecognizersAsyncPager:
    """A pager for iterating through ``list_recognizers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.speech_v2.types.ListRecognizersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``recognizers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRecognizers`` requests and continue to iterate
    through the ``recognizers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.speech_v2.types.ListRecognizersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_speech.ListRecognizersResponse]],
        request: cloud_speech.ListRecognizersRequest,
        response: cloud_speech.ListRecognizersResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.speech_v2.types.ListRecognizersRequest):
                The initial request object.
            response (google.cloud.speech_v2.types.ListRecognizersResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_speech.ListRecognizersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_speech.ListRecognizersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[cloud_speech.Recognizer]:
        async def async_generator():
            async for page in self.pages:
                for response in page.recognizers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCustomClassesPager:
    """A pager for iterating through ``list_custom_classes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.speech_v2.types.ListCustomClassesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``custom_classes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCustomClasses`` requests and continue to iterate
    through the ``custom_classes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.speech_v2.types.ListCustomClassesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_speech.ListCustomClassesResponse],
        request: cloud_speech.ListCustomClassesRequest,
        response: cloud_speech.ListCustomClassesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.speech_v2.types.ListCustomClassesRequest):
                The initial request object.
            response (google.cloud.speech_v2.types.ListCustomClassesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_speech.ListCustomClassesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_speech.ListCustomClassesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[cloud_speech.CustomClass]:
        for page in self.pages:
            yield from page.custom_classes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCustomClassesAsyncPager:
    """A pager for iterating through ``list_custom_classes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.speech_v2.types.ListCustomClassesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``custom_classes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCustomClasses`` requests and continue to iterate
    through the ``custom_classes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.speech_v2.types.ListCustomClassesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_speech.ListCustomClassesResponse]],
        request: cloud_speech.ListCustomClassesRequest,
        response: cloud_speech.ListCustomClassesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.speech_v2.types.ListCustomClassesRequest):
                The initial request object.
            response (google.cloud.speech_v2.types.ListCustomClassesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_speech.ListCustomClassesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_speech.ListCustomClassesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[cloud_speech.CustomClass]:
        async def async_generator():
            async for page in self.pages:
                for response in page.custom_classes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPhraseSetsPager:
    """A pager for iterating through ``list_phrase_sets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.speech_v2.types.ListPhraseSetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``phrase_sets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPhraseSets`` requests and continue to iterate
    through the ``phrase_sets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.speech_v2.types.ListPhraseSetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_speech.ListPhraseSetsResponse],
        request: cloud_speech.ListPhraseSetsRequest,
        response: cloud_speech.ListPhraseSetsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.speech_v2.types.ListPhraseSetsRequest):
                The initial request object.
            response (google.cloud.speech_v2.types.ListPhraseSetsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_speech.ListPhraseSetsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_speech.ListPhraseSetsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[cloud_speech.PhraseSet]:
        for page in self.pages:
            yield from page.phrase_sets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPhraseSetsAsyncPager:
    """A pager for iterating through ``list_phrase_sets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.speech_v2.types.ListPhraseSetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``phrase_sets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPhraseSets`` requests and continue to iterate
    through the ``phrase_sets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.speech_v2.types.ListPhraseSetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_speech.ListPhraseSetsResponse]],
        request: cloud_speech.ListPhraseSetsRequest,
        response: cloud_speech.ListPhraseSetsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.speech_v2.types.ListPhraseSetsRequest):
                The initial request object.
            response (google.cloud.speech_v2.types.ListPhraseSetsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_speech.ListPhraseSetsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_speech.ListPhraseSetsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[cloud_speech.PhraseSet]:
        async def async_generator():
            async for page in self.pages:
                for response in page.phrase_sets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
