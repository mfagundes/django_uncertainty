from django.test import TestCase
from unittest.mock import MagicMock, patch

from uncertainty.behaviours import (Behaviour, default, HttpResponseBehaviour, html, ok,
                                    bad_request, forbidden, not_allowed, server_error, not_found)


class BehaviourTests(TestCase):
    def setUp(self):
        self.get_response_mock = MagicMock()
        self.request_mock = MagicMock()
        self.behaviour = Behaviour()

    def test_calls_get_response(self):
        """Tests that invoking the behaviour calls get_response"""
        self.behaviour(self.get_response_mock, self.request_mock)
        self.get_response_mock.assert_called_once_with(self.request_mock)

    def test_returns_get_response_result(self):
        """Tests that the behaviour returns the result of calling get_response"""
        self.assertEqual(self.get_response_mock.return_value,
                         self.behaviour(self.get_response_mock, self.request_mock))


class DefaultTests(TestCase):
    def test_default_is_behaviour_base(self):
        """Test that default is the Behaviour base class"""
        self.assertEqual(default, Behaviour)


class HttpResponseBehaviourTests(TestCase):
    def setUp(self):
        self.get_response_mock = MagicMock()
        self.request_mock = MagicMock()
        self.response_class_mock = MagicMock()
        self.args_mock = [MagicMock(), MagicMock()]
        self.kwargs_mock = {'kwarg0': MagicMock(), 'kwarg1': MagicMock()}
        self.behaviour = HttpResponseBehaviour(self.response_class_mock, *self.args_mock,
                                               **self.kwargs_mock)

    def test_calls_response_class_constructor(self):
        """Tests that invoking the behaviour calls response class constructor"""
        self.behaviour(self.get_response_mock, self.request_mock)
        self.response_class_mock.assert_called_once_with(*self.args_mock, **self.kwargs_mock)

    def test_returns_response_class_constructor_result(self):
        """Tests that the behaviour returns the result of calling the response class constructor"""
        self.assertEqual(self.response_class_mock.return_value,
                         self.behaviour(self.get_response_mock, self.request_mock))


class HttpResponseBehaviourTestsBase(TestCase):
    def setUp(self):
        http_response_behaviour_patcher = patch('uncertainty.behaviours.HttpResponseBehaviour')
        self.http_response_behaviour_mock = http_response_behaviour_patcher.start()
        self.addCleanup(http_response_behaviour_patcher.stop)
        self.args_mock = [MagicMock(), MagicMock()]
        self.kwargs_mock = {'kwarg0': MagicMock(), 'kwarg1': MagicMock()}


class HtmlTests(HttpResponseBehaviourTestsBase):
    def setUp(self):
        super().setUp()
        http_response_patcher = patch('uncertainty.behaviours.HttpResponse')
        self.http_response_mock = http_response_patcher.start()
        self.addCleanup(http_response_patcher.stop)

    def test_calls_http_response_behaviour(self):
        """Tests that html calls HttpResponseBehaviour with HttpResponse"""
        html(*self.args_mock, **self.kwargs_mock)
        self.http_response_behaviour_mock.assert_called_once_with(self.http_response_mock,
                                                                  *self.args_mock,
                                                                  **self.kwargs_mock)

    def test_returns_http_response_behaviour_result(self):
        """Tests that html returns the result of calling HttpResponseBehaviour constructor"""
        self.assertEqual(self.http_response_behaviour_mock.return_value,
                         html(*self.args_mock, **self.kwargs_mock))

    def test_ok_is_html(self):
        """Test that ok is an alias for html"""
        self.assertEqual(html, ok)


class BadRequestTests(HttpResponseBehaviourTestsBase):
        def setUp(self):
            super().setUp()
            http_response_bad_request_patcher = patch(
                'uncertainty.behaviours.HttpResponseBadRequest')
            self.http_response_bad_request_mock = http_response_bad_request_patcher.start()
            self.addCleanup(http_response_bad_request_patcher.stop)

        def test_calls_http_response_behaviour(self):
            """Tests that bad_request calls HttpResponseBehaviour with HttpResponseBadRequest"""
            bad_request(*self.args_mock, **self.kwargs_mock)
            self.http_response_behaviour_mock.assert_called_once_with(
                self.http_response_bad_request_mock, *self.args_mock, **self.kwargs_mock)

        def test_returns_http_response_behaviour_result(self):
            """Tests that bad_request returns the result of calling HttpResponseBehaviour
            constructor"""
            self.assertEqual(self.http_response_behaviour_mock.return_value,
                             bad_request(*self.args_mock, **self.kwargs_mock))


class ForbiddenTests(HttpResponseBehaviourTestsBase):
    def setUp(self):
        super().setUp()
        http_response_forbidden_patcher = patch(
            'uncertainty.behaviours.HttpResponseForbidden')
        self.http_response_forbidden_mock = http_response_forbidden_patcher.start()
        self.addCleanup(http_response_forbidden_patcher.stop)

    def test_calls_http_response_behaviour(self):
        """Tests that forbidden calls HttpResponseBehaviour with HttpResponseForbidden"""
        forbidden(*self.args_mock, **self.kwargs_mock)
        self.http_response_behaviour_mock.assert_called_once_with(
            self.http_response_forbidden_mock, *self.args_mock, **self.kwargs_mock)

    def test_returns_http_response_behaviour_result(self):
        """Tests that forbidden returns the result of calling HttpResponseBehaviour constructor"""
        self.assertEqual(self.http_response_behaviour_mock.return_value,
                         forbidden(*self.args_mock, **self.kwargs_mock))


class NotAllowedTests(HttpResponseBehaviourTestsBase):
    def setUp(self):
        super().setUp()
        http_response_not_allowed_patcher = patch(
            'uncertainty.behaviours.HttpResponseNotAllowed')
        self.http_response_not_allowed_mock = http_response_not_allowed_patcher.start()
        self.addCleanup(http_response_not_allowed_patcher.stop)

    def test_calls_http_response_behaviour(self):
        """Tests that not_allowed calls HttpResponseBehaviour with HttpResponseNotAllowed"""
        not_allowed(*self.args_mock, **self.kwargs_mock)
        self.http_response_behaviour_mock.assert_called_once_with(
            self.http_response_not_allowed_mock, *self.args_mock, **self.kwargs_mock)

    def test_returns_http_response_behaviour_result(self):
        """Tests that not_allowed returns the result of calling HttpResponseBehaviour constructor"""
        self.assertEqual(self.http_response_behaviour_mock.return_value,
                         not_allowed(*self.args_mock, **self.kwargs_mock))


class ServerErrorTests(HttpResponseBehaviourTestsBase):
    def setUp(self):
        super().setUp()
        http_response_server_error_patcher = patch(
            'uncertainty.behaviours.HttpResponseServerError')
        self.http_response_server_error_mock = http_response_server_error_patcher.start()
        self.addCleanup(http_response_server_error_patcher.stop)

    def test_calls_http_response_behaviour(self):
        """Tests that server_error calls HttpResponseBehaviour with HttpResponseNotAllowed"""
        server_error(*self.args_mock, **self.kwargs_mock)
        self.http_response_behaviour_mock.assert_called_once_with(
            self.http_response_server_error_mock, *self.args_mock, **self.kwargs_mock)

    def test_returns_http_response_behaviour_result(self):
        """Tests that server_error returns the result of calling HttpResponseServerError
        constructor"""
        self.assertEqual(self.http_response_behaviour_mock.return_value,
                         server_error(*self.args_mock, **self.kwargs_mock))


class NotFoundTests(HttpResponseBehaviourTestsBase):
    def setUp(self):
        super().setUp()
        http_response_patcher = patch('uncertainty.behaviours.HttpResponse')
        self.http_response_mock = http_response_patcher.start()
        self.addCleanup(http_response_patcher.stop)

    def test_calls_http_response_behaviour(self):
        """Tests that not_found calls HttpResponseBehaviour with HttpResponse"""
        not_found(*self.args_mock, **self.kwargs_mock)
        self.http_response_behaviour_mock.assert_called_once_with(self.http_response_mock,
                                                                  status=404,
                                                                  *self.args_mock,
                                                                  **self.kwargs_mock)

    def test_returns_http_response_behaviour_result(self):
        """Tests that not_found returns the result of calling HttpResponseBehaviour constructor"""
        self.assertEqual(self.http_response_behaviour_mock.return_value,
                         not_found(*self.args_mock, **self.kwargs_mock))


# TODO Add status tests
# TODO Add json tests
# TODO Add DelayResponse tests
# TODO Add DelayRequest tests
# TODO Add RandomChoice tests
# TODO Add ConditionalBehaviour tests
# TODO Add MultiConditionalBehaviour tests
