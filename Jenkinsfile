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
        sh 'docker-compose build'
        echo 'docker-compose build finished'
        sh 'docker-compose up'
        echo 'docker-compose up finished' 
        }
}

void nodeWithTimeout(String label, def body) {
    node(label) {
        timeout(time: 500, unit: 'MINUTES') {
            body.call()
        }
    }
}