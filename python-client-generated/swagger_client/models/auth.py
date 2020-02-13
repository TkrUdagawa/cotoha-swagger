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


class Auth(object):
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
        'client_id': 'str',
        'client_secret': 'str',
        'grant_type': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'client_secret': 'clientSecret',
        'grant_type': 'grantType'
    }

    def __init__(self, client_id=None, client_secret=None, grant_type='client_credentials'):  # noqa: E501
        """Auth - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._client_secret = None
        self._grant_type = None
        self.discriminator = None
        self.client_id = client_id
        self.client_secret = client_secret
        if grant_type is not None:
            self.grant_type = grant_type

    @property
    def client_id(self):
        """Gets the client_id of this Auth.  # noqa: E501


        :return: The client_id of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Auth.


        :param client_id: The client_id of this Auth.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this Auth.  # noqa: E501


        :return: The client_secret of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this Auth.


        :param client_secret: The client_secret of this Auth.  # noqa: E501
        :type: str
        """
        if client_secret is None:
            raise ValueError("Invalid value for `client_secret`, must not be `None`")  # noqa: E501

        self._client_secret = client_secret

    @property
    def grant_type(self):
        """Gets the grant_type of this Auth.  # noqa: E501


        :return: The grant_type of this Auth.  # noqa: E501
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this Auth.


        :param grant_type: The grant_type of this Auth.  # noqa: E501
        :type: str
        """

        self._grant_type = grant_type

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
        if issubclass(Auth, dict):
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
        if not isinstance(other, Auth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other