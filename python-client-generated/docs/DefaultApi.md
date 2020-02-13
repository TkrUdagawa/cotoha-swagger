# swagger_client.DefaultApi

All URIs are relative to *https://api.ce-cotoha.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_dev_nlp_beta_detect_misrecognition_post**](DefaultApi.md#api_dev_nlp_beta_detect_misrecognition_post) | **POST** /api/dev/nlp/beta/detect_misrecognition | 
[**api_dev_nlp_beta_remove_filler_post**](DefaultApi.md#api_dev_nlp_beta_remove_filler_post) | **POST** /api/dev/nlp/beta/remove_filler | 
[**api_dev_nlp_beta_user_attribute_post**](DefaultApi.md#api_dev_nlp_beta_user_attribute_post) | **POST** /api/dev/nlp/beta/user_attribute | 
[**api_dev_nlp_v1_coreference_post**](DefaultApi.md#api_dev_nlp_v1_coreference_post) | **POST** /api/dev/nlp/v1/coreference | 
[**api_dev_nlp_v1_keyword_post**](DefaultApi.md#api_dev_nlp_v1_keyword_post) | **POST** /api/dev/nlp/v1/keyword | 
[**api_dev_nlp_v1_ne_post**](DefaultApi.md#api_dev_nlp_v1_ne_post) | **POST** /api/dev/nlp/v1/ne | 
[**api_dev_nlp_v1_parse_post**](DefaultApi.md#api_dev_nlp_v1_parse_post) | **POST** /api/dev/nlp/v1/parse | 
[**api_dev_nlp_v1_sentence_type_post**](DefaultApi.md#api_dev_nlp_v1_sentence_type_post) | **POST** /api/dev/nlp/v1/sentence_type | 
[**api_dev_nlp_v1_sentiment_post**](DefaultApi.md#api_dev_nlp_v1_sentiment_post) | **POST** /api/dev/nlp/v1/sentiment | 
[**api_dev_nlp_v1_similarity_post**](DefaultApi.md#api_dev_nlp_v1_similarity_post) | **POST** /api/dev/nlp/v1/similarity | 
[**v1_oauth_accesstokens_post**](DefaultApi.md#v1_oauth_accesstokens_post) | **POST** /v1/oauth/accesstokens | 

# **api_dev_nlp_beta_detect_misrecognition_post**
> DetectMisrecognitionResult api_dev_nlp_beta_detect_misrecognition_post(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.DetectMisrecognition() # DetectMisrecognition | 

try:
    api_response = api_instance.api_dev_nlp_beta_detect_misrecognition_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_dev_nlp_beta_detect_misrecognition_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DetectMisrecognition**](DetectMisrecognition.md)|  | 

### Return type

[**DetectMisrecognitionResult**](DetectMisrecognitionResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_dev_nlp_beta_remove_filler_post**
> RemoveFillerResult api_dev_nlp_beta_remove_filler_post(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.RemoveFiller() # RemoveFiller | 

try:
    api_response = api_instance.api_dev_nlp_beta_remove_filler_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_dev_nlp_beta_remove_filler_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoveFiller**](RemoveFiller.md)|  | 

### Return type

[**RemoveFillerResult**](RemoveFillerResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_dev_nlp_beta_user_attribute_post**
> UserAttributeResult api_dev_nlp_beta_user_attribute_post(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserAttribute() # UserAttribute | 

try:
    api_response = api_instance.api_dev_nlp_beta_user_attribute_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_dev_nlp_beta_user_attribute_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAttribute**](UserAttribute.md)|  | 

### Return type

[**UserAttributeResult**](UserAttributeResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_dev_nlp_v1_coreference_post**
> CoreferenceResult api_dev_nlp_v1_coreference_post(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Coreference() # Coreference | 

try:
    api_response = api_instance.api_dev_nlp_v1_coreference_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_dev_nlp_v1_coreference_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Coreference**](Coreference.md)|  | 

### Return type

[**CoreferenceResult**](CoreferenceResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_dev_nlp_v1_keyword_post**
> KeywordResult api_dev_nlp_v1_keyword_post(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Keyword() # Keyword | 

try:
    api_response = api_instance.api_dev_nlp_v1_keyword_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_dev_nlp_v1_keyword_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Keyword**](Keyword.md)|  | 

### Return type

[**KeywordResult**](KeywordResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_dev_nlp_v1_ne_post**
> NeResult api_dev_nlp_v1_ne_post(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Ne() # Ne | 

try:
    api_response = api_instance.api_dev_nlp_v1_ne_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_dev_nlp_v1_ne_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ne**](Ne.md)|  | 

### Return type

[**NeResult**](NeResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_dev_nlp_v1_parse_post**
> ParseResult api_dev_nlp_v1_parse_post(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Parse() # Parse | 

try:
    api_response = api_instance.api_dev_nlp_v1_parse_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_dev_nlp_v1_parse_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Parse**](Parse.md)|  | 

### Return type

[**ParseResult**](ParseResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_dev_nlp_v1_sentence_type_post**
> SentenceTypeResult api_dev_nlp_v1_sentence_type_post(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.SentenceType() # SentenceType | 

try:
    api_response = api_instance.api_dev_nlp_v1_sentence_type_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_dev_nlp_v1_sentence_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SentenceType**](SentenceType.md)|  | 

### Return type

[**SentenceTypeResult**](SentenceTypeResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_dev_nlp_v1_sentiment_post**
> SentimentResult api_dev_nlp_v1_sentiment_post(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Sentiment() # Sentiment | 

try:
    api_response = api_instance.api_dev_nlp_v1_sentiment_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_dev_nlp_v1_sentiment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Sentiment**](Sentiment.md)|  | 

### Return type

[**SentimentResult**](SentimentResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_dev_nlp_v1_similarity_post**
> SimilarityResult api_dev_nlp_v1_similarity_post(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Similarity() # Similarity | 

try:
    api_response = api_instance.api_dev_nlp_v1_similarity_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_dev_nlp_v1_similarity_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Similarity**](Similarity.md)|  | 

### Return type

[**SimilarityResult**](SimilarityResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_oauth_accesstokens_post**
> AuthResult v1_oauth_accesstokens_post(body)



issue access token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Auth() # Auth | specify your clientID and clientSecret

try:
    api_response = api_instance.v1_oauth_accesstokens_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_oauth_accesstokens_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Auth**](Auth.md)| specify your clientID and clientSecret | 

### Return type

[**AuthResult**](AuthResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

