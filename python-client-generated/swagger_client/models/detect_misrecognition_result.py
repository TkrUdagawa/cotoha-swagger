# coding: utf-8

"""
    COTOHA API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class DetectMisrecognitionResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'result': 'list[DetectMisrecognitionInfo]',
        'status': 'int',
        'message': 'str'
    }

    attribute_map = {
        'result': 'result',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, result=None, status=None, message=None):  # noqa: E501
        """DetectMisrecognitionResult - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self._status = None
        self._message = None
        self.discriminator = None
        if result is not None:
            self.result = result
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def result(self):
        """Gets the result of this DetectMisrecognitionResult.  # noqa: E501


        :return: The result of this DetectMisrecognitionResult.  # noqa: E501
        :rtype: list[DetectMisrecognitionInfo]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DetectMisrecognitionResult.


        :param result: The result of this DetectMisrecognitionResult.  # noqa: E501
        :type: list[DetectMisrecognitionInfo]
        """

        self._result = result

    @property
    def status(self):
        """Gets the status of this DetectMisrecognitionResult.  # noqa: E501


        :return: The status of this DetectMisrecognitionResult.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DetectMisrecognitionResult.


        :param status: The status of this DetectMisrecognitionResult.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this DetectMisrecognitionResult.  # noqa: E501


        :return: The message of this DetectMisrecognitionResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DetectMisrecognitionResult.


        :param message: The message of this DetectMisrecognitionResult.  # noqa: E501
        :type: str
        """

        self._message = message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DetectMisrecognitionResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DetectMisrecognitionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
