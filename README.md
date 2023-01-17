# Azure Custom Vision Annotated Images to Yolo Format
A step by step walkthrough to convert all the annotated images from Azure Custom Vision servcice to an exported Yolo compatible format to train a variety of yolo models directly.

P.S: By default, we are allowed to import our custom training images into Azure Custom Vision and can annotate those images with labels. From there directly there is a feature for training models based on these annotations. However, it is not an easy task to obtain those images from the service directly, and this would require some manipulation.

Can we export the images with their annotations from CustomVision: Yes, but it's not very clean and requires some processing for the same.
The API has a GET method we need to call either directly or with optional parameters.

## Direct Method:
```
GET {Endpoint}/customvision/v3.3/training/projects/{projectId}/images/tagged
```
With Optional Parameters:
```
GET {Endpoint}/customvision/v3.3/training/projects/{projectId}/images/tagged?iterationId={iterationId}&tagIds={tagIds}&orderBy={orderBy}&take={take}&skip={skip}
```

## The parameters within the POST option are:
![image](https://user-images.githubusercontent.com/65887524/212827506-5998027d-e9df-4a06-869e-ea5be833dcbb.png)

A sampple POST request that we would need for this would follow this style and syntax.
```
GET https://westus.api.cognitive.microsoft.com/customvision/v3.3/training/projects/bc3f7dad-5544-468c-8573-3ef04d55463e/images/tagged?iterationId=cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12
```

## This documentation is pretty important, you can use this directly for the POST request as well:
https://learn.microsoft.com/en-us/rest/api/customvision/training3.3/get-tagged-images/get-tagged-images?tabs=HTTP&tryIt=true&source=docs#code-try-0

We open the URL mentioned above and fill in the required data:
```
Endpoint: https://customvisionfiredetectionv1.cognitiveservices.azure.com/
ProjectID: b325643b-2b0c-4d3f-a0b3-2084c70cd2e4
Training-Key: b8e5dcf7cc7443e2b3d95c32470ce4d6
```

This provides us with the following translation in terms of an HTTP Request:
![image](https://user-images.githubusercontent.com/65887524/212828128-6bf5cfcd-9fc4-43f5-a435-3bb1025ad9a4.png)

We can now use this data in Postman to call a GET Request to the CustomVision API and obtain all the image annotations [By default the API will only return 50 tagged images of the mentioned tags, need to manually change parameters for this].

## Using POSTMAN
```
Params: Key: Training-key, Value: {Training-key}
Authorization: Type: Bearer Token, Token: {The long text obtained from the HTTP request on the second line}
GET https://customvisionfiredetectionv1.cognitiveservices.azure.com//customvision/v3.3/training/projects/b325643b-2b0c-4d3f-a0b3-2084c70cd2e4/images/tagged?Training-key=b8e5dcf7cc7443e2b3d95c32470ce4d6
{Bascially the GET Request from the top line}
```

## Output
We obtain a JSON compatible output which returns the image via URL which is in the .file format. We also obtain for each image, the bounding box locations for each of the requested tags.
![image](https://user-images.githubusercontent.com/65887524/212828524-f1ad31bc-45a0-4957-a6e2-98a48d849d2b.png)

We can then directly use this in Python for calling GET Requests
```
import requests

url = "{Endpoint}/customvision/v3.3/training/projects/{Project-ID}/images/tagged?Training-key={Training-Key}"

payload={}
headers = {
  'Authorization': 'Bearer {Bearer Token}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```
