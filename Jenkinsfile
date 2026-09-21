pipeline {
    agent any

    environment {
        DOCKER_USER = 'niranjanhulamudde'
        DOCKER_IMAGE = 'flask-app'
        IMAGE_TAG = 'latest'
    }
    stages {
        stage('Code checking') {
            steps {
                checkout scm
            }
        }
        stage('Building the image') {
            steps {
                sh 'docker build -t ${Docker_IMAGE}:${IMAGE_TAG} .' 
            }
        }
     post {
        success {
                echo "deployed successfully"
            }
        failure {
                echo "failed  to deploy"
            }
        }
    }
}
