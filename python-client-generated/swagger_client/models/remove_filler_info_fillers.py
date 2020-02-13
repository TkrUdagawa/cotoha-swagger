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


class RemoveFillerInfoFillers(object):
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
        'begin_pos': 'int',
        'end_pos': 'int',
        'fomr': 'str'
    }

    attribute_map = {
        'begin_pos': 'begin_pos',
        'end_pos': 'end_pos',
        'fomr': 'fomr'
    }

    def __init__(self, begin_pos=None, end_pos=None, fomr=None):  # noqa: E501
        """RemoveFillerInfoFillers - a model defined in Swagger"""  # noqa: E501
        self._begin_pos = None
        self._end_pos = None
        self._fomr = None
        self.discriminator = None
        if begin_pos is not None:
            self.begin_pos = begin_pos
        if end_pos is not None:
            self.end_pos = end_pos
        if fomr is not None:
            self.fomr = fomr

    @property
    def begin_pos(self):
        """Gets the begin_pos of this RemoveFillerInfoFillers.  # noqa: E501


        :return: The begin_pos of this RemoveFillerInfoFillers.  # noqa: E501
        :rtype: int
        """
        return self._begin_pos

    @begin_pos.setter
    def begin_pos(self, begin_pos):
        """Sets the begin_pos of this RemoveFillerInfoFillers.


        :param begin_pos: The begin_pos of this RemoveFillerInfoFillers.  # noqa: E501
        :type: int
        """

        self._begin_pos = begin_pos

    @property
    def end_pos(self):
        """Gets the end_pos of this RemoveFillerInfoFillers.  # noqa: E501


        :return: The end_pos of this RemoveFillerInfoFillers.  # noqa: E501
        :rtype: int
        """
        return self._end_pos

    @end_pos.setter
    def end_pos(self, end_pos):
        """Sets the end_pos of this RemoveFillerInfoFillers.


        :param end_pos: The end_pos of this RemoveFillerInfoFillers.  # noqa: E501
        :type: int
        """

        self._end_pos = end_pos

    @property
    def fomr(self):
        """Gets the fomr of this RemoveFillerInfoFillers.  # noqa: E501


        :return: The fomr of this RemoveFillerInfoFillers.  # noqa: E501
        :rtype: str
        """
        return self._fomr

    @fomr.setter
    def fomr(self, fomr):
        """Sets the fomr of this RemoveFillerInfoFillers.


        :param fomr: The fomr of this RemoveFillerInfoFillers.  # noqa: E501
        :type: str
        """

        self._fomr = fomr

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
        if issubclass(RemoveFillerInfoFillers, dict):
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
        if not isinstance(other, RemoveFillerInfoFillers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
