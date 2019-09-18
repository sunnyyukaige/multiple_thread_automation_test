#!/usr/bin/env groovy

properties([
    buildDiscarder(logRotator(numToKeepStr: '50', artifactNumToKeepStr: '5')),
    pipelineTriggers([cron('H H/6 * * *')]),
])

nodeWithTimeout('master') {
    deleteDir()

    stage('Checkout') {
        checkout scm
    }
  
    stage('Publish') {
            infra.withDockerCredentials {
                sh 'docker-compose build'
                sh 'docker-compose up'
            }
        }
}

void nodeWithTimeout(String label, def body) {
    node(label) {
        timeout(time: 40, unit: 'MINUTES') {
            body.call()
        }
    }
}