pipeline {
  agent any
  stages {
    stage('Docker Build') {
      steps {
        sh 'docker-compose build'
      }
    }
    stage('Docker Run') {
      steps {
        sh 'docker-compose up -d'
      }
    }
    stage('Docker stop') {
      steps {
        sh 'docker-compose stop'
      }
    }
  }
}