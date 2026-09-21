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
    }

    post {
        success {
            echo "built successfully"
        }
        failure {
            echo "failed to build"
        }
    }
}
