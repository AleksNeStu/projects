### Sub tree projects

[cloud/aws/cloudformation/001_aws_cloudformation_templates/subtree](cloud/aws/cloudformation/001_aws_cloudformation_templates/subtree)

[cloud/gcp/samples/001_python_docs_samples/subtree](cloud/gcp/samples/001_python_docs_samples/subtree)

[code/templates/001_fastapi_best_practices/subtree](code/templates/001_fastapi_best_practices/subtree)

[code/templates/002_full_stack_fastapi_postgresql/subtree](code/templates/002_full_stack_fastapi_postgresql/subtree)

[ml/ai/001_fastapi_ai_lib/subtree](ml/ai/001_fastapi_ai_lib/subtree)

[ml/ai/002_fastapi_ai_txt_to_image/subtree](ml/ai/002_fastapi_ai_txt_to_image/subtree)


### Example how to add / del subtree
```
git subtree add --prefix=cloud/gcp/samples/001_python_docs_samples/subtree https://github.com/GoogleCloudPlatform/python-docs-samples.git main

git rm -r --cached cloud/azure/samples/001_python_docs_samples/subtree
git clean -df
rm -rf cloud/azure/samples/001_python_docs_samples/subtree
```