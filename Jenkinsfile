pipeline {
    agent any

    environment {
        DOCKER_USER  = 'niranjanhulamudde'
        DOCKER_IMAGE = 'flask-app'
        IMAGE_TAG    = 'latest'
    }

    stages {
        stage('Code checking') {
            steps {
                checkout scm
            }
        }
        
        stage('Building the image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ." 
            }
        }
        stage('Pushing the image to dockerhub') {
            steps {
                withCredentials([(usernamePassord(credentialsId: 'docker-pass',
                                                  usernameVariable: '$DOCKER_USER',
                                                  usernamePassword: '$DOCKER_PASS'  ))])  {
                sh 'docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}'
                sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ." 
                sh docker push ${DOCKER_IMAGE}
                }
        }
        
    }

    post {
        success {
            echo "Image uploaded successfully"
        }
        failure {
            echo "failed to uploade Image"
        }
    }
}
}

    
