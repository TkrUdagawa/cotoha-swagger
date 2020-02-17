# coding: utf-8

# flake8: noqa

"""
    COTOHA API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.default_api import DefaultApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.auth import Auth
from swagger_client.models.auth_result import AuthResult
from swagger_client.models.chunk_info import ChunkInfo
from swagger_client.models.coreference import Coreference
from swagger_client.models.coreference_info import CoreferenceInfo
from swagger_client.models.coreference_result import CoreferenceResult
from swagger_client.models.coreference_result_result import CoreferenceResultResult
from swagger_client.models.dep_info import DepInfo
from swagger_client.models.detect_misrecognition import DetectMisrecognition
from swagger_client.models.detect_misrecognition_candidates import DetectMisrecognitionCandidates
from swagger_client.models.detect_misrecognition_candidates_correction import DetectMisrecognitionCandidatesCorrection
from swagger_client.models.detect_misrecognition_result import DetectMisrecognitionResult
from swagger_client.models.detect_misrecognition_result_result import DetectMisrecognitionResultResult
from swagger_client.models.dialog_act import DialogAct
from swagger_client.models.keyword import Keyword
from swagger_client.models.keyword_info import KeywordInfo
from swagger_client.models.keyword_result import KeywordResult
from swagger_client.models.link_info import LinkInfo
from swagger_client.models.modality import Modality
from swagger_client.models.ne import Ne
from swagger_client.models.ne_info import NeInfo
from swagger_client.models.ne_result import NeResult
from swagger_client.models.parse import Parse
from swagger_client.models.parse_info import ParseInfo
from swagger_client.models.parse_result import ParseResult
from swagger_client.models.referent import Referent
from swagger_client.models.remove_filler import RemoveFiller
from swagger_client.models.remove_filler_info import RemoveFillerInfo
from swagger_client.models.remove_filler_info_fillers import RemoveFillerInfoFillers
from swagger_client.models.remove_filler_result import RemoveFillerResult
from swagger_client.models.sentence_type import SentenceType
from swagger_client.models.sentence_type_result import SentenceTypeResult
from swagger_client.models.sentence_type_result_result import SentenceTypeResultResult
from swagger_client.models.sentiment import Sentiment
from swagger_client.models.sentiment_result import SentimentResult
from swagger_client.models.sentiment_result_result import SentimentResultResult
from swagger_client.models.sentiment_result_result_emotional_phrase import SentimentResultResultEmotionalPhrase
from swagger_client.models.similarity import Similarity
from swagger_client.models.similarity_result import SimilarityResult
from swagger_client.models.similarity_result_result import SimilarityResultResult
from swagger_client.models.summary import Summary
from swagger_client.models.summary_result import SummaryResult
from swagger_client.models.token_info import TokenInfo
from swagger_client.models.user_attribute import UserAttribute
from swagger_client.models.user_attribute_info import UserAttributeInfo
from swagger_client.models.user_attribute_result import UserAttributeResult
