create docker image: `docker build -t philippweinmann/locust_testing:NEW_TAG .`
run docker image: `docker run -p 8089:8089 philippweinmann/locust_testing:TAG`
upload docker image to docker hub: `docker push philippweinmann/locust_testing:tagname`

Upload to AWS Lightsail (#todo move to hivebuy's AWS Elastic Beanstalk):
`aws lightsail push-container-image    \
    --region eu-central-1             \
    --service-name locust-test \
    --label [NEWLABEL]                    \
    --image philippweinmann/locust_testing:[TAG]`

Don't forget to set environment Variables in AWS