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


class TokenInfo(object):
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
        'id': 'int',
        'form': 'str',
        'kana': 'str',
        'lemma': 'str',
        'pos': 'str',
        'feature': 'list[str]',
        'dependency_labels': 'list[DepInfo]',
        'attributes': 'object'
    }

    attribute_map = {
        'id': 'id',
        'form': 'form',
        'kana': 'kana',
        'lemma': 'lemma',
        'pos': 'pos',
        'feature': 'feature',
        'dependency_labels': 'dependency_labels',
        'attributes': 'attributes'
    }

    def __init__(self, id=None, form=None, kana=None, lemma=None, pos=None, feature=None, dependency_labels=None, attributes=None):  # noqa: E501
        """TokenInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._form = None
        self._kana = None
        self._lemma = None
        self._pos = None
        self._feature = None
        self._dependency_labels = None
        self._attributes = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if form is not None:
            self.form = form
        if kana is not None:
            self.kana = kana
        if lemma is not None:
            self.lemma = lemma
        if pos is not None:
            self.pos = pos
        if feature is not None:
            self.feature = feature
        if dependency_labels is not None:
            self.dependency_labels = dependency_labels
        if attributes is not None:
            self.attributes = attributes

    @property
    def id(self):
        """Gets the id of this TokenInfo.  # noqa: E501


        :return: The id of this TokenInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TokenInfo.


        :param id: The id of this TokenInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def form(self):
        """Gets the form of this TokenInfo.  # noqa: E501


        :return: The form of this TokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._form

    @form.setter
    def form(self, form):
        """Sets the form of this TokenInfo.


        :param form: The form of this TokenInfo.  # noqa: E501
        :type: str
        """

        self._form = form

    @property
    def kana(self):
        """Gets the kana of this TokenInfo.  # noqa: E501


        :return: The kana of this TokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._kana

    @kana.setter
    def kana(self, kana):
        """Sets the kana of this TokenInfo.


        :param kana: The kana of this TokenInfo.  # noqa: E501
        :type: str
        """

        self._kana = kana

    @property
    def lemma(self):
        """Gets the lemma of this TokenInfo.  # noqa: E501


        :return: The lemma of this TokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._lemma

    @lemma.setter
    def lemma(self, lemma):
        """Sets the lemma of this TokenInfo.


        :param lemma: The lemma of this TokenInfo.  # noqa: E501
        :type: str
        """

        self._lemma = lemma

    @property
    def pos(self):
        """Gets the pos of this TokenInfo.  # noqa: E501


        :return: The pos of this TokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._pos

    @pos.setter
    def pos(self, pos):
        """Sets the pos of this TokenInfo.


        :param pos: The pos of this TokenInfo.  # noqa: E501
        :type: str
        """

        self._pos = pos

    @property
    def feature(self):
        """Gets the feature of this TokenInfo.  # noqa: E501


        :return: The feature of this TokenInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this TokenInfo.


        :param feature: The feature of this TokenInfo.  # noqa: E501
        :type: list[str]
        """

        self._feature = feature

    @property
    def dependency_labels(self):
        """Gets the dependency_labels of this TokenInfo.  # noqa: E501


        :return: The dependency_labels of this TokenInfo.  # noqa: E501
        :rtype: list[DepInfo]
        """
        return self._dependency_labels

    @dependency_labels.setter
    def dependency_labels(self, dependency_labels):
        """Sets the dependency_labels of this TokenInfo.


        :param dependency_labels: The dependency_labels of this TokenInfo.  # noqa: E501
        :type: list[DepInfo]
        """

        self._dependency_labels = dependency_labels

    @property
    def attributes(self):
        """Gets the attributes of this TokenInfo.  # noqa: E501


        :return: The attributes of this TokenInfo.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this TokenInfo.


        :param attributes: The attributes of this TokenInfo.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

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
        if issubclass(TokenInfo, dict):
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
        if not isinstance(other, TokenInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other