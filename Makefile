.PHONY: build

build: 
	sam build

deploy-infra:
	sam build && aws-vault exec shivamagrawal --no-session -- sam deploy

deploy-site:
	aws-vault exec shivamagrawal --no-session -- aws s3 sync ./shivam-resume-site s3://shivam-resume-website

invoke-put:
	sam build && aws-vault exec shivamagrawal --no-session -- sam local invoke PutFunction